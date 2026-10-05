---
title: "GPT-6.1 Sol"
created: 2026-10-05
updated: 2026-10-05
type: entity
aliases:
  - gpt-6.1-sol
  - gpt-6-1-sol
  - GPT 6.1 Sol
tags:
  - model
  - openai
  - gpt
  - frontier-models
  - reasoning
  - coding-agents
  - computer-use
  - factuality
  - token-economics
  - pricing
sources:
  - raw/articles/2026-10-05_openai_introducing-gpt-6-1-sol.md
related:
  - entities/openai-astra
  - events/claude-opus-5-5-gpt-6-release-sep-2026
  - entities/openai
confidence: high
---

# GPT-6.1 Sol

**GPT-6.1 Sol** is OpenAI's October 5, 2026 upgrade to [[events/claude-opus-5-5-gpt-6-release-sep-2026|GPT-6 Sol]], positioned as a "value" frontier model: it *nearly matches* [[entities/openai-astra|GPT-6 Astra]] on agentic coding, computer use, and professional work at roughly **one-fifth of Astra's** standard input/output token prices. Its headline economic story is cached input at **$0.10/M tokens** — 95% below standard input and 50% below GPT-6 Sol's cached price — explicitly aimed at agents that reuse context across many requests.

## Positioning in the Sol/Luna/Astra family

GPT-6.1 Sol sits below the flagship [[entities/openai-astra|Astra]] in the family OpenAI established in September 2026 with GPT-6 Sol and Luna. The strategy is a price/capability frontier: Sol handles high-volume everyday professional and agentic work cheaply, while Astra remains the pick for the hardest tasks (it still tops Terminal-Bench Science at 68.1%). The 6.1 refresh widens the gap between "good-enough-and-cheap" and "flagship" — a recurring theme in the [[concepts/token-economics|token-economics]] / [[comparisons/llm-api-pricing|LLM API pricing]] race that began with the September price war.

## Benchmarks vs. GPT-6 Sol / Astra / Opus 5.5

| Benchmark | What it measures | GPT-6.1 Sol result | Cost angle |
|-----------|------------------|--------------------|------------|
| DeepSWE v1.1 | Complex SWE in real codebases | Matches Astra; +6.4 pts over GPT-6 Sol at lower effort | ~1/5 Astra cost |
| GDP.pdf | Professional Q&A over complex PDFs | Beats Opus 5.5 w/ fallbacks; nears Astra | <½ Opus, ~⅕ Astra cost/task |
| AutomationBench 1.0.6 | Multi-step business workflows (47 tools) | +2.2 pts over Opus 5.5 (medium); +4.8 over GPT-6 Sol | ~⅓ Opus cost |
| OSWorld 2.0 (offline, v2026.08.08) | Long-horizon computer use | +7 pts over GPT-6 Sol (max); within 2.1 of Astra | <½ Sol, ~⅐ Astra cost/task |
| Terminal-Bench Science 0.1 | Data analysis, simulation, theorem proving | >2× GPT-6 Sol (max); Astra still highest at 68.1% | $5.47/task vs $23.21 Opus, $23.80 Astra (>75% cheaper) |
| Factuality | % responses with ≥1 factual error (user-flagged hard prompts) | 11.4% → 7.7% over Sol (low effort, ~32% cut); within 1.9 pts of Astra | <⅕ Astra cost/task |

Factuality is measured on de-identified ChatGPT conversations where users flagged a prior model's error — deliberately hard, not representative of typical use (cf. [[concepts/ai-benchmarks/benchmaxxing]] on benchmark framing caveats).

## Alignment & safety posture

OpenAI reports substantial gains over GPT-6 Sol on alignment evals — lower failure rates on transparency about broken search tools, respecting explicit restrictions, and avoiding unauthorized outcomes during agentic tasks. No attempts to bypass an automated safety reviewer were observed, matching Astra and Sol. Details are in the GPT-6.1 Sol system card addendum (deploymentsafety.openai.com/gpt-6-1-sol). This is the same "monitorability / eval-awareness" family of concerns that OpenAI formalized the same day in [[concepts/frontier-rl-safety-cases|safety cases for frontier training]].

## Pricing & availability

- ChatGPT Work + Codex for Plus/Pro/Business/Enterprise/Edu (not yet in Chat).
- API model id `gpt-6.1-sol`: **$2/M input, $0.10/M cached input, $10/M output**.
- An "Ultrafast" tier (up to 8× faster token generation) to follow in Codex.

## Related

- [[entities/openai-astra]] — flagship this model undercuts on price
- [[events/claude-opus-5-5-gpt-6-release-sep-2026]] — original GPT-6 Sol/Luna launch + price war
- [[comparisons/llm-api-pricing]] — where the $0.10 cached-input point lands
- [[concepts/frontier-rl-safety-cases]] — companion safety-training framework published same day
