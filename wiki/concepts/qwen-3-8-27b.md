---
title: "Qwen 3.8 27B"
type: concept
created: 2026-08-17
updated: 2026-08-27
tags:
  - model
  - qwen
  - alibaba
  - open-source
  - local-llm
  - reasoning
  - vision
  - coding-agents
  - mixture-of-experts
aliases: ["Qwen3.8-27B", "Qwen 3.8 27B dense"]
sources:
  - raw/articles/simonwillison.net--2026-aug-16-qwen-38-27b--e8876b7c.md
  - https://simonwillison.net/2026/Aug/16/qwen-38-27b/
---

# Qwen 3.8 27B

A **dense** (non-MoE) 27B parameter vision-capable LLM from Alibaba's Qwen team, released August 15, 2026 under Apache 2.0. The successor to [[concepts/qwen3-6-27b|Qwen 3.6 27B]], positioned as a local-friendly model that can run on high-end consumer hardware (17GB quantized).

This is distinct from the larger [[concepts/qwen-3-8|Qwen 3.8 Max]] (2.4T MoE), which requires datacenter-class hardware.

## Specifications

| Spec | Value |
|------|-------|
| Parameters | 27B (dense) |
| License | Apache 2.0 |
| Context window | 262,144 tokens |
| Quantized size | ~17GB (Q4_K_M GGUF) |
| Vision | Yes (bounding boxes, image analysis) |
| Reasoning effort levels | `xhigh` (default), `medium`, `low`, off |
| Predecessor | [[concepts/qwen3-6-27b\|Qwen 3.6 27B]] |

## Key characteristics

### Overthinking default

The model defaults to `xhigh` reasoning effort, which causes it to spend enormous amounts of tokens on reasoning traces even for simple tasks. Simon Willison found that asking it to "draw an svg of a circle" triggered a multi-minute internal deliberation about Bauhaus aesthetics and animation frameworks before producing an elaborate animated circle — entirely unsolicited.

**Recommendation**: Run on `low` or no reasoning initially. The `xhigh` default is entertaining but impractical for consumer hardware. (Simon later confirmed the upside of the default: in an Aug 18 X reply, "I got a fantastic pelican out of that one!" — the `xhigh` overthinking produced his best local-model pelican SVG ever. See "Vision and bounding boxes" below.)

### Vision and bounding boxes

Excellent at returning structured bounding boxes for image analysis. On a pelican photo test, it produced accurate 0-1000 scale bounding boxes that closely matched the actual bird positions. Can also build interactive HTML tools from bounding box JSON in a single prompt.

### Coding agent capability

Successfully drives coding agent loops (tested with Pi agent framework):
- Answered complex "how does auth work?" questions about Datasette by reading multiple source files
- Built working Python tools from natural language descriptions
- Requires longer system prompts than larger models — Pi's shorter prompt made it a better fit

### Multi-Token Prediction (MTP)

Supports MTP, an architecture trick where a cheaper mechanism guesses several tokens ahead and the main model verifies. Using llama.cpp's `--spec-type draft-mtp` flag on DGX Spark showed ~72% throughput improvement over default GGUF serving.

## Performance observations

- **Speed**: 15-30 tokens/second on M5 Max MacBook Pro and NVIDIA DGX Spark — usable but not fast
- **Quality**: Best local-model pelican SVG ever generated; strong reasoning when given enough context
- **Comparison**: At 17GB, it demonstrates capabilities that required frontier proprietary models just a year ago
- **Limitation**: Dense models require high memory bandwidth; neither consumer Mac nor DGX Spark are top performers in this regard

## Significance

Qwen 3.8 27B demonstrates that open-weight general-purpose models can offer long context, effective tool calling, strong vision, and competent code generation in a 17GB file. The model at this size continues to improve at an impressive rate, narrowing the gap with datacenter-class models.

## Related

- [[concepts/qwen-3-8|Qwen 3.8 Max]] — MoE variant (2.4T parameters)
- [[concepts/qwen3-6-27b|Qwen 3.6 27B]] — predecessor
- [[concepts/qwen|Qwen Model Family]]
- [[concepts/local-qwen-vs-claude-opus|Local Qwen vs Claude Opus]]
- [[entities/simon-willison|Simon Willison]] — hands-on review
