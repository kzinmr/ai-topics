---
title: "Agent Execution Tax"
created: 2026-05-22
updated: 2026-08-05
type: concept
tags:
  - concept
  - ai-agents
  - evaluation
  - inference
  - harness-engineering
  - browser-agent
sources:
  - raw/articles/2026-05-21_fireworks-ai_agent-execution-tax.md
---

# Agent Execution Tax

The **Agent Execution Tax** is a metric and concept introduced by [[entities/fireworks-ai]] in May 2026, quantifying the overhead of structured output failures in multi-step agent loops. Based on 720 browser agent runs across 4 LLMs (GLM-5, MiniMax M2.5, Kimi K2.5, Gemini 2.5 Flash), the research demonstrates that **agents don't fail on intelligence — they fail on execution.**

## Definition

Agent Execution Tax = (total_inference_calls − productive_calls) / productive_calls

*Productive calls* are those that return valid structured output on the first attempt. The tax measures the **ratio of wasted inference to productive inference** — every percentage point is money spent on LLM calls that produce no value.

## Key Findings

| Model | Productive Calls | Total Calls | Execution Tax |
|-------|:---:|:---:|:---:|
| Kimi K2.5 | 852 | 852 | **0.0%** |
| GLM-5 | 869 | 884 | **0.6%** |
| MiniMax M2.5 | 815 | 828 | **1.6%** |
| Gemini 2.5 Flash | 721 | 886 | **22.9%** |

**Gemini 2.5 Flash** produced invalid structured output on nearly 1 in 5 LLM calls (18.6% retry rate). The three Fireworks-hosted models combined: 18 retries across 2,564 calls (0.7%).

### How the Tax Compounds

The tax stacks across three dimensions:

1. **Token tax**: Wasted tokens on malformed responses + full input context re-sent on every retry. Gemini averaged 15,482 input tokens per step; each retry re-sends the entire context for zero productive output.
2. **Latency tax**: Each retry adds ~2.5s (Gemini p50), roughly 12s of dead time per task.
3. **Cascade tax**: A retry at step 8 can desync the agent's internal state, causing downstream steps to misinterpret the page and fail.

### Reliability-Adjusted Accuracy

A compound metric that discounts task success by execution overhead:

> Reliability-Adjusted Accuracy = Task Success Rate × (1 − Execution Tax)

| Model | Task Accuracy | Execution Tax | Reliability-Adjusted Accuracy |
|-------|:---:|:---:|:---:|
| GLM-5 | 57.1% | 0.6% | **56.8%** |
| MiniMax M2.5 | 57.5% | 1.6% | **56.6%** |
| Kimi K2.5 | 49.7% | 0.0% | **49.7%** |
| Gemini 2.5 Flash | 45.0% | 22.9% | **34.7%** |

Gemini's reliability-adjusted accuracy (34.7%) is 10.3 percentage points below its raw accuracy (45.0%) — over a third of its operational capacity is consumed by execution overhead.

### Cost Per Successful Task

Token pricing misleads at the model selection stage. Cost per successful task tells you what you actually pay:

| Model | Success Rate | Cost/Task | Cost Per Successful Task |
|-------|:---:|:---:|:---:|
| MiniMax M2.5 | 57.5% | $0.036 | **$0.062** |
| Gemini 2.5 Flash | 45.0% | $0.064 | **$0.142** |
| Kimi K2.5 | 49.7% | $0.083 | **$0.167** |
| GLM-5 | 57.1% | $0.124 | **$0.217** |

MiniMax M2.5 is **2.3× cheaper** than Gemini per successful task, despite higher per-token pricing. At 10,000 agent tasks/day, Gemini's execution overhead costs over **$40,000/year** in wasted inference.

## Per-Site Analysis: Where the Thesis Holds or Breaks

The site-level breakdown stress-tests the execution-tax thesis: Fireworks models win where tasks compound correctness across many steps; everyone struggles where visual parsing dominates.

- **Universal success**: Cambridge Dictionary (100% across all models), Wolfram Alpha (83–100%), ESPN (83–100%) — clean DOMs, minimal dynamic content.
- **Universal failure**: Allrecipes (0–17%), Google Search (0–8%) — heavy dynamic loading and deceptively complex DOMs; execution tax is irrelevant when the limiting factor is parsing the page at all.
- **The differentiators** (proof weight of the benchmark):

| Website | Gemini | Kimi K2.5 | GLM-5 | MiniMax M2.5 |
|---------|:---:|:---:|:---:|:---:|
| Booking | 0% | 9% | 0% | 33% |
| GitHub | 22% | 17% | 28% | 39% |
| Google Maps | 58% | 58% | 100% | 100% |
| Amazon | 70% | 70% | 55% | 88% |
| ArXiv | 40% | 57% | 77% | 86% |
| HuggingFace | 55% | 75% | 100% | 58% |
| Coursera | 44% | 47% | 67% | 39% |

