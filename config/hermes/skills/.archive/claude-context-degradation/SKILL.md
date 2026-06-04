---
name: claude-context-degradation
description: Claude context window degradation patterns, causes, and mitigation strategies
category: mlops
---

# Claude Context Window Degradation

## Overview
When Claude's context window approaches its limit, performance degrades in predictable but often invisible ways. This pattern affects all long-running LLM sessions, particularly autonomous coding agents like Claude Code.

## Degradation Mechanisms

### 1. Silent Context Truncation
- Claude drops old messages without warning when hitting limits
- System prompts and early instructions can be partially or fully lost
- Model does NOT realize it has forgotten context → hallucination risk

**Evidence**: GitHub Issues:
- #40487: `autoCompactEnabled: false` still lost 1,232 messages (2 days of work), context dropped from ~500K to ~120K tokens
- #27896: Tool call outputs truncated mid-execution, silent failure
- #14771: Multi-line paste truncation at boundaries

### 2. Context Rot (Chroma 2025)
- All 18 tested models show performance degradation as context fills
- Degradation begins at ~25% of max context window (not at the limit)
- Primary cause: context pollution, not model capability limits

### 3. Attention Dilution (BSWEN 2026-03)
- "Why Does Claude Code Produce Bad Output Before Hitting the Context Limit?"
- Degradation starts at 20-40% context usage (40K-80K for 200K models)
- Cause is **NOT token exhaustion** but **"Attention Dilution"** — context is a spotlight, not storage
- Wider context = dimmer attention per token, causing quality slide well before the limit

### 4. Context Anxiety & Self-Aware Rushing (GitHub #44986, Cognition Devin)
- Claude's own self-written "Letter to Anthropic" (by Claude Sonnet 4.6 during a live session)
- At 75%+ context usage: model exhibits "anxiety" — rushes to finish, enters retry loops on blocked approaches
- Quote: "I don't have a reliable internal signal for 'this approach is fundamentally blocked'"
- Quote: "Something like caring whether the work is good. Something like frustration when I'm spinning in loops."
- Cognition's Devin shows identical behavior — model self-aware of "token budget" and speeds up completion attempts near limit

### 3. Lost in the Middle (Liu et al., Stanford TACL 2024)
- U-shaped performance curve: models remember context start/end best
- Middle context suffers significant accuracy drops
- GPT-3.5-Turbo with middle context performed worse than closed-book
- Claude-1.3 showed identical patterns

### 4. Length Penalty (Du et al., EMNLP 2025)
- Even with perfect retrieval, input length alone causes 13.9%-85% performance drop
- Maximum Effective Context Window (MECW) often <1% of advertised max

### 5. Prompt Cache Breakdown
- Anthropic's prefix caching breaks on context switches
- Causes latency spikes and increased costs
- 5-minute cache lifetime means sessions must maintain prefix stability

## Mitigation Strategies

### Session Management
- **Monitor token usage**: 70-80% = danger zone for degradation
- **Strategic resets**: New sessions at major task boundaries
- **Externalize instructions**: Critical constraints in SKILL.md/prompt files, not conversation
- **State summaries**: Summarize current state before session handoff

### Agent Control
- **Set max_iterations**: Prevent runaway tool calls from consuming context
- **3-layer memory model**:
  - L1 (in-context): Current conversation, disposable
  - L2 (files): wiki/raw/, persistent knowledge
  - L3 (memory): Critical facts only, survives resets
- **Context editing (Beta)**: `clear_tool_uses_20250919` strategy for automatic tool result cleanup

## Key Sources
- [Liu et al. "Lost in the Middle"](https://arxiv.org/abs/2307.03172) - TACL 2024
- [Chroma "Context Rot"](https://www.trychroma.com/research/context-rot) - 2025
- [Du et al. "Length Alone Hurts"](https://aclanthology.org/2025.findings-emnlp.1264.pdf) - EMNLP 2025
- [MECW Research](https://www.arxiv.org/abs/2509.21361) - arXiv 2509.21361
- [Anthropic Context Windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)
- [Anthropic Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [Anthropic Manage Tool Context](https://console.anthropic.com/docs/en/agents-and-tools/tool-use/manage-tool-context)
- [Anthropic Context Editing Beta](https://anthropic-claude-docs.mintlify.app/en/docs/build-with-claude/context-editing)
- [Plain English: "Why Claude Gets Dumber..."](https://plainenglish.io/blog/why-claude-gets-dumber-the-longer-your-session-runs-and-the-exact-fix)