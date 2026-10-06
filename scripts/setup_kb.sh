#!/usr/bin/env bash
# One-shot knowledge-base setup:
#   1. clone the ITU reference code next to this repo (if missing)
#   2. install its Python dependencies
#   3. download the sources in knowledge_base/sources.csv
#   4. ingest them into the ITU ChromaDB knowledge base
#   5. run the retrieval test
# Needs: git, Python 3.10+, and Ollama running with `ollama pull nomic-embed-text`.
set -euo pipefail
cd "$(dirname "$0")/.."
ITU_DIR="${ITU_DIR:-../ITUAIReadiness}"

if [ ! -d "$ITU_DIR" ]; then
  git clone https://github.com/CrashingGuru/ITUAIReadiness.git "$ITU_DIR"
fi

python -m pip install -r requirements.txt
if [ -f "$ITU_DIR/simulation/requirements.txt" ]; then
  python -m pip install -r "$ITU_DIR/simulation/requirements.txt"
else
  python -m pip install chromadb ollama pydantic-settings sqlmodel pymupdf
fi

python scripts/fetch_sources.py || echo "Some downloads failed; see the list above and save them by hand."
python scripts/ingest_ph.py --itu-dir "$ITU_DIR"
python scripts/run_retrieval_tests.py --itu-dir "$ITU_DIR"
