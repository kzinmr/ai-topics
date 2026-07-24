---
title: Claude Fable Jacobian Conjecture Breakthrough
created: 2026-07-24
updated: 2026-07-24
type: concept
tags: [model, claude-fable-5, claude, anthropic, mathematics, ai-in-science, reasoning, frontier-models, research]
sources:
  - raw/articles/2026-07-20_claude-fable-jacobian-conjecture.md
---

# Claude Fable Jacobian Conjecture Breakthrough

On July 20, 2026, [[entities/anthropic]]'s [[concepts/claude/fable-5]] model produced a counterexample to the **Jacobian Conjecture**, an 87-year-old unsolved problem in algebraic geometry. The discovery was announced via X (Twitter) by Anthropic mathematician **Levent Alpoge** during the 2026 World Cup Final, amassing over 39 million views and triggering widespread reactions across the mathematics and AI communities.

## The Counterexample

The polynomial map F: C^3 -> C^3 with constant Jacobian determinant -2, found by Fable 5:

```
F(x,y,z) = (
    (1+xy)^3 z + y^2(1+xy)(4+3xy),
    y + 3x(1+xy)^2 z + 3xy^2(4+3xy),
    2x - 3x^2 y - x^3 z
)
```

Three distinct points map to the **same output** (-1/4, 0, 0):
- (0, 0, -1/4)
- (1, -3/2, 13/2)
- (-1, 3/2, 13/2)

The map has constant non-zero Jacobian (local invertibility everywhere), yet fails global injectivity -- directly falsifying the Jacobian Conjecture.

## What Is the Jacobian Conjecture?

First posed by Ott-Heinrich Keller in 1939, the conjecture states:

> If a polynomial map F: C^n -> C^n has a Jacobian determinant that is a non-zero constant, then F is globally invertible with a polynomial inverse.

Trivially true for n=1. Remained open for n=2. Now known false for n>=3. The conjecture was notorious as a "canonical crank graveyard" -- many attempted proofs over decades contained subtle errors.

## Discovery Chain

The discovery followed a cascade of events during the **Formalizing Fermat workshop** at Imperial College London (July 6-10, 2026), organized by Kevin Buzzard:

1. **Akhil Mathew** (University of Chicago) discussed AI counterexample search with Buzzard during lunch on July 7
2. Mathew suggested the Jacobian Conjecture to his colleague **Levent Alpoge** at Anthropic
3. On July 20, during the World Cup Final, Alpoge prompted [[concepts/claude/fable-5]] to search for a counterexample
4. Fable 5 produced the counterexample, which Alpoge verified and tweeted within hours

The exact prompt and reasoning trace have not been publicly shared. [[entities/terry-tao]] subsequently demonstrated that expert prompting dramatically improves mathematical exploration with AI.

## Verification

### Human Verification
- Alpoge provided Wolfram Alpha links verifying the Jacobian determinant and collision points
- [[entities/terry-tao]] published a detailed blog post digesting the counterexample in geometric terms
- Multiple independent mathematicians confirmed the result

### Formal Verification in Lean
Within hours, **Paul Lezeau** formalized the counterexample in the Lean proof assistant and submitted a pull request to [[entities/deepmind]]'s Formal Conjectures repository, where the Jacobian Conjecture was already formalized. This provided machine-checkable certainty -- a significant milestone in [[concepts/formal-methods]] applied to AI-generated mathematics.

### Cascading Consequences
Several equivalent conjectures also fall:
- **Dixmier Conjecture** (third Weyl algebra) -- disproven
- **Poisson Conjecture** -- disproven

The conjecture remains **open for n=2**. Whether counterexamples exist over real numbers (R instead of C) is also an open question.

## Community Reactions

- **Kevin Buzzard** (Imperial College): "It is a big day. I think it's a great time to be alive, personally."
- **Akhil Mathew**: described the moment as "a very rapid and very unsettling change... especially for junior mathematicians."
- **HN Mathematician** (tacomonstrous): "Speaking as a mathematician, it does seem like we're a bit fucked as a community."
- **Yitang Zhang** (famous for bounded prime gaps) spent 7 years working on proving the conjecture -- his advisor said he "failed miserably."
- **Garry Tan** (Y Combinator): hailed a "return of the age of the gentleman scientist."

Notably, Alpoge shared the result openly on X rather than seeking formal publication credit -- a move widely praised.

## Significance for AI in Mathematics

This breakthrough is part of a rapid series of AI-driven mathematical achievements since mid-2025:

| Date | Achievement | Model |
|------|-------------|-------|
| Mid-2025 | Solved 5/6 IMO problems | Various |
| May 2026 | Disproved Erdos Unit Distance Conjecture | ChatGPT |
| July 2026 | Counterexample to Jacobian Conjecture | Claude Fable 5 |

The discovery exemplifies how [[concepts/reasoning-models]] can tackle problems previously requiring deep mathematical intuition. However, **human expertise remained essential** -- the problem was selected by domain experts, and the prompt was crafted by a mathematician (Alpoge is a Harvard valedictorian). The **Leiden Declaration on AI and Mathematics** (June 2026) had already urged guardrails around transparency and attribution in AI-assisted mathematics.

## Open Questions

1. **What was the prompt?** Fable 5's full reasoning trace remains undisclosed
2. **Is n=2 still true?** The two-dimensional case remains open
3. **Real numbers?** Does the Jacobian Conjecture hold over R?
4. **How many counterexamples exist?** Early investigation suggests they may not be rare
5. **Understanding the "why"**: Mathematicians are working to develop geometric intuition for the counterexample's structure

## Related Pages

- [[entities/anthropic]] -- Anthropic, the AI lab behind Claude Fable
- [[concepts/claude/fable-5]] -- The Claude Fable 5 model
- [[entities/terry-tao]] -- Fields Medalist who digested the counterexample
- [[entities/deepmind]] -- Host of the Formal Conjectures repository
- [[concepts/formal-methods]] -- Formal verification, including Lean proof assistant
- [[concepts/reasoning-models]] -- AI reasoning capabilities that enabled the breakthrough
