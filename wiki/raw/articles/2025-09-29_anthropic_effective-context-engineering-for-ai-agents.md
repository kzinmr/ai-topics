# Effective Context Engineering for AI Agents

**Source:** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
**Date:** September 29, 2025
**Authors:** Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield (Anthropic Applied AI team)

---

## Key Concepts

**Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts.

**Context** is the set of tokens included when sampling from a large-language model (LLM). The engineering problem at hand is **optimizing the utility of those tokens against the inherent constraints of LLMs** in order to consistently achieve a desired outcome.

## Context Engineering vs. Prompt Engineering

- **Prompt engineering:** writing and organizing instructions for one-shot tasks.
- **Context engineering:** managing *the entire context state* — system instructions, tools, MCP, external data, message history — across multi-turn, long-horizon agent loops.

> "Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information."

## Why It Matters

- **Context rot:** model recall degrades as token count increases — a performance *gradient*, not a cliff.
- **Attention budget:** like human working memory, LLMs have limited capacity; every new token depletes it.
- **n² attention:** transformer's pairwise attention stretches thin with length, and models are trained more on shorter sequences.
- Therefore, building capable agents demands deliberate context curation.

## Core Principle

> Find the **smallest possible set of high-signal tokens** that maximize the likelihood of some desired outcome.

## Anatomy of Effective Context

### System Prompts
- Use **clear, simple, direct language** at the "right altitude."
- Avoid over‑specified (brittle if‑else) and over‑general (vague).
- Organize with **sections** (`## Tool guidance`, `## Output description`) using XML tags or Markdown headers.
- **Start minimal:** test with the best model, then iteratively add constraints only for observed gaps.

### Examples (Few-Shot)
- "For an LLM, **examples are the 'pictures' worth a thousand words**."
- Goldilocks zone: too few → model hallucinates format; too many → overfitting, cost, context rot.

### Tools and MCP
- Tool definitions are a direct tax on the attention budget.
- Best practices:
  - Name and describe tools, inputs, outputs **clearly and consistently**
  - Use shared naming conventions across all tools
  - Omit rarely used tools → retrieve or activate them dynamically
  - Provide specific input descriptions with format and examples
  - Avoid unnecessary tokens (verbose descriptions, custom wrapper fields, unused tool configs)
- **Progressive disclosure:** Cursor Agent syncs MCP tool descriptions to a folder with short names; agent reads full descriptions only when relevant.

### Just-in-Time Retrieval
- Rather than pre-processing all relevant data upfront, maintain **lightweight identifiers** (file paths, stored queries, web links) and use tools to dynamically load data at runtime.
- Claude Code example: writes targeted queries, stores results, uses Bash `head`/`tail` to analyze large data **without loading full data objects into context**.
- Mirrors human cognition: file systems, inboxes, bookmarks instead of memorizing entire corpuses.

## Techniques for Long-Horizon Agents

### Compaction
- When context exceeds ~95% of the window, summarize the conversation history.
- Claude Code **auto-compact** summarizes full user-agent trajectory.
- **Art of compaction:** selecting what to keep vs. discard. Overly aggressive compaction can lose subtle but critical context.

### Structured Note-Taking (Memory)
- Agents persist information to external storage (files, databases) rather than keeping everything in context.
- Claude Playing Pokémon example: agent maintains precise tallies across thousands of game steps — "for the last 1,234 steps I've been training my Pokémon in Route 1, Pikachu has gained 8 levels toward the target of 10."
- Memory enables learning across sessions.

### Sub-Agent Delegation
- Delegate tasks to sub-agents with **isolated context windows**, each focused on a narrow sub-task.
- Anthropic's multi-agent researcher: sub-agents "operate in parallel with their own context windows, exploring different aspects of the question simultaneously."
- Trade-offs: higher token usage (up to 15× more), need for careful planning and coordination.

## Key Insight

> Context engineering represents a fundamental shift in how we build with LLMs. As models become more capable, the challenge isn't just crafting the perfect prompt—it's thoughtfully curating what information enters the model's limited attention budget at each step.
