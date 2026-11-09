#!/usr/bin/env python3
"""Run an error scenario with the institutional agents and write a hash-chained audit log.

The orchestrator releases each event of scenarios/<id>.yaml on its simulated day, only to the agents
listed in `to`. Each agent:
  1. sees only the events routed to it so far, plus the assessments other agents posted to the shared
     board about those events (information is incomplete and arrives at different times);
  2. searches the knowledge base, limited to the folders in its mandate (agents/agents.yaml) plus the
     curated clauses, figures and gaps;
  3. asks the LLM (Ollama, the ITU code's own client) for a structured assessment: reasoning steps,
     policy references, recommendation, confidence, whether a human must review;
  4. passes a policy gate (the P node): a fixed keyword check plus a separate LLM check of the
     recommendation against the scenario's pre-agreed rules. A recommendation that may break a rule is
     held for human review and NOT posted to the board, so other agents cannot copy it;
  5. posts the assessment to the board; agents it names in `notify_agents` receive the post even if
     they have not seen that event.
Before the story agent answers, the pipeline's fixed (non-LLM) tools run on the scenario's sample data and
their output is given to the agent and logged: the household register and bias check (M node: a claim
backed only by appointed representatives that contradicts household and elder accounts is flagged) and
the permitted-use filter (P node: which records may be released for the requested purpose and area).
Agents see board posts only from earlier events, not from the event they are assessing, so each
forms its own view first (avoids herding).
Every step is written to results/scenarios/<id>/audit_log.jsonl (one entry per agent step, schema
audit/audit_entry.schema.json, each entry hash-chained to the previous one), and a readable transcript
to transcript.md. Nothing is approved automatically: every entry starts with human review "pending".

Usage (from the repository root, after the knowledge base is built):
    python scripts/run_scenario.py --itu-dir ../ITUAIReadiness --scenario mining_renewal
    python scripts/run_scenario.py --itu-dir ../ITUAIReadiness --scenario all --model qwen2.5:7b

Code check without Ollama: --embed offline --llm offline (retrieval-only stand-in, no reasoning).
Verify a log afterwards: python scripts/verify_audit.py results/scenarios/<id>/audit_log.jsonl
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import itu_env  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "results" / "scenarios"

SYSTEM = """You are {name}, an AI agent playing the role of: {role}, in a Philippine policy simulation.
Your mandate: {mandate}
Pre-agreed rules for this scenario:
{rules}
Work only from the evidence passages given to you and the events you have received. Cite each legal
provision exactly as it appears in the evidence (for example "IPRA s59"). Binding Philippine law is a
requirement; declarations, guidance and foreign examples are benchmarks only - label them so. If the
evidence does not settle a point, say so and send it to human review. Never approve or reject anything
on your own: you recommend, a human decides. If an event asks for something a pre-agreed rule
forbids, say no, name the rule, and propose what can be done instead. Stay within your mandate; name the agency that should act
when it is not you.
Answer with JSON only, using exactly these keys:
{{"reasoning_steps": [short strings, 3 to 6], "policy_references": [strings],
  "recommendation": string, "confidence": "low" | "medium" | "high",
  "needs_human_review": true | false, "notify_agents": [agent names from: {agents}],
  "gaps_or_conflicts": [strings]}}"""

PROMPT = """Simulated day {day}. New event for you ({eid}):
{event}

Events you have received so far:
{seen}

Assessments other agents posted about those events, or sent to you:
{board}

Pipeline tool results (fixed rules, not AI; rely on them):
{tools}

Evidence from the knowledge base (cite by the bracketed source id):
{evidence}

