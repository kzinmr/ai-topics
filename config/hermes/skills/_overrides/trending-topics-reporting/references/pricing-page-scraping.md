# Pricing Page Scraping Reference

> **Policy**: Always fetch live data from provider pricing pages. Never use wiki cache, raw articles, or stale snapshots as source of truth.

## Provider Fetch Commands

### OpenAI (Astro SPA — NOT Next.js)

The OpenAI pricing page switched from Next.js to **Astro** (v6.0.4+) in mid-2026. There is NO `__NEXT_DATA__` JSON. The pricing data is embedded in Astro island hydration data as inline arrays.

**Save to file first** (tirith blocks `curl | python3` pipes):
```bash
curl -s 'https://developers.openai.com/api/docs/pricing' -o /tmp/openai_pricing.html
```

**Extract model pricing** — the data appears as `[0,"model-name"],[0,input],[0,cached],[0,output]` tuples in the HTML:
```bash
python3 << 'PYEOF'
import re
with open('/tmp/openai_pricing.html') as f:
    html = f.read()

pattern = r'\[0,&quot;([\w\-\.]+)(?:\s*\([^)]*\))?\&quot;\],\[0,([\d.]+|null)\],\[0,([\d.]+|null|\&quot;\&quot;)\],\[0,([\d.]+|null)\]'
matches = re.findall(pattern, html)
seen = set()
for m in matches:
    model, inp, cached, out = m
    if model in seen: continue
    seen.add(model)
    inp_s = f"${float(inp):.2f}" if inp != 'null' else '—'
    cached_s = f"${float(cached):.2f}" if cached not in ('null', '&quot;&quot;') else '—'
    out_s = f"${float(out):.2f}" if out != 'null' else '—'
    print(f"{model:<30} {inp_s:>10} {cached_s:>10} {out_s:>10}")
PYEOF
```

**Key patterns in the Astro HTML**:
- Text token pricing: `[0,&quot;gpt-5.5&quot;],[0,5],[0,0.5],[0,30]` → Input $5.00, Cached $0.50, Output $30.00
- Long context pricing: model name includes `(<272K context length)` suffix
- Pro models (`-pro`) typically have no cached pricing (`null`)
- Empty string `&quot;&quot;` for cached = not offered (distinct from `null`)
- **4-value tuple trap (observed 2026-11-02)**: GPT-6-era rows carry FIVE values `[input, cached, cacheWrite5m, output, ...]` (cache write inserted), so the 4-group regex silently truncates output (e.g. gpt-5.6-sol showed output $5.00 instead of $20.00). Do not trust the quick regex for new generations — re-verify any suspicious price by dumping the raw tuple: `re.finditer(re.escape(model), html)` and print `html[m.start():m.start()+300]`. The tier tabs (Standard/Flex/Fast/Ultrafast = 1×/0.5×/2×/6×) each repeat the model list — dedupe and identify the tier by the ratio pattern.

**Alternative quick extraction** (model names only, for verification):
```bash
grep -oP 'gpt-5[\w.\-]*|o3[\w\-]*|o4[\w\-]*' /tmp/openai_pricing.html | sort -u
```

**Dollar amount frequency** (spot-check for unexpected prices):
```bash
grep -oP '\$\d+[\d.]*' /tmp/openai_pricing.html | sort | uniq -c | sort -rn | head -20
```

**Pitfall**: The page includes models not on the standard pricing table (codex variants, image models, audio models, chat-latest aliases). Filter for the models you're tracking.

### Anthropic — Two Pages

**Option A: Pricing page** (consumer-facing, Webflow):
```bash
curl -sL 'https://www.anthropic.com/pricing' -o /tmp/anthropic_pricing.html
```
This redirects to `claude.com/pricing` (Webflow). Content is heavily JS-rendered. Limited extraction via curl.

**Option B: Docs page** (developer-facing, Next.js RSC) — **preferred for model/pricing data**:
```bash
curl -sL 'https://docs.anthropic.com/en/docs/about-claude/models' -H 'User-Agent: Mozilla/5.0' -o /tmp/anthropic_docs.html
```
This page contains the official model comparison table with pricing. Extract with:
```bash
python3 << 'PYEOF'
import re
with open('/tmp/anthropic_docs.html') as f:
    html = f.read()
clean = re.sub(r'<[^>]+>', '\n', html)
lines = [l.strip() for l in clean.split('\n') if l.strip()]
for i, l in enumerate(lines):
    if any(kw in l.lower() for kw in ['$', 'pricing', 'input mtok', 'output mtok']):
        context = lines[max(0,i-2):i+3]
        for c in context:
            print(c)
        print("---")
PYEOF
```

