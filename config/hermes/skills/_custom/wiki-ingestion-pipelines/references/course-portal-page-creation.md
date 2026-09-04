# Course / Lecture Series Portal Page Creation

When ingesting a multi-lecture course or lecture series into the wiki, create a structured portal page that connects the course content to related concepts, entities, and platforms.

## Architecture: Multi-Directory Pattern

A course portal spans multiple wiki directories:

| Directory | Content | Example |
|-----------|---------|---------|
| `concepts/` | Portal page (concept type) | `concepts/agents-mcp-rl-course.md` |
| `raw/articles/` | Course overview metadata | `raw/articles/2026-06-10_maven_agents-mcp-rl-course-overview.md` |
| `transcripts/` | Lecture transcripts | `transcripts/2025-06-17_willbrown_agents-mcp-rl-agent-patterns-lecture.md` |
| `raw/articles/` | Per-lecture summaries | `raw/articles/2025-06-18_willbrown_agents-mcp-rl-lesson1.md` |
| `entities/` | Instructor pages | `entities/will-brown.md`, `entities/kyle-corbitt.md` |

## Portal Page Structure (concepts/)

```yaml
---
title: "<Course Full Title>"
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [relevant, tags, from, SCHEMA]
sources:
  - raw/articles/<course-overview>.md
  - <course-url>
---
```

### Required Sections

1. **Header** — Course name, platform link, instructors (as wikilinks), schedule, time commitment, price
2. **Course Overview** — 3-pillar summary of what the course covers
3. **Learning Objectives** — Numbered table of topics
4. **Instructors** — Each with role, background, key contributions, link to entity page
5. **Companion Resources** — GitHub repos, related tools
6. **Lecture Schedule** — Table with Date | Lecture | Transcript columns. Initially `*pending*` for future lectures; update with wikilinks as transcripts are ingested
7. **Ecosystem Context** — How the course connects to platforms/services (see below)
8. **Key Concepts Covered** — Links to related concept pages
9. **Related** — Wikilinks to instructors, concepts, entities

### Ecosystem Context Section (CRITICAL)

This section explains WHY the course exists — what platforms/services it serves as education/onboarding for. Structure:

```markdown
## Ecosystem Context

This course is not just educational content — it is a **strategic onboarding path**
into the <ecosystem> built around key platforms:

### <Platform A> ↔ <Core Library>
<Platform> provides <what>. The <library> is the core building block.
The course teaches the **background knowledge needed to use <library> effectively**.

### <Platform B> ↔ <Service>
<Platform> provides <service>. The course teaches the **fundamentals**
that <Platform>'s customers need.

### The <Framework Name>
This course embodies the [[concepts/framework]] thesis: <explanation>.
The course teaches both sides — <harness skill> and <RL skill> — as complementary skills.
```

## Bidirectional Linking (MANDATORY)

After creating the portal page, ensure links flow in all directions:

```
Portal Page ──────────────────────────────────────┐
  ├─→ Instructor Entity Pages (entities/)          │
  ├─→ Platform Entity Pages (entities/)            │
  ├─→ Related Concept Pages (concepts/)            │
  ├─→ Lecture Transcripts (transcripts/)           │
  └─→ Lecture Summaries (raw/articles/)            │
                                                    │
Instructor Entity ←── portal link                   │
Platform Entity ←── portal link                     │
Related Concepts ←── "Related Course Materials"     │
  section with transcript links                     │
                                                    │
agentic-search ←── portal + transcript links        │
rl-harness-lifecycle ←── portal link                │
```

### Step-by-Step Linking

1. **Portal → Instructor entities**: Add `[[entities/instructor-name]]` in header and instructors section
2. **Instructor entity → Portal**: Add portal link in Key Projects section AND Related section
3. **Portal → Platform entities**: Add `[[entities/platform-name]]` in Ecosystem Context
4. **Platform entity → Portal**: Add portal link in Related Pages section
5. **Related concepts → Portal**: Add "Related Course Materials" section to concept pages (e.g., `agentic-search.md`, `rl-harness-lifecycle.md`) with links to portal and transcripts
6. **Portal → Related concepts**: Add in Key Concepts Covered and Related sections

## Per-Lecture Ingestion Workflow

For each lecture transcript:

1. **Save transcript** to `transcripts/` following naming: `{date}_{source-slug}_{content-slug}-lecture.md`
2. **Create summary** in `raw/articles/` with model recommendations, key topics table, takeaways
3. **Update portal page** lecture table: replace `*pending*` with wikilinks to transcript + summary
4. **Update index.md**: Add transcript entry to Transcripts section
5. **Update log.md**: Append ingestion entry
6. **Commit and push**

### Lightning Lessons / Pre-Course Workshops

Many Maven courses offer free "Lightning Lessons" before the main cohort begins. These are **separate from the regular lecture schedule** and need their own section in the portal page:

