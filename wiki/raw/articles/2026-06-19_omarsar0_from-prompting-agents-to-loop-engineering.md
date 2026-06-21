---
source: "X Article (x.com/i/article/2068004233849290752)"
author: "Elvis Saravia (@omarsar0)"
author_url: "https://x.com/omarsar0"
published: "2026-06-19"
retrieved: "2026-06-21"
title: "From Prompting Agents to Loop Engineering"
url: "https://x.com/i/article/2068004233849290752"
tweet_id: "2068008743153832264"
plain_text_source: true
engagement:
  likes: 911
  retweets: 125
  bookmarks: 2174
  impressions: 242484
  replies: 41
  quotes: 25
mentions:
  - steipete (Peter Steinberger)
  - bcherny (Boris Cherny)
  - addyosmani (Addy Osmani)
  - mvanhorn (Matt Van Horn)
tags: [loop-engineering, coding-agents, agent-loop, claude-code, prompting, agentic-engineering, harness-engineering, orchestration]
---

# From Prompting Agents to Loop Engineering

A claim has been circulating in AI coding circles: stop prompting your coding agents and start designing loops that prompt them for you. As with everything new, this stuff gets repeated often and explained rarely. This is the practical version: what an agent loop is, why it matters, and what one looks like in production.

Below you can read some of my thoughts (written with the help of Claude) from some of the conversations I've been having with some of our students, technical founders, AI engineers, and startups.

## Where the claim comes from

"You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — Peter Steinberger (@steipete), Jun 7 2026. 2.2M views.

Boris Cherny, the creator of Claude Code, makes the same point from the other side: "I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and figuring out what to do. My job is to write loops." — Boris Cherny (@bcherny).

The point is not that prompt engineering is dead. With loop engineering, the work moves up a level, from writing the code to writing the system that writes the code. Developers furthest along this path report months where they shipped hundreds of PRs without opening an IDE, with every line written by the agent.

## What a loop actually is

A loop is a small program you write that does four things:
- prompts the coding agent for you,
- reads what it produced,
- decides whether it is done,
- and if not, prompts it again with the error or the next step.

You stop sitting inside the loop typing prompts; you write the loop, and the model becomes a subroutine it calls.

The shape is always the same: set a goal, act, check, feed the error back, and repeat until the check passes or the loop stops itself.

## "Loop" means at least five things

Much of the disagreement is people using one word for five different ideas. Here is the progression, oldest to newest.

1. **ReAct (2022)**. The original research pattern: reason, act, observe, repeat.
2. **AutoGPT (2023)**. A self-prompting goal loop, notorious for not knowing when to stop.
3. **ralph loop**. A deliberate context reset between iterations so the agent does not drown in its own history.
4. **/loop and /goal**. Cadence and completion conditions are built into the agent, carrying the state across turns.
5. **orchestration**. One author fans out many agents that read your GitHub, Slack, and chat, and decide what to build next.

## The parts you actually assemble

The progression explains what people mean by loop; this is what a loop is built from. The same six parts show up every time, and most now ship inside the coding tools instead of custom scripting you maintain yourself.

1. **A trigger**. Something that starts the loop without you pressing go: a schedule, a webhook, a file change, a label landing on a PR. This is what separates a real loop from a single run you repeat by hand.
2. **Isolation**. A private checkout per agent, usually a git worktree, so two agents running at once cannot overwrite each other's files. Once you run more than one, this stops being optional.
3. **Written-down context**. The conventions, build steps, and project-specific rules are kept where the agent reads them on every run. Skip it, and the loop re-derives your project from scratch each pass and guesses at the gaps.
4. **Reach into your tools**. Connectors to the issue tracker, CI, database, and chat, so the loop can open the PR, link the ticket, and post the result instead of printing a fix and waiting for you to carry it the rest of the way.
5. **A second agent checks**. A separate worker who grades the output is held apart from the one who produced it, because a model reviewing its own work passes almost everything.
6. **State on disk**. A markdown file, a board, or a queue: anything outside the conversation that records what is finished and what is next. The model forgets between runs; the file does not.