**Key data points available on the docs page**:
- Model comparison table: Feature / Claude Fable 5 / Claude Opus 4.8 / Claude Sonnet 5 / Claude Haiku 4.5
- Pricing row: `$10 / input MTok` / `$50 / output MTok` etc.
- Introductory pricing footnotes (e.g., "Introductory pricing of $2/$10 per MTok applies to Claude Sonnet 5 through August 31, 2026")
- Context window sizes, max output tokens, extended thinking support
- New model announcements (e.g., Claude Mythos 5)

**Best extraction (observed 2026-11-02)**: the rendered HTML tables are thin, but the page embeds a `ModelComparisonSheet` RSC payload with a `models:[...]` array carrying machine-readable pricing per model: `{"id":"claude-opus-5-5",...,"pricing":{"inputPerMTok":4,"outputPerMTok":20,"cacheWrite5mPerMTok":5,"cacheWrite1hPerMTok":8,"cacheReadPerMTok":0.2},"releasedOn":"2026-09-22","contextWindowTokens":1000000,"maxOutputTokens":128000}` — plus `pricingLines` and `cacheReadExceptions` (multiplier vs base input, e.g. 0.025× for Fable/Mythos, 0.05× for Opus/Sonnet). Grep for `"inputPerMTok"` rather than stripping tags; it gives exact cache-write 5m/1h splits and release dates that the visible table omits. The `www.anthropic.com/pricing` page (redirects to claude.com, Webflow) yields almost nothing via curl (1.3MB, no model names) — don't waste time on it.

### Google — Vertex AI table parsing

The Vertex pricing page renders tab-tier rows (Standard/Priority/Flex/Batch × Global/Non-global). Grep the tag-stripped text around each `Gemini <name>` token for `Input ... Global $X ... Text output ... Global $Y` patterns. Watch for **promo tables with dated sub-headers** — e.g. "Gemini 4 Argon* through November 30, 2026 → $2/$10" followed by a separate "Starting December 1, 2026 → $4/$20" row; capture BOTH the current price and the step-up date, and put the date in the wiki footnote. Non-global endpoints are a uniform 1.1× Global.

### Model generation drift (the big one, 2026-11-02)

