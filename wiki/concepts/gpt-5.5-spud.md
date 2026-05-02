---
title: "GPT-5.5 \"Spud\""
type: concept
tags:
  - model
  - openai
  - benchmark
  - ai-agents
status: active
created: 2026-04-27
updated: 2026-04-27
aliases: ["GPT-5.5 Spud", "Spud"]
sources:
  - https://openai.com/index/introducing-gpt-5-5/
  - https://venturebeat.com/technology/openais-gpt-5-5-is-here-and-its-no-potato-narrowly-beats-anthropics-claude-mythos-preview-on-terminal-bench-2-0/
  - https://en.wikipedia.org/wiki/GPT-5.5
---

# GPT-5.5 "Spud"

GPT-5.5 is the newest model in the GPT series, released April 23, 2026, codenamed internally **"Spud"**. It is the first fully retrained base model since GPT-4.5, co-designed with and served on **NVIDIA GB200 and GB300 NVL72 systems**.

See [[concepts/gpt-5.5]] for the general overview.

## Key Differentiators
- **Agency-first design:** Excels at multi-part autonomous tasks with minimal prompting — "understands intent faster, carries more of the work" (OpenAI)
- **Token efficiency:** Uses fewer tokens than GPT-5.4 for same Codex tasks; per-token latency matches GPT-5.4 despite higher capability
- **Self-optimizing infrastructure:** The model itself wrote custom load-balancing heuristics that improved token generation speed by **>20%**

## Benchmark Performance

| Benchmark | GPT-5.5 | Claude Opus 4.7 | Gemini 3.1 Pro |
|-----------|---------|----------------|----------------|
| **Terminal-Bench 2.0** | **82.7%** | 69.4% | 68.5% |
| **Expert-SWE (internal)** | **73.1%** | — | — |
| **GDPval (wins/tie)** | **84.9%** | 80.3% | 67.3% |
| **OSWorld-Verified** | **78.7%** | 78.0% | — |
| **FrontierMath T1–3** | **51.7%** | 43.8% | 36.9% |
| **FrontierMath T4** | **35.4%** | 22.9% | 16.7% |
| **GPQA Diamond** | **93.6%** | — | — |
| **Humanity's Last Exam** | 41.4% | **46.9%** | — |
| **SWE-bench Pro Public** | 58.6% | **64.3%** | 54.2% |
| **CyberGym** | **81.8%** | 73.1% | — |
| **Capture-the-Flag (internal)** | **88.1%** | — | — |
| **ARC-AGI-2 Verified** | **85.0%** | 75.8% | 77.1% |
| **BixBench** | **80.5%** | — | — |
| **GeneBench** | 25.0% | — | — |
| **Tau2-bench Telecom** | **98.0%** | — | — |
| **OfficeQA Pro** | **54.1%** | 43.6% | 18.1% |

- GPT-5.5 leads on **14 benchmarks** among publicly available models
- Claude Opus 4.7 leads on **4** (software engineering, reasoning without tools)
- Gemini 3.1 Pro leads on **2** (academic reasoning, financial analysis)

## Pricing

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|---------------------|---------------------|
| **GPT-5.5** | $5.00 | $30.00 |
| **GPT-5.5 Pro** | $30.00 | $180.00 |
| **GPT-5.4** | $2.50 | $15.00 |

- No "mini" or "nano" tiers for GPT-5.5 yet
- GPT-5.5 Thinking mode available in ChatGPT (extra compute for verification)
- API access delayed until April 24, 2026 due to additional safety safeguards
- Fast mode in Codex generates tokens 1.5× faster at 2.5× price premium

## Safety
- Classified as **"High"** (not Critical) under OpenAI's Preparedness Framework
- Deployed stricter classifiers for higher-risk cyber activity
- **Trusted Access for Cyber** program provides "cyber-permissive" license for verified security professionals
- GPT-5.5 Pro contributed a new proof about Ramsey numbers (verified in Lean)

## GPT-5.5 Pro
- Higher-precision variant for legal research, data science, advanced analytics
- Available from Pro ($100/mo) tier upward
- GeneBench: 33.2% (vs 25.0% standard GPT-5.5)
- Humanity's Last Exam (no tools): **43.1%**
- Used by early testers as a research partner — critiquing manuscripts, stress-testing arguments

## Early User Reactions
> "The first coding model I've used that has serious conceptual clarity." — **Dan Shipper**, CEO of Every
> "It genuinely feels like I'm working with a higher intelligence." — **Pietro Schirano**, CEO of MagicPath
> "GPT-5.5 is noticeably smarter and more persistent than GPT-5.4... stays on task for significantly longer without stopping early." — **Michael Truell**, Co-founder & CEO of Cursor

## Related Pages
- [[concepts/gpt-models]] — Full GPT model family overview
- [[concepts/gpt-5.5]] — General GPT-5.5 overview
- [[concepts/gpt-model-milestones]] — History of GPT model generations
