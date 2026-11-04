---
title: "Revolut moves to self-hosted GLM (X post by Guillermo Flor)"
source: "https://x.com/guilleflorvs/status/2117379073785696395"
author: "Guillermo Flor (@guilleflorvs)"
date: 2026-11-02
type: raw-article
captured: 2026-11-04
note: "Single-tweet announcement; full quoted talk by David Abitbol (Revolut AI ops lead) at https://www.youtube.com/watch?v=Ok6QdZHCcI8 (linked by swyx on HN). Content via cdn.syndication.twimg.com tweet-result API."
---

# Revolut moves to self-hosted GLM

BREAKING: Revolut moved ~2,000 engineers onto self-hosted GLM for coding and pushed Claude Code and Codex to the exception list.

Per David Abitbol, who leads AI ops there: 56 Nvidia B200s, a blended 30 cents per million tokens, roughly a tenth of what they paid Anthropic and [OpenAI — truncated in tweet; see HN thread and YouTube talk]

— Guillermo Flor (@guilleflorvs), 2026-11-02T22:11:24Z. 7,514 likes, 273 replies.

## HN discussion context (HN item 50350004, 190 points as of 2026-11-04)

- **swyx**: "their full talk is here" → https://www.youtube.com/watch?v=Ok6QdZHCcI8 (David Abitbol's full talk on the Revolut GLM migration)
- **mtrovo**: "30 cents per million tokens is wild. The relevant question is how easy is to setup 56x B200s in a cluster, are we talking about an adhoc infra team job or clicking a button on AWS?"
- **gosen**: estimates ~$2.5M-3M hardware investment + operating costs; wonders what prior monthly token spend justified the switch
- **InsidiousWombat**: "If investors knew how powerful open models are the AI companies valuation would tank overnight"
- **aurareturn**: open-weight models are "good enough" for most SWE tasks, but goal posts will move; frontier labs will find areas needing absolute frontier
- **jacquesm**: did the same on much less powerful hardware; key motive is not trusting inference suppliers long-term with your data — "absolutely not"
- **torginus**: "there's little proof that the quality gap between open models and OAI/Anthropic stuff translates to business results, but you surrender all control of your data to a third party" — financial regulations can outright block third-party data processing (esp. outside national/EU jurisdiction)
- **injidup**: only relevant past ~150 engineers when enterprise bucket forces per-token pricing rather than subsidized seat plans
- **redmalang**: ~90% of their work now goes to open-source models; open models "generally more closely follow instructions" on longer timeframes
- **littlecranky67**: "the gains showed up when tokens stopped being rationed" — observed at a large insurance company with junior-heavy dev teams
- **andy99**: "a sane version of what 'sovereign' AI can look like" — contrasts with Canada's national AI plan; even if GLM is slightly behind it is close to the Pareto frontier; could sell spare capacity on OpenRouter
