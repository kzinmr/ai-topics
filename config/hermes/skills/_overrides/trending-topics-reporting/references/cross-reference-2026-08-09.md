# Cross-Reference Worked Example — 2026-08-09

Daily trending-topics run. **7th consecutive no-active-crawl day** — volume-based skip is now the stable default: blogwatcher DB yielded 91 articles (3d) with clear event clusters, so no full HN discovery sweep; 10 targeted HN Algolia point-score queries calibrated ★ ratings.

## Day shape

- Prior reports read: 8/6, 8/7, 8/8 (the anchor). All three are dense; dedup required grepping all three for candidate entity names (`grep -n "Muse" trending-topics-2026-08-0*.md`) before declaring anything fresh.
- Morning pipelines ingested most candidates before 12:00 UTC (blog-wiki-ingest 4 takes: claude-code auto mode, discovery-loop funding, muse-spark, seangoedecke-com; newsletter-wiki-ingest: deepseek price reversal). `head -90 wiki/log.md` was the fastest "already done" check — 4 of 7 final actions were ✅ before the report was written.

## Topic selection decisions

1. **Oracle/OpenJDK AI-code ban (HN 530pts/374c)** — fresh, NOT in any prior report despite being wiki-covered. **Key pattern: "wiki-ingested ≠ reported"** — `concepts/ai-generated-code-policies.md` already had it (dreaming 8/8 spot-check) but no daily report surfaced the 530pt story. A major HN story can be wiki-covered and report-missed simultaneously; when that happens, the report should still carry it (it's the reader-facing surface). Ranked #1 ★★★★★.
2. **DeepSeek price hike reversal** — newsletter subject "Who Is Really Paying for Cheap Intelligence" (Superintel+) was the signal; blogwatcher DB had only low-point HN hits (SCMP 30pts). Already ingested into `entities/deepseek.md` by newsletter-wiki-ingest. Kept as ★★★★☆ because it's the price-war REVERSAL — a genuine narrative turn, not incremental. **Newsletter subject lines remain the primary discovery channel for economics stories RSS under-weights.**
3. **ByteDance 10T model** — newsletter subject "TikTok's Owner Builds a Secret AI Giant on Mythos-level" → FT exclusive (8/7) + Ars Technica (8/9). HN points 2-4 (nearly zero) BUT FT+Ars+newsletter overlap = authoritative single-source depth → ★★★★☆. **Low-HN + high-authority overlap heuristic applied again** (same as 7/19 Apple-vs-OpenAI pattern). Arguably the most important story of the day that HN entirely ignored.
4. **Meta Muse Code + Spark 1.2** — launch cluster (research.meta.ai + daringfireball + AINews). Already ingested ✅. This is the second Meta agent-product item after the 8/6 Muse Spark hack story — treat as new product event, not a re-report of the hack.
5. **AI Engineer Conference second wave** — 9 talks 8/6-8/9 (routing, harness, CCA exam, local models). 8/3 report already covered the conference as cluster #5; this is a NEW wave of talks → new cluster topic. Applied conference-cluster rule (one topic, not 9).
6. **OpenAI motion to dismiss Apple suit** — already in `events/openai-apple-conflict-2026.md` ✅. ★★★☆☆, continuation of 8/5 conflict topic.
7. **Sean Goedecke resistance essay** — already ingested ✅. ★★★☆☆ culture/philosophy item.

## Techniques that worked

- **`head -90 wiki/log.md` + `grep` of prior reports** = complete dedup in one read; faster than per-page frontmatter checks.
- **Blogwatcher Query 3a + 3b split** worked as documented; 3b caught ByteDance-adjacent items via "essay/announce" keywords that 3a missed.
- **Newsletter subject scan** (`ls -t wiki/raw/newsletters/`) surfaced 2 of the top 3 stories (DeepSeek price, ByteDance). The newsletter files themselves are link-dumps (beehiiv redirects) — subject lines are the signal, always.
- **`_index.md` wikilink pitfall**: `[ -f wiki/concepts/coding-agents.md ]` returned MISS because the page is `concepts/coding-agents/_index.md`. Fix: for category-looking MISS paths, check `_index.md` before declaring broken; wikilink as `[[concepts/coding-agents/_index]]`.

## What was skipped

- OpenAI/HF Black Hat timeline (covered 8/8, events page updated 8/8)
- SpaceX 10GW SemiAnalysis (6pts/3c, weak AI relevance)
- App Store review times / Some New Data Centers (daringfireball minor)
- Meta $942M child-safety lawsuit (not AI-core)
- Sierra Voice Personas (no HN signal, minor product feature)

## Final shape

7 topics: 1×★★★★★ (Oracle/OpenJDK), 4×★★★★☆ (DeepSeek, ByteDance, Muse, AI Engineer), 2×★★★☆☆ (Apple dismiss, Goedecke). Wiki actions: 4 already done, 3 residual (open-source-ai, enterprise-ai-cost-management, bytedance/china-ai-industry stale pages — note the two China pages were stale at 6/22 and 5/26 respectively, a good "stale page" catch pattern).
