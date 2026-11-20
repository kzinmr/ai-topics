---
title: "AI Evals People"
type: concept
aliases:
  - ai-evals-people
  - evals-practitioners
  - human-evaluators
created: 2026-04-25
updated: 2026-11-20
tags:
  - concept
  - evaluation
  - llm-evaluation
  - community
  - llm-as-judge
  - human-in-the-loop
sources: []
related:
  - "[[concepts/llm-evaluation]]"
  - "[[concepts/benchmark-ceiling]]"
  - "[[concepts/evaluation/evals-vs-monitoring-debate]]"
---

# AI Evals People

**AI Evals People** is the community stratum of practitioners who design, run, and
critique the evaluation layer for LLMs and AI agents. The wiki already documents the
*tools* (eval harnesses, judges, benchmarks) under [[concepts/llm-evaluation]] and
[[concepts/ai-benchmarks]]; this page is the human layer — the researchers,
consultants, and open-source builders whose methods, blog posts, and disagreements
actually move the field forward. They are the people a frontier lab treats as scarce
judgment-capital when automated metrics run out (see [[concepts/benchmark-ceiling]]).

## Why a "People" Stratum Exists

Automated metrics saturate. Once a benchmark is gamed or a leaderboard is
"benchmaxxed", what remains is *human judgment*: knowing what "good" means in a
domain, spotting failure modes a judge model misses, and designing evals that
correlate with real user satisfaction. This stratum is where that judgment is
institutionalized — through published methodology, open-source eval tooling, and
consulting practices.

The community coheres around a few recurring tensions also tracked elsewhere in the
wiki:

- **LLM-as-judge vs human labels** — how much can a model grade itself? ([[concepts/evaluation/llm-as-judge]])
- **Vibes vs systematic evals** — ad-hoc prompting vs repeatable error analysis ([[concepts/evaluation/eval-loops]])
- **Offline evals vs production monitoring** — the "evals vs monitoring" debate ([[concepts/evaluation/evals-vs-monitoring-debate]])

## The Practitioner Community

People with dedicated entity pages who are central to this stratum:

| Person | Base | Known for |
|--------|------|-----------|
| [[entities/hamel-husain\|Hamel Husain]] | Parlance Training / independent | "Process first, tools second"; the five eval pitfalls; *What We've Learned From A Year of Building with LLMs* (O'Reilly, with Shreya Shankar); harness engineering |
| [[entities/shreya-shankar\|Shreya Shankar]] | UC Berkeley | EvalGen (UIST 2024), DocETL (VLDB 2025); systematic error analysis / open coding; "benevolent dictator" principle for eval design |
| [[entities/drmaciver\|David R. MacIver]] | Antithesis | Property-based testing applied to AI; foundational LLM evaluations; the Hegel universal PBT protocol |
| [[entities/simon-willison\|Simon Willison]] | Independent | `smevals` small eval suite; LLM-as-judge pragmatism; pelican-SVG model sniffing |

Adjacent names that appear in eval discussions but lack their own page yet:
**Percy Liang** (Stanford HELM — holistic evaluation), **David Kahneman / Daniel
Sarov** (the "evals" framing at OpenAI), **Evan Hubinger & the Anthropic evals team**,
**METR** and **Epoch AI** (independent capability & safety evaluation orgs, see
[[concepts/evaluation/epoch-capabilities-index]]).

## Recurring Methods & Positions

These are the ideas the community keeps re-litigating — each maps to a concept page:

- **Error analysis first.** Shreya Shankar's "open coding" — read many failures by
  hand, cluster them, *then* write evals. Opposed to writing a judge before you have
  seen what breaks.
- **Binary judges over Likert scales.** LLM judges grade far more reliably on
  pass/fail than on 1-10; the community converged on decomposing fuzzy rubrics into
  boolean checks. ([[concepts/evaluation/llm-as-judge]])
- **The harness is the eval.** Hamel's "the harness is data science" — most eval
  signal is recoverable from prompt/response logging you already collect
  ([[concepts/harness-engineering]]).
- **Property-based testing for AI.** MacIver imports PBT from Hypothesis: don't pin
  a golden answer, assert invariants that must hold across generated inputs
  ([[entities/drmaciver#Property-Based Testing (PBT) Philosophy]]).
- **Evals vs monitoring.** Whether pre-launch evals or post-launch observability
  catches real failure ([[concepts/evaluation/evals-vs-monitoring-debate]]).

## How to Use This Page

- Looking for an **eval tool/methodology** → start at [[concepts/llm-evaluation]] and
  the [[concepts/evaluation/_index|evaluation sub-wiki]].
- Looking for **who to read / whose opinion matters** on a sub-topic → this page.
- A new eval practitioner becomes central (appears in 2+ sources) → create an entity
  page and add them to the table above.

## Graph Structure Query

```
[ai-evals-people] ──documents──→ [concept: llm-evaluation]
[ai-evals-people] ──includes──→ [entity: hamel-husain]
[ai-evals-people] ──includes──→ [entity: shreya-shankar]
[ai-evals-people] ──includes──→ [entity: drmaciver]
[ai-evals-people] ──includes──→ [entity: simon-willison]
[ai-evals-people] ──relates-to──→ [concept: benchmark-ceiling]
[ai-evals-people] ──embodies──→ [concept: evaluation/evals-vs-monitoring-debate]
[ai-evals-people] ──part-of──→ [concept: harness-engineering]
```

> Informs graph queries: the human stratum that supplies the scarce judgment
> [[concepts/benchmark-ceiling]] describes; methodologically grounded in
> [[concepts/llm-evaluation]] and [[concepts/evaluation/evals-vs-monitoring-debate]].

## Related Pages

- [[concepts/llm-evaluation]] — the tools/methodology this community builds
- [[concepts/evaluation/_index]] — the full evaluation sub-wiki
- [[concepts/benchmark-ceiling]] — the scarce-judgment framing that motivates the stratum
- [[concepts/evaluation/evals-vs-monitoring-debate]] — central community disagreement
- [[concepts/harness-engineering]] — the umbrella under which evals sit
- [[entities/_index]] — all person entities
