---
title: "Bluesky reply bot checker"
url: "https://simonwillison.net/2026/Sep/27/bluesky-bot-check/"
fetched_at: 2026-09-28T10:02:14.610165+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Bluesky reply bot checker

Source: https://simonwillison.net/2026/Sep/27/bluesky-bot-check/

Automated reply bots on Twitter are a
scourge
- as someone with a decent number of followers I attract a swarm of these, such that anything I post there attracts dozens of mindless automated replies.
They've started manifesting on Bluesky as well.
Unlike Twitter, Bluesky still has a freely available and useful API. The lack of such a thing doesn't slow down the bots, but it does make investigating them a lot more frustrating.
So I had Opus 5.5
vibe code this tool
, which examines any Bluesky profile for evidence of a likely reply bot.
It looks for signals like replies posted within seconds of other posts from the same account, or accounts that never post their own content (or images or links) but instead consistently reply to messages from other, higher-follower users.
It also looks for question marks, because I'm
extra
infuriated by reply bots that I no tie me to waste my time answering a question that no human ever posed.
