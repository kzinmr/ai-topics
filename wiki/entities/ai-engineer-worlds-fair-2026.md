---
title: "AI Engineer World's Fair 2026 — San Francisco, June 22-25"
type: entity
created: 2026-09-15
updated: 2026-09-15
confidence: medium
tags:
  - conference
  - ai-agents
  - ai-software-engineering
  - harness-engineering
  - open-source
aliases: ["AIE 2026", "AI Engineer World's Fair", "AI Engineer Conference 2026"]
sources:
  - raw/articles/2026-09-15_ghuntley_can-we-have-it-both.md
  - raw/articles/2026-09-14_ghuntley_a-featureless-world.md
  - raw/articles/seangoedecke.com--ai-is-breaking-our-proxies-for-expertise--0af86730.md
related:
  - concepts/agent-slop
  - concepts/harness-engineering
  - concepts/proxies-for-expertise
  - entities/geoffrey-huntley
  - entities/swyx
  - entities/amberawn
---

# AI Engineer World's Fair 2026

The third annual AI Engineer World's Fair (AIE) ran **June 22–25, 2026** in San Francisco. It has become the flagship practitioner conference for the people building on top of frontier models, and the 2026 edition is notable less for its announced lineup than for what attendees took away from it: a set of shared assumptions about agent reliability, harness design, and developer reputation that several of the year's most-discussed essays pushed back against.

## Why This Page Exists (post-event discourse)

AIE 2026 was a citation hub for the "agent engineering orthodoxy" that the rest of 2026's best criticism targeted:

- **Geoffrey Huntley** opened *"Can we have it both ways?"* by recounting his AI Engineer SF talk "**The Real Coding Agent Is a Graph of Interacting Feedback Loops**" and his "Featureless World" talk — then arguing the agent-coding field has stopped doing the eval work its own conference narrative is built on. Key accusation: **"we cite each other's talks at AI Engineer conferences as evidence enough."** See [[entities/geoffrey-huntley]]. ^[raw/articles/2026-09-15_ghuntley_can-we-have-it-both.md]
- **Huntley's "featureless world" thesis** (also an AI Engineer talk): frontier labs are commoditizing the outer harness layer — browser automation, memory, sandboxing — so most agent tooling is being absorbed upstream; he singles out **OpenClaw** for shipping "hundreds of thousands of lines of TypeScript" as a "giant pile of tech debt that no human being can read." ^[raw/articles/2026-09-14_ghuntley_a-featureless-world.md]
- **Sean Goedecke's** "AI is breaking our proxies for expertise" (July 2026) came out of the same ecosystem — the "leaderboard-washing" and conference-credential dynamics it describes are the reputation layer of AIE itself. Filed into [[concepts/proxies-for-expertise]]. ^[raw/articles/seangoedecke.com--ai-is-breaking-our-proxies-for-expertise--0af86730.md]

## Speaker Ecosystem

The AIE 2026 speaker list overlaps heavily with the wiki's tracked agent-infra figures: swyx (organizer), Simon Willison, Amber Wilks ("Agentic Engine Design: The Real Moat"), Eric Ma ("Agent Management System"), and Huntley himself. The conference functions as the annual roll-call of the agent-infra layer documented in [[concepts/agent-infra-landscape]].

## Key Takeaways (synthesized from post-event criticism)

1. **The harness moat is thinner than the conference implies.** If labs absorb browser automation, memory, and sandboxing (the "featureless world"), the practitioner layer's differentiation is quality *assurance*, not plumbing.
2. **Conference consensus is not evidence.** Multiple independent critics now name cross-citation between talks, funding announcements, and vendor evals as a self-sealing loop — the [[concepts/agent-slop]] "quality blind spot" in institutional form.
3. **Reputation proxies are inflating.** Conference credentials are exactly the proxy [[concepts/proxies-for-expertise]] predicts AI will saturate: cheap to obtain, hard to verify as substantive.

## Related Pages

- [[concepts/agent-slop]] — the reliability gap AIE talks tend to skip
- [[concepts/proxies-for-expertise]] — leaderboard-washing / conference-credential dynamics
- [[entities/geoffrey-huntley]] — "Featureless World" and feedback-loop theses
- [[concepts/harness-engineering]] — the layer Huntley argues is being commoditized

## See Also

- [AI Engineer (YouTube channel)](https://www.youtube.com/@aiDotEngineer) — publishes full AIE talks
- [ai.engineer](https://www.ai.engineer/) — conference site
