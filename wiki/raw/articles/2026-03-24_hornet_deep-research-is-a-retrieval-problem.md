# Deep research is a retrieval problem

- **Source**: https://hornet.dev/blog/deep-research-is-a-retrieval-problem
- **Author**: Jo Kristian Bergum
- **Date**: March 24, 2026
- **Reading time**: 6 min
- **Series**: Part 1 of a series on agentic retrieval
- **Tags**: deep research, BrowseComp-Plus, retrieval bottleneck, BM25, oracle retrieval

## Summary

Why retrieval is a dominant bottleneck in BrowseComp-Plus.

BrowseComp-Plus is a multi-hop question answering benchmark for agents. Questions are designed to require evidence from multiple documents across a fixed corpus of **100,195 web pages**, about **736 million GPT-4.1 tokens** in total. The benchmark also includes human-annotated evidence documents for each answer. Its headline number looks like a measure of end-to-end reasoning. A closer look suggests that **retrieval is a dominant bottleneck** in the benchmark.

The clearest evidence comes from the paper's **oracle retrieval setting**, where the agent is prompted with all labeled positive documents up front instead of having to find them itself. This isolates what happens when retrieval is effectively perfect.

### Key Oracle Numbers

| Setting | Model | Accuracy |
|---------|-------|----------|
| Oracle (perfect retrieval) | GPT-4.1 | **93.49%** |
| Weak BM25 baseline | GPT-4.1 | **14.58%** |
| Oracle (perfect retrieval) | Qwen3-32B | **83%** |
| Search tool | Qwen3-32B | **<5%** |

That **~79-point gap** (GPT-4.1) and **~78-point gap** (Qwen3-32B) is hard to explain without retrieval playing a major role.

---

## Why this benchmark is hard

BrowseComp-Plus is not a deep-research benchmark in the sense of producing long reports or summaries. The answers are **short and verifiable**, often just a person's name, a date, or a currency amount. What makes the task difficult is that the questions are **densely multi-hop** and usually require evidence from multiple documents across the fixed corpus.

### Example Question

> *Could you provide the name of the individual who: as of December 2023, was the coordinator of a research group founded in 2009; co-edited a book published in 2018 by Routledge; had a co-editor who was a keynote speaker at a conference in 2019; served as the convenor of a panel before 2020; published an article in 2012; and completed their PhD on the writings of an English writer.*

### Corpus Characteristics

- **100,195 web pages**, ~736M GPT-4.1 tokens
- Each question: avg **6.1 evidence documents**, **2.9 gold documents**, **76 hard negatives**
- A 128k context window holds only ~0.017% of the corpus
- A 1M context window holds only ~0.14%
- Snippets truncated to **512 tokens** in standard evaluation — answer may be in the retrieved document but past the visible window

## Retrieval is a dominant bottleneck

Three signals converge:

1. **Oracle gap**: GPT-4.1 goes from 93.49% (oracle) → 14.58% (BM25)
2. **Model-agnostic**: The same gap appears with Qwen3-32B (83% → <5%)
3. **One-shot retrieval**: Weak lexical retrieval leaves large share of evidence undiscovered; stronger embedding-based retrieval brings more into view

## What the leaderboard number compresses

The leaderboard shows one number, but it compresses **three distinct evaluation layers**:

| Layer | What it measures |
|-------|-----------------|
| **One-shot retrieval quality** | What the retriever returns for the full question as a single query. Standard IR metrics: Recall@5/100/1000, nDCG@10. |
| **Session-level recall** | Cumulative set of evidence documents retrieved across ALL queries the agent makes. A retriever that looks strong in one-shot can still perform poorly if the agent formulates weak queries. |
| **End-to-end judged accuracy** | The headline number. Can the system return the correct answer? Right documents retrieved ≠ correct answer (512-token snippet truncation, reasoning extraction failures). |

Each layer isolates a different part of the system. The headline number alone does not tell you what is actually constraining performance.

## What the benchmark makes clear

BrowseComp-Plus is useful because it breaks a vague idea of "deep research" into concrete layers: **query formulation, retrieval, context exposure, and answer extraction**. Performance depends on all of them, but **retrieval is central** because it determines what evidence the model ever gets a chance to use.

---

## Series

- **Part 2**: [This is what agentic retrieval looks like](https://hornet.dev/blog/this-is-what-agentic-retrieval-looks-like) — analyzes 19,279 search calls across 830 questions, phrase search in 98% of sessions
- **Part 3**: Why BM25 looks weak in one-shot retrieval but considerably stronger inside the agent loop
- **Part 4**: What happens when you put the best retrieval strategies together
