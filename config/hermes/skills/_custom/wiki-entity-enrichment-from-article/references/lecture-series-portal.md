# Lecture Series Portal Page Pattern

When ingesting a multi-lecture course or training series (e.g., Maven courses, workshop series), create a **portal page** in `concepts/` that serves as the central hub for all lectures in the series.

## When to Use This Pattern

- Cohort-based courses with multiple lectures (Maven, Coursera, etc.)
- Workshop series with 3+ sessions
- Any lecture series where transcripts will be added incrementally
- Courses backed by companies/platforms that have entity pages in the wiki

## Portal Page Structure (`concepts/`)

```yaml
---
title: "<Course Title>"
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - <topic tags>
  - education
  - <relevant technique tags>
sources:
  - raw/articles/YYYY-MM-DD_<source>_course-overview.md
  - <course URL>
---
```

### Required Sections

1. **Header**: Course title, platform link, instructors (as wikilinks), schedule, price
2. **Course Overview**: 2-3 sentence description + learning objectives table
3. **Instructors**: Brief bios with wikilinks to entity pages
4. **Companion Resources**: Table of GitHub repos, slides, etc.
5. **Lecture Schedule**: Table with Date | Lecture | Transcript columns
   - Use `*pending*` for lectures not yet ingested
   - Update rows as transcripts are added
6. **Key Concepts Covered**: Links to related concept pages
7. **Comparison with Similar Courses**: Optional but useful for context
8. **Ecosystem Context**: See below
9. **Related**: Wikilinks to instructors, platforms, concepts

### Ecosystem Context Section (MANDATORY for platform-backed courses)

Many lecture series are **strategic onboarding paths** for products/services. The portal page MUST include an "Ecosystem Context" section that explains:

```markdown
## Ecosystem Context

This course is not just educational content — it is a **strategic onboarding path**
into the [ecosystem name] built around [key platforms]:

### [Platform A] ↔ [Core Product]
[Entity link] provides [what]. The [product] is the core building block.
The course teaches the **background knowledge needed to use [product] effectively**:
[specific skills taught]. Students receive [credits/incentives].

### [Platform B] ↔ [Service]
[Entity link] provides [what]. The course teaches the **[fundamentals]
that [Platform B]'s customers need** to [use the service effectively].

### Connection to the Broader Ecosystem
- [[related-concept-1]] — [how it relates]
- [[related-concept-2]] — [how it relates]
```

## Triangle Linking Pattern

When a course is backed by platforms/services, create **bidirectional links** between:

```
Course Portal ←→ Platform Entity ←→ Related Concept
     ↕                                      ↕
     └──────────────────────────────────────┘
```

1. **Portal → Platform**: In "Ecosystem Context" and "Related" sections
2. **Platform → Portal**: In the platform entity's "Related Pages" section
3. **Portal → Concept**: In "Key Concepts Covered" and "Ecosystem Context"
4. **Concept → Portal**: In the concept page's "Related Course Materials" section

### "Related Course Materials" Section (for concept pages)

Add to concept pages that are substantively covered by a course:

```markdown
## Related Course Materials

- **<Course Title>** (<Platform>, <Instructor>) — <Brief description>.
  Lecture transcripts in wiki:
  - [[transcripts/...|Lecture 1: Topic]]
  - [[transcripts/...|Lecture 2: Topic]]
```

## Raw Article for Course Metadata

Save course metadata to `raw/articles/YYYY-MM-DD_<source>_course-overview.md`:

```yaml
---
title: "<Course Title> (Course Overview)"
date: YYYY-MM-DD
date_ingested: YYYY-MM-DD
source: <course URL>
type: course-overview
tags:
  - <topic tags>
  - education
---
```

Include: platform, instructors, schedule, price, description, learning objectives, target audience, companion resources, included credits.

## Maven Course Page Extraction

Maven course pages are SPAs (Next.js). Course metadata is embedded in:
```html
<script id="__NEXT_DATA__" type="application/json">
```

Extract from `course` and `pageProps` objects:
- `course.name`, `course.description`
- `course.instructor_infos[].name`, `.bio_html`
- `pageProps.sections[]` — find `schedule`, `overview`, `topics`, `faqs`
- `pageProps.course_schedule` — dates and times

Use `curl -sL <url> | grep -o '__NEXT_DATA__.*</script>'` then parse JSON.

## Lightning Lessons / Pre-Course Workshops

Some courses (especially Maven) offer **Lightning Lessons** — free, standalone workshops before the main cohort begins. These are different from regular lectures:

- They are typically shorter (~60-90 min) and focus on a single topic
- They may be taught by different instructors than the main course
- They have their own Maven URLs (e.g., `maven.com/p/<id>/<slug>` vs the course URL)
- They may have companion GitHub repos separate from the main course repo

### Portal Page Treatment

Add a **Lightning Lessons** section to the portal page, **before** the main Lecture Schedule:

```markdown
## Lightning Lessons (Pre-Course Workshops)

Free, standalone workshops offered before the main course cohort begins.

| Date | Lightning Lesson | Resources |
|------|-----------------|-----------|
| <date> | [[raw/articles/...|Title]] (Instructor) | [[transcripts/...|Notebook]] · [GitHub](url) · [Maven](url) |
| TBD | Title (Instructor) | *pending* · [Maven](url) |
```

### File Naming for Lightning Lessons

Lightning Lessons follow the same naming convention but use a descriptive slug:
- `raw/articles/YYYY-MM-DD_<source-slug>_<topic>-lightning.md`
- `transcripts/YYYY-MM-DD_<source-slug>_<topic>-notebook.md`

When a lesson walks through a Jupyter notebook (not a spoken transcript), the transcript file is a **notebook walkthrough** — structured by notebook sections rather than timestamps.

## Pitfalls

- **Don't create individual lecture concept pages** — use `transcripts/` for lectures, `concepts/` only for the portal
- **Date correction**: Always verify course dates with the user; SPA metadata may show future/current year incorrectly
- **Ecosystem context is mandatory** — don't skip it for platform-backed courses. The user explicitly requires this for proper wiki graph connectivity
- **Tag taxonomy**: Check SCHEMA.md before using tags. Known pitfalls:
  - `agent-engineering` → use `ai-agent-engineering`
  - `rl-post-training` → use `agent-training`
- **Transcript frontmatter**: Use `type: transcript` (not `type: article`), add `transcript` tag
- **Bidirectional linking**: Always create links in BOTH directions (portal ↔ entity, portal ↔ concept)
- **Lecture schedule table**: Update the portal page table when adding new transcripts
- **Subagent quality variance**: When delegating raw article + transcript creation in parallel, the raw article (summary) may be too generic if the subagent lacks the specific source material (Maven page content, notebook code) in its context. The transcript (code-heavy) tends to be higher quality because it has the actual notebook content. Always verify the raw article has specific details (Maven URL, repo link, video chapters, key code patterns) and rewrite if it's too abstract.
