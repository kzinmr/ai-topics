---
entity: "ian-nuttall"
type: entity
aliases: [iannuttall]
url: "https://ian.is/"
blog: "https://ian.is"
twitter: "@iannuttall"
github: "https://github.com/iannuttall"
role: "Indie hacker, developer-tools builder, AI-coding advocate"
updated: 2026-04-10
tags:
  - person
  - indie-hacker
  - developer-tools
  - AI-assisted-development
  - programmatic-seo
  - MCP
  - Claude-Code
sources: []
---


# Ian Nuttall

**URL:** https://ian.is
**Blog:** ian.is
**Twitter/X:** @iannuttall
**GitHub:** https://github.com/iannuttall
**Projects:** Playbooks.com, Create Pages, Typemat, Practical Programmatic, Claude-Agents, MCP-Boilerplate
**Location:** Nottingham, United Kingdom

## Overview

Ian Nuttall is a serial indie hacker and developer-tools builder based in Nottingham, UK. He describes himself as a "serial internet biz builder with multiple 6 & 7 figure exits" who "makes software with AI and talks about it." His work sits at the intersection of programmatic SEO, indie business building, and AI-assisted development tooling.

Nuttall gained prominence in the indie-hacker community for building and acquiring programmatic SEO tools, most notably acquiring Typemat (a free pSEO page generator) and creating Create Pages (a platform for automated content creation). His website ian.is serves as his personal brand hub, while Practical Programmatic (practicalprogrammatic.com) is his content platform where he shares detailed tutorials and strategies for programmatic SEO — a technique he has used to drive millions of monthly pageviews to his properties.

In 2025–2026, Nuttall emerged as a significant voice in the AI coding tools space. His GitHub repositories for Claude Code — including `claude-agents` (2,041+ stars), `claude-sessions` (1,178+ stars), and `mcp-boilerplate` (1,016+ stars) — have become go-to resources for developers adopting AI-powered coding workflows. His practical, no-nonsense approach to AI-assisted development focuses on shipping features, avoiding context drift, and building profitable tools.

His philosophy is captured in his Twitter bio: "TLDR; I make software with AI and talk about it. Serial internet biz builder with multiple 6 & 7 figure exits. Always learning."

## Timeline

| Date | Event |
|------|-------|
| 2014 | Created GitHub account (@iannuttall) |
| ~2018 | Began building programmatic SEO sites using PHP and CSV files |
| 2020 | Launched Practical Programmatic blog and courses |
| 2021 | Published the viral "How I Built a $20,000/mo Programmatic SEO Business" tweet (370K+ views, 3,500+ bookmarks) |
| 2022 | Built Niche Site Metrics — a directory of profitable niche site ideas |
| 2023 | Created IndexMeNow, a Google Indexing API tool; built $30K MRR membership site using WordPress |
| 2023 | Published $7M portfolio acquisition strategy using aged domains and cold email |
| Jan 2024 | Acquired Typemat.com, a free programmatic SEO page builder |
| 2024 | Published comprehensive "Best Programmatic SEO Tools" guide based on real-world usage |
| 2025 | Shifted focus to AI development tools; began publishing Claude Code tips and techniques |
| Jun 2025 | Released `claude-sessions` — slash commands for Claude Code session tracking (1,178+ stars) |
| Jul 2025 | Released `claude-agents` — custom subagents for Claude Code (2,041+ stars) |
| Aug 2025 | Published viral thread on "Best practices to stop Claude Code being 'dumb'" |
| Sep 2025 | Published guide on custom Cursor modes at playbooks.com/modes |
| Oct 2025 | Launched Playbooks.com — a curated directory of agent skills and MCP servers |
| Feb 2026 | Released `mcp-boilerplate` — Cloudflare MCP server template with auth and Stripe (1,016+ stars) |
| Feb 2026 | Released `ralph` — minimal file-based agent loop for autonomous coding (851+ stars) |
| Feb 2026 | Released `dotagents` — centralized location for hooks, commands, skills, and AGENT/CLAUDE.md files |
| 2026 | Published comprehensive Claude Code workflow guide at 10xdevelopers.dev |
| 2026 | Active contributor to RSSNext/Folo, Raycast extensions, and Subscribe Openly |

## Core Ideas

### Programmatic SEO as a Business Moat

Nuttall's core business philosophy centers on programmatic SEO — creating large volumes of data-driven, template-generated pages to capture long-tail search traffic. He has driven over 1 million monthly pageviews to his products using this approach.

His key insight: **"If you have a product with a lot of data, using that is perfect for pSEO because it means your content and data together is a moat against the competition."** This isn't just about generating pages — it's about combining proprietary data with SEO strategy to create defensible assets that competitors can't easily replicate.

He also emphasizes topical authority: **"Programmatic SEO also lets you cover topics more thoroughly to increase 'topical authority' (basically how Google thinks you are to the keyword topic)."** By creating hundreds or thousands of related pages targeting long-tail variations, you build domain-level relevance that compounds over time.

### Go Slower with AI Agents

One of Nuttall's most counterintuitive tips for AI-assisted coding is to **"GO SLOWER!"** In his widely-circulated Claude Code tips guide, he argues:

> "For deep work, slow down. Understanding your code is 100x better. You'll lose track of your context and codebase. Don't rush by launching 6 agents and 20+ subagents."

This philosophy extends to his `claude-sessions` project, which implements structured session tracking and logging so developers can preserve context across multiple AI coding sessions. Rather than letting the agent spiral into confusion, Nuttall advocates for disciplined, methodical workflows.

### The AI Loop of Death and How to Escape It

