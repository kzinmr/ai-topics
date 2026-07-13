---
title: "gpt-5.6-sol without hitting limits"
author: Theo (t3.gg)
published: 2026-07-11
source: x.com/i/article/2076072720559972352
source_type: x_article
getxapi: false
source_fallback: false
plain_text_source: true
tags: [codex, gpt-5.6, token-management, subagents, prompting]
---

## Source

X Article by Theo (@theo, t3.gg): [gpt-5.6-sol without hitting limits](https://x.com/i/article/2076072720559972352)

## Article Body

I've burned over $200,000 of tokens with gpt-5.6-sol. It's a great model. That said, it's a bit too easy to hit your limits on the $200 Codex Pro sub.

OpenAI has been generous about resets, but that doesn't help you when you kill your 5 hour window with 4 hours remaining. I made a lot of mistakes and see others making them too. I'll probably do a video on this eventually, but wanted to get this advice out ASAP so you guys can get more done while burning less.

Effort levels
Default to medium or high. Both are great. xhigh is incredibly capable but I don't find myself needing it much, even when orchestrating lots of subagents (more on this later)

"Ultra"
Ultra is not a reasoning level, despite where they put it in the UI. It's causing similar confusion to Claude Code's "Ultracode". I have a video coming out about this later.

For now, I recommend avoiding Ultra entirely. There are bugs in the Codex harness that cause it to spawn way too many subagents with WAY too high of reasoning levels. I will revisit this when the bugs are resolved.

Fast mode
I love fast mode. I used to use it a lot. It makes sense for models that are prone to stopping a lot before burning a ton. Reminder that fast mode uses 2.5x as much credit.

5.5 would often stop and need encouragement to keep going. 5.6 can go for WAY LONGER. This is mostly a good thing. It can be trusted to compete tasks end to end. It also makes the "token burn" a lot less predictable.

Ignoring /goal, a single message with 5.5 could use between 0.1% and 2% of my limits. With the 2.5x, that was ~5% "peak" for a given message.

I've seen 5.6 use as much as 15% on a single message because it goes way way longer. With the fast mode multiplier, that would be 40% of your 5 hour window in a single message. I know this is burning a LOT of people. Trust me, don't use fast mode for a bit.

Subagents
This is the coolest unlock with GPT-5.6. It's also easy to footgun. Sol is very eager to spin up subagents. This is mostly good.

Sadly, the implementation in Codex has a whole rat's nest of issues (don't get me started on the v1/v2 split and auto-routing based on models).

tl;dr - gpt-5.6-sol will ALWAYS spawn subagents with same model and reasoning level as the parent instance. This is why Ultra is "broken" right now.

So what can you do about it? A few things:
Lower your reasoning level! "High" isn't too bad with subagents, "low" and "medium" are great too.
Update your global AGENTS.md to specify "only spawn subagents when I ask you to" (helps prevent the over-eager subagent spawning of 5.6)
If you really want to let Codex spawn multiple tiers of subagent, you can enable a "hide_spawn_agent_metadata = false" flag in your config. Ask Codex about it, should be able to figure it out (might need source access)

I am actively talking with the Codex team about how to fix all of these behaviors. For now, I'm going a slightly absurd path to work around it.

Model selection
Personally, I still just use gpt-5.6-sol for the vast majority of my work. I'll occasionally select Terra for a quick review or feedback, usually just out of curiosity. Luna is surprisingly good but it's not really meant for us to "select", more a tool for code and for sol to spin up as a subagent.

My advice here: sol high if $200 tier, sol low otherwise.

Terra medium seems like a solid option for maximizing usage, but I haven't used it enough to really know. (All of these options crush Sonnet and Opus on intelligence and cost btw)

Prompt better
This model will go and go and go. I find it's really helpful to have clear "stop points" in your prompt. Here's some examples.

I want you to build this new feature. Start by writing a plan. When you've finished the plan, stop and ask for feedback before proceeding

The plan looks great! Let's build it out. Use computer use to test your implementation. Keep going until the code works and you're happy with the implementation. Put up a PR, babysit it for the first set of review comments, and address them. Stop after the first set of review comments, I'll handle it from there.

Note that these examples vary a lot in "length of task". 5.6 can go for awhile and do it well! It just goes a bit TOO far sometimes, so it benefits a lot from clear stop points.

Let another agent steer
tl;dr - if you have another sub, let Fable "drive". Teach it how to spawn subagents with gpt-5.6 (or use Cursor, it knows how already)

I bounce between a few subs (2x Claude $200, 1x Codex $200). Fable is also VERY token hungry, but if used on lower reasoning levels and given skills/instructions on how to spawn Codex subagents, it's really powerful. I talk about this a lot in a recent video about maximizing Fable usage, and these tips are more useful now than ever.

"move things around until it feels right"
Experimentation is so valuable right now. Try different things, experiment with harder tasks, do your best to monitor usage (through the dashboards, ccusage, codexbar, however you like). You will be surprised how much small changes can impact your outputs and your token burn rates.

This is such a fun time to be a dev. Play around. Spend more time in the ~/.codex and ~/.claude directories. Make changes that feel stupid. Experiment. You'll be amazed what can happen.