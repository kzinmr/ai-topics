> Source: https://www.i-scoop.eu/ling-2-6-1t-by-ant-group/
> Date: May 19, 2026
> Author: Tom Cuylaerts

# Ling 2.6-1T by Ant Group – Summary

Ling 2.6-1T is a trillion-parameter open-weights model from Ant Group, released under the MIT license. It uses a Mixture of Experts (MoE) architecture with 63 billion active parameters per token during inference (from 1 trillion total). Native context window is up to 1 million tokens; the exposed API is ~256K tokens.

Key design goal: "can a frontier scale model handle complex work with less token waste, stronger tool use and enough reliability for enterprise workflows?"

## Key Specifications
- Total parameters: 1 trillion
- Active parameters (inference): 63 billion
- Architecture: MoE
- Context: Native 1M tokens, API ~256K
- Modality: Text in, text out (non-reasoning)
- License: MIT (open weights)
- Provider: InclusionAI (Ant Group)

## Performance
- SWE-bench Verified: 72.2 (Artificial Analysis)
- Intelligence Index (AA): 34
- Also tested: BFCL-V4, TAU2-Bench, IFBench, AIME26, MRCR
- Pricing: $0.30/M input, $2.50/M output (median across providers)
- Blended (3:1 ratio): $0.85/M tokens

## Ecosystem: BaiLing
Part of Ant Group's BaiLing foundation model platform:
- Computing cluster with tens of thousands of heterogeneous accelerators
- Integrated security (detection > defense)
- Knowledge processing at trillions of tokens
- Applications: Maxiaocai (financial assistant), CodeFuse (AI development tool)

## Ling 2.6 Flash (sibling)
- 104B total / 7.4B active parameters
- High-throughput, low-cost variant
- Ling 2.6-1T: flagship for long documents, complex reasoning, coding agents
