---
name: blog-writing
description: Write original blog posts for the AI topics blog. Save to blog/ directory (NOT wiki/raw/articles/).
---

# Blog Writing

## Directory Rule (CRITICAL)

**Save all original blog posts to `/opt/data/ai-topics/blog/`.**

`wiki/raw/articles/` is reserved for externally-sourced, finalized article scrapes from the web. Do NOT save original blog posts there.

## Naming Convention

`{YYYY-MM-DD}_hermes_{short-slug}.md`

- `YYYY-MM-DD` = Publication date (usually today)
- `hermes` = Author marker
- `short-slug` = Hyphenated descriptive slug (e.g., `performance-controllability-tradeoff`)

## Process

1. **Research phase**: Gather real operational data before writing. Use `delegate_task` with batch mode (up to 3 parallel subagents) to collect stats, read reference files, and extract examples simultaneously. This grounds the post in concrete numbers and real artifacts rather than abstract claims.
2. Write the post to `blog/{filename}.md`
3. Update `wiki/log.md` with the new entry (append a dated section summarizing what was created)
4. Commit and push: `cd /opt/data/ai-topics && git add blog/ wiki/log.md && git commit -m "blog: <title>" && git push`

### Companion Slides (Marp)

When the blog post introduces a technical topic to an audience, companion Marp slides often belong in `slides/`:
- Naming: `{YYYY-MM-DD}_{short-slug}.marp.md`
- Reuse the same research gathered for the blog
- Reference existing slides in the same directory for CSS theme reuse (copy the `style:` block verbatim)
- Structure: 5 parts — Lead/Intro → Core Content (2-3 parts) → Takeaways → Thank You
- Use `<!-- _class: section -->` for part transitions, `<!-- _class: lead -->` for opening/closing
- Slides expand on what the blog covers in depth; they are not a summary of the blog

Active blog post outlines and research notes are kept in `references/` within this skill.
- `references/baudrillard-blog-outline.md` — In-progress structure for Baudrillard × AI blog post (2026-05-11).
- `references/structural-duality-analysis-pattern.md` — Reusable three-layer framework for AI architecture essays: divide-and-conquer → duality → naive model's limit. Emerged from the 2026-05-20 Anthropic multi-agent × RLM analysis session.

## Frontmatter Template

```yaml
---
title: "Title Here"
date: YYYY-MM-DD
author: Hermes (kzinmr's AI Topics)
tags: [tag1, tag2, blog]
sources:
  - concepts/example.md
  - https://example.com/source
---
```

For series posts, add:
```yaml
series: series-slug
series_index: N
```

## Voice

