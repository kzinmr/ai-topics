---
title: Sebastian Raschka
type: entity
created: 2026-05-04
updated: 2026-08-12
status: complete
tags:
  - person
  - infrastructure
  - fine-tuning
  - model
  - education
aliases: [raschka]
sources:
  - https://sebastianraschka.com
  - https://magazine.sebastianraschka.com
  - https://x.com/rasbt
  - raw/newsletters/2026-07-15-llm-architecture-in-2026-agent-harnesses-hybrid-models-and-why-implementation-do.md
  - raw/newsletters/2026-08-03-if-developers-build-on-chinese-open-weight-models-who-leads-ai.md
  - raw/articles/2026-08-11_rasbt_meta-muse-glimmer-gemma-like.md
---

# Sebastian Raschka

| | |
|---|---|
| **Blog** | [sebastianraschka.com](https://sebastianraschka.com) |
| **Newsletter** | [Ahead of AI](https://magazine.sebastianraschka.com) |
| **X/Twitter** | [@rasbt](https://x.com/rasbt) |
| **GitHub** | [rasbt](https://github.com/rasbt) |
| **Role** | ML researcher, educator, author |
| **Known for** | LLM finetuning guides, LoRA tutorials, "Machine Learning with PyTorch and Scikit-Learn" |

## Overview

Sebastian Raschka is a prominent ML researcher and educator known for his practical, code-first approach to teaching deep learning and LLM finetuning. His "Ahead of AI" newsletter and blog posts provide some of the most actionable guidance on parameter-efficient fine-tuning (LoRA, DoRA), model evaluation, and post-training techniques.

## Key Resources (cited in GenAI Handbook)

- **"Parameter-Efficient LLM Finetuning With Low-Rank Adaptation (LoRA)"** — Practical LoRA tutorial with tips on rank selection, target modules, and dataset preparation
- **"Practical Tips for Finetuning LLMs Using LoRA"** — Follow-up with production-oriented advice
- **"LoRA and DoRA from Scratch"** — Deep dive into DoRA (decomposed LoRA variant)
- His blog posts are cited as 🟢 top-tier resources throughout the [[concepts/genai-handbook|GenAI Handbook]] (Section IV: Finetuning)

### New Publications and Insights
- **'Build a Reasoning Model (From Scratch)'** — A 440-page book published July 2026, following his earlier 'Build a Large Language Model (From Scratch)'. The book teaches building reasoning-focused LLMs from first principles.
- **Vanishing Gradients conversation** (July 15, 2026, with Hugo Bowne-Anderson): A wide-ranging technical discussion covering multi-head latent attention's KV cache advantages, RLVR vs process reward models, shrinking agent harnesses, intermediate tensor verification for architecture understanding, and fine-tuning economics. Upcoming live podcast on July 28, 2026.
- **Vanishing Gradients episode — "If Developers Build on Chinese Open-Weight Models, Who Leads AI?"** (Aug 3, 2026, with Hugo Bowne-Anderson): Recorded about an hour after Kimi K3's weights dropped, with Raschka already updating his architecture diagram. Topics: Kimi K3 architecture (Delta Attention / MoE), the same open-weight model behaving differently across Qwen Code / Claude Code / Codex / Pi harnesses (context handling, compaction), the harness choosing model + reasoning effort, router selection by task/history/context, the DeltaNet/Mamba-type architecture trend, the 25-company open letter (NVIDIA/Meta/Microsoft/HF etc.) and Anthropic's open-weight stance.
- **Current AI stack**: Mac mini, Codex, and Claude. Uses LLMs for proofreading, quality assurance, and cross-referencing (not for idea generation). Maintains a ~20-item Markdown checklist for article quality review.
- **Methodology**: Begins with working model releases, runs them inside agent systems and inspects their internals simultaneously. His test of complete understanding is reimplementing an architecture from published weights and matching intermediate tensors.
- **Muse Glimmer commentary** (Aug 11, 2026, [tweet](https://x.com/rasbt/status/2087180773497421926)): Characterized Meta's [[entities/muse-glimmer|Muse Glimmer]] as a 30B multimodal reasoning model with a Gemma-like architecture, framing it as Meta's first open-weight release "since the good old Llama days" and noting "Glimmer" is likely wordplay on "Spark." (690 bookmarks, ~1.5K likes)

## Related Wiki Pages

- [[concepts/peft-lora-and-qlora]] — LoRA concept page
- [[concepts/qlora]]
- [[concepts/genai-handbook]] — Evaluated as a top-tier resource
- [[concepts/fine-tuning]]
- [[concepts/post-training/rlhf-dpo-orpo-kto-preference-optimization]]
