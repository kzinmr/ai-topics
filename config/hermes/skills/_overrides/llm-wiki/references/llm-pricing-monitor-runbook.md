# LLM Pricing Monitor Runbook

Cron job `llm-pricing-monitor` (weekly Monday 10:00 UTC) fetches live pricing from 4 US providers and compares against `wiki/comparisons/llm-api-pricing.md`.

## Provider-Specific Fetch Quirks (Updated 2026-07-27)

### OpenAI
- **URL**: `https://developers.openai.com/api/docs/pricing`
- **Page type**: SPA with structured data arrays embedded in HTML (NOT `__NEXT_DATA__` JSON as of 2026-07).
- **How to extract**: Pricing data is in structured arrays embedded in the HTML, e.g. `[[0,"gpt-5.6-sol"],[0,5],[0,0.5],[0,6.25],[0,30]]` where the values are `[0, input], [0, cache_read], [0, cache_write], [0, output]`. The format is `[[0,"model_name"],[0,price1],[0,price2],[0,price3],[0,price4]]`. For batch pricing, a second table exists with similar format. Extract with: `grep -oP 'gpt-5[^"]*' /tmp/openai_pricing.html | sort -u` to find models, then grep for each model's surrounding context to get prices. Models with `(&lt;272K context length)` qualifier have separate (higher) pricing.
- **Fallback**: OpenRouter API `openrouter.ai/api/v1/models` for cross-checking.
- **Gotcha**: Long-context models (>272K) have separate pricing tiers — note the context qualifier. `gpt-5.4-cyber` has `-` for all prices (undisclosed). New specialized models (cyber, codex, search) may appear without announcement.

### Anthropic
- **URL**: `https://www.anthropic.com/pricing`
- **Page type**: Server-rendered HTML, pricing data embedded in page. **NOT a SPA** — `curl -sL` returns full pricing data.
- **How to extract**: `curl -sL` (needs `-L` for redirects — first request returns 301), parse embedded pricing from HTML
- **Gotcha**: Cache write = base + 25%, cache read = 90% discount. Batch = ~50% off. Models are grouped into sections: "Standard/Batch" (older: 4.5, 4.6, 4.7, 4.8) and "Latest" (Fable 5, Opus 5, Sonnet 5, Haiku 4.5). Multiple Opus variants (4.5, 4.6, 4.7, 4.8, 5) may coexist at identical pricing.

### Google
- **URL**: `https://cloud.google.com/vertex-ai/generative-ai/pricing`
- **⚠️ URL redirect**: As of 2026-06, redirects to `cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing`. MUST use `curl -sL` to follow redirect.
- **⚠️ `ai.google.dev` blocked**: The `.dev` TLD pricing page is blocked by security policy (returns minimal page). Always use the Cloud/Vertex AI URL.
- **Table structure quirk**: Newer models (Gemini 3.x) use **Global/Non-global** columns instead of ≤200K/>200K token threshold columns. Don't confuse them — the column position that says "≤200K" in older models contains "Global" pricing for 3.x models.
- **How to extract**: `curl -sL 'https://cloud.google.com/vertex-ai/generative-ai/pricing' -o /tmp/google_vertex.html`, then grep for model names and read surrounding table rows. Page is ~800KB.
- **Gotcha**: Gemini 3.x models may have separate audio input pricing (typically 2x text input). New model versions appear frequently (3.1→3.5→3.6 within months).

### DeepSeek
- **URL**: `https://api-docs.deepseek.com/quick_start/pricing`
- **⚠️ `platform.deepseek.com` returns 403**: The main platform URL is blocked by CloudFront. Use the API docs URL instead.
- **How to extract**: Small HTML page (~21KB), pricing embedded directly in readable text.
- **Gotcha**: `deepseek-chat` and `deepseek-reasoner` aliases being deprecated — check for alias→model mapping changes.

### Chinese Providers (Qwen, Xiaomi, Zhipu, etc.)
- No centralized pricing pages; use OpenRouter API or provider-specific docs
- Prices in CNY — convert at ~7.2 CNY/USD

## Fetch Commands (Copy-Paste)

```bash
# OpenAI
curl -s 'https://developers.openai.com/api/docs/pricing' -o /tmp/openai_pricing.html

# Anthropic
curl -sL 'https://www.anthropic.com/pricing' -o /tmp/anthropic_pricing.html

# Google (follow redirect)
curl -sL 'https://cloud.google.com/vertex-ai/generative-ai/pricing' -o /tmp/google_vertex.html

# DeepSeek
curl -s 'https://api-docs.deepseek.com/quick_start/pricing' -o /tmp/deepseek_pricing.html
```

## Comparison Methodology

1. **Fetch fresh** from live URLs (never use wiki/raw/articles/cache)
2. **Read wiki page** to get current recorded prices
3. **Diff model-by-model** against freshly fetched data
4. **If change detected**:
   - Patch only the changed values (use unique surrounding context)
   - Update `updated:` frontmatter date
   - Add Changelog entry with source URL and timestamp
   - If the change corrects a previous erroneous entry, fix that too
   - Update ALL affected derived tables (cache pricing, tier analysis, cost comparison, batch pricing, reasoning section)
   - Update `wiki/log.md`
5. **If no changes**: Report "No pricing changes detected" with verified model list
6. **Commit and push**: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: llm-pricing-monitor — [summary]" && git push`

## Sections to Update (8 total — from wiki-maintenance §2)

When adding a new model or changing a price, ALL 8 sections may need updating:
1. Main frontier/legacy table — new row with tier classification
2. Cache pricing section — cache read price row
3. Batch pricing section — batch in/out prices
4. Tier analysis section — blended cost, "why it wins" column
5. Cost comparison section (chat + code gen workloads) — standard and cached costs
6. Anthropic Cache Break-Even table (if Anthropic model)
7. Key Trends — if significant market shift
8. Changelog — always add entry

## Pitfalls

- **NEVER use `replace_all=True` on comparison table rows** — same model name appears in 5+ sections with different column layouts
- **Duplicate row trap**: When using `patch` to add a new row after an existing one, use the FULL surrounding context (2+ adjacent rows) to avoid accidentally inserting the row in the wrong position or duplicating an existing row. (2026-07-27: accidentally duplicated GPT-5.4-nano in cache table by matching only one row.)
- **Changelog flip-flop tracking**: Prices can change multiple times (e.g., o3-deep-research: $5/$20 → $10/$40 → $5/$20 → $10/$40). When a price reverts to a previous value, update the ORIGINAL changelog entry to note it was re-reverted, rather than adding a new standalone entry that might confuse the timeline.
- **Subagent data may be stale/cached**: Always verify subagent-reported prices by spot-checking the downloaded HTML directly
- **Google Global vs Non-global**: Don't mistake "Global" pricing for "≤200K" — they're different column semantics used in the same table position
- **Git commit message `&`**: If the message contains `&`, use single quotes
- **Existing wiki page instruction stale**: The `Monitoring & Update Policy` section in the comparison page references `__NEXT_DATA__` for OpenAI and `ai.google.dev` for Google — both are wrong. Update the wiki page instructions when you update this runbook.
