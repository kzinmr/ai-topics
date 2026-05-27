---
title: "Codex App-Server Runtime (optional) — Hermes Agent"
source_url: "https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime"
source_type: "official-documentation"
author: "Nous Research"
publication: "Hermes Agent Docs"
date: "2026-05-27"
tags: ["hermes-agent", "codex", "openai", "protocol", "runtime"]
---

# Codex App-Server Runtime — Hermes Agent

Hermes can optionally delegate `openai/*` and `openai-codex/*` turns to the Codex CLI app-server instead of its own tool loop.

## Overview
- Opt-in only — default behavior unchanged unless you flip the flag
- All terminal commands, file edits, sandboxing, MCP tool calls execute inside Codex's runtime
- Hermes becomes the shell: sessions DB, slash commands, gateway, memory & skill review

## Why
- Use ChatGPT subscription (no API key)
- Codex's own toolset & sandbox: shell, apply_patch, update_plan, view_image
- Native Codex plugins (Linear, GitHub, Gmail, Calendar, Canva, …) auto-migrated
- Hermes' richer tools (web_search, browser, vision, image generation, skills, TTS) via MCP callback
- Memory & skill nudges still work

## Three Tool Sources

### 1. Codex built-in tools (always on)
shell, apply_patch, update_plan, view_image, web_search

### 2. Native Codex plugins (auto-migrated)
Linear, GitHub, Gmail, Google Calendar, Outlook, Canva, and any other installed plugin

### 3. Hermes tool callback (MCP server)
Hermes registers itself as MCP server in ~/.codex/config.toml. Available: web_search/web_extract (Firecrawl), browser automation (Camofox/Browserbase), vision_analyze, image_generate, skill_view/skills_list, text_to_speech

## What's NOT available
delegate_task, memory, session_search, todo (use Codex's update_plan)

## Workflow Features
- /goal (Ralph loop): Works. Goal judge runs via auxiliary client.
- Kanban: Works. Workers inherit Codex runtime.
- Cron jobs: Not specifically tested but use same run_conversation path.

## Switch Back
Use /codex-runtime auto to switch back to default runtime for delegate_task/memory/session_search.
