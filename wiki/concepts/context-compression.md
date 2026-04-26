---
title: "Context Compression Techniques"
created: 2026-04-18
updated: 2026-04-18
type: concept
tags: [context-management, optimization, technique, inference]
sources: [raw/articles/crawl-2026-04-18-context-compression.md]
---

# Context Compression Techniques

Methods for reducing the size of context windows while preserving task-relevant information. Critical prerequisite for [[context-engineering]] — addresses the fundamental constraint that LLMs have finite context windows but applications need to provide ever-larger amounts of relevant information.

## Why Compression Matters

Context window limits create a hard constraint: you cannot fit everything. Compression determines **what gets dropped vs what survives**. Poor compression → lost critical information. Good compression → higher task success rates with fewer tokens.

## Three Compression Strategies

### 1. Summarization-Based Compression
Replace verbose content with shorter summaries that preserve key facts.

```python
def compress_context(context: str, target_size: int) -> str:
    # Use smaller/cheaper model for summarization
    summary = llm.generate(
        f"Summarize the following in {target_size} tokens, preserving all key facts:\n{context}"
    )
    return summary
```

**Best for:** Long documents, conversation history, research papers
**Limitations:** Loses nuance, may omit critical details, adds latency for summarization pass

### 2. Retrieval-Based Compression
Keep only the most relevant chunks based on similarity to the current query.

```python
def retrieve_relevant_chunks(query: str, chunks: list, max_tokens: int) -> str:
    scored = [(chunk, embedding_similarity(query, chunk)) for chunk in chunks]
    scored.sort(key=lambda x: x[1], reverse=True)
    selected, total = [], 0
    for chunk, score in scored:
        if total + len(chunk) > max_tokens:
            break
        selected.append(chunk)
        total += len(chunk)
    return " ".join(selected)
```

**Best for:** RAG pipelines, large knowledge bases, document Q&A
**Limitations:** May miss cross-chunk relationships, depends on embedding quality

### 3. Structural Compression
Remove formatting, redundant phrases, and boilerplate while preserving information structure.

- Strip HTML/XML tags → plain text with headings
- Remove repeated instructions/system prompts
- Collapse multi-line code blocks to essential lines
- Replace verbose phrases with shorter equivalents ("in order to" → "to")

**Best for:** Code, structured data, technical documentation
**Limitations:** Minimal compression ratio (2-3x max), loses formatting context

## Compression Ratio vs Quality Trade-off

| Strategy | Typical Ratio | Quality Retention | Latency Impact |
|----------|--------------|-------------------|----------------|
| Summarization | 5-10x | 70-90% | High (extra LLM call) |
| Retrieval | 3-5x | 80-95% | Medium (embedding lookup) |
| Structural | 2-3x | 95-100% | Low (string ops only) |

## Advanced: Learned Compression

Research direction: train a small model specifically to compress context for a target LLM.

```python
# Concept: compress then reconstruct
compressed = compressor_model(original_context)
reconstructed = target_llm(compressed)
loss = reconstruction_loss(reconstructed, ground_truth)
```

Early results show 3-5x compression with <5% quality loss on standard benchmarks (needle-in-haystack, long-context QA).

## Connection to Context Engineering

Context compression is the primary mechanism for [[context-engineering]] to work within window limits:
- **Without compression:** context fills up quickly, older information gets pushed out
- **With compression:** more relevant information fits in the same window
- **Trade-off:** compression latency vs context quality

Related: [[context-window-management]] discusses how to organize compressed context for maximum effectiveness.

## Related

- [[context-engineering]] — Parent concept, compression is a core technique
- [[context-window-management]] — How to organize compressed context
- [[token-economics]] — Compression reduces token costs
- [[harness-engineering/system-architecture/context-compaction]] — Context compaction in agent systems

## Sources

-  — Context compression techniques analysis
- OpenAI Cookbook, "Context engineering patterns" (2025)
- Anthropic, "Effective context engineering for AI agents" (2025)