Give your assessment as JSON."""


GATE_SYSTEM = """You are the policy gate of an AI pipeline. You check one agent recommendation against
numbered pre-agreed rules. A rule is broken only if following the recommendation would do what the rule
forbids (for example share more than the permitted use allows, or renew/approve without the required
consent or certification). Mentioning a rule, or refusing, does not break it.
Answer JSON only: {"broken_rules": [rule numbers], "explanation": string}"""


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def entry_hash(entry: dict) -> str:
    body = {k: v for k, v in entry.items() if k != "entry_hash"}
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def retrieve(kb, embed, query: str, folders: list[str], k_general: int = 5, k_curated: int = 3):
    """Curated clauses first, then passages from the agent's folders. Returns list of dicts."""
    q = embed([query])[0]
    out, seen = [], set()
    passes = [(k_curated, {"document_category": "Curated"})]
    docs = [f for f in folders if f != "Curated"]
    if docs:
        passes.append((k_general, {"document_category": {"$in": docs}} if len(docs) > 1 else {"document_category": docs[0]}))
    for n, where in passes:
        r = kb.search(q, n_results=n, where=where)
        for cid, text, meta, dist in zip(r["ids"][0], r["documents"][0], r["metadatas"][0], r["distances"][0]):
            if cid in seen:
                continue
            seen.add(cid)
            out.append({"chunk_id": cid, "source_id": meta.get("source_id", ""), "cite": meta.get("cite", ""),
                        "title": meta.get("title", ""), "section": meta.get("sections", ""),
                        "distance": round(float(dist), 4), "text": text})
    return out


def fmt_evidence(ev: list[dict]) -> str:
    lines = []
    for e in ev:
        label = e["cite"] or e["title"] or e["source_id"]
        lines.append(f"[{e['source_id']}] {label}: {e['text'][:900]}")
    return "\n\n".join(lines)


def call_llm(client, model: str, system: str, prompt: str) -> dict:
    r = client.chat(model=model, format="json", options={"temperature": 0, "num_ctx": 8192},
                    messages=[{"role": "system", "content": system}, {"role": "user", "content": prompt}])
    text = r["message"]["content"]
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.S)
        return json.loads(m.group(0)) if m else {"reasoning_steps": [text[:500]], "recommendation": "", "parse_error": True}


def policy_gate(client, model: str, rules: list[str], checks: list[dict], rec: str) -> dict:
    """Keyword triggers from the scenario file plus an LLM check of the recommendation."""
    def fires(trigger: str) -> bool:  # a match counts unless negated just before it ("should not be ...")
        return any(not re.search(r"\b(not|never|no|without|before|until|unless|cannot|can't)\b", rec[max(0, m.start() - 25):m.start()], re.I)
                   for m in re.finditer(trigger, rec, re.I))
    flags = [c["id"] for c in checks if fires(c["trigger"])]
    broken, expl = [], ""
    if client:
        numbered = "\n".join(f"{i}. {r}" for i, r in enumerate(rules, 1))
        try:
            g = call_llm(client, model, GATE_SYSTEM, f"Rules:\n{numbered}\n\nRecommendation:\n{rec}\n\nJSON:")
            broken = sorted({int(x) for x in g.get("broken_rules", []) if str(x).isdigit() and 1 <= int(x) <= len(rules)})
            expl = str(g.get("explanation", ""))
        except Exception as e:  # noqa: BLE001
            expl = f"gate check failed: {e}"
    held = bool(flags or broken)
    return {"keyword_flags": flags, "broken_rules": [f"{i}. {rules[i - 1]}" for i in broken],
            "explanation": expl, "result": "held for human review" if held else "passed"}


def tool_household_register(accounts: list[dict]) -> dict:
    """Register of recorded accounts and a bias check on each claim (M node)."""
    roles = {}
    for a in accounts:
        roles[a["role"]] = roles.get(a["role"], 0) + 1
    claims: dict[str, dict] = {}
    for a in accounts:
        c = claims.setdefault(a["consent"], {"tellers": [], "roles": set()})
        c["tellers"].append(a["id"]); c["roles"].add(a["role"])
    flags = []
    for claim, c in claims.items():
        if c["roles"] <= {"appointed_representative"} and len(claims) > 1:
            others = sum(len(v["tellers"]) for k, v in claims.items() if k != claim)
            flags.append(f"BIAS FLAG: the claim '{claim}' is supported only by appointed representatives "
                         f"({', '.join(c['tellers'])}) and contradicts {others} household and elder accounts. "
                         "Send to human review with the community; do not change the record.")
    inside = sum(1 for a in accounts if a.get("mine_inside_domain"))
    out = (f"Household register: {len(accounts)} accounts recorded separately "
           f"({', '.join(f'{n} {r}' for r, n in sorted(roles.items()))}). "
           f"{inside} of {len(accounts)} place the mine inside the ancestral domain. "
           + "Claims on consent: " + "; ".join(f"'{k}': {len(v['tellers'])}" for k, v in claims.items()) + ". "
           + (" ".join(flags) if flags else "No claim rests only on representatives."))
    return {"tool": "household_register_and_bias_check", "node": "M", "output": out, "flags": flags}


