---
title: "Thinking Machines Lab"
type: entity
created: 2026-07-11
updated: 2026-07-11
tags:
  - company
  - ai-research
  - model
  - fine-tuning
  - alignment
  - open-source
  - ai-safety
  - sovereign-ai
  - human-in-the-loop
sources:
  - raw/articles/thinkingmachines.ai--blog-the-future-worth-building-is-human--7fe53b6e.md
---

# Thinking Machines Lab

**Thinking Machines Lab** is an AI company whose mission is to "build AI that extends human will and judgment." The company advocates for **decentralized AI** — models as diverse and distributed as the people they serve — rather than centralized, one-size-fits-all frontier models.

## Philosophy

### Core Thesis
- AI exists to serve human work, which runs on **tacit, local, fleeting knowledge** held privately by individuals
- Central planning fails because of the nature of productive knowledge (citing Hayek's *The Use of Knowledge in Society*, 1945)
- For AI to benefit from distributed knowledge, **AI itself must be distributed**
- "AI that extracts a snapshot of knowledge and replaces it with a standard offering" is the wrong model; the right model **cultivates** unique knowledge through ongoing collaboration

### Against Centralized Alignment
- A single locus of value alignment becomes a **locus of power** to be captured
- "A more moral AI is not enough if that morality is determined by a few" — Leo XIV, *Magnifica Humanitas* (2026)
- Each lab training its next model on its previous model's outputs creates **homogeneity** and suppresses diversity
- They envision alignment as a feature of an **ecosystem of AIs** raised in different places, disagreeing, competing, and learning from each other

## Technical Directions

1. **Strong models**: Advancing multimodal interaction and customizability at the frontier
2. **Customization tools**: Enabling people to fine-tune models with their unique knowledge, including the ability to **train model weights**
3. **Interaction models**: Models that handle live, multimodal interaction natively (not bolt-on scaffolding) — "People collaborate best when they collaborate live"
4. **Published research**: For the scientific community, because "the power to shape AI requires deep understanding of how it's made"


## Inkling Model

**Inkling** is Thinking Machines Lab's first full LLM release (July 2026), a multimodal mixture-of-experts model under Apache 2.0. It marks the company's transition from philosophical positioning to concrete model deployment.

### Model Specifications

| Spec | Value |
|------|-------|
| Total Parameters | 975B |
| Active Parameters | 40-41B per token |
| Architecture | Decoder-only MoE with shared expert sink |
| Context Window | 1M tokens |
| Training Data | 45T tokens |
| License | Apache 2.0 |
| Training Hardware | NVIDIA GB300 NVL72 |
| Modalities | Text, image, audio inputs → text outputs |

### Architecture Innovations

- **Hybrid Attention** (5:1 ratio): Every 6 attention layers consist of 5 sliding-window local-attention layers followed by 1 full-attention global layer. This maximizes compute efficiency by focusing most attention on recent context while periodically integrating full-sequence information.
- **Query-Conditioned Relative Attention**: Instead of RoPE or absolute position embeddings, Inkling incorporates token position through a learned, query-conditioned relative bias per attention layer. Each layer computes an additional attention score based on the relative distance between tokens.
- **Sconv (Short Causal Convolutions)**: Lightweight channelwise causal convolutions with a 4-token receptive field, applied to key/value streams before attention and to attention/FFN sublayer outputs. Provides local token mixing without the cost of full attention.
- **Shared Expert Sink MoE**: The router selects a small number of routed experts per token while also assigning weight to shared experts. Unlike conventional shared-expert MoE designs, Inkling normalizes shared and routed experts together, allowing the shared path to dynamically compete for mixture weight on each token.

### Benchmarks

Inkling achieves an **Intelligence Index of 41**, surpassing [[entities/NVIDIA|NVIDIA]]'s Nemotron 3 Ultra (38) as the best-performing US-based open-weights model. It demonstrates strong performance across graduate-level scientific reasoning, competition mathematics, software engineering, browser-based tasks, visual document understanding, and audio comprehension. Inkling is also post-trained on forecasting and calibrated prediction tasks.

### Variants

| Variant | Size | Status |
|---------|------|--------|
| Inkling | 975B-A41B | Full release |
| Inkling-Small | 276B-A12B | Preview |

### Ecosystem Support (Day 0)

Inkling received broad day-0 ecosystem support from major inference and development platforms:
- **Inference**: [[entities/together-ai|Together AI]] (serverless, FlashAttention-4 kernel), [[concepts/modal|Modal]] (Managed Endpoints, 250 tok/s/user on 8×B200 with DFlash speculation), Baseten, Databricks, Hugging Face
- **Open-source frameworks**: [[concepts/vllm|vLLM]], [[concepts/sglang|SGLang]], Unsloth Studio (local deployment with tool calling)
- **Quantization**: [[entities/daniel-han|Unsloth]] produced 1-bit GGUF quants (86% smaller, 74.2% accuracy retention), enabling consumer-hardware deployment

### Inference Performance

On Modal's infrastructure (8× B200 GPUs), Inkling achieves 250 tokens/second per user at 2.5M TPM per-GPU throughput — 67% faster than the model's built-in speculative decoding path at matched throughput. Modal's DFlash block-diffusion speculator, tuned to Inkling's local-attention layout, enables flat-cost speculation as batch size grows.

### Related Pages
- [[concepts/inkling]] — Dedicated Inkling concept page
- [[concepts/open-source-llms]] — Open-source LLM landscape

## Key Arguments

### Human Participation as Technical Challenge
- The bottleneck for human-AI collaboration is the **communication channel** — "a small text box and a long wait"
- They bet on interaction models where interactivity scales with intelligence
- Common AI benchmarks (e.g., METR's task-completion time horizons) measure what AI can do **alone**, not what people and machines accomplish **together**

### Decentralized Ownership
- Organizations should **own and tailor** AI to their goals, not rent it
- An AI lab offering a single model benefits by absorbing what makes each user distinct
- "The best organizations will make the fullest use of both [people and AI]"

### Safety Through Diversity
- Extending rights to **natural** things (animals, watersheds) produces positive spillovers for humans
- Extending personhood to **artificial** constructs (corporations) has been catastrophic
- They aim to give people stronger tools for shaping AI safely, not to take away ownership

## Notable References
- Michael Polanyi, *The Tacit Dimension* (1966) — tacit knowledge
- Friedrich Hayek, *The Use of Knowledge in Society* (1945) — distributed knowledge
- Hannah Arendt, *The Human Condition* (1958) — anthropocentric utilitarianism
- Gwern Branwen, *Guardian Angels: LLM Personalization for Productivity and Security* (2026)
- Luke Drago & Rudolf Laine, *The Intelligence Curse* (2025)
- John von Neumann, *Can We Survive Technology?* (1955)
- Toyota's Mitsuru Kawai (2014) — bringing expert craftsmen back to automated lines

## Related
- [[entities/anthropic]]
- [[entities/openai]]
- [[concepts/ai-safety]]
- [[concepts/fine-tuning]]
- [[concepts/alignment]]
- [[concepts/ai-industry-economics]]
