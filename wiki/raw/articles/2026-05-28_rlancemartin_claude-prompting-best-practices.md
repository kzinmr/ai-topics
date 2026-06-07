---
title: "Claude Prompting Best Practices — Claude Platform Docs"
source: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices"
scraped: 2026-06-07
type: raw-article
tags: [claude-api, prompt-engineering, claude-opus, adaptive-thinking, agentic-systems]
---

# Claude Prompting Best Practices — Claude Platform Docs

> Comprehensive guide to prompt engineering techniques for Claude's latest models, covering clarity, examples, XML structuring, thinking, and agentic systems. Single reference for Claude Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6, and Haiku 4.5.

## Prompting Claude Opus 4.8

Claude Opus 4.8 has particular strengths in long-horizon agentic work, knowledge work, vision, and memory tasks. It performs well out of the box on existing Claude Opus 4.7 prompts.

### Response length and verbosity

Claude Opus 4.8 calibrates response length to how complex it judges the task to be, rather than defaulting to a fixed verbosity. This usually means shorter answers on simple lookups and much longer ones on open-ended analysis. Use positive examples showing how Claude can communicate with the appropriate level of concision.

### Calibrating effort and thinking depth

The effort parameter allows you to tune Claude's intelligence vs. token spend:

- **xhigh**: Best for most coding and agentic use cases. Start here.
- **max**: May deliver performance gains in some use cases, but may show diminishing returns and overthinking.
- **high**: Minimum for most intelligence-sensitive use cases. Balances token usage and intelligence.
- **medium**: Good for cost-sensitive use cases.
- **low**: Reserve for short, scoped tasks and latency-sensitive workloads.

Claude Opus 4.8 respects effort levels strictly, especially at the low end. At low and medium, the model scopes its work to what was asked rather than going above and beyond. On Claude Opus 4.8, thinking is off unless you explicitly set `thinking: {type: "adaptive"}`.

For coding agents at max or xhigh effort, set a large max output token budget (start at 64k tokens) so the model has room to think and act across subagents and tool calls.

### Tool use triggering

Claude Opus 4.8 has a tendency to favor reasoning over tool calls. This produces better results in most cases. However, increasing the effort setting (high or xhigh) increases tool usage substantially in agentic search and coding. For scenarios where you want more tool use, adjust your prompt to explicitly instruct the model about when and how to properly use its tools.

### User-facing progress updates

Claude Opus 4.8 provides more regular, higher-quality updates to the user throughout long agentic traces. If you've added scaffolding to force interim status messages, try removing it.

### More literal instruction following

Claude Opus 4.8 interprets prompts literally and explicitly, particularly at lower effort levels. It does not silently generalize an instruction from one item to another, and it does not infer requests you didn't make. The upside is precision and less thrash — generally better for API use cases with carefully tuned prompts.

## Extended Thinking Migration (Sonnet 4.6)

- **Not using extended thinking on Sonnet 4.5**: Continue without it on Sonnet 4.6. Use `effort: "low"` for similar or better performance.
- **Using extended thinking with budget_tokens**: Still functional but deprecated. Migrate to adaptive thinking with the effort parameter.
- **Autonomous multi-step agents**: Start at `high` effort with adaptive thinking.
- **Computer use agents**: Sonnet 4.6 achieved best-in-class accuracy using adaptive mode.
- **Bimodal workloads**: Adaptive skips thinking on simple queries and reasons deeply on complex ones.
- **For coding use cases**: Start with `medium` effort (budget_tokens ~16k during migration).
- **For chat and non-coding**: Start with `low` effort.