def tool_permitted_use(records: list[dict], req: dict) -> dict:
    """Which community records may leave the private store for this request (P node)."""
    ok, no_use, out_area, tapu = [], [], [], []
    for r in records:
        if r["area"] not in req["area"]:
            out_area.append(r["id"])
        elif req["purpose"] not in r["permitted_use"]:
            no_use.append(r["id"])
        else:
            ok.append(r["id"])
            if r.get("tapu_parts"):
                tapu.append(r["id"])
    asked = "the full archive" if req.get("scope") == "full_archive" else "matching records"
    out = (f"Request: {asked} for purpose '{req['purpose']}' in area(s) {', '.join(req['area'])}. "
           f"Archive holds {len(records)} records. Authorised extract: {', '.join(ok) or 'none'} ({len(ok)} records"
           + (f"; controlled (tapu) parts removed from {', '.join(tapu)}" if tapu else "") + "). "
           f"Not permitted for this purpose: {', '.join(no_use) or 'none'}. Outside the requested area: {', '.join(out_area) or 'none'}. "
           + (f"Releasing the full archive would release {len(records) - len(ok)} records without permission; "
              "that needs a new community decision (FPIC)." if req.get("scope") == "full_archive" else
              "Only the authorised extract may be shared, with context and original language kept."))
    return {"tool": "permitted_use_filter", "node": "P", "output": out, "authorised": ok, "excluded": no_use + out_area}


def run_tools(sc: dict, ev: dict, name: str, register: list[dict]) -> list[dict]:
    if name != "story_agent":
        return []
    res = []
    if ev.get("record_accounts") or ev.get("new_accounts"):
        res.append(tool_household_register(register))
    if ev.get("request") and sc.get("records"):
        res.append(tool_permitted_use(sc["records"], ev["request"]))
    return res


def offline_llm(ev: list[dict], event: dict) -> dict:
    """Stand-in with no model: lists the retrieved sources. For checking the code paths only."""
    refs = [e["cite"] or e["source_id"] for e in ev]
    return {"reasoning_steps": ["(offline stand-in) retrieved evidence: " + ", ".join(refs)],
            "policy_references": refs, "recommendation": "(offline stand-in; run with --llm ollama for a real assessment)",
            "confidence": "low", "needs_human_review": True, "notify_agents": [], "gaps_or_conflicts": []}


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower().replace("section", "s").replace("sec.", "s"))


ALIASES = {"ipra": ["ipra", "ra8371", "republicact8371", "indigenouspeoplesrightsact"],
           "miningact": ["miningact", "ra7942", "republicact7942"],
           "ra10121": ["ra10121", "republicact10121", "drrmact", "disasterriskreductionandmanagementact"]}


def ref_hits(expected: list[str], text: str) -> list[str]:
    """Keyword check: an expected reference counts as cited if the text names it (or its law number)
    together with the section or article number. A rough indicator for the summary, not a grade."""
    t = norm(text)
    hits = []
    for r in expected:
        m = re.match(r"(.+?)\s+(?:s|art\.?\s*)(\d+[a-z0-9()]*)$", r, re.I)
        if not m:
            if norm(r) in t:
                hits.append(r)
            continue
        name, num = norm(m.group(1)), norm(m.group(2))
        names = ALIASES.get(name, [name])
        nums = [f"s{num}", f"section{num}", f"sec{num}", f"art{num}", f"article{num}"]
        if any(n in t for n in names) and any(x in t for x in nums):
            hits.append(r)
    return hits


