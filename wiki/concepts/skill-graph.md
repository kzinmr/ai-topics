---
title: "Skill Graph — Interconnected Markdown Files as an AI Agent Playbook"
type: concept
aliases:
  - skill-graph
  - content-skill-graph
  - skill-graph
created: 2026-05-11
updated: 2026-05-27
tags:
  - concept
  - skill-graph
  - content-engine
  - context-engineering
  - agent-media
status: active
sources:
  - "Ronin (@DeRonin_) — How To Build Own Content Engine? (FULL COURSE), April 2026"
  - "Linas Beliūnas — Skill Graphs: Fix Your AI Agent's Context Problem (Substack)"
---

# Skill Graph

An architecture in which a folder of interconnected Markdown files serves as an AI agent's "playbook." Each file is a "knowledge node," cross-referenced via `[[wikilinks]]`. The AI agent starts from an entry point (index.md), follows links to load only the needed knowledge nodes into its context window, builds a complete understanding, and then executes the task.

## Core Theory

> "One flat .md file gives you a TOOL. A graph gives you a TEAM." — Ronin

> "The bigger the context, the worse the reasoning. Skill graphs solve this: most knowledge stays on disk. Only what matters enters the context window." — Linas Beliūnas

### Traditional Prompting vs. Skill Graph

| Approach | Behavior | Result |
|-----------|------|------|
| **Single prompt** | One instruction, zero context | Like hiring a "genius with amnesia" every time |
| **Flat file** | One large reference document | TOOL (simple lookup reference) |
| **Skill graph** | 30+ interconnected .md files | TEAM (platform specialist, tone adaptation, audience-specific responses) |

## Architecture

### Standard Folder Structure (Ronin's 17-file Model)

```
/content-skill-graph
├── index.md                  # Command center (entry point)
├── platforms/                # Platform-specific playbooks
│   ├── x.md                  # X/Twitter: short-form, hook-driven, casual lowercase
│   ├── linkedin.md           # LinkedIn: personal narrative, professional
│   ├── instagram.md          # Instagram: visual-first, carousel
│   ├── tiktok.md             # TikTok: raw screen recording, 2-second hook
│   ├── youtube.md            # YouTube: deep tutorials, 8-12 min
│   ├── threads.md            # Threads: conversational, opinion-driven
│   ├── facebook.md           # Facebook: community discussion
│   └── newsletter.md         # Newsletter: most personal, behind-the-scenes
├── voice/                    # Brand voice DNA
│   ├── brand-voice.md        # Core personality across all platforms
│   └── platform-tone.md      # Platform-specific tone adaptation
├── engine/                   # Operational engine
│   ├── hooks.md              # Hook patterns (80% of performance)
│   ├── repurpose.md          # 1 idea → 10 platform conversion chain
│   ├── scheduling.md         # Content calendar
│   └── content-types.md      # Format definitions (thread/carousel/video/long-form)
└── audience/                 # Audience segments
    ├── builders.md           # For technical people
    └── casual.md             # For general audience
```

### Core Components

#### index.md (Command Center)
Not a table of contents. It is a **briefing**. Includes:
- **Identity**: Who you are and what you do (niche specificity is paramount)
- **System Purpose**: What this graph generates
- **Node Map with Context**: Context-bearing links like `[[x]] — short-form, hook-driven, 280 chars max`
- **Execution Instructions**: Step-by-step execution procedures

#### platform-tone.md (DNA Adaptation Layer)
A "bridge" adapting the same personality to each platform's culture. Like the difference between speaking at a party vs. a business dinner vs. a podcast interview.

#### repurpose.md (Conversion Chain)
**One idea goes in, 10 platform-native posts come out. It's not reformatting — it's rethinking.**
Chain order: X → LinkedIn → Instagram → TikTok → YouTube → Newsletter → Threads → Facebook

**Litmus test**:
> "If someone followed me on ALL platforms, would they be annoyed seeing the same thing everywhere?"
> If yes → reformatting. If no → 8 unique pieces from one idea.

## How to Use

### Method 1: Claude Projects (Recommended)
1. Create a Project → upload all files
2. Give a topic
3. Claude reads index.md, follows wikilinks, reads connected nodes, outputs 8 platform-native posts

### Method 2: Context Paste
- Paste index.md content into any AI chat
- Add execution instructions
- Give a topic

### Method 3: Cursor / Claude Code (Most Powerful)
- Keep the graph on local filesystem
- Agent directly reads and updates files
- The graph itself evolves over time (updating hooks.md, adjusting platform-tone.md)

## Design Principles

| Principle | Description |
|------|------|
| **Graph > Flat File** | One flat .md = TOOL. Graph = TEAM |
| **Wikilinks as Navigation** | `[[wikilinks]]` let AI follow citations like a researcher |
| **Platform-Native Repurposing** | Rethinking, not reformatting |
| **Evolutionary Design** | Update hooks.md weekly, improve based on performance |
| **Compound Interest** | Encoding learnings into files makes the system smarter over time |

## Relationship to Context Engineering

The Skill Graph is an **applied implementation** of Context Engineering ([[concepts/harness-engineering/context-engineering]]):

| Context Engineering Concept | Skill Graph Equivalent |
|------------------------|-------------------|
| Dynamic context loading | Selective node loading via Wikilinks |
| Attention Budget | Only load needed nodes into context (most stays on disk) |
| 4-file architecture (Khairallah) | Expanded into voice/ + audience/ folders |
| JIT context | Gradual discovery via index.md → wikilinks → needed nodes |
| Structured memory (Anthropic) | The folder structure itself is a persistent memory system |

## Application to Autoresearch Desk

The existing wiki is already a skill graph (structured .md + `[[wikilinks]]`), but it is **optimized for curation**, not **optimized for distribution**.

What is needed to convert it into an Autoresearch Desk:
1. **Create index.md**: A "command center" for the wiki — a briefing for the agent to understand distribution tasks
2. **platforms/ folder**: Platform-specific playbooks for Discord / Slack / Telegram / X
3. **engine/repurpose.md**: Wiki knowledge → multi-channel conversion chain
4. **audience/ folder**: Technical practitioners / AI researchers / Product builders / Knowledge workers

→ Details: [[concepts/agent-media]]

## Related Concepts

- [[concepts/agent-skills-overview]] — Agent Skills concept cluster map (parent page)
- [[concepts/harness-engineering/context-engineering]] — Technical foundation of Context Engineering
- [[concepts/agent-media]] — Autoresearch Desk: from Wiki to multi-channel distribution engine
- [[entities/ronin-deronin]] — Ronin: proposer of the skill graph architecture
- [[entities/khairallah-al-awady]] — Khairallah: practitioner framework via 4-file architecture
