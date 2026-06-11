---
title: "Anthropic Infrastructure Postmortems (2025-2026)"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - anthropic
  - infrastructure
aliases:
  - Claude quality degradation
  - Anthropic postmortem
  - Claude Code quality issues
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_a-postmortem-of-three-recent-issues.md
  - raw/articles/2026-05-08_anthropic-engineering_april-23-postmortem.md
  - https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
  - https://www.anthropic.com/engineering/april-23-postmortem
related:
  - infrastructure-noise-agent-evals
  - anthropic
---
# Anthropic Infrastructure Postmortems (2025-2026)

Detailed postmortem analyses of two major quality degradation incidents published by Anthropic. Two-part structure covering infrastructure bugs (Aug-Sep 2025) and product changes (Mar-Apr 2026).

---

## Part 1: Aug-Sep 2025 — Three Infrastructure Bugs

> "We never reduce model quality due to demand, time of day, or server load."

### Bug 1: Context Window Routing Error

- **Duration**: August 5 – September 16-18, 2025
- **Impact**: Up to 16% of Sonnet 4 requests (at worst). 30% of Claude Code users affected at least once
- **Cause**: Short-context requests misrouted to 1M-token context servers
- **Aggravating factor**: "Sticky" routing (once misrouted, subsequent requests followed)
- **Fix**: Routing logic correction (September 4-18)

### Bug 2: Output Corruption

- **Duration**: August 25 – September 2, 2025
- **Impact**: Opus 4.1/4, Sonnet 4 — Thai and Chinese characters mixed into English prompts, syntax errors in code
- **Cause**: Misconfiguration from TPU server runtime performance optimization. Low-probability tokens incorrectly assigned high probability
- **Fix**: Change rollback + added detection tests for unexpected character outputs

### Bug 3: XLA:TPU Approximate Top-k Miscompilation

- **Duration**: August 25 – September 4-12, 2025
- **Models**: Haiku 3.5 (confirmed), Sonnet 4/Opus 3 (possible)
- **Cause**: Latent XLA compiler bug where approximate top-k operations returned completely wrong results for specific batch sizes and model configurations
- **Complexity**: A workaround from December 2024 was incorrectly removed, exposing the bug. bf16/fp32 mixed precision mismatch
- **Fix**: Approximate top-k → exact top-k + fp32 standardization

### Detection Difficulty

- Each bug produced different symptoms on different platforms at different frequencies → appeared as "random, inconsistent degradation"
- Internal evaluations failed to capture user-reported degradation (Claude is good at recovering from individual mistakes)
- Privacy constraints hindered user interaction investigation

---

## Part 2: Mar-Apr 2026 — Claude Code Quality Degradation

> Three independent changes manifested as "broad, inconsistent degradation."

### Issue 1: Default Reasoning Effort Misconfiguration

- **Change**: March 4 — reasoning effort changed from `high` to `medium`
- **Reason**: Mitigate extreme latency in `high` mode (UI freezing)
- **Result**: Reports pouring in that Claude Code "became less smart"
- **Fix**: April 7 — Opus 4.7 set to `xhigh`, others set to `high`
- **Lesson**: Intelligence should be prioritized over latency (users prefer slow, high quality)

### Issue 2: Reasoning History Deletion Bug

- **Change**: March 26 — optimization to clear old thinking for sessions idle over 1 hour
- **Bug**: Supposed to run once, but kept clearing every turn until session end
- **Symptom**: Forgetfulness, repetition, strange tool choices. Memory loss of "why it made that decision"
- **Secondary effect**: Cascading cache misses → faster rate limit consumption
- **Fix**: April 10
- **Discovery path**: Opus 4.7's Code Review found it in a PR (Opus 4.6 missed it)

### Issue 3: Redundancy Reduction System Prompt

- **Change**: April 16 — added instruction "inter-tool text ≤25 words, final response ≤100 words"
- **Result**: 3% coding quality degradation (both Opus 4.6/4.7)
- **Fix**: April 20 immediate rollback
- **Lesson**: Insufficient impact evaluation of system prompt changes. Broader evaluation suite needed

### Prevention Measures

- More internal staff using the same Claude Code build as public release
- Model-specific broad evaluation + soak period + gradual rollout for system prompt changes
- Code Review tool improvements (support additional repositories as context)
- Detailed explanation of product decisions published on @ClaudeDevs (X)

---

## Common Patterns

1. **Detection lag**: Multiple independent changes overlapping, appearing as "random degradation"
2. **Internal evaluation limitations**: Existing evaluation suites fail to capture user experience degradation
3. **Privacy vs investigation**: Restricted access to user data delays root cause identification
4. **Importance of user feedback**: Specific reports via `/feedback`, `/bug`, and social media were key to eventual resolution

## See Also

- [[entities/anthropic]] — Anthropic entity
- [[concepts/coding-agents/infrastructure-noise-agent-evals]] — Infrastructure noise in agent evals
- [[concepts/ai-benchmarks/ai-resistant-evaluations]] — AI-resistant evaluation design
