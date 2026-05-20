---
title: "How AI is Changing Software Engineering at Shopify — Farhan Thawar on The Pragmatic Engineer"
created: 2026-05-20
author: Gergely Orosz (@GergelyOrosz)
guest: Farhan Thawar (@fnthawar)
source: YouTube (The Pragmatic Engineer)
url: https://www.youtube.com/watch?v=u-3IILWQPRM
type: podcast
duration: "47:03"
published: 2025-07-02
tags: [claude-code, ai-coding, ai-agents, mcp, shopify, agentic-engineering, coding-agents, ai-adoption, podcast, cursor, github-copilot, llm-proxy, vibe-coding, developer-experience, internship]
---

# How AI is Changing Software Engineering at Shopify

Podcast episode from The Pragmatic Engineer, recorded live at LDX3 in London. Gergely Orosz interviews Farhan Thawar, Head of Engineering at Shopify, about how the company went all-in on AI.

## Episode Overview

Shopify was the first company outside of GitHub to deploy GitHub Copilot (2021, a year before ChatGPT). They've since expanded to Cursor, Claude Code, and are experimenting with Devin and Gumloop. The company has no cost limit on AI token spending and expects engineers to use AI tools.

## Key Topics Covered

### Early AI Tool Adoption (00:00-12:00)
- Shopify was first outside GitHub to use Copilot (2021), negotiated via direct email to GitHub's CEO
- Got 2 years free in exchange for feedback
- Deployed Cursor ~1 year ago; interestingly, Cursor growth is happening OUTSIDE engineering — finance, sales, support teams are vibe-coding MCP servers
- Non-engineers building MCP servers for Salesforce, Google Calendar, Gmail, Slack without engineer help
- Shifted from "one tool" philosophy to embracing multiple AI tools

### Working with AI Labs (06:22)
- Farhan pairs directly with engineers at Anthropic, OpenAI
- Spent 1 hour pairing with an Anthropic applied AI engineer on Claude Code to learn how they use it internally
- Records sessions and shares internally as case studies
- Philosophy: "hire smart people and pair with them on problems" (not "hire smart people and get out of their way")

### Code Red for Tech Debt (08:50)
- Shopify ran a 7-month "Code Red" (Nov 2024 - May 2025) to eliminate tech debt
- 30-50% of engineering focused on reducing exceptions, segfaults, unique exception counts
- Tracked via 28-day rolling averages across 4 reliability surfaces
- Core contributors to Ruby and MySQL (2nd largest MySQL fleet outside Meta)

### LLM Proxy Architecture (19:50)
- Built internal LLM proxy for centralized model access
- Routes all AI requests through one gateway (Claude Code, Copilot, Cursor all go through it)
- Provides: privacy protection, token tracking, cost analytics, model routing
- Tobi Lütke's AI memo: internal document setting AI expectations

### MCP Integration (23:00)
- Using MCP servers to connect Claude Code to Shopify APIs
- Non-engineering teams building their own MCP servers
- Shopify released open-source MCP server for their platform

### No Token Spending Limits (26:59)
- Zero cost limits on AI token usage per engineer/team
- Celebrate engineers who spend more (investigating what they're doing)
- Push engineers to use expensive models (O1 Pro, O3 Pro, Claude Max) not defaults
- CTO Mikey: "If you don't pay personally for O1 Pro or Gemini Ultra, you are crazy"

### 1,000 Interns Program (32:50)
- Shopify hiring 1,000 interns (vs 25/term last year) — ~350 per term, ~10% of engineering
- Hypothesis: interns are "AI reflexive" — grew up with LLMs, change internal culture
- Interns are "the secret weapon" — company learns more from them than they learn from the company
- Internship may become the only entry-level path into Shopify engineering

### Engineering Culture & Tools (36:20)
- Built own project management tool "GSD" (Get Stuff Done) instead of Jira/Linear
- Philosophy: "first you make the tool, then the tool makes you"
- AI now auto-generates weekly project updates from PRs + Slack conversations
- Engineering managers get dashboards: focus time, meeting load, AI adoption rates

### Coding Interviews for Directors+ (40:31)
- Added coding interviews for ALL engineering director and VP hires
- Candidates pair-program with Farhan; AI tools allowed (and encouraged)
- "If they don't use a co-pilot, they usually get creamed by someone who does"
- Tests ability to discern good AI-generated code from bad

### What Changed with AI (43:40)
- Best engineers using AI for infrastructure work they always wanted to do but "never had time"
- Tech debt reduction, refactoring, readability improvements
- Engineers unleashing agents in parallel, reviewing PRs like they have a team
- Not afraid to try things that may fail — unleash for 24 hours, delete if garbage

### Advice for AI Adoption (44:40)
- #1: Role modeling — leaders must code and share their AI workflows
- Internal prompt library where engineers share prompts that worked
- Hackathons focused on AI (senior people embracing Claude Code)
- "No one has it figured out. No one's there yet."

## Key Quotes

> "We're not a swim lane company — we don't try to put people into roles where you only think about product or only think about engineering. We're curious problem solvers."

> "Hire smart people and pair with them on problems" (not "hire smart people and get out of their way")

> "Interns are the secret weapon. You always learn more from the interns."

> "I want you to come to work with an LLM and a brain, not one or the other."

> "If they don't have a co-pilot, they will lose [the coding interview]."

> "You should not be penny pinching on AI tools because the productivity gains are there."

> "The engineer's job shifts from writing code to reviewing and merging agent outputs — orchestrating intelligent systems."

## Related Pragmatic Engineer Deep Dives
- How Shopify built its Live Globe for Black Friday
- Vibe coding as a software engineer
- Inside Shopify's leveling split
- Real-world engineering challenges: building Cursor
- How Anthropic built Artifacts
