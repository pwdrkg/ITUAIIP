#!/usr/bin/env python3
"""Ingest the downloaded sources into the ITU reference knowledge base.

Reuses the ITU reference code (CrashingGuru/ITUAIReadiness) for parsing,
chunking, embedding and storage, and adds metadata from sources.csv to
every chunk: source id, title, issuer, year, document type, URL, folder,
country, and the section numbers that appear in the chunk (for example
"52,59"), so agents can cite the exact clause.

Run from the repository root, after scripts/fetch_sources.py:
    python scripts/ingest_ph.py --itu-dir ../ITUAIReadiness [--reset]

Code check without Ollama (word-matching stand-in, separate database; not the real knowledge base):
    python scripts/ingest_ph.py --itu-dir ../ITUAIReadiness --embed offline

Also loads knowledge_base/use_case/*.md into the ITU use-case collection (kb_usecase), which the
ITU use-case agent searches. Skip with --no-usecase.

--export-inputdocs DIR copies the downloaded sources and the use-case document into the ITU code's own
InputDocs layout (DIR/AI_Strategies, DIR/AI_Use_Cases), file names prefixed "Philippines_", so the ITU
documented command `python -m server.knowledge.ingest --reset` can load them too.

Requires the ITU code's dependencies (chromadb, ollama, docling or PyMuPDF)
and a running Ollama server with the nomic-embed-text model.

Also stores each curated provision, fact and gap (knowledge_base/curated/*.yaml)
as its own chunk; skip with --no-curated.
"""
from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import itu_env  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "knowledge_base"
SECTION_RE = re.compile(r"\b(?:Section|Sec\.|SECTION)\s+(\d{1,3})", re.I)
ARTICLE_RE = re.compile(r"\bArt(?:icle|\.)\s+(\d{1,3})", re.I)


def sections_in(text: str) -> str:
    found = sorted({int(n) for n in SECTION_RE.findall(text)} | {int(n) for n in ARTICLE_RE.findall(text)})
    return ",".join(str(n) for n in found[:30])


def main() -> int:
    ap = argparse.ArgumentParser()
    itu_env.add_common_args(ap)
    ap.add_argument("--no-usecase", action="store_true", help="skip knowledge_base/use_case/*.md")
    ap.add_argument("--export-inputdocs", default="", help="also copy files into this ITU InputDocs folder")
    ap.add_argument("--reset", action="store_true", help="delete existing chunks from these sources first")
    ap.add_argument("--only", default="", help="comma-separated source ids")
    ap.add_argument("--no-curated", action="store_true", help="skip knowledge_base/curated/*.yaml")
    ap.add_argument("--curated-only", action="store_true", help="only (re)load knowledge_base/curated/*.yaml")
    args = ap.parse_args()

    itu = itu_env.load_itu(args.itu_dir)
    build_metadata, chunk_text, parse_file = itu.ingest.build_metadata, itu.ingest.chunk_text, itu.ingest.parse_file
    embed_texts = itu_env.get_embedder(args.embed, itu)
    kb = itu.KnowledgeBase(args.persist_dir or itu_env.default_persist_dir(args.embed, itu))
    if args.embed == "offline":
        print("NOTE: offline word-matching embedder - a code check only, not the real knowledge base.\n")
    rows = list(csv.DictReader((KB / "sources.csv").open(encoding="utf-8")))
    only = {s.strip() for s in args.only.split(",") if s.strip()}
    total = 0
    for r in rows:
        if args.curated_only:
            break
        if only and r["id"] not in only:
            continue
        files = [f for f in sorted((KB / "InputDocs" / r["folder"]).glob(f"{r['id']}_*")) if f.is_file()]
        if not files:
            print(f"missing {r['id']}: run scripts/fetch_sources.py (or download by hand)")
            continue
        if args.reset:
            kb.main.delete(where={"source_id": r["id"]})
        # every file for this id: e.g. a scanned PDF plus its OCR text, or a PDF plus a DOCX
        texts = [read_any(f, parse_file) for f in files]
        text = "\n\n".join(t for t in texts if t and t.strip())
        path = files[0]
        chunks = chunk_text(text) if text.strip() else []
        if not chunks:
            print(f"empty   {r['id']}: no text extracted from {', '.join(f.name for f in files)} (scanned? run OCR)")
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
        print(f"ok      {r['id']:8} {len(chunks):>4} chunks  {path.name}{f' (+{len(files) - 1} more)' if len(files) > 1 else ''}")
        if args.export_inputdocs:
            export(path, Path(args.export_inputdocs) / "AI_Strategies", r["id"])
    if args.curated_only or (not args.no_curated and not only):
        total += ingest_curated(kb, embed_texts)
    if not args.no_usecase and not only:
        total += ingest_usecase(kb, itu, embed_texts, chunk_text, parse_file, build_metadata, args.export_inputdocs)
    print(f"\nStored {total} chunks.")
    return 0


