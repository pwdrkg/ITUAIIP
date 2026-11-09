#!/usr/bin/env python3
"""Run the retrieval test in knowledge_base/retrieval_tests.yaml.

    python scripts/run_retrieval_tests.py --itu-dir ../ITUAIReadiness            # real knowledge base
    python scripts/run_retrieval_tests.py --itu-dir ../ITUAIReadiness --embed offline   # code check only

Prints pass/fail per question and the overall hit rate, then checks that the use-case collection
(kb_usecase) answers use-case questions. Exit code 1 if any knowledge-base test fails.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import itu_env  # noqa: E402
import kb_search  # noqa: E402

USECASE_QUESTIONS = [
    "Which ITU-T Y.3172 pipeline nodes does the IKSP record pipeline use?",
    "How does the policy gate handle consent and human override?",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    itu_env.add_common_args(ap)
    ap.add_argument("--quiet", action="store_true", help="only print failures and the summary")
    args = ap.parse_args()
    itu = itu_env.load_itu(args.itu_dir)
    embed = itu_env.get_embedder(args.embed, itu)
    kb = itu.KnowledgeBase(args.persist_dir or itu_env.default_persist_dir(args.embed, itu))
    if args.embed == "offline":
        print("NOTE: offline word-matching embedder - checks the code, not the real retrieval quality.\n")
    if kb.main.count() == 0:
        print("The knowledge base is empty: run scripts/ingest_ph.py first.")
        return 1

    spec = yaml.safe_load((ROOT / "knowledge_base" / "retrieval_tests.yaml").read_text(encoding="utf-8"))
    k = spec.get("top_k", 5)
    passed = 0
    for t in spec["tests"]:
        emb = embed([t["q"]])[0]
        metas = [m for _, _, m, _ in kb_search.search(kb, emb, k=k, curated_k=spec.get("curated_k", 2))]
        hits = [m for m in metas if m.get("source_id") in t["expect"]]
        ok = bool(hits)
        if ok and t.get("section"):
            ok = any(str(t["section"]) in m.get("sections", "").split(",") for m in hits)
        passed += ok
        if not (args.quiet and ok):
            got = ", ".join(f"{m.get('source_id', m.get('source_file'))}[{m.get('sections', '')}]" for m in metas)
            print(f"{'PASS' if ok else 'FAIL'}  {t['q']}\n      expected {t['expect']} got {got}")
    total = len(spec["tests"])
    print(f"\nKnowledge base: {passed}/{total} passed ({kb.main.count()} chunks in {itu.settings.kb_main_collection})")

    uc_name = itu.settings.kb_usecase_collection
    uc = kb._col(uc_name)
    if uc.count() == 0:
        print(f"Use-case collection {uc_name} is empty (run ingest without --no-usecase).")
    else:
        for q in USECASE_QUESTIONS:
            r = kb.search(embed([q])[0], n_results=1, collection_name=uc_name)
            print(f"Use case: {q}\n      top hit {r['ids'][0][0]}: {r['documents'][0][0][:110]!r}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