A weekly monitor can be 2+ generations stale if runs were skipped: the 08-24 snapshot predated the entire OpenAI GPT-6 family, Anthropic Claude 5.5 generation, and Gemini 4. When OpenRouter shows `gpt-6*`/`claude-*-5-5`/`gemini-4-*` ids absent from the wiki frontier tables, this is a frontier reorganization, not a price tweak — add new rows at the top of the US/China frontier tables, re-tier old flagships to "prev gen", fix lapsed intro promos (an expired promo like Sonnet 5's $2/$10 must move to standard list price with a † footnote), and rewrite the promo footnote block with current expiry dates. Save verbatim scrape evidence to `wiki/raw/articles/YYYY-MM-DD_<provider>-pricing-scrape.md` (with source URLs + fetched_at frontmatter) and cite those notes in the Changelog rows.

### Google — Use Vertex AI (NOT ai.google.dev)

**`ai.google.dev` is blocked by tirith** as "lookalike TLD" (`.dev` TLD). Use the enterprise pricing page instead:
```bash
curl -sL 'https://cloud.google.com/vertex-ai/generative-ai/pricing' -o /tmp/google_pricing.html
```

**Alternative**: OpenRouter API (see below) for quick verification of Google model prices.

### DeepSeek

Use the API docs page (NOT `platform.deepseek.com` which returns CloudFront 403):
```bash
curl -sL 'https://api-docs.deepseek.com/quick_start/pricing' -o /tmp/deepseek_pricing.html
```

Extract pricing:
```bash
python3 << 'PYEOF'
import re
with open('/tmp/deepseek_pricing.html') as f:
    html = f.read()
clean = re.sub(r'<[^>]+>', '\n', html)
lines = [l.strip() for l in clean.split('\n') if l.strip()]
for i, l in enumerate(lines):
    if any(kw in l.lower() for kw in ['price', '$', 'per', 'token', 'v4', 'flash', 'pro']):
        context = lines[max(0,i-2):i+3]
        for c in context:
            print(c)
        print("---")
PYEOF
```

DeepSeek's page is usually clean Docusaurus HTML — easy to parse. Pricing includes cache hit/miss columns.

**Pitfall (observed 2026-11-02)**: the page can serve a JS shell to curl — body reads "Your Docusaurus site did not load properly" with no pricing tables, even with a 200 response and ~50KB file. `cdn.deepseek.com/pricing.html` returns ~352 bytes (dead). Fallback chain that worked: (1) OpenRouter API listing for the model id, (2) the wiki's own event/entity page for the model (e.g. `wiki/events/2026-10-17-deepseek-v4.1-flash-1017-release.md` carried the $0.15/$0.60 figure with a cited OpenRouter source), (3) carry forward previously-verified peak/off-peak rows and label them "carried forward from <date>" in the Changelog rather than leaving them silently unverified.

## Cross-Provider Verification: OpenRouter API

**OpenRouter** at `https://openrouter.ai/api/v1/models` returns structured JSON with pricing for ALL providers. This is the single best cross-check source.

```bash
curl -sL 'https://openrouter.ai/api/v1/models' -o /tmp/openrouter_models.json
```

Parse with Python:
```bash
python3 << 'PYEOF'
import json
with open('/tmp/openrouter_models.json') as f:
    data = json.load(f)
models = data.get('data', [])
tracked = ['gpt-5', 'claude', 'gemini', 'deepseek', 'qwen', 'kimi', 'minimax', 'mimo', 'hy3', 'glm']
for m in models:
    mid = m.get('id', '').lower()
    if any(t in mid for t in tracked):
        pricing = m.get('pricing', {})
        inp = float(pricing.get('prompt', '0')) * 1000000
        out = float(pricing.get('completion', '0')) * 1000000
        ctx = m.get('context_length', 0)
        print(f'{m["id"]}: in=${inp:.2f}/M out=${out:.2f}/M ctx={ctx}')
PYEOF
```

**OpenRouter pricing vs official pricing**: OpenRouter prices may differ from official provider pages due to:
- OpenRouter markup/discount
- Introductory/promotional pricing
- Regional pricing differences
- Model version differences (OpenRouter may route to different model versions)

**Use OpenRouter as**: (1) discovery of new models not yet on wiki, (2) quick verification that prices haven't changed dramatically, (3) fallback when official pages are blocked/JS-rendered. **Do NOT use as primary source** — always prefer official provider pages.

## Common Pitfalls

- **`curl | python3` blocked**: tirith blocks this in ALL modes. Always save to file first.
- **`.dev` TLD blocked**: tirith blocks `ai.google.dev`. Use `cloud.google.com` instead.
- **Anthropic 301 redirects**: Always use `curl -sL` (follow redirects).
- **DeepSeek CloudFront 403**: Use `api-docs.deepseek.com` not `platform.deepseek.com`.
- **OpenAI page generator changed**: Was Next.js (had `__NEXT_DATA__`), now Astro (v6.0.4). The extraction pattern changed completely.
- **OpenRouter prices ≠ official prices**: Use for verification/discovery, not as primary source.
- **Introductory pricing**: Anthropic sometimes offers time-limited introductory prices (e.g., Sonnet 5 at $2/$10 through Aug 2026). Note these with `*` footnotes in the wiki. **Check expiry dates every run** — an expired promo is a silent wrong-price bug: as of 2026-11-02 Sonnet 5's $2/$10 had lapsed 8/31 and had to be corrected to $3/$15, while new promos (Gemini 4 Argon until 11/30, 3.8/3.7/3.6 Flash until 12/31, GPT-5.6 until ≥11/21) needed adding. Keep the footnote block dated ("active promos as of YYYY-MM-DD").
- **Batch pricing section**: When updating prices, also update batch pricing, cache pricing, tier analysis, and cost comparison sections — not just the main table.

## Cross-Check Sources

- **OpenRouter API** (`openrouter.ai/api/v1/models`): Structured JSON, all providers, best for verification
- **Provider docs pages**: More reliable than consumer pricing pages for model details
- **Provider blog posts**: Announcements often include pricing details before the pricing page updates
- **Wiki page**: `comparisons/llm-api-pricing.md` — the target page to update (but NOT the source of truth)

## Cron-mode notes (llm-pricing-monitor job)

- `execute_code` is BLOCKED in cron mode — build the log.md prepend with `write_file` to `/tmp/log_entry.md` then `cat /tmp/log_entry.md wiki/log.md > /tmp/log_merged.md && mv ...` in terminal.
- The working tree usually carries other jobs' uncommitted changes (skills edits etc.). Use **scoped `git add <your 5 files>`**, never blanket `git add wiki/`. If `git pull --rebase` refuses due to unstaged changes, `git stash && git pull --rebase && git push && git stash pop`.
- Verification gates: pre-commit runs index validator + tag taxonomy; commit message format `wiki: llm-pricing-monitor — <summary>` (single quotes if it contains `&`).
- Log entry / Changelog must state per-provider which rows changed vs "verified unchanged", and label any carried-forward (unverifiable this run) rows with their original verification date.
