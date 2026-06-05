---
title: Randy Olson
type: entity
aliases: [randyolson, randal_olson]
created: 2026-06-05
updated: 2026-06-05
status: L2
tags:
  - person
  - ai-agents
  - agent-skills
  - data-visualization
  - data-science
  - evaluation
  - personal-software
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - raw/articles/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
---

# Randy Olson

**Data scientist, r/dataisbeautiful moderator, co-founder of Good Eye Labs.** Randy has worked in AI and ML for 15-20 years and has been writing data-viz code since the early 2010s. He publishes a daily data-viz post using a single high-signal chart workflow powered by an agent skill that generates, critiques, and iterates on charts using **Tuftean criteria**.

## Quick Facts

| | |
|---|---|
| **X/Twitter** | [@randal_olson](https://x.com/randal_olson) |
| **Role** | Co-founder, [Good Eye Labs](https://goodeyelabs.com) |
| **Reddit** | Moderator, r/dataisbeautiful |
| **Experience** | 15-20 years in AI/ML; data-viz code since early 2010s |
| **Focus** | Agent-driven data visualization, generator-evaluator pattern |

## Daily Data-Viz Workflow

Randy publishes a **data-viz post every morning**, generated end-to-end by an agent skill:

1. **Pick the idea** — One sentence (e.g., "The history of marriage and divorce in the USA")
2. **Fire the skill** — Sets up isolated working directory, searches web for authoritative data (CDC, government/education sources preferred), pulls data, generates 3 chart variants in parallel, scores them, picks one, runs verifier loop
3. **Walk away** — Dataset discovery takes 5-10 minutes; rest is fast
4. **Come back** — Read the chart and agent's log; check that log matches chart
5. **Last-5% human pass** — Almost entirely one problem: detecting when an inline annotation overlaps a line ("If anyone solves this consistently, you're a billionaire")
6. **Publish, then edit the skill** — Anything the verifier missed goes into the next iteration

## The Generator-Evaluator Pattern

Randy's key contribution is the **generate-and-verify** pattern encoded in his data-viz skill:

### Two Verification Gates

1. **Deterministic Python verifier** — Checks what scripts can measure (DPI, file integrity, basic constraints)
2. **Tuftean LLM-as-judge** — Evaluates what scripts can't (annotation placement, data-to-ink ratio, whether the chart reveals the data)

> *"You don't want to just tell it what to do, you also want to tell it how to check it."*

The evaluator returns a pass-or-fail verdict with improvement feedback. On failure, the feedback becomes the agent's next fix-it instructions, and the skill rewrites the chart and runs both gates again.

> *"Even still, if an eval flips or is wrong 80% of the time, it's still directionally valuable."*

The agent decides when the chart is good enough. LLM-as-judge has known variance; **generate-and-verify still beats generate-and-hope**.

### Tuftean Criteria

The LLM judge evaluates charts against Edward Tufte's principles:
- **Data-to-ink ratio** — maximize data representation, minimize chart junk
- **Annotation discipline** — clear, non-overlapping labels
- **Clarity** — chart reveals the data, not obscures it
- **Whether the chart actually says what it's supposed to**

## Three Principles for Designing Skills

1. **Skills are polite notes, not programs** (Jeremiah Lowin's framing) — A markdown file that politely asks the agent to do a thing. Writing one is cheap; iterate fast as you notice failure modes.

2. **Deterministic in scripts, ambiguous to the LLM** (Randy's framing) —
   > *"A skill plus an LLM is kind of a program."*
   What you can specify exactly (DPI, file integrity, axis units) goes in scripts. What needs judgment (which chart type, Tufte compliance) goes to the LLM. The skill is the seam.

3. **Skills are living documents** —
   > *"Even the harness, unless you're hardcore and making your own, is kind of fixed too. The skills are really the thing that can evolve with you."*
   Randy tweaks his data-viz skill after most mornings: phases, design checklist, verifier criteria. The skill is a living document, not a frozen artifact.

## Related People

| Person | Connection |
|--------|-----------|
| **[[entities/wes-mckinney\|Wes McKinney]]** | Fellow guest on Show Us Your Agent Skills Ep. 1 |
| **[[entities/jeremiah-lowin\|Jeremiah Lowin]]** | Fellow guest; skills-as-polite-notes framing |
| **[[entities/hugo-bowne-anderson\|Hugo Bowne-Anderson]]** | Host of Show Us Your Agent Skills |

## See Also

- [[entities/jeremiah-lowin]]
- [[entities/wes-mckinney]]
- [[concepts/generator-evaluator-pattern]]
- [[concepts/personal-software]]

## References

- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)
- Show Us Your Agent Skills, Episode 1 (May 2026)

## Log

- **2026-06-05**: Initial entity page created from "The Agentic Software Factory" article.
