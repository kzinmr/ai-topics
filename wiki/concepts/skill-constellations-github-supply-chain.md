---
title: "Skill Constellations: The Agent Skill Supply Chain on GitHub"
created: 2026-10-11
updated: 2026-10-11
type: concept
tags: [agent-skills, supply-chain, security, open-source, reproducibility, agent-governance]
sources: [raw/papers/2026-10-11_2610.11169_skill-constellations-github-supply-chain.md]
confidence: high
related: [concepts/skill-co-installation-conflict, concepts/security-and-governance/agent-skill-supply-chain-attacks, concepts/agent-skills, concepts/skill-library, concepts/apex-adversarial-skill-chain-hijacking, concepts/skillopt]
---

# Skill Constellations: The Agent Skill Supply Chain

Agent skills (`SKILL.md` + scripts) run with **the user's permissions** inside Claude Code, Codex,
and similar [[concepts/agent-harness-primitives|coding harnesses]]. They spread by **copy-paste
between repositories** — which makes them a software supply chain with **no registry, no versions,
no provenance**. Consequences that follow directly: the origin of a copied skill is unknown, the
reach of a security fix is unknown, and which repositories warrant review is unknown.

## The dated copy network

Prior studies record which repositories hold a skill at a single point in time, which structurally
cannot reveal *who copied from whom*. This work reconstructs a **dated copy network** from the
**git history of every `SKILL.md` in GitSkills**, covering **2,193,119 skill adoptions** across
GitHub, plus an interactive viewer.

| Property | Measured |
|---|---|
| Skill adoptions traced | 2,193,119 |
| Origin concentration | a few repositories are the source of almost all copies |
| Do GitHub stars identify origins? | **No** |
| Do copies track their source? | almost never change with their source |
| Audit yield: top-100 model-ranked repos | prevents **14.9%** of later adoptions of high-risk skills |
| Audit yield: top-100 most-starred repos | prevents **0.5%** |

A **model of which repositories others copy from** is fit on the network and used to rank
repositories for audit. The 30× gap versus stars is the actionable result: security engineers get a
short list to check *before* a skill spreads, rather than after.

## The fix is distribution, not vetting

Because copies almost never change with their source, **a fix at the source rarely reaches them**.
That makes post-hoc patching structurally unavailable at scale. The authors' recommendation:
platforms should distribute **versioned references rather than copies** — i.e. import the npm/cargo
model into a namespace that currently has none.

## Why this differs from skill-security literature

[[concepts/security-and-governance/agent-skill-supply-chain-attacks]] and
[[concepts/apex-adversarial-skill-chain-hijacking]] model a *malicious payload* moving through the
ecosystem. This page is about the **topology that makes any payload untraceable** — and about
benign-but-stale skills, which is the far more common failure. It is also the structural explanation
for [[concepts/skill-co-installation-conflict]]: if skills spread by untracked copying, near-duplicate
co-installation is the expected end state, not an anomaly.

## Open questions

- Who owns the registry, and does a `SKILL.md` reference resolve at install time or run time?
- Copy-network inference is fit on git history; forks, squashes, and vendored directories may
  systematically hide edges.
- Ranking is trained on historical adoptions — a novel origin repository is cold-start invisible by
  construction.

## Source

Fahd Seddik, *Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub*,
arXiv:2610.11169 (2026-10-08) —
`raw/papers/2026-10-11_2610.11169_skill-constellations-github-supply-chain.md`
