---
title: "Agent Media — From Wiki to Multi-Channel Autoresearch Desk"
type: concept
aliases:
  - agent-media
  - autoresearch-desk
  - agent-media-concept
created: 2026-05-11
updated: 2026-05-26
tags:
  - concept
  - agent-media
  - skill-graph
  - context-engineering
status: active
description: "Design philosophy for evolving a structured knowledge base (wiki) into an audience-aware, multi-channel distribution system. Integration of Khairallah's Context Engineering + Ronin's Skill Graph."
sources:
  - "Khairallah AL-Awady — How to Master Context Engineering (May 2026)"
  - "Ronin (@DeRonin_) — Skill Graph Content Engine (April 2026)"
  - "Hermes wiki's own structure and delivery pipeline"
---

# Agent Media — Autoresearch Desk

**Agent Media** is a system design philosophy in which a structured knowledge base (wiki) is operated by AI agents as "editors," redistributing knowledge in **platform-native forms** across multiple channels and audiences.

A traditional wiki is a pull model — "humans come and search." An Autoresearch Desk is a push model — "agents deliver tailored content to audiences."

## Design Origins

The Autoresearch Desk emerges at the intersection of two independent frameworks:

| Framework | What It Provides | Source |
|--------------|------------|------|
| **Context Engineering** (practitioner perspective) | 4-file architecture, dynamic loading, memory evolution ladder, need for audience definition | Khairallah AL-Awady |
| **Skill Graph** (implementation perspective) | Folder structure, wikilink navigation, repurpose chain, platform-native rethinking, Litmus Test | Ronin (@DeRonin_) |

## Current Wiki vs Autoresearch Desk

| Dimension | Current Wiki | Autoresearch Desk |
|------|-----------|-------------------|
| **Delivery model** | Pull (humans come and search) | Push (agents deliver) |
| **Channels** | Single (Discord) | Multi-channel (Discord / Slack / Telegram / X) |
| **Audience awareness** | None (same info for everyone) | Segmented (tech depth / business / quick) |
| **Content transformation** | Raw update notifications | Platform-native restructuring |
| **Feedback loop** | None | Engagement tracking → delivery optimization |
| **index.md** | Exists but not for delivery | Briefing for delivery agents |

## Architecture Design

### Proposed Folder Structure

Adding an `agent-media/` layer to the existing wiki structure:

```
wiki/
├── concepts/          # Existing: Knowledge nodes
├── entities/          # Existing: People/organization nodes
├── raw/               # Existing: Source articles
├── SCHEMA.md          # Existing: Quality standards (= Standards File)
├── index.md           # Existing: Full index (for curation)
│
└── agent-media/       # NEW: Delivery engine layer
    ├── index.md                # Command center (briefing for delivery agent)
    ├── voice/
    │   ├── brand-voice.md      # Wiki's voice: analytical, technically accurate, Japanese/English bilingual
    │   └── channel-tone.md     # Channel-specific tone adaptation
    ├── channels/               # Channel-specific playbooks
    │   ├── discord.md          # Real-time, technical depth, conversational
    │   ├── slack.md            # Team-oriented, structured, action-oriented
    │   ├── telegram.md         # Builder-focused, insight-driven, link-based
    │   └── x.md                # Public, short-form, hook-driven
    ├── engine/
    │   ├── repurpose.md        # Wiki knowledge → channel-specific transformation chain
    │   ├── hooks.md            # Channel-specific hook patterns
    │   └── scheduling.md       # Delivery calendar (Daily Report, etc.)
    └── audience/
        ├── practitioners.md    # Technical practitioners (agent developers)
        ├── researchers.md      # AI researchers
        ├── builders.md         # Product builders (PMs/entrepreneurs)
        └── knowledge-workers.md # Knowledge workers (AI adopters)
```

### repurpose.md: Wiki Knowledge → Multi-Channel Transformation Chain

Adapting Ronin's repurpose chain for knowledge delivery:

