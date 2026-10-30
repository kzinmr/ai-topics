---
title: "HN discussion: Claude Code regularly sends each background agent's transcript to its model"
url: "https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce"
hn_item: "https://news.ycombinator.com/item?id=50284255"
published: 2026-10-29
fetched_at: "2026-10-30T11:35:00+00:00"
source: "hn-algolia"
extraction: partial_blocked
points: 567
comments: 230
tags: [hn-discussion, raw]
---

# Claude Code regularly sends each background agent’s transcript to its model

Original gist: https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce
(extraction: the gist itself was not fetched; this file captures the HN submission metadata
and the full top-level thread, which contains both the independent measurement and an
on-the-record Anthropic engineer response.)

HN story: Claude Code regularly sends each background agent’s transcript to its model
URL: https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce
points=567 created_at=2026-10-29T03:33:42.000Z item=https://news.ycombinator.com/item?id=50284255

**NikZaal**: Claude Code's (CC) status summaries used 16.4% of our token spend in a week! We have investigated a source of overhead in CC: it's an agent_summary query that calls your current session/subagent model approximately every 30 seconds for a few words in CC’s status line. Our DRIM system flagged the anomaly in CC's OTEL traces. Grouping requests by query_source showed that over one measured week agent_summary accounted for: 16.4% of total estimated spend (versus 15.7% for the main conversation), and 19.7% of all API requests with approximately 9,000 input tokens per output token. Most requests reuse the prompt cache, but repeatedly reading a large cached transcript still has a cost. Longer contexts and more concurrent agents increase the overhead. We couldn’t find a supported setting that disables only these summaries while preserving background agents and forks. Disabling those capabilities also stops the summaries, but changes the workflow we want to keep. Our workaround is a small Bun preload that intercepts the summary timer without modifying the CC binary. It identifies the timer callback by source-text anchors and leaves other timers alone. In controlled tests on Linux (from ver 

**quantbuilder**: i think its not the status line at the bottom of the terminal, but actually the few words summary claude generates for each background agents in the agents panel. so if we mostly run one plain session we wont pay for this? i do run claude code with disableAgentView on in my settings. does anyone know if that helps to stop the summary calls or just hides the panel?

**helsinki**: I’m sure they release a decision model that alleviates this problem in due time.

**HeavenFox**: If they are literally sending the entire transcript and asking for a summary, wouldn't almost all of the tokens be cache hit, and therefore fairly cheap?

**gym**: I was surprised the usage issue wasn't mentioned here before this based on my searching on hn.algolia. I'm on pro. Two days ago, 100% 5 hour was using 25% of my weekly. Today, 100% 5 hour is like 13% so something was fixed.

**apt-apt-apt-apt**: At least they seem to have fixed their free-revenue feature-bug, where they randomly invalidate your cache (~$8 a pop (turn))

**simianwords**: Isn’t this prompt cached? Then it’s not that big of a deal

**creamyhorror**: Background agents only have 5 minutes' cache TTL, but I'm guessing this doesn't help extend it (not that it would be too useful anyway, especially considering the extra burn). Also, the claim "15-20% of your tokens" seems unclear; of all tokens, or of tokens spent on background agents? Poorly edited AI writing strikes again!

**jakozaur**: I tested it, and it looks real but more nuanced. It is just for subagents; workflows do not seem affected. I guess many new users prefer workflows (ultracode), so the impact is less than the report suggested. Moreover it is mostly cached reads, so subagents with short context cost little, while long-context ones cost much more. In my Claude Code sessions, it looks more like ~8% at most.

**edwinarbus**: I work on Claude Code. You've got the basic mechanism right, but to be super clear, this only applies to background agents that are actively working. They get a summary call about every 30 seconds, and idle background agents don't. These summaries are used for both you and Claude Code to track what each background agent is working on, without reading transcripts. Your 16.4% sounds like it was for a team running mostly background agents, and doesn't seem like a typical session. (Feel free to send me the session ID at edwinarbus@anthropic.com and we can dig further.) Last week, across Claude Code users who send us telemetry, agent_summary was about 2% of cost at API list prices and just under 4% of requests. In the terminal, where nearly all of these calls happen, it was about 6% of cost. That said, we agree that's a lot for a status line. We just rolled out a fix for the most expensive case, summaries that miss the prompt cache (2.1.311+), and right now we're working on a much cheaper mode that sends short notes to a smaller model instead of the full transcript.

**digitaltrees**: It’s almost like they are trying to go public. Burn those tokens.

**_boffin_**: Just looked and we're burning around ~3%, but that's across everything / everyone.

**ab_wahab01**: Does this happen in the VS Code extension? or only in the terminal?

**leroman**: At the base there is a conflict of interests- what we pay for

**rurban**: That's why people are using pi, not Claude. What a waste of money

**hypfer**: With the ever-increasing amount of paper cuts one gets from using their products, I wonder how long this will really go on? After all, for most of the work people seem to be doing daily, Claude kinda isn't.. necessary? In fact, for a lot of tasks, not using it leads to better results in my experience. There are things that only it can reasonably accomplish, but if every interaction with it hurts you in various ways (like this one), then, eventually, I do not see that working out for them anymore. But perhaps this is just a way to push the numbers a bit further up for the IPO? That would make a lot of sense to me.

**dozerly**: This is the harness’s job. Incentives are not aligned for inference providers to own the harnesses.

**franticgecko3**: Claude Code burning a large amount of tokens for no good reason is a headline we've seen more than a few times now. Time to start questioning the motivations of model providers shipping their own harnesses.

**nikolay**: Opus 5.5 burns tokens like there's no tomorrow! Meanwhile, GPT 6.1 Sol on Extra High feels unlimited! Opus (on Max 20x) munches my weekly quota in a day, or two at best. Meanwhile, working with Codex and reviewing with a $50/mo Muse Code Wonder Full seems like it can go own forever (on the same codebase, the same skills, etc.) I am highly disappointed by the overly glorified Opus and Claude Code in general - there's no commit in which Codex or Muse Code or GitHub Pilot don't find critical flaws! I have long sessions of Claude Code having over 100 review cycles of Codex and still not addressing all the valid issues that Codex finds in Claude Code's work! Claude Code keeps injecting British English into prose and identifiers with nothing being able to stop it! Of course, there are almost never resets for Claude Code either - they would rather me focus on Codex being my primary and Claude Code being the reviewer (it works much better than in reverse). Anyway, enver trust a single model! Always review with another frontier one!

