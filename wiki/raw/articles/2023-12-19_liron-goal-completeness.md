---
title: "Goal-Completeness is like Turing-Completeness for AGI"
author: Liron
date: 2023-12-19
source: https://www.lesswrong.com/posts/iFdnb8FGRF4fquWnc
platform: LessWrong
tags:
  - turing-completeness
  - agi
  - ai-safety
  - goal-completeness
  - gwern
  - analogy
scraped: 2026-05-08
---

# Goal-Completeness is like Turing-Completeness for AGI

By Liron — 2023-12-19 — 51 points — 26 comments

Turing-completeness is a useful analogy we can use to grasp why AGI will inevitably converge to "goal-completeness".

By way of definition: An AI whose input is an arbitrary goal, which outputs actions to effectively steer the future toward that goal, is **goal-complete**.

A goal-complete AI is analogous to a Universal Turing Machine: its ability to optimize toward any other AI's goal is analogous to a UTM's ability to run any other TM's same computation.

## Expecting Turing-Completeness

From Gwern's classic page, [Surprisingly Turing-Complete](https://gwern.net/turing-complete):

> [Turing Completeness] is also weirdly common: one might think that such universality as a system being smart enough to be able to run any program might be difficult or hard to achieve, but it turns out to be the opposite—it is difficult to write a useful system which does not immediately tip over into TC.

> Computation is not something esoteric which can exist only in programming languages or computers carefully set up, but is something so universal to any reasonably complex system that TC will almost inevitably pop up unless actively prevented.

If you look at any electronic device today, like your microwave oven, you won't see a microwave-oven-specific circuit design. What you'll see in virtually every device is the same two-level architecture:

1. A Turing-complete chip that can run any program
2. An installed program specifying application-specific functionality, like a countdown timer

It's a striking observation that your Philips Sonicare™ toothbrush and the guidance computer on the Apollo moonlander are now architecturally similar. But with a good understanding of Turing-completeness, you could've predicted it half a century ago.

## Expecting Goal-Completeness

If you don't want to get blindsided by what's coming in AI, you need to apply the thinking skills of someone who can look at a Breakout circuit board in 1976 and understand why it's not representative of what's coming.

When people laugh off AI x-risk because "LLMs are just a feed-forward architecture!" or "LLMs can only answer questions that are similar to something in their data!" — I hear them as saying "Breakout just computes simple linear motion!" or "You can't play Doom inside Breakout!"

OK, BECAUSE AI HASN'T CONVERGED TO GOAL-COMPLETENESS YET. We're not living in the convergent endgame yet.

When I look at GPT-4, I see the furthest step that's ever been taken to push out the frontier of outcome-optimization power in an unprecedentedly large and general outcome-representation space (the space of natural-language prompts).

And I can predict that algorithms which keep performing better on these axes will, one way or the other, converge to the dangerous endgame of **goal-complete AI**.

By the 1980s, by the time you saw Pac-Man in arcades, it was knowable to insightful observers that the Turing-complete convergence was happening. It wasn't a 100% clear piece of evidence: After all, Pac-Man's game semantics aren't Turing Complete AFAIK. But it was part of a general trend you could look at and think, "OK, this is where we're headed."

## Recapping the Analogy

| Concept | Turing-Completeness | Goal-Completeness |
|---------|---------------------|-------------------|
| **Definition** | Can compute any computable function | Can optimize toward any specifiable goal |
| **Convergence driver** | General-purpose chips cheaper than ASICs at scale | General-purpose optimizers more capable than narrow systems |
| **Historical example** | Breakout (1976) → Pac-Man (1980) → Modern games all Turing-complete | GPT-3 (2020) → GPT-4 (2023) → ??? |
| **Why it's inevitable** | Complexity threshold → TC emerges | Capability threshold → goal-directedness emerges |
| **"Unseeing" required** | Seeing CSS as a computational substrate, not just styling | Seeing LLMs as outcome-optimizers, not just text-predictors |

The key insight: Just as the entire electronics industry converged on Turing-complete architectures (rather than application-specific circuits), AI will converge on goal-complete architectures (rather than narrow, task-specific systems). The economic and capability advantages are simply too great.
