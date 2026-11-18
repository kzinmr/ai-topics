---
title: "External sandboxes for coding agents"
url: "https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/"
fetched_at: 2026-11-18T10:01:22.015235+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# External sandboxes for coding agents

Source: https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/

17th November 2026 - Link Blog
External sandboxes for coding agents
. I've been exploring new ways to sandbox code that is executed by agents, with a focus on making it safer to try out local models without worrying that a mistake or prompt injection attack might cause them to take damaging actions on a machine.
I worked on this project with
Prime Radiant
, the AI research lab behind Superpowers and
other projects
.
My post
on the Prime Radiant blog introduces the
external sandbox
pattern, where code executed by the agent runs inside a dedicated sandbox while the agent itself lives outside of that sandbox.
To demonstrate this pattern we've released three sandbox server implementations:
Each of these implementations offers the same localhost API. You can then configure Pi, Claude Code, or Codex to send API calls to that sandbox any time they want to execute code.
The sandboxes also include an optional HTTP/HTTPS allow-list proxy, so you can control exactly which hosts your agent's code is allowed to communicate with - plus a credential replacement mechanism to make authenticated API calls without sharing a secret with the agent. Here's the UI you can use to reconfigure that proxy while the sandbox is still running:
I continue to be fascinated by the challenge of safely running untrusted code. This external sandbox pattern provides a neat way to experiment with different approaches.
