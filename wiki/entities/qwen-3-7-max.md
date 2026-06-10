---
title: Qwen 3.7 Max
created: 2026-05-23
updated: 2026-05-23
type: entity
tags:
  - entity
  - model
  - text-generation
  - reasoning
  - ai-agents
  - coding-agents
  - agentic-engineering
  - multi-agent
  - inference
  - alibaba
  - qwen
  - china
  - context-management
  - orchestration
sources: [https://explainx.ai/blog/qwen-3-7-max-agent-frontier-long-horizon-autonomy, https://ai-trends.today/qwen-introduces-qwen3-7-max-a-reasoning-agent-model-with-a-1m-token-context-window/]
---

# Qwen 3.7 Max

Alibaba Cloud's most advanced agentic reasoning model, announced at the **Alibaba Cloud Summit on May 20, 2026**. Qwen 3.7 Max represents a strategic pivot from general-purpose benchmarks toward **sustained autonomous execution** — designed for long-horizon tasks spanning hours or days with hundreds of tool calls. It is a proprietary, closed-weight, text-only model.

## Overview

Qwen 3.7 Max is described by Alibaba as their "most sophisticated and comprehensive agent to date." Unlike previous Qwen models focused on broad capability benchmarks, 3.7 Max is optimized for autonomous task loops that require sustained reasoning, error recovery, and adaptation across hundreds to thousands of steps.

> "Let the agent cook." — Alibaba's design philosophy

## Key Specifications

| Feature | Qwen 3.7 Max | Qwen 3.6 Max (predecessor) |
|---|---|---|
| Context window | **1M tokens** | 256K tokens |
| Modality | Text-only | — |
| Weight access | Closed-weight, proprietary | — |
| Thinking mode | Yes (CoT trace visible) | — |
| API compatibility | OpenAI + Anthropic API spec | — |

## Benchmark Performance

### Artificial Analysis Intelligence Index v4.0
- **Score: 56.6** — ranked **#5 overall**, up 4.8 points from Qwen 3.6 Max Preview (51.8)
- Ahead of: [[concepts/gemini/3-5-flash|Gemini 3.5 Flash]] (55.3), [[concepts/gpt/gpt-5-5|GPT-5.5]] (55.2)
- Behind: Claude Opus 4.7 (57.3), Gemini 3.1 Preview (57.2)

### Agentic Coding Benchmarks

| Benchmark | Qwen 3.7 Max | Opus 4.6 Max | DeepSeek V4 Pro |
|---|---|---|---|
| Terminal Bench 2.0 | **69.7** | 65.4 | 67.9 |
| SWE-bench Verified | 80.4 | **80.8** | 80.6 |
| SWE-bench Pro | **60.6** | 57.3 | 59.0 |
| SciCode | **53.5** | 51.9 | — |

### General Agent Benchmarks
- **MCP-Mark: 60.8** — orchestrating multiple MCP servers (DBs, APIs, file ops, web scraping)
- **SkillsBench: 59.2** — discovering and combining skills on the fly
- **SpreadSheetBench: 87.0** — office automation (formulas, data cleaning, pivot tables)

### LM Arena Rankings
- Text Arena: #13 worldwide (Elo 1475)
- Top-10 categories: #7 Math, #9 Expert Prompts & IT, #10 Coding

### AA Omniscience Trade-off
- Raw accuracy **dropped** 7.6 pp (36.7% → 30.1%)
- Hallucination rate **dropped** 21.3 pp (42.2% → 20.9%)
- Abstention rate fell to 48.0% — the lowest attempt rate among frontier models
- Indicates conservative knowledge-recall strategy: prefers "I don't know" over hallucination

## The 35-Hour Kernel Optimization Feat

Alibaba's defining demo: Qwen 3.7 Max autonomously optimized a memory-bound "Extend Attention" kernel for the **T-Head ZW-M890** — a proprietary chip it had never seen during training.

### Timeline

| Phase | Hours | Activity | Result |
|---|---|---|---|
| Initial Analysis | 0-3 | Profiled reference, identified memory bottleneck, read architecture docs | Strategy formulated |
| First Attempts | 3-12 | Loop tiling + vectorization | Only 1.2× speedup — diagnosed failure |
| Architecture Redesign | 12-20 | Discovered scratchpad memory, redesigned kernel staging | Crash recovery via binary-search debugging |
| Fine-Grained Opt | 20-30 | Double-buffering, 18 buffer configs tested, SIMD instructions | **8.2× speedup** |
| Final Refinement | 30-35 | Adaptive algorithms per input shape | **10.1× geometric mean** |

**Total:** 35 hours continuous, **1,158 tool calls**, zero human intervention.

### Significance
- **Sustained context**: Coherent strategy across 1,000+ tool calls with no "instruction drift"
- **True problem-solving**: Read unfamiliar chip docs, transferred principles, experimented, failed, recovered
- **Error handling**: Handled segfaults, performance regressions, and build failures autonomously
- **Computational confidence**: At ~$2-3/M tokens, Alibaba bet millions of tokens on the model's reliability

## Training Innovation: Environment Scaling

Alibaba's methodology for building agent-capable models — preventing **harness overfitting** by diversifying execution environments, not just training data.

Training instances decouple into three components:
1. **Task** — the objective (e.g., "Fix bug #1234")
2. **Harness** — execution environment (e.g., Claude Code, raw terminal, IDE)
3. **Verifier** — success criteria (e.g., "All tests pass")

By varying all three, the model learns underlying strategies rather than tool-specific shortcuts. This is analogous to how diverse text data produces general language models — diverse environments produce general agent models.

## Thinking Mode

Qwen 3.7 Max generates internal chain-of-thought (CoT) before answering. On Qwen Chat, toggle "Thinking" mode to see the reasoning trace. In testing, it generated ~97M tokens vs. 24M average for comparable models — high token overhead but superior on multi-step plans, code refactoring, and large agent chains.

## API Access

- Base URL: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
- Model string: `qwen3.7-max`
- Compatible with both OpenAI API spec and Anthropic API spec
- Thinking mode via `extra_body={"enable_thinking": True}`
- Pricing not yet announced (predecessor was $1.30/$7.80 per 1M input/output tokens)

**⚠️ Preview status**: Benchmark scores, behavior, and pricing may change before stable release. No open-weight version planned post-May 2026.

## Related

- [[entities/qwen3-6-plus|Qwen 3.6 Plus]] — predecessor model
- [[concepts/gemini/3-5-flash|Gemini 3.5 Flash]] — competing agent-first model
- [[entities/deepseek-v4|DeepSeek V4 Pro]] — competing agent model
- [[concepts/agentic-engineering|Agentic Engineering]]
- [[concepts/coding-agents|Coding Agents]]
- [[concepts/multi-agent|Multi-Agent Systems]]
