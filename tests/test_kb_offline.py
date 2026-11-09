"""Offline check of the knowledge-base build against the ITU reference code.

Needs the ITU code cloned (default ../ITUAIReadiness, or set ITU_DIR) and its Python requirements.
No Ollama or downloads needed: uses the offline word-matching embedder in a temporary database.

    ITU_DIR=../ITUAIReadiness python -m pytest tests/test_kb_offline.py -q
"""
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ITU_DIR = os.environ.get("ITU_DIR", str(ROOT.parent / "ITUAIReadiness"))
pytestmark = pytest.mark.skipif(not (Path(ITU_DIR) / "simulation").exists(), reason="ITU reference code not found")


def run(*args, db):
    return subprocess.run([sys.executable, *args, "--itu-dir", ITU_DIR, "--embed", "offline", "--persist-dir", str(db)],
                          cwd=ROOT, capture_output=True, text=True, timeout=900)


def test_ingest_and_retrieve(tmp_path):
    r = run("scripts/ingest_ph.py", db=tmp_path)
    assert r.returncode == 0, r.stderr
    assert "curated" in r.stdout and "kb_usecase" in r.stdout
    t = run("scripts/run_retrieval_tests.py", "--quiet", db=tmp_path)
    assert "Knowledge base:" in t.stdout, t.stderr
    passed = int(t.stdout.split("Knowledge base:")[1].split("/")[0])
    assert passed >= 20, t.stdout  # curated chunks alone answer most questions even with the crude embedder
    assert "top hit UC-" in t.stdout