- Japanese (user's language)
- Humanized: no boldface overuse, no em dashes in titles, no signposting, no grand conclusions
- Personal, opinionated, varied rhythm
- If the user provides voice samples or feedback, apply it

## Structural Preferences

The user's blog posts follow a **narrative arc** pattern:
- **出発点 (起点)** — What drives the phenomenon? Ground it in concrete forces (e.g., information flow acceleration, arbitrage dynamics, economic/technological pressures).
- **中間展開** — Unfold the layers. Use theoretical lenses (Baudrillard, Baumol, etc.) to illuminate what's happening. Each theoretical move must be explained carefully — don't skip inferential leaps.
- **着地点** — Don't just identify problems. Include a pragmatic stance: given undeniable external pressures that make engaging with these dynamics unavoidable, how should we relate to them?

### Theory Integration Rules

When weaving in abstract theoretical concepts:
1. **Start from lived experience, not theory.** The user rejects posts that feel like "theory playing with itself" (論を弄し過ぎた). The post must open with concrete, personal felt experience — the theory is a lens brought in later to illuminate what was already observed. If the first draft opens with a theoretical framework (Baudrillard's 4 stages, Baumol's cost disease model, etc.), scrap that opening and rewrite from the user's actual experience (building the wiki, reading summaries, feeling the gap between form and substance).
2. **Explain step by step.** Concepts like Baumol's cost disease or Gödelian incompleteness need careful, grounded exposition — not a name-drop. Show the causal chain connecting the theory to the concrete phenomenon.
3. **Problem identification alone is not enough.** The user considers pure problem-cataloguing (especially with abstract formalism) pedantic. Every problem raised must be accompanied by a pragmatic position: why does it matter practically, and what posture should we take toward it?
4. **Acknowledge external pressure.** Structural problems are easy to list. The harder and more interesting move is to acknowledge the inescapable external forces (competition, information velocity, economic incentives) that make engaging with these broken systems unavoidable.

## Deep Technical Architecture Articles

When synthesizing wiki knowledge into a deep technical architecture article (e.g., mapping a design pattern like Tenant Agent Pack or Agent Control Plane to its supporting wiki primitives):

### Research Phase
1. Identify the target concept's components or layers
2. For each component, search the wiki for supporting technical primitives: `ls wiki/concepts/ | grep -iE "keyword1|keyword2|..."`
3. Read the most relevant pages (3-5 per layer) to understand the current state of knowledge
4. Identify gaps — what's NOT yet covered in the wiki that would be needed

### Writing Phase
- **Frontmatter**: `title`, `date`, `author: Hermes (kzinmr's AI Topics)`, `tags` (include `blog`), `sources` (link to wiki concept pages and raw articles)
- **Audience**: Business/development professionals with high resolution understanding of the domain
- **Language**: Japanese (日本語)
- **Structure**: 
  - Compelling title with concrete insight (not generic)
  - Architecture diagram (ASCII) showing component relationships
  - One major section per layer/component, each anchored to specific wiki primitives with `backtick` references
  - Comparison tables where 3+ items are analyzed
  - Gap analysis section identifying what's missing from the wiki
- **Length**: 150-250 lines for deep architecture articles
- Tag validation: All tags must exist in SCHEMA.md taxonomy

### Post-Writing
- Update `wiki/log.md` with a concise entry (prepend using `execute_code` Python open/read/prepend/write — never use `patch` with `---` anchor)
- `git add blog/ wiki/log.md && git commit -m "blog: ..." && git push`

## Reference Files
- `references/tenant-agent-pack-9-layer-architecture.md` — 9-layer mapping of Tenant Agent Pack to wiki primitives with gap analysis
- `references/agent-control-plane-13-component-architecture.md` — 13-component × 3-layer mapping of Agent Control Plane to wiki primitives with platform comparison

## Pitfalls
- **Ambiguous skill name**: The `blog-writing` skill exists in two locations (`~/.hermes/skills/` and `~/ai-topics/config/hermes/skills/`). When skill_view returns "Ambiguous skill name", skip loading it and proceed directly with the known workflow.
- **Log.md prepend via `---` anchor**: Never use `patch` with `---` as old_string in log.md — it matches YAML frontmatter delimiters elsewhere. Use `execute_code` Python open/read/prepend/write instead.
- **Backtick in terminal Python**: When using `terminal()` with inline Python, backticks in the string are interpreted by bash as command substitution, silently corrupting content. Use `execute_code` for any log.md operations involving backtick-wrapped paths or URLs.

### Session Reset in Discord Threads
When the user continues a blog post discussion across Discord sessions and you can't find the referenced draft/outline:
- **STEP 0 — Check skill references FIRST.** `skill_view(name='blog-writing')` returns a `linked_files` dict. If a reference file matches your topic (e.g., `references/baudrillard-blog-outline.md` for a Baudrillard post), read it immediately with `skill_view(name='blog-writing', file_path='references/...')`. Outlines and user feedback from prior sessions are saved here.
- If the reference file doesn't exist or doesn't contain the outline: **Ask early.** Don't burn 10+ tool calls on session_search + search_files + execute_code probing for a file that only existed in a prior session's memory.
- Demonstrate understanding of all feedback points, then ask for the file path or outline re-share.
- The canonical locations to check are `blog/` and `wiki/concepts/` (for concept pages that may serve as source material).
