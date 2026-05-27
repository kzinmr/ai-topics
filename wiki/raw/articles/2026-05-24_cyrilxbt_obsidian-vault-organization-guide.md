---
title: "How to Organize Your Obsidian Vault So You Can Always Find What You Need"
source: https://x.com/cyrilxbt/status/2058373087330959829
source_type: x_article
author: "@cyrilxbt"
author_id: "1373665408193036293"
date: 2026-05-24
date_retrieved: 2026-05-27
type: x_article
tags: [obsidian, knowledge-management, pkm, note-taking, claude-code, mcp, retrieval]
---

# How to Organize Your Obsidian Vault So You Can Always Find What You Need

## Summary

A comprehensive guide to organizing Obsidian vaults around a "retrieval-first" principle. The author argues that most vaults fail because they're organized for storage (like filing cabinets) rather than for retrieval (like thinking systems). The guide covers folder structure, naming conventions, YAML properties, tagging taxonomy, Maps of Content (MOCs), inbox processing, search strategies, quarterly reviews, and Claude Code integration via Filesystem MCP for natural language vault queries.

## Key Sections

1. **The Retrieval-First Principle**: Organize for retrieval speed, not capture convenience
2. **Folder Structure**: 8 top-level folders (INBOX, NOTES, PROJECTS, AREAS, RESOURCES, ARCHIVE, SYSTEM)
3. **Naming Convention**: `YYYY-MM-DD-[TYPE]-[TOPIC].md` for searchable filenames
4. **Properties System**: YAML frontmatter with type, status, date, tags for Dataview filtering
5. **Tagging System**: Three categories with prefixes — topic tags (no prefix), status/ prefix, project/ prefix
6. **Maps of Content**: Hub notes that link related notes together for topic navigation
7. **Inbox Processing**: Daily/periodic triage of uncategorized notes into the structured system
8. **Search Strategy**: Full-text, property, and tag-based search combinations
9. **Claude Integration via MCP**: Natural language querying of vaults through Claude Code + Filesystem MCP
10. **Quarterly Vault Review**: Regular maintenance audits for structure integrity

## Full Content

Most Obsidian users have the same problem six months after they start.
They have hundreds of notes. They know the information they need is in there somewhere. They cannot find it quickly enough to be useful.
The search returns too many results. The folder structure they designed in week one no longer makes sense for the notes they are creating in month six. The tags they applied inconsistently are worse than no tags at all.
The vault that was supposed to make them more organized has become another thing to manage.

This happens not because Obsidian is poorly designed.
It happens because most people organize their vault the way they organize a filing cabinet rather than the way they organize a thinking system.
A filing cabinet is optimized for storage.
A thinking system is optimized for retrieval.
The difference between those two goals produces completely different organizational architectures.

This article is the complete guide to organizing your Obsidian vault so you can find anything in under 30 seconds regardless of how many notes you have.

### The Retrieval-First Principle

Before the structure understand the principle that should drive every organizational decision.
You do not organize a vault to put things away neatly.
You organize a vault to get things back quickly.
Every folder you create, every tag you apply, every naming convention you adopt should be evaluated against one question: does this make retrieval faster or slower.
Most organizational systems fail because they are designed for the moment of capture rather than the moment of retrieval.
You create a folder called "Ideas" because that is what the note contains when you create it.
Six months later you are looking for a note about a business idea you had. You do not remember whether you filed it in Ideas, Projects, Business, or your daily note from the day you had the thought.
The folder name made sense at capture time. It tells you nothing at retrieval time.

### The Four Things You Always Know About a Note

When you are looking for a note in the future you will reliably know one or more of four things about it:
1. What type of content it is (project, reference, daily note, task, meeting, book summary, idea)
2. When you created or used it (this week, this month, last year, specific event)
3. What topic it relates to (subject area, person, project, concept)
4. What status it currently has (active, completed, archived, in progress, waiting)

### The Folder Structure

The correct folder structure has between five and eight top-level folders:
- `00 - INBOX/` — landing zone for uncategorized captures
- `01 - NOTES/` (daily/, meetings/, books/, courses/) — time-stamped captures
- `02 - PROJECTS/` — one subfolder per active project with defined outcomes
- `03 - AREAS/` — ongoing responsibilities without end dates (health, finances, career)
- `04 - RESOURCES/` — reference material organized by topic/person/place/tool
- `05 - ARCHIVE/` — completed projects, outdated references, old notes
- `06 - SYSTEM/` — templates, MOCs, configuration files

### The Naming Convention

`YYYY-MM-DD-[TYPE]-[TOPIC].md`

Examples:
- `2026-05-20-daily-wednesday.md`
- `2026-05-18-project-website-launch.md`
- `2026-05-15-meeting-client-quarterly-review.md`
- `2026-04-28-resource-claude-prompting-techniques.md`

The date prefix enables automatic chronological sorting, approximate temporal search, and prevents naming conflicts.

### The Properties System

Every note has YAML frontmatter with universal properties:
```yaml
type: [daily/meeting/project/area/resource/book/course/idea/task]
status: [active/complete/archived/reference/waiting]
date: 2026-05-20
tags: [topic1, topic2, topic3]
```

Additional properties by note type for projects (deadline, priority, next_action), books (author, rating, key_insight), meetings (attendees, decisions, actions), resources (topic, source, reliability).

### The Tagging System

Three categories with consistent prefixes:
- **Topic tags** (no prefix): `#productivity`, `#machine-learning`, `#real-estate`
- **Status tags** (`status/` prefix): `#status/active`, `#status/waiting`, `#status/complete`
- **Project tags** (`project/` prefix): `#project/website-launch`, `#project/book-writing`

Rule: only create a new tag if you will use it on at least five notes.

### Maps of Content (MOC)

A Map of Content is a note that links to other notes, serving as an index for a cluster of related notes. Create an MOC when a topic has accumulated >20 notes and backlink navigation becomes difficult.

### The Inbox Processing Habit

Process INBOX regularly (15 min/day). For each note ask: What type? Does it have a home? Should it be added to an existing note? Then update properties, rename, and move.

### The Search Strategy

Four search modes:
1. Full text search — when you remember distinctive phrases
2. Property search — filter by `type:project status:active`
3. Tag search — filter by `#productivity`
4. Date-based — sort by creation date within relevant folder

### The Claude Integration That Makes Retrieval Intelligent

Connected to Claude Code via Filesystem MCP, the vault becomes searchable in natural language:
- "Find all notes about pricing strategy I created in the last six months."
- "What have I written about managing energy versus managing time?"
- "Show me every project note that is currently active and has a deadline before July."

Claude reads the vault structure, properties, and content, returning relevant notes with context about why they matched.

### The Quarterly Vault Review

Four areas: folder audit, tag audit, archive sweep, naming inconsistency check. Takes 30 min to 2 hours depending on vault size.

### Starting From Where You Are

Progressive reorganization over 3 months:
- Week 1: Create folder structure
- Week 2: Start filing new notes correctly
- Week 3: Process INBOX backlog
- Month 2: Retroactive tagging, first MOC
- Month 3: First quarterly review

