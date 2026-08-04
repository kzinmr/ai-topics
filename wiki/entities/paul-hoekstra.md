---
title: Paul Hoekstra
type: entity
created: 2026-05-02
updated: 2026-08-04
status: L3
tags:
  - person
  - agentic-engineering
  - claude-code
  - context-management
  - blogger
aliases:
  - paulhoekstra
sources:
  - https://paulhoekstra.substack.com/
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part1-configuration-layer.md
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part2-capability-layer.md
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part3-orchestration-layer.md
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part4-guardrails-layer.md
  - raw/articles/2026-05-02_paul-hoekstra-claude-code-statusline-aquarium.md
  - raw/articles/2026-05-02_paul-hoekstra-visual-output-claude-code.md
  - raw/articles/2026-06-03_paul-hoekstra-context-rot.md
---

# Paul Hoekstra

**Paul Hoekstra** is a data engineer and author of the Substack publication **Paul's Pipeline** (launched April 2026). He writes about AI, data engineering, and side projects, with a focus on practical agentic engineering workflows using coding agents like Claude Code and Codex.

## Context Rot: Why AI Gets Worse the More You Explain (June 2026)

Hoekstra's most-cited standalone essay provides a mechanistic explanation of **[[concepts/context-engineering/context-rot|context rot]]** — the steady decline in how reliably a model uses what is in its context, the more you put there. It reframes the phenomenon as *not* a bug but an inherent property of transformer architecture:

### The Gap: Nominal vs. Functional Context
- **Nominal context**: how much you can physically cram in before the model refuses
- **Functional context**: the length where it still does your task well
- Functional is always smaller, and the gap widens the more you load in

### Three Causes (They Stack)
1. **Attention is a pie that never gets bigger** — softmax forces attention shares to sum to one regardless of input size; splitting across a million tokens thins every slice. Cites Liu et al. "Lost in the Middle" (2023).
2. **The model loses track of where things are** — RoPE position encoding laps its dial beyond 8K-32K tokens; positions at 412K and 478K have nearly identical angles, so the model can't tell which is closer. Rescaling tricks (YaRN) keep writing fluent but don't restore retrieval.
3. **The model barely practised at long lengths** — training data is mostly under 8K tokens; behavior at 4K is backed by trillions of tokens of practice, at 100K by a few billion at best. >80% of training exposure is at positions ≤ 1024.

### Evidence & Practical Advice
- **MRCR v2 (OpenAI)**: GPT-5.5 falls to 54% recall at 500K tokens; Grok 4.20 (2M window) down at 12%.
- **Chroma study (July 2025)**: same decay shape across 18 frontier models — "a generation newer, and the shape did not change."
- **Key insight**: "Context is not the enemy. Useless context is." Value of added context climbs fast then flattens while cost keeps climbing — they cross.
- **The big lever is resetting**: trim context or start a clean conversation. "The drift was never about how clearly you explained. It was about how much had piled up behind you."
- Points to his aquarium statusline article as tooling for watching context fill up in Claude Code.

See [[raw/articles/2026-06-03_paul-hoekstra-context-rot]] for the full article. This essay extends his Agentic Engineering framework into the [[concepts/context-engineering/context-window-management|context window management]] domain, positioning context discipline as a core layer of agent engineering.

## Agentic Engineering Series (March–April 2026)

Hoekstra's signature contribution is a 4-part series defining the **Agentic Engineering Framework** — a systematic approach to configuring, equipping, orchestrating, and safeguarding AI coding agents.

### The Four Layers

1. **[[concepts/harness-engineering/agentic-engineering-configuration-layer|The Configuration Layer]]** — CLAUDE.md, Skills, pre-commit hooks. The foundational layer that prevents agents from defaulting to "defensive sludge."
2. **[[concepts/harness-engineering/agentic-engineering-capability-layer|The Capability Layer]]** — MCP tools, live documentation, visual output, persistent memory strategies.
3. **[[concepts/harness-engineering/agentic-engineering-orchestration-layer|The Orchestration Layer]]** — Subagents, Git worktrees, agent teams, context quality management.
4. **[[concepts/harness-engineering/agentic-engineering-guardrails-layer|The Guardrails Layer]]** — Permission systems, sandboxing, AST-grep, homoglyph attack prevention.

### Core Philosophy

> "Engineers who were already writing good code can now ship much more, much faster. Engineers who were writing dogwater before... well, they're mostly just writing lots more of that."

The difference between elite and mediocre agent results is the **Configuration Layer** — structured project-level instructions that override the model's default "sycophantic" behavior.

## Other Notable Articles

### Visual Output with Claude Code (April 2026)
Argues that Claude Design is a wrapper around capabilities Claude Code already has. Covers frontend-slides, Remotion, Figma MCP, and draw.io MCP for generating slides, video, UI designs, and architecture diagrams.

### Claude Code Statusline Customization (April 2026)
Shows how to transform the empty Claude Code statusline into a real-time dashboard for development metrics, ops monitoring, and personal productivity — including creative visualizations like a Doom HUD and aquarium.

## Key Contributions

- **Named the Configuration Layer problem** — identified that agents without structured project instructions default to low-quality "defensive sludge"
- **<HARD-GATE> enforcement pattern** — XML-like tags that Claude gives disproportionate weight to
- **Three-layer memory strategy** — MEMORY.md (project), episodic-memory (session), QMD (knowledge)
- **Context over Roles design principle** — read-heavy delegation as sweet spot for subagent orchestration

## Related Entities

- [[entities/simon-willison]] — Agentic Engineering patterns (precursor framework)
- [[concepts/harness-engineering/agentic-engineering]] — Main concept page
- [[concepts/context-engineering/context-rot]] — Context rot concept page (his June 2026 essay is a key source)
- [[concepts/context-engineering/context-window-management]] — Context window management in production

## Sources

- [Paul's Pipeline (Substack)](https://paulhoekstra.substack.com/)
- [Context Rot: Why AI Gets Worse the More You Explain](https://paulhoekstra.substack.com/p/context-rot-the-constraint-agentic) (June 2026)
- Various raw articles in `wiki/raw/articles/`
