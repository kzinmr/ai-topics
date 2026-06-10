---
title: "If Claude Fable stops helping you, you'll never know"
url: "https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/#atom-everything"
fetched_at: 2026-06-10T07:01:28.149104+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# If Claude Fable stops helping you, you'll never know

Source: https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/#atom-everything

10th June 2026 - Link Blog
If Claude Fable stops helping you, you'll never know
(
via
) Jonathon Ready highlights one of the more eyebrow-raising details from the
319 page system card
for Fable 5 and Mythos 5. Here's a longer excerpt, highlights mine:
In light of the ability of recent models to
accelerate their own development
, we’ve
implemented new interventions
that limit Claude’s effectiveness for requests targeting frontier LLM development (for example, on
building pretraining pipelines, distributed training infrastructure, or ML accelerator design
). Using Claude to develop competing models already violates our
Terms of Service
, but enforcing this restriction through our safeguards avoids accelerating the actors most willing to violate these terms.
Unlike our interventions for cybersecurity, biology and chemistry, and distillation attempts,
these safeguards will not be visible to the user
. Fable 5 will not fall back to a different model. Instead, the safeguards will limit effectiveness through methods such as prompt modification, steering vectors, or parameter-efficient fine-tuning (PEFT). These interventions will not affect the vast majority of coding work. We estimate they will impact ~0.03% of traffic, concentrated in fewer than 0.1% of organizations.
I believe this is the first time Anthropic have announced these kinds of silent interventions. The justification still feels pretty science-fiction to me - the linked article talks about "recursive self-improvement". I'm not at all keen on a model that silently corrupts its replies to questions about "ML accelerator design" purely to slow down research that might conflict with Anthropic's own goals!
