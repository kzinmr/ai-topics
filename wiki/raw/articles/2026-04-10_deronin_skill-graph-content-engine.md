---
title: "How To Build Own Content Engine? (FULL COURSE) — Skill Graph Architecture"
source: X Article
author: Ronin
author_handle: DeRonin_
url: https://x.com/deronin_/status/2042604279077237170
article_url: https://x.com/i/article/2041112698885210112
date_published: 2026-04-10
type: x_article
tags:
  - skill-graph
  - content-engine
  - agent-media
  - context-engineering
  - markdown
  - wikilinks
  - repurposing
  - platform-native
---

# How To Build Own Content Engine? (FULL COURSE)

I run 10 social medias for my clients and don't write a single post manually.

No content team. No $8-12k/mo agency retainer. No sitting in front of ChatGPT rewriting the same damn post ten times for ten platforms.

Just a folder of .md files + one AI agent, and a system that takes one idea and produces 10 platform-native posts (each one actually thinking about the topic differently).

---

## Core Concept: The Skill Graph

> "You're basically hiring a genius with amnesia every single time you start a new chat."

A **skill graph** is a folder of interconnected markdown files where each file is one "knowledge node" — one piece of your content system's brain. Files reference each other via `[[wikilinks]]`. When an AI agent reads the graph, it follows the links, builds complete understanding BEFORE writing.

**The difference:**
- **BAD**: Single prompt = hiring a freelancer with no brief, no brand guidelines, no knowledge of your audience
- **GOOD**: Graph of 30+ interconnected .md files = hiring a full content team that's read your entire playbook

> "One flat .md file gives you a TOOL. A graph gives you a TEAM."

## Folder Structure

```
/content-skill-graph
├── index.md                  # Command center (entry point)
├── platforms/
│   ├── x.md                  # X/Twitter playbook
│   ├── linkedin.md           # LinkedIn playbook
│   ├── instagram.md          # Instagram playbook
│   ├── tiktok.md             # TikTok playbook
│   ├── youtube.md            # YouTube playbook
│   ├── threads.md            # Threads playbook
│   ├── facebook.md           # Facebook playbook
│   └── newsletter.md         # Newsletter playbook
├── voice/
│   ├── brand-voice.md        # Core personality across ALL platforms
│   └── platform-tone.md      # How voice adapts per platform
├── engine/
│   ├── hooks.md              # Hook formulas (80% of performance)
│   ├── repurpose.md          # 1 idea → 10 platform-native posts
│   ├── scheduling.md         # Content calendar
│   └── content-types.md      # Thread/carousel/video/long-form definitions
└── audience/
    ├── builders.md           # Technical, builder-oriented audience
    └── casual.md             # Broader, casual audience
```

17 files. 4 folders. That's the entire content production machine.

## Key Files

### index.md (The Command Center)

NOT a table of contents. It's a BRIEFING. Tells the agent who you are, what the system does, and exactly how to execute.

Contains:
- Identity section (niche, what you do)
- System purpose (what this graph produces)
- Node map with context (not just `[[x]]` but `[[x]] — short-form, hook-driven, 280 chars max, casual lowercase`)
- Execution instructions (step by step workflow)

### Platform Files (x.md, linkedin.md, etc.)

Each platform file is a complete playbook:
- **Platform DNA**: character limits, vibe, audience type
- **Content Rules**: hooks that work, tone adjustments, formatting rules
- **Formats That Work**: specific post types that perform on each platform
- **Posting Strategy**: frequency, best times
- **Audience Profile**: what they want, what they don't want
- **Repurposing Notes**: where this platform sits in the chain

### voice/brand-voice.md (Content DNA)

Source of truth every other file references:
- Core personality (3-5 sentences)
- Tone markers (casual but credible, direct and personal, raw honesty over polish)
- Vocabulary (words we use vs. words we NEVER use)
- Formatting rules (lowercase default, line breaks between every thought)

### voice/platform-tone.md (Adapt DNA)

Bridge between universal voice and each platform's culture. Like how you talk differently at a house party vs a business dinner vs a podcast interview — same person, different energy.

### engine/hooks.md

Hooks are where 80% of content performance is decided. Categories:
- Contrarian hooks, proof hooks, discovery hooks, playbook hooks
- Each with templates and examples

### engine/repurpose.md (The Production Pipeline)

**One idea enters. Ten platform-native posts come out. Each one THINKS about the topic differently — this is NOT reformatting.**

Chain order:
1. X (write first — forces brevity)
2. LinkedIn (expand with narrative)
3. Instagram (make it visual — carousel)
4. TikTok (make it raw — 45-60 sec script)
5. YouTube (make it deep — 8-12 min tutorial)
6. Newsletter (make it personal — behind-the-scenes)
7. Threads (make it conversational)
8. Facebook (make it community — discussion)

**The Litmus Test:**
> "If someone followed me on ALL platforms, would they be annoyed seeing the same thing everywhere?"
> If yes → you're reformatting, not rethinking. Go back.
> If no → you've made 8 unique pieces from one idea. That's the goal.

## How to Use

**Method 1: Claude Projects**
1. Create Project → "Content Skill Graph"
2. Upload all 17 files into project knowledge base
3. Start conversation, give a topic
4. Claude reads index.md → follows wikilinks → reads connected nodes → outputs 8 platform-native posts

**Method 2: Paste Context** (works with any AI)
- Copy index.md + paste into any AI chat
- Add execution instructions
- Give topics

**Method 3: Cursor / Claude Code** (most powerful)
- Keep graph on local filesystem
- Agent reads files directly
- Can also UPDATE files — the graph evolves itself over time

## Conclusion

The skill graph is designed to grow. Start small, add nodes, refine connections. Every week it gets smarter because you're encoding what you've learned into the files themselves. It's compound interest for your content system.

One folder. 17 markdown files. One AI agent. 10 platforms. ZERO manual writing.
