# IKSP Record Pipeline

AI for Good Sandbox Hackathon (ITU AI for Good Lab, UAE) · Public services: indigenous knowledge, culture and public programmes · Philippines

Team: Paul Alvarez (lead) · Repository: https://github.com/pwdrkg/ITUAIIP

Indigenous knowledge systems and practices (IKSP) sustain how Philippine Indigenous communities farm, govern themselves and respond to hazards, and they can improve public programmes such as disaster and climate planning. This pipeline helps communities make AI-assisted IKSP records they judge accurate and appropriate: it records accounts from many knowledge holders in their own languages, reads documents, cross-checks accounts, flags one-sided ones for human review, and reads the result back so holders can correct it (every correction logged). Records are released only for uses the community permits: community archive, education, disaster and climate planning, ancestral domain recognition, or protection against appropriation. Institutional AI agents (NCIP, DENR, NPC, LGU, legal adviser) test it against step-by-step error scenarios, and every decision is logged with its sources and reasoning.

**Research problem:** under what conditions can AI support community-directed documentation of IKSP that sustains knowledge transmission and gives a sound basis for authorised educational or policy use? (Problem statement by a team member; see `docs/full-report.docx`.)

![Architecture](docs/architecture.png)

## Repository layout

| Folder | What it holds | Y.3172 stage |
| --- | --- | --- |
| `knowledge_base/` | Verified source list, downloaded documents, retrieval test | SRC (policy corpus) |
| `knowledge_base/private_store/` | Community recordings and documents. **Never committed or published** | SRC (community) |
| `pipeline/collector/` | Web and phone recorder, document upload, consent | C |
| `pipeline/preprocessor/` | Voice reader (speech-to-text), text reader (OCR), translation, entity extraction | PP |
| `pipeline/models/` | Story matcher, bias check | M |
| `pipeline/policy/` | Consent gate, controlled (tapu) / open (noa) marks, human review | P |
| `pipeline/distributor/` | Role- and consent-based routing | D |
| `pipeline/sink/` | Read-back, sample dossier | SINK |
| `agents/` | Institutional agents and their mandates | M (orchestrated) |
| `scenarios/` | Error scenarios with events released over simulated days | Orchestrator |
| `audit/` | Audit log schema (hash-chained) | Audit |
| `app/` | Web interface | C / SINK |
| `scripts/` | Fetch, ingest and retrieval-test scripts | |
| `docs/` | Concept paper, technical report, full report, diagram | |

## Build the knowledge base

Requires Python 3.10+, git, and [Ollama](https://ollama.com) running with `ollama pull nomic-embed-text`.

```bash
bash scripts/setup_kb.sh            # clone ITU code, download sources, ingest, test
```

Or step by step:

```bash
git clone https://github.com/CrashingGuru/ITUAIReadiness.git ../ITUAIReadiness
pip install -r requirements.txt -r ../ITUAIReadiness/simulation/requirements.txt
python scripts/fetch_sources.py                     # downloads into knowledge_base/InputDocs/
python scripts/ingest_ph.py --itu-dir ../ITUAIReadiness
python scripts/run_retrieval_tests.py --itu-dir ../ITUAIReadiness
```

61 sources download automatically; 70 are marked `manual` in `knowledge_base/sources.csv` and must be saved by hand into `knowledge_base/InputDocs/<folder>/<id>_<name>` (the fetch script lists them). Ingestion also loads `knowledge_base/use_case/` into the ITU use-case collection (`kb_usecase`), which the ITU use-case agent searches.

To use the ITU code's own documented ingest instead, add `--export-inputdocs ../ITUAIReadiness/simulation/server/knowledge/InputDocs` to the ingest command, then run `python -m server.knowledge.ingest --reset` inside `ITUAIReadiness/simulation`.

## Run the error scenarios (agents and audit log)

After the knowledge base is built, with an Ollama chat model pulled (`ollama pull qwen2.5:7b`; the ITU default is `qwen2.5:14b`):

```bash
python scripts/run_scenario.py --itu-dir ../ITUAIReadiness --scenario all   # both scenarios
python scripts/verify_audit.py                                               # schema + hash chain check
```

The orchestrator releases each event on its simulated day only to the agents listed in `to`. Each agent sees only its own events plus other agents' board posts about them, searches only its mandated folders (plus curated clauses), and returns reasoning steps, policy references, a recommendation, confidence and a human-review flag. Every step goes to `results/scenarios/<id>/audit_log.jsonl` (hash-chained; schema in `audit/`) and a readable `transcript.md`. Nothing is approved automatically.

**Check the code without Ollama or downloads** (word-matching stand-in, separate database in `data/chromadb_offline`; the scores say nothing about the real knowledge base):

```bash
python scripts/ingest_ph.py --itu-dir ../ITUAIReadiness --embed offline
python scripts/run_retrieval_tests.py --itu-dir ../ITUAIReadiness --embed offline
ITU_DIR=../ITUAIReadiness python -m pytest tests -q
```

Offline check, 9 November 2026: curated chunks (65) and the use-case document (5) load through the ITU code; 25 of 39 test questions pass from curated chunks alone; the other 14 need the full documents.

## Knowledge base

131 sources are listed in [`knowledge_base/SOURCES.md`](knowledge_base/SOURCES.md), each with its URL, the date it was checked, and how the solution uses it. Curated files add 27 key clauses (16 verbatim), 16 key figures, 17 policy gaps and 5 gaps in current practice linked to global examples, each stored as its own chunk for exact citation. See [`knowledge_base/README.md`](knowledge_base/README.md). Philippine government works are not covered by copyright (IP Code s176), so the Philippine laws and rules can be published in the open knowledge base. Check the licence of each global-practice document before publishing it; community data is never published.

## Status

- [x] Concept, architecture, scenario and audit design
- [x] Verified source list, fetch, ingest and retrieval-test scripts
- [x] Ingestion and retrieval test run end to end against the ITU code (offline check)
- [x] Use-case document loaded into the ITU use-case collection
- [ ] Full build with Ollama (nomic-embed-text) and all 128 sources; pass the retrieval test
- [ ] Agents and orchestrator
- [ ] Speech-to-text and entity-extraction fine-tunes
- [ ] Web interface
- [ ] End-to-end run of `scenarios/mining_renewal.yaml` (Scenario 1, use case D) and `scenarios/policy_reuse.yaml` (Scenario 2, use case C) with audit log
- [ ] Demo video (if shortlisted)

Key dates: registration 21 October 2026 · submission 10 November 2026.
