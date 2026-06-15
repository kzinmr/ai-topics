---
title: "Fine-Tuning — When, Why, and How (Post-Training)"
type: concept
tags:
  - fine-tuning
  - post-training
  - training
  - rag
  - prompting
  - evaluation
  - context-engineering
created: 2026-06-15
updated: 2026-06-15
aliases: [LLM Fine-Tuning, Model Fine-Tuning, SFT, When to Fine-Tune]
sources:
  - transcripts/2024-01-24_emeisen_why-fine-tuning-is-dead-lecture
  - raw/articles/2024-01-24_emeisen_why-fine-tuning-is-dead
  - concepts/context-engineering/context-rot
  - concepts/modern-retrieval-toolkit
  - concepts/knowledge-storage-spectrum
---

# Fine-Tuning — When, Why, and How

Fine-tuning is the process of continuing training on a pre-trained model using domain-specific or task-specific data. This page covers **when to fine-tune vs. use alternatives**, the decision hierarchy, and how the landscape evolved from 2024 to 2026.

> For the full catalog of fine-tuning techniques (SFT, LoRA, GRPO, etc.), see [[concepts/post-training/_index|Post-Training Overview]].

## Decision Framework: When to Fine-Tune vs Prompt

| Approach | Best For | Cost | Latency | When to Choose |
|----------|----------|------|---------|----------------|
| **Prompting** | Quick iteration, general tasks | Low | Variable | First thing to try. Always. |
| **Few-shot / Dynamic few-shot** | Pattern demonstration, edge case handling | Low | Variable | Prompt alone fails; add targeted examples via RAG over example DB |
| **RAG** | Knowledge injection, domain-specific facts | Low–Medium | Variable | Model lacks information (not capability). Most knowledge tasks. |
| **SFT** | Domain adaptation, format enforcement, style transfer | Medium | Low | Prompting + RAG plateau; need consistent output format or style |
| **PEFT/LoRA** | Task-specific specialization with limited compute | Medium | Low | SFT needed but GPU memory constrained; multi-adapter serving |
| **RL/GRPO** | Reasoning, verifiable domains (math, code, structured output) | High | Low | Need behavioral optimization, not knowledge injection; verifiable rewards exist |
| **Full fine-tuning** | Maximum performance, new capabilities | High | Low | Last resort; all other approaches exhausted |

## The Hierarchy of Needs (Ameisen, 2024)

Emmanuel Ameisen ([[entities/emmanuel-ameisen]]) articulated the canonical priority order for practical ML systems. This remains valid in 2026:

```
1. Evals first
   └─ Representative, large, easy-to-run eval sets
   
2. Work on prompts
   └─ "I've gotten people from 30% to 98% accuracy just by improving the prompt"
   
3. Dynamic few-shot examples
   └─ RAG over a database of examples; pull the most relevant ones
   
4. RAG / context injection
   └─ For knowledge the model doesn't have
   
5. Fine-tuning (consider last)
   └─ Only after all above are exhausted and measured
```

> *"If you talk to me, I will only allow you to do fine-tuning if you've done all of this first."* — Emmanuel Ameisen

### The 80% Rule

Regardless of whether you fine-tune, **80% of ML work is data work** — collecting, labeling, enriching, cleaning, and debugging data. The failure mode is skipping this and going straight to fine-tuning as a "side quest."

