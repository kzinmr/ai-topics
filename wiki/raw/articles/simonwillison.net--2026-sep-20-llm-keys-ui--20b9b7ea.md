---
title: "Release: llm-keys-ui 0.1"
url: "https://simonwillison.net/2026/Sep/20/llm-keys-ui/"
fetched_at: 2026-09-21T10:02:06.103222+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm-keys-ui 0.1

Source: https://simonwillison.net/2026/Sep/20/llm-keys-ui/

This plugin solves a very specific problem.
I've started using
Codex Remote
to run coding agents on various machines while controlling them from my phone.
Sometimes I use those machines to hack on LLM projects, and occasionally that means I need to configure an API key.
I don't like pasting API keys into agent sessions, so I wanted a way to get those keys onto a machine without pasting them into the ChatGPT app directly.
With this plugin, I can tell Codex to run:
uvx --with llm-keys-ui llm keys-ui --all
Then have it tell me the URL - including local network or Tailscale device IPs - for an interface to save additional API keys.
Then later it can use a command like
llm keys get anthropic
as part of a shell command when it needs to use a key.
