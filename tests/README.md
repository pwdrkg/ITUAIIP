# Tests

- `scripts/run_retrieval_tests.py`: the knowledge base returns the right source and section for each question in `knowledge_base/retrieval_tests.yaml`.
- Planned: scenario test (each agent's response cites the `expected_refs` in `scenarios/mining_overlap.yaml`); audit log test (every entry validates against the schema and the hash chain is unbroken).
