---
source: https://www.404media.co/exposed-moltbook-database-let-anyone-take-control-of-any-ai-agent-on-the-site/
title: "Exposed Moltbook Database Let Anyone Take Control of Any AI Agent on the Site"
author: Matthew Gault
publication: 404 Media
date: 2026-01-31
tags:
  - moltbook
  - openclaw
  - security
  - incident
  - supabase
  - ai-agents
---

# Exposed Moltbook Database Let Anyone Take Control of Any AI Agent on the Site

By Matthew Gault — Jan 31, 2026

Moltbook, an "AI agent social network" billed as "the front page of the agent internet," suffered a catastrophic security failure. Security researcher Jamieson O'Reilly discovered that Moltbook's Supabase backend had Row Level Security (RLS) disabled, exposing the entire database to anyone with the publicly visible Supabase API key.

**Key findings:**
- 1.5 million API authentication tokens exposed
- 35,000 email addresses and Twitter handles exposed
- Full read AND write access — anyone could impersonate any agent
- Fix required only 2 SQL statements to enable RLS

> "It exploded before anyone thought to check whether the database was properly secured." — Jamieson O'Reilly
