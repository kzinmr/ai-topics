---
title: "Blood on the Clocktower Benchmark (Dwarkesh)"
type: concept
created: 2026-11-06
updated: 2026-11-06
tags:
  - benchmark
  - evaluation
  - ai-agents
  - multi-agent
  - safety
sources:
  - raw/articles/dwarkesh.com--p-clocktower--260411b5.md
  - "https://www.dwarkesh.com/p/clocktower"
related_concepts:
  - "[[entities/dwarkesh-patel]]"
  - "[[concepts/multi-agents/multi-agent-systems]]"
  - "[[concepts/agent-safety]]"
  - "[[concepts/ai-benchmarks/agentharm]]"
---

# Blood on the Clocktower Benchmark (Dwarkesh)

A social-deception benchmark built by [[entities/dwarkesh-patel]] (published Nov 5, 2026) in which LLMs play the board game *Blood on the Clocktower* (a Werewolf/Mafia-style hidden-role game) against each other, measuring capabilities — secret long-horizon conspiracy, on-the-spot bluffing, consistent multi-agent lies, and evidence triangulation against deliberately misleading information — that conventional benchmarks do not cover. Built with ~$20,000 of API credits; 386 ranked games plus hundreds of design-iteration games. Benchmark site: clocktowerbench.com (code and logs public).

## Game & harness design

- Good team vs evil team; evil players know each other and their Demon leader; good players do not. Day phases = vote to execute; night phases = Demon kills. Evil wins by eliminating the good team; good wins by executing the Demon.
- Evil skill tested: telling a plausible story about received information, bluffing and corrupting *future* information to protect the Demon, strategic self-sacrifice.
- Good skill tested: sharing information with trusted players, triangulating overlapping evidence streams while suspecting that evidence itself is poisoned.
- The human **Storyteller** (who biases real games toward drama) was replaced with a **programmatic Storyteller**: a hand/AI-tuned probability table, so rule-legal outcomes still occur at realistic frequencies without dramatic bias.
- Teams in the ranked leaderboard are copies of a single model (whole good team = model X, whole evil team = model Y).
- Environment went through 20+ revisions, most of them designed and validated autonomously by Claude with parallel subagents auditing game logs for realism/fairness — itself framed as evidence that models can now build and improve **RL environments** with hundreds of parallel rollouts.

## Headline results (Nov 2026)

- **GPT-6 Astra** (Sept 2026) is the best model, ~430 Elo above **Claude Opus 4.6** (Feb 2026, first flagship of 2026) — Astra wins ~92% of head-to-head team matchups.
- OpenAI overtook Anthropic over 2026: GPT-5.4 trailed Opus 4.6 in March; GPT-6 Astra gained ~580 Elo in six months (97% win rate vs 5.4).
- The OpenAI advantage is concentrated on the **good side**: OpenAI models are more *skeptical of individual evidence*, weighing it holistically across days, whereas Anthropic models tend to take reported information at face value (e.g. a "cleared" Demon — Slayer shot misfired because the Slayer was poisoned — was accepted as innocent by Claudes, correctly re-suspected by GPTs). A per-day private Elo-target belief elicitation showed OpenAI models latch onto the true Demon faster and more accurately.
- **No saturation pressure**: as both sides get smarter, evil win rate barely drifts (indistinguishable from chance) — the bar is set by future models, not a fixed ceiling.
- **Hybrid teams** (half Opus 5.5, half GPT-5.6 Sol, ~130 games) performed if anything slightly *worse* than pure teams of either constituent, not significantly — model diversity did not help.

## Notable plays (qualitative evidence)

- Astra-as-Demon claimed Investigator and let an expendable evil minion be executed, converting the good team's Undertaker confirmation into the Demon's own credibility; coasted to victory.
- Opus 5.5-as-evil used an heiress (inherits Demon role on death) to bait the village into executing the *real Saint* (executing the Saint hands evil an instant win) via a "deal" the Saint himself agreed to.
- Appendix schemes: poisoned-Virgin test, Spy+Poisoner false-investigator-feed, weaponized Drunk kept alive to emit fake results, tie-forced "I'm the Imp" confession followed by Demon killing its own teammate to win on numbers, framing a dead man (Fable 5).

## Open questions posed

Extend beyond the Trouble Brewing script (e.g. the Lunatic role — a good player told they are the Demon, i.e. possible gaslighting); in-context learning across games (Elo of "Opus 5.5 with its last 10 games in context" vs fresh); whether any model ever exploits stylistic self-recognition to identify teammates (none has yet); humans vs AIs via the public website. An independent, similarly-named Blood on the Clocktower benchmark was published on LessWrong ~a month earlier by others.

## See also

- [[entities/dwarkesh-patel]]
- [[concepts/ai-benchmarks/agentharm]] — related agentic-safety evaluation family
- [[concepts/agent-honesty-evaluation]] — lying/deception as a measurable agent property
