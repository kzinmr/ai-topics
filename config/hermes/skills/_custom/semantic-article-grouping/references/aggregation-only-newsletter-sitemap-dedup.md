# Aggregation-Only Newsletter Mentions vs Sitemap Originals

**Validated**: June 30, 2026 — AINews "not much happened today" linked Cognition Devin Fusion.
Sitemap-monitor (06:00 UTC) had already scraped `raw/articles/2026-06-29_cognition-devin-fusion-multi-model-harness.md`.

**Pattern**: A roundup newsletter (AINews, The Signal, etc.) links to a company-blog or research-lab article whose original source was already captured by the sitemap-monitor pipeline earlier the same day. The newsletter adds zero editorial value — just a 1-2 line summary from the blog post's abstract.

**When to use**: Any newsletter topic whose newsletter body is a 1-2 line summary from the original source's abstract, with no additional data, benchmarks, or editorial framing. The tell is visible in the newsletter post body around each linked topic.

**Action**: Skip — not reference. The sitemap-monitor dedup section in the main skill already covers model-release announcements; this extends the same logic to any company-blog or research-lab article aggregated without independent analysis.

**Distinction from genuine references**: A newsletter mention that adds context, comparison, or editorial framing qualifies as a reference (downgrade take → reference). A link-only mention with no added value → skip.
