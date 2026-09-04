# Course / Lecture Series Portal Page Pattern

A portal page for a course or lecture series is a **concept-type wiki page** that serves as the central hub for a set of lecture transcripts, companion resources, and instructor profiles. It follows the MOC pattern but has a distinct structure tailored to educational content.

## When to Create a Course Portal Page

- User ingests a lecture series (Maven course, YouTube series, workshop recordings)
- Multiple lectures will be added over time as transcripts
- The series has identifiable instructors, a schedule, and companion resources
- Example: "Cheat at Search" (Doug Turnbull, 7 lectures), "Production-Ready Agent Engineering" (Will Brown & Kyle Corbitt, 6 lectures)

## Pattern: Lecture Series with Transcripts (No Slides)

When the source material is **transcript-based** (no slides), the pattern is:

```
wiki/
├── raw/articles/YYYY-MM-DD_platform_course-name-overview.md   ← course metadata
├── concepts/course-name-portal.md                              ← portal page
├── entities/instructor-name.md                                 ← instructor entities
└── transcripts/YYYY-MM-DD_instructor_lecture-slug.md           ← lecture transcripts
```

### Portal Page Structure

```yaml
---
title: "Course Name"
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [relevant-tags-from-schema]
sources:
  - raw/articles/YYYY-MM-DD_platform_course-name-overview.md
  - https://course-url
---
```

Body sections (in order):
1. **One-paragraph overview** with instructor links, schedule, price
2. **Course Overview** — 2-3 sentence description + numbered learning objectives table
3. **Instructors** — brief bios with entity page links
4. **Companion Resources** — table of GitHub repos, docs, related materials
5. **Lecture Schedule** — table with date, lecture title, transcript link (use `*pending*` for future lectures)
6. **Included Credits / Perks** — if applicable
7. **Key Concepts Covered** — wikilinks to related concept pages
8. **Comparison with Similar Courses** — optional table
9. **Related** — wikilinks to entities, concepts, and other portal pages

### Lecture Schedule Table (Living Index)

The lecture schedule table is the **key living artifact** — it gets updated as transcripts are added:

```markdown
| Date | Lecture | Transcript |
|------|---------|------------|
| Jun 17 (Tue) | Lecture 1 | *pending* |
| Jun 19 (Thu) | Lecture 2 | [[transcripts/YYYY-MM-DD_instructor_lecture-slug]] |
```

When a transcript is added:
1. Save transcript to `wiki/transcripts/`
2. Update the portal page table entry from `*pending*` to the wikilink
3. Bump `updated` date in portal frontmatter

### Raw Article for Course Metadata

Save course landing page metadata to `raw/articles/` as a structured summary:
- Course name, platform, instructors, schedule, price, description
- Learning objectives, target audience, companion resources
- Type: `course-overview` (not in SCHEMA — this is raw/ so tag rules are relaxed)

## Pattern: Lecture Series with Slides + Transcripts

When slides are available (e.g., Google Slides), each lecture produces TWO files:

```
wiki/
├── raw/articles/YYYY-MM-DD_instructor_lecture-name.md    ← slides summary
└── transcripts/YYYY-MM-DD_instructor_lecture-name.md     ← lecture transcript
```

The raw article has `type: slides` and links to the transcript; the transcript has `type: transcript` and links to the slides article. The portal page links to both.

## Instructor Entity Pages

- Check if entity pages already exist before creating
- If a stub exists in `concepts/`, create the full entity in `entities/` and redirect the stub
- Add the course to the instructor's entity page under a "Key Projects" or similar section
- Add bidirectional links: portal ↔ entity

## Tag Taxonomy Pitfalls

Common tag traps when creating course portal pages:

| Used | Problem | Correct |
|------|---------|---------|
| `agent-engineering` | Not in SCHEMA | `ai-agent-engineering` |
| `agent-training` | Check if exists | `agent-training` (exists) |
| `course` | Not in SCHEMA | `education` |
| `tutorial` | Check if exists | `tutorial` (exists) |

**Always verify tags** with `grep "tag-name" wiki/SCHEMA.md` before committing.

## Index.md Entry Format

For portal pages in `index.md` Concepts section:
```
- [[concepts/course-name]] — "Course Title" — Platform by Instructors. Date range. Key topics covered.
```

## Example

- `concepts/agents-mcp-rl-course.md` (2026-06-10) — Maven course by Will Brown & Kyle Corbitt. 6 lectures over 3 weeks. Portal for agent engineering + RL optimization content.
- Doug Turnbull's "Cheat at Search" series — lectures embedded in `entities/doug-turnbull.md` under a dedicated section, with 5 transcript pages in `wiki/transcripts/`.

## Pitfalls

- **Don't create placeholder transcripts** — only add transcript pages when actual content is available
- **Use `*pending*`** in the lecture table for future lectures, not broken wikilinks
- **English only** for all non-raw/ wiki content (portal pages, entity pages, index entries)
- **Bidirectional links are mandatory** — portal → entity, entity → portal, portal → related concepts
- **Lecture title extraction**: Maven SPA pages embed lecture titles in JSON `__NEXT_DATA__` — extract via terminal `curl + grep` rather than browser
