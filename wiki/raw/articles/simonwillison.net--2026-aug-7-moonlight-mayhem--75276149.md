---
title: "Moonlight & Mayhem (Raccoon Heist by Codex + GPT-5.6 Sol Ultra)"
url: "https://simonwillison.net/2026/Aug/7/moonlight-mayhem/#atom-everything"
fetched_at: 2026-08-08T10:13:47.001714+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Moonlight & Mayhem (Raccoon Heist by Codex + GPT-5.6 Sol Ultra)

Source: https://simonwillison.net/2026/Aug/7/moonlight-mayhem/#atom-everything

7th August 2026 - Link Blog
Moonlight & Mayhem (Raccoon Heist by Codex + GPT-5.6 Sol Ultra)
. On Wednesday I wrote about
One-shotting a Raccoon Heist game using Claude Fable 5
, where I had Claude Fable 5 build a full working game from a premise I generated with GPT-3 and DALL-E
four years ago
.
I decided to pose the
exact same prompt
to Codex Desktop running GPT-5.6 Sol Ultra - the mode where Sol makes
aggressive
use of sub-agents - to see how it would do.
It produced a much better game! Here's
Moonlight & Mayhem
-
GitHub repository here
, including the
textures and prompts
it generated using
gpt-image-2
.
Your browser does not support HTML5 video.
The original GPT-3 generated game description included:
In “Raccoon Heist”, you and your team of thieving raccoons are tasked with pulling off a series of daring heists. From robbing banks to stealing priceless art, no job is too big or too small for your furry crew.
Fable's version had you as a single raccoon running around a back yard collecting coins and fish. GPT-5.6 Sol has you in a museum, rescuing your two other raccoon crewmates in order to stack on top of each other and bust the golden sardine out of its case.
Much more heisty!
There was one catch though: the version produced from the one-shot prompt had a bug where each raccoon had an eyeball that was enlarged to the size of a giant sphere floating over their head!
You can
play that version here
.
Despite reviewing screenshots during development Codex failed to spot and correct this bug.
I fixed it by prompting:
Why do the raccoons have huge black spheres on them?
And then:
Fix it
Which resulted in
this fix
.
I shared
the full Codex transcript
in the repository - I wish Claude Code had the same "copy as Markdown" feature.
Codex spent 52 minutes on the project. Here's the
AgentsView
cost estimate for that session if I had been paying full API prices as opposed to using my monthly Codex subscription:
