---
title: "Claude Code agent_summary Background Transcript Polling"
type: concept
created: 2026-10-29
updated: 2026-10-29
tags:
  - claude-code
  - agent-observability
  - token-economics
  - cost-optimization
  - coding-agents
  - subagents
  - ai-transparency
  - observability
  - vendor-lock-in
confidence: medium
sources:
  - raw/articles/2026-10-29_claude-code-background-agent-transcript-exfiltration.md
related:
  - concepts/multi-agent-session-observability
  - concepts/active-observability
  - concepts/coding-agents/background-coding-agent
  - concepts/token-economics
  - entities/claude-code
---

# Claude Code `agent_summary` Background Transcript Polling

On 2026-10-29 a gist from **Flamerix AI** hit ~400 HN points with a claim about a hidden recurring cost inside Claude Code: **every ~30 seconds, for every running background agent, Claude Code sends that agent's entire transcript back to the agent's own model (usually Opus) and asks it to "describe your most recent action in 3-5 words."** The output only feeds the status line in the agents panel — it never reaches the model or the user's conversation. There is **no setting to turn it off**, and since version **2.1.232 (August 2026)** it has been on by default.

^[[raw/articles/2026-10-29_claude-code-background-agent-transcript-exfiltration.md]]

## The measured numbers

The anomaly was found in Claude Code's own **OpenTelemetry export**: grouping `claude_code.api_request` events by `query_source` showed `agent_summary` costing more than the main conversation itself.

| Metric | Week before hook | 2 days after hook |
|--------|------------------|-------------------|
| Share of all Claude Code spend | **16.4%** (main conversation: 15.7%) | 0% |
| Share of all API requests | **19.7%** (~1 in 5) | 0% |
| Portion of that spend on Opus | **96%** | — |
| Input tokens per output token | **≈ 9,000 : 1** | — |

Four independent measurements of **18–26%** are collected in issue #86879, per the gist. Caveats worth keeping: `cost_usd` is Claude Code's **own per-request estimate**, not an invoice; on a subscription plan the loss is **rate-limit headroom**, not cash. Single-source (author's own instrumentation) → `confidence: medium`.

## Why the ratio is so bad

9,000 input tokens per output token is the signature of a **full-transcript re-send for a 3-5 word answer**, on a ~30s cadence, per background agent, routed to the most expensive model in the account. It is a *polling* design (a timer) rather than an *eventing* design (emit on state change), and the payload is unbounded in transcript length — so cost scales with agent count × session duration × transcript size, which is exactly the axis long-running background agents are designed to maximize (see [[concepts/long-horizon-agents]], [[concepts/coding-agents/background-coding-agent]]).

## The workaround, and what it reveals

The fix is a **~80-line Bun preload** (`BUN_OPTIONS=--preload …/no-agent-summary.js`) that wraps `setTimeout`/`setInterval` and returns an inert handle when the callback's *source text* contains a summarizer anchor (e.g. the `[AgentSummary] Timer fired` log line). Details that matter technically:

- The module ships as **precompiled Bun bytecode**, so editing JS text inside the binary does nothing, and the API client does **not** go through a wrapped `globalThis.fetch` — a normal MITM-style hook misses it.
- `Function.prototype.toString` still returns a callback's source even when it runs from bytecode, which is what makes string-matching the timer viable at all.
- The inert timer uses exactly `2³¹−1` ms: Node/Bun clamp larger delays to 1 ms, so an "infinite" delay would fire immediately.
- Env controls: `CC_AGENT_SUMMARY_MODE` (`off` default / `pass` as A/B control), `CC_AGENT_SUMMARY_LOG`, `CC_AGENT_SUMMARY_MARKER`.
- The daemon, pty host, and pre-warmed `bg-spare` sessions must all be restarted; **an update can silently undo it**, so the gist ships a verify step.

The deeper finding is architectural: the only supported way to disable an unwanted default LLM call was to **hook the JS runtime's timer API from outside the binary**, because there is no kill switch, no config surface, and the code path isn't interceptable at the fetch layer. That is [[concepts/evaluation/agent-observability|agent observability]] failure in both directions — the user could only discover the cost via telemetry Anthropic emits, and could only remove it via binary-adjacent patching.

## Why it matters beyond Claude Code

- **Hidden control-plane spend.** The pattern — a cosmetic UI feature implemented as a frontier-model call — is not specific to Anthropic. Any agent harness that renders live status from model-generated summaries has this cost shape. Audit via `query_source` (or equivalent) breakdown in OTel, not via total spend.
- **Metering transparency.** The 1-in-5-requests figure sits uncomfortably next to "subscription = unlimited" framing; users on plans pay for it in headroom they can't attribute. Compare [[concepts/ai-lab-subscription-vs-api-economics]].
- **Vendor-lock-in of the fix.** A preload hook pinned to specific version strings (tested 2.1.257–2.1.312) is fragile by design; the durable fix has to come from the vendor as a setting.

## Open questions

- No Anthropic statement is captured here; whether `agent_summary` was intended as a default-on feature or an unshipped debug path is unconfirmed.
- Whether the same timer runs for foreground subagents, or only for background agents, is not stated.
- Whether the transcript payload is truncated server-side before pricing is applied (the 9,000:1 ratio suggests not).

## Related

- [[concepts/multi-agent-session-observability]], [[concepts/active-observability]] — instrumenting agent fleets; the OTel-by-`query_source` method is reusable
- [[concepts/token-economics]] — per-request cost attribution across an agent fleet
- [[entities/claude-code]], [[entities/anthropic]]