Assemble those six, and you have a good starting point for loop engineering. You used to hand-build everything; now most ship as built-in features, which is why the pattern has moved from a fringe technique into common use.

## A concrete loop, the PR babysitter

- **Trigger**. Every 15 minutes.
- **Scope**. Open PRs labeled agent-watch.
- **Action**. If CI is red for a deterministic reason, attempt one fix. If the main moved, rebase once.
- **Budget**. One fix attempt per PR, five minutes, ten files changed.
- **Stop condition**. CI green, or budget exhausted, then stop and ping a human.

You return to merged PRs instead of a backlog of broken builds. The same shape covers most ops work:
- **CI health**. Every 30 minutes, pull failing runs and cluster them by signature, so ten red PRs with one root cause become one thing to look at.
- **Deploy verification**. After a push, hit your endpoints, confirm 200s and the expected content, and flag regressions before users do.
- **Feedback clustering**. Every 30 minutes, pull comments from your channels, group them into themes, and map each cluster to the file or doc that owns it.

## A concrete Claude Code loop with /goal

The babysitter is a loop you wire up yourself; it also helps to see one that ships inside the agent. In Claude Code, the smallest complete loop is /goal: you hand it a verifiable end state, and it keeps taking turns until that state is true.

At this point, it's clear that a strong /goal reads less like a prompt and more like a contract. The good ones specify four things: the end state you want, the evidence that proves you reached it, the constraints the agent must not break getting there, and the budget of work it is allowed to spend. Leave any one of them vague, and the model fills the gap with the easiest reading: it stops early, takes a shortcut, or redefines success so the transcript looks done while the real system is broken.

1. **Set the condition**. Type /goal plus a checkable end state, for example, `/goal tests in test/auth pass`. The first turn starts immediately.
2. **The agent works a turn**. It edits, runs the tests, and surfaces the results in the session.
3. **An evaluator checks**. A fast model reads the transcript and decides whether it is met or not met, so the agent is not grading its own work.
4. **Loop or finish**. Not met means another turn with guidance; met means the goal clears itself and the run stops.

State carries across turns, so it does not quit early or drop a constraint partway through. A few controls keep it reliable:
- Make the check measurable. A test result, an exit code, a file count, or an empty queue. `npm test exits 0` is a goal; "make it better" is not.
- Bound the run. Append something like "or stop after 20 turns" so a stuck loop halts instead of burning turns.
- Pair it with auto mode so that turns run unattended, and use `/goal clear` to abandon it early.

The evaluator step hides a useful subtlety: the checker does not have to be the same model as the coder. Once the loop has distinct roles (planner, executor, evaluator, vision reviewer), each can run on a different model, and choosing which model fills which role becomes an architecture decision rather than a single bet on one "best" coding agent. Some models plan better, some execute more cheaply, some judge a screenshot more accurately, and a good orchestrator lets you swap them per role instead of waiting for one vendor to win every category.

## Running many loops unattended

A single /goal loop is one agent working toward one finish line. Running many unattended processes raises the stakes, because a loop is only as trustworthy as its ability to check its own work. Cherny's setup for running Opus autonomously for hours comes down to five steps:

1. Auto-approve permissions so the agent does not stop to ask on every tool call.
2. Use dynamic workflows (drop Ultracode into the prompt) to fan out across many agents instead of one serial thread.
3. Use /goal or /loop to keep it going. /goal sets a completion condition, /loop re-prompts on a schedule, and both carry state, so it does not quit early.
4. Run it in the cloud (desktop or mobile app) so the session survives when you close the laptop.
5. Give it a way to self-verify end-to-end. Claude in Chrome for web, a simulator MCP for mobile, and a live server for backend. This is the step that makes the other four safe.

The full sequence:
```
claude --permission-mode auto                          # 1 · no approval prompts
ultracode  orchestrate sub-agents to ship the feature  # 2 · fan out
/goal all tests pass and the demo loads clean          # 3 · keep going
→ cloud / desktop app                                  # 4 · close the laptop
→ chrome ext · sim MCP · live server                   # 5 · self-verify, then halt
```

## crabfleet: orchestration as a product

Orchestration is easier to picture with a concrete tool. Peter Steinberger's crabfleet, an OpenClaw project billed as "mission control for agent runs," is a loop packaged as a product, and its shape maps onto everything above.

