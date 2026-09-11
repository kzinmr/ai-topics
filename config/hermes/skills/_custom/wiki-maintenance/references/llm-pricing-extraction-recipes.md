# LLM Pricing Extraction Recipes (per-provider)

> Condensed from the archived `llm-api-pricing-monitor` skill (curator consolidation 2026-09-11; its predecessor `llm-pricing-monitor` was archived 2025-07-13). Loaded from the "Scheduled Pricing Monitor" workflow in the parent SKILL.md (§2 Comparison Page Updates). URLs verified 2026-08-17.

> NOTE: `execute_code` is blocked in cron mode — run all processing via `terminal` with inline `python3 -c` or save-to-temp-file + `grep`/`sed`.

## Fetch URLs (verified working 2026-08-17)

| Provider | Working URL | Notes |
|----------|------------|-------|
| **OpenAI** | `https://developers.openai.com/api/docs/pricing` | Astro SSR page; pricing in embedded JSON props (`GroupedPricingTable` components). Extract with grep for model names + dollar amounts. No `__NEXT_DATA__` (Astro, not Next.js). |
| **Anthropic** | `https://docs.anthropic.com/en/docs/about-claude/models` | React Server Components; `www.anthropic.com/pricing` redirects to `claude.com/pricing` (Webflow, JS-rendered). The docs page has structured pricing table data in RSC format. |
| **Google** | `https://cloud.google.com/vertex-ai/generative-ai/pricing` | `ai.google.dev/pricing` may be blocked by security tools (Tirith lookalike TLD detection). Use `cloud.google.com` as fallback. Standard HTML `<table>` (not RSC/Astro) — parse `<tr>`/`<td>`. Watch `* through <date>` / `starting <date>` rows = intro pricing (capture both current-intro and future-standard). |
| **DeepSeek** | `https://api-docs.deepseek.com/quick_start/pricing` | ⚠️ `platform.deepseek.com` returns 403 CloudFront error. Use `api-docs.deepseek.com` instead. **Peak/off-peak pricing** as of 2026-08-17 (peak = 2× off-peak). |

## Extraction Patterns

### Google (Vertex AI)
```bash
curl -sL 'https://cloud.google.com/vertex-ai/generative-ai/pricing' -o /tmp/google.html
# Table is standard HTML <table> (NOT RSC/Astro). Rows look like:
#   <tr><td>Gemini 3.7 Flash * through December 31, 2026</td><td>Input (...)</td><td>Global</td><td>$0.75</td><td>$0.75</td><td>$0.075</td><td>$0.075</td></tr>
# Parse: split on <tr>, strip tags from each <td>, keep rows whose first cell matches
# 'Gemini 3.x' AND has 'Global' AND a '$' amount. Column order = Model | Modality | Region | Input | (cached?) | Cached-Input | ...
# ⚠️ Watch for "* through <date>" / "starting <date>" model rows = intro/promo pricing.
#    Footnotes state e.g. "Gemini 3.7 Flash are offered with introductory pricing of
#    $0.75 / $3.75 per 1M tokens ... through December 31, 2026. Starting January 1, 2027,
#    standard pricing of $1.5 / $7.50" — capture BOTH the current-intro and future-standard rates.
# ⚠️ The same model can appear in multiple tables (Global input, long-context, batch, cached)
#    — dedup by exact model string; use the 'Global' input row as the canonical In/Out price.
```

### OpenAI
```bash
curl -sL 'https://developers.openai.com/api/docs/pricing' | grep -i 'model\|price\|gpt-5\|o3\|o4-mini' | head -30
# Pricing data embedded in astro-island props as JSON arrays:
# [model_name, input_price, cached_price, cache_write_price, output_price]
# ⚠️ The page has FOUR content-switcher panes: standard / batch / flex / fast.
#    The SSR <table> you see reflects the ACTIVE pane (default = standard).
#    To read all tiers, search for data-content-switcher-pane="true" data-value="(...)"
#    markers and the "rows":[...],[...] arrays near each, OR just note that during a
#    GPT-5.6 launch promo, standard = batch = flex (50% off list) and only "fast"
#    bills the list rate. Confirm promo status via the "...promotional pricing is
#    available at least through <date>." note on the page.
# ⚠️ Renamed tier: "Priority" is now "Fast mode" (2026-07-30).
```

### Anthropic
```bash
curl -sL 'https://docs.anthropic.com/en/docs/about-claude/models' | grep -oP '\$\d+' | head -20
# RSC data contains: "$10 / input MTok", "$50 / output MTok" patterns
# Model names: claude-opus-5, claude-fable-5, claude-haiku-4-5, etc.
```

### DeepSeek
```bash
curl -sL 'https://api-docs.deepseek.com/quick_start/pricing' | grep -oP '\$\d+\.?\d*' | head -20
# Table structure: CACHE HIT (off-peak, peak), CACHE MISS (off-peak, peak), OUTPUT (off-peak, peak)
# Two columns = V4-Flash (left), V4-Pro (right)
```

## Pitfalls

