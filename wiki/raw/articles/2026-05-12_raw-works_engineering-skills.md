---
title: "Engineering Skills"
source_url: https://raw.works/engineering-skills/
author: Raymond Weitekamp (@raw_works)
published: 2026-05-12
ingested: 2026-10-28
source_type: blog
tags: [raw, blog, agent-skills, skillmd, openprose, dirpack, vercel-skills-sh, mattpocock]
---

# Engineering Skills

**Author:** Raymond Weitekamp ([@raw_works](https://x.com/raw_works)) — RAW Works (raw.works)
**Published:** May 12, 2026
**URL:** https://raw.works/engineering-skills/

Agent skills are a powerful and portable way to transform generally capable AI agents into specifically useful tools — even teammates. There are skills for almost anything you can imagine: doing your taxes, setting up Cloudflare, speaking like a caveman, generating algorithmic art…there's even a skill dedicated to industrial brutalism.

Skills became so easy to make that the next challenge became finding them. This was quickly solved by various "skill registries" like Vercel's skills.sh. OpenClaw was a huge inflection point for the skills boom — it made agent skills first-class in the product architecture and provided a high-permission substrate for millions of people to experiment with.

Of course, then safety became a problem. That's a topic for a longer post, but in case you are curious, I developed the **Skill Safety Data Sheet** as an analogy to material safety data sheets — for evaluating the risks of specific agent skills.

## So where do skills stand today?

If you are an information hoarder like me, your computer is also full of dozens or even hundreds of awesome agent skills — some that 10x devs shared on GitHub, and some that Claude Code made for you after you got tired of saying the same thing over and over and over again.

And if you are like me, your Claude Code and Codex have a terrible habit of finding random skills you don't even remember installing. Worse, they never load the ones you just added — or at least not until you scold them.

There are two details of the skills implementation that make it very unreliable:

- LLMs are nondeterministic. They aren't guaranteed to load the right skill at the right time.
- Progressive disclosure (implemented as a context window workaround) means the agent has to go looking for the information fresh each time. The clanker has to think to find the skill first, which is really inefficient.

In fact, Vercel recently showed that model-mediated skill activation lost to a simple index — a compressed 8KB AGENTS.md hit a 100% pass rate on their Next.js evals while a carefully crafted skill maxed out at 79%, and the skill was never invoked at all in 56% of cases. The winning approach still used a form of progressive disclosure — it just moved the routing layer into stable passive context. (In case you're curious, I made **dirpack** as a general utility for creating indices of a fixed token budget for any directory.)

## Engineer the skills!

So how can we take advantage of the power of agent skills without giving up our own agency to decide when and how they should be used? **Engineer the skills!**

Right now I'm having a lot of fun working on **OpenProse** — a "programming language" that is compiled inside of a coding agent. If this sounds sci-fi, it is…and OpenProse only really works with today's top models.

The fun thing about OpenProse is that you can express very complex workflows in very simple markdown files. As an example, using the legacy v0 syntax purely for brevity:

```
input topic
loop until **editor approves** (max: 5):
    session "research {{topic}}, address editor's prior notes"
    session "draft from research, revise per prior notes"
    session "review draft: approve as report or emit notes"
return report
```

This kind of logical statement is impossible to express in any other language. Prose is super fun!

But the problem I quickly ran into is that many of the prose programs I would want to run assume that my agents will use a specific skill. So I recently added the ability to deterministically declare agent skills inside prose programs — here's the PR.

As a fun example of what's possible with this new feature, I created **auto-pocock**: a headless prose program that incepts your favorite coding agent into running a deterministic sequence of Matt Pocock's engineering skills (grill-with-docs → to-prd → to-issues → tdd → verify → commit), all from one input — a description of the feature you want built.

> Introducing: "Auto-Pocock" An @OpenProseVM program that runs a headless sequence of @mattpocockuk's engineering skills. You input the feature brief, auto-pocock engineers the rest. `npx skills add openprose/prose` `prose run …`
> — Raymond Weitekamp (@raw_works), May 12, 2026

This combination of specific instructions (skills), deterministic processes (the prose contract), and nondeterministic magic (coding agents) is extremely versatile. By engineering skills with OpenProse, you can express complex multi-agent workflows, imbue each agent with detailed discipline, and hopefully get a much-needed break from the keyboard.
