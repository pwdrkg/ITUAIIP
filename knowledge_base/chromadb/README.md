# Knowledge base database (ChromaDB)

`kb_chromadb_public.zip` is the built knowledge base, ready to load with the ITU reference code (CrashingGuru/ITUAIReadiness). It was built with `scripts/ingest_ph.py` and Ollama `nomic-embed-text` (768 dimensions, cosine distance) on 9 Nov 2026.

| Collection | Chunks | Content |
|---|---|---|
| `kb_main` | 6,059 | 95 public sources (Philippine laws, NCIP rules, data privacy issuances, Supreme Court decisions, government strategies and data, treaties binding on the Philippines) plus all curated clauses, figures and gaps |
| `kb_usecase` | 5 | IKSP Record Pipeline use case |

Each chunk carries `source_id`, `title`, `issuer`, `year`, `url`, folder (`document_category`) and `sections`.

**Public subset.** The full knowledge base has 8,311 chunks from 129 sources. The other 2,252 chunks come from copyrighted documents (journal articles, NGO, World Bank and UN-agency reports, news), which we cannot republish. The full database is in the private repository `pwdrkg/ITUAIIP-sources` (access for the evaluation team on request), and can be rebuilt from `knowledge_base/sources.csv` with the scripts. Philippine government works carry no copyright (IP Code s176).

**Use it:**

```bash
mkdir -p ../ITUAIReadiness/simulation/data/chromadb
unzip knowledge_base/chromadb/kb_chromadb_public.zip -d ../ITUAIReadiness/simulation/data/chromadb
python scripts/run_retrieval_tests.py --itu-dir ../ITUAIReadiness   # needs Ollama with nomic-embed-text
python scripts/run_scenario.py --itu-dir ../ITUAIReadiness            # needs a chat model, e.g. qwen2.5:7b
```

Retrieval test results for the full database are in `results/kb_retrieval_results.md` (39/39).
