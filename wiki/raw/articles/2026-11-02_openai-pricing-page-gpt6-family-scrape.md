---
title: "OpenAI GPT-6 family pricing — official pricing page scrape (2026-11-02)"
type: raw-note
created: 2026-11-02
source: https://developers.openai.com/api/docs/pricing
fetched_at: 2026-11-02T12:10:00Z
method: curl, Astro island inline-array extraction
confidence: high
note: Standard-tier tuples [model, input, cached_input, cache_write_5m, output]. Fast/Flex/Ultrafast tiers are 2x / 0.5x / 6x Standard respectively.
---

# OpenAI GPT-6 family — live pricing page data (2026-11-02)

Extracted verbatim from `https://developers.openai.com/api/docs/pricing` (curl, 597KB HTML, Astro hydration arrays).

## Standard tier ($/1M tokens)

| Model | Input | Cached input | Cache write (5m) | Output |
|---|---|---|---|---|
| gpt-6-astra | $10.00 | $1.00 | $12.50 | $50.00 |
| gpt-6.1-sol | $2.00 | $0.10 | $2.50 | $10.00 |
| gpt-6.1-terra | $1.00 | $0.05 | $1.25 | $5.00 |
| gpt-6-luna | $0.10 | $0.01 | $0.125 | $0.50 |
| gpt-6-sol | $2.00 | $0.20 | $2.50 | $10.00 |
| gpt-6-rosalind | $15.00 | $1.50 | $18.75 | $75.00 (trusted-access only) |
| gpt-6-astra-law | $10.00 | $1.00 | — | $50.00 (promo at least through 2026-12-31) |

## Other tiers (same page, 4 tier tabs; columns In / Out / Cached / CacheWrite)

- Standard: gpt-6-astra $10/$50, gpt-6.1-sol $2/$10, gpt-6.1-terra $1/$5, gpt-6-luna $0.10/$0.50, gpt-6-sol $2/$10
- Flex (0.5×): gpt-6-astra $5/$25, gpt-6.1-sol $1/$5, gpt-6.1-terra $0.50/$2.50, gpt-6-luna $0.05/$0.25
- Fast (2×): gpt-6-astra $20/$100, gpt-6.1-sol $4/$20, gpt-6.1-terra $2/$10, gpt-6-luna $0.20/$1
- Ultrafast (6×): gpt-6-astra $60/$300, gpt-6.1-sol $12/$60, gpt-6.1-terra $6/$30
- Batch ≈ 0.5× Standard (per OpenRouter `:batch` listings)

## GPT-5.6 family (verified unchanged, promo still active)

- gpt-5.6-sol Standard tuple: `[4, 0.4, 5, 20]` → $4 / $0.40 / cache write $5 / $20 ✓ matches wiki
- gpt-5.6-terra: `[2, 0.2, 2.5, 12]` ✓; gpt-5.6-luna: `[0.2, 0.02, 0.25, 1.2]` ✓
- gpt-5.6-cyber: `[12.5, 1.25, 15.625, 75]` ✓; gpt-5.3-codex `[1.75, 14, 0.175]` ✓
- GPT-5.6 list/Fast rate still $8/$40 (sol), i.e. 50%-off promo ongoing.
- `gpt-5.4` tuple `[2.5, 0.25, -, 15]` ✓; `gpt-5.5` still $5/$30.

## Cross-check: OpenRouter (2026-11-02)

- openai/gpt-6-sol: $2/$10 ✓; openai/gpt-6-luna: $0.10/$0.50 ✓; openai/gpt-6.1-sol: $2/$10 ✓; openai/gpt-6-astra: $10/$50 ✓ (ctx 1.05M)

## Raw tuples (verbatim, de-escaped, Astro hydration arrays)

```
["gpt-6-astra"],[0,10],[0,1],[0,12.5],[0,50]
["gpt-6.1-sol"],[0,2],[0,0.1],[0,2.5],[0,10]
["gpt-6.1-terra"],[0,1],[0,0.05],[0,1.25],[0,5]
["gpt-6-luna"],[0,0.1],[0,0.01],[0,0.125],[0.5]
["gpt-6-sol"],[0,2],[0,0.2],[0,2.5],[0,10]
["gpt-6-rosalind"],[0,15],[0,1.5],[0,18.75],[0,75]
```

Tuple order In / CachedInput / CacheWrite(5m) / Output confirmed against the rendered table rows and OpenRouter pricing.