Nuttall coined the term "AI loop of death" to describe when an AI coding agent spirals, breaks things, and can't fix itself. His solution: a 4-rule task management system that prevents context degradation:

1. **Plan first** — use Claude Desktop in open-ended conversation to discuss MVP features, tech stack, and packages before coding
2. **Use structured session logs** — document every session so context can be restored after `/clear`
3. **Clear early** — use `/clear` as soon as you hit a good stopping point, rather than letting context degrade
4. **Subagents sparingly** — use them for understanding and planning, then save and clear before continuing

His `ralph` project implements a minimal file-based agent loop that avoids these problems by design — using the filesystem as persistent state rather than relying solely on the LLM's context window.

### Build in Public, Share the Playbook

Nuttall is a prolific sharer of knowledge. His tweet threads on programmatic SEO routinely garner hundreds of thousands of views and thousands of bookmarks. He believes in giving away the playbook:

> "My programmatic SEO portfolio gets 80+ million impressions and 1+ million clicks a month — on autopilot. So... here's everything I know about programmatic SEO in 2025."

This generosity is strategic — it builds audience, authority, and a flywheel of engagement that feeds his businesses. His "alternatives" content strategy (building comparison pages for competing pSEO tools) is itself a demonstration of the programmatic SEO techniques he teaches.

### MCP Servers Are the New Micro-SaaS

In early 2025, Nuttall began championing MCP (Model Context Protocol) servers as a new category of micro-SaaS products. His viral post "10 MCP BIZ IDEAS TO MAKE $10K+ MRR" argued that everyone was covering *how* to build MCP servers but not *what* to build. His `mcp-boilerplate` project provides a complete Cloudflare-based template with user authentication and Stripe integration for paid tools — effectively lowering the barrier to entry for anyone wanting to monetize MCP servers.

He also released `dotagents` as a centralized location for all hooks, commands, skills, and AGENT/CLAUDE.md files — recognizing that the developer tooling ecosystem around AI coding agents was fragmenting and needed consolidation.

### File-Based State Management

Nuttall's approach to AI agent state management is distinctly file-based rather than database-first. His projects `ralph`, `claude-sessions`, and `dotagents` all use the filesystem as the source of truth for agent state, session logs, and configuration. This philosophy connects to the broader "file system is the new database" movement in AI development, but Nuttall approaches it from a practical indie-hacker angle: files are free, portable, and don't require infrastructure management.

## Key Quotes

> "TLDR; serial internet biz builder, 100+ exits. Always learning. Usually from my mistakes."
> — ian.is

> "I make software with AI and talk about it."
> — Twitter bio

> "My programmatic SEO portfolio gets 80+ million impressions and 1+ million clicks a month — on autopilot."
> — Tweet, March 2025

> "I got sick of the 'AI loop of death' where the agent spirals, breaks stuff, and can't fix it! So I built a 4-rule task management system."
> — Tweet, 2025

> "Vibe coders and new developers coding with AI should be building MCP servers ASAP. An entire market is wide open."
> — Tweet, 2025

> "Back then there was no such thing as a programmatic SEO tool, unless you count PHP and a CSV! (which by the way, I still use both of those every day!)"
> — Practical Programmatic blog, December 2024

> "For deep work, slow down. Understanding your code is 100x better."
> — 10xDevelopers.dev tips

## Key Projects

### Claude-Agents (2,041+ GitHub stars)
Custom subagents for Claude Code including code-refactorer, content-writer, frontend-designer, prd-writer, project-task-planner, security-auditor, and vibe-coding-coach. Designed to be installed globally or per-project.

### Claude-Sessions (1,178+ GitHub stars)
Custom slash commands for Claude Code that provide comprehensive development session tracking and documentation. Solves the context degradation problem in long AI coding sessions.

### MCP-Boilerplate (1,016+ GitHub stars)
A remote Cloudflare MCP server boilerplate with user authentication and Stripe integration for paid tools. Designed to lower the barrier for indie developers building monetizable MCP servers.

### Ralph (851+ GitHub stars)
A minimal, file-based agent loop for autonomous coding. Demonstrates Nuttall's philosophy of using the filesystem as persistent state for AI agents.

### Playbooks.com
A curated directory of agent skills and MCP servers. Free to browse, no account required. Supports Claude Code, Cursor, Cline, Windsurf, and other AI coding tools.

### Typemat
A free programmatic SEO tool acquired by Nuttall in January 2024. Generates optimized pages from Google Sheets data, exportable to WordPress, Wix, or Squarespace.

### Practical Programmatic
Nuttall's content platform and course business teaching programmatic SEO strategies. Drives over 1M monthly pageviews using the techniques described.

## Related Concepts

- [[Programmatic-SEO]] — Nuttall's core business methodology
-  — Community he actively participates in
-  — His 2025–2026 focus area
- [[concepts/model-context-protocol-mcp.md]] — Model Context Protocol servers as a new product category
- [[Claude-Code]] — His primary AI coding tool
- [[concepts/harness-engineering/system-architecture/agent-skills.md]] — Playbooks.com is a skill directory for AI agents
-  — His approach to agent state management

## Sources

- Personal website: https://ian.is
- GitHub: https://github.com/iannuttall
- Twitter/X: @iannuttall
- Practical Programmatic blog: https://practicalprogrammatic.com
- Playbooks.com: https://playbooks.com
- Indie Hackers: https://www.indiehackers.com/iannuttall
- Thread Reader compilation: https://threadreaderapp.com/user/iannuttall
- 10xDevelopers.dev: https://10xdevelopers.dev/reference/claude-code-tips
- Tiny Startups: https://www.tinystartups.com/founders/ian-nuttall
