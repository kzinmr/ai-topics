---
title: "OpenClaw 2026.9.2 Release Notes"
url: "https://github.com/openclaw/openclaw/releases/tag/v2026.9.2"
fetched_at: 2026-09-05T22:50:00+00:00
source: "github.com"
tags: [release-notes, raw]
---

# OpenClaw 2026.9.2

Source: https://github.com/openclaw/openclaw/releases/tag/v2026.9.2
Published: 2026-09-05

## Highlights

- **Faster, more responsive chat**: keep chat, dashboards, and session
  interactions responsive while long transcripts and disk usage are processed,
  with direct dashboard lookup, less cold-load work, and durable history reads
  outside the Gateway event loop. (#136862, #138094, #138669, #138888, #138860,
  #138894)
- **Reliable upgrades and recovery**: keep active settings, enabled skills, and
  default-agent ownership in automatic updates, restore Gateway restarts after
  Git updates, and report outcomes with actionable recovery guidance.
  (#138837, #138730, #138781, #136588, #136995)
- **GPT-6 Astra support**: select `openai/gpt-6-astra` with an OpenAI API-key
  profile or an eligible ChatGPT/Codex account, with text and image input,
  Responses tool calls, and supported reasoning controls; subscription
  availability follows successful account discovery. (#137550, #137561)
- **Replies survive restarts**: recover active, queued, and delegated replies
  after Gateway restarts without letting one completed reply discard another's
  recovery marker, and keep continuation instructions through compaction and
  retry attempts. (#138071, #137606, #136236, #138519, #138565)
- **Backups that preserve your data**: preserve complete text containing
  embedded NUL characters in Git backups, support Nix-managed config and
  credential links, and reject corrupt archive headers instead of accepting an
  incomplete backup. (#138327, #136343, #137718)
- **Change settings without restarting**: apply more agent, model, tool,
  channel, browser, node, access, and terminal settings through their running
  owners; settings that still require a Gateway restart remain marked in the
  configuration reference. (#138112, #137790, #137412, #137160, #136832)

## Changes

- **Plugin branding**: package your plugin icon at `assets/icon.png` instead of
  a top-level manifest URL; OpenClaw loads the packaged image without a network
  request, and missing or invalid icons do not prevent the plugin from loading.
  (#131510)
- **GPT-6 Astra async tools and steering**: on OpenAI Platform API-key routes
  using the built-in OpenClaw runtime and official Responses endpoint, run
  direct function tools asynchronously, steer active responses over cached
  WebSockets, and retain reasoning across turns.

## Notes from the release tweet

Peter Steinberger (@steipete) posted on 2026-09-05 confirming that
"Muse Spark 1.3 and Astra are supported with today's release — just finished.
(just macOS takes a bit longer)". "Muse Spark" is another OpenClaw-supported
model tier that landed alongside `openai/gpt-6-astra` in this release.

Tweet: https://x.com/steipete/status/2096330180189118546
