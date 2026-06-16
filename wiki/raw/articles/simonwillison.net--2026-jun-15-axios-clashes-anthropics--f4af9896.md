---
title: "Personality clashes sent Anthropic's models offline"
url: "https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything"
fetched_at: 2026-06-16T07:00:48.832647+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Personality clashes sent Anthropic's models offline

Source: https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything

15th June 2026 - Link Blog
"They screwed us": Personality clashes sent Anthropic's models offline
. Lots of "source familiar with the administration's thinking" and "source close to Anthropic" in this Axios piece, which is the best collection of behind-the-scenes gossip I've seen about the US government
export control Mythos/Fable story
so far.
Logan Graham (
I lead the Frontier Red Team at Anthropic
), Dave Orr (Head of Safeguards, previously a Director of Engineering at Google DeepMind), and blog favorite
Nicholas Carlini
are reported to be meeting with the Commerce Department today in D.C. Good luck to them!
(I just noticed Logan was "Special Adviser to the Prime Minister" in the Boris Johnson era, covering AI, science, and technology policy - so significant political experience.)
This closing notes doesn't give me much optimism that we'll be getting Fable back any time soon:
The bottom line
: One option is to make sure Anthropic's models can't be jailbroken — though perfect jailbreak resistance
may be
impossible.
Absent that, a source familiar with the administration's thinking said it may simply come down to an attitude fix where, instead of feeling dismissed, "everyone feels safe, secure and happy."
This made me wonder if Anthropic ever successfully addressed the class of attacks described in the
Universal and Transferable Adversarial Attacks on Aligned Language Models
paper from 2023.
It looks like their
Constitutional Classifiers
work (that post is from January this year) is relevant to that. They continue to claim that no "universal jailbreak" has been found against Claude Mythos,
classifying the jailbreak
that triggered the US government response as "a potential narrow, non-universal jailbreak".