| Activity | % of Time |
|----------|----------|
| Data work (collect, label, enrich, clean, debug) | 80% |
| General engineering (serve, monitor, drift detection) | 18% |
| Debugging (model won't train, GPU issues) | 2% |
| Architecture research | 0% |

## Fine-Tuning Is Not for Adding Knowledge

The most common misconception: "our model doesn't know about X, so we need to fine-tune it."

**Reality**: If the model lacks information, the solution is **RAG or prompting** — not fine-tuning. Fine-tuning on knowledge data typically produces:
- **Surface-level pattern matching**: The model learns to mention the fact when asked the specific question from the training data, not to truly "know" it
- **Poor generalization**: "Emmanuel likes strawberries" fine-tuned on Q&A pairs only triggers on that exact question format
- **Marginal gains over RAG**: Papers comparing fine-tuning vs RAG consistently show RAG delivers ~90% of the improvement; fine-tuning adds 1-2% marginal gains (Ameisen, 2024)

### What Fine-Tuning *Is* Good For

| Use Case | Why Fine-Tuning Helps |
|----------|----------------------|
| **Style / format enforcement** | Consistent output structure (JSON, XML, specific tone) |
| **Behavioral optimization** | GRPO/RLVR for reasoning chains, code generation |
| **Latency optimization** | Distill large model behavior into smaller, faster model |
| **Domain-specific retrieval** | Embedding model fine-tuning for specialized terminology (rare) |

### The Knowledge-Style Boundary Shifts

A key insight from Ameisen: **what requires fine-tuning today can often be done with a prompt tomorrow.** Learning a "style of speaking" used to require fine-tuning; newer models learn it from a 2-line prompt. The boundary between "knowledge" and "style" is model-generation-dependent.

## The 2026 Landscape: What Changed Since 2024

### 1. Context Rot — Long Context ≠ Reasoning Capacity

Ameisen predicted that falling prices and growing context windows would eliminate fine-tuning. The first part came true (1M+ context is standard in 2026), but [[concepts/context-engineering/context-rot|Context Rot]] showed that **stuffing everything into context doesn't work**:

- LLM performance **degrades** as context length increases, even within supported limits
- Models maintain lexical matching ("needle in haystack") but fail on **semantic queries**
- Failure modes vary: GPT hallucinates, Claude abstains, Gemini produces noise

**Implication**: The "just throw everything in context" strategy has hard limits. RAG remains essential — not as a workaround for small windows, but as a **precision tool** that provides only relevant context to avoid rot.

### 2. Naive RAG Is Dead, Retrieval Is Not

The "RAG is dead" discourse (2025) clarified that **naive single-vector RAG** is what died. Modern retrieval evolved:

| Old (2023) | Modern (2026) |
|-----------|---------------|
| Single-vector embedding | ColBERT (late interaction), multi-vector |
| Cosine similarity only | BM25 + embedding hybrid |
| Static chunk retrieval | Agentic retrieval (LLM-driven query expansion) |
| One-shot retrieval | Multi-step, recursive retrieval |

See [[concepts/modern-retrieval-toolkit]] for the full toolkit.

### 3. Fine-Tuning Evolved: SFT → GRPO/RFT

Fine-tuning didn't die — it **transformed**. The 2024 paradigm (SFT on instruction pairs) gave way to:

- **GRPO** (Group Relative Policy Optimization): Compare completions within groups, optimize toward verifiable rewards. Dominant for reasoning tasks.
- **RFT** (Reinforcement Fine-Tuning): Production traces + LLM-as-Judge scoring. See [[concepts/post-training/reinforcement-fine-tuning]].
- **RLVR** (RL with Verifiable Rewards): Automatic verification for math, code, structured output. See [[concepts/post-training/rlvr]].

The shift: from "teach the model by example" (SFT) to "let the model explore and optimize toward outcomes" (RL).

### 4. The Knowledge Storage Spectrum

All forms of LLM knowledge exist on a single spectrum:

```
Model Weights ←→ KV Cache ←→ RAG Retrieval ←→ In-Context Prompts
   (persistent)    (session)    (dynamic)         (ephemeral)
   (expensive)     (medium)     (medium)          (cheap)
   (slow update)   (fast)       (fast)            (instant)
```

Fine-tuning = encoding knowledge into weights. RAG = encoding knowledge into retrieval. Prompting = encoding knowledge into context. The choice is an **economic and operational trade-off**, not a technical absolute.

See [[concepts/knowledge-storage-spectrum]] for the full framework.

## When Fine-Tuning Still Makes Sense (2026)

| Scenario | Recommended Approach |
|----------|---------------------|
| Model doesn't know about your product | RAG (not fine-tuning) |
| Need consistent JSON output format | Prompting first; SFT if insufficient |
| Math/code reasoning with verifiable answers | GRPO/RLVR |
| Speed-critical: distill frontier model → small model | SFT distillation |
| Domain-specific embedding search | Embedding fine-tuning (rare) |
| 500 examples that fit in 5K context | Just put them in the prompt |
| 100K+ proprietary documents | RAG + hybrid search |
| Style/tone enforcement | Prompting (newer models); SFT (older models) |

## Sources

- [[transcripts/2024-01-24_emeisen_why-fine-tuning-is-dead-lecture]] — Ameisen's original talk
- [[raw/articles/2024-01-24_emeisen_why-fine-tuning-is-dead]] — Summary article
- [[concepts/context-engineering/context-rot]] — Context Rot (Chroma/Kelly Hong, 2025)
- [[concepts/modern-retrieval-toolkit]] — Modern retrieval (Ben Clavié, 2025)
- [[concepts/knowledge-storage-spectrum]] — Unified framework
- [[concepts/rag-not-dead-series]] — "RAG Is Not Dead" 7-part series (Hamel Husain, 2025)
- [[concepts/post-training/reinforcement-fine-tuning]] — RFT methodology
- [[concepts/post-training/grpo]] — GRPO fundamentals
