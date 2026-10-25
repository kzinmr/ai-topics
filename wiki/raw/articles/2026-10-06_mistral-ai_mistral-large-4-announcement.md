---
title: "Introducing Mistral Large 4 (ML4, le Chonk)"
url: https://mistral.ai/news/mistral-large-4/
source: mistral-ai
source_name: Mistral AI
date: 2026-10-06
fetched_at: 2026-10-25
type: article
tags: [mistral, model, open-source, multimodal, code-model, cybersecurity]
author: Mistral AI (codename "Le Chonk")
status: complete
---

# Introducing Mistral Large 4

Official announcement of **Mistral Large 4** (internal codename **ML4**, nickname **le Chonk**), released as a **public preview** on 2026-10-06. Weights promised by **end of October 2026**.

## Model card

- **1 trillion parameters**, natively multimodal, **52B active parameters** (sparse MoE).
- Open-weight hybrid **instruct-and-reasoning MoE with multimodal input** — unifies instruction, reasoning, and agentic capabilities in a single model.
- Natively fluent in **160+ languages**, including every official EU language.
- Trained from scratch on **3,800 NVIDIA Grace Blackwell GPUs** in Mistral's own European datacenters. Public preview served on that same infrastructure.
- First milestone funded by the **€3 billion Series D** — the largest equity round ever raised by a European technology company.
- Positioned around **AI sovereignty**: state-of-the-art performance in critical verticals, delivered through open weights, self-deployment; a European deployment operated end-to-end by Mistral under European law, independent of other digital service providers.

## Pre-release safety posture

Until weights drop, Mistral is **red-teaming in real-world settings** with cybersecurity leaders, vetted partners, and state authorities who access the model with **reduced moderation and expanded cyber capabilities**.

## Benchmarks (per Mistral)

**Cybersecurity**
- Artificial Analysis **Cyber Index**: top five globally; leads non-China open-weight models by a wide margin.
- On the vuln-reproduce-and-patch test: **82%** — highest of any model. Notably Claude Opus 5.5 and GPT-6 Astra score **near zero on the same test because they refuse** the task.
- **Cybench** (40 security-competition exercises): **93%** solved.
- Refusal behaviour: on cyber prompts from JailbreakBench, StrongREJECT, AgentHarm, ML4's refusal rate is **higher than all OSS models** despite strong cyber performance.

**Coding / agents**
- DeepSWE v1.1: **61.7%**
- SWE-Atlas-QnA: **59.4%**
- Terminal-Bench 4: **28.3%**
- Combined Coding Agent Index: **49.8%** — ahead of DeepSeek V4 Pro 0813 and Qwen3.8 Max.
- Surge AI blind human eval (1–5 scale, identities hidden): ML4 Preview **3.74**, second of five — ahead of Kimi K3 (3.59), GLM-5.3 (3.60), GLM-5.2 (3.40); behind Claude Opus 5 (4.22).
- **AutomationBench** (657 business workflows across Gmail/Sheets/Slack/Salesforce): **59.9%**, ahead of Kimi K3, MiMo-V2.6-Pro, DeepSeek V4 Pro.
- AA-Briefcase (long-horizon knowledge work): **1,393 Elo**.

**Multimodal / vision**
- Visual grounding: surpasses GPT-6-Astra on **Dense 200 (42% vs 41%)**.
- Grounds dense natural scenes, verifies mechanical parts in technical drawings, retrieves evidence from PDFs, scans gigapixel satellite/geospatial imagery.

**Science / math**
- State of the art on **SciCode-Verified** among open-weight models.
- One-shot generation of a full **Hartree–Fock simulation** (multi-step chemistry task).
- Internal STEM eval vs GLM-5.3: preferred in CAD and STEM; on par/close in finance and coding.

**Finance / law**
- vals.ai third-party eval on representative legal & financial tasks — **exceeds GPT-6-Astra in both**.
- **HarveyAI Legal Agent** benchmark: outperforms all open-source models.
- **FinWorkBench** (spreadsheet creation/editing for real F&A use cases).

**Safety**
- Saturated Mistral's benchmarks on **indirect prompt injection** robustness; **Lakera B3** AI Security Benchmark: resists **93.3%** of attacks (no higher competitor score).
- **KORA Benchmark**: **1.691** (max 2 = "Exemplary") — highest for Mistral among OSS.

## Reinforcement learning at scale (post-training)

Mistral details its RL library design:
- Shared, **composable interface** lets one training run combine single-turn chat, scientific problem solving, safety alignment, factuality, long-horizon tool use. Environments share scaffolds: code sandboxes, web search, external APIs.
- Verification composable too: reward models, unit tests, LLM judges, static checks.
- Runtime: autoscaling actor fleet generating tens of thousands of parallel rollouts while training proceeds **asynchronously**; optimized for long trajectories, rollout budgets of **millions of tokens** across multiple compactions with low staleness; minimizes off-policy drift.
- Current scale: **3k GPUs → ~33B tokens/day**, of which **~16B trainable completion tokens** after filtering/masking.
- Post-training = SFT + RL; both stages contribute to eval gains.

## Roadmap statement

Weights to be released end of October 2026 with architecture details, additional benchmarks, and post-training methodology. ML4 is the base for a new generation of specialized/optimized Mistral models. RL run behind the preview still in flight, no signs of saturation.
