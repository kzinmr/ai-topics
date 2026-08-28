# Provider-Specific Fetch Quirks

Detailed notes on fetching pricing data from each LLM provider. Updated 2026-06-15.

## OpenAI

**URL**: `https://developers.openai.com/api/docs/pricing`

**Page type**: Astro SPA. May contain `__NEXT_DATA__` JSON, but not always.

**Fetch strategy**:
```bash
curl -s 'https://developers.openai.com/api/docs/pricing' -o /tmp/openai_pricing.html
```

**Parse strategy**:
1. Try `__NEXT_DATA__` JSON extraction first
2. Fallback: strip HTML tags and extract text around model names
3. Look for pricing table: "Standard Batch Flex Priority" section

**Key patterns**:
- Standard pricing table has: Model, Input, Cached input, Output (short context), then same for long context
- Batch pricing: separate section with ~50% discount
- Flex pricing: same as Batch
- Priority pricing: ~2.5x standard
- Specialized models (Codex, Cyber, Deep Research, Computer Use) in separate categories

**Last verified**: 2026-06-15 — GPT-5.5/5.4/5.4-mini/5.4-nano confirmed. o3/o4-mini removed from standard (deep-research only).

## Anthropic

**URL**: `https://www.anthropic.com/pricing`

**Page type**: Static HTML with 301 redirect (openresty). `curl -sL` required.

**Fetch strategy**:
```bash
curl -sL 'https://www.anthropic.com/pricing' -o /tmp/anthropic_pricing.html
```

**Parse strategy**:
1. Strip HTML tags
2. Search for "Claude Fable", "Claude Opus", "Claude Sonnet", "Claude Haiku"
3. Prices appear as `$ X / MTok` format
4. Prompt caching: Write and Read prices listed separately per model

**Key patterns**:
- Models listed newest-first: Fable 5 → Opus 4.8 → Sonnet 4.6 → Haiku 4.5
- "Fast mode" available for Opus at 2x pricing
- US-only inference at 1.1x pricing
- Batch processing available (separate section)
- Managed Agents: $0.08/session-hour (not per-token)
- Web search: per-query pricing (not per-token)

**Last verified**: 2026-06-15 — All models confirmed at expected prices.

## Google (Vertex AI)

**URL**: `https://cloud.google.com/vertex-ai/generative-ai/pricing`

**⚠️ DO NOT use `https://ai.google.dev/pricing`** — the `.dev` TLD is blocked by tirith security scanner as "lookalike TLD". Use Vertex AI URL instead.

**Page type**: Static HTML, large (~800KB). No JS rendering needed.

**Fetch strategy**:
```bash
curl -sL 'https://cloud.google.com/vertex-ai/generative-ai/pricing' -o /tmp/google_pricing.html
```

**Parse strategy**:
1. Strip HTML tags
2. Search for "Gemini 3", "Gemini 2.5" model names
3. Tables have columns: Model Type, Price (/1M tokens), Price >200K input, cached input, >200K cached
4. Global vs Non-global pricing (typically 10% uplift for non-global)

**Key sections**:
- **Gemini 3 Standard**: Current generation (3.1 Pro Preview, 3.5 Flash, 3 Flash Preview, 3.1 Flash-Lite)
- **Gemini 2.5 Standard**: Legacy (2.5 Pro, 2.5 Flash, 2.5 Flash Lite)
- **Priority tier**: ~1.8x standard pricing
- **Image models**: Separate pricing (Gemini 3 Pro Image, 3.1 Flash Image)

**Pricing discrepancy note**: `ai.google.dev` (consumer API) and Vertex AI may show different prices. As of 2026-06-15, Gemini 3.1 Pro showed $2.50/$10.00 on ai.google.dev but $2.00/$12.00 on Vertex AI. Prefer Vertex AI as the authoritative enterprise source.

**Last verified**: 2026-06-15 — Gemini 3.1 Pro ($2/$12), 3.5 Flash ($1.50/$9), 3 Flash Preview ($0.50/$3), 3.1 Flash-Lite ($0.25/$1.50).

## DeepSeek

**URL**: `https://api-docs.deepseek.com/quick_start/pricing`

**⚠️ DO NOT use `https://platform.deepseek.com`** — blocked by CloudFront (403).

**Page type**: Docusaurus static site.

**Fetch strategy**:
```bash
curl -sL -A 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36' \
  'https://api-docs.deepseek.com/quick_start/pricing' -o /tmp/deepseek_pricing.html
```

**Parse strategy**:
1. Strip HTML tags
2. Search for "PRICING" section
3. Prices in "1M INPUT TOKENS (CACHE HIT)", "1M INPUT TOKENS (CACHE MISS)", "1M OUTPUT TOKENS"
4. Two models: deepseek-v4-flash and deepseek-v4-pro

**Key patterns**:
- Cache hit prices are ~99% cheaper than cache miss
- Model names `deepseek-chat` and `deepseek-reasoner` being deprecated (2026-07-24) — aliases for v4-flash and v4-pro
- Concurrency limits: v4-flash=2500, v4-pro=500

**Last verified**: 2026-06-15 — V4-Flash ($0.14/$0.28, cache $0.0028), V4-Pro ($0.435/$0.87, cache $0.003625).

## Cross-Provider Notes

- **"Preview" models**: Google and others may label models as "Preview" — these are GA-ready but may have pricing changes. Track them but note the preview status.
- **Batch API availability**: Not all providers offer batch APIs. Only OpenAI and Anthropic currently do.
- **Regional pricing**: Some providers charge uplift for data residency (OpenAI: 10%) or non-global regions (Google: 10%).
- **Cache mechanisms differ**: OpenAI auto-caches, Anthropic requires explicit write, Google has Context Caching API, DeepSeek auto-caches via MLA.
