"""Shared retrieval used by the agents and the retrieval test.

Two passes over the same knowledge base:
1. curated pass: the best hand-checked clauses, figures and gaps (exact citations);
2. general pass: the best passages from the full documents.
Results are merged (curated first, no duplicates) and cut to k.
"""
from __future__ import annotations


def search(kb, query_embedding, k: int = 5, curated_k: int = 2, where: dict | None = None):
    """Return a list of (id, text, metadata, distance), best first."""
    def run(n, w):
        r = kb.search(query_embedding, n_results=n, where=w) if w else kb.search(query_embedding, n_results=n)
        return list(zip(r["ids"][0], r["documents"][0], r["metadatas"][0], r["distances"][0]))

    cur_filter = {"document_category": "Curated"}
    if where:
        cur_filter = {"$and": [cur_filter, where]}
    curated = run(curated_k, cur_filter) if curated_k else []
    general = run(k, where)
    seen, out = set(), []
    for item in curated + general:
        if item[0] not in seen:
            seen.add(item[0]); out.append(item)
    return out[:k]
