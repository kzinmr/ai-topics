---
title: "[AINews] The Claude Code Source Leak"
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=192814599&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTI4MTQ1OTksImlhdCI6MTc3NTAyNDY3OCwiZXhwIjoxNzc3NjE2Njc4LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.4usDwRTQ-6M42xmE7B378wZZXtbCwT8WfuDBKnLUBpE"
fetched_at: 2026-04-09T16:28:19.917194+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# [AINews] The Claude Code Source Leak

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=192814599&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTI4MTQ1OTksImlhdCI6MTc3NTAyNDY3OCwiZXhwIjoxNzc3NjE2Njc4LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.4usDwRTQ-6M42xmE7B378wZZXtbCwT8WfuDBKnLUBpE

OpenAI’s
Largest Fundraise in Human History
closed today,
growing by a few billion
, but disclosing some cool numbers like $24B ARR (growing 4x faster than Google/Meta in their heyday), and also had a “soft IPO” with $3B of investment from rich people and inclusion in
ETFs from ARK Invest
, although ChatGPT WAU growth seem to has stalled out - they STILL have not crossed the 1B WAU mark targeted for end 2025. Codex also worryingly has
not announced a new milestone for March
.
By far the biggest news of the day is
the Claude Code source leak
, in itself not particularly damaging for Anthropic, but surely embarrassing and also somewhat educational - Christmas come early for Coding Agent nerds. You can read the many many tweets and posts covering the 500k LOC codebase, and you can
browse multiple hosted forks of the source
.
There are fun curiosities, such as the
full verb list
, or
Capybara/Mythos v8
, or
the /buddy April Fools feature
, or Boris’
confirmed WTF counter
, or creating the cursed “
Claude Codex
”, or the
dozen other unreleased features
, but most serious players are commenting on a few things. Sebastian Raschka probably has
a good list of the top 6
:
Putting Repo state in Context (eg recent commits, git branch info)
Aggressive cache reuse
Custom Grep/Glob/LSP (standard in industry)
Claude code has
less than 20 tools
default on (up to
60+ total
): AgentTool, BashTool, FileReadTool, FileEditTool, FileWriteTool, NotebookEditTool, WebFetchTool, WebSearchTool, TodoWriteTool, TaskStopTool, TaskOutputTool, AskUserQuestionTool, SkillTool, EnterPlanModeTool, ExitPlanModeV2Tool, SendMessageTool, BriefTool, ListMcpResourcesTool, and ReadMcpResourceTool.
File read deduplication/tool result sampling
Structured Session Memory (more on this)
Subagents
Claude Code’s Memory has a
3 layer design
with 1) a MEMORY.md that is just an index to other knowledge, 2) topic files loaded on demand, and 3) full session transcripts that can be searched. There’s also an “autoDream” mode for “sleep” - merging memories, deduping, pruning, removing contradictions.
A
deeper analysis from mem0
finds 8 phases:
And there are 5 kinds of Compaction:
A key feature
of CC
: they use the KV cache to create a fork-join model for their subagents, meaning they contain the full context and don’t have to repeat work. In other words:
Parallelism is basically free
.
here
:
Including
an employee-only gate
and an
employee TUI
, but also a bunch of
other stuff in development
including ULTRAPLAN and
KAIROS
:
And internal
MAGIC DOCS
:
AI News for 3/23/2026-3/24/2026. We checked 12 subreddits,
544 Twitters
and no further Discords.
AINews’ website
lets you search all past issues. As a reminder,
AINews is now a section of Latent Space
. You can
opt in/out
of email frequencies!
Top Story: Claude Code source leak — architecture discoveries, Anthropic’s response, and competitor reactions
Claude Code had substantial source artifacts exposed via shipped source maps / package contents, which triggered rapid public reverse-engineering, mirroring, and derivative ports. The discussion quickly shifted from “embarrassing leak” to “what does this reveal about state-of-the-art agent harness design?” Multiple observers highlighted that the leak exposed orchestration logic rather than model weights, including autonomous modes, memory systems, planning/review flows, and model-specific control logic. Public forks proliferated; one post claimed
32.6k stars and 44.3k forks
on a fork before legal fear led to a Python conversion effort using Codex (
Yuchenj_UW
). Later commentary put the exposed code volume at
500k+ lines
(
Yuchenj_UW
). Anthropic then moved to contain redistribution via
DMCA takedowns
according to several posters (
dbreunig
,
BlancheMinerva
). Separately, a Claude Code team member announced a product feature during the fallout — easier local/web GitHub credential setup via
/web-setup
(
catwu
) — implying normal product operations continued. The leak also created a live security hazard: attackers quickly registered suspicious npm packages such as
color-diff-napi
and
modifiers-napi
to target people trying to compile the leaked code (
Butanium_
).
What is reasonably factual from the tweets:
