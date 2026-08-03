---
title: "The Shared Discovery Paradox"
source_url: "https://x.com/i/article/2079412885021970432"
date: 2026-07-21
author: "Yohei Nakajima (@yoheinakajima)"
getxapi: false
source_fallback: false
status: ingested
tags: [game-theory, coordination, collective-intelligence, multi-agent, information-sharing, x-article]
related_urls:
  - "https://arxiv.org/abs/2607.18045"
  - "https://github.com/yoheinakajima/shared-discovery-paradox"
  - "https://yoheinakajima.github.io/shared-discovery-paradox/"
---

# The Shared Discovery Paradox

A simple math game explaining how information sharing without action coordination can lead to better-informed individual decision-making, but a worse expected outcome for the group.

Pooling independent judgements can improve collective estimation. But in collective discovery, shared information without coordination can result in a worse outcome for the group. This underlying mechanism has been studied in organizational learning, information cascades, optimal search, and the division of cognitive labor.

## The Game

Imagine a game with 16 boxes and eight players. There is exactly one jackpot in one of the boxes, and each player gets to choose one box. The goal is to guess which box has the jackpot.

### No Information Scenario

If a player chooses a box at random, their chance of guessing the jackpot is 6.25%. Eight independent random guesses collectively have a 40.3% chance of finding the jackpot. If the players coordinate, they can increase their collective chance to 50% by picking different boxes.

### With Imperfect Clues (No Sharing)

Each player is given an imperfect clue that points to the correct box 20% of the time. When a clue is wrong, it points to one of the other 15 boxes at random, and the clues are independent. If there is no sharing of information, each player has a 20% chance of choosing the jackpot, and collectively they have an 83.2% chance that somebody finds it.

### With Information Sharing (No Action Coordination)

Now, if they all share their clues with each other, the probability that the group's most likely box containing the jackpot goes up to 38.4%. However, if each player simply picks the box with the highest chance of being correct, without coordinating their actions, they will all choose the same box. The collective probability that somebody finds the jackpot is therefore also 38.4%.

In this specific scenario, sharing information almost doubles the accuracy of each player's selection, but cuts the likelihood that somebody finds the jackpot by more than half. It shows that in collective discovery, information sharing without action coordination can decrease the expected outcome for the group.

### With Jackpot Splitting

You might say that in most games, the jackpot would have to be split among the people who chose it. In that case, complete convergence is no longer stable because players have an incentive to avoid crowded boxes. But under a symmetric mixed-strategy equilibrium, we still end up with some overlap in choices, and the collective likelihood that somebody chooses the jackpot is around 60%, well below the scenario where no information is shared.

### With Coordination

If they instead coordinate to maximize the likelihood that somebody gets the jackpot, and choose the eight most likely boxes, the collective likelihood goes up to 85.9%. The average probability attached to any one assigned box is only 10.74%, which illustrates the difference between maximizing the accuracy of an individual action and maximizing the chance that at least one action succeeds. One way to align incentives here would be to agree upfront that the jackpot is pooled and split equally among all eight players.

## Results Summary

| Scenario | Individual Accuracy | Collective Success Probability |
|----------|-------------------|-------------------------------|
| Random (no info, no coord) | 6.25% | 40.3% |
| Coordinated (no info) | 6.25% | 50.0% |
| Imperfect clues (no sharing) | 20.0% | 83.2% |
| Info sharing (no coord) | 38.4% | 38.4% |
| Info sharing + jackpot split equilibrium | — | ~60% |
| Info sharing + coordination | 10.74% (avg) | 85.9% |

## Academic Foundations

Builds on classic results in:
- Information cascades (Banerjee; Bikhchandani, Hirshleifer & Welch)
- Observational learning (Smith & Sørensen)
- Organizational learning (March)
- Optimal search (Koopman)
- Division of cognitive labor (Kitcher; Zollman)
- Price of anarchy / congestion (Roughgarden)
- Informational Braess' paradox (Acemoglu et al.)

## Implications

This distinction matters for:
- Corporations managing innovation across competing departments
- Multi-agent systems with shared memory
- The allocation of funding in venture capital or scientific discovery

## Resources

- arXiv: https://arxiv.org/abs/2607.18045
- GitHub: https://github.com/yoheinakajima/shared-discovery-paradox
- Site: https://yoheinakajima.github.io/shared-discovery-paradox/
