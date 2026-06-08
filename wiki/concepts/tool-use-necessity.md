---
title: "Tool Use Necessity Detection"
created: 2026-05-31
updated: 2026-05-31
type: concept
tags:
  - tool
  - optimization
  - reasoning
  - interpretability
  - architecture
sources:
  - https://www.agentupdate.ai/news/llm-agents-tool-necessity-hidden-states/
---

# Tool Use Necessity Detection

Research into when LLM agents should use external tools versus answering directly from internal knowledge.

## The Problem

LLM agents often invoke external tools indiscriminately, even when the model could directly provide an answer. Each unnecessary tool call wastes API fees and adds latency.

## When2Tool Benchmark

- 18 environments (15 single-hop, 3 multi-hop tasks)
- Three dimensions: computational scale, knowledge boundaries, execution reliability
- Controlled difficulty levels establishing clear decision boundaries

## Key Finding: Hidden-State Decodability

**Tool necessity is linearly decodable from pre-generation hidden states**, achieving AUROC 0.89-0.96 across 6 different models. This means:
- Models inherently "know" when tools are needed
- This internal knowledge is NOT reflected in their verbalized reasoning
- Models fail to act upon their own internal knowledge during response generation

## Probe&Prefill Method

- Lightweight linear probe reads hidden-state signal for tool necessity
- Prefills model response with a steering sentence based on probe output
- **Results**: 48% reduction in tool calls, only 1.7% accuracy loss
- Best baseline: 6% tool call reduction at comparable accuracy, OR similar reduction with 5x higher accuracy loss

## Implications for [[concepts/axpo|AXPO]]

AXPO addresses the "Thinking-Acting Gap" through tool-call resampling during training. Probe&Prefill addresses the same fundamental problem through inference-time steering. Together they suggest:
1. The tool-use failure mode is structural, not model-specific
2. Both training-time and inference-time interventions are effective
3. Hidden-state analysis provides a reliable signal for tool necessity

## Related Pages
- [[concepts/axpo]] — AXPO training-time tool-call resampling
- [[concepts/tool-use]] — Tool use in agentic systems
- [[entities/qwen]] — Qwen3-VL-Thinking models
