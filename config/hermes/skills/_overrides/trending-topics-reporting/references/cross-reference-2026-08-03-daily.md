# Cross-Reference: 2026-08-03 (Monday daily run — weekly digest dedup + digest-miss hunt)

## Context

- Monday 00:00 UTC: `weekly-ai-digest-2026-08-03.md` published (covers 7/27→8/3).
- 12:00 UTC: this daily run. **First-time pattern**: the digest was created ~12h before the daily report, so the daily report's dedup anchor is the digest, NOT yesterday's daily.
- No active-crawl research note (4th consecutive day; volume-based skip is now the stable default).
- blogwatcher DB: 85 articles published / 190 discovered in last 3 days. AI Engineer conference = 16 talks/3d (conference cluster).

## What the report selected (7 topics) and why

| # | Topic | Strength | Why kept |
|---|-------|----------|----------|
| 1 | Qwen3.8-Max open-weight (8/3) | ★★★★★ | Post-digest (launched same morning), HN 683pts/339c, newsletter subject directly on it |
| 2 | OpenAI Astra math breakthrough (8/1) | ★★★★★ | **DIGEST MISS** — missed by BOTH 8/2 daily and 8/3 weekly digest; 8.4M X views, HN 459pts |
| 3 | Boris Cherny × Startup School (Opus 5, prompt-injection resistance, 80% sysprompt deletion) | ★★★★☆ | Fresh 8/2-8/3; HN 62pts; deep raw article available |
| 4 | Anyscale × Nscale $1.65B | ★★★★☆ | **DIGEST MISS** — Bloomberg 7/30, definitive agreement 8/3; low HN pts (2-7) but real M&A |
| 5 | AI Engineer conference cluster (MCP Apps/Tasks + Benchmaxxing) | ★★★☆☆ | Conference cluster rule: 16 talks = ONE topic, not 16 signals |
| 6 | GEMA v. Suno music copyright ruling | ★★★☆☆ | German court, 8/2; legal milestone; newsletter subject "music copyright bites back" |
| 7 | ElevenLabs IVR phone-tree navigation | ★★★☆☆ | Weak single-source signal; kept for voice-agent capability theme |

## Key techniques validated

### 1. Weekly digest is the dedup anchor on Mondays
- Read order: weekly digest (00:00) → yesterday's daily (8/2) → today's new signals.
- Sierra×Plaid was digest topic 7 (covered 00:00) — correctly skipped in daily despite the raw article existing.
- **Digest-miss hunt**: grep raw articles with `-mtime -2` on BOTH paths; if a raw file exists for a big-point story (Gary Marcus Astra essay `garymarcus.substack.com--p-openais-amazing-but-vastly-oversold--9b1f0537.md`, Simon Willison `2026-aug-1-ten-advances-in-mathematics`) but neither report covered it → digest miss → promote to ★★★★★.

### 2. log.md head-scan for "already done" detection (5/7 actions already executed)
`head -80 wiki/log.md` showed the morning's pipeline activity in one read:
- active-crawl (11:03): created `concepts/ai-productivity-gap`, `concepts/mu-tools-for-agents`; enriched `concepts/qwen-3-8` with Max section
- newsletter-wiki-ingest (11:00): created `concepts/gemini/gemini-robotics-2`, `concepts/ai-music-copyright`; enriched deepseek-v4
- blog-wiki-ingest (10:35): verified boris-cherny--claude-code-development, openai-astra, anyscale "already executed (commit 00b3e5ba)" — no redundant edits
- blog-triage (10:24): created `entities/openai-astra.md`
- llm-pricing-monitor (10:00): GPT-5.6-terra/luna price corrections

Residual recommendations were only stale pages: `entities/qwen.md` (updated 7/15), `entities/claude-code--capabilities.md` (updated 5/26). Verified with `[ -f wiki/<path> ]` before writing the table.

### 3. HN points grow between scrape and report
Qwen raw article embedded "623 pts"; live Algolia `search_by_date` showed 683pts/339c. Re-query at report time and cite live numbers.

### 4. Newsletter subject lines validate same-day stories
- 8/3 subject "If Developers Build on Chinese Open-Weight Models, Who Leads AI?" → confirmed Qwen3.8-Max as the day's central story (Chinese open-weight leadership angle).
- 8/2 subject "DeepSeek's Flash Sale, Google's Gemini Finds Its Feet, and Music Copyright Bites Back" → GEMA v. Suno is real; DeepSeek flash sale is price-war continuation (already covered, skip).

## Pitfalls re-confirmed
- AI Engineer = YouTube-only conference talks (no raw files) — DB titles + web search only; treat as cluster.
- Newsletter Substack redirect URLs unusable — use subject lines only.
- Wiki already has `entities/openai-astra` (created 8/3 by blog-triage) and `concepts/qwen-3-8` (updated 8/3) — do NOT recommend creating duplicates.
