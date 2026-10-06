#!/usr/bin/env python3
"""Ingest the downloaded sources into the ITU reference knowledge base.

Reuses the ITU reference code (CrashingGuru/ITUAIReadiness) for parsing,
chunking, embedding and storage, and adds metadata from sources.csv to
every chunk: source id, title, issuer, year, document type, URL, folder,
country, and the section numbers that appear in the chunk (for example
"52,59"), so agents can cite the exact clause.

Run from the repository root, after scripts/fetch_sources.py:
    python scripts/ingest_ph.py --itu-dir ../ITUAIReadiness [--reset]

Requires the ITU code's dependencies (chromadb, ollama, docling or PyMuPDF)
and a running Ollama server with the nomic-embed-text model.

Also stores each curated provision, fact and gap (knowledge_base/curated/*.yaml)
as its own chunk; skip with --no-curated.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "knowledge_base"
SECTION_RE = re.compile(r"\b(?:Section|Sec\.|SECTION)\s+(\d{1,3})", re.I)
ARTICLE_RE = re.compile(r"\bArt(?:icle|\.)\s+(\d{1,3})", re.I)


def sections_in(text: str) -> str:
    found = sorted({int(n) for n in SECTION_RE.findall(text)} | {int(n) for n in ARTICLE_RE.findall(text)})
    return ",".join(str(n) for n in found[:30])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--itu-dir", required=True, help="path to the cloned ITUAIReadiness repo")
    ap.add_argument("--reset", action="store_true", help="delete existing chunks from these sources first")
    ap.add_argument("--only", default="", help="comma-separated source ids")
    ap.add_argument("--no-curated", action="store_true", help="skip knowledge_base/curated/*.yaml")
    args = ap.parse_args()

    sim = Path(args.itu_dir).resolve() / "simulation"
    if not (sim / "server").exists():
        print(f"Cannot find ITU code at {sim}/server", file=sys.stderr)
        return 2
    sys.path.insert(0, str(sim))
    from server.knowledge.ingest import build_metadata, chunk_text, embed_texts, parse_file  # noqa: E402
    from server.knowledge.kb import KnowledgeBase  # noqa: E402

    kb = KnowledgeBase()
    rows = list(csv.DictReader((KB / "sources.csv").open(encoding="utf-8")))
    only = {s.strip() for s in args.only.split(",") if s.strip()}
    total = 0
    for r in rows:
        if only and r["id"] not in only:
            continue
        files = sorted((KB / "InputDocs" / r["folder"]).glob(f"{r['id']}_*"))
        if not files:
            print(f"missing {r['id']}: run scripts/fetch_sources.py (or download by hand)")
            continue
        path = files[0]
        if args.reset:
            kb.main.delete(where={"source_id": r["id"]})
        text = parse_file(path)
        chunks = chunk_text(text)
        if not chunks:
            print(f"empty   {r['id']}: no text extracted from {path.name}")
            continue
        embeddings = embed_texts(chunks)
        extra = {
            "source_id": r["id"], "title": r["title"], "issuer": r["issuer"], "year": r["year"],
            "doc_type": r["doc_type"], "url": r["url"], "document_category": r["folder"],
            "country": "Philippines" if r["folder"].startswith("PH_") else "Global",
        }
        metas = []
        for i, ch in enumerate(chunks):
            m = build_metadata(path, i, len(chunks), extra)
            m["sections"] = sections_in(ch)
            metas.append(m)
        ids = [f"{r['id']}::{i}" for i in range(len(chunks))]
        kb.add_documents(texts=chunks, embeddings=embeddings, metadatas=metas, ids=ids)
        total += len(chunks)
        print(f"ok      {r['id']:8} {len(chunks):>4} chunks  {path.name}")
    if not args.no_curated and not only:
        total += ingest_curated(kb, embed_texts)
    print(f"\nStored {total} chunks.")
    return 0


def ingest_curated(kb, embed_texts) -> int:
    """Store each curated provision, fact and gap as its own chunk.

    One clause per chunk gives precise retrieval and exact citations.
    """
    import yaml

    cur = KB / "curated"
    items: list[tuple[str, str, dict]] = []
    for p in yaml.safe_load((cur / "provisions.yaml").read_text(encoding="utf-8"))["provisions"]:
        items.append((f"CUR::{p['id']}", f"{p['cite']}. {p['text']}",
                      {"source_id": p["source_id"], "curated": "provision", "cite": p["cite"],
                       "kind": p["kind"], "topics": ",".join(p.get("topic", [])),
                       "sections": ",".join(sorted(set(re.findall(r"\bs(\d{1,3})", p["cite"]))
                                                   | set(filter(None, sections_in(p["text"]).split(",")))))}))
    for f in yaml.safe_load((cur / "facts.yaml").read_text(encoding="utf-8"))["facts"]:
        items.append((f"CUR::{f['id']}", f["fact"] + (f" Note: {f['note']}" if f.get("note") else ""),
                      {"source_id": f["source_id"], "curated": "fact", "sections": ""}))
    for g in yaml.safe_load((cur / "gaps.yaml").read_text(encoding="utf-8"))["gaps"]:
        ex = " ".join(e["example"] for e in g.get("global_examples", []))
        text = f"Policy gap ({g['type']}): {g['title']}. {g['detail']} Global examples: {ex}"
        srcs = [e["source_id"] for e in g.get("global_examples", [])]
        items.append((f"CUR::{g['id']}", text,
                      {"source_id": srcs[0] if srcs else "", "curated": "gap", "gap_type": g["type"],
                       "related_sources": ",".join(srcs), "ph_refs": ",".join(g.get("ph_refs", [])),
                       "sections": ""}))
    ids = [i[0] for i in items]
    kb.main.delete(ids=ids)  # idempotent re-run
    kb.add_documents(texts=[i[1] for i in items], embeddings=embed_texts([i[1] for i in items]),
                     metadatas=[{**i[2], "country": "Philippines", "document_category": "Curated"} for i in items],
                     ids=ids)
    print(f"ok      curated  {len(items):>4} chunks  (provisions, facts, gaps)")
    return len(items)


if __name__ == "__main__":
    sys.exit(main())
