"""Shared setup for scripts that use the ITU reference code (CrashingGuru/ITUAIReadiness).

- load_itu(itu_dir): puts the ITU `simulation/` folder on the path and returns its modules.
- get_embedder(name, itu): returns a function texts -> vectors.
    "ollama"  : the ITU code's own embed_texts (nomic-embed-text via Ollama). Use this for the real build.
    "offline" : a word-hashing stand-in with no model download. For checking the code paths only;
                its retrieval scores say nothing about the real knowledge base.
- default_persist_dir(name): the real build uses the ITU default ChromaDB folder; the offline check
  uses ./data/chromadb_offline so the two can never mix.
"""
from __future__ import annotations

import hashlib
import math
import re
import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parent.parent


def load_itu(itu_dir: str) -> SimpleNamespace:
    sim = Path(itu_dir).resolve() / "simulation"
    if not (sim / "server" / "knowledge" / "ingest.py").exists():
        raise SystemExit(f"Cannot find the ITU reference code at {sim} (clone CrashingGuru/ITUAIReadiness first)")
    if str(sim) not in sys.path:
        sys.path.insert(0, str(sim))
    from server.config import settings  # noqa: E402
    from server.knowledge import ingest  # noqa: E402
    from server.knowledge.kb import KnowledgeBase  # noqa: E402
    return SimpleNamespace(settings=settings, ingest=ingest, KnowledgeBase=KnowledgeBase)


_STOP = set("""a an and are as at be by can do does for from has have how in into is it its may must not of on or
should that the their them there these this to under was were what when where which who why will with without""".split())
_DIM = 768


def _tokens(text: str) -> list[str]:
    words = [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in _STOP and len(w) > 1]
    words = [w[:-1] if len(w) > 4 and w.endswith("s") else w for w in words]  # crude plural folding
    return words + [f"{a}_{b}" for a, b in zip(words, words[1:])]


def _offline_embed(texts: list[str]) -> list[list[float]]:
    out = []
    for t in texts:
        v = [0.0] * _DIM
        for tok in _tokens(t):
            h = int(hashlib.md5(tok.encode()).hexdigest(), 16)
            v[h % _DIM] += 1.0 if (h >> 64) & 1 else -1.0
        n = math.sqrt(sum(x * x for x in v)) or 1.0
        out.append([x / n for x in v])
    return out


def get_embedder(name: str, itu: SimpleNamespace):
    if name == "ollama":
        return itu.ingest.embed_texts
    if name == "offline":
        return _offline_embed
    raise SystemExit(f"unknown embedder {name!r} (use ollama or offline)")


def default_persist_dir(embed: str, itu: SimpleNamespace) -> str | None:
    if embed == "offline":
        d = ROOT / "data" / "chromadb_offline"
        d.mkdir(parents=True, exist_ok=True)
        return str(d)
    return None  # ITU default (settings.chromadb_dir)


def add_common_args(ap) -> None:
    ap.add_argument("--itu-dir", required=True, help="path to the cloned ITUAIReadiness repo")
    ap.add_argument("--embed", choices=["ollama", "offline"], default="ollama",
                    help="ollama = real build (nomic-embed-text); offline = code check only")
    ap.add_argument("--persist-dir", default=None, help="ChromaDB folder (default: ITU default, or data/chromadb_offline)")
