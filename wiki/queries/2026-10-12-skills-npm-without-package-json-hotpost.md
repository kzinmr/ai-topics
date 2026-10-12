---
title: "Queries — 2026-10-12 morning hot-post: skills are npm without package.json"
created: 2026-10-12
updated: 2026-10-12
type: query
tags: [agent-skills, supply-chain, agent-governance, benchmark-framing, knowledge-management]
confidence: high
sources: [raw/papers/2026-10-11_2610.11169_skill-constellations-github-supply-chain.md, raw/papers/2026-10-11_2610.11647_skill-co-installation-conflict.md]
related: [concepts/agent-skill-ecosystem-missing-package-manager, concepts/skill-constellations-github-supply-chain, concepts/skill-co-installation-conflict, concepts/five-tier-skill-precedence, concepts/runtime-oversight-knobs, concepts/security-and-governance/agent-skill-supply-chain-attacks]
---

# Skills Are npm Without `package.json`

Morning hot-post (2026-10-12 09:30 JST). Forwardable synthesis of the two 2026-10-08 arXiv papers,
framed as "the skill namespace is a 2010 package manager minus six primitives." Primary hub page:
[[concepts/agent-skill-ecosystem-missing-package-manager]].

## Thesis

Distribution is solved (copy-paste works), resolution is not. So the dominant failures are not
malicious payloads but *silent selection* — whichever `SKILL.md` the filesystem placed first.

## Load-bearing numbers

| Measurement | Value | Source |
|---|---|---|
| Skill adoptions traced via git history | 2,193,119 | arXiv:2610.11169 |
| Audit yield: top-100 model-ranked vs top-100 starred repos | 14.9% vs 0.5% (~30×) | arXiv:2610.11169 |
| Skills co-installed with a same-job rival | ~1 in 4 | arXiv:2610.11647 |
| Runs where the rival skill takes over | 1 in 5 | arXiv:2610.11647 |
| Exclusive core functions lost when rival opens first | > 1 in 3 | arXiv:2610.11647 |
| What decides the winner | install **location** (listing order barely matters) | arXiv:2610.11647 |

## Key framings delivered

1. Six missing primitives: registry, version pinning, provenance/signature, update propagation,
   name resolution, dependency solver — each row a mechanism, not a metaphor.
2. Stars are not a substitute for a registry: 30× audit-yield gap.
3. Copies almost never change with their source → a fix at origin structurally cannot propagate.
4. Task completion unchanged during conflicts → completion-based benchmarks report green while
   normative constraints (git ban, mandatory verification) are silently void.
5. Closest existing ordering attempt [[concepts/five-tier-skill-precedence]] is still a stub — and
   "location not declared precedence wins" is direct evidence a precedence order without
   enforcement is not a control.
6. Runtime-side consequence: [[concepts/runtime-oversight-knobs]] — a monitor grading "the right
   behaviour" has no fixed referent while the namespace lacks an exclusivity primitive.

## Dedup

10-11 night post used runtime-oversight-knobs/Cadence/OnTrack/ISE as PRIMARY; this post uses them
only as a supporting cross-link. Skill ecosystem pages (agent-skill-ecosystem-missing-package-manager,
skill-constellations-github-supply-chain, skill-co-installation-conflict) appear as primary here for
the first time.
