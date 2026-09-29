---
title: "Unreal Agent"
created: 2026-09-29
updated: 2026-09-29
type: concept
tags:
  - harness-engineering
  - coding-agents
  - ai-agents
  - developer-tooling
  - token-economics
  - context-engineering
confidence: medium
sources:
  - raw/articles/2026-09-09_unreal-labs-unreal-agent-moe-mobile.md
---

# Unreal Agent

**Unreal Agent** is a from-scratch agent harness (SDK + interactive TUI) built by Unreal Labs, designed around a single thesis: *the harness must not waste the model's context.* Published 2026-09-09 ([blog](https://unrealauto.github.io/blog/Unreal-Agent/)). With the same model (GPT-6 Sol xhigh), it beats vendor harnesses on three agentic benchmarks — and its win is driven by **tool-call architecture**, not prompt tuning.

> *"There's no golden path for building an agent-first product. Big-brand vendors offer different SDKs, each with trade-offs that might not be immediately apparent. So we built our own."*

## Headline Results (same model: GPT-6 Sol xhigh, Sep 2026)

| Benchmark | Unreal Agent | Codex (vendor baseline) | Pi |
|---|---|---|---|
| Terminal-Bench 2.1 | **84.0** | 79.3 | 82.1 |
| SWE-atlas | **74.5** | — | 71.5 |
| DeepSWE | **72.7** | 69.4 | 70.6 |
| ALE (Agents Last Exam, `ale-cli`) | **12.3** | 11.9 | 11.8 |

+4.7pt over Codex on Terminal-Bench; +2.6pt on the hardest benchmark (ALE). Modest but consistent across all four — the interesting signal is *how* it wins, since the model is held constant.

## Three Architectural Bets

1. **Minimal harness footprint.** Simple prompts, token-optimized tool results, **no sub-agents, no workflows** — the anti-pattern to [[concepts/agent-team-swarm/_index|multi-agent orchestration]].
2. **Asynchronous tool calling.** Every tool call immediately appends an "in-progress" event-log record while execution continues in the background; the final result is appended on completion, then the LLM is invoked. More heavy tool calls per model turn, zero tokens burned on polling/waiting. Keeping prompt caches warm across this pattern was "an interesting engineering challenge in itself."
3. **More tool work per model turn.** Fewer model turns and fewer input tokens for the same outcome.

The mechanism is explicit: *"On the surface, Unreal Agent achieves the same outcomes with fewer model turns and fewer input tokens"* — i.e. the benchmark gain is a [[concepts/token-economics|token economics]] gain, echoing [[concepts/elo-per-token-analysis|Elo-per-token analysis]].

## Context in the Harness Debate

This is 2026 evidence for the "harness > model" camp against [[concepts/harness-commoditization|harness commoditization]]: a small team, same frontier model, beating Codex/Pi via async tool-call design and context frugality. The paper's own framing ("harness design is a research area in its own right") cites **HarnessTax** (Pan, Yang, Arabzadeh, Chiang, Stoica, Zaharia, 2026) — *"How Much Does Harness Matter for Coding Agents?"*

**Caveats:** vendor-ran comparison (Unreal Labs built the harness under test); single model tested; the async two-item tool-call pattern is *underspecified in the Responses API docs* — the authors hit provider rejections (non-OpenAI) where the `function_call_output` status field had no effect.

## Platform Support (SDK)

- iOS app with on-device model support (MLX)
- Web app with persistent agent sessions in WebAssembly
- TUI (full-screen keyboard-driven interactive agent)
- Multi-platform session support

## Related

- [[concepts/harness-engineering]] — harness > model consensus this extends
- [[concepts/harness-commoditization]] — the thesis this argues against
- [[concepts/ai-benchmarks/terminal-bench]] / [[concepts/ai-benchmarks/deepswe-benchmark]] — benchmark venues
- [[concepts/benchmark-ceiling]] — why only ALE (~12%) still discriminates
- [[concepts/kv-cache]] — the cache-warmth constraint behind async tool calls
- [[concepts/elo-per-token-analysis]] — rate-of-token-conversion framing
