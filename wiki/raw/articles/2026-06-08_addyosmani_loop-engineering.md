---
title: "Loop Engineering"
author: Addy Osmani (@addyosmani)
published: 2026-06-08
source_url: "https://x.com/i/article/2064127981161959567"
type: x-article
captured: 2026-06-08
tags:
  - agentic-loop
  - agent-loop
  - coding-agents
  - agent-harness
  - agentic-engineering
  - subagents
  - workflow
  - verification
---

# Loop Engineering

**Author:** Addy Osmani (@addyosmani)
**Published:** 2026-06-08
**Source:** https://x.com/i/article/2064127981161959567

## Definition

Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead. A loop can be thought of as a recursive goal where you define a purpose and the AI iterates until complete.

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — @steipete

> "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops." — @bcherny

## Context: From Prompting to Loops

For two years, the way you got something out of a coding agent was you wrote a good prompt and shared enough context. You type a thing, you read what came back, you type the next thing. The agent is a tool and you are holding it the entire time.

Now you build a small system that finds the work, hands it out, checks it, writes down what is done and then decides the next thing, and you let that system poke the agents instead of you.

Loop engineering sits one floor above the [[concepts/agent-harness|agent harness]]. The harness but it runs on a timer, it spawns little helpers, and it feeds itself.

## The Five Building Blocks + Memory

A loop needs five things and one place to remember stuff. Both Codex and Claude Code have all five.

### 1. Automations (the heartbeat)

Automations are what make a loop an actual loop and not just one run you did once.

**Codex:** Automations tab — pick project, prompt, frequency, local or background worktree. Runs that find something go to Triage inbox; runs that find nothing archive themselves. Used internally for daily issue triage, CI failure summarization, commit briefings, bug hunting.

**Claude Code:** `/loop` re-runs on a cadence. `/goal` keeps going until a condition is true (a separate small model checks completion). Scheduling via cron. Hooks fire shell commands at agent lifecycle points. GitHub Actions for background runs after laptop closure.

### 2. Worktrees (parallel without chaos)

Two agents writing the same file is the exact same headache as two engineers committing to the same lines. A git worktree fixes it — separate working directory on its own branch sharing the same repo history.

**Codex:** Built-in worktree support for concurrent threads.

**Claude Code:** `--worktree` flag, `isolation: worktree` setting for subagents. Each helper gets a fresh checkout that cleans itself up.

> "The worktrees take away the mechanical collision but YOU are still the ceiling, your review bandwidth decides how many you can actually run, not the tool." — Osmani

### 3. Skills (stop explaining your project every time)

A skill is how you stop re-explaining the same project context every session. Both tools use the same format: a folder with a SKILL.md holding instructions and metadata, plus optional scripts, references, assets.

> "Without skills the loop re-derives your whole project from zero every cycle. With skills it compounds." — Osmani

Skills are also where **intent debt** stops costing you over and over. An agent starts every session cold and fills any hole in your intent with a confident guess. A skill is that intent written down — the conventions, the build steps, the "we don't do it like this because of that one incident."

**Key distinction:** The skill is the authoring format; a plugin is how you ship it.

### 4. Plugins and Connectors (the loop touches your real tools)

A loop that can only see the filesystem is a tiny loop. Connectors (built on MCP) let the agent read your issue tracker, query a database, hit a staging API, drop a message in Slack.

This is the difference between an agent that says "here is the fix" and a loop that opens the PR, links the Linear ticket and pings the channel once CI is green by itself.

### 5. Sub-agents (maker away from checker)

The most useful structural thing in a loop: splitting the one who writes from the one who checks. The model that wrote the code is way too nice grading its own homework.

**Codex:** Spawns subagents on request. Define agents as TOML files in `.codex/agents/` with name, description, instructions, optional model and reasoning effort.

**Claude Code:** Subagents in `.claude/agents/` and agent teams. The usual split: one agent explores, one implements, one verifies against the spec.

> "A verifier you actually trust is the only reason you can walk away." — Osmani

### 6. Memory (the spine)

A markdown file, or a Linear board — anything that lives outside the single conversation and holds what's done and what is next. The model forgets everything between runs so the memory has to be on disk and not in the context. The agent forgets, the repo doesn't.

## One Concrete Loop

An automation runs every morning on the repo. Its prompt calls a triage skill that reads yesterday's CI failures, the open issues, the recent commits, and writes the findings into a markdown file or a Linear board. For each finding that is worth doing, the thread opens an isolated worktree and sends a sub-agent to draft the fix, and a second sub-agent reviews that draft against the project skills and the existing tests. Connectors let the loop open the PR and update the ticket. Anything the loop can not handle lands in the triage inbox. The state file remembers what got tried, what passed, what is still open.

> "You designed it one time. You did not prompt any of those steps." — Osmani

## What the Loop Does NOT Do

Three problems get sharper as the loop gets better, not easier:

1. **Verification is still on you.** A loop running unattended is also a loop making mistakes unattended. "Done" is a claim, not a proof.

2. **Comprehension debt.** The faster the loop ships code you did not write, the bigger the gap between what exists and what you actually get.

3. **Cognitive surrender.** When the loop runs itself it's very tempting to stop having an opinion and just take whatever it gives back. "Designing the loop is the cure when you do it with judgment and the accelerant when you do it to avoid thinking."

> "Two people can build the exact same loop and get completely opposite results. One uses it to move faster on work they understand deeply. The other uses it to avoid understanding the work at all. The loop doesn't know the difference. You do."

## References

- https://addyosmani.com/blog/agent-harness-engineering/
- https://addyosmani.com/blog/agent-skills/
- https://addyosmani.com/blog/intent-debt/
- https://addyosmani.com/blog/comprehension-debt/
- https://addyosmani.com/blog/cognitive-surrender/
- https://addyosmani.com/blog/orchestration-tax/
- https://addyosmani.com/blog/code-agent-orchestra/
- https://addyosmani.com/blog/adversarial-code-review/
- https://addyosmani.com/blog/long-running-agents/
- https://addyosmani.com/blog/factory-model/
- https://addyosmani.com/blog/code-review-ai/
