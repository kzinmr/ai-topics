---
title: "AI Coding Cost Optimization — Ronin's Complete System"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags:
  - coding-agents
  - optimization
  - economics
  - token-economics
  - model-routing
  - prompt-caching
  - context-engineering
aliases: ["ai-coding-cost-optimization", "cut-ai-coding-bill"]
sources:
  - "https://x.com/deronin_/status/2054255152555545079"
  - "https://x.com/i/article/2053183959341711361"
  - "https://x.com/DeRonin_/status/2054235707791778034"
---

# AI Coding Cost Optimization — Ronin's Complete System

A comprehensive, battle-tested system for reducing AI coding bills by 80%+ through context discipline, multi-model routing, prompt caching, and workflow optimization. Documented by [[entities/ronin-deronin|Ronin]] (@DeRonin_), who cut his own monthly bill from $4,200 to $312.

## Core Philosophy

> "90% of your AI coding bill is paying for context you didn't need to send" — attribution to Andrej Karpathy

The fundamental mistake is thinking the fix is "use cheaper models." The real fix is **stop sending tokens you didn't need to send**. Context discipline is the lever; model selection is downstream of it.

## The 10 Token Wastes (Summary)

1. **Auto-context loading 50 files for 30-line fixes** — 80% input waste, $1.20/turn
2. **Running Opus on lint/format tasks** — 30x overpay vs Haiku
3. **Tool call loops re-sending full repo** — 5x context cost per agentic flow
4. **Sonnet as default model** — Kimi 2.6 matches quality at 1/6 cost
5. **Streaming on stable-prefix workflows** — kills prompt cache, 10x cost
6. **"Just in case" file includes** — 80k-token prompts that should be 3k
7. **Per-session knowledge rebuilding** — SKILL.md once vs re-figuring environment every run
8. **Single-model setups** — premium tier on every task
9. **10 small questions one at a time** — 10 prefix charges vs one batched call
10. **Stacked subscriptions (Pro + Plus + Cursor Pro)** — use one, pay for three

## Token Economics

| Token Type | Description | Pricing Characteristic |
|------------|-------------|----------------------|
| **Input** | Everything sent TO the model | Baseline cost |
| **Output** | Everything returned BY the model | 3-5x input cost |
| **Cached** | Input from recent requests | ~10% of regular input cost |
| **Reasoning** | Internal "thinking" tokens | Billed but invisible to user |

Mid-2026 approximate pricing:
| Model | Input/M | Output/M | Use Case |
|-------|---------|----------|----------|
| Opus 4.6 | ~$15 | ~$75 | Architecture, security review (10% of work) |
| GPT-5 | ~$10 | ~$40 | Premium alternative to Opus |
| Sonnet 4.6 | ~$3 | ~$15 | Edge cases only — **NOT a default in 2026** |
| Haiku 4.5 | ~$1 | ~$5 | Lint, format, single-line edits |
| Kimi 2.6 | ~$0.50 | ~$2 | **Daily driver** — 90% of implementation work |

## The 5 Token Traps

### 1. Re-Sending Entire Repo on Every Turn
**Problem**: Auto-context includes 30-50 unchanged files every turn. 50 files = ~80,000 input tokens = $1.20/turn × 50 turns = $1,800/month.
**Fix**: Turn off auto-context. Use grep/ripgrep before fetching. `@file` not `@codebase`.
**Savings**: 60-80% on input tokens.

### 2. Tool Call Loops That Spiral
**Problem**: Agent calls tool → re-sends context → calls another tool → re-sends. Paying full input cost 5x per agent loop.
**Fix**: Batch related tool calls. Summarise outputs aggressively. Replace loops with deterministic Python helpers.
**Savings**: 3-5x cost reduction on agentic flows.

### 3. Premium Models on Cheap Tasks
**Problem**: Opus to fix a typo = $0.60. Haiku does it for $0.02. Sonnet for refactoring = $0.12. Kimi matches at $0.04.
**Fix**: Multi-model router. Kimi 2.6 default. Opus reserved for 10% of decisions.
**Savings**: 95% on cleanup tier, 10-15x on long agentic loops.

### 4. Streaming Killing Prompt Cache
**Problem**: Streaming responses defeat prompt caching. Paying 10x for tokens that should cost cents.
**Fix**: BATCH for stable-prefix workflows. STREAM for interactive UX.
**Savings**: 30-50% on cached-prefix calls.

### 5. Context Bloat From "Just in Case"
**Problem**: Including utils.ts, test file, schema "just in case." 80k-token prompts for 30-line fixes.
**Fix**: Grep first. If grep finds no reference, model doesn't need the file. Summarise old context periodically.
**Savings**: 70%+ on input tokens.

## Router Architecture (Manual, Config-Based)

Unlike [[concepts/model-routing|Augment Prism]]'s automated per-turn routing, Ronin's approach uses a static config that routes based on task type keywords:

