---
title: "Get Player Stats From Your Minecraft Server Logs"
url: "https://jayd.ml/2026/10/08/minecraft-log-analyzer.html"
fetched_at: 2026-10-09T10:01:08.122459+00:00
source: "jayd.ml"
tags: [blog, raw]
---

# Get Player Stats From Your Minecraft Server Logs

Source: https://jayd.ml/2026/10/08/minecraft-log-analyzer.html

NOTE:
The subject of this post was vibecoded, but this post is 100% written
by a real life human being
I have a Minecraft server with about 6 years of logs (covid minecraft server baby!)
and I always wondered who has played the most and when, so I had a friendly robot
slop together a little go app you can run on a cronjob to generate an HTML report.
For a demo of the report, see here:
https://jaydens-tasty-slop.github.io/minecraft-log-analyzer/
Here’s the repo: https://github.com/jaydens-tasty-slop/minecraft-log-analyzer
It saves events it parses out of the logs into a sqlite database, then incrementally
parses new files daily if you run it in a cronjob.
Features
Server Stats:
Total unique players
Total play time in hours
Play time by year
Play time by player
Player Stats:
Play time (hours) (and by year)
Play time with other players (see who plays with who)
Sessions
Time played
Social time (with at least 1 other player on)
Loner time (playing alone)
Longest, shortest, and average session
Longest, shortest, and minimum in-game lifetime
Deaths
Chat messages / commands
Previous aliases
Chat Messages:
By default there is also a chat log rendered (but not linked to from other pages)
Pass
-no-chat
to omit the generated
chat.html
transcript. Chat counts remain
in player statistics.
