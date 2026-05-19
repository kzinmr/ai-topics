# Autoresearching BM25 on MSMarco

source: https://softwaredoug.com/blog/2026/05/17/autoresearching-a-better-msmarco-bm25
author: Doug Turnbull (@softwaredoug)
date: 2026-05-17
tags: [autoresearch, bm25, msmarco, search, information-retrieval, lexical-search, agentic-search, agent-loop, overfitting, validation]

---

> At Haystack I spoke about auto***research:*** Code generation to optimize search rankers.
> Can we use it to improve on BM25?

## Overview

This article represents Doug Turnbull's lab notes on using an **autoresearch** coding agent to iteratively improve a BM25 ranking function on the MSMarco passage retrieval dataset. The agent starts with a BM25 implementation, proposes changes, and accepts those that improve NDCG.

Key takeaway: the agent finds modest but **non‑groundbreaking tuning tweaks** (stopword removal, phrase boost, constant term score), but the process **overfits the small "minimarco" sample**, revealing subtle data leakage through validation. The exercise yields valuable lessons for building search tuning agents.

Full code in [this notebook](https://github.com/softwaredoug/search-experiments/blob/main/notebooks/codegen/codegen_minimarco.ipynb).

---

## Starting BM25 Code

The baseline uses **SearchArray** to fetch numpy arrays and compute BM25 manually:

```python
def rerank_minimarco(query, fielded_bm25, get_corpus):
    ...
```

Inputs:
- `fielded_bm25`: Simple BM25 search helper (OR, phrase, AND)
- `get_corpus`: Raw index access to term freqs, doc freq, doc lengths

```python
k1 = 0.6
b = 0.62
n_docs = len(corpus)
scores = np.zeros(n_docs)

for term in terms:
    term_freqs = snowball.termfreqs(term)
    doc_freq = snowball.docfreq(term)
    if doc_freq == 0:
        continue

    idf = np.log(1.0 + (n_docs - doc_freq + 0.5) / (doc_freq + 0.5))
    denom = term_freqs + k1 * (1.0 - b + b * (doc_lengths / avg_dl))
    scores += idf * (term_freqs * (k1 + 1.0)) / np.where(denom == 0, 1.0, denom)
```

---

## The Training Process

Doug built his own coding agent that talks directly to OpenAI, submitting code patches. Not using Pi, Claude Code, or other off-the-shelf tools.

### Dual-Gate Evaluation

**`try_out_patch` — Training Sandbox:**
- Agent proposes a code change
- Tool creates scratch version of the ranker
- Replays training queries, returns per-query impact (full visibility)
- No permanent state saved

**`apply_patch` — Validation Gate:**
- Agent decides to commit a change
- Tool re‑evaluates on **held‑out validation set** (no per-query visibility for agent)
- If overall validation metric improves → change saved
- If not → rejected
- Prevents overfitting to training data

### Additional Agent Tools
- `run_reranker`: test current ranker on single query with top‑N labeled results
- `fielded_bm25`: direct use of search primitives
- Revert to prior states
- Grep previous round directories to learn from past attempts

### Rounds & Dataset
- **~8 rounds**: each round starts from prior round's best code
- **Minimarco**: smaller sampled MSMarco used for all training + validation
- Full MSMarco only used for final measurement

---

## Results

### Performance
- **Minimarco:** steady NDCG increase across rounds
- **Full MSMarco:** plateau — most gains in round 1 (MRR ~0.2), then marginal

### What the Agent Learned

1. **Stopword removal** for longer queries (>3 tokens):
```python
q = [t for t in toks if t not in sw]
toks = q if len(toks) > 3 and len(q) > 1 and "de" not in q else toks
```

2. **Phrase/bigram boost** (0.08 × termfreq of each consecutive bigram):
```python
s += sum((.08 * a.termfreqs(toks[i:i+2]) for i in range(len(toks)-1)), np.zeros(n))
```

3. **Constant term boost** (+0.25 × (tf > 0)) after BM25

> These are not novel — just "encyclopedic" tuning tricks the LLM pulled from its training data.

---

## Overfitting & Data Leakage

The stopword list reveals overfitting to minimarco:

```python
sw = set(("what is are was were be as a an the"
          "in to for do doe did can you i me there"
          "where when who why how "
          "which consid achiev mani some word need and"
          "or on with from that call place medicin vacat").split())
```

**`medicin`** and **`vacat`** are completely idiosyncratic — useful only on the minimarco sample. This demonstrates that **any validation gate in a brute‑force optimization loop can leak sample‑specific information** into the final solution.

---

## Lessons & Future Directions

### Key Takeaways
- Smaller datasets accelerate iteration but risk **overfitting**
- Agents can find sensible, but not revolutionary, tuning improvements
- The approach is still a **useful tuning tool** for a single dataset

### Open Research Questions
1. How to give per-query insights without overwhelming context?
2. Use full MSMarco dataset — how to avoid context exhaustion?
3. Perhaps queries and results need to be treated as a knowledge base with subagents?

---

## Related
- Previous article: [Agentic code generation to optimize a search reranker](https://softwaredoug.com/blog/2025/10/19/agentic-code-generation-to-optimize-a-search-reranker) (2025-10-19)
- GitHub: [search-experiments](https://github.com/softwaredoug/search-experiments)
- Maven course: [Autoresearch workshop](http://maven.com/softwaredoug/autoresearch)
- Talk: Haystack Conf 2026