- Work as cards on a board. Tasks are entered as cards built from a prompt, a GitHub issue, or a PR, then move through todo, running, human review, and done. That board is the loop's queue and its stop-and-report step, made visible.
- Durable runs, not fire-and-forget. Each run is a tracked attempt with heartbeats, so it keeps going when you look away and survives a closed laptop. You take over only when the runtime advertises that it supports handoff.
- Agents that spawn agents. A run can start child sessions, send messages, read transcripts, and update its own summary from inside a sandbox: on-disk memory and fan-out in one place, one author and many agents.
- It runs on disposable cloud sandboxes with browser-based terminals, which is what makes walking away from an unattended run safe. The point is not the specific tool but that the loop has hardened into infrastructure: a queue, durable execution, fan-out, and a human-review gate are now things you configure rather than hand-script every time.

## Where the cost goes now

For two years, the cost question in AI coding was simple: which model, and how many tokens. Inside a loop, that instinct points at the wrong layer. The spend is no longer a single call but how many times the loop goes around, so a loop that retries six times before it converges costs six times as much as one that lands on the first pass, on the same model.

That changes what is worth optimizing:
- **Iterations are the budget line, not tokens.** A cheaper model that loops twice as often is not cheaper, so track cost per finished task, not cost per call.
- **A weak verifier is the most expensive bug you can ship.** If the check that decides "done" is loose, the loop either stops early on broken work or grinds on work that was already fine, and both waste whole iterations. Tighten this before anything else.
- **Failing fast is a cost control.** A loop with no cap on consecutive failures does not eventually succeed; it eventually drains the account, so the stop condition protects the bill as much as the codebase.

You used to tune the prompt; now you tune the loop, because that is where the cost accumulates.

## When not to loop

Loops pay off when a task repeats, and a machine can tell when it is done. Outside that, a loop only automates churn. Skip it in these cases:
- **One-shot edits.** If you can finish it in a single pass, a loop is pure overhead.
- **Unscoped or exploratory work.** "Figure out why users are churning" has no pass condition, so the loop never converges.
- **Anything without a cheap automated check.** If the only verifier is your own eyes, you are still inside the loop. Build the check first, or do the task by hand.

## What can go wrong

A loop that runs while you sleep also makes mistakes while you sleep, and the failure modes are predictable.

- **The verification burden stays human.** The loop writes faster than you can review, so if you stop reading the diffs, you have not removed the work, only deferred it.
- **Comprehension gaps widen.** Shipping code you did not write, faster than you can absorb it, erodes the model of your own system, and that debt comes due during the next incident.
- **Silent drift on a loose check.** A weak verifier lets wrong-but-passing work through on every iteration, so the loop looks productive while it digs a hole.

None of this is an argument against loops; it is why the engineer who designs the loop matters more, not less.

## How to build your own

1. **Pick one repeatable task.** Babysitting PRs, fixing CI, verifying deploys: start with routine work.
2. **Scope it tight.** "Fix the billing webhook validation, only touch app/api/billing and lib/billing," beats "fix the bug." A loose loop wanders.
3. **Give it a budget and a stop condition.** Max attempts, max runtime, max files, max spend, max consecutive failures. A loop running unattended is also a loop making mistakes unattended.
4. **Add an independent verifier.** A separate sub-agent grades the work, because the agent who wrote the code is the worst judge of whether it is done.
5. **Run it on a cadence.** /loop for an interval, cron for a schedule, hooks at lifecycle points, or GitHub Actions so it survives a closed laptop.
6. **Keep memory on disk.** The model forgets between runs, so state lives in markdown or a board, not in the context window.

**The takeaway: the loop, not the model, is now the expensive and failure-prone part. Build it like someone who intends to stay the engineer responsible for the output, not just the person who starts the run.**

## Other Useful References

- Addy Osmani (@addyosmani), on AI-assisted coding loops
- Matt Van Horn (@mvanhorn), "WTF Is a Loop?"
- Peter Steinberger (@steipete), on designing loops
- Boris Cherny (@bcherny), on running agents autonomously
