---
title: "Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k"
date: 2026-07-12
source: https://systima.ai/blog/claude-code-vs-opencode-token-overhead
tags: [claude-code, opencode, coding-agents, token-efficiency, tool-calling, system-prompt, prompt-caching, subagents]
---

# Claude Code vs OpenCode: Token Overhead Comparison

**Author**: Systima (systima.ai)
**Published**: 2026-07-12
**Source**: https://systima.ai/blog/claude-code-vs-opencode-token-overhead

## Executive Summary

Systima conducted a measurement study comparing the token overhead of Claude Code (2.1.207) and OpenCode (1.17.18), both pinned to Claude Sonnet 4.5, with cross-validation on Claude Fable 5. The key finding: Claude Code sends approximately 33,000 tokens of system prompt, tool schemas, and injected scaffolding before the user prompt even arrives; OpenCode sends about 7,000.

## Method

A logging proxy was spliced between each harness and the model endpoint:

```
harness (Claude Code / OpenCode)
→ logging proxy (captures request payloads + response usage)
→ model endpoint
```

The proxy records both the exact JSON payload and the API usage block (input tokens, cache writes, cache reads, output tokens).

**Conditions:**
- Fresh config directories, no MCP servers, no user settings, empty workspace
- Tasks: T1 (reply "OK" — isolates fixed overhead), T2 (read file and summarize), T3 (write-run-test-fix FizzBuzz loop)
- Quality check: separate 10-lane benchmark, 5 runs per harness, hash-verified test suite

**Note:** Traffic passed through Meridian gateway (~6,200 token envelope on Sonnet path, subtracted from all metered figures).

## Part I: The Floor

### Fixed overhead of saying "OK" (22-character prompt)

| Component | Claude Code | OpenCode |
|---|---|---|
| System prompt | 27,344 chars, 3 blocks | 9,324 chars, 1 block |
| Tool schemas | 27 tools, 99,778 chars | 10 tools, 20,856 chars |
| First-message scaffolding | 7,997 chars of `<system-reminder>` blocks | none |
| Actual prompt | 22 chars | 22 chars |
| **First-turn payload (calibrated)** | **~32,800 tokens** | **~6,900 tokens** |

OpenCode's system block opens with "You are OpenCode, the best coding agent on the planet" plus 10 classic coding tools.

Claude Code includes 27 tools: coding core plus background-agent and orchestration suite (CronCreate, Monitor, Task family, worktree management, push notifications). Three injected reminder blocks carry agent delegation types, available skills, and user context.

### Zero tools (pure harness prompt)

| | Claude Code | OpenCode |
|---|---|---|
| System prompt (chars) | 26,891 | 8,811 |
| System prompt (tokens) | ~6,500 | ~2,000 |

Even with no tools, Claude Code's instruction set is over 3x OpenCode's.

### One-tool task (T2: file summarization)

| Metric | Claude Code | OpenCode |
|---|---|---|
| HTTP requests | 6 | 4 (+1 Haiku title call) |
| Cumulative metered input | ~199,000 tokens | ~41,000 tokens |

### Multi-step task (T3: FizzBuzz loop)

| Metric | Claude Code | OpenCode |
|---|---|---|
| Model requests | 3 | 9 (+1 title call) |
| Tool-calling style | parallel batch, one round trip | one tool call per turn |
| Cumulative metered input | ~121,000 tokens | ~132,000 tokens |

Claude Code batched all file writes and script executions into a single parallel tool round trip; OpenCode made one tool call per turn. Baseline re-sent on every request means request count multiplies baseline, so totals converged.

### Model dependency (Fable 5 re-run)

On Fable 5, the floor gap shrank to ~3.3x (vs 4.7x on Sonnet). Claude Code's system prompt is model-conditional: 27,787 chars to Sonnet but only 10,526 to Fable, with tools trimmed from 99,778 to 82,283 chars. OpenCode's payload was byte-identical across both models.

The multi-step convergence did NOT survive: Claude Code took 6 requests on Fable (vs 3 on Sonnet) with an 85,686-token mid-session cache re-write, landing at ~298,000 tokens vs OpenCode's 133,000.

