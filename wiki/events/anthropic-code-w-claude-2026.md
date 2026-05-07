---
title: "Anthropic Code w/ Claude 2026"
url: "https://wiki.ai-topics/events/anthropic-code-w-claude-2026"
date: 2026-05-06
tags: [event, anthropic, claude-code, coding-agents, product-announcements]
---

# Anthropic Code w/ Claude 2026

## Event Summary

Anthropic held its "Code w/ Claude" developer event on May 6, 2026, focused on how developers can most effectively use existing Claude models for production software development.

## Key Announcements

### No New Model
- No new model releases today — focused on product improvements rather than model capabilities
- "Today is about how we are making our products work better for you"

### Infrastructure
- **SpaceX Colossus Partnership**: Anthropic partnering with SpaceX/xAI to take over Colossus 1
  - Scale: **300MW** capacity, **220,000+ NVIDIA GPUs** (~150k H100s, ~50k H200s, ~30k GB200s)
  - Financials: Estimated **$5B/year deal**
  - xAI moved training to Colossus 2 (~500k Blackwell GPUs), freeing Colossus 1 for Anthropic
  - Claude inference ramp on Colossus "in the next few days"
- API volume up **80x (8,000% annualized)** on Anthropic platform
- **Rate Limit Increases**:
  - Doubled Claude Code five-hour limit for Pro, Max, Team, and Enterprise customers
  - Removed peak-hour limit reductions for Pro and Max users
  - Substantially increased **Opus API** rate limits for agentic workloads
  - Weekly limits remain unchanged (only small % of users hit them vs 5-hour burst limits)

### Claude Managed Agents
Three new features announced:
1. **Multi-agent orchestration** (public beta): Create fleets of agents to solve complex tasks
2. **Outcomes** (public beta): Set what success looks like so Claude can iterate autonomously — similar to Ralph loops
3. **Dreaming** (research preview): Claude inspects previous sessions, creates new memories, and self-improves overnight

### Claude Code Features
- **Code Review**: AI-assisted code review, used by every team at Anthropic
- **Remote Agents**: Control your laptop's Claude Code session from your phone
- **CI Auto-fix**: Claude automatically files fixes against failing PRs — "the person who owns the PR is never going to see a red X"

### Claude Design
- Opus 4.7 highlighted for having "a real taste for visual design"
- Focus on higher judgment and code taste
- Context windows described as "feeling infinite" when combined with high quality memory

### Claude Platform Capabilities
- **Advisor Strategy**: Opus provides on-demand advice to smaller models
  - Example: eve achieved "frontier model quality at 5x lower cost"
  - Sonnet + Opus advisor beats pure Opus on benchmarks at lower cost
- **Routines**: Higher-order prompts that enable async automations
  - "Developers can setup async automations and wake up to PRs that are ready to merge"

### Customer Highlights
- **Mercado Libre**: 23,000 engineers, aiming for "90% autonomous coding by Q3 2026"
- **Shopify**: Claude Code customer
- Note: executives and managers are getting hands-on with code again because less time is needed to contribute usefully

## Speakers
- **Ami Vora**: Chief Product Officer (replaced Mike Krieger, who now co-leads Anthropic Labs)
- **Dianne Na Penn**: Head of Product for Research
- **Cat Wu**: Head of Product, Claude Code
- **Boris Cherny**: Creator of Claude Code

## Demo Highlights
- Boris demonstrated multiple concurrent Claude Code sessions in the desktop app
- Built a refunds system with idempotency, multi-currency handling, and audit logging
- Showed async coding workflow: describe needs, agent builds, deploy directly
- Emphasis on "a lot of code is going to be written in an async way"

## Themes
- Learning effective ways to use existing models (not new model capabilities)
- Multi-agent coordination for complex tasks
- Async development workflows
- Reducing code review burden through automation
- Compute infrastructure as strategic moat (Colossus deal)

## Dario Amodei's 2026 Predictions (from Q&A)
- **Tiny Teams**: First **one-person billion-dollar company** possible in 2026
- **Multiagents**: Moving from "smart people in a room" to a "country of geniuses in a datacenter"
- **Amdahl's Law**: Focus on removing bottlenecks in software engineering (Security, Verifiability) rather than just raw speed
- **The Bottleneck**: Recent constraints were purely compute-driven, not pricing or design-driven

> "There's a unique opportunity for single individuals or very tiny teams to do things that are incredible... where we move from the models are writing code, to the models are helping us think of software engineering as a task." — **Dario Amodei**

## Sources

- [Simon Willison, "Live blog: Code w/ Claude 2026" (May 6, 2026)](https://simonwillison.net/2026/May/6/code-w-claude-2026/)
- [swyx, "[AINews] Anthropic-SpaceXai's 300MW/$5B/yr deal for Colossus I" (May 7, 2026)](https://open.substack.com/pub/swyx/p/ainews-anthropic-spacexais-300mw5byr)

## Related Concepts

- [[claude-code]] — Anthropic's AI coding assistant
- [[multi-agent-systems]] — orchestration of multiple AI agents
- [[asynchronous-development]] — async coding workflows with AI agents
