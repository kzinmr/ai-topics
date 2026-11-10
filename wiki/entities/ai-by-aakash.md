---
title: "AI by Aakash"
created: 2026-11-10
updated: 2026-11-10
type: entity
tags:
  - newsletter
  - evals
  - product-management
  - content-creator
  - ai-commentary
aliases:
  - AI by Aakash
  - aibyaakash
url: https://www.aibyaakash.com/
sources:
  - raw/newsletters/2026-11-10-spotify-s-claude-code-token-trick-tested-the-real-savings.md
---

# AI by Aakash

**AI by Aakash** is a weekly Substack newsletter (publication_id 5747120) by Aakash Gupta, a product-management-focused writer and cohort instructor ("Land a PM Job"). It is a curated weekly AI-news digest plus one long **deep dive** that runs hands-on experiments rather than only summarizing announcements. Tagline in each issue: "I follow the AI news so you don't have to."

## What makes it worth tracking

- **Independent replication of vendor claims.** The newsletter's signature move is to take a viral company engineering claim and re-run it on real code. Its Spotify Claude Code token-coverage piece took Spotify's reported 90% reduction, reproduced the setup on a 78K-line personal repo and Apache Commons Lang, and found the claim is **conditional**: −87% with Spotify's hook on a large monorepo with whole-file reads, but a **cost increase** in the Claude Code search-and-edit harness. See [[concepts/claude-code-token-cost-optimization]].
- **In-house model evals with published prompts and answers.** Gupta runs **8 product-management tasks** (A/B-test analysis, roadmap prioritization, PRD critique), each scored out of 10 by a blind judge, across frontier models at medium and max effort. Nov 2026 results: **Opus 5.5 (max) 9.2**, Fable 5.2, **GPT-6 Astra 8.4**, **Gemini 4 Argon 8.0** — all within 8.0–9.2, i.e. **a small frontier gap on PM work**, with max effort costing ~24× more for under half a point. He publishes one task with every model's answer and score, so the eval is checkable (methodology still single-evaluator, 8 tasks, unpublished rubric — treat as directional).
- **Qualitative model "vibes" separated from scores.** Fable at max: terse, decisive, catches buried facts. Opus: double-checks its own arithmetic. GPT-6 Astra: precise but hedges. Gemini 4 Argon: runs long but makes the plain call. Useful as a practitioner's model-selection signal alongside the index scores.
- **Weekly news round-up** that is dense enough to be a discovery source for [[concepts/recursive-self-improvement]], [[concepts/semianalysis-gdpx]] and model-release tracking.

## Positioning

Gupta is primarily a **product-management educator** (PM cohorts, Ctrl Alt Podcast at Dreamforce appearance, LinkedIn-dominant distribution — his Spotify post drew 3,757 likes). The newsletter's technical credibility rests on the replicated experiments and published eval artifacts rather than on ML research credentials; weight its conclusions accordingly and prefer the underlying primary source when one exists.

## Related

- [[entities/aakash-gupta]] — the author's person page
- [[concepts/claude-code-token-cost-optimization]] — the newsletter's main Nov 2026 deep dive
- [[concepts/evaluation/ai-evals]] — context for the private PM evals
- [[concepts/semianalysis-gdpx]] — reported by the newsletter

## Sources

- https://www.aibyaakash.com/ — newsletter archive
- ["Spotify's Claude Code Token Trick, Tested: The Real Savings"](https://www.aibyaakash.com/p/spotifys-90-trick), Nov 9, 2026. Raw: `raw/newsletters/2026-11-10-spotify-s-claude-code-token-trick-tested-the-real-savings.md`
