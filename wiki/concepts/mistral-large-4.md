---
title: "Mistral Large 4 (ML4)"
type: concept
created: 2026-10-25
updated: 2026-10-25
tags: [mistral, model, open-source, multimodal, frontier-models, code-model, reasoning, cybersecurity, infrastructure]
sources:
  - "https://mistral.ai/news/mistral-large-4/"
  - "[[raw/articles/2026-10-06_mistral-ai_mistral-large-4-announcement]]"
confidence: medium
related:
  - "[[entities/mistral-ai]]"
  - "[[concepts/mixture-of-experts]]"
  - "[[concepts/multimodal]]"
  - "[[concepts/sovereign-ai]]"
  - "[[concepts/open-weight-vs-closed-llm-gap]]"
---

# Mistral Large 4 (ML4)

**Mistral Large 4** (internal codename **ML4**, nickname **"le Chonk"**) is Mistral AI's flagship model, announced as a **public preview on 2026-10-06** with open weights promised by the **end of October 2026**. Mistral describes it as "the most powerful open-weight model developed in the US or Europe" and its largest and most capable model to date.

## Model card

| Property | Value |
|---|---|
| Parameters | **1 trillion** total, **52B active** (sparse [[concepts/mixture-of-experts]]) |
| Modality | Natively **multimodal** (text + vision input) |
| Type | Open-weight hybrid **instruct-and-reasoning** MoE (instruction + reasoning + agentic in one model) |
| Languages | 160+ (incl. every official EU language) |
| Training | From scratch on **3,800 NVIDIA Grace Blackwell GPUs** in Mistral's own EU datacenters |
| License | Open weights (end of Oct 2026) |
| Funding | First milestone on the roadmap funded by Mistral's **€3B Series D** (largest EU tech equity round ever) |

The model is positioned as the foundation for a **new generation of specialized/optimized Mistral models**. Post-training methodology, architecture details, and more benchmarks were withheld pending weight release.

## Sovereignty positioning

ML4 is Mistral's clearest statement of the [[concepts/sovereign-ai]] thesis in a frontier model: state-of-the-art capability in critical verticals, delivered through open weights and **self-deployment**, including a European deployment Mistral operates **end-to-end under European law**, independent of other digital service providers. Mistral frames provider-level refusals as themselves a security risk — "losing access to a capability mid-incident can itself become a critical security risk" — arguing open weights + self-hosting give organizations autonomy to run advanced security work under their own policies.

## Benchmarks (Mistral-reported)

### Cybersecurity (headline)
- **Artificial Analysis Cyber Index**: top five globally; leads **non-China open-weight models by a wide margin**.
- Vulnerability reproduce-and-patch test: **82%** — highest of any model. **Claude Opus 5.5 and GPT-6 Astra score near zero on the same test because they refuse** the task.
- **Cybench** (40 security-competition exercises): **93%** solved.
- Despite strong cyber capability, **refusal rate on cyber prompts (JailbreakBench, StrongREJECT, AgentHarm) is higher than all open-weight models** — strong capability *without* weak moderation.
- Pre-release: red-teamed by cybersecurity leaders, vetted partners, and state authorities with reduced moderation + expanded cyber capabilities.

### Coding / agents
- DeepSWE v1.1 **61.7%**, SWE-Atlas-QnA **59.4%**, Terminal-Bench 4 **28.3%**.
- Combined Coding Agent Index **49.8%** — ahead of DeepSeek V4 Pro 0813 and Qwen3.8 Max.
- **Surge AI blind human eval** (1–5, identities hidden): ML4 **3.74**, 2nd of 5 — ahead of Kimi K3 (3.59), GLM-5.3 (3.60), GLM-5.2 (3.40); behind Claude Opus 5 (4.22).
- **AutomationBench** (657 business workflows): **59.9%**; **AA-Briefcase** long-horizon knowledge work **1,393 Elo**.

### Multimodal / vision
- Visual grounding **Dense 200: 42% vs 41% GPT-6-Astra**. Grounds dense scenes, verifies mechanical parts in technical drawings, retrieves PDF evidence, scans gigapixel geospatial imagery (disaster response, engineering).

### Science / math / finance / law
- **SciCode-Verified**: state of the art among open weights; one-shot **Hartree–Fock simulation**.
- **vals.ai** third-party eval: exceeds GPT-6-Astra on legal and financial tasks; **HarveyAI Legal Agent** benchmark: outperforms all open-source models.
- **FinWorkBench** spreadsheet F&A tasks.

### Safety
- Saturated robustness-to-indirect-[[concepts/prompt-injection]] benchmarks; **Lakera B3**: resists **93.3%** of attacks (highest reported).
- **KORA Benchmark**: **1.691** (max 2 = "Exemplary").

## Reinforcement learning at scale

Mistral's post-training RL library uses a **shared, composable interface**: one training run combines single-turn chat, scientific problem solving, safety alignment, factuality, and long-horizon tool use; environments share scaffolds (code sandboxes, web search, APIs) and verification (reward models, unit tests, LLM judges, static checks). An autoscaling actor fleet generates tens of thousands of parallel rollouts while training runs **asynchronously**, supporting **million-token rollout budgets** with multiple compactions at low staleness, minimizing off-policy drift. At the current **3k-GPU** scale a single run yields **~33B tokens/day**, ~16B of them trainable completion tokens. See [[concepts/post-training/rlvr]].

## Significance

ML4 is the first 1T-param open-weight frontier model from a **European** lab trained on European infrastructure, and the most direct open-weight challenge to the Claude/GPT frontier on cybersecurity — where closed-model refusals create a capability gap open weights deliberately close. The pre-release refusal posture (high refusal on malicious cyber prompts despite low-refusal defensive capability) is an explicit attempt to separate *defensive* cyber capability from *offensive* misuse, a tension explored in [[concepts/ai-vulnerability-discovery]].

## See also
- [[entities/mistral-ai]] — the company
- [[concepts/mistral-medium-3-5]] / [[concepts/mistral-ocr-4]] — earlier Mistral releases
- [[concepts/mixture-of-experts]] — architecture
- [[concepts/multimodal]] — vision-language models
- [[concepts/sovereign-ai]] — the strategic framing
- [[concepts/ai-vulnerability-discovery]] — cyber-capable model trade-off
- [[concepts/prompt-injection]] — robustness eval

## Sources
- [Introducing Mistral Large 4 — Mistral AI (2026-10-06)](https://mistral.ai/news/mistral-large-4/)
- Raw: [[raw/articles/2026-10-06_mistral-ai_mistral-large-4-announcement]]
