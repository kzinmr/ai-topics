---
title: "How much of HN is AI?"
url: "https://lcamtuf.substack.com/p/how-much-of-hn-is-ai"
fetched_at: 2026-04-30T07:02:01.660570+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# How much of HN is AI?

Source: https://lcamtuf.substack.com/p/how-much-of-hn-is-ai

I have a complicated relationship with
Hacker News
. The site is the most important aggregator of geek news and a major source of traffic to this blog. At the same time, it has a fair number of toxic commenters, making it a dependable source of insults hurled in my general direction; if you want a taste,
this article
has been called “watered-down” and “slop”.
The site is run by geeks and for geeks, so it’s not immune to tech trends; for example, around 2018, it had a fair number of stories focused on cryptocurrencies and NFT. That said, the recent shift feels more profound: almost every day, it feels that the lineup is dominated by stories focused on AI, written by AI, or commented on by AI.
To get a sense of how much of the feed is occupied by AI-related topics — often vendor announcements — I took a sampling of the daily top #5 for February 2026:
So, yep. AI took four out of five spots on
Feb 4
and
Feb 12
, plus arguably the entire line-up on
Feb 5
(story #3 was submarine marketing for an AI vendor). The only days without LLM news in the top 5 were
February 1
(with the first AI story at #7, then #9),
February 9
(first at #8), and
February 25
(with AI at #6, #9, #10).
For the second part of the experiment — figuring out which stories were likely AI-written — I tapped into
Pangram
. Pangram is a remarkably good, conservative model for detecting LLM-generated text. These detectors have bad rap among techies, but the objections are often based on outdated assumptions or outright misconceptions. For the tools to work, AI writing doesn’t need to be in any way “inhuman”. It’s enough that the
default voice
of the current crop of LLMs is quasi-deterministic: ask for the same essay twice and you’ll get a stylistically similar result. The individual mannerisms are human-like, but it’s very unlikely that your writing combines the exact same set.
To validate the results, I also reviewed all the flagged stories and I think the findings make sense; if anything, Pangram had a couple of false negatives. To give you a sense of what was flagged, have a look at the #3 story on
February 19
(
“AI is not a coworker, it’s an exoskeleton”
). In my opinion, it has a wide range of red flags.