def read_any(path: Path, parse_file) -> str:
    """Text of a source file. DOCX is read directly; everything else goes through the ITU parser."""
    if path.suffix.lower() == ".docx":
        import zipfile
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", "ignore")
        xml = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    try:
        return parse_file(path)
    except Exception as e:  # noqa: BLE001
        print(f"warning {path.name}: {e}")
        return ""


def export(path: Path, dest: Path, sid: str) -> None:
    """Copy a file into the ITU InputDocs layout with a Philippines_ prefix."""
    dest.mkdir(parents=True, exist_ok=True)
    name = path.name if path.name.startswith("Philippines_") else f"Philippines_{path.name}"
    shutil.copy2(path, dest / name)


def ingest_usecase(kb, itu, embed_texts, chunk_text, parse_file, build_metadata, export_dir: str) -> int:
    """Load knowledge_base/use_case/*.md into the ITU use-case collection (kb_usecase)."""
    col_name = itu.settings.kb_usecase_collection
    col = kb._col(col_name)
    total = 0
    for path in sorted((KB / "use_case").glob("*.md")):
        chunks = chunk_text(parse_file(path))
        if not chunks:
            continue
        sid = "UC-" + path.stem
        col.delete(where={"source_id": sid})
        metas = []
        for i, ch in enumerate(chunks):
            m = build_metadata(path, i, len(chunks), {"source_id": sid, "title": path.stem.replace("_", " "),
                                                      "document_category": "AI_Use_Cases", "country": "Philippines"})
            m["sections"] = sections_in(ch)
            metas.append(m)
        kb.add_documents(texts=chunks, embeddings=embed_texts(chunks), metadatas=metas,
                         ids=[f"{sid}::{i}" for i in range(len(chunks))], collection_name=col_name)
        total += len(chunks)
        print(f"ok      use case {len(chunks):>4} chunks  {path.name} -> {col_name}")
        if export_dir:
            export(path, Path(export_dir) / "AI_Use_Cases", sid)
    return total


def ingest_curated(kb, embed_texts) -> int:
    """Store each curated provision, fact and gap as its own chunk.

    One clause per chunk gives precise retrieval and exact citations.
    """
    import yaml

    cur = KB / "curated"
    items: list[tuple[str, str, dict]] = []
    for p in yaml.safe_load((cur / "provisions.yaml").read_text(encoding="utf-8"))["provisions"]:
        topics = " ".join(t.replace("_", " ") for t in p.get("topic", []))
        items.append((f"CUR::{p['id']}", f"{p['cite']}. Topics: {topics}. {p['text']}",
                      {"source_id": p["source_id"], "curated": "provision", "cite": p["cite"],
                       "kind": p["kind"], "topics": ",".join(p.get("topic", [])),
                       "sections": ",".join(sorted(set(re.findall(r"\bs(\d{1,3})", p["cite"]))
                                                   | set(filter(None, sections_in(p["text"]).split(",")))))}))
    for f in yaml.safe_load((cur / "facts.yaml").read_text(encoding="utf-8"))["facts"]:
        items.append((f"CUR::{f['id']}", f["fact"] + (f" Note: {f['note']}" if f.get("note") else ""),
                      {"source_id": f["source_id"], "curated": "fact", "sections": ""}))
    for g in yaml.safe_load((cur / "gaps.yaml").read_text(encoding="utf-8"))["gaps"]:
        ex = " ".join(e["example"] for e in g.get("global_examples", []))
        label = "Gap in current practice" if g.get("scope") == "practice" else "Policy gap"
        text = f"{label} ({g['type']}): {g['title']}. {g['detail']} Global examples: {ex}"
        srcs = [e["source_id"] for e in g.get("global_examples", [])]
        items.append((f"CUR::{g['id']}", text,
                      {"source_id": srcs[0] if srcs else "", "curated": "gap", "gap_type": g["type"], "gap_scope": g.get("scope", "policy"),
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
