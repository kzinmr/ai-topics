---
title: "Hunyuan Hy4"
created: 2026-11-06
updated: 2026-11-06
type: concept
tags: [model, open-source, reasoning, coding-agents, tencent, multimodal, computer-use, rsi, mixture-of-experts, vision]
sources:
  - https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/
  - https://news.ycombinator.com/item?id=50383963
related:
  - "[[concepts/hunyuan-hy3]]"
  - "[[entities/tencent]]"
  - "[[concepts/kimi-k3]]"
  - "[[concepts/recursive-self-improvement]]"
  - "[[entities/deepseek]]"
confidence: medium
---

# Hunyuan Hy4

**Tencent Hy4** (announced 2026-11-04) is Tencent's next-generation LLM, positioned as ranking among the world's leading open-source models. Weights and system cards promised "in the coming days," with emphasized cybersecurity and biosafety safeguards. HN: 95 pts ([item 50383963](https://news.ycombinator.com/item?id=50383963)).

## New capabilities vs Hy3

- **First visual understanding** in the Hunyuan line: fine-grained image processing, complex chart analysis, mathematical visual reasoning.
- **First computer-use**: CLI and GUI interaction; specialized training on professional software (Blender, CAD) for long-horizon tasks.
- Major gains in instruction following, long-context comprehension, long-horizon agentic tasks.

## Evaluation claims (largely internal/blind, treat with caution)

- WorkBuddy (Tencent office agent): average score 83.18, pass rate 96.15%, first place in 9/12 mainland-market scenarios.
- Financial blind eval (with Tencent Financial Technology, 213 professionals, 579 real tasks): **Hy4 3.04 > DeepSeek-V4.1-Flash-1017 2.97 > Kimi K3.1 Pro 2.68 = GLM-5.3 2.68** — the ranking note in HN discussion fueled "benchmaxxed" suspicions aimed at both Hy4 and K3.1.
- Hallucination rate 12.95% → 7.2% vs Hy4 Preview; unsupported-assumption errors 23.1% → 5.6%.
- GameDev +19.1%, GameLogic +9.8% vs Preview (Unreal/Unity/Godot integration with Tencent IEG).
- Science: TenureTrail 123 executable tasks across 7 disciplines; open-sourced HyCell (single-cell) and HyPDE (physics fields) foundation models built with Hy4 + **Hyra 2.0 harness** — framed by Tencent as the "next stage of Recursive Self-Improvement."

## Safety posture

- Defensive-security training only (PoC development, vuln remediation, reverse engineering, analysis-purpose pentesting); offensive exploitation material explicitly excluded. Xuanwu Lab + Keen Security Lab assessments found "no significant concerns" on offensive cyber capabilities.
- Biosafety: strong foundational biology knowledge, limited open-ended experimental design vs frontier models.

## Pricing & availability

- Unchanged from Hy4 Preview: ~**$0.90 /M input, $2.70 /M output, $0.045 /M cached input**; Hy4 Flash planned for lower-cost tier.
- Available on Tencent Cloud TokenHub, WorkBuddy, CodeBuddy, Yuanbao, WeCom Dayuan, ima; API via OpenRouter and other third parties.

## Caveats

Most benchmarks are Tencent-internal or blind evaluations run with Tencent-affiliated partners; independent Artificial Analysis-style scores pending weight release. HN reception was muted (95 pts) compared with Kimi K3.1 Pro's weight drop the same day.

## Related

- [[concepts/hunyuan-hy3]] — predecessor
- [[entities/tencent]] — owner
- [[concepts/kimi-k3]] / [[concepts/deepseek-v4]]-class Chinese open-weight competition
- [[concepts/recursive-self-improvement]] — Hyra 2.0 RSI framing

## Sources

- https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/
- HN: https://news.ycombinator.com/item?id=50383963
