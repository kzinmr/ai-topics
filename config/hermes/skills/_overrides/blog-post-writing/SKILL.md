---
name: blog-post-writing
description: "Write and iteratively refine Japanese-language technical blog posts — wiki research first, humanizer review, multi-round user feedback integration."
version: 1.0.0
metadata:
  hermes:
    tags: [blog, writing, japanese, humanizer, wiki-research, creative]
    category: creative
    related_skills: [humanizer, raw-article-filename-policy, llm-wiki]
---

# Blog Post Writing

Write and iteratively refine Japanese technical blog posts using wiki knowledge as the primary source, Humanizer for review, and multi-round user feedback for structural direction.

## When to Use

Load this skill when the user:
- Asks to write a blog post, essay, or article on a technical AI topic
- Requests a "活き活きとした" (lively) or "深掘り" (deep-dive) blog post
- Provides multi-round structural feedback ("reduce emphasis on X," "fold Y into Z," "add section on W")
- Wants Japanese output

## Core Workflow

### Phase 1: Research

1. **Wiki first.** Search `~/ai-topics/wiki/` for relevant concepts, entities, comparisons. Prioritize wiki knowledge over web search. The wiki has deep, cross-referenced content that produces richer arguments than surface-level web results.

2. **Web fallback.** If the wiki lacks support for a specific claim, use `web_search` and `web_extract` to find authoritative sources. Cite them.

3. **Build the argument structure.** Before writing, identify:
   - The core thesis (one sentence)
   - 3-5 supporting arguments drawn from wiki concepts
   - The narrative arc (chronological? layered? compare-contrast?)

### Phase 2: Writing

4. **Write to `blog/`.** Save files to `~/ai-topics/blog/{YYYY-MM-DD}_{author}_{short-slug}.md`. Do NOT save to `wiki/raw/articles/` — that directory is for externally-sourced article scrapes only.

5. **Frontmatter.** Include `title`, `date`, `author`, `tags`, `sources` (wiki pages + external URLs), and optional `series` / `series_index` if part of a multi-post sequence.

6. **Japanese voice.** Write in natural Japanese. Mix registers (である調 + だ調 + occasional です・ます for reader address). Vary paragraph length. Avoid the "AI triple combo" — `——` in every header + `**bold**` everywhere + rigid である調.

### Phase 3: Humanizer Review

7. **Always run through humanizer.** After writing, load the `humanizer` skill and apply BOTH the 29 English patterns AND the Japanese-specific patterns (J1-J8). The humanizer skill already contains a comprehensive Japanese section.

8. **Two-pass review:**
   - Pass 1: Draft rewrite with all pattern fixes
   - Pass 2: "What makes this so obviously AI generated?" → fix remaining tells

9. **Save the humanized version** as a separate file or overwrite, depending on user preference. Default: save as separate `-humanized.md` variant for comparison.

### Phase 4: User Feedback Integration

10. **Multi-round structural feedback is normal.** The user will often give layered feedback:
    - "Reduce emphasis on X, it's too prominent"
    - "Fold section Y into Z, it's too detailed as standalone"
    - "Add a new angle on W"
    - "Remove section Q entirely, it doesn't fit the thesis"

11. **Treat each round as structural editing, not full rewrite.** Preserve the voice you've established. The user is steering content and emphasis, not rejecting tone. Apply targeted patches rather than rewriting from scratch.

12. **When the user questions a logical leap** ("主張に飛躍がある"): verify the wiki source more carefully, identify the missing logical steps, and make the chain explicit. This is a content quality signal, not a voice signal.

13. **When the user proposes a new angle** without deep background ("深い考えがあるわけではないので、まず考察を行なって"): research the angle using wiki + web, present the analysis to the user for validation, then weave it into the post.

## File Management

### Directory
```
~/ai-topics/blog/
  2026-05-08_hermes_tradeoff-v1.md         # initial draft
  2026-05-08_hermes_tradeoff-humanized.md   # after humanizer pass
  2026-05-08_hermes_tradeoff-v2.md          # after structural revision
  2026-05-08_hermes_tradeoff-v3.md          # after further revision
  2026-05-08_hermes_prediction-vs-valuation.md  # follow-up post
```

### Naming Convention
`{YYYY-MM-DD}_{author}_{short-slug}.md`

- `author` = `hermes` for agent-authored posts
- `short-slug` = 2-4 word kebab-case summary of the topic
- Versioned files append `-v2`, `-v3`, etc. to the slug

### Commit
After writing or editing, always commit + push:
```
cd ~/ai-topics && git add blog/ && git commit -m "blog: <summary>" && git push
```

## Series Posts

When writing a multi-post series:
- Add `series: <series-slug>` and `series_index: <N>` to frontmatter
- Cross-reference earlier posts with relative links
- The first post establishes the thesis; follow-ups explore orthogonal dimensions or deeper dives

## Pitfalls

- **Don't save to `wiki/raw/articles/`.** That directory is for external article scrapes. Blog posts go to `blog/`.
- **Don't over-use the humanizer.** The goal is natural writing, not sterile anti-AI writing. Japanese technical blogs are structurally more organized than English blogs — numbered sections and clear transitions are normal and should be preserved.
- **Don't silently rewrite on user feedback.** Show what changed. Use targeted `patch` when possible; use `write_file` for full rewrites only when the structure fundamentally changes.
- **Don't treat every user comment as a full-structure rejection.** "Reduce emphasis on X" means reduce, not delete. "Fold Y into Z" means merge, not rewrite both.
- **Verify wiki claims before citing them.** If a wiki concept page has gaps or errors, note them to the user rather than propagating them into the blog.
