---
title: "Harness Design for Long-Running Apps — Anthropic's Multi-Agent Architecture"
tags: [harness-engineering, multi-agent, agentic-engineering]
sources:
  - raw/articles/2026-05-08_anthropic-engineering_harness-design-long-running-apps.md
created: 2026-04-13
updated: 2026-08-10
type: concept
---

# Harness Design for Long-Running Apps — Anthropic's Multi-Agent Architecture

Practical design for long-running autonomous agents by Anthropic Labs (Prithvi Rajasekaran). An architecture that scales the **GAN-inspired loop** (Generator ↔ Evaluator) to full-stack development.

## Core Problem: Why Naive Implementations Fail

Long-running autonomous agents consistently degrade through two failure modes:

### 1. Context Anxiety & Window Limits

> "Context resets—clearing the context window entirely and starting a fresh agent, combined with a structured handoff that carries the previous agent's state and the next steps—addresses both these issues. This differs from compaction, where earlier parts of the conversation are summarized in place... A reset provides a clean slate, at the cost of the handoff artifact having enough state for the next agent to pick up the work cleanly."

**Anthropic's Solution**: 
- **Context Reset** recommended over **Compaction**
- Instead of summarizing in place, restart with a completely fresh agent
- Include sufficient state in the handoff artifact so the next agent can pick up cleanly

### 2. Self-Evaluation Bias

LLMs tend to be overconfident in their own intermediate outputs. Separating generation and evaluation is crucial.

## Frontend Design Experiment: Making Subjective Quality Gradable

Before scaling to full-stack coding, Rajasekaran validated the GAN-inspired loop on frontend design, where the self-evaluation problem is most visible (untouched Claude gravitates to safe, predictable layouts). Two insights shaped the harness:

1. **Subjective quality can be made gradable** — "Is this design beautiful?" is hard to answer consistently, but "does this follow our principles for good design?" gives Claude something concrete to grade against.
2. **Separating generation from grading** creates a feedback loop that drives stronger outputs.

**Four grading criteria** (given to both generator and evaluator, with design quality and originality weighted most heavily to counteract "AI slop" patterns):

| Criterion | Definition |
|-----------|-----------|
| **Design quality** | Coherent whole vs collection of parts; distinct mood and identity |
| **Originality** | Custom decisions vs template layouts, library defaults, purple-gradient AI tells |
| **Craft** | Typography hierarchy, spacing, color harmony, contrast (competence check) |
| **Functionality** | Usability independent of aesthetics — can users complete tasks without guessing |

**Mechanics**: built on the Claude Agent SDK; generator creates HTML/CSS/JS; evaluator uses **Playwright MCP** to navigate the live page, screenshot, and study the implementation before scoring each criterion and writing a detailed critique. 5–15 iterations per generation (full runs up to 4 hours); the generator decides after each evaluation whether to refine the current direction or pivot aesthetics entirely. The evaluator was calibrated with few-shot examples with detailed score breakdowns to align judgment and reduce score drift. A striking result: on a Dutch art museum prompt, iteration 10 scrapped the polished landing page and reimagined the site as a 3D room with CSS-perspective checkered floor and doorway-based navigation — a creative leap unseen in single-pass generation. The criteria wording itself steered output (e.g., "museum quality" phrasing caused visual convergence), and later iterations trended more complex but were not always preferred over middle iterations.

## Multi-Agent Architecture: GAN-Inspired Loop

| Agent | Role | Key Design Choice |
|-------------|------|-------------|
| **Planner** | Expands 1-4 sentence prompts into ambitious product specs | Avoids premature technical over-specification. Focuses on product context and AI capability integration |
| **Generator** | Iteratively builds features | Sprint (v1) or continuous execution (v2). State handoff via structured artifacts |
| **Evaluator** | QA, grading, feedback | Live interactive testing via **Playwright MCP**. Negotiates "sprint contracts" before coding |

**Communication Pattern**: File-based state transfer. Agents read and write files to maintain context across sessions.

## Sprint Contracts (Anthropic's Unique Memory Pattern)

```
Generator proposes scope and success criteria
         ↓
Evaluator reviews
         ↓
Negotiate until agreement
         ↓
Coding → Evaluation → Feedback → Fix
```

**Significance as a memory system**:
- Contracts are stored in **files**, not in conversation
- Each sprint runs in an independent context
- State is externalized, allowing continuation even after agent restart

## Harness Evolution: Opus 4.5 → 4.6

As model capabilities improve, harness complexity is systematically reduced:

| Element | Opus 4.5 | Opus 4.6 |
|------|----------|----------|
| Sprint | Required | Removable |
| Context Reset | Required | Removable |
| Evaluator | Continuous feedback | End-of-run or conditional use |
| Reason | Cannot maintain consistency without rigid structure | Long-term context, planning, and debugging capabilities improved |

> **Key Rule**: The Evaluator only offloads tasks that exceed the model's reliable solo execution capability. Otherwise it is overhead.

## Performance Comparison

| Harness Type | Task | Time | Cost | Result |
|---------------|--------|------|--------|------|
| **Solo Agent** | Retro Game Maker | 20 min | $9 | Core gameplay broken, poor UI |
| **Full Harness (v1)** | Retro Game Maker | 6 hours | $200 | Polished UI, working physics, 16 feature specs / 10 sprints |
| **Updated Harness (v2)** | Browser DAW | ~4 hours | $124.70 | Feature arrangement view, mixer, transport, AI agent-driven |

## Relationship to Memory System Design

### Anthropic vs ChatGPT vs Claude (Connecting to Shlok Khemani's Analysis)

| Design Element | Anthropic Harness | Claude Memory | ChatGPT Memory |
|---------|-------------------|---------------|----------------|
| **State Storage** | File-based (sprint contracts) | CLAUDE.md + .agent/ | Proprietary database |
| **Session Management** | Context Reset (new agent) | Stateless (full context each time) | Stateful (memory persistence) |
| **Evaluation Isolation** | Evaluator agent (independent) | Self-evaluation (in-prompt) | Self-evaluation (in-prompt) |
| **Scalability** | Harness simplifies as model capabilities improve | Depends on filesystem | Limited by database schema |

### Key Insights

1. **Context Reset > Compaction** — Anthropic recommends launching a new agent over in-conversation summarization
2. **File-Based State Transfer** — Inter-session state is maintained in files (same pattern as Claude's CLAUDE.md)
3. **Evaluator Isolation** — Separating generation and evaluation avoids self-evaluation bias
4. **Model-Capacity-Driven Simplification** — As models improve, harnesses can be simplified (avoiding over-engineering)

## Sources

- [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps) — Prithvi Rajasekaran, Anthropic Labs, Mar 24, 2026
- [[raw/articles/2026-05-08_anthropic-engineering_harness-design-long-running-apps.md]] — Raw article (published 2026-03-24, scraped 2026-05-08)

## See Also

- [[entities/_index]]
- [[concepts/memory-systems-design-patterns]]
- [[concepts/meta-harness]]
- [[concepts/coding-agents/long-context-coding-agents]]
- [[concepts/evaluation/llm-evaluation-harness]]
