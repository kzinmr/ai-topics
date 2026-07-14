---
title: "Claude Code vs OpenCode: Token Overhead Comparison"
created: 2026-07-14
updated: 2026-07-14
type: comparison
tags: [claude-code, opencode, coding-agents, token-efficiency, tool-use, system-prompt, prompt-caching, subagents, token-economics, harness-engineering, context-management]
sources: [raw/articles/2026-07-12_systima_claude-code-vs-opencode-token-overhead.md]
hn_discussion: https://hn.algolia.com/api/v1/items/48883275
---

# Claude Code vs OpenCode: Token Overhead Comparison

## Summary

A July 2026 measurement study by Systima compared the token overhead of **[[entities/claude-code]]** (v2.1.207) and **[[entities/opencode|OpenCode]]** (v1.17.18), both pinned to Claude Sonnet 4.5, with cross-validation on Claude Fable 5. The headline finding: **Claude Code sends ~33,000 tokens of system prompt, tool schemas, and scaffolding before the user prompt arrives; OpenCode sends ~7,000 tokens** — a ~4.7× gap on Sonnet, narrowing to ~3.3× on Fable 5 where Claude Code's system prompt is model-conditional.

## Core Comparison

| Dimension | Claude Code (Sonnet 4.5) | OpenCode (Sonnet 4.5) |
|---|---|---|
| **System prompt** | 27,344 chars, 3 blocks | 9,324 chars, 1 block |
| **Tool schemas** | 27 tools, 99,778 chars | 10 tools, 20,856 chars |
| **First-message scaffolding** | 7,997 chars of `<system-reminder>` | None |
| **First-turn payload (tokens)** | ~32,800 | ~6,900 |
| **Zero-tools system prompt (tokens)** | ~6,500 | ~2,000 |
| **Tool-calling style** | Parallel batch (single round trip) | Serial (one tool per turn) |
| **Cache prefix stability** | 3+ distinct prefixes per session; frequent mid-session re-writes | Byte-identical across all runs; zero mid-session re-writes (Sonnet) |
| **Mid-session cache re-writes** | 37K–86K tokens (observed in 2 model families) | ~1K–6K (rare, one event on Fable) |
| **AGENTS.md/CLAUDE.md reading** | Only reads CLAUDE.md (ignores AGENTS.md) | Reads both filenames |
| **Subagent bootstrap** | 3,554 chars system + 24/27 tools per subagent | 1,379 chars system + 5 tools per subagent |
| **Multiplier: instruction file** | +20K tokens/request | +20K tokens/request |
| **Multiplier: MCP servers** | +1K–1.4K tokens/server/request | +1K–1.4K tokens/server/request |

## Cost Comparison (Identical Tasks)

| Task | Claude Code | OpenCode | Ratio |
|---|---|---|---|
| T1: Reply "OK" (first request) | ~32,800 tokens | ~6,900 tokens | 4.8× |
| T2: File summarization | ~199,000 cumul. input | ~41,000 cumul. input | 4.9× |
| T3: FizzBuzz (multi-step) | ~121,000 cumul. input | ~132,000 cumul. input | 0.9×* |
| T3: FizzBuzz (Fable 5 re-run) | ~298,000 cumul. input | ~133,000 cumul. input | 2.2× |
| Quality benchmark (avg/pass) | ~268,000 input tokens | ~72,000 input tokens | 3.7× |
| Cache writes (T2, Sonnet) | 53,839 tokens | 1,003 tokens | 54× |
| Cache writes (T2, Fable 5) | 50,053 tokens | ~960 tokens | 52× |

*One observation of one task shape. A strictly sequential task would push Claude Code's request count back up.

## Architecture Differences

### Claude Code
- **Full platform bootstrap**: 27 tools including background-agent suite (CronCreate, Monitor, Task delegation, worktree management, push notifications)
- **Rich system prompt**: 3-block structure with behavioral doctrine, safety guidance, task-management instructions, environment description
- **Progressive scaffolding**: `<system-reminder>` blocks grow with turn count (3 on first turn, 4 by first tool round trip)
- **Model-conditional prompts**: Sends different instruction payloads to different models (27,787 chars to Sonnet, 10,526 to Fable)
- **Batching advantage** (model-dependent): Parallel tool execution can reduce request count and close the total-cost gap on some tasks
- **Subagent architecture**: Each subagent gets 3,554-char system prompt + 24/27 tools — near-full re-bootstrap

### OpenCode
- **Minimal harness**: 10 classic coding tools, single system block
- **Lean system prompt**: Opens with "You are OpenCode, the best coding agent on the planet" — functional, no extra doctrine
- **Pure conversation growth**: Per-turn marginal payload is 400–2,200 chars of conversation content only
- **Model-agnostic payloads**: Byte-identical across Sonnet and Fable — no model-specific prompt engineering
- **Serial tool execution**: One tool call per turn, which multiplies baseline cost on multi-step tasks
- **Lean subagent design**: 1,379-char system prompt + 5 tools per subagent

## Implications

### Cost
Claude Code's larger baseline means higher per-session cost in almost all measured scenarios. The exception is when aggressive batching reduces request count enough to offset the baseline difference — but this advantage proved model-dependent (held on Sonnet, failed on Fable 5). On the quality benchmark (identical outcomes), Claude Code cost 3.7× more.

### Latency
OpenCode completed the quality benchmark lanes in 1–2 minutes vs Claude Code's 4–8 minutes. The larger payload incurs processing cost even when cached.

### Context Pollution
An 85,000-token bootstrap occupies >40% of a 200K context window on every single request, shrinking the room for actual code before compaction kicks in and spends yet more tokens summarizing. This is immune to cache discounts.

### Cache Inefficiency
Claude Code's prefix instability — three distinct request classes per session, variable system bytes between sessions, mid-session re-writes — means cache write costs (billed at 1.25× or 2× premium) accumulate significantly. On identical tasks, Claude Code wrote 52–54× more cache tokens than OpenCode.

### Vendor Incentives
As noted in the HN discussion: Anthropic controls both the model and the harness, creating an incentive to maximize token consumption. OpenCode and other third-party harnesses must compete on efficiency.

## Verdict

For **cost-sensitive or high-volume API usage**, OpenCode's leaner baseline and cache-stable prefixes provide substantial savings with equivalent task completion quality on the measured benchmark. Claude Code's larger platform may earn its tokens on genuinely hard engineering tasks requiring background agents, skills, and orchestration — but two sources of waste are independent of quality: (1) mid-session cache re-writes of byte-identical content, and (2) silently ignored instruction files.

## Cross-References

- [[entities/claude-code]] — Claude Code product page
- [[entities/opencode|OpenCode]] — OpenCode harness
- [[concepts/coding-agents/coding-agents]] — Overview of AI coding agents
- token efficiency — Token efficiency in LLM systems
- [[concepts/context-engineering/context-management]] — Context window management strategies
- [[concepts/prompt-caching]] — Prompt caching economics and mechanics
- [[concepts/harness-engineering]] — Agent harness design principles
