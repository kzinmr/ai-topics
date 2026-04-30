---
title: "P1: I don't use RAG, I just retrieve documents"
source: https://hamel.dev/notes/llm/rag/p1-intro.html
author: Hamel Husain (featuring Benjamin Clavié)
date: 2025
type: article
---

# P1: I don't use RAG, I just retrieve documents

**Author:** Hamel Husain (featuring Benjamin Clavié)
**Topic:** The evolution of Retrieval-Augmented Generation (RAG) and why "naive" RAG is obsolete.

## 1. The Core Argument: "RAG is Dead" is a Myth

Benjamin Clavié argues that while the term "RAG" has been diluted by marketing, the underlying necessity of retrieval is more critical than ever.

- **The Misconception:** In 2023, "RAG" became synonymous with naive, single-vector semantic search. This specific, simplistic implementation is what is "dead" or obsolete.
- **The Reality:** RAG is simply the process of providing external documents to a generative model.
  > "Claiming RAG is dead because we're now using better retrieval tools is... akin to claiming HTML is dead because we are now using CSS."
- **The Definition:** If you add external documents to a context window to augment generation—even via manual copy-paste—you are technically performing RAG.

## 2. Why Naive Single-Vector Search Fails

The "2023-style" RAG relies on compressing entire documents into a single vector (~1000 dimensions):
- **Information Loss:** Massive compression inevitably drops nuances.
- **Domain Mismatch:** General-purpose embedding models are trained on public data (like Bing search), failing on specialized data like proprietary codebases.
- **The "SSD" Analogy:** Modern retrieval techniques are replacing naive RAG by being "better RAG."

## 3. Why Long Context Windows Won't Kill Retrieval

Despite models offering 1M+ token windows, retrieval remains essential:
1. **Scale:** 10M tokens is still insufficient for massive enterprise knowledge bases.
2. **Efficiency:** Prohibitively expensive and slow to "stuff" every document into every query.
3. **Model Intelligence vs. Storage:** LLM weights are frozen. Retrieval handles knowledge storage for up-to-date info.

## 4. The Modern Retrieval Toolkit

Effective systems combine multiple methods:
- **Traditional Tools:** `grep`, `wget`, `BM25`
- **Advanced Models:** ColBERT (Late-interaction), ModernBERT
- **Agentic Approaches:** Using reasoning and web search
- **Multi-vector models:** Vector for every token rather than one for the whole document

## 5. Upcoming Deep-Dives

| Topic | Expert | Key Focus |
|-------|--------|-----------|
| Modern Evals | Nandan Thakur | FreshStack (continuously updated benchmarks) |
| Reasoning | Orion Weller | Can retrievers "think" to improve selection? |
| Late-Interaction | Antoine Chaffin | ColBERT and ColPali |
| Multimodal | B. Bischof & A. Chaurasia | Graphs, tables, and images |

## 6. Key Takeaways
- RAG is not a single technology; it is a pipeline.
- Stop brute-forcing with a single vector.
- Retrieval is permanent: LLMs will always need external data.
- Hybrid is better: combining keyword search + semantic search + reasoning.
