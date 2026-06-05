---
title: 'Agent Arena: Causal Evaluation of Agents in the Real World'
source: 'arena-ai'
url: 'https://arena.ai/blog/agent-arena-methodology/'
date: '2026-06-04T15:23:00.000Z'
type: raw_article
tags: [raw, source]
fetched: '2026-06-05'
description: 'Agents are increasingly doing real work. The resulting task distribution has greatly expanded. We desire an agent evaluation that scales along with usage and capability.'
---

# Agent Arena: Causal Evaluation of Agents in the Real World

**Source**: [arena-ai](https://arena.ai/blog/agent-arena-methodology/)  
**Date**: 2026-06-04T15:23:00.000Z  
**Fetched**: 2026-06-05  

> Agents are increasingly doing real work. The resulting task distribution has greatly expanded. We desire an agent evaluation that scales along with usage and capability.

Agents are increasingly doing real work. From chat to terminal to OpenClaw, users everywhere are interacting with complex agents, comprising a model and a harness with many subcomponents and tools. As a result, the task distribution has greatly expanded. This makes evaluating agents progressively more difficult, because both task coverage and task complexity are growing in tandem. We desire an agent evaluation that scales
along with
usage and capability.
Today we are releasing the Agent Arena leaderboard. Arena has always focused on evaluations in the real world. As such, Agent Arena collects and analyzes millions of in-the-wild interactions from people using
Agent Mode
on
arena.ai/agent
doing their jobs — software engineering, financial analysis, and more. From our observations of these agents running on our platform, we derive our first Agent Arena leaderboard, shown below:
Agent Arena Leaderboard
Agent Arena Leaderboard; calculated from an aggregate of all signals; Net improvement is the casual treatment effect; error bars are 95% CIs. Color runs green (top of the board) → red (bottom).
The methodology powering the Agent Arena Leaderboard is different from our previous arenas. Rather than pairwise votes, rankings are calculated using a methodology we call
causal tracing
. Causal tracing treats the agent as a multi-component system, with each component selection representing a possible treatment. We observe individual point-wise traces and measure signals such as task success rates, verbal feedback, tool error recovery, tool hallucinations, and, over time, much more. Then, by randomizing the component selections, we create a multi-intervention randomized controlled trial in which we can aggregate measurements to estimate causal treatment effects. We refer to these effects as "net improvement" in the figure above. The causal framework produces an interpretable ranking that represents the improvement in agent performance due to a component selection. This decouples the contributions of the main orchestrator model, any subagents, image generation models, and the different elements in the harness, letting us combine multiple signals into one coherent leaderboard.
This first leaderboard is the result of our causal evaluation of orchestrator models — the main LLMs that choose which tools to call. Rankings of other aspects of the agentic harness are coming soon. We include more methodological detail in the statistical-methodology section below.
Per-Signal Leaderboards
Every Agent Arena session contains a stream of rich feedback. Users iterate with the agent in natural language, expressing approval, frustration, or clarification turn by turn. They decide whether to download an artifact the agent produced. They click explicit approve / disapprove buttons. They issue in-line corrections when the agent goes off-track. And the agent, on its side, is interacting with an environment that talks back continuously: shell exit codes, tool errors, the absence of a tool it tried to call.
Agent Mode
lets us extract all of these signals — explicit user feedback, implicit user feedback, and feedback from the agent's environment. After we compute per-session outcomes for each signal, we turn them into leaderboards with causal methods and then aggregate them into the headline leaderboard. We present our first 5 signals today, and we plan to measure more in the near future.
Per-Signal Rankings
Each model's score on the canonical sub-signals that compose the aggregate (τ̂). Click a column to sort.
Each individual leaderboard signal. Cells shaded green → red by score within each column. The aggregate of all signals is shown on the left.
The headline leaderboard aggregates the following signals:
Confirmed success
— the user marks a task as a success or failure using the Arena UI. Arena gives users approve and disapprove buttons on every turn; we use the final approval or disapproval of a given task's trajectory to determine the outcome. (There can be more than one task per session.)
Praise vs. complaint
— the user praises or complains about the agent's output. For each task we identify messages expressing explicit verbal praise ("looks great", "this is exactly what I needed") or explicit verbal complaint ("this is broken", "you misunderstood entirely"). The task is marked a success if praise outnumbers complaints.
Steerability
— the agent executes on user corrections. When a user issues an in-line correction ("no, do X instead", "you misread the file"), the agent should attempt to fix it. If the user accepts the fix, we mark the correction successful; if they reject it or give up, unsuccessful. When doing real work, mistakes are inevitable — this signal captures whether these errors are quickly resolved.
Bash recovery
— turns taken to recover from a bash error. When the agent issues a bash command that errors due to a model failure (not an environment issue), the recovery clock starts; we count follow-up bash calls until the next non-erroring command. If the agent gives up, we impose an additional penalty.
Tool hallucination
— the agent references a tool that does not exist. This penalizes invented tool names, malformed syntax that produces a junk name, and chain-of-thought tokens leaking into the tool field. We mark the task a failure if the agent calls a nonexistent tool.
This set of five signals is only a starting point. We plan to add more signals to further enrich these evaluations, retire ones that age out of relevance, and modify them as we improve our trace-mining.
Finally, though not a leaderboard signal, we can also calculate the realized, post-deployment cost of the agents to assess Pareto optimality. We directly calculate the
exact
cost of a session. We find some models more expensive in practice, despite cheaper on-paper pricing. This is as a result of model behavior (e.g. more steps per turn) or induced user behavior (e.g. more turns to reach satisfaction).
Cost vs. Performance
Net Improvement vs. list-price cost per session (7-day window)
Square markers sit on the cost–performance frontier (
——
dotted). Hover any point for its model, provider, and score.
Error bars are 95% CIs on the net improvement (τ̂). Marker color encodes the model provider. Cost is derived from list prices.
Agents in the Real World
Here we present a deep dive into the data that powers the leaderboards. Agent Arena is a live stream of real users asking models to work: write code, debug broken projects, research across the web, create documents, build frontends, analyze files, and iterate over multi-step tasks.
Task Distribution
Primary intent across 160,480 agent tasks (7-day window)
TOP CATEGORIES (≥5%)
Code writing
17.5%
Research / lookup
10.8%
Planning / brainstorm
10.6%
Image / video
10.2%
Document creation
9.1%
Code debugging
8.9%
Chitchat
6.8%
Education / tutoring
5.7%
Creative writing
5.3%
Hover a slice for its share; inner arcs show its sub-intents.
Labeled by an LLM categorizer. Inner arcs split each intent into sub-intents; intents without a sub-breakdown show none.
In a recent 7-day slice, Arena saw 160,480 Agent Mode tasks (note there can be multiple tasks in a session). The largest categories were code writing (17.5%), research and lookup (10.8%), planning and brainstorming (10.6%), and multimodal image/video work (10.2%), followed by document creation (9.1%) and code debugging (8.9%). Code writing alone accounted for roughly 28,000 tasks, with another ~14,000 in code debugging and ~17,000 in research and lookup.
Tool Calls by Volume
Total calls per tool across 2,060,159 tool calls (7-day window)
bash
936,046
write_file
549,893
web_search
275,660
read_file
117,873
fetch_page
85,684
list_files
45,686
ask_user
39,043
generate_image
10,274
Model-agnostic · 160,480 tasks · distinct tool calls per task (ask-user double-count removed) — same basis as tool intensity below.
Tool Calls per Task, by Category
The box and whiskers mark P10 · P25 · P50 · P75 · P90; the diamond ◆ is the mean.
Model-agnostic · 160,480 tasks (7-day window). The mean sits well right of the median for coding and automation: most tasks are modest, but a long tail runs 60+ tool calls (P99 ≈ 200, max 2,000+).
Across 128,244 sessions, 75.6% used at least one tool — 41.1% ran bash and 27.1% ran web search. In the week, Agent Mode issued 2 million structured tool calls, including ~936,000 bash calls, ~550,000 file writes, and ~275,000 web searches.
Lines of Code Written, by Language
Final non-blank lines from successful write_file calls (7-day window); tile area scales with lines written
write_file only (excludes the bash-write proxy); lines de-duplicated to the final version per path.
Tracking via successful
write_file
calls, Agent Mode wrote
40.3 million lines of code
in the last week — roughly 1,000 lines per coding session.
Tool Calls per Agent Session
Tool calls per session, grouped into complexity tiers (7-day window)
17% of sessions make 26+ tool calls and a long tail runs into the hundreds — a large slice of work is high-complexity, multi-step agent runs.
Heaviest Sessions
Work-type mix of 3,467 highest tool-use sessions (7-day window)
TOP CATEGORIES (≥5%)
Coding & repo debugging
53.2%
Artifact & file creation
39.0%
Research & web synthesis
5.0%
Hover a slice for its share; inner arcs break down its tool mix.
High-tool sessions are the top tool-call sessions after loop/runaway filtering. Inner arcs show the tool mix within each work type (share of tool calls).
In the past 7 days, sessions averaged ~16.5 structured tool calls, and high-tool sessions were common enough to form their own cohort: more than 3,400 loop-filtered sessions ran very long tool chains in a single week. Those sessions were mostly real work — 53.2% coding or repo-debugging, 39.0% artifact/file-creation, with the rest spanning web synthesis, terminal workflows, and data analysis.
Session Context Length
Input context on the final turn (7-day window)
32% of sessions reach 128k+ tokens and 8% exceed 1M by their final turn.
Finally, about 32% of recent sessions ended with at least 128k input tokens in the final turn, 22% with at least 256k, and 8% with at least 1M.
What People Build
In a sample of the heaviest real sessions we saw: a live sports-TV schedule site, an autonomous-underwater-vehicle autopilot, a self-hosted movie-watchlist app, a financial-research RAG pipeline, a live study-tracking platform, and more. Many end with the user downloading the finished workspace.
Real Agent Mode Usage Examples
A sample of high-effort Agent Mode sessions (7-day window)
Live sports-TV schedule site
⤓ workspace downloaded
Web app / data aggregation · Italian
Built a web app that aggregates the day's sports broadcasts across several Italian TV and streaming guides, merging duplicate events across sources, plus a password-protected admin page to monitor and repair broken data feeds.
Deliverable —
A deployable web app with a per-source health dashboard and uptime alerts; workspace downloaded.
Claude Opus 4.7 (Thinking)
140 turns
448 tool calls
Self-hosted movie watchlist
Full-stack / DevOps · English
Took a personal movie-tracking idea from a written product spec and a high-fidelity HTML mockup through to a Dockerized, self-hosted web app that imports a year of films from free movie databases, filters by region and language, and exports curated watchlists.
Deliverable —
A product spec, interactive mockup, implementation plan, and a running containerized build.
GPT 5.4 (High)
60 turns
522 tool calls
Underwater-vehicle autopilot
Robotics / control systems · Russian
Debugged and re-architected the control system for an autonomous underwater vehicle in a ROS/Gazebo simulation — fixing rudder and ballast physics, PID depth and pitch control, and adding selectable autopilot modes for different motor and control-surface configurations.
Deliverable —
A reworked physics model and a modular autopilot with depth-aware maneuvering.
Anonymous model
162 turns
494 tool calls
Blender add-on fo

[... truncated at 12000 chars, total 20709 chars ...]
