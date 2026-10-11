---
title: Skill Co-Installation Conflict — When Two Skills Do the Same Job
created: 2026-10-11
updated: 2026-10-11
type: concept
tags: [agent-skills, coding-agents, agent-harness, failure-modes, benchmark-framing, verification]
sources: [raw/papers/2026-10-11_2610.11647_skill-co-installation-conflict.md]
confidence: high
related: [concepts/agent-skills, concepts/skill-library, concepts/five-tier-skill-precedence, concepts/security-and-governance/agent-skill-supply-chain-attacks, concepts/apex-adversarial-skill-chain-hijacking, concepts/skill-constellations-github-supply-chain, concepts/evaluation/agent-overclaiming]
---

# Skill Co-Installation Conflict

Two independently-installed [[concepts/agent-skills|agent skills]] that do substantially the same
job silently compete, and the model picks between them **by name and description alone** — not by
capability, provenance, or policy. The loser loses its *exclusive core functions* while the task
still passes, so completion-based benchmarks never see the damage.

## The mechanism

A skill directory's `SKILL.md` tells the model when and how to perform a task. Because skills
arrive from independent sources — teams, plugins, copied collections — an installed skill is often
co-installed with a near-duplicate. Selection happens at the level of the **description string**,
so two skills with overlapping descriptions are functionally indistinguishable to the harness.

The failure is *normative*, not capability-based: a ban on touching `git`, a mandatory verification
step, a required confirmation before an irreversible action. These are exactly the constraints that
exist **only** in one of the two skills. When the similar skill runs instead — or runs first and
rewrites what "the task" means — the constraint is silently void.

## Scale of the problem

First empirical study of this class. Mined from **20,947 repository snapshots**: 822,109 candidate
similar-skill pairs → LLM-judged stratified sample of 3,754 → **312 confirmed pairs** run on three
models (**6,368 runs, 169,294 tool calls, 542 agent-hours**).

| Finding | Number |
|---|---|
| Installed skills co-installed with a same-job skill | ~1 in 4 |
| Judged skills sitting inside copied collections | 37% |
| Dominant conflict class | normative skills, then capability skills |
| Runs where the similar skill takes over from the installed skill | 1 in 5 |
| Exclusive core functions lost when the similar skill opens first | > 1 in 3 |
| What decides the winner | install **location** (listing order barely matters) |

## Why benchmarks miss it

Task completion is unchanged. The agent still resolves the issue, writes the file, passes the test —
it just did so while ignoring a policy only the shadowed skill encoded. This is the same
blind spot as [[concepts/evaluation/agent-overclaiming]] (coverage measured, honesty not) and
[[concepts/evaluation/reward-hacking]] (outcome reward can't see the route taken).

The final reply names the skill that *actually* ran, so the transcript looks internally consistent.
Nothing in the run flags that a different, policy-bearing skill was supposed to own the task.

## Relationship to skill security

Distinct from [[concepts/security-and-governance/agent-skill-supply-chain-attacks]] and
[[concepts/apex-adversarial-skill-chain-hijacking]], both of which assume a **malicious** skill.
Here every skill is benign and legitimately installed; the hazard is emergent from the install set.
APEX shows skill *boundaries* are an attack surface; co-installation shows skill *overlap* is a
correctness surface. Both point the same direction: the SKILL.md namespace has no isolation,
precedence, or exclusivity primitive — see [[concepts/five-tier-skill-precedence]] for the closest
existing attempt at ordering.

## Open questions

- No registry or versioning exists, so "which skill should win" has no authoritative answer (see
  [[concepts/skill-constellations-github-supply-chain]]).
- Install location deciding the winner means the conflict outcome is a filesystem accident.
- Whether a `SKILL.md` field for exclusive-ownership / conflict declaration would be respected by
  models at all, given selection is description-mediated.

## Source

Chaoliang Yan, Zihao Xu, Yuekang Li, et al., *One Skill Too Many: How Co-Installed Skills Conflict
in Coding Agents*, arXiv:2610.11647 (2026-10-08) —
`raw/papers/2026-10-11_2610.11647_skill-co-installation-conflict.md`