```markdown
## Lightning Lessons (Pre-Course Workshops)

Free, standalone workshops offered before the main course cohort begins.

| Date | Lightning Lesson | Resources |
|------|-----------------|-----------|
| <date> | [[raw/articles/<summary>\|<Title>]] (<Instructor>) | [[transcripts/<notebook>\|Notebook]] · [GitHub](<url>) · [Maven](<url>) |

### Lightning Lesson N: <Title>
<1-paragraph summary with bullet list of key topics>
**Key takeaway:** <one-line insight>
```

- Place the Lightning Lessons section **before** the regular Lecture Schedule section
- Each Lightning Lesson gets its own raw article summary + transcript (notebook walkthrough)
- Include links to both the Maven page AND the GitHub notebook source
- **Pitfall**: Don't confuse Lightning Lessons with regular lectures. Verify the lecture type from the Maven page URL pattern (`/p/<slug>/` = Lightning Lesson, course page = regular lecture).
- **Pitfall**: Don't assume the 2nd Lightning Lesson's instructor/topic from partial Maven page data. Always verify with the user if unsure.

## Pitfalls
- **Don't create portal pages in entities/**: Portal pages are `type: concept`, not `type: entity`. They belong in `concepts/`.
- **Don't forget ecosystem context**: A portal page without ecosystem context is just a content listing. The context explains WHY the course matters and connects it to the broader wiki graph.
- **Update BOTH directions**: Creating a portal page without updating the instructor entity pages leaves the graph one-directional.
- **Lecture table must be maintained**: Each transcript ingestion MUST update the portal page's lecture table. Don't leave `*pending*` entries after the transcript exists.
- **Date corrections propagate**: If the user corrects course dates, update ALL files: portal page, raw overview article, lecture table, and any transcript frontmatter.
- **Companion repos**: Course notebooks may live in a separate repo from the main course repo (e.g., `agent-engineering` for notebooks vs `research-agent-lesson` for MCP server + example reports). Always verify the canonical notebook URL with the user or check both repos. Reference both repos in Companion Resources.
- **Source-slug is X handle, not real name**: Transcript filenames use the instructor's X/Twitter handle (e.g., `willccbb` for Will Brown), NOT their real name. This is a common mistake — check `transcript-ingestion.md` naming convention.

### Tag Pre-Flight for Lecture Transcripts

When writing frontmatter for lecture transcripts and summaries, domain-specific tags are the most common commit blocker. The pre-commit hook checks ALL tags against SCHEMA.md's taxonomy.

**Workflow:**
1. Before writing frontmatter, `grep` SCHEMA.md for each planned tag: `grep -i "keyword" wiki/SCHEMA.md`
2. Common lecture-related traps:

| Invented tag | Correct SCHEMA.md tag | Notes |
|---|---|---|
| `reward-engineering` | (add to SCHEMA.md, Models section) | New domain — add next to `reward-hacking` |
| `rl-infrastructure` | `ml-infrastructure` | Under Infrastructure taxonomy |
| `ppo` | (add to SCHEMA.md, next to `grpo`) | Standard RL algorithm |
| `prompt-engineering` | `prompting` | Shorter canonical form |
| `agent-sandboxing` | `sandbox` | Under Models taxonomy |
| `async-processing` | `async-agents` | Under AI Agents taxonomy |

3. If a tag doesn't exist, decide: (a) use an existing canonical synonym, or (b) add it to SCHEMA.md before committing.
4. After adding tags to SCHEMA.md, the commit must include both the SCHEMA.md change AND the transcript files in the same `git add` + `git commit` cycle.

### Wikilink Target Validation

Before creating wikilinks to entity/concept pages in transcripts and summaries, verify target pages exist. Transcripts often reference related projects, tools, and organizations that may not have wiki pages yet.

**Workflow:**
1. `search_files(pattern="page-slug", path="~/wiki", target="files")` for each wikilink target
2. If target doesn't exist: either create a stub page, or use a raw article link instead (e.g., `[[raw/articles/2025-04-14_corbt_art-trainer-new-rl-trainer]]` instead of `[[concepts/art-agent-reinforcement-trainer]]`)
3. Existing entity pages may use different slugs than expected — always search broadly (e.g., `search_files(pattern="*corbitt*", target="files")` to find `entities/kyle-corbitt.md` AND `concepts/corbett-kyle-corbitt.md`)

### Wikilink Escaping in Patch Tool

When using `patch` to edit markdown tables containing wikilinks with pipe characters (`|`), the patch tool may double-escape them (`\\|` → `\\\\|`). This corrupts the wikilink rendering.

**Fix:** After patching a markdown table with wikilinks, immediately `read_file` the affected lines and check for `\\|` corruption. If present, do a second `patch` to fix `\\\\|` → `\\|`.

### Notebook Fetching and Storage

Course companion notebooks hosted on GitHub should be saved alongside lecture content:

```
# Save notebook to raw/articles/
curl -sL "<raw-github-notebook-url>" -o ~/wiki/raw/articles/<notebook-name>.ipynb

# Reference in transcript and summary frontmatter:
notebook: https://raw.githubusercontent.com/.../<notebook>.ipynb
```

The notebook URL goes in both the transcript's YAML frontmatter AND the portal page's Companion Resources table. The Lecture Schedule table links to the summary article, not the notebook directly — the notebook link belongs in the Lesson Summary section below the schedule.
