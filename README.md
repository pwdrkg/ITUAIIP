# Community IKSP Record Pipeline

AI for Good Sandbox Hackathon (ITU AI for Good Lab, UAE) · Public services: indigenous knowledge, culture and public programmes · Philippines

Team: Paul Alvarez (lead), Kahlil de Silva · Repository: https://github.com/pwdrkg/ITUAIIP

Indigenous knowledge systems and practices (IKSP) sustain how Philippine Indigenous communities farm, govern themselves and respond to hazards, and they can improve public programmes such as disaster and climate planning. This pipeline helps communities make AI-assisted IKSP records they judge accurate and appropriate: it records accounts from many knowledge holders in their own languages, reads documents, cross-checks accounts, flags one-sided ones for human review, and reads the result back so holders can correct it (every correction logged). Records are released only for uses the community permits: community archive, education, disaster and climate planning, ancestral domain recognition, or protection against appropriation. Institutional AI agents (NCIP, DENR, NPC, LGU, legal adviser) test it against step-by-step error scenarios, and every decision is logged with its sources and reasoning.

**Research problem:** under what conditions can AI support community-directed documentation of IKSP that sustains knowledge transmission and gives a sound basis for authorised educational or policy use? (Problem statement by Kahlil de Silva; see `docs/full-report.docx`.)

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

One source (the IP Code, `PH-L04`) must be downloaded by hand; the fetch script prints instructions.

## Knowledge base

106 sources are listed in [`knowledge_base/SOURCES.md`](knowledge_base/SOURCES.md), each with its URL, the date it was checked, and how the solution uses it. Curated files add 25 key clauses (16 verbatim), 16 key figures and 17 policy gaps linked to global examples, each stored as its own chunk for exact citation. See [`knowledge_base/README.md`](knowledge_base/README.md). Philippine government works are not covered by copyright (IP Code s176), so the Philippine laws and rules can be published in the open knowledge base. Check the licence of each global-practice document before publishing it; community data is never published.

## Status

- [x] Concept, architecture, scenario and audit design
- [x] Verified source list, fetch, ingest and retrieval-test scripts
- [ ] Run ingestion and pass the retrieval test
- [ ] Agents and orchestrator
- [ ] Speech-to-text and entity-extraction fine-tunes
- [ ] Web interface
- [ ] End-to-end run of `scenarios/mining_overlap.yaml` with audit log
- [ ] Demo video (if shortlisted)

Key dates: registration 21 October 2026 · submission 10 November 2026.
