---
title: "Fable's judgement"
url: "https://simonwillison.net/2026/Jul/3/judgement/#atom-everything"
fetched_at: 2026-07-04T07:01:39.513988+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Fable's judgement

Source: https://simonwillison.net/2026/Jul/3/judgement/#atom-everything

One of the most interesting tips I got from
the Fireside Chat
I hosted with Cat Wu and Thariq Shihipar from the Claude Code team at AIE on Wednesday was to let Fable (and to a certain extent Opus) use their own judgement rather than dictating how they should work.
The example they gave was testing. You can tell Fable "only use automated testing for larger features, don't update and run tests for small copy or design changes" - but it's better to just tell Fable to use its own judgement when deciding to write tests instead.
Jesse Vincent just gave me a related tip to help avoid burning too many of those valuable Fable tokens in the few days we have left before the prices go up. Tell Fable to use other models for smaller tasks, applying its own judgement about which model to use.
I prompted Claude Code just now with:
For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent
Claude saved this memory file in
~/.claude/projects/name-of-project/memory/delegate-coding-to-subagents.md
:
---
name: delegate-coding-to-subagents
description: Simon wants coding tasks delegated to subagents running an appropriately lower-power model
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 30068d78-43a9-4fb1-bb29-9799e18c526a
---
Stated by Simon on 2026-07-03: "For all coding tasks use your judgement to
decide an appropriate lower power model and run that in a subagent."
Why:
cost/efficiency — implementation work rarely needs the top-tier
model; judgment, review, and synthesis stay with the main loop.
How to apply:
when a task in this project is primarily writing/editing
code, spawn an Agent with a model override (sonnet for substantive
implementation, haiku for trivial/mechanical edits) and a self-contained
prompt; review the result in the main loop before committing. Design,
auditing, data synthesis, and anything judgment-heavy stays in the main
model. See also [[project-goals]].
So far it seems to be working well. I'm getting a
ton
of work done and my Fable allowance is shrinking less quickly than before.
