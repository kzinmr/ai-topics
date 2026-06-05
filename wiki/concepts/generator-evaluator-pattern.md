---
title: Generator-Evaluator Pattern
type: concept
aliases: [generate-and-verify, generator-evaluator, generate-evaluate-loop]
created: 2026-06-05
updated: 2026-06-05
tags:
  - ai-agents
  - agent-skills
  - evaluation
  - verification
  - llm-as-judge
  - data-visualization
  - agent-design-patterns
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - raw/transcripts/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
---

# Generator-Evaluator Pattern

A design pattern where an AI agent **generates** an output, then runs a **verification loop** against explicit criteria before declaring the result complete. The evaluator can be deterministic (scripts) or probabilistic (LLM-as-judge), but the key principle is: **tell the agent how to check its own work, not just what to produce**.

## Definition

> *"You don't want to just tell it what to do, you also want to tell it how to check it."* — [[entities/randy-olson|Randy Olson]], Show Us Your Agent Skills Ep. 1

The generator-evaluator pattern decomposes a task into two phases:

1. **Generator** — Produces candidate outputs (e.g., chart variants, code, text)
2. **Evaluator** — Tests those outputs against explicit criteria and returns pass/fail with improvement feedback

On failure, the feedback becomes the generator's next set of instructions, creating an iterative refinement loop.

## Two-Gate Verification

The pattern typically uses **two verification gates**:

### Gate 1: Deterministic Verifier (Scripts)

Checks that can be specified exactly and measured programmatically:
- File integrity, DPI, resolution, axis units
- Syntax correctness, test coverage, linting rules
- Data format compliance, output constraints

> *"You can't programmatically assess images."* — Randy Olson (acknowledging the limits of deterministic verification)

### Gate 2: Probabilistic Judge (LLM-as-Judge)

Checks that require judgment and subjective evaluation:
- Is the annotation placement clear?
- Does the chart reveal the data (Tuftean criteria)?
- Is the code structurally sound?
- Does the output actually say what it's supposed to?

> *"Even still, if an eval flips or is wrong 80% of the time, it's still directionally valuable."* — Randy Olson

**Key insight**: LLM-as-judge has known variance, but **generate-and-verify still beats generate-and-hope**.

## Applications

### Data Visualization (Randy Olson)

Randy's daily data-viz skill embodies this pattern:
1. Pull data from authoritative sources
2. Generate 3 chart variants in parallel
3. Score variants against Tuftean criteria (data-to-ink ratio, annotation discipline, clarity)
4. Pick the best variant
5. Run deterministic verifier (DPI, file integrity)
6. Run LLM judge (Tufte compliance)
7. On failure: feedback → regenerate → re-verify
8. Agent decides when the chart is good enough

### Code Review (Wes McKinney / RoboRev)

[[entities/roborev|RoboRev]] implements a variant of this pattern:
1. Coding agent generates code (generator)
2. RoboRev reviews every commit via Codex/GPT 5.5 (evaluator)
3. Findings accumulate in a per-repo ledger
4. `roborev fix` feeds findings back to the generator
5. Code is read 4-5 times minimum before merge

### Agent Skills (General)

[[entities/jeremiah-lowin|Jeremiah Lowin]]'s framing: *"A skill plus an LLM is kind of a program."* The skill defines the deterministic spine; the LLM fills in the parts that require judgment. The skill is the **seam** between determinism and ambiguity.

## Design Principles

1. **Deterministic in scripts, ambiguous to the LLM** — Put anything you can specify exactly into scripts. Put anything that needs judgment into the LLM.
2. **Skills are living documents** — When the evaluator misses something, update the checklist, verifier, or judge prompt so the next run catches it.
3. **Iterative improvement** — Each missed failure is an opportunity to strengthen the evaluation criteria.

## Related Concepts

- [[concepts/agentic-engineering]] — The broader discipline this pattern serves
- [[concepts/evaluation-driven-development]] — Eval-first methodology
- [[concepts/personal-software]] — Skills encode personal taste and judgment
- [[concepts/vibe-coding-vs-agentic-engineering]] — The antithesis: accepting output without verification

## Related Entities

- [[entities/randy-olson]] — Primary practitioner (data-viz domain)
- [[entities/wes-mckinney]] — Primary practitioner (code review domain)
- [[entities/roborev]] — Automated code review implementing this pattern
- [[entities/jeremiah-lowin]] — Skills-as-programs framing

## References

- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)

## Log

- **2026-06-05**: Initial concept page created.
