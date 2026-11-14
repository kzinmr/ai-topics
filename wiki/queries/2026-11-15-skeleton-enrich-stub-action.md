---
title: "Skeleton enrichment run — 2026-11-15 (stub backlog: AI umbrella concepts cluster — 9 pages)"
type: query
created: 2026-11-15
updated: 2026-11-15
tags:
  - query
  - knowledge-management
sources: []
---

# Skeleton enrichment run — 2026-11-15

> Snapshot note from the `skeleton-enrich-daily` cron run (2026-11-15 19:0x UTC).
> The `status: skeleton` backlog remains **empty** (streak since 2026-10-17): frontmatter scans
> (`grep -rln "^status:[[:space:]]*skeleton"`) across `wiki/entities/` and `wiki/concepts/` return
> **0** live markers. As in the 2026-11-11/12/13 runs, productive action was taken on the
> highest-inbound-link `status: stub` subset — this time the **AI umbrella-concept cluster**
> suggested by the 2026-11-13 plan (robotics 8, embodied-ai 6, ai-coding-tools 5, generative-ai 5 inbound).

## Actions this run (9 enriched, 0 redirects, 0 net new pages)

| Page | Before | After |
|------|--------|-------|
| `concepts/tinygrad.md` | 268 B stub | ~4.6 KB — geohot's minimalist DL framework: lazy one-kernel fusion architecture diagram, backend codegen table, milestones (nanoGPT speedrun era), framework-landscape comparison, CUDA-moat framing; GitHub API verified 33,914★ MIT, active 2026-11-14 |
| `concepts/trey-grainger.md` | 272 B stub | ~3.3 KB — Searchkernel founder (GitHub-bio verified), ex-Lucidworks CAO/SVP, ex-Presearch CTO, Vectorize.io; *AI-Powered Search* + *Solr in Action*; Maven Search School course; relevance-engineering→RAG positioning |
| `concepts/ai-alliance.md` | 260 B stub | ~4.2 KB — thealliance.ai-scraped: two-nonprofit structure (501c3 Community / 501c6 Association), Common Corpus 2.3T tokens, SYNTH, Project Tapestry, GEO-Bench-2, NAIRR pilot; disambiguation table vs Open Secure AI Alliance |
| `concepts/robotics.md` | 268 B stub | ~3.3 KB — modern VLA stack diagram, layer table linking 10 existing wiki pages (cosmos-3, robostral, gemini-robotics-2, figure, jim-fan, enpire...), sim-vs-real / hierarchical-VLA / ChatGPT-moment debates |
| `concepts/embodied-ai.md` | 252 B stub | ~3.4 KB — embodiment-vs-video-proxy-vs-text-first position table, data pyramid, action representations, agent-stack mapping (harness=simulator) |
| `concepts/ai-coding-tools.md` | 264 B stub | ~4.2 KB — 3+1 generation timeline (completion→IDE→terminal/background→app builders), 2026 field map of ~20 tools with entity links, 5 differentiation axes, effectiveness-debate context |
| `concepts/generative-ai.md` | 252 B stub | ~3.9 KB — modality×architecture map table, unifying ideas (conditioning, AR–diffusion convergence, content→action), socioeconomic layer (labor, copyright, slop, bubble) |
| `concepts/vision-models.md` | 252 B stub | ~3.7 KB — CNN→CLIP→ViT→VLM→omni lineage table, 4 VLM design axes (encoder, resolution, grounding, reasoning), sub-categories (OCR, on-device, video, agent-vision), benchmark shift |
| `concepts/ai-education.md` | 260 B stub | ~4.2 KB — canonical curriculum table (cs231n, CS336, Karpathy Zero-to-Hero, Ng, fast.ai, Raschka, 3B1B, Husain), from-scratch pedagogy pattern, AI-as-tutor vs deskilling, credential disruption |

## Verification performed

- Git-history richness check: all 9 pages last touched 2026-08-15 (stub-era bulk commit) — no richer historical versions existed
- Live source verification: GitHub API (tinygrad 33,914★ MIT, pushed 2026-11-14; @treygrainger bio "Founder @searchkernel"), thealliance.ai homepage via Jina Reader, treygrainger.com about/career via Jina Reader
- All wikilinks machine-verified to resolve (`os.path.exists` sweep over every `[[...]]`): dead targets replaced (bitter-lesson→rich-suttons-bitter-lesson, system-one→system-one-models, ai-benchmarks→prose, spatial-intelligence/ai-content-detection→world-labs/ai-slop, coding-agents subtree paths qualified)
- Tags all pre-registered in SCHEMA.md taxonomy (robotics, embodied-ai, humanoid-robot, physical-ai, vision, vlm, multimodal, generative-ai, open-source, ai-infrastructure, gpu, information-retrieval, search, relevance, organization, nonprofit, ibm, ai-organization, education, ml-education, ai-educator, ai-coding, coding-agents, developer-tools, comparison, person, python, ai-industry, model)
- index.md: 9 description updates (stub placeholders → real summaries), 0 new entries, page count unchanged (3458)
- log.md entry prepended

## Remaining backlog

~407 `status: stub` pages remain. Next-run candidates: `elasticsearch`, `threat-modeling`, `compiler-explorer`, `searcharray`, `cohereio`, `ai-benchmarks/yourbench`, `open-source-sustainability` family, `mastodon`, `fuzzing`, plus entity-shaped stubs misplaced in concepts/ (`alex-hall`, `bozavlado`, `brainchop`, `hack-club`, `colin`, `jay-v`).
