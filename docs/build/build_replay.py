#!/usr/bin/env python3
"""Build docs/replay.html from the scenario files and the audit logs in results/ (self-contained page)."""
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
data = {"agents": yaml.safe_load((ROOT / "agents/agents.yaml").read_text(encoding="utf-8"))["agents"], "scenarios": {}}
for sid in ["mining_renewal", "policy_reuse"]:
    sc = yaml.safe_load((ROOT / f"scenarios/{sid}.yaml").read_text(encoding="utf-8"))
    runs = {}
    for run, folder in [("v2", "results/scenarios"), ("baseline", "results/scenarios_baseline")]:
        p = ROOT / folder / sid / "audit_log.jsonl"
        runs[run] = [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]
    data["scenarios"][sid] = {
        "title": sc["title"], "use_case": sc.get("use_case"), "sim_days": sc.get("sim_days"),
        "rules": sc.get("pre_agreed_rules", []), "controversy": str(sc.get("controversy", "")).strip(),
        "events": [{k: e.get(k) for k in ("id", "day", "to", "event", "expected", "expected_refs", "test")} for e in sc["events"]],
        "runs": runs}
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (ROOT / "docs/build/replay_template.html").read_text(encoding="utf-8").replace("__DATA__", blob)
(ROOT / "docs/replay.html").write_text(html, encoding="utf-8")
print("wrote docs/replay.html", len(html))
