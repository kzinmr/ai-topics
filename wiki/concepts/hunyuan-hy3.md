---
title: Hunyuan Hy3
created: 2026-06-14
updated: 2026-06-14
type: concept
tags:
  - concept
  - model
  - open-source
  - moe
  - reasoning
  - coding-agents
  - agentic-search
sources: [raw/articles/2026-06-14_tencent_hunyuan-hy3-moe.md]
---

# Hunyuan Hy3

**Hunyuan Hy3** is Tencent's flagship open-source Mixture-of-Experts (MoE) language model, released as the Hy3 Preview in April 2026. It represents a major architectural and capability leap over previous Hunyuan models, built on entirely rebuilt pre-training and reinforcement learning infrastructure.

## Architecture

| Property | Specification |
|---|---|
| Architecture | Mixture-of-Experts (MoE) |
| Total Parameters | 295B |
| Activated Parameters | 21B |
| MTP Layer Parameters | 3.8B |
| Number of Layers (excl. MTP) | 80 |
| Number of MTP Layers | 1 |
| Attention Heads | 64 (GQA, 8 KV heads, head dim 128) |
| Hidden Size | 4096 |
| Intermediate Size | 13312 |
| Context Length | 256K |
| Vocabulary Size | 120,832 |
| Number of Experts | 192 experts, top-8 activated |
| Supported Precisions | BF16 |

The 295B-total / 21B-active ratio yields high capacity with inference efficiency. The model uses Multi-Token Prediction (MTP) with a single 3.8B-parameter MTP layer for speculative decoding, supported in both vLLM and SGLang deployment configurations.

## Rebuilt Infrastructure

Starting February 2026, Tencent rebuilt its pre-training and RL infrastructure around three principles:

1. **Well-rounded capabilities** — balancing reasoning, long-context, instruction following, and tool use
2. **Authentic evaluation** — moving beyond standard benchmarks toward real-world performance
3. **Product-driven integration** — co-designing model and inference with business applications for cost efficiency

Hy3 Preview is the first model trained on this rebuilt infrastructure and the strongest Tencent has shipped to date.

## Benchmark Results

### Pre-trained Base Model

Compared against Kimi-K2 BASE (1043B/32B active), DeepSeek-V3 BASE (671B/37B active), and GLM-4.5 BASE (355B/32B active):

| Category | Benchmark | Hy3-Base | Best Competitor |
|---|---|---|---|
| English | MMLU (5-shot) | 87.42 | Kimi-K2: 88.24 |
| English | MMLU-Pro (5-shot) | 65.76 | Kimi-K2: 65.98 |
| English | SuperGPQA (5-shot) | **51.60** | Kimi-K2: 51.10 |
| Code | CRUXEval-I (3-shot) | **71.19** | GLM-4.5: 68.51 |
| Code | LiveCodeBench-v6 (1-shot) | **34.86** | Kimi-K2: 30.86 |
| Math | GSM8K (4-shot) | **95.37** | Kimi-K2: 93.46 |
| Math | MATH (4-shot) | **76.28** | Kimi-K2: 71.20 |
| Math | CMath (4-shot) | **91.17** | Kimi-K2: 90.83 |
| Multilingual | MMMLU (5-shot) | **80.15** | DeepSeek-V3: 79.54 |
| Multilingual | INCLUDE (5-shot) | **78.64** | DeepSeek-V3: 77.86 |

Despite having the fewest activated parameters (21B vs 32-37B), Hy3-Base leads in math, multilingual, and several coding benchmarks.

### Instruct Model: STEM and Reasoning

Hy3 Preview performs strongly on challenging STEM benchmarks including FrontierScience-Olympiad and IMOAnswerBench. It achieved excellent results in the Tsinghua Qiuzhen College Math PhD qualifying exam (Spring 2026) and the China High School Biology Olympiad (CHSBO 2025).

### Instruct Model: Context Learning and Instruction Following

Tencent built **CL-bench** and **CL-bench-Life** from its own business scenarios to measure context learning ability — the capacity to parse messy, lengthy contexts and follow complex rules. Hy3 Preview shows solid gains over previous models in these internally-developed measures.

### Instruct Model: Code and Agent

The largest gains were in coding and agent capabilities, driven by the rebuilt RL infrastructure and larger-scale training tasks:

- **SWE-bench Verified** — competitive scores against other open-source models
- **Terminal-Bench 2.0** — strong coding agent performance
- **BrowseComp** and **WideSearch** — competitive search agent benchmarks
- **ClawEval** and **WildClawBench** — practical agent scenario evaluation
- **Internal benchmarks**: Hy-Backend (backend tasks), Hy-Vibe Bench (real-user dev workflows), Hy-SWE Max — scores competitively against other open-source models

## Deployment

Hy3 Preview supports multiple inference frameworks:

- **vLLM**: Served with tensor parallelism (8 GPUs), MTP speculative decoding, tool-call parser, and reasoning parser
- **SGLang**: EAGLE speculative decoding, MTP enabled

Recommended GPU: H20-3e or higher memory capacity GPUs for 8-GPU deployment. Recommended parameters: `temperature=0.9`, `top_p=1.0`. Supports reasoning effort modes (`no_think`, `low`, `high`) for controlling chain-of-thought depth.

## Training and Quantization

- **Full fine-tuning and LoRA** supported via DeepSpeed ZeRO configurations and LLaMA-Factory integration
- **AngelSlim** toolkit for model compression: common quantization algorithms, low-bit quantization, speculative sampling

## Comparison to Previous Hunyuan Models

Hy3 represents a generational leap over Hy2, driven by the rebuilt infrastructure:

- Enhanced reasoning across STEM, math, and coding domains
- Dramatically improved agent capabilities (coding agents, search agents)
- Rebuilt RL pipeline enabling larger-scale training tasks
- Inference efficiency improvements from model-inference co-optimization
- Real-world product gains: 20% generation success rate increase vs Hy2 in Tencent Docs AI PPT; TTFT reduced 54% and end-to-end latency reduced 47% in CodeBuddy/WorkBuddy

## License

Released under the **Tencent Hy Community License**.

## Related

- [[entities/tencent-hy3]] — Entity page with pricing, OpenRouter analysis, and product integration details
- [[concepts/mixture-of-experts]] — MoE architecture overview
- [[concepts/open-source-ai]] — Open-source AI movement
- [[entities/tencent]] — Tencent company page
- [[entities/deepseek]] — Competing MoE model provider
- [[concepts/agentic-search]] — Agentic search capabilities
