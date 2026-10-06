# Knowledge base

| Path | What it is |
| --- | --- |
| `sources.csv` | Manifest of 50 sources: URL, issuer, year, how the solution uses it, key sections, and how each was checked |
| `SOURCES.md` | The same list, readable |
| `InputDocs/<folder>/` | Downloaded documents (filled by `scripts/fetch_sources.py`) |
| `curated/provisions.yaml` | Key clauses, one per entry, verbatim where the text is official |
| `curated/facts.yaml` | Key figures with sources |
| `curated/gaps.yaml` | Domain policy gaps linked to Philippine clauses and global examples |
| `retrieval_tests.yaml` | 27 questions with the sources each must retrieve |
| `fetch_log.csv` | Created on download: file, size, SHA-256, time |
| `private_store/` | Community data for local testing only; git-ignored |

## How chunks are tagged

Every chunk carries `source_id`, `title`, `issuer`, `year`, `doc_type`, `url`, `document_category` (folder), `country`, and `sections` (section or article numbers found in the chunk). Curated chunks also carry `curated` (provision, fact or gap), `cite`, `topics`, and for gaps `gap_type`, `ph_refs` and `related_sources`.

Agents filter by folder (see `agents/agents.yaml`) and cite `cite` or `source_id` plus `sections` in the audit log.

## Adding a source

1. Add a row to `sources.csv` with a new id (`PH-L10`, `G-18`, …), the folder, URL and what it is for.
2. Open the document and confirm its title before setting `verified` to `opened <date>`.
3. Run `python scripts/fetch_sources.py --only <id>` then `python scripts/ingest_ph.py --itu-dir ../ITUAIReadiness --only <id>`.
4. Add at least one question to `retrieval_tests.yaml`.