```yaml
default: kimi-2.6-instruct
routes:
  planning:
    model: claude-opus-4-6
    triggers: ["plan", "architect", "design system", "security review"]
  implementation:
    model: kimi-2.6-instruct
    triggers: ["review", "debug", "refactor", "implement"]
  cleanup:
    model: claude-haiku-4-5
    triggers: ["lint", "format", "fix typo", "rename"]
  boilerplate:
    model: ollama:qwen3:7b
    triggers: ["autocomplete", "stub", "boilerplate"]
caching: {enabled: true, prefix_cache: true}
context: {max_tokens: 50000, auto_summarize_after: 15, use_grep_first: true}
```

### Why Kimi 2.6 as Default (Not Sonnet)

Kimi 2.6 in 2026 matches Sonnet 4.6 on shipped code quality at 1/6 the cost:
- 30-step refactor agent: $1 on Kimi vs $5 on Sonnet
- Background agents: $15-30/mo on Kimi vs $200-400/mo on Sonnet
- 256k context window matches Sonnet's coherence at upper range
- Moonshot rate limits dramatically more generous

## 7 Practical Techniques

| # | Technique | Mechanism | Savings |
|---|-----------|-----------|---------|
| 1 | **Prompt Caching** | Stable context in cached prefix. Work in 5-min chunks (TTL). Cached = ~10% of regular input. | 60-90% on stable input |
| 2 | **Grep Before Fetching** | `rg "symbol" --type ts -l` before including files. 90% of time, 30 lines is enough. | 70-90% on input |
| 3 | **Profile Tool Calls** | Log every call's token count for 1 week. Find spiraling loops. Fix top 3 worst. | 30-50% |
| 4 | **Graduated Skills (SKILL.md)** | Capture working workflows. Next run skips discovery. Deploy workflow: $4→$0.18/run. | 10-20x per repeated workflow |
| 5 | **Local Models (Ollama)** | Qwen 3 / Llama 3 for autocomplete, boilerplate. $0/token. | 100% on boilerplate tier |
| 6 | **Aggressive Summarisation** | Every 10-15 turns, summarise, drop originals. 200k→5k compression. | 95% on continued sessions |
| 7 | **Batch Small Requests** | 10 questions in one prompt vs 10 API calls. | 70-90% on input |

## Cost Benchmarks (Real Tasks)

| Task | Opus 4.6 | GPT-5 | Sonnet 4.6 | Kimi 2.6 |
|------|----------|-------|------------|----------|
| Refactor 500-line file | $0.42 / ★9.5 | $0.32 / ★9.4 | $0.12 / ★9.0 | **$0.04 / ★9.2** |
| Build CRUD endpoint | $0.18 / ★9.0 | $0.14 / ★9.0 | $0.06 / ★9.0 | **$0.02 / ★9.0** |
| Debug stack trace | $0.08 / ★9.5 | $0.07 / ★9.4 | $0.03 / ★9.0 | **$0.01 / ★9.1** |
| Architecture plan | **$0.65 / ★9.8** | $0.50 / ★9.7 | $0.22 / ★8.5 | $0.08 / ★9.2 |

Key insight: Kimi 2.6 matches or beats Sonnet on quality across all 4 tasks while costing 3-4x less. Opus/GPT-5 only meaningfully ahead on architectural decisions.

## 30-Day Rollout Plan

| Week | Focus | Key Actions | Cumulative Savings |
|------|-------|-------------|-------------------|
| 1 | Stop the Bleeding | Enable prompt caching, turn off auto-context, install ripgrep | 30-40% |
| 2 | Switch Default Model | Route default to Kimi 2.6, lint to Haiku, Opus for planning only | 70-85% |
| 3 | Profile & Fix Loops | Enable verbose tool logging, find top 3 worst loops, replace with batched calls | 80-90% |
| 4 | Graduate & Localize | Write SKILL.md for 3 repeat workflows, set up Ollama + Qwen 3 | 85-90% |

## When Premium Models Still Win (The 10%)

Always use Opus/GPT-5 for:
- System architecture decisions
- Security-critical code review
- Complex multi-file refactors with cross-cutting concerns
- Debugging concurrency/race conditions
- Compiler/formal-verification work

**Decision rule**: If the cost of a wrong answer > 100x the model cost difference → use premium. Price the model to the cost of failure, not the cost of the call.

## Related Concepts

- [[concepts/model-routing]] — Augment Prism: automated per-turn routing vs Ronin's manual config-based approach
- [[concepts/tokenmaxxing]] — Quality-over-quantity philosophy; Ronin's system is the practical implementation
- [[concepts/token-economics]] — Token cost framework underlying routing decisions
- [[concepts/prompt-caching]] — Technical deep-dive on how prompt caching works
- [[concepts/context-engineering]] — Token-efficient context management techniques
- [[concepts/skill-graph]] — Ronin's Skill Graph architecture for content engines
- [[concepts/agent-engineering-guide-2026]] — Broader agent engineering practices including cost management
- [[concepts/codex-prompting]] — Coding agent prompt strategies
- [[entities/ronin-deronin]] — Ronin's profile and other works
