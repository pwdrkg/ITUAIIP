#!/usr/bin/env python3
"""Download the knowledge-base sources listed in knowledge_base/sources.csv.

Each file is saved to knowledge_base/InputDocs/<folder>/<id>_<slug>.<ext>,
and a log (knowledge_base/fetch_log.csv) records status, size and SHA-256
so the team can show exactly which version of each document was ingested.

Usage:
    python scripts/fetch_sources.py              # download everything not yet downloaded
    python scripts/fetch_sources.py --dry-run    # list what would be downloaded
    python scripts/fetch_sources.py --only PH-L01,PH-N02
    python scripts/fetch_sources.py --force      # re-download existing files

Sources marked download=manual are listed at the end with instructions.
Only the Python standard library is used.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "knowledge_base"
SOURCES = KB / "sources.csv"
INPUT = KB / "InputDocs"
LOG = KB / "fetch_log.csv"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36 ancestral-land-story-pipeline/0.1")
EXT_BY_TYPE = {
    "application/pdf": ".pdf",
    "text/html": ".html",
    "application/xhtml+xml": ".html",
    "text/plain": ".txt",
}


def slug(text: str, n: int = 60) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")
    return s[:n].rstrip("_")


def guess_ext(url: str, content_type: str, head: bytes) -> str:
    if head.startswith(b"%PDF"):
        return ".pdf"
    ct = content_type.split(";")[0].strip().lower()
    if ct in EXT_BY_TYPE:
        return EXT_BY_TYPE[ct]
    if url.lower().split("?")[0].endswith(".pdf"):
        return ".pdf"
    return ".html"


def existing_file(row: dict) -> Path | None:
    folder = INPUT / row["folder"]
    hits = sorted(folder.glob(f"{row['id']}_*"))
    return hits[0] if hits else None


def download(url: str, retries: int = 3, timeout: int = 60) -> tuple[bytes, str]:
    last = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.headers.get("Content-Type", "")
        except (urllib.error.URLError, TimeoutError) as e:  # noqa: PERF203
            last = e
            time.sleep(2 * attempt)
    raise RuntimeError(f"failed after {retries} tries: {last}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", default="", help="comma-separated source ids")
    args = ap.parse_args()

    rows = list(csv.DictReader(SOURCES.open(encoding="utf-8")))
    only = {s.strip() for s in args.only.split(",") if s.strip()}
    if only:
        rows = [r for r in rows if r["id"] in only]

    log_rows, manual, failed = [], [], []
    for r in rows:
        if r["download"].strip().lower() == "manual":
            manual.append(r)
            continue
        have = existing_file(r)
        if have and not args.force:
            print(f"skip  {r['id']:8} already have {have.name}")
            continue
        if args.dry_run:
            print(f"would {r['id']:8} -> {r['folder']}/  {r['url']}")
            continue
        try:
            data, ctype = download(r["url"])
            ext = guess_ext(r["url"], ctype, data[:5])
            out = INPUT / r["folder"] / f"{r['id']}_{slug(r['title'])}{ext}"
            out.parent.mkdir(parents=True, exist_ok=True)
            if have and have != out:
                have.unlink()
            out.write_bytes(data)
            sha = hashlib.sha256(data).hexdigest()
            print(f"ok    {r['id']:8} {len(data):>9,} bytes  {out.relative_to(ROOT)}")
            log_rows.append({"id": r["id"], "file": str(out.relative_to(ROOT)), "bytes": len(data),
                             "sha256": sha, "url": r["url"], "status": "ok",
                             "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds")})
        except Exception as e:  # noqa: BLE001
            print(f"FAIL  {r['id']:8} {e}")
            failed.append(r)
            log_rows.append({"id": r["id"], "file": "", "bytes": 0, "sha256": "", "url": r["url"],
                             "status": f"failed: {e}",
                             "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds")})

    if log_rows:
        new = not LOG.exists()
        with LOG.open("a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(log_rows[0].keys()))
            if new:
                w.writeheader()
            w.writerows(log_rows)

    if manual:
        print("\nDownload these by hand and save them in the folder shown,")
        print("named <id>_<anything>.pdf (or .html):")
        for r in manual:
            print(f"  {r['id']:8} {r['folder']}/  {r['title']}\n           {r['url']}\n           {r['notes']}")
    if failed:
        print(f"\n{len(failed)} download(s) failed. Open the URL in a browser, save the file into the")
        print("folder shown above, and name it <id>_<anything>.pdf (or .html).")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
