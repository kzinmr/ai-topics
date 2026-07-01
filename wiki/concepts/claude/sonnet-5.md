---
title: "Claude Sonnet 5"
type: concept
created: 2026-07-01
updated: 2026-07-01
tags:
  - claude
  - anthropic
  - model
  - ai-agents
aliases: ["Sonnet 5", "Claude Sonnet 5"]
sources:
  - raw/articles/simonwillison.net--2026-jun-30-claude-sonnet-5--6e28b886.md
  - raw/articles/2026-07-01_harvey_sonnet-5-in-harvey.md
  - raw/newsletters/2026-07-01-ainews-sonnet-5-today-and-fable-5-tomorrow.md
---

# Claude Sonnet 5

**Claude Sonnet 5** is an Anthropic mid-tier frontier model released on June 30, 2026. Anthropic describes it as "our most agentic Sonnet yet," emphasizing planning, browser/terminal tool use, and autonomous execution capabilities. Its performance is close to [[concepts/claude/opus-4-8|Opus 4.8]] but at lower prices.

## Overview

Sonnet 5 represents a significant upgrade over [[concepts/claude/sonnet-4-6|Sonnet 4.6]] with architectural improvements that deliver near-Opus-level quality at Sonnet price points. The model was released alongside Claude Code, API, and ecosystem partner rollouts.

| Attribute | Value |
|-----------|-------|
| **Release date** | June 30, 2026 |
| **Context window** | 1,000,000 tokens |
| **Max output** | 128,000 tokens |
| **Input price** | $3.00 / million tokens |
| **Output price** | $15.00 / million tokens |
| **Intro discount** | $2.00 / $10.00 (until Aug 31, 2026) |
| **Pricing status** | Same as Sonnet 4.6 list, but intro discount |

## Key Technical Changes

### New Tokenizer

Sonnet 5 introduces a new tokenizer that produces **~30% more tokens for the same input text** compared to [[concepts/claude/sonnet-4-6|Sonnet 4.6]]. This represents an effective 30% price increase for English text:

| Language | Token Ratio vs Sonnet 4.6 |
|----------|---------------------------|
| English | ~1.42× |
| Spanish | ~1.33× |
| Python code | ~1.28× |
| Chinese (Mandarin Simplified) | ~1.01× |

Source: [[entities/simon-willison|Simon Willison]]'s [Claude Token Counter](https://tools.simonwillison.net/token-count) analysis.

### Sampling Parameter Removal

The following sampling parameters are **no longer supported**:
- `temperature`
- `top_p`
- `top_k`

These are replaced by **adaptive thinking**, which is enabled by default unless explicitly disabled with `"thinking": {type: "disabled"}`.

### Platform Features

Sonnet 5 shares "the same set of tools and platform features as Claude Sonnet 4.6," including:
- Tool use (function calling)
- Vision capabilities
- Extended thinking
- Batch API support

## Agentic Capabilities

Anthropic positioned Sonnet 5 as "our most agentic Sonnet yet" with strengths in:

- **Planning**: Complex multi-step task decomposition
- **Browser tool use**: Web interaction and data extraction
- **Terminal tool use**: CLI/Codex-style agentic operation
- **Autonomous execution**: Reduced human-in-the-loop requirements
- **Coding**: Significant improvements over Sonnet 4.6 in software engineering tasks

The model was rolled out immediately across Claude, [[concepts/claude-code/claude-code|Claude Code]], the Anthropic API, and ecosystem partners ([[entities/harvey|Harvey]], [[entities/glean|Glean]], etc.).

## Enterprise Benchmarks

### Harvey Legal Benchmarks

[[entities/harvey|Harvey]] published Sonnet 5 evaluation results on legal-domain benchmarks:

| Benchmark | Score | Notes |
|-----------|-------|-------|
| **Legal Agent Benchmark (LAB)** | 5.8% all-pass | Strict multi-step legal work evaluation |
| **BigLaw Bench** | 91.3% | Highest recorded across Sonnet and Opus models |

LAB tests multi-step legal work from assignment through review. Sonnet 5 showed strengths in energy/natural resources, real estate, and capital markets — with **drafting** as its strongest LAB task type. BigLaw Bench strengths included risk assessment, compliance, case management, and transactional drafting.

Niko Grupen, Head of Applied Research at Harvey:
> "Sonnet 5 brings a meaningful jump in legal quality over Sonnet 4.6. In early testing, it was both more accurate and more precise than its predecessor, delivering stronger answers in fewer words."

Limitations noted: dense specialized analytical tasks (tax, structured finance) remain challenging, as does multi-step agentic completion without any missed steps.

### Simon Willison's Assessment

[[entities/simon-willison|Simon Willison]] noted that Anthropic's official "What's New" developer docs contained more actionable information than the official announcement. His key findings:
- Performance is "close to that of Opus 4.8, but at lower prices"
- The new tokenizer creates a significant effective price increase for English text
- The removal of sampling parameters represents a philosophical shift toward adaptive defaults

## Safety

Per the Sonnet 5 system card, the model is **significantly less capable at cyber tasks than [[concepts/claude/mythos|Mythos 5]]**. Its safeguards are similar to those applied to [[concepts/claude/opus-4-7|Opus 4.7]] and [[concepts/claude/opus-4-8|Opus 4.8]] (models more capable than Sonnet 5 but much less capable than Mythos 5). This positioning enabled release without being blocked by US government export control review under [[concepts/claude/fable-5|Fable 5]] regulations.

## See Also

- [[concepts/claude/sonnet-4-6]] — Claude Sonnet 4.6 (predecessor)
- [[concepts/claude/opus-4-8]] — Claude Opus 4.8 (performance comparable)
- [[concepts/claude/mythos]] — Claude Mythos family (cyber-capable frontier models)
- [[concepts/claude/index]] — Claude models hub
- [[entities/anthropic]] — Anthropic entity page
- [[concepts/claude-code/claude-code]] — Claude Code (coding agent)
