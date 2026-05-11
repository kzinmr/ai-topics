---
title: "CLAUDE.md Rules — Karpathy's Behavioral Guidelines for AI Coding Agents"
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [claude-code, agentic-engineering, context-engineering, coding-agents, developer-tooling]
sources: [raw/articles/2026-05-09_mnilax_claude-md-12-rules.md]
aliases: ["claude-md", "CLAUDE.md", "Karpathy CLAUDE.md"]
---

# CLAUDE.md Rules

Karpathy's CLAUDE.md rules are a set of behavioral guidelines for AI coding agents, encoded in a project-level `CLAUDE.md` file. Derived from Andrej Karpathy's January 2026 observations about LLM coding failure modes, they represent the most-starred single-file developer resource of 2026 — 120,000+ GitHub stars for what is essentially 4 sentences in a markdown file.

## Origin

In late January 2026, Andrej Karpathy posted a thread describing three failure modes he observed while using Claude Code extensively:

1. **Hidden assumptions**: Models make wrong assumptions and run with them without checking, don't seek clarifications, don't surface tradeoffs.
2. **Over-engineering**: Overcomplicate code and APIs, bloat abstractions, don't clean up dead code.
3. **Unintended side effects**: Change/remove comments and code they don't sufficiently understand.

Developer Forrest Chang read the thread and converted Karpathy's complaints into 4 actionable behavioral rules in a single `CLAUDE.md` file, open-sourced on GitHub at [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills). It hit 5,828 stars in the first day, 60,000 bookmarks in two weeks.

## The Four Principles

| Principle | Addresses | Rule |
|-----------|-----------|------|
| **1. Think Before Coding** | Wrong assumptions, hidden confusion | State assumptions explicitly. If uncertain, ask. Present multiple interpretations. Push back when warranted. |
| **2. Simplicity First** | Over-engineering, bloated abstractions | Minimum code that solves the problem. Nothing speculative. No abstractions for single-use code. If 200 lines could be 50, rewrite. |
| **3. Stay in Scope** | Unintended side effects, orthogonal damage | Only modify what the task asks for. Don't "improve" unrelated code. Don't remove comments you don't understand. |
| **4. Goal-Driven Execution** | Task drift, incomplete verification | Define success criteria. Loop until verified. Multi-step tasks: state a brief plan with verification steps. |

**Tradeoff**: These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## Evolution: From 4 to 12 Rules

As of May 2026, practitioners have extended the rules. The original 4 rules addressed January 2026 code-writing problems. But by May 2026, agent-orchestration problems had emerged that didn't exist when the template was written:

- Multi-step agents with hook cascades
- Skill loading and context management  
- Multi-codebase work with shared state
- Agent fleet coordination patterns

@Mnilax tested the original 4 rules on 30 codebases over 6 weeks and reported mistake rates dropping from ~40% to under 3% on tasks that played to their strengths. Then added 8 more rules covering agent orchestration, reporting 12 rules total with mistake rate 41% → 3%.

## CLAUDE.md Compliance Dynamics

Key findings from extensive use:

- Anthropic docs state CLAUDE.md is **advisory** — Claude follows it ~80% of the time
- Past **200 lines**, compliance drops sharply because important rules get buried in noise
- Most developers: bloat to 4,000+ tokens (compliance drops to 30%), skip entirely (5x token waste), or copy once and forget (breaks silently as codebase shifts)
- The optimal format: short (<70 lines), focused on behavioral constraints, not feature checklists

## Why CLAUDE.md Matters

CLAUDE.md is arguably **the most under-leveraged file in the AI coding stack**. It is:

- **Free**: No API, no build step, no dependencies
- **Portable**: Works with any Claude Code-compatible coding agent
- **Compounding**: Encodes team conventions and architectural decisions that every agent run follows automatically
- **The simplest form of context engineering**: Drop a file in your repo, and every agent run respects your conventions

The broader lesson: behavioral constraints beat feature checklists for directing AI coding agents. The repo's virality (120K+ stars, fastest-growing single-file repo of 2026) signals where the real bottleneck in AI-assisted coding lies — not in model capability, but in the quality of instructions and guardrails.

## Related

- [[entities/andrej-karpathy]] — Originator of the observations
- [[entities/forrest-chang]] — Creator of the andrej-karpathy-skills repo
- [[entities/claude-code]] — Claude Code
- [[concepts/context-engineering]] — Context engineering discipline
- [[concepts/agentic-engineering]] — Agent-centric software engineering
- [[concepts/claude-code-auto-mode]] — Claude Code auto mode
