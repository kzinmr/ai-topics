---
title: "Harness Engineering 101 (Isuru Maduranga)"
type: concept
created: 2026-10-24
updated: 2026-10-24
tags:
  - harness-engineering
  - agent-harness
  - agent-engineering
  - education
  - coding-agents
  - open-source
sources:
  - https://github.com/IsuruMaduranga/harness-engineering-101
  - raw/articles/2026-10-22_harness-engineering-101-readme.md
related_concepts:
  - harness-engineering
  - agent-harness
---

# Harness Engineering 101 (Isuru Maduranga)

**Harness Engineering 101** is a 16-chapter open-source book by [[entities/isuru-maduranga|Isuru Maduranga]] (v1.1, October 2026) that derives the entire agent stack from one premise: *an LLM API is stateless — every turn you send the whole conversation as a JSON array and get text back — so a **harness** is simply the program that builds, maintains, and protects that array.* Everything the field calls "agents" is then presented as a set of patches to that single loop, each patch existing because something concrete broke. A ~300-line toy agent in plain Python grows into a real harness across the chapters.

> "The LLM is the brain. The harness is the body."

**▶ One-line summary**: One JSON array, 16 patches — each agent "feature" is framed as the minimal fix for a specific failure, plus what that fix costs.

## Structure: failure → minimal patch → cost

Every chapter has the same three-part shape, which is the book's main pedagogical contribution: capabilities are not features to adopt but trade-offs to price.

| Part | Chapters | Failure being patched |
|---|---|---|
| **I — The Wire** (nothing is magic) | 1 It's Just a JSON Array · 2 The Brain: A Next-Token Black Box · 3 Tools: JSON Mapped to Functions · 4 The Agent Loop · 5 Caching: Why Order Matters | "How do I even talk to this thing?" → the brain can't touch the world → resending the array gets expensive |
| **II — Running Long** (the array under pressure) | 6 Context Is a Budget, Not a Bag · 7 Subagents: Fork the Context · 8 Steering the Running Loop · 9 Background Work and Time | The window fills up → one array can't hold all the work → the brain drifts mid-task → the loop is synchronous, the world isn't |
| **III — The Ecosystem** (naming what you already understand) | 10 Every Framework Is a Wrapper Around Chapter 1 · 11 Extending the Body: MCP, Skills, Deferred Loading, Hooks · 12 Debugging the Array | Abstraction anxiety → capabilities don't fit in the array → you can't fix the prompt you can't see |
| **IV — Trust, Domains, Data** | 13 Reflexes and Guardrails · 14 Case Study: Coding Agents · 15 RAG Was a Harness Pattern All Along | The loop will do something dumb → how specialized must the body be? → a thousand names for one idea |
| **Epilogue + Appendices** | 16 Build Your Own · A One Harness, Many Brains (routing, prompt tiers, cost engineering) · B Worktrees and Isolation · C Modes and Plan Mode · D Retries, Rate Limits, Streaming | Complete annotated toy harness; the unglamorous plumbing |

Three claims do the argumentative work:

1. **Frameworks are wrappers.** Chapter 10's thesis is that every agent framework adds an abstraction layer over the single array loop from chapter 1 — an anti-"abstraction anxiety" demystification move.
2. **RAG is a harness pattern, not a subsystem** (ch. 15): retrieval is one of many ways to decide what enters the array, not its own architectural tier.
3. **Subagents are context forks** (ch. 7), matching the "subagents as Tools" reading found elsewhere in the wiki (see [[concepts/unbundled-agents]]).

## Provenance and disclosure

The author discloses using AI in the book's own production: every chapter was drafted by hand from experience building **WSO2 MI Copilot**, **WSO2 BI Copilot** and **One Code**; Claude Code and One Code were used to reorder chapters to lead with the answer (the Minto pyramid), polish the English, generate diagrams, and write the charting code. The book is built with mdBook (mermaid diagrams) and ships `src/harness/` — a runnable toy harness, one file per stage — so the progression is reproducible rather than descriptive.

The ideas are the same ones used in **One Code**, the author's open-source coding agent built on `pi` (see [[entities/mario-zechner-badlogicgames]]).

## Why it matters

Most harness material in the wild is either vendor architecture posts (OpenAI Codex, Anthropic Managed Agents) or term coinage. This is the closest thing to a **first-principles curriculum**: it gives the [[concepts/harness-engineering]] field a teachable spine where each component — caching, compaction, subagents, steering, guardrails, MCP, hooks — is introduced as a response to a named failure with a stated cost, rather than as a feature list. It is the natural on-ramp beneath [[concepts/harness-engineering/agent-harness]].

## Limitations

- **Single practitioner's frame.** The failure→patch→cost structure is a strong organizing device but also a lens that flattens alternatives (e.g. it treats RAG exclusively as harness plumbing).
- **Coding-agent centred.** Chapters 14 and appendix C are coding-specific; the general-agent claims are extrapolated from that domain.
- **No formal evaluation.** Unlike the benchmark-driven harness writing in this wiki, the book's claims about what each patch costs are argued and demonstrated, not measured.

## Related

- [[concepts/harness-engineering]] — the broader discipline
- [[concepts/harness-engineering/agent-harness]] — component taxonomy this book teaches bottom-up
- [[concepts/context-engineering]] — chapter 6's "context is a budget" framing
- [[concepts/unbundled-agents]] — subagents-as-tools, same reading as chapter 7
- [[entities/isuru-maduranga]] — author; One Code, WSO2 Copilot lineage

## Sources

- [Harness Engineering 101 — GitHub](https://github.com/IsuruMaduranga/harness-engineering-101) · [read online](https://isuruwijesiri.com/harness-engineering-101/) (raw: `raw/articles/2026-10-22_harness-engineering-101-readme.md`)
