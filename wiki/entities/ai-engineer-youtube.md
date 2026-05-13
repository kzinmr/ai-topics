---
title: "AI Engineer (YouTube Channel)"
created: 2026-05-13
updated: 2026-05-13
type: entity
tags: [youtube, ai-agents, community, developer-experience, agentic-engineering, ai-infrastructure, ai-coding]
sources: [https://www.youtube.com/@aidotengineer, https://ai.engineer]
---

# AI Engineer (YouTube Channel)

**AI Engineer** (@aiDotEngineer) is the official YouTube channel of the [AI Engineer](https://ai.engineer) conference series — the largest technical AI conference community in the world. With **466K subscribers** and **700+ videos**, it publishes talks, workshops, and training sessions from AI Engineer events (World's Fair, Summit, Code) and partner conferences globally.

The channel is the primary free distribution platform for AI Engineer conference content, making high-signal technical talks from frontier AI labs and startups accessible to a global audience of AI engineers.

## Key Facts

| Field | Detail |
|-------|--------|
| **Channel** | [@aiDotEngineer](https://www.youtube.com/@aidotengineer) |
| **Subscribers** | 466K |
| **Videos** | 707+ |
| **Parent Org** | [AI Engineer](https://ai.engineer) |
| **Conference Series** | World's Fair (SF), Summit (NYC), Code, Europe (London), partner events worldwide |
| **Content Type** | Technical talks, workshops, panel discussions, live coding sessions |
| **RSS Feed** | `https://www.youtube.com/feeds/videos.xml?channel_id=UCLKPca3kwwd-B59HNr-_lvA` |

## Content Themes

The channel covers the full spectrum of AI engineering topics:

- **AI Agent Architecture**: Harness design, multi-agent systems, agent-computer interaction
- **AI Coding & Developer Tools**: Claude Code, OpenClaw, Pi, Codex, Copilot workflows, vibe coding
- **Frontier Model Capabilities**: Anthropic, OpenAI, DeepSeek research and product talks
- **Infrastructure & Deployment**: GPU optimization, inference serving, on-device AI, MLX
- **Software Engineering Fundamentals**: TDD, vertical slices, deep modules applied to AI development
- **Enterprise AI**: Fortune 500 deployments, agentic commerce, vertical AI applications

## Notable Talks

| Talk | Speaker | Views | Date |
|------|---------|-------|------|
| ["Don't Build Agents, Build Skills Instead"](https://www.youtube.com/watch?v=wflNENRSUb4) | Barry Zhang & Mahesh Murag (Anthropic) | 1.3M | Dec 2025 |
| ["The New Code"](https://www.youtube.com/watch?v=z4zXicOAF28) | Sean Grove (OpenAI) | 1M | Jul 2025 |
| ["Software Fundamentals Matter More Than Ever"](https://www.youtube.com/watch?v=xmbSQz-PNMM) | Matt Pocock | 642K | Apr 2026 |
| ["No Vibes Allowed: Solving Hard Problems in Complex Codebases"](https://www.youtube.com/watch?v=D7BzTxVVMuw) | Dex Horthy (HumanLayer) | 540K | Dec 2025 |
| ["How We Build Effective Agents"](https://www.youtube.com/watch?v=5zE2sMka620) | Barry Zhang (Anthropic) | 455K | Jun 2024 |
| ["Extreme Harness Engineering: 1M LOC, 1B toks/day"](https://www.youtube.com/watch?v=veShHxQYPzo) | Ryan Lopopolo (OpenAI) | 39K | Mar 2026 |
| ["Dark Factory: Notes from OpenClaw's #2 maintainer"](https://www.youtube.com/watch?v=wflNENRSUb4) | Vincent Koc (Comet ML) | 6.2K | May 2026 |

## Relationship to Wiki

- **Conference coverage**: Talks from AI Engineer events are ingested into the wiki as raw articles with full transcripts via the [[youtube-content]] workflow
- **Speaker entities**: Many speakers ([[ryan-lopopolo]], [[matt-pocock]], [[barry-zhang]], [[sean-grove]]) have dedicated entity pages enriched from their AI Engineer talks
- **Concept enrichment**: Frameworks and taxonomies from AI Engineer talks extend concept pages like [[ai-agents]], [[agent-harness]], and [[ai-coding]]
- **RSS monitoring**: The channel's RSS feed is tracked via [[blogwatcher]] for daily new video discovery

## Monitoring

The channel is monitored through the blogwatcher RSS pipeline (`config/feeds/blogs.opml` → YouTube Channels section). New video descriptions are captured daily; full transcript ingestion is done on-demand via the `/opt/data/bin/yt-dlp` workflow for high-signal talks.
