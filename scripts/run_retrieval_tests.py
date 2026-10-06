#!/usr/bin/env python3
"""Run the retrieval test in knowledge_base/retrieval_tests.yaml.

    python scripts/run_retrieval_tests.py --itu-dir ../ITUAIReadiness

Prints pass/fail per question and the overall hit rate. Exit code 1 if any fail.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--itu-dir", required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(Path(args.itu_dir).resolve() / "simulation"))
    from server.knowledge.ingest import embed_texts  # noqa: E402
    from server.knowledge.kb import KnowledgeBase  # noqa: E402

    spec = yaml.safe_load((ROOT / "knowledge_base" / "retrieval_tests.yaml").read_text())
    k = spec.get("top_k", 5)
    kb = KnowledgeBase()
    passed = 0
    for t in spec["tests"]:
        emb = embed_texts([t["q"]])[0]
        res = kb.search(emb, n_results=k)
        metas = res["metadatas"][0]
        hits = [m for m in metas if m.get("source_id") in t["expect"]]
        ok = bool(hits)
        if ok and t.get("section"):
            ok = any(str(t["section"]) in m.get("sections", "").split(",") for m in hits)
        passed += ok
        got = ", ".join(f"{m.get('source_id', m.get('source_file'))}[{m.get('sections', '')}]" for m in metas)
        print(f"{'PASS' if ok else 'FAIL'}  {t['q']}\n      expected {t['expect']} got {got}")
    print(f"\n{passed}/{len(spec['tests'])} passed")
    return 0 if passed == len(spec["tests"]) else 1


if __name__ == "__main__":
    sys.exit(main())
