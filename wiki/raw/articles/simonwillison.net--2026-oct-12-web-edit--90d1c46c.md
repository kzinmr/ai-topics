---
title: "Release: web-edit 0.1a0"
url: "https://simonwillison.net/2026/Oct/12/web-edit/"
fetched_at: 2026-10-13T10:01:07.983255+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: web-edit 0.1a0

Source: https://simonwillison.net/2026/Oct/12/web-edit/

I was working on a project from my phone using Codex Remote when I found myself wanting to edit a credentials file without round-tripping those credentials through the LLM itself.
So... I had Codex and GPT-6 Astra Extra High build this Python web app which provides a web UI for viewing and editing files in a folder. It's intended to be run over Tailscale, so I can have an agent start this running and then edit files via my Tailscale network directly from my phone.
Here's the interface for browsing files in a folder:
Editing uses
CodeMirror 6
- I was going to use
Monaco
but that still doesn't have a great mobile experience yet.
