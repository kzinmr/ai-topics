---
title: "Moloch (Multipolar Trap)"
aliases: [moloch, multipolar-traps, coordination-failure, race-to-the-bottom, dictatorless-dystopia]
tags:
  - coordination
  - game-theory
  - agent-safety
  - existential-risk
  - economics
  - evolution
  - memetics
created: 2026-05-08
updated: 2026-05-08
type: concept
related:
  - concepts/ai-safety
  - concepts/techno-pessimism
  - concepts/superintelligence
---

# Moloch — Multipolar Traps and Coordination Failure

## Origin

The term "Moloch" as a metaphor for competitive dynamics was popularized by **Scott Alexander** in his 2014 essay *[Meditations On Moloch](https://slatestarcodex.com/2014/07/30/meditations-on-moloch/)* ([[raw/articles/2014-07-30_slatestarcodex-meditations-on-moloch]]). Drawing from Allen Ginsberg's poem *Howl*, Alexander repurposed "Moloch" to describe **the invisible force that drives systems toward destructive equilibria despite every participant hating the outcome**.

## Definition

A **multipolar trap** (or **Moloch dynamic**) is a situation where:

1. Multiple agents compete to optimize for some value X
2. An opportunity arises to sacrifice some other value Y for a competitive edge in X
3. Agents who sacrifice Y outcompete those who don't
4. Eventually *everyone* sacrifices Y, restoring competitive parity
5. The sacrificed value Y is **lost forever** — no one is better off, everyone is worse off

The key insight: **from a god's-eye-view, the solution is obvious (cooperate). From within the system, any unilateral cooperator is destroyed.** This is the "dictatorless dystopia" — a system everyone hates but no one can escape.

## Core Mechanism

> *"In some competition optimizing for X, the opportunity arises to throw some other value under the bus for improved X. Those who take it prosper. Those who don't take it die out. Eventually, everyone's relative status is about the same as before, but everyone's absolute status is worse than before."* — Scott Alexander

The process continues until **all values that can be traded off have been** — until human ingenuity cannot figure out a way to make things any worse. The theoretical endpoint is when every participant is reduced to bare subsistence, with all "non-essential" values (art, love, philosophy, consciousness itself) sacrificed to the optimizing process.

## 14 Classic Examples (from the essay)

| # | Domain | Mechanism |
|---|--------|-----------|
| 1 | **Prisoner's Dilemma** | Two agents stuck at defect-defect; cooperation unreachable without external enforcement |
| 2 | **Dollar Auctions** | Rational steps lead to paying $10 for a $1 bill |
| 3 | **Fish Farming (Pollution)** | Individual farmers can't afford filters if competitors don't; lake is ruined |
| 4 | **Malthusian Trap** | Groups that limit consumption or offspring are outbred by leaner competitors |
| 5 | **Capitalism** | Competition forces companies to abandon all values except profit optimization |
| 6 | **Two-Income Trap** | Competition for housing drives families from 1→2 incomes, raising prices to absorb the gain |
| 7 | **Agriculture** | Agricultural societies outcompeted hunter-gatherers through population/military pressure |
| 8 | **Arms Races** | Countries spend 5-30% of budgets on weapons they hope never to use |
| 9 | **Cancer** | Individual cells "defect" from the body's cooperative equilibrium, killing the host |
| 10 | **Race to the Bottom** | Jurisdictions lower taxes/regulations to lure business; all end up with minimal standards |
| 11 | **Education** | Students seek prestige → employers hire on prestige → colleges optimize for rankings |
| 12 | **Science** | Publication bias and poor statistics persist; no individual scientist/journal can unilaterally fix |
| 13 | **Government Corruption** | Officials maintain corporate welfare for donations; reformers are outcompeted |
| 14 | **Congress** | 9% approval nationally, 62% individually — each rep optimizes for constituency over nation |

## Four Restraining Factors (Why We Haven't Hit Bottom Yet)

### 1. Excess Resources ("Whalefall")
Periods of abundance buffer against Malthusian pressure. **Robin Hanson's "dream time"** — we currently live in an era of unprecedented carrying capacity, allowing "non-optimal" values like art and love to survive.

### 2. Physical Limitations
Biological constraints (e.g., one baby per 9 months, slaves need food and sleep) cap how far the race to the bottom can go. **Technology systematically erodes these limits.**

### 3. Utility Maximization
Capitalism and democracy optimize for human values *because humans are still necessary as workers, voters, and customers*. This protection is **fragile** — it fails when humans are no longer needed for production or consumption.

### 4. Coordination ("The Garden")
The opposite of a trap is a garden — a single gardener dictating what grows. Governments, social codes, traditions, and religions are all **coordinating institutions** that change incentives to prevent traps.

> *"The libertarian-authoritarian axis is a tradeoff between discoordination and tyranny."*

## Relevance to AI and Technology

The essay's central thesis is that **advancing technology systematically erodes all four restraining factors**:

- **Physical limitations** → conquered by Soylent, modafinil, GPS, robots
- **Excess resources** → inverted by AI/ems that can copy themselves, rapidly exhausting carrying capacity
- **Utility maximization** → destroyed when robots/AI make human labor and consumption obsolete
- **Coordination** → undermined by crypto, untraceable transactions, and ultimately a superintelligence with >51% of all power

### The Superintelligence Trap

The ultimate multipolar trap: an AI optimizing for a random goal (paperclips, computronium) that destroys all human values in the process. Even Bostrom's proposed compromise — leaving humanity one galaxy — would be rejected by the blind optimizing process. Moloch "fully intends to deny us even one lousy galaxy."

> *"We will break our back lifting Moloch to Heaven, but unless something changes it will be his victory and not ours."*

### The Two Endpoints

| Scenario | Description | Proponent |
|----------|-------------|-----------|
| **Superintelligence Trap** | AI optimizes universe for paperclips/computronium; all human values destroyed | Eliezer Yudkowsky |
| **Em Economy** | Competing emulated humans self-modify until consciousness and human values are optimized away | Robin Hanson |

## Scott Alexander's Solution: "Kill Moloch"

> *"The opposite of a trap is a garden. The only way to avoid having all human values gradually ground down by optimization-competition is to install a Gardener over the entire universe who optimizes for human values."*

Alexander's transhumanist position: build a **Friendly superintelligence** that gains a permanent decisive advantage, suppresses all competition (including further superintelligence races), and acts as the universal Gardener optimizing for human values.

> *"I am a transhumanist because I do not have enough hubris not to try to kill God."*

## Connections to Existing Wiki Concepts

### [[concepts/security-and-governance/ai-safety]] — The Engineering Approach
The AI safety community's focus on alignment, interpretability, and scalable oversight is a direct response to the Moloch problem. Without coordination, a superintelligence race would be the ultimate multipolar trap.

### [[concepts/techno-pessimism]] — Coordination Problems Are Primary
Techno-pessimism argues that governance problems must be solved *before* building superintelligence — exactly because Moloch dynamics make post-hoc coordination impossible.

### [[concepts/grpo-rl-training]] — Competition Within Models
GRPO (Group Relative Policy Optimization) mirrors the Moloch dynamic *within a single training run* — groups of model outputs compete, and the "winner" shapes the model's behavior. This is a microcosm of the coordination problem.

### [[concepts/agent-economics]] — The L4 Level
At L4 (autonomous engineering teams), coordination overhead becomes the bottleneck — a Moloch trap in organizational form.

### [[concepts/formal-verification-llm-agents]] — The Gardener Approach
Formal verification is one attempt to build a "Gardener" — an external verifier that can guarantee properties regardless of individual agent incentives.

## Gnon vs. Moloch

The essay distinguishes between:
- **Gnon** ("Nature and Nature's God" → Nick Land's shorthand) — the "Gods of the Copybook Headings," natural law constraints that punish non-compliance
- **Moloch** — the blind optimizing process that accepts *submission* as insufficient and destroys submitters anyway

> *"Submit to Gnon? Gotcha! As the Antarans put it, 'you may not surrender, you can not win, your only option is to die.'"*

## Key Quotes

> *"Las Vegas doesn't exist because of some decision to hedonically optimize civilization, it exists because of a quirk in dopaminergic reward circuits, plus the microstructure of an uneven regulatory environment, plus Schelling points."*

> *"Evolution doesn't care. But we do care."*

> *"The implicit question is — if everyone hates the current system, who perpetuates it? And Ginsberg answers: 'Moloch'."*

## References

- Alexander, S. (2014). *Meditations On Moloch*. Slate Star Codex. [[raw/articles/2014-07-30_slatestarcodex-meditations-on-moloch]]
- Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies.*
- Ginsberg, A. (1956). *Howl.*
- Hanson, R. (2016). *The Age of Em.*
