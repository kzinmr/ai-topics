---
title: "Every (company)"
created: 2026-05-25
updated: 2026-05-25
type: entity
tags:
  - entity
  - company
  - ai-native
  - agent-native
  - blog
  - podcast
  - openclaw
  - content-creator
sources:
  - "https://every.to/about"
  - "https://every.to/products"
  - "raw/articles/2026-04-17_every-to_folder-is-the-agent.md"
  - "raw/articles/2026-01-17_every-to_agent-native-architectures.md"
  - "raw/articles/2026-03-26_every-to_plus-one-openclaw-agents.md"
  - "raw/articles/2026-05-21_after-automation.md"
  - "raw/articles/2026-05-02_guide-to-agent-native-product-management.md"
  - "raw/articles/2026-05-24_lenny-podcast-dan-shipper-ai-paradox.md"
---

# Every

Every is a media and software company founded in 2020 by [[entities/dan-shipper|Dan Shipper]]. They publish a daily newsletter about emerging technology, run the "AI & I" podcast, build AI-native software products, offer courses, and provide AI consulting and training services.

**Website**: https://every.to  
**X**: [@every](https://x.com/every)  
**Subscribers**: 125,000+ founders, operators, and investors

## Products

### AI Applications
| Product | Description |
|---|---|
| **Spiral** | AI writing assistant with taste |
| **Cora** | AI email assistant ($15/month) |
| **Sparkle** | Automatic file organization (Mac) |
| **Monologue** | Voice dictation (3x faster) |
| **Proof** | Collaborative editor for humans and AI agents |
| **Plus One** | Hosted [[openclaw]] agent in Slack (one-click setup) |

### Content
- **Newsletter**: Daily technology coverage
- **AI & I Podcast**: Weekly conversations with tech leaders
- **Columns**: Chain of Thought (Dan Shipper), Context Window (staff)
- **Vibe Check**: Day-zero AI model reviews

### Experiments (Product Studio)
Every runs a product studio incubating AI-native tools:
| # | Product | Description |
|---|---|---|
| 006 | Proof | Write/edit with AI agents, track authorship |
| 005 | Kairos | Engage with reading content |
| 004 | TLDR | Business storytelling |
| 003 | Extendable Media | AI-expanded perspective media |
| 002 | MindTune | Attention control for thought shaping |
| 001 | Machcast | Guided prompts for shareable thoughts |

## Philosophy: Compound Engineering

Every pioneered [[concepts/compound-engineering-every|Compound Engineering]] — an AI-native development methodology where:
- Humans set up the right conditions (prompts, context files, skills)
- AI agents do the iterative building work
- Humans review and provide taste/judgment
- The loop compounds over time, building institutional knowledge

Key insight: **"The folder is the agent"** — a project directory with CLAUDE.md, skills, and accumulated context transforms a general model into a specialist [[concepts/folder-is-the-agent|Folder Is the Agent pattern]].

## Agent-Native Architecture

Every published definitive guides on [[concepts/agent-native-architecture|Agent-Native Architecture]]:

### Core Principles
1. **Parity** — Agent achieves everything UI can
2. **Granularity** — Tools are atomic primitives; features are outcomes via prompts
3. **Composability** — New features = new prompts, not code
4. **Emergent Capability** — Agents accomplish unanticipated tasks
5. **Improvement Over Time** — Better through context accumulation + prompt refinement

### Dispatch Layer Pattern
- Ruby daemon watches directory for spawn requests
- Lead agent breaks tasks into subtask files
- Daemon spawns workers in correct folders
- Workers report back via files (no custom networking needed)
- **Scale**: Running 44 folders-as-agents across projects

## Key People
- **Dan Shipper** — CEO, cofounder
- **Kieran Klaassen** — Cora general manager, compound engineering pioneer
- **Trevin Chow** — Product leader
- **Katie Parrott** — Writer, AI guides
- **Willie Williams** — Writer, OpenClaw guides
- **Lucas Fischer** — Designer, Monologue

## Team AI Usage
- 95% of work emails handled by AI (Cora)
- No one writes code by hand — all engineering is AI-assisted
- Team of ~30 runs 5 software products + media operation
- AI agents (@Claudie, @Andy, @Viktor) are first-class Slack team members
- **44 folders-as-agents** running across projects

## Related Pages
- [[entities/dan-shipper]] — CEO and cofounder
- [[concepts/compound-engineering-every]] — Development methodology
- [[concepts/folder-is-the-agent]] — Architecture pattern
- [[concepts/agent-native-architecture]] — Design principles
- [[concepts/after-automation]] — Automation paradox analysis
- [[concepts/human-sandwich]] — Human-AI collaboration pattern
- [[openclaw]] — Underlying agent platform for Plus One
- [[concepts/ai-slop]] — "Visible sameness" concept coined here
