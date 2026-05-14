---
title: "How to make your agent learn and ship while you sleep"
created: 2026-01-28
date_ingested: 2026-05-14
type: x_article
x_article_tweet_id: "2016520542723924279"
x_article_author: "Ryan Carson"
x_article_author_handle: "@ryancarson"
source: "https://x.com/ryancarson/status/2016520542723924279"
tags: [x-article]
---

Most developers use AI agents reactively - you prompt, it responds, you move on. 
But what if your agent kept working after you closed your laptop? 
What if it reviewed the day's work, extracted lessons, updated its own instructions, and then picked up the next feature from your backlog?
That's what I've built: a nightly loop where my agent learns from every thread, compounds that knowledge into persistent memory, and then ships the next priority item - all while I sleep.
Here's how to set it up.
This setup builds on three open-source projects:
Compound Engineering Plugin by @kieranklaassen  - The original compound engineering skill for Claude Code. Install it to give your agent the ability to extract and persist learnings from each session.
Compound Product - The automation layer that turns prioritized reports into shipped PRs. Includes the auto-compound.sh script, execution loop, and PRD-to-tasks pipeline.
Ralph - An autonomous agent loop that can run continuously, picking up tasks and executing them until complete.
Using Claude Code? This guide uses Amp, but the same workflow works with Claude Code. Replace `amp execute` with `claude -p "..." --dangerously-skip-permissions`, and update AGENTS.md references to CLAUDE.md.
The Two-Part Loop
The system runs two jobs in sequence every night:
10:30 PM - Compound Review 
Reviews all threads from the last 24 hours, extracts learnings, and updates AGENTS.md files.
11:00 PM - Auto-Compound 
Pulls latest (with fresh learnings), picks #1 priority from reports, implements it, and creates a PR.
The order matters. The review job updates your AGENTS.md files with patterns and gotchas discovered during the day. The implementation job then benefits from those learnings when it picks up new work.
Step 1: The Compound Review Script
This script tells your AI agent to review all threads from the past 24 hours and compound any learnings it missed:
 
Make it executable:
 
What This Does
The agent will:
Find all your threads from the last 24 hours
Check if each thread ended with a "compound" step (extracting learnings)
For threads that didn't, retroactively extract the learnings
Update the relevant AGENTS.md files with patterns, gotchas, and context
Commit and push to main
Your AGENTS.md files become a living knowledge base that grows every night.
Step 2: The Auto-Compound Script
This is the implementation engine. It reads from your prioritized reports, picks the top item, creates a PRD, breaks it into tasks, and executes them:
 
The loop.sh script runs your agent iteratively—one task at a time—until all tasks pass or it hits the iteration limit.
Step 3: Set Up launchd (macOS)
Cron works, but launchd is native to macOS and handles edge cases better. Create these plist files:
Compound Review (10:30 PM)
 
Auto-Compound (11:00 PM)
 
Load them:
 
Verify:
 
Step 4: Keep Your Mac Awake
launchd won't wake a sleeping Mac. Use caffeinate to keep it awake during your automation window:
 
This keeps your Mac awake from 5 PM to 2 AM - plenty of time for your nightly jobs to complete.
The Compound Effect
Here's what happens every night:
10:30 PM - Agent reviews the day's threads, finds missed learnings, updates AGENTS.md files, pushes to main
11:00 PM - Agent pulls main (now with fresh context), picks the top priority, implements it, opens a PR
When you wake up, you have:
Updated AGENTS.md files with patterns your agent learned
A draft PR implementing your next priority
Logs showing exactly what happened
The agent gets smarter every day because it's reading its own updated instructions before each implementation run. Patterns discovered on Monday inform Tuesday's work. Gotchas hit on Wednesday are avoided on Thursday.
Debugging
Check if jobs are scheduled:
 
View logs:
 
Test manually:
 
Going Further
Some ideas to extend this:
Slack notifications when PRs are created or jobs fail
Multiple priority tracks - run different reports on different nights
Automatic PR merge if CI passes and changes are small
Weekly summary - have the agent write a changelog of everything it shipped
The goal is a self-improving loop: every unit of work makes future work easier. Your AGENTS.md files become institutional memory. Your agent becomes an expert in your codebase.
Stop prompting. Start compounding.
