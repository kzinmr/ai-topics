---
title: "Exclusive: Microsoft To Shift GitHub Copilot Users To Token-Based Billing, Tighten Rate Limits"
url: "https://www.wheresyoured.at/news-microsoft-to-shift-github-copilot-users-to-token-based-billing-reduce-rate-limits-2/"
fetched_at: 2026-04-28T07:01:43.193828+00:00
source: "wheresyoured.at"
tags: [blog, raw]
---

# Exclusive: Microsoft To Shift GitHub Copilot Users To Token-Based Billing, Tighten Rate Limits

Source: https://www.wheresyoured.at/news-microsoft-to-shift-github-copilot-users-to-token-based-billing-reduce-rate-limits-2/

Executive Summary:
Internal documents reveal that Microsoft plans to temporarily suspend individual account signups to its GitHub Copilot coding product, as it transitions from requests (single interactions with Copilot) towards token-based billing.
The documents reveal that the weekly cost of running Github Copilot has doubled since the start of the year.
Microsoft also intends to tighten the rate limits on its individual and business accounts, and to remove access to certain models for those with the cheapest subscriptions.
Note:
Microsoft has now confirmed some of these details in a blog post
.
Leaked internal documents viewed by
Where’s Your Ed At
reveal that Microsoft intends to pause new signups for the student and paid individual tiers of AI coding product GitHub Copilot, tighter rate limits, and eventually move users to “token-based billing,” charging them based on what the actual cost of their token burn really is.
Explainer:
At present, GitHub Copilot users have a certain amount of “
requests
” — interactions where you ask the model to do something, with Pro ($10-a-month) accounts getting 300 a month, and Pro+ ($39-a-month) getting 1500. More-expensive models use more requests, cheaper ones use less (I’ll explain in a bit).
Moving to “token-based billing” would mean that instead of using “requests,” GitHub Copilot users would pay for the actual cost of tokens. For example,
Claude Opus 4.7 costs $5 per million input tokens (stuff you feed in) and $25 per million output tokens
(stuff the model outputs, including tokens for chain-of-thought reasoning.
Token-Based-Billing
The document says that although token-based billing has been a top priority for Microsoft, it became more urgent in recent months, with the week-over-week cost of running GitHub Copilot nearly doubling since January.
The move to token-based billing will see GitHub users charged based on their usage of the platform, and how many tokens their prompts consume — and thus, how much compute they use. It’s unclear at this time when this will begin.
This is a significant move, reflecting the significant cost of running models on any AI product. Much like
Anthropic, OpenAI, Cursor, and every other AI company
, Microsoft has been subsidizing the cost of compute, allowing users to burn way, way more in tokens than their subscriptions cost.
The party appears to be ending for subsidized AI products, with Microsoft’s upcoming move following Anthropic’s (
per The Information
) recent changes shifting enterprise users to token-based billing as a means of reducing its costs.
Pauses on Signups for Individual and Student Tiers
GitHub Copilot currently has two tiers for individual developers — a $10-per-month package called GitHub Copilot Pro, and a $39-a-month subscription called GitHub Copilot Pro+.
According to the leaked documents, both of these tiers will be impacted by the shutdown, as will the GitHub Copilot Student product, which is included within the free GitHub Education package.
Removing Opus From GitHub Copilot Pro, Rate Limits Tightened on GitHub Copilot Pro, Pro+, Business, Enterprise
According to the documents, Microsoft also intends to tighten rate limits on some Copilot Business and Enterprise plans, as well as on individual plans, where limits have already been squeezed, and plans to suspend trials of paid individual plans as it attempts to “fight abuse.”
Although Microsoft has regularly tweaked the rate limits for individual GitHub Copilot accounts, most recently at the start of April, the document notes that these changes weren’t enough, and that more rate limits changes are to come in the next few weeks.
As part of this cost-cutting exercise, Microsoft intends to remove Anthropic’s Opus family of AI models from the $10-per-month GitHub Copilot Pro package altogether.
Microsoft
most recently retired Opus 4.6 Fast at the start of April for
GitHub
Copilot Pro+ users
, although this decision was framed as a way to “further improve service reliability” and “[streamline] our model offerings and focusing resources on the models our users use the most.”
Other Opus models — namely Opus 4.6 and Opus 4.5 — will be removed from the GitHub Copilot Pro+ tier in the coming weeks,
as Microsoft transitions to Anthropic’s latest Opus 4.7 model
.
The move towards Opus 4.7 will likely see GitHub Copilot Pro+ users reach their usage limits faster.
Microsoft is offering a 7.5x request multiplier until April 30
— although it’s unclear what the multiplier will be after this date. This might
sound
like a good thing, but it actually means that each request using Opus 4.7 is actually 7.5 of them.
Redditors immediately worked that out and are a little bit worried
.
Premium request multipliers allow GitHub to reflect the cost of compute for different models. LLMs that require the most compute will have higher premium request multipliers compared to those that are comparatively more lightweight.
For example, the GPT-5.4 Mini model has a premium request multiplier of 0.33 — meaning that every prompt is treated as one-third of a premium request — whereas the now-retired Claude Opus 4.6 Fast had a 30x multiplier, meaning each request was treated as
thirty of them.
The standard version of Claude Opus 4.6 has a premium request multiplier of three — meaning that, even with the promotional pricing, Claude Opus 4.7 is around 250% more expensive to use.
The announcements for all of these changes are scheduled to take place throughout the week.
If you liked this news hit and want to support my independent reporting and analysis, why not subscribe to my premium newsletter?
It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of
NVIDIA
,
Anthropic and OpenAI’s finances
, and
the AI bubble writ large
. I recently put out the timely and important
Hater’s Guide To The SaaSpocalypse
, another on
How AI Isn't Too Big To Fail
, a deep (17,500 word)
Hater’s Guide To OpenAI
, and just last week put out the massive
Hater’s Guide To Private Credit
.
Subscribing to premium is both great value and makes it possible to write these large, deeply-researched free pieces every week.
