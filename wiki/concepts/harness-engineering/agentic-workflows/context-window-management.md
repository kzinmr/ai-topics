---
title: "Context Window Management"
type: concept
aliases:
  - context-window-management
  - context-management
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - agentic-engineering
  - prompting
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/context-window-management/"
---

# Context Window Management

Patterns for effectively managing coding agent context windows to optimize quality and cost. Detailed in Simon Willison's [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/context-window-management/).

## Core Principles

> "Context windows have a maximum size, and they have a cost. Every token in the context costs money and compute — and the more you put in, the harder it is for the model to pay attention to the right parts."

Context windows are a finite resource. You cannot put in unlimited content.

## Drew Breunig's 5 Context Patterns

Willison introduced a systematic approach to context management through [Drew Breunig's analysis](https://simonwillison.net/2025/Jun/29/how-to-fix-your-context/):

### 1. Context Poisoning
> "When a hallucination or other error makes it into the context, where it is repeatedly referenced."

A phenomenon where hallucinations or errors become embedded in the context, cascading negative effects across subsequent responses.

**Countermeasure**: Validate agent outputs; reset the session before incorrect information becomes entrenched in the context.

### 2. Context Distraction
> "When a context grows so long that the model over-focuses on the recent context, neglecting what it was originally told."

When context grows too long, the model forgets initial instructions and becomes overly focused on recent content.

**Countermeasure**: Context Summarization, periodic session refresh.

### 3. Context Quarantine
> "The act of isolating contexts in their own dedicated threads."

Willison calls this the **sub-agents** pattern. Run each task in independent threads/sessions to prevent context contamination and diffusion.

**Implementation examples:**
- Launching new Claude Code sessions
- Independent workspaces in parallel agents
- State handover via `plan.md` files

### 4. Context Pruning
> "Removing irrelevant or otherwise unneeded information from the context."

Remove unnecessary information from the context to focus the model's attention on important parts.

### 5. Context Summarization
> "Boiling down an accrued context into a condensed summary."

Summarize accumulated context from long sessions and carry it over to the next session.

### 6. Context Offloading
> "The act of storing information outside the LLM's context."

One of the most practical patterns. The agent writes files like `plan.md` or `notes.md` to the repository, and reads from them when needed, bypassing context window limitations.

**Implementation examples:**
- Coding agents creating and updating `plan.md` during work
- Reading files in the next session to restore state
- Functioning as persistent memory

## Tool Loadout Pattern

> "Selecting a subset of tools to enable for a prompt, based on research that shows anything beyond 20 can confuse some models."

Keeping the number of tools available to an agent at or below 20 is effective. Too many tools diffuse the model's attention.

## Effective Context Window is 50-60%

> *"Context rot sets in as the window fills. Effective window is ~50-60% of max."*
> — Sankalp (Claude Code 2.0 Guide)

Model performance degrades as the context fills. 50-60% of the maximum token count is the practical limit.

| Model | Max Context | Practical Limit |
|-------|-------------|-----------------|
| Opus 4.5 | 200K tokens | ~120K tokens |
| GPT-5.2 | 400K tokens | ~240K tokens |
| Gemini 3 Pro | 1M tokens | ~600K tokens |

**Sankalp's recommendation**: When context usage reaches 60%, use `/compact` or `/handoff` to reorganize the session.

## Practical Context Management Strategies

| Strategy | Method | Effect |
|----------|--------|--------|
| Session Splitting | Context Quarantine | Prevents contamination and distraction |
| File Externalization | Context Offloading | Bypasses context constraints |
| Periodic Summarization | Context Summarization | Maintains long sessions |
| Tool Limiting | Tool Loadout | Focuses attention |
| Irrelevant Info Removal | Context Pruning | Improves quality |
| 60% Rule | `/compact` at 60% | Prevents performance degradation |

## Related Concepts

- [[concepts/harness-engineering/agentic-workflows/how-agents-work]] — Agent internals (including token caching)
- [[concepts/subagents]] — Context Quarantine implementation patterns
- [[concepts/agentic-engineering]] — Parent concept
- [[concepts/harness-engineering/agentic-workflows/cognitive-debt]] — Consequences of failed context management

## References

- [[entities/simon-willison]] — Creator of Agentic Engineering Patterns
- [Drew Breunig — How to Fix Your Context](https://simonwillison.net/2025/Jun/29/how-to-fix-your-context/)

