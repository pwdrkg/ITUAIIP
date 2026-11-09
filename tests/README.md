# Tests

- `scripts/run_retrieval_tests.py`: the knowledge base returns the right source and section for each question in `knowledge_base/retrieval_tests.yaml`.
- `tests/test_kb_offline.py`: builds the knowledge base through the ITU reference code with the offline embedder in a temporary database and checks that ingestion, the retrieval test and the use-case collection work (`ITU_DIR=../ITUAIReadiness python -m pytest tests -q`).
- Planned: scenario test (each agent's response cites the `expected_refs` in `scenarios/mining_renewal.yaml` and `scenarios/policy_reuse.yaml`); audit log test (every entry validates against the schema and the hash chain is unbroken).