## Part II: The Multipliers

### Multiplier 1: Instruction files
A 72KB AGENTS.md added ~20,000 tokens per request to both harnesses. Claude Code 2.1.207 ignored AGENTS.md entirely — only ingested CLAUDE.md. OpenCode reads either filename.

### Multiplier 2: MCP servers
~1,000–1,400 tokens per small server, per request. Five servers added 4,900 tokens (payload) to Claude Code and 6,967 (metered) to OpenCode.

### Multiplier 3: Framework templates
An 8,405-char BMAD-style template (~2,100 tokens) enters conversation history and re-carries on every subsequent request. A 9-request session re-sends it 9 times.

### Multiplier 4: Subagents
Claude Code fanned to 2 subagents: cumulative metered input reached **513,000 tokens** vs **121,000 for direct execution** (4.2x multiplier). Each subagent carries its own bootstrap (3,554-char system prompt + 24 tools).

### Multiplier 5: Extended thinking
Not quantified due to gateway interference, but mechanism confirmed: thinking blocks join conversation history and compound with every other multiplier.

### The "Everything" number
Real configuration (11 MCP servers + 72KB instruction file):
- OpenCode: 90,817 tokens cold cache write (179 tools, 277KB schemas)
- Claude Code: ~75,000 tokens (118 tools, 311KB payload)

~12x configuration multiplier against OpenCode's ~7,000-token floor.

## Cache Economics

### Key findings:
- **OpenCode**: byte-identical prefixes across every request and every run. Zero mid-session cache re-writes on Sonnet.
- **Claude Code**: three distinct request classes per session (warmup probe, main conversation, subagent calls), each with its own cache entry. System bytes vary between sessions.

On the identical file-summarize task:
- Claude Code wrote 53,839 cache tokens across 5 requests (including full mid-task re-write of ~43k prefix)
- OpenCode wrote 1,003 cache tokens

Reproduced on Fable 5: 50,053-token mid-session re-write, 52x cache-write gap.

Three costs survive cache discount:
1. The write itself (re-paid after 5-min TTL pauses)
2. Reads multiplied by request count (inflated by subagents and serial tool loops)
3. Context-window consumption (immune to caching): 85k bootstrap = >40% of 200k window

## Quality Check

10-lane benchmark (2 date utilities, 10-assert test suite, 5 fresh workspaces each):

| Metric | Claude Code | OpenCode |
|---|---|---|
| Pass rate | 5/5 | 5/5 |
| Avg metered cost per passing run | ~268,000 input tokens | ~72,000 input tokens |
| Time per lane | 4-8 min | 1-2 min |

Both passed identically. Cost ratio: ~3.7x.

## Caveats

- Single machine, single version pair, small n
- Harness prompts change frequently — July 2026 snapshot
- Local gateway sat in measurement path (subtracted for metered figures)
- Claude Code's batching advantage is model-dependent, not a harness constant

## Reproduction

Open-source measurement rig at: github.com/systima-ai/agentic-coding-tools-comparison
Set ANTHROPIC_BASE_URL at the proxy, give harness fresh config + empty workspace, add multipliers one at a time.

---

## HN Discussion Context

[Source: https://hn.algolia.com/api/v1/items/48883275 — 687 points, 70 comments]

Notable comments:
- **MallocVoidstar**: Questions use of old model (Sonnet 4.5), notes article appears AI-written
- **slopinthebag**: Anthropic is incentivized to maximize costs; other harnesses must trade off performance vs cost
- **bel8/drtournier**: Pi agent sends even less (~1k tokens or less)
- **nubg**: Argues it doesn't matter because after first turn it's cached (article responds: cache writes, reads, and context consumption survive discounts)
- **PUSH_AX**: Questions whether tokens are the right metric — like comparing contractor quotes by dollar amount
- **token_roast**: Suggests renting GPU and writing own harness (~200 lines)
- **mcv**: Subagents burn budget fastest; 7 subagents burned through budget before any finished
- **eigenblake**: Notes cache hit tokens are billed at 1/10th
- **systima (author)**: Updated post after feedback to include in-depth task and quality comparison
