---
title: "What We Learned from a Year of Building with LLMs (Part I): Tactical"
source: "https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/"
authors: ["Eugene Yan", "Bryan Bischof", "Charles Frye", "Hamel Husain", "Jason Liu", "Shreya Shankar"]
date: 2024-05-28
tags: [llm, production, prompting, rag, evals, flow-engineering, oreilly]
---

# What We Learned from a Year of Building with LLMs (Part I): Tactical

Published by O'Reilly Media, June 2024. Co-authored by **Eugene Yan, Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, and Shreya Shankar**.

This report distills tactical lessons from six industry experts who spent a year moving LLM projects from demo to production. Focuses on the "nuts and bolts" of the emerging LLM stack: prompting, RAG, workflow engineering, and evaluation.

---

## 1. Prompting Tactics
Prompting is often underestimated (it can go very far) and overestimated (it requires significant engineering to be robust).

### Fundamental Techniques
- **N-Shot Prompts:** Provide >=5 examples to align outputs. Ensure examples represent the expected input distribution.
- **Chain-of-Thought (CoT):** Encourage the model to explain its process. Be specific — instead of just "think step-by-step," instruct: "1. List decisions in a sketchpad, 2. Check for consistency, 3. Synthesize."
- **Structured Inputs/Outputs:** Use Instructor (for APIs) or Outlines (for self-hosted models). Model preferences: Claude prefers XML; GPT favors Markdown and JSON.

### The "God Prompt" Anti-Pattern
Avoid massive, 2,000-token prompts that try to handle every edge case. **Solution:** Break complex tasks into a pipeline of small, focused prompts (e.g., one for extraction, one for checking, one for summarizing).

### Pre-filling Claude's Response
Guide Claude by starting its response — e.g., `{"role": "assistant", "content": "<response><name>"}`

---

## 2. Information Retrieval & RAG
RAG is generally preferred over fine-tuning for adding new knowledge: cheaper, easier to update, more transparent.

### Key Quality Factors
1. **Relevance:** Measure using Mean Reciprocal Rank (MRR) or NDCG.
2. **Information Density:** Prefer concise, high-signal documents over "fluffy" ones.
3. **Detail:** Including metadata (like SQL column descriptions) significantly improves performance.

### The Hybrid Search Baseline
"Vector embeddings do not magically solve search... Making a genuine improvement over BM25 or full-text search is hard." — Aravind Srinivas, CEO Perplexity.ai
- **Recommendation:** Use Keyword Search (BM25) for names, acronyms, IDs; use Embeddings for synonyms and multimodality.

### Why Long Context Won't Kill RAG
Even with 10M token windows (Gemini 1.5), RAG remains relevant because:
- **Cost:** Inference cost scales with context length.
- **Reasoning:** Models can still be overwhelmed by "distractors" in massive contexts.

---

## 3. Tuning and Workflow Optimization
Moving from a single prompt to a flow can yield massive accuracy gains (e.g., AlphaCodium increased GPT-4 accuracy from 19% to 44% using multi-step flows).

### Flow Engineering Tips
- **Prioritize Determinism:** Use agents to generate a plan (DAG or state machine), then execute deterministically.
- **Diversity Beyond Temperature:** Shuffle input order, vary prompt phrasing, maintain a "recent output" list.
- **Caching:** Use unique IDs to cache responses for static content, eliminating latency/cost.

---

## 4. Evaluation & Monitoring
Evaluation is the most critical part of the LLM lifecycle.

### The "Intern Test"
If an average college intern couldn't do the task given the same context + 10 minutes, the LLM will likely fail.

### LLM-as-Judge Best Practices
- **Pairwise Comparison:** Ask "Is A or B better?" rather than "Rate A from 1-10."
- **Swap Positions:** Run the eval twice, swapping order of A and B to account for position bias.
- **Allow Ties:** Don't force a choice if both are equal.

### Assertion-Based Testing
Create unit tests based on real production samples. Check for: phrase inclusion/exclusion, word counts, or execution-evaluation (if the LLM writes code, does it actually run?).

### The Hallucination Problem
Hallucinations occur at a baseline rate of 5-10%. Even with heavy optimization, it is difficult to drop below 2%. **Defense:** Use Factual Inconsistency Guardrails downstream.
