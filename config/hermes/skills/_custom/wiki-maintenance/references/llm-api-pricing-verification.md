# LLM API Pricing Verification Techniques

## Problem
Most LLM provider pricing pages are SPAs (Single Page Applications). `curl` returns empty/minimal HTML, making automated price extraction unreliable.

## SPA Providers (require API or browser)
- **OpenRouter** — `openrouter.ai` pricing pages
- **Xiaomi MiMo** — `platform.xiaomimimo.com`
- **DashScope (Qwen)** — `help.aliyun.com/zh/model-studio/`
- **Anthropic** — `anthropic.com/pricing`
- **Google** — `ai.google.dev/pricing` (partially SSR)

## SSR Providers (curl works)
- **DeepSeek** — `platform.deepseek.com` (may return pricing data in HTML)
- **Baidu Cloud** — `cloud.baidu.com`

## Verification Methods

### Method 1: OpenRouter API (Preferred Cross-Check)
```bash
curl -s 'https://openrouter.ai/api/v1/models' | python3 -c "
import sys, json
data = json.load(sys.stdin)
targets = ['provider/model-id', 'provider/model-id-2']
for m in data.get('data', []):
    if m['id'] in targets:
        p = m.get('pricing', {})
        print(f\"ID: {m['id']}\")
        print(f\"  Name: {m.get('name', 'N/A')}\")
        print(f\"  Context: {m.get('context_length', 'N/A')}\")
        print(f\"  Input: \${float(p.get('prompt', '0'))*1e6:.4f}/1M\")
        print(f\"  Output: \${float(p.get('completion', '0'))*1e6:.4f}/1M\")
        print(f\"  Max Out: {m.get('top_provider', {}).get('max_completion_tokens', 'N/A')}\")
        print()
"
```
- Pricing is in $/token (multiply by 1e6 for $/1M tokens)
- Returns: context window, max output, model name
- Caveat: OpenRouter pricing may include markup — always note source

### Method 2: Browser Tool (for official pages)
```python
delegate_task(
    goal="Visit https://provider.com/pricing and extract ALL pricing data for ModelName",
    toolsets=["browser"]
)
```
- Use when OpenRouter doesn't have the model
- Use when you need official/cache/batch pricing not exposed via OpenRouter

### Method 3: Web Search Fallback
```
web_search("provider model-name API pricing per million tokens 2026")
```
- Use for historical pricing or when both above methods fail

## `~` (Unverified Estimate) Removal Workflow

When user says "remove `~` if the price is confirmed":

1. **Verify** price via OpenRouter API or official source
2. **Search all occurrences**:
   ```
   search_files(pattern="~\\$.*ModelName", path="wiki/comparisons/FILE.md")
   ```
   The `~` appears in **5-8 locations** across sections:
   - Main frontier table
   - Cache read prices table
   - Cache break-even table
   - Batch pricing table
   - Tier analysis table
   - Cost comparison (chat workload)
   - Cost comparison (code gen workload)
   - Legacy models table (if moved there)

3. **Patch each occurrence** — each section has different column layouts, so one-at-a-time `patch` is safest
4. **Verify context window** — verification may reveal the context window changed (e.g., `200K → 1M`)
5. **Check model name** — the model may have been renamed (see below)

## Model Name Change Detection

Provider model names change between versions:
- `MiMo-V2.5-Pro` → `MiMo-7B-RL` (Xiaomi, June 2026)
- `Gemini 2.5 Flash` → `Gemini 3.5 Flash` (Google)

When updating pricing, always check the official page for the **current** model name. Update in ALL sections:
- Frontier/main table
- Tier analysis
- Cache pricing (if applicable)
- Related Pages wikilink description
- Entity page references

## Case Study: June 2026 LLM Pricing Update (5 items)

Changes applied in a single session:
1. **Sonnet 4.6 `~` removal** — verified $3.00/$15.00 via OpenRouter, removed `~` from 7 locations, updated ctx 200K→1M
2. **Gemini 3.1 Flash Lite** — added $0.25/$1.50 (1M ctx) from OpenRouter
3. **Xiaomi MiMo** — model renamed MiMo-V2.5-Pro→MiMo-7B-RL, price dropped 6.7x ($1/$3→$0.15/$0.60), added cache 75%
4. **Hy3 Preview** — verified $0.063/$0.21 via OpenRouter (was ~$0.07/~$0.26), ctx 128K→256K
5. **Qwen3.7-Max/Plus** — added two new frontier models from OpenRouter

Key lesson: **SPA pages require API-first verification**. The delegate_task browser approach returned incomplete data for Xiaomi, but the OpenRouter API returned exact prices for all 4 models in a single call.
