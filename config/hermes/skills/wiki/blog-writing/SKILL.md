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

1. Write the post to `blog/{filename}.md`
2. Update `wiki/log.md` with the new entry
3. Commit and push: `cd /opt/data/ai-topics && git add blog/ wiki/log.md && git commit -m "blog: <title>" && git push`

Active blog post outlines and research notes are kept in `references/` within this skill.
- `references/baudrillard-blog-outline.md` — In-progress structure for Baudrillard × AI blog post (2026-05-11).

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

## Pitfalls

### Session Reset in Discord Threads
When the user continues a blog post discussion across Discord sessions and you can't find the referenced draft/outline:
- **STEP 0 — Check skill references FIRST.** `skill_view(name='blog-writing')` returns a `linked_files` dict. If a reference file matches your topic (e.g., `references/baudrillard-blog-outline.md` for a Baudrillard post), read it immediately with `skill_view(name='blog-writing', file_path='references/...')`. Outlines and user feedback from prior sessions are saved here.
- If the reference file doesn't exist or doesn't contain the outline: **Ask early.** Don't burn 10+ tool calls on session_search + search_files + execute_code probing for a file that only existed in a prior session's memory.
- Demonstrate understanding of all feedback points, then ask for the file path or outline re-share.
- The canonical locations to check are `blog/` and `wiki/concepts/` (for concept pages that may serve as source material).