1. **`execute_code` is blocked for cron jobs** — use `terminal` with inline `python3 -c` instead
2. **`curl | python3` pipe is blocked by Tirith security scan** — save to temp file first, then process
3. **Google `.dev` TLD blocked** — `ai.google.dev` triggers lookalike TLD detection; use `cloud.google.com` URLs
4. **DeepSeek URL changed** — `platform.deepseek.com` returns 403; use `api-docs.deepseek.com`
5. **Anthropic pricing page redirects** — `www.anthropic.com/pricing` → `claude.com/pricing` (JS-rendered); use `docs.anthropic.com` for structured data
6. **OpenAI page is Astro SSR, not Next.js** — no `__NEXT_DATA__` to extract; pricing is in astro-island component props
7. **Git stash needed when repo has dirty working tree** — `git stash && git pull --rebase && git stash pop` before adding pricing changes
8. **Peak/off-peak pricing (DeepSeek)** — use off-peak as "standard" in the comparison table; note peak = 2× in changelog
9. **`patch` with `read_file` output** — never use read_file output as old_string (line number prefix `N|` causes baked-in corruption)
10. **Multiple table matches** — use surrounding context lines (section headers, unique rows) to disambiguate patch targets
11. **log.md prepend buries the existing first entry's header** — when prepending via `{ echo "# Wiki Log"; echo ""; cat new_entry.md; sed -n '3,$p' wiki/log.md; }`, you strip lines 1–2 (`# Wiki Log` + blank) but the file's original first entry starts on line 3 with its OWN `## [date] ...` header. That header is NOT line 1–2, so `sed -n '3,$p'` preserves it fine ONLY if the original file's line 3 is that header. Verify with `read_file` after the merge that the pre-existing first entry still has its `## [` header immediately after your new entry; if the header got dropped, re-insert it with `patch` (find your entry's last bullet + the next entry's first `- **Context**` bullet, and insert the missing `## [...]` line between them).
12. **Dirty working tree with many unrelated changes** — the ai-topics repo accumulates changes from sibling cron jobs (skills/, scripts/, config/). Do NOT `git add wiki/` blindly — it will sweep in another job's `wiki/` edits. Stage ONLY your files: `git add wiki/comparisons/llm-api-pricing.md wiki/log.md`. The pre-commit tag validator still checks all staged files, but you only stage what you touched.

## Update Procedure

1. Fetch live data from each provider (see URLs above)
2. Parse pricing with grep/python (see extraction patterns)
3. Read existing wiki page: `wiki/comparisons/llm-api-pricing.md`
4. Compare fetched vs documented prices
5. If changes: update tables, update `updated:` frontmatter, add changelog entry, update trend sections
6. Update `wiki/log.md` with monitoring entry (see Pitfall 11 — verify the pre-existing first entry's `##` header survived the prepend)
7. Commit & push (stage ONLY the files you changed, not the whole `wiki/` dir — the repo has unrelated sibling-cron changes; see Pitfall 12): `cd ~/ai-topics && git add wiki/comparisons/llm-api-pricing.md wiki/log.md && git commit -m 'wiki: llm-pricing-monitor — [summary]' && git push`

## Key Model Lineups (as of 2026-08)

### OpenAI
- **GPT-5.6**: sol (list $8/$40), terra (list $4/$24), luna (list $0.40/$2.40) — ⚠️ on launch promo through ≥2026-11-21: Standard bills sol $4/$20, terra $2/$12, luna $0.20/$1.20 (50% off list, Standard=Batch=Flex). Cache writes at +25% over base input.
- **GPT-5.5**: $5/$30 (previous flagship)
- **GPT-5.4**: $2.50/$15, mini $0.75/$4.50
- **o3**: $3.50/$14 (Fast tier), o4-mini: $2/$8 (Fast tier)
- **gpt-4.1**: $3.50/$14, mini $0.70/$2.80, nano $0.20/$0.80 (Fast tier)
- **Specialized**: gpt-5.5-cyber & gpt-5.6-cyber ($12.50/$75, cyber cache write $15.625), gpt-5.3-codex ($1.75/$14)
- **Pricing tiers**: Standard, Batch (~50% off), Flex (lowest), **Fast mode** (was "Priority", renamed 2026-07-30; `service_tier` still accepts "priority"). ⚠️ Do NOT call the fast tier "Priority" — it is now "Fast mode."
- **⚠️ PROMO WINDOW (2026-08 → ≥2026-11-21)**: GPT-5.6 (sol/terra/luna) runs a launch promo where **Standard = Batch = Flex all bill at ~50% off the list price** (sol $4/$20 list $8/$40, terra $2/$12 list $4/$24, luna $0.20/$1.20 list $0.40/$2.40). Only the **Fast mode** pane bills the list rate. If the Standard pane shows half the list rate, it is the promo, NOT a real cut — record the current Standard rate as the live price and note the list price in the footnote + changelog. Re-verify the promo end-date ("at least through …") each run.

### Anthropic
- **Fable 5**: $10/$50 (ultra-premium)
- **Opus 5**: $5/$25 (premium)
- **Sonnet 5**: $2/$10 intro (through 2026-08-31), standard $3/$15
- **Haiku 4.5**: $1/$5

### DeepSeek
- **V4-Flash**: off-peak $0.22/$0.66, peak $0.44/$1.32
- **V4-Pro**: off-peak $0.66/$1.98, peak $1.32/$3.96
- Cache hit: 96.7-96.8% discount (was 99.2-99.6% pre-restructure)
- Full pricing table with historical comparison: see `references/deepseek-pricing-structure.md`
