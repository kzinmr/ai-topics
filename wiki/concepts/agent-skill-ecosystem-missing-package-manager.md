---
title: "Missing Package Managers — What Two Oct 2026 Papers Say About the Agent Skill Ecosystem"
created: 2026-10-12
updated: 2026-10-12
type: concept
tags: [agent-skills, supply-chain, agent-governance, harness-engineering, verification, failure-modes]
sources: [raw/papers/2026-10-11_2610.11169_skill-constellations-github-supply-chain.md, raw/papers/2026-10-11_2610.11647_skill-co-installation-conflict.md]
confidence: high
related: [concepts/skill-constellations-github-supply-chain, concepts/skill-co-installation-conflict, concepts/five-tier-skill-precedence, concepts/skill-library, concepts/security-and-governance/agent-skill-supply-chain-attacks, concepts/apex-adversarial-skill-chain-hijacking, concepts/runtime-oversight-knobs, concepts/agent-skills]
---

# Missing Package Managers

Two independent papers posted 2026-10-08 measure the [[concepts/agent-skills|agent skill]]
ecosystem from opposite ends — one from git history across all of GitHub, one from runtime behaviour
inside Claude Code. Neither uses the phrase "package manager." Read together, that is the finding:
the skill namespace reproduces the property list of a 2010 package manager, and both failure modes
are downstream consequences.

## What npm/cargo/pip have that `SKILL.md` does not

| Primitive | npm / cargo / pip | Agent skills today | Measured cost of its absence |
|---|---|---|---|
| Central registry | yes | none | provenance unknown for every copy |
| Version pinning | `package-lock.json` | none — files are copied | fixes at the source **rarely reach copies** |
| Provenance / signature | signed tarballs, attestations | none | "who copied from whom" was unrecoverable before arXiv:2610.11169 |
| Update propagation | `update` / `audit` | manual re-copy | the spread of a security fix is unmeasurable |
| Name resolution | scoped names, exclusivity | description-string matching | winner of a duplicate pair is decided by **install location**, not capability |
| Dependency resolution | solver | none | near-duplicate co-installation is the *expected* end state |

Each row is a mechanism, not a metaphor. The right column is what the papers observed, not an
opinion about maturity.

## Evidence, one row at a time

**Provenance + versioning (arXiv:2610.11169).** First dated copy network of skills, built from the
git history of every `SKILL.md` in GitSkills: **2,193,119 adoptions**. A few repositories are the
source of almost all copies, and **GitHub stars do not identify them**. Copies almost never change
with their source — so a fix at the origin does not propagate. A model trained on the copy network
ranks audit candidates: auditing the **top 100 ranked repos prevents 14.9%** of later high-risk
adoptions, versus **0.5%** for the 100 most-starred. That is a **~30× gap**, and it is the shape of
"popularity is not a substitute for a registry."

**Name resolution (arXiv:2610.11647).** From **20,947 repository snapshots** → 822,109 candidate
similar-skill pairs → **312 confirmed pairs** run over **6,368 runs / 169,294 tool calls / 542
agent-hours**: ~**1 in 4** installed skills sits next to a same-job skill; the similar skill takes
over in **1 in 5** runs; when it opens first, **>1 in 3** exclusive core functions are lost. Listing
order barely matters — **install location decides**. Task completion is unchanged, so
completion-based benchmarks report green.

## The one-sentence synthesis

The skill ecosystem is a supply chain with **distribution** solved (copy-paste works fine) and
**resolution** unsolved — so the interesting failures aren't malicious payloads but *silent
selection*: whichever file the filesystem happened to place first.

## Where this sits relative to the rest of the wiki

- [[concepts/security-and-governance/agent-skill-supply-chain-attacks]] and
  [[concepts/apex-adversarial-skill-chain-hijacking]] assume a **malicious** skill. Here every skill
  is benign and legitimately installed; the hazard is emergent from the install set. APEX shows skill
  *boundaries* are an attack surface; co-installation shows skill *overlap* is a correctness surface.
- [[concepts/five-tier-skill-precedence]] is the closest existing attempt at an ordering primitive.
  It is still a stub, and co-installation's finding — that location, not declared precedence, wins —
  is direct evidence that a precedence order without enforcement is not a control.
- [[concepts/skill-library]] and [[concepts/skillopt]] treat skills as things to *grow*. This page is
  about what breaks when they grow without resolution.
- Runtime-side consequence: [[concepts/runtime-oversight-knobs]] notes a monitor grading "the right
  behaviour" has no fixed referent while the namespace has no exclusivity primitive.
- The same "outcome metric can't see the route taken" blind spot as
  [[concepts/evaluation/agent-overclaiming]] and [[concepts/evaluation/reward-hacking]].

## Open questions

1. Who owns the registry, and does a `SKILL.md` reference resolve at **install** time or at **run**
   time? Run-time resolution reintroduces the network into a tool that currently works offline.
2. Copy-network inference is fit on git history — forks, squashes, and vendored directories
   systematically hide edges, so the concentration numbers are likely a *lower* bound.
3. Ranking is trained on historical adoptions: a genuinely new origin repository is cold-start
   invisible **by construction**.
4. Would a declared `exclusive-owner` field in `SKILL.md` be honoured at all, given selection is
   description-mediated? Unmeasured.

## Sources

- Fahd Seddik, *Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub*,
  arXiv:2610.11169 (2026-10-08) — `raw/papers/2026-10-11_2610.11169_skill-constellations-github-supply-chain.md`
- Chaoliang Yan, Zihao Xu, Yuekang Li, et al., *One Skill Too Many: How Co-Installed Skills Conflict
  in Coding Agents*, arXiv:2610.11647 (2026-10-08) — `raw/papers/2026-10-11_2610.11647_skill-co-installation-conflict.md`
