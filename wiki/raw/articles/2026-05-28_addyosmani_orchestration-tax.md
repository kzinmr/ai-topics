---
type: x_article
author: Addy Osmani
author_handle: addyosmani
tweet_id: "2059844244907696186"
article_url: https://x.com/i/article/2059839454370828288
date: 2026-05-28
date_ingested: 2026-05-29
title: "The Orchestration Tax"
source: x
tags:
  - ai-agents
  - agent-orchestration
  - cognitive-load
  - productivity
  - software-engineering
  - concurrent-systems
  - amdahls-law
public_metrics:
  likes: 732
  bookmarks: 1312
  retweets: 88
  replies: 30
  quotes: 28
  impressions: 106107
references:
  - https://addyosmani.com/blog/cognitive-surrender/
  - https://addyosmani.com/blog/cognitive-parallel-agents/
  - https://margaretstorey.com/blog/2026/02/09/cognitive-debt/
  - https://www.youtube.com/watch?v=VTYx7Ex-0bA (Google I/O panel)
  - https://en.wikipedia.org/wiki/Amdahl%27s_law
---

# The Orchestration Tax

Starting more AI agents is easy now. However, more agents running doesn't mean there's more of you available - your cognitive bandwidth doesn't parallelize. All the judgement to actually steer them and merge the changes they make still has to route through exactly one serial processor which is just you. Orchestration tax is basically the price you pay for forgetting this and the only real fix is to start architecting your own attention like you architect any concurrent system.

I was on a panel at Google I/O with Richard Seroter, Aja Hammerly and Ciera Jaspan talking about what software engineering looks like right now and how it will probably evolve. Near the end Richard asked us what is one thing developers should walk away and do differently. I said the thing I been circling around for months: feeling busy is definitely not the same as being productive. You can run 20 agents and feel completely busy. But thats not 20 agents worth of shipped work.

Earlier in that chat Richard gave this problem a name. "You talked about the orchestration tax" he said. "You can't manage twenty agents successfully in your own brain." He is totally right. I want to breakdown this idea properly because its not a discipline problem. It is an architecture problem.

The line from the panel I keep thinking about is something I said almost randomly: running multiple agents does not mean there is more of you.

## The asymmetry people don't price in

There is this hidden asymmetry in agentic workflows. Starting an agent is very cheap. It is just a keystroke or a sentence prompt. But closing the loop on the agent is not cheap at all. Someone has to check if what came back is correct and reconcile it with whatever the other agents touched. That someone is you. And there is exactly one of you.

