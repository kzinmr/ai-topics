---
title: "WTF Is a Loop? Peter Steinberger vs. Boris Cherny"
author: Matt Van Horn (@mvanhorn)
published: 2026-06-08
source_url: "https://x.com/i/article/2063850827694096385"
type: x-article
captured: 2026-06-08
tags:
  - agentic-loop
  - agent-loop
  - coding-agents
  - cost-optimization
  - multi-agent
  - orchestration
---

# WTF Is a Loop? Peter Steinberger vs. Boris Cherny

**Author:** Matt Van Horn (@mvanhorn)
**Published:** 2026-06-08
**Source:** https://x.com/i/article/2063850827694096385

The most repeated sentence in AI coding this week is six words long, and almost nobody saying it can define it.

## The Tweet That Started It

Peter Steinberger posted on June 7, 2026, clearing 2.2 million views:

> "Here's your monthly reminder that you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — @steipete, June 7, 2026

The most telling reply was Matthew Berman's: "nobody knows but him and boris."

## Boris Cherny's Definition (WorkOS Acquired Unplugged, June 2, 2026)

Boris Cherny created Claude Code as a side project in September 2024. It now sits behind ~4% of all public commits on GitHub.

> "Now it's actually leveled up, I think, again, to the next wave of abstraction where I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and figuring out what to do. My job is to write loops." — Boris Cherny, WorkOS Acquired Unplugged, June 2, 2026

**Plain version:** A loop is a small program you write that prompts the coding agent for you, reads what it produced, decides whether it is done, and if not, prompts it again. You stop being the thing inside the loop typing prompts. You become the author of the loop. The model becomes a subroutine.

## Boris's Three Stages

1. **Stage 1 (a year ago):** Write code by hand with autocomplete
2. **Stage 2:** Run 5-10 Claude sessions in parallel, prompt each one
3. **Stage 3 (now):** Don't prompt at all. Write loops that prompt Claude. 200 agents read GitHub/Slack/Twitter and decide what to build next.

> "In the last 30 days, 100% of my contributions to Claude Code were written by Claude Code. I landed 259 PRs." — Boris Cherny, via Simon Willison, December 27, 2025

He deleted his IDE in November 2025 and hasn't opened it since.

## The 5-Stage Loop Spectrum

### Stage 1: Academic While-Loop (2022)
The ReAct paper formalized it: model reasons, calls a tool, reads result, repeats. One model, one loop, human watching.

### Stage 2: AutoGPT (2023)
Gave it a goal and let it prompt itself. Famous for spinning forever doing nothing. Seeded "agents are a toy" narrative.

### Stage 3: Ralph Loop (July 2025)
Geoffrey Huntley's bash one-liner that pipes the same prompt file into the agent over and over. Innovation: every iteration resets context to fixed anchor files instead of letting conversation grow. Huntley built an entire programming language with it for ~$297.

### Stage 4: /goal Command (Spring 2026)
Both Codex and Claude Code shipped `/goal` — runs the ralph loop until a small validator model confirms the task is done.

### Stage 5: Orchestration Loops (Now)
Four things changed:
1. The loop became the unit of work, not the task
2. Loops started supervising other loops, concurrently and on a schedule
3. Scheduling replaced the human kickoff (runs on infrastructure time, not your attention)
4. Durability became explicit — git-backed state and crash recovery

Ralph assumed your terminal stayed open. The 2026 version assumes it does not.

## "It's Just a Cron Job with a Hat On"

> "Cronjobs have funny re-branding rn." — X reply, loops discourse, June 2026

**The honest answer:** Yes, the scheduling layer is cron. Boris literally runs his on cron. But cron never had the decision-maker in the middle. A cron job runs a fixed script. A loop runs a model that looks at the current state, decides what to do next, does it, checks whether it worked, and decides whether to keep going.

Stack those, let one loop dispatch and supervise others, give them durable shared state, and you have something cron cannot express.

## Boris's Five Tips for Running Opus Autonomously

1. Use **auto mode** for permissions so Claude doesn't ask for approval
2. Use **dynamic workflows** to orchestrate hundreds or thousands of agents
3. Use **/goal or /loop** to keep going until done
4. Use **Claude Code in the cloud** so you can close your laptop
5. Make sure Claude has a way to **self-verify its work end to end**

Tip 5 is the one hype skips and practitioners obsess over.

## The Plot Twist: The Loop Is Now the Expensive Part

> "Every ai agent i shipped this year is a for-loop, an llm call, and a try/catch around the json parsing. The only thing agentic about it is the anthropic bill at the end of the month." — @rohit_jsfreaky, June 2026

**Cost evidence:** Uber capped engineers at $1,500/person/month for Claude Code and Cursor after burning its annual AI budget in four months.

> "The costliest thing in AI coding is no longer writing code, it's managing the agent loop." — @runes_leo, June 2026

### Three Hard Stops Every Production Loop Needs
1. Maximum iteration count
2. No-progress detection
3. Token or dollar budget ceiling

## It's Not Loops. It's Skills.

Steinberger's other recurring point: if you do something more than once, turn it into an automated skill. A loop with no reusable skills inside it is just a while-true around a stranger. A loop that calls a library of sharp, tested, named skills is a system that compounds.

## Key Patterns Summary

1. A loop is cron plus a decision-maker in the body
2. The lineage is real: ReAct (2022) → AutoGPT (2023) → ralph (2025) → /goal (spring 2026) → orchestration loops (now)
3. The loop is only as good as its feedback
4. The expensive resource shifted from tokens to loop management
5. The reusable unit inside the loop is a skill, not a prompt

## Research Sources

- Reddit: 17 voices (r/ClaudeAI, r/AI_Agents, r/ExperiencedDevs), 47 threads, 34k upvotes
- X: 21 voices (steipete, bcherny, runes_leo), 56 posts, 175 reposts
- YouTube: 4 voices (WorkOS, Lenny's Podcast, Y Combinator)
- Hacker News: 12 voices, 54 stories, 1k comments
- GitHub: 6 repos (gastownhall/gastown, NousResearch/hermes)

## References

- https://arxiv.org/abs/2210.03629 (ReAct paper)
- https://ghuntley.com/ralph/ (Ralph loop)
- https://github.com/gastownhall/gastown (Gas Town)
- https://simonwillison.net/2025/Dec/27/boris-cherny/
- https://www.youtube.com/watch?v=RkQQ7WEor7w (Boris at WorkOS Acquired Unplugged)
