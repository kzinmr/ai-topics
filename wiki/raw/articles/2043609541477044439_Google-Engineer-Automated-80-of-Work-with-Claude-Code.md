---
title: "Google engineer automated 80% of his work with Claude Code. here's the exact system he built."
source: X/Twitter Native Article
author: @noisyb0y1
tweet_id: 2043609541477044439
tweet_url: https://x.com/noisyb0y1/status/2043609541477044439
article_url: http://x.com/i/article/2043574857867120640
date: 2026-04-27
---

# Google engineer automated 80% of his work with Claude Code. here's the exact system he built.

> @noisyb0y1 — [X Article](https://x.com/noisyb0y1/status/2043609541477044439)

Google engineer with 11 years of experience automated 80% of his work using Claude Code and a simple dotnet app. 

Now he works 2-3 hours a day instead of 8 and chills the rest of the time while the system runs itself making $28,000 in passive income.
Here's what he knows that you don't.
Part 1 - CLAUDE.md by Karpathy's rules
Andrej Karpathy - one of the most influential AI researchers in the world - documented the most common mistakes LLMs make when writing code: over-engineering, ignoring existing patterns, adding dependencies nobody asked for.
 
Someone took these observations and turned them into a single CLAUDE.md file. 

The result - 15,000 stars on GitHub in a week, you could say 15k people changed their lives
The idea is simple: if mistakes are predictable — they can be prevented with the right instructions. One markdown file in the repo gives Claude Code a structured set of behavioral rules for the entire project.
Four principles inside:
 
No frameworks. No complex tooling. One file that changes Claude's behavior at the project level.
Real difference:
 
Command that auto-generates your own CLAUDE.md:
 
Replaces: Claude that over-engineers simple tasks, adds dependencies nobody asked for and touches files it shouldn't.
Part 2 - Everything Claude Code: a full engineering team in one repo
github.com/affaan-m/everything-claude-code ( 153,000+ stars )
This isn't just a prompt collection. It's a complete AI operating system for building products.
 
 
 
 
Works on Claude, Codex, Cursor, OpenCode, Gemini - one system everywhere.
How to install:
 
Or manually - copy the components you need into your project's .claude/. Don't load everything at once - 27 agents and 64 skills in context simultaneously will burn your limits faster than you can type your first prompt. Take only what you actually need.
Real difference:
 
Replaces: weeks of setting up your own agent system, separate tools for planning/review/security, $200-500/month on specialized AI services.
Part 3 - The hidden scandal: Claude Code v2.1.100 is silently stealing your tokens
Someone set up an HTTP proxy to intercept full API requests across 4 different Claude Code versions. 

Here's what they found:
 
v2.1.100 sends FEWER bytes but charges 20,000 MORE tokens. The inflation is entirely server-side - you can't see it and can't verify it through /context.
 
Why this matters beyond billing:
 
Fix takes 30 seconds:
 
Temporary solution until Anthropic officially fixes the issue. But the difference in sessions is noticeable immediately.
Replaces: guessing why Claude suddenly stopped following your instructions.
Case study: what full automation looks like
An engineer with 11 years of experience built a three-part system:
 
Result after a week:
 
This isn't magic. It's CLAUDE.md + the right agents + a 15-minute cycle.
Full checklist
 
What you get after reading this
 
> If your time is worth $30/hr - that's $3,000-3,600/month you're just not seeing right now. 
> If $100/hr - that's $10,000-12,000/month going nowhere while you manually write code Claude could write itself.
Most developers will never reach this level - not because they can't, but because they think it's complicated. In reality between you and full automation there are three commands and one file.
The engineer I described at the beginning isn't a genius or a senior from Google. He just spent one evening on the right setup and now his system does the work while he lives his life.
You can do the same thing tonight. While others argue about whether AI will replace developers - those who already set up the system just collect their pay and chill.
The choice is obvious.
You build your own life - so choose the right path. 
/ If this was useful - follow /