I wrote about a piece of this last month in [Your parallel Agent limit](https://addyosmani.com/blog/cognitive-parallel-agents/), mostly about the ambient anxiety of not knowing which parallel thread is quietly failing. This post is about the shape underneath that cost. When you start seeing agent development as a concurrent system, you realize the human is just a component inside it. The slow serial component.

## You are the single thread resource

If you ever wrote concurrent code you already have the right intuition. You just been pointing it at the wrong part of the system.

Python has the Global Interpreter Lock (GIL). You can spawn as many threads as you want but only one executes python bytecode at a time because they must acquire the lock. You are the GIL of your AI agents. They all can run at once. But when any of their work needs genuine understanding of the architecture or resolving merge conflicts, that work has to acquire the lock. There is one lock. You hold it.

Amdahl's Law makes this very precise. The speedup you get from parallelizing is capped by the fraction of work that stays serial. If a big chunk of your pipeline can't be parallelized, you top out at a hard limit no matter how many cores you throw at it. In agent development the serial fraction is the judgement. Spawning 8 agents doesn't speed up your judgement time. It just makes the queue of things feeding into it much deeper.

This is an old performance engineering fact that still surprise people: optimizing the non bottleneck part doesn't increase throughput. You just grow the pile of unfinished work sitting in front of the bottleneck. Adding agents optimize the part that was never the constraint. The constraint is the review step and the throughput of your system equals exactly the throughput of that step. The orchestration tax is the structural gap between agent production and what you can actually merge. It's what happens when you put a single-threaded resource in charge of a concurrent one.

## Grinding won't fix structural limits

At the panel I said I never felt more productive with my tools but I am also more tired than I ever been. Both halves are completely real and they have the same cause.

The tiredness has a very specific cause. It is how running a serial processor at 100% with no slack feels like. Every time you check on an agent you been away from you pay a context switch cost. You flush your brain and reload a different context from cold. CPUs do this in microseconds and architects still work hard to avoid it. You do it in minutes and you never reload the context perfectly. Five agents is not 1x workload done five times. It is 5 cold reloads plus a background brain process constantly worrying about which agent you should be checking.

You can't just try harder to fix a structural limit. The tax will be paid anyway. If you try to grind it out, the limit just shows up as shallow code reviews or experiencing [cognitive surrender](https://addyosmani.com/blog/cognitive-surrender/) where you just accept the agent's code because forming your own opinion costs attention you don't have anymore. You either pay the tax deliberately or you let it quietly destroy your understanding of your own system.

## Architect your attention

So you have to treat your attention as the scarce serial resource it is. You wouldn't design a distributed system without thinking hard about the bottleneck. Give your brain the same respect.

Some things that actually held up for me:

**Scale fleet to review rate, not the UI.** A good concurrent system uses backpressure so the queue doesn't grow infinitely. The producer slows down to match the consumer. Your agent count is the producer and your review rate is the consumer. The right number of parallel agents is how many you can actually code review properly. For most of us this is a low single digit. The AI tool will happily let you spawn 20 but that is just a UI feature.

**Sort the work.** I mentioned this to Richard when he asked how I navigate it. I keep two piles of tasks. One is isolated work that I'm happy to delegate to background agents running in the Cloud. These can run async and often just need me at the final gate. The other pile is complex tasks where the judgement is the work. Like a weird bug or architecture design. The big mistake is trying to parallelize the second pile. Doing multiple complex tasks doesn't scale your output. It just thrashes the lock and everything comes out worse.

**Batch your reviews.** Context switching cost you heavily every time you do it. Reviewing 4 agents at the same time in one sitting is much cheaper than checking one, leaving to do something else and returning cold. Give agents a long leash. Let the work pile up a bit and process the batch.

**Only spend the lock on judgement.** Don't waste your brain on things the machine can verify itself. Make the agent write a passing test or generate a screenshot. They can prove the boring 80% themselves so you only spend your scarce attention on the 20% that genuinely needs a human.

**Protect your serial time.** The bottleneck needs your best hours, not the leftover minutes between agent check-ins. Sometimes the highest leverage move is to stop orchestrating entirely, close the laptop full of agents and just think hard about one single problem with the lock held the whole time. Orchestrating is not the real work. Its the overhead around the work.

Aja pointed out that architecture is the urgent skill now. Knowing what belongs inside one agent and what is too much for it. I would add that you are a component in that system. Your attention has a known, low serial throughput. The system either respects that number or it routes around it by secretly lowering your standards.

## Busy vs Productive

This is really important because the failure mode is invisible to you. Twenty running agents gives you this feeling of massive productivity. The dashboard is full and everything moves. But that feeling is decoupled from actually shipping good code to main. You can be maximally busy and barely produce anything. From the inside it feels identical.

Ciera pointed out Margaret-Anne Storey's work on debt. We talked about technical debt and [cognitive debt](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/). The orchestration tax left unpaid is how you accumulate both at once. You merge stuff you didn't read well. Your mental model of the codebase goes completely stale. None of this shows up on the dashboard today. It shows up when production breaks and you look at the system and realize you have no idea how it works anymore.

So this is the actual takeaway. Spawning agents is not the skill. Anyone can run 20.

The real skill is designing the system around the one serial resource that cannot be cloned or parallelized. That resource is your attention.

Architect it the way you architect anything else you depend on in production.
