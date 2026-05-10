---
title: "Expanding our long-running agents research preview · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/long-running-agents"
scraped: "2026-05-10T01:19:41.615504+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Expanding our long-running agents research preview · Cursor

**Source**: [https://cursor.com/blog/long-running-agents](https://cursor.com/blog/long-running-agents)

Blog
/
product
Feb 12, 2026
·
product
Expanding our long-running agents research preview
5 min read
Table of Contents
↑
Making models more capable
Findings to date
Using long-running agents at Cursor
Toward self-driving codebases
Cursor's long-running agents research preview is now available at
cursor.com/agents
for all Ultra, Teams, and Enterprise users.
The long-running agent is the result of our research on agents working autonomously on more ambitious projects, including the work we shared last month on
how Cursor built a web browser
.
During that experiment, we saw frontier models fail in predictable ways on long-horizon tasks. We addressed these limitations by creating a custom harness that enables agents to take on more difficult work and see it through to completion.
We released a version of this harness last week as part of a
research preview
. The results show that
long-running agents produced substantially larger PRs with merge rates comparable to other agents.
Talking with participants in our research preview, we heard that long-running agents successfully completed a range of tasks that were previously out of reach for agents. A few example runs from the research preview include:
Building an all-new chat platform integrated with an existing open-source tool (runtime: 36 hours)
Implementing a mobile app based on an existing web app (runtime: 30 hours)
Refactoring an authentication and RBAC system (runtime: 25 hours)
#
Making models more capable
Successfully completing difficult tasks requires frontier intelligence and the right harness. By working with every frontier model and building a custom harness for each, we are in a unique position to build the best scaffolding that leverages the strengths of different models. We found that there are a couple general principles that help us achieve better performance.
Planning before execution
When iterating directly with a model, tight prompt-response loops let you monitor the agent and nudge it back on course when needed. When the agent goes off and works on a larger task autonomously, a slightly wrong assumption can turn into a completely incorrect solution by the end.
Long-running agents in Cursor propose a plan and wait for approval instead of immediately jumping into execution, recognizing that upfront alignment reduces the need for follow-ups.
Following through on tasks
Frontier models can write great code, but often forget the big picture of their task, lose track of what they're doing, or stop at partial completion.
Long-running agents use a plan and multiple different agents checking each other's work in order to follow through on larger, more complex tasks.
#
Findings to date
Initial participants in the research preview used long-running agents to implement large features, refactor complex systems, fix challenging bugs, overhaul performance, and create high-coverage tests.
I shipped two architecture overhauls. It's an incredible tool for "I don't know if this is possible but I'm curious to see" type work. I can run five in parallel, for everything from creating Mac window managers to stuffing CEF into Tauri.
Theo Browne
CEO
,
T3 Chat
Agents commonly ran for more than a day, producing PRs that merged with minimal follow-up work. Users could step away, focus on other work, close their laptop, and come back to working solutions.
I planned for this project to take an entire quarter to accomplish. With Cursor long-running agents, that timeline compressed to just a couple days. And I could do two or three additional projects. I can kick-off a 52-hour task that I don't have to babysit and come back to a big PR with 151k lines of code.
Zack Jackson
Infra Architect
,
Rspack
Compared to synchronous agents, long-running agents were more thorough in their approach and wrote code that was more production-ready.
The magical part of the new harness is allowing the same model to make something production-ready. I tested the same bug-fix prompt locally vs. with a long-running agent, both with Codex 5.3. The local agent fixed it fairly quickly, but the long-running one went further to find edge cases, fix similar occurrences, and create high-coverage tests.
Tejas Haveri
CTO
,
DevAccel-Labs
#
Using long-running agents at Cursor
For the last month, we've been testing the limits of long-running agents internally. We’ve used them for experiments to see how far we could push them, as well as for production work on Cursor itself. Here are a few tasks we gave long-running agents that we have since merged.
Video renderer optimization
We asked an agent to optimize a video renderer whose performance was bottlenecking deployment. It completed a full migration to Rust and implemented custom kernels, reproducing identical visual output by working purely from the original logic.
Policy-driven network access for sandboxed code
We needed JSON-driven network policy controls and a local HTTP proxy for sandboxed processes. The proxy needed to be correct across protocols, enforce policy consistently, and fail safely without allowing blocked traffic. The long-running agent created a ten-thousand line PR that had very few issues when we ran a large test suite against it. Follow-up work consisted mainly of changes we didn't specify in our initial request.
Sudo support in Cursor CLI
Some tasks break CLI agents the moment they hit sudo, especially tasks related to system administration or ops. We asked a long-running agent to implement secure sudo password prompting, which required stitching together multiple subsystems and reasoning about Unix auth flows. It produced a working implementation that Cursor CLI now uses.
#
Toward self-driving codebases
Long-running agents in Cursor are an early milestone on the path
toward self-driving codebases
, where agents can handle more work with less human intervention. It's now possible to delegate larger tasks and come back hours or days later to working solutions.
We are working on improving collaboration across long-running agents so they can break up bigger projects into parallel work streams and take on even more ambitious projects with less human intervention.
We’re also working to develop new tools to handle the volume of code now being generated. As the cost of code generation continues to fall, we'll need new approaches to deploying that code to production safely.
Try long-running agents today at
cursor.com/agents
.
Filed under:
product
Author
:
Cursor Team