```
1 Wiki update (e.g., expanding the context-engineering concept page)
    │
    ├─→ Discord: Technical details + code-level changes + [[wikilinks]]
    │   "Added Khairallah's 4-file architecture to context-engineering.
    │    Dynamic context loading implementation → [[concepts/skill-graph]]"
    │
    ├─→ Slack: Structured summary + action items
    │   "📋 Context Engineering refined: Added 3-layer model, 4-file architecture,
    │    memory evolution ladder. Directly applicable to Autoresearch Desk design."
    │
    ├─→ Telegram: Insights + links + business context
    │   "How AI agents stop being 'geniuses with amnesia.'
    │    Integrated the practical framework of Context Engineering into the wiki.
    │    Details→ [link]"
    │
    └─→ X: Short-form hook + 1 insight
        "prompt engineering = syntax.
         context engineering = infrastructure.
         infrastructure beats syntax every single time.
         How to give AI 'eyes' in 6 weeks — now wiki'd."
```

### channel-tone.md: Channel-Specific Tone Adaptation

| Channel | Tone | Depth | Length | Frequency |
|---------|--------|------|------|------|
| **Discord** | Analytical, conversational, technically accurate | Deep | Medium–Long | On update |
| **Slack** | Structured, professional, action-oriented | Medium | Medium | Daily Report |
| **Telegram** | Casual, insight-driven, builder-focused | Shallow–Medium | Short–Medium | 1–2/day |
| **X** | Short-form, hook-driven, public | Shallow | 280–2000 chars | 1–2/day |

### hooks.md: Channel-Specific Hook Patterns

Hooks tailored to each channel's characteristics:

| Channel | Effective Hooks |
|---------|-------------|
| **Discord** | "Expanded a new concept page" / "Added implementation patterns for ~" |
| **Slack** | "📋 Today's Wiki Update: [N] items" / "Weekly key topic: [topic]" |
| **Telegram** | "What does it mean for AI to have 'eyes'" / "What most people overlook about ~" |
| **X** | "prompt engineering is syntax. context engineering is infrastructure." |

## Implementation Roadmap

### Phase 1: Audience Definition (This Week)
- Create 4 files in `agent-media/audience/`
- Define each audience's information needs, tone expectations, and channel preferences

### Phase 2: Command Center (Next Week)
- Create `agent-media/index.md`
- Wiki identity, delivery purpose, channel map, execution instructions
- Experiment with audience-specific branching in existing Daily Report cron job

### Phase 3: Channel Playbooks (Within 2 Weeks)
- Create channel-specific files for Discord / Slack / Telegram / X
- Migrate existing delivery pipeline to channel-specific templates

### Phase 4: Feedback Loop (Within 1 Month)
- Track engagement on each channel
- Learn which information resonates with which audience
- Continuously improve hooks.md and channel-tone.md

## Design Principles

1. **Rethinking, not Reformatting** (Ronin): Rethink the same knowledge for each channel. Not reformatting.
2. **Context tells WHY/WHAT, Channels tell HOW, Schedule tells WHEN/WHERE** (Khairallah): Application of MCP integration patterns.
3. **Litmus Test**: "Would someone following all channels be bored seeing the same thing?" Yes → it's mere reformatting.
4. **Evolutionary Design** (Ronin): Improve weekly. Encode performance data into files.
5. **Memory Evolution Ladder** (Khairallah): Manual → Structured KB → Vector DB+RAG → **Autoresearch Desk**

## Related Concepts

- [[concepts/skill-graph]] — Interconnected Markdown for AI agent playbooks
- [[concepts/harness-engineering/context-engineering]] — Context Engineering (including practitioner framework)
- [[entities/khairallah-al-awady]] — Khairallah AL-Awady: Proponent of the 4-file architecture
- [[entities/ronin-deronin]] — Ronin: Proponent of the Skill Graph architecture
- [[concepts/memory-systems-design-patterns]] — AI agent memory design patterns
