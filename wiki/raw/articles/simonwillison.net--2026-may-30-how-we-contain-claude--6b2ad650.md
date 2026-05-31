---
title: "How we contain Claude across products"
url: "https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything"
fetched_at: 2026-05-31T07:01:05.298842+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# How we contain Claude across products

Source: https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything

30th May 2026 - Link Blog
How we contain Claude across products
. A complaint I often have about sandboxing products is that they are rarely thoroughly
documented
, and in the absence of detailed documentation it's hard to know how much I can trust them.
Anthropic just published a fantastic overview of how their various sandbox techniques work across
Claude.ai
, Claude Code, and Cowork.
We constrain where and how an agent can act with process sandboxes, VMs, filesystem boundaries, and egress controls. The goal is to set a hard boundary on what an agent can reach. For example, if credentials never enter the sandbox, they can't be exfiltrated, regardless of whether the cause is a user, a model finding a “creative” path, or an attacker.
Claude.ai uses gVisor. Claude Code, run locally, uses Seatbelt on macOS and Bubblewrap on Linux. Claude Cowork runs a full VM (Apple's Virtualization framework on macOS, HCS on Windows).
There's a lot in here, including some interesting stories of risks they missed such as the
api.anthropic.com/v1/files
exfiltration vector
covered here previously
.
This reminded me it's time I took another look at Anthropic's open source
srt (Anthropic Sandbox Runtime)
tool - it's mature enough know that I'm ready to give it a proper go.
