#!/usr/bin/env python3
"""Check an audit log: every entry matches audit/audit_entry.schema.json and the hash chain is unbroken.

    python scripts/verify_audit.py results/scenarios/mining_renewal/audit_log.jsonl
Exit code 0 when the log is intact; any edited, removed or reordered entry is reported.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def entry_hash(entry: dict) -> str:
    body = {k: v for k, v in entry.items() if k != "entry_hash"}
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def verify(path: Path) -> list[str]:
    import jsonschema
    schema = json.loads((ROOT / "audit" / "audit_entry.schema.json").read_text(encoding="utf-8"))
    errors, prev = [], "GENESIS"
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    for i, line in enumerate(lines, 1):
        e = json.loads(line)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(e):
            errors.append(f"entry {i}: schema: {err.message}")
        if e.get("previous_entry_hash") != prev:
            errors.append(f"entry {i}: chain broken (previous_entry_hash does not match entry {i - 1})")
        if entry_hash(e) != e.get("entry_hash"):
            errors.append(f"entry {i}: content changed after logging (hash mismatch)")
        prev = e.get("entry_hash")
    print(f"{path}: {len(lines)} entries, {'OK' if not errors else f'{len(errors)} problem(s)'}")
    return errors


def main() -> int:
    paths = [Path(p) for p in sys.argv[1:]] or sorted((ROOT / "results" / "scenarios").glob("*/audit_log.jsonl"))
    bad = []
    for p in paths:
        bad += verify(p)
    for b in bad:
        print("  " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
