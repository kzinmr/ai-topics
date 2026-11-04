---
title: "Revolut Self-Hosted GLM Migration"
created: 2026-11-04
updated: 2026-11-04
type: concept
aliases: [revolut-glm-migration, revolut-self-hosted-glm]
tags:
  - case-study
  - open-weight
  - self-hosted-inference
  - coding-agents
  - fintech
  - token-economics
  - china
sources:
  - raw/articles/x.com--guilleflorvs-revolut-self-hosted-glm--2026-11-02.md
  - https://news.ycombinator.com/item?id=50350004
  - https://www.youtube.com/watch?v=Ok6QdZHCcI8
confidence: medium
---

# Revolut Self-Hosted GLM Migration

On **Nov 2, 2026**, Guillermo Flor (@guilleflorvs) announced on X (190 pts / 7.5k likes on HN as of Nov 4): **Revolut moved ~2,000 engineers onto self-hosted GLM for coding, pushing Claude Code and Codex to the exception list.** The numbers come from **David Abitbol**, Revolut's AI-ops lead, whose full talk is on YouTube.

## Reported numbers (single-source, treat with caution)

| Item | Value |
|---|---|
| Engineers migrated | ~2,000 |
| Model | GLM (Zhipu / Z.ai, open-weight) — see [[concepts/glm-5-3]] |
| Hardware | 56 Nvidia B200s |
| Blended cost | ~$0.30 per million tokens |
| vs. prior API spend | ~1/10th of what they paid Anthropic and OpenAI |

**Confidence: medium.** All figures are company-reported via one tweet + one conference talk; no independent audit of utilization, TCO (power/cooling/staff), or output quality. Commenter estimate for the B200 fleet: ~$2.5-3M hardware plus opex (gosen, HN).

## Why it matters

1. **Largest disclosed open-weight coding migration at fintech scale.** It converts the [[concepts/open-weight-vs-closed-llm-gap]] debate from benchmark charts into a production procurement decision by a regulated bank-like institution — the same "irresistibly good and cheap on-prem" thesis IBM's CEO articulated in Oct 2026, now with concrete unit economics.
2. **Data sovereignty as the binding constraint, not just cost.** HN practitioners (jacquesm, torginus) stress that financial regulation often *prohibits* third-party inference on customer-adjacent data — making self-hosting a compliance requirement where per-token pricing (see [[concepts/token-economics]]) is secondary. This is enterprise-scale [[concepts/sovereign-ai]] in practice;andy99 called it "a sane version of what 'sovereign' AI can look like."
3. **The seat-plan cliff.** injidup (HN): subsidized per-seat Claude Code/Codex plans break down past ~150 engineers, where enterprise per-token billing begins — exactly the threshold at which a 56×B200 cluster starts winning.
4. **Token rationing → token abundance.** littlecranky67's field report: "the gains showed up when tokens stopped being rationed" — cheap unlimited tokens change how junior-heavy teams use agents, not just what they cost.

## Counterpoints (community reaction, HN 50350004)

- Aurareturn: goal posts will move — frontier labs retain needs where absolute frontier quality matters.
- InsidiousWombat's valuation thesis ("if investors knew how powerful open models are...") is opinion, not evidence.
- B200 depreciation risk vs. Nvidia's roadmap; cluster-operation difficulty unanswered (mtrovo).

## See Also

- [[concepts/self-hosting-ai-development]] — the broader self-hosting thesis (Revolut case-study section)
- [[concepts/open-weight-vs-closed-llm-gap]] — benchmark + enterprise signal context
- [[concepts/token-economics]] — per-token vs per-seat pricing structures
- [[concepts/sovereign-ai]] — regulatory/data-control motivations
- [[entities/zhipu]] — GLM's developer
