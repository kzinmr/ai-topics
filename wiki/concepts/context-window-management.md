---
title: "Context Window Management"
created: 2026-04-13
updated: 2026-04-13
tags: [context-window, token-management, prompt-engineering, claude-code, llm-optimization]
aliases: ["context-window-optimization", "token-budget-management", "conversation-hygiene"]
related: [[claude-code-best-practices]], [[claude-code-source-patterns]], [[inference-speed-development]], [[agentic-engineering]]
---

# Context Window Management

**Context Window Management** encompasses the strategies, patterns, and techniques for effectively working within the finite context limits of LLM-powered coding agents. As sessions grow longer, developers face **context bloat** — where accumulated conversation history degrades model performance, increases costs, and causes instruction drift.

The core challenge: **LLMs have a fixed context window, but software projects have unbounded complexity.** Effective management is the difference between a productive AI session and a confused, expensive one.

---

## The Context Budget Problem

Every interaction with an AI coding agent consumes a shared budget:

```
System Prompt + CLAUDE.md + Conversation History + Tool Outputs + New Input ≤ Context Window
```

When this budget is exhausted:
- The model starts **forgetting earlier instructions**
- Response quality **degrades non-linearly**
- API costs **increase with every token**
- Sessions become **slower to process**

---

## Key Strategies

### 1. Session Partitioning

**Divide work into discrete sessions** rather than maintaining one continuous conversation.

| Approach | Pros | Cons |
|----------|------|------|
| Single long session | Full history available | Context bloat, expensive, slow |
| Partitioned sessions | Fresh context per task | Lost information between sessions |
| Hybrid (CLAUDE.md + sessions) | Best of both | Requires discipline to maintain CLAUDE.md |

**Best Practice**: Start a new session for each distinct task. Use CLAUDE.md to carry forward essential project knowledge.

### 2. Context Compression

When a session approaches its limit, compress the conversation while preserving critical information:

#### The `<analysis> → <summary>` Pattern (from Claude Code source)

1. Model writes **detailed analysis** of the conversation so far
2. Model produces **condensed summary** preserving key decisions and user feedback
3. Analysis block is **stripped** — only summary enters context

```
Compression Prompt (simplified):
"Summarize the conversation so far. Pay special attention to:
- What the user asked for
- What approaches were tried
- What the user liked/disliked
- What decisions were made
- What still needs to be done"
```

#### Manual Compression Techniques

- **`/compact` command** — Trigger built-in compression
- **Explicit summary** — Ask the model to summarize before continuing
- **Key extraction** — Copy critical decisions to CLAUDE.md

### 3. Instruction Decay Prevention

As conversations grow, models tend to **forget or dilute early instructions**. Countermeasures:

| Technique | How It Works | When to Use |
|-----------|--------------|-------------|
| Dynamic injection | Re-insert key rules at decision points | Long sessions |
| System reminders | XML-tagged context blocks in user messages | Anthropic pattern |
| CLAUDE.md pinning | Persistent project-level instructions | Always |
| Session resets | Start fresh when task changes | Task boundaries |

### 4. Fork Patterns

**Clone a conversation** to explore alternatives without polluting the main context.

```bash
# Claude Code fork primitive
/fork
```

**When to fork:**
- Exploring alternative implementations
- Answering side questions ("BTW, how does X work?")
- Testing risky changes without affecting main thread
- Parallel investigation of different modules

**Fork criterion** (from Claude Code source):
> "Fork yourself when the intermediate tool output isn't worth keeping in your context. The criterion is qualitative — 'will I need this output again?' — not task size."

---

## Token Economics

### Cost-Aware Development

Every token costs money. Optimize for value, not verbosity:

| Action | Token Cost | Value |
|--------|-----------|-------|
| Reading a 1000-line file | High | Medium (may not need all) |
| Grep for specific pattern | Low | High (targeted) |
| Full conversation summary | Medium | High (enables compression) |
| Repeating already-stated context | High | Zero (wasteful) |

### Cache-First Engineering

From [[claude-code-source-patterns]]:
> "Every design decision in the codebase is evaluated through a single lens: does this invalidate the prompt cache?"

**User-level cache optimization:**
1. Keep system prompts stable across sessions
2. Reuse CLAUDE.md content (cached between runs)
3. Avoid unnecessary schema changes
4. Use delta-based tool announcements

---

## Anti-Patterns

### 1. The Hoarding Session

**Problem**: Never clearing context, assuming "more is better."

**Result**: Model becomes confused, slow, and expensive. Key instructions get buried.

**Fix**: Regular compression and session resets.

### 2. The Context Dump

**Problem**: Pasting entire files into prompts instead of referencing them.

**Result**: Wastes tokens on irrelevant content.

**Fix**: Use tool-based file reading (the model reads files on-demand).

### 3. The Drifting Task

**Problem**: Starting with one task, gradually shifting to another without session reset.

**Result**: Model carries irrelevant context from the original task.

**Fix**: Explicit session boundaries. New task = new session.

### 4. The Over-Compressed Summary

**Problem**: Compressing too aggressively, losing critical nuance.

**Result**: Model makes decisions based on incomplete information.

**Fix**: Preserve user feedback and explicit constraints in summaries.

---

## Relationship to Agentic Engineering

Context management is a **meta-skill** for agentic engineering:

- **Good context management** → efficient, reliable AI collaboration
- **Poor context management** → wasted tokens, confused agents, buggy code

The [[inference-speed-development]] paradigm depends on effective context management: fast iteration requires clean, focused contexts.

---

## Practical Checklist

Before starting a session:
- [ ] Is this a new task? → Start fresh session
- [ ] Does CLAUDE.md reflect current project state? → Update if needed
- [ ] Are MCP servers configured correctly? → Verify connections

During a session:
- [ ] Is the conversation getting long? → Consider `/compact`
- [ ] Am I exploring alternatives? → Use `/fork`
- [ ] Is the model losing focus? → Re-state key constraints

Before ending a session:
- [ ] Were important decisions made? → Update CLAUDE.md
- [ ] Is there follow-up work? → Note it for next session
- [ ] Can I summarize progress? → Document for future reference

---

## Related Concepts

- [[claude-code-best-practices]] — User-facing patterns that depend on context management
- [[claude-code-source-patterns]] — Internal Anthropic patterns for context handling
- [[inference-speed-development]] — Why fast iteration requires clean contexts
- [[agentic-engineering]] — The methodology this supports
- [[ai-coding-reliability]] — How context drift leads to bugs

## Sources

- [Sankalp: My Experience with Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/) — Context bloat and session hygiene patterns
- [Peter Steinberger: Shipping at Inference Speed](https://steipete.me/posts/2025/shipping-at-inference-speed) — Context as a limiting factor in iteration speed
- [Shlok Khemani: What I Found Interesting in Claude Code's Source](https://www.shloked.com/writing/claude-code-source-patterns) — Compression, fork, and cache-first patterns from Anthropic's implementation
- [Anthropic: Claude Code Documentation](https://docs.anthropic.com/claude-code) — Official context management features
