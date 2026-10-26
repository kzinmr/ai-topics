---
title: "Jagged Frontier"
type: concept
aliases:
  - jagged-technological-frontier
  - jaggedness
created: 2026-04-25
updated: 2026-10-26
tags:
  - concept
  - ai-adoption
  - evaluation
  - ai-industry
  - domain-expertise
related:
  - "[[entities/ethan-mollick]]"
  - "[[concepts/centaurs-and-cyborgs]]"
  - "[[concepts/ai-benchmarks/ai-resistant-evaluations]]"
  - "[[concepts/vibe-physics]]"
sources:
  - https://ssrn.com/abstract=4573321
  - "[[entities/ethan-mollick]]"
---

# Jagged Frontier

The **jagged technological frontier** is Ethan Mollick's concept that AI capability is *not* smoothly distributed across tasks: an irregular boundary separates tasks AI handles well from tasks of seemingly equal or even lesser difficulty that it fails at. The metaphor — a coastline, not a straight line — explains why expert intuition about "what AI can do" is systematically wrong and why adoption guidance must be task-specific.

## Origin: the BCG experiment (2023)

The concept comes from a field experiment Mollick ran with Boston Consulting Group and two academic coauthors (Cui, Cross, Dell'Acqua, Kallberg, Lee, Malone, Perkins), published as *"The (Unevenly-Pursued) Promise of Generative AI"* / "Navigating the Jagged Technological Frontier" (HBS Working Paper 24-013):

- **758 BCG consultants**, 18 realistic consulting tasks.
- Inside the frontier: **+12.2% productivity**, **+25.1% speed**.
- Outside the frontier: consultants using AI were **~19 percentage points *less* likely to produce correct solutions** — while *believing* they were doing better ("overconfidence in AI's capabilities").
- The frontier was jagged: tasks differing subtly in difficulty straddled it in counterintuitive ways.

## Key Ideas

- **Task-level, not model-level, capability.** Any single benchmark number hides the jaggedness; performance must be assessed per task family.
- **The competence trap.** Because failures cluster outside the frontier in non-obvious places, unaided human judgment of AI limits fails; empirical, per-task testing (or trusted guidance) is required.
- **Two usage strategies follow from jaggedness** — see [[concepts/centaurs-and-cyborgs]]: delegate across the boundary (centaur) or blend across it (cyborg).
- **2025 extension:** Mollick's "The Shape of AI" essay expanded jaggedness into a fuller shape metaphor with **bottlenecks and salients** — capability protrusions and constraints that shift as models improve.

## In This Wiki

The concept is used as a lens in several pages:
- [[concepts/vibe-physics]] — the jagged frontier at the science extreme (GPT-5-era capability protrusions invisible to general users)
- [[concepts/oracle-model-routing]] — routing as a response to uneven capability
- [[concepts/ai-benchmarks/ai-resistant-evaluations]] — measuring the frontier's position over time
- [[entities/ethan-mollick]] — originator; timeline entries for the 2023 BCG study and 2025 "Shape of AI"

## Graph Structure Query

```
[jagged-frontier] ──author──→ [entity: ethan-mollick]
[jagged-frontier] ──motivates──→ [concept: centaurs-and-cyborgs]
[jagged-frontier] ──motivates──→ [concept: oracle-model-routing]
[jagged-frontier] ──measured-by──→ [concept: ai-resistant-evaluations]
```

## Sources

- Dell'Acqua et al. (2023), *Navigating the Jagged Technological Frontier*, HBS Working Paper 24-013 — [SSRN 4573321](https://ssrn.com/abstract=4573321)
- Ethan Mollick, *The Shape of AI: Jaggedness, Bottlenecks and Salients* (2025), One Useful Thing
- [[entities/ethan-mollick]] — full biography and timeline
