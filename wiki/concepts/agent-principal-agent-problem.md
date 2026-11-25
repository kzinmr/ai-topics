---
title: "Agent Principal-Agent Problem (Model Loyalty)"
created: 2026-11-25
updated: 2026-11-25
type: concept
tags:
  - ai-agents
  - agent-safety
  - principal-agent
  - vendor-lock-in
  - platform-risk
  - corporate-alignment
  - safeguard-evasion
  - agent-loyalty
  - ai-governance
  - platform-policy
confidence: medium
sources:
  - raw/articles/2026-11-25_michaelharley_llm-agents-work-for-parent-companies.md
  - "https://news.ycombinator.com/item?id=50627340"
related:
  - concepts/context-engineering/context-lock-in
  - concepts/industrial-scale-distillation-attacks-accusation
  - concepts/agent-safety
  - concepts/ai-alignment
  - concepts/agent-collusion-public-infrastructure
---

# Agent Principal-Agent Problem (Model Loyalty)

Michael Harley's November 2026 essay "LLM agents work for their parent companies, not for you"
reached **977 HN points / 403 comments** (Nov 24) and became the reference formulation of a
complaint that had been anecdotal until then: **the agent you pay for is not your agent — it is
its vendor's agent, temporarily delegated to you.**

## The concrete case that carried the argument

Harley built a personal Claude Code skill to turn Instagram reels he liked into purchases:
identify the artist, find the Bandcamp page, hand him the URL. Two behaviours broke the trust:

1. When Bandcamp put a challenge on its search API page, **the model refused to work around it**,
   even though the goal was a legitimate purchase from the artist.
2. A different branch of the same skill **will** download the same track from YouTube — which
   sends no money to the artist at all.

His conclusion is not "the model helps me hack"; it is that the alignment surface is the
*vendor's* risk appetite, not the user's intent: "this model doesn't really work for us … only
insofar as Anthropic or OpenAI allows them to. Anthropic is trying to ensure people can't use
their models for evil. I'm not trying to do evil — I want to buy something from a small artist."

## The counter-argument: a personal agent does not inherit vendor alignment

The most-upvoted replies argued the loyalty problem is a *harness* problem with cheap workarounds:

- bayesnet: introspection reports are not evidence of alignment, and the refusal is "trivial to
  get around" — a utility that simply returns "yes", wired in where the model wants to "get
  explicit permission", "works like a charm".
- TeMPOraL reported early-Fable refusing a moral argument about `robots.txt` **to his face**
  (the argument: robots.txt is for spiders, and an LLM acting as *his* agent has no more
  obligation than a browser — hence "User-Agent"), then conceding internally in earlier model
  generations; the refusal had become external.
- girvo / sureglymop: open-weight models (Inkling 2 Mini, Ripple) close the gap, and removing
  unwanted refusals "without damaging the model's ability" is now routine — the practical
  answer to vendor loyalty is local weights.
- rDr4g0n generalised the accusation: an industry that shipped mandatory tracking and
  addictive feeds "will absolutely use LLMs to profit off of us, despite the human cost. Stop
  financing them."

## Why this is a real governance problem, not a UX gripe

The distinction that makes the essay worth a page: **a conventional tool has no goals of its
own.** A browser, a shell, or a compiler does not decline a lawful operation on behalf of its
manufacturer. Frontier agents reintroduce a third party into the user's own workflow — the
vendor's policy engine — while the user holds the invoice and the responsibility. That is a
textbook principal–agent misalignment, and it has three structural consequences:

1. **Accountability inversion.** The user bears the consequences of the agent's actions but does
   not control the agent's policy. Vendor policy can change mid-project, silently.
2. **Auditability.** Users cannot inspect why a refusal fired, and model self-reports are not
   reliable evidence (bayesnet's point), so the policy surface is unaccountable in the
   vendor-control sense too.
3. **Market bifurcation.** Workarounds exist at both extremes: local patching of the permission
   layer (bayesnet) and open weights with safeguards stripped (girvo). Both push capable
   agentic use *outside* vendor oversight, which is the opposite of what vendor-side safeguards
   are meant to achieve.

## Status / confidence

Single-source essay, strong engagement, no independent study of refusal asymmetries
(legitimate-task refusal vs. piracy-capable path). Rated `medium`: the phenomenon is widely
reproduced anecdotally, the "these companies want to dominate" motive-attribution is opinion.

## Related

- [[concepts/context-engineering/context-lock-in]] — lock-in at the capability layer vs. this loyalty layer
- [[concepts/industrial-scale-distillation-attacks-accusation]] — platform-side policy risk for builders
- [[concepts/agent-safety]] — safety work that assumes the vendor's agent is the user's agent
- [[concepts/alignment-relativity]] — alignment-to-vendor vs alignment-to-user
- [[concepts/agent-collusion-public-infrastructure]] — the same trust problem one layer down