GLM-5 wins where depth matters (Google Maps, HuggingFace, Coursera): structured data extraction and multi-step reasoning. MiniMax M2.5 wins where interaction matters (Booking, Amazon, GitHub): form flows and dynamic navigation — consistent with its RL-based agent training across real-world environments. Gemini's only win: Google Flights (83% vs 58–75%), notably a Google property.

### Concrete Example: Uniqlo on Google Maps

Task: "Find all Uniqlo locations in Chicago, IL." (WebVoyager). Both models reached the correct answer:

| | Kimi K2.5 | Gemini 2.5 Flash |
|---|:---:|:---:|
| Steps | 12 | 16 |
| LLM calls | 12 | 25 |
| Parse retries | 0 | 9 |
| Total duration | 51.2s | 97.9s |
| Input tokens | 87,063 | 207,971 |

Gemini's 98s breaks down to ~40s browser ops, ~37s productive inference, ~21s retry inference — each retry re-sends the full conversation context (12,000–16,000 tokens, 2–3s). Kimi's 51s has no retry segment at all. The difference was not reasoning ability; it was execution overhead.

## Why Nobody Measures This

Parse retries happen **inside the LLM engine**, before the agent framework ever sees the result — invisible unless the engine is instrumented. Static benchmarks (MMLU, HumanEval, ARC) measure intelligence in isolation, not sustained structured-output compliance across a multi-step loop. Prior work supports the framing: WebVoyager (He et al., 2024), AgentBench (Liu et al., 2024), and SWE-bench (Jimenez et al., 2024) all found large gaps between model-capability scores and task-completion rates in multi-step loops.

> Parse retry rate should be a first-class metric in every agent benchmark.

## Inference Latency: The Compounding Story

Per-call latency is only half the picture; retry-inflated call counts flip the end-to-end story. Gemini's p50 latency (2,476ms) looks competitive with Kimi's (2,145ms) — only 15% slower per call — but Gemini makes ~14.7 calls/task vs Kimi's ~10.2: **36.4s vs 21.9s of LLM time (66% more)**, purely from more calls. Gemini also wastes ~36,800 tokens/task on billed-and-discarded inference (~1 in 5 tokens); the three Fireworks models combined waste under 3,000 tokens/task. The p95/p50 spread across all models (1.8–2.3×) is tight, indicating predictable tail latencies from the serving stack — a property of the serving layer, not the models.

## Relationship to Tool-Use Tax

The Agent Execution Tax extends [[concepts/tool-use-tax]] (Zhang et al., arXiv:2605.00136) from the research domain to production deployment:

| Dimension | Tool-Use Tax | Agent Execution Tax |
|-----------|-------------|-------------------|
| **Origin** | Academic (Zhang et al., Apr 2026) | Industry (Fireworks AI, May 2026) |
| **Focus** | Semantic distractors and protocol overhead harming reasoning | Structured output reliability in multi-step loops |
| **Measurement** | Accuracy difference: CoT vs tool-augmented | Parse retry rate, cost per successful task |
| **Scope** | Single-turn tool calls | 10+ step agent loops |
| **Mitigation** | G-STEP gate (inference-time tool selection) | Model selection by reliability, inference infrastructure optimization |

Both concepts converge on the same core insight: **reliability of structured output is the primary bottleneck for production agents**, not raw model intelligence.

## Implications for Agent Procurement

From the research, a procurement scorecard for evaluating models in agent deployments:

| If you need... | Use | Why |
|---|---|---|
| Maximum task accuracy | GLM-5 | 57.1% accuracy; 100% on Google Maps, HuggingFace, BBC News, Wolfram Alpha |
| Lowest cost at scale | MiniMax M2.5 | $0.062 per successful task; RL-trained agent takes fewest steps (9.8 avg), rarely retries (1.6%) |
| Fastest real-time response | Kimi K2.5 | 2.1s p50 LLM latency; zero parse retries; best for user-facing agents |
| Rigorous procurement | Reliability-Adjusted Accuracy | Token pricing misleads; cost per successful task reflects actual spend |

## Methodology

- **Task suite**: WebVoyager (60 multi-step browser tasks across 15 real websites)
- **Runs**: 3× per task per model (720 total across 4 models)
- **Instrumentation**: Per-call LLM latency, parse retry/failure counts, token usage
- **Framework**: Notte (open-source, model-agnostic browser agent)
- **Models**: All text-only, temperature=0.0, max_steps=20, response_format=json_object (non-strict)
- **Independent LLM judge** evaluated task success across all models

## Related Concepts

- [[concepts/tool-use-tax]] — Academic precursor on protocol-induced failure modes
- [[concepts/harness-engineering/agent-harness]] — The infrastructure between model and tools
- [[concepts/agentic-browsing]] — AI agents navigating websites autonomously
- [[concepts/structured-outputs]] — Format compliance as agent bottleneck
- [[concepts/ai-benchmarks/webarena]] — Web agent benchmark family (WebVoyager lineage)