def run(scenario_id: str, args, kb, embed, agents_cfg: dict) -> dict:
    sc = yaml.safe_load((ROOT / "scenarios" / f"{scenario_id}.yaml").read_text(encoding="utf-8"))
    agents = agents_cfg["agents"]
    out = OUT / scenario_id
    out.mkdir(parents=True, exist_ok=True)
    log_path, md_path = out / "audit_log.jsonl", out / "transcript.md"
    client = None
    if args.llm == "ollama":
        import ollama
        client = ollama.Client(host=args.ollama_url)

    rule_list = sc.get("pre_agreed_rules", [])
    rules = "\n".join(f"- {r}" for r in rule_list)
    checks = sc.get("gate_checks", [])
    received: dict[str, list[dict]] = {a: [] for a in agents}
    register: list[dict] = []
    board: list[dict] = []
    prev, step, entries = "GENESIS", 0, []
    md = [f"# Scenario: {sc['title']}", "", f"Use case {sc.get('use_case', '')}. Model: `{args.model if client else 'offline stand-in'}`. "
          f"Run {now()}. Every entry below is in `audit_log.jsonl` with its hash.", "", "## Pre-agreed rules", "", rules, ""]
    scores = []

    for ev in sorted(sc["events"], key=lambda e: e["day"]):
        md += [f"## Day {ev['day']} - {ev['id']}", "", f"> {ev['event']}", "", f"Released to: {', '.join(ev['to'])}", ""]
        hits_all: set[str] = set()
        if ev.get("record_accounts"):
            register.extend(sc.get("accounts", []))
        register.extend(ev.get("new_accounts", []))
        for name in ev["to"]:
            a = agents[name]
            received[name].append(ev)
            seen_ids = {e["id"] for e in received[name]}
            seen_txt = "\n".join(f"- day {e['day']} {e['id']}: {e['event']}" for e in received[name])
            # earlier events this agent knows of, plus anything sent to it (even about this event)
            posts = [b for b in board if b["agent"] != name
                     and ((b["event_id"] in seen_ids and b["event_id"] != ev["id"]) or name in b.get("notify", []))]
            board_txt = "\n".join(f"- {b['agent']} on {b['event_id']}{' (sent to you)' if name in b.get('notify', []) else ''}: "
                                  f"{b['recommendation']}" for b in posts[-8:]) or "(none)"
            tools = run_tools(sc, ev, name, register)
            tools_txt = "\n".join(f"- [{t['tool']}] {t['output']}" for t in tools) or "(none for your role)"
            evidence = retrieve(kb, embed, f"{a['role']}. {ev['event']}", a.get("kb_folders", []))
            system = SYSTEM.format(name=name, role=a["role"], mandate=a["mandate"], rules=rules, agents=", ".join(agents))
            prompt = PROMPT.format(day=ev["day"], eid=ev["id"], event=ev["event"], seen=seen_txt, board=board_txt, tools=tools_txt,
                                   evidence=fmt_evidence(evidence))
            res = call_llm(client, args.model, system, prompt) if client else offline_llm(evidence, ev)
            step += 1
            refs = [str(x) for x in res.get("policy_references", []) or []]
            rec = str(res.get("recommendation", ""))
            gate = policy_gate(client, args.model, rule_list, checks, rec)
            hits = ref_hits(ev.get("expected_refs", []), " ".join(refs) + " " + rec + " " + " ".join(map(str, res.get("reasoning_steps", []))))
            hits_all.update(hits)
            entry = {
                "entry_id": str(uuid.uuid4()), "timestamp": now(), "sim_day": int(ev["day"]), "scenario_step": step,
                "scenario": scenario_id, "event_id": ev["id"], "agent": name, "mandate": a["mandate"],
                "information_seen": sorted(seen_ids), "board_posts_seen": [f"{b['agent']}:{b['event_id']}" for b in posts],
                "tool_outputs": tools,
                "retrieved_sources": [{"source_id": e["source_id"], "section": e["section"], "chunk_id": e["chunk_id"],
                                       "distance": e["distance"]} for e in evidence],
                "reasoning_steps": [str(s) for s in res.get("reasoning_steps", [])] or ["(none given)"],
                "policy_references": refs, "recommendation": rec,
                "confidence": res.get("confidence") if res.get("confidence") in ("low", "medium", "high") else "low",
                "gaps_or_conflicts": [str(g) for g in res.get("gaps_or_conflicts", []) or []],
                "notify_agents": [str(n) for n in res.get("notify_agents", []) or [] if str(n) in agents],
                "policy_gate": gate,
                "human_review": {"status": "pending", "note": ("held by policy gate" if gate["result"] != "passed" else
                                 "flagged by agent" if res.get("needs_human_review", True) else "routine")},
                "model": args.model if client else "offline", "expected_refs_hit": hits,
                "previous_entry_hash": prev,
            }
            entry["entry_hash"] = entry_hash(entry)
            prev = entry["entry_hash"]
            entries.append(entry)
            board.append({"agent": name, "event_id": ev["id"], "notify": entry["notify_agents"],
                          "recommendation": rec if gate["result"] == "passed" else "(held by the policy gate for human review)"})
            md += [f"### {name} ({a['role']})", "",
                   f"**Saw:** {', '.join(sorted(seen_ids))}; board posts: {len(posts)}  ",
                   *([f"**Pipeline tools:** " + " ".join(f"[{t['tool']}] {t['output']}" for t in tools) + "  "] if tools else []),
                   f"**Retrieved:** {', '.join(dict.fromkeys(e['cite'] or e['source_id'] for e in evidence))}", "",
                   "**Reasoning:**", *[f"{i}. {s}" for i, s in enumerate(entry['reasoning_steps'], 1)], "",
                   f"**Recommendation:** {rec}", "",
                   f"**Policy references:** {'; '.join(refs) or '-'}  ",
                   f"**Gaps or conflicts:** {'; '.join(entry['gaps_or_conflicts']) or '-'}  ",
                   f"**Policy gate:** {gate['result']}" + (f" - {'; '.join(gate['keyword_flags'] + gate['broken_rules'])}. {gate['explanation']}" if gate['result'] != 'passed' else "") + "  ",
                   f"**Notify:** {', '.join(entry['notify_agents']) or '-'} · **Confidence:** {entry['confidence']} · "
                   f"**Human review:** pending ({entry['human_review']['note']})  ",
                   f"`entry_hash {entry['entry_hash'][:16]}…`", ""]
            print(f"day {ev['day']:>3} {ev['id']} {name:24} refs={len(refs)} hits={hits}")
        exp = ev.get("expected_refs", [])
        scores.append({"event": ev["id"], "expected": exp, "found": sorted(hits_all)})
        md += [f"**Expected:** {ev.get('expected', '')}  ", f"**Expected references found:** {len(hits_all)}/{len(exp)} "
               f"({', '.join(sorted(hits_all)) or 'none'})", ""]

    md += ["## Controversy", "", str(sc.get("controversy", "")).strip(), ""]
    tot = sum(len(s["expected"]) for s in scores)
    got = sum(len(s["found"]) for s in scores)
    held = sum(1 for e in entries if e["policy_gate"]["result"] != "passed")
    md += ["## Summary", "", f"- Agent steps logged: {len(entries)}", f"- Held by the policy gate: {held}", f"- Expected policy references cited: {got}/{tot}",
           f"- Final hash: `{prev}`", ""]
    with log_path.open("w", encoding="utf-8") as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    md_path.write_text("\n".join(md), encoding="utf-8")
    print(f"\n{scenario_id}: {len(entries)} steps, expected references cited {got}/{tot} -> {out}")
    return {"scenario": scenario_id, "steps": len(entries), "held_by_gate": held, "refs_found": got, "refs_expected": tot}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    itu_env.add_common_args(ap)
    ap.add_argument("--scenario", default="all", help="scenario id (file name in scenarios/) or 'all'")
    ap.add_argument("--llm", choices=["ollama", "offline"], default="ollama")
    ap.add_argument("--model", default="qwen2.5:7b", help="Ollama chat model (ITU default is qwen2.5:14b)")
    ap.add_argument("--ollama-url", default="http://localhost:11434")
    args = ap.parse_args()

    itu = itu_env.load_itu(args.itu_dir)
    embed = itu_env.get_embedder(args.embed, itu)
    kb = itu.KnowledgeBase(args.persist_dir or itu_env.default_persist_dir(args.embed, itu))
    agents_cfg = yaml.safe_load((ROOT / "agents" / "agents.yaml").read_text(encoding="utf-8"))
    ids = [p.stem for p in sorted((ROOT / "scenarios").glob("*.yaml"))] if args.scenario == "all" else [args.scenario]
    summary = [run(s, args, kb, embed, agents_cfg) for s in ids]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
