# Blog Triage Patterns — 2026-08-11 (run 20260811T101550Z)

Batch: 13 blog candidates (simonwillison, martinalderson, johndcook×2, garymarcus, daringfireball×4, seangoedecke, entropicthoughts, dfarq, oldnewthing) + 7 unsaved (NYT RAM crisis, OpenAI News×2, Edinburgh Fringe×4).

## Result
- **Takes 3** (all ★★★★☆ existing-entity enrichments, zero new pages): `entities/martin-alderson.md` (cache read costs), `entities/gary-marcus.md` (open-weight≠open-source), `entities/seangoedecke-com.md` (local models will not win)
- **References 2**: `entities/simon-willison.md` (Muse Glimmer hands-on), `concepts/vibe-coding.md` (tedium Vibe-Coded Flattery / Dark Hours incident)
- **Skips 12**: 7 non-AI (math/Apple/Windows/tech-history/App Store policy) + 5 no-extractable-content (NYT paywall, OpenAI unsaved×2, Edinburgh Fringe batch)
- Take rate ≈ 23% on blog candidates — consistent with `blog-triage-2026-08-04-patterns.md` mixed-batch composition shift (cost-analysis technical explainer + editorial-substack follow-up + opinion essay + curator hands-on + cultural commentary → higher yield than homogeneous opinion-blog batches).

## Pattern: model-release blog post → entity page already exists (official-source variant)
Candidate `simonwillison.net — Introducing Muse Glimmer` (Aug 10) looked like a potential ★★★★★ take (new Meta 30B open-weights model, Apache 2.0). **Before rating, check the model entity:**
- `entities/muse-glimmer.md` ALREADY existed (created 2026-08-10, sources: `raw/articles/2026-08-10_research-meta-ai_introducing-muse-glimmer.md`) — the official Meta research blog was scraped the previous day by sitemap-monitor/prior pipeline.
- Entity page was comprehensive (architecture/training phases, agentic capabilities incl. DeepSearch QA/MCP-Atlas/τ-Bench/SWE-Bench, quantization, local deployment).
- → Downgrade to **reference** on the author's entity page (`entities/simon-willison.md`, August 2026 Updates section): the blog adds hands-on perspective not present in the official-source entity page (LM Studio 18.16GB quantized run, llm-coding-agent plugin against Datasette, vision/multimodal description test, llm-lmstudio LLM 0.32 compat patch).
- **Procedure**: for ANY blog candidate about a newly released model, `ls wiki/entities/ | grep -i <model>` and read the entity page BEFORE deciding. If the page exists with official sources and created-date ≥ article date → reference (author perspective), not take. Locate the author's Updates section with `grep -n "^## \|^### " entities/<author>.md` to say where the reference entry lands.

## Gap-verification greps that worked (all three takes were entity-enrichment gaps)
- `grep -c "cache read\|cache reads" entities/martin-alderson.md` → **0** even though the page has rich cost-analysis sections (inference profitability, "No $5k per Claude Code user", KV cache 100x compression). Cache-read-specific analysis (quadratic cost growth with turns, DeepSeek 1/10th cache pricing, ~$0.5/GB-h profit math vs AWS <1¢) was a genuine gap → take.
- `entities/seangoedecke-com.md` (510 lines): grep sources list + body for "local models will not win" → absent; body only had "Datacenter Cost Structure" from a different essay (`luddites-and-ai-datacenters`) → genuine gap → take.
- `entities/gary-marcus.md`: `grep -n "^## \|^### "` shows 30+ Core Positions subsections but no open-weight-vs-open-source essay (only a tangential Anthropic open-weight letter mention) → genuine gap → take.
- Lesson: entity pages accumulate author essays; each new essay needs its own subsection. The section-list grep is the fastest coverage check — cheaper than full body reads.

## unsaved_articles: OpenAI News items
- OpenAI Texas letter + Model ML/GPT-5.6 Sol in the unsaved array → **skip** per unsaved rule (no extractable body). But first check `ls -lt wiki/raw/articles/ | grep -i openai` — no openai.com sitemap captures existed for these → flag in the reason for sitemap-monitor follow-up. Body excerpt: （unsaved_articles — 抽出不可）.
- GPT-5.6 Sol itself is already covered by `concepts/gpt/gpt-5-6.md` — the unsaved item is just a case-study variant.

## Archive idempotency confirmation
- Second invocation of `python3 scripts/archive_triage.py blog --keep-reference` returns `{"blog": {"ok": true, "message": "All items already archived (dedup)", "archived": 0}}` — cheap confirmation the first run archived everything (14 items: 12 skip + 2 reference).
- First-run output showed a nested-looking path `/opt/data/.hermes/home/ai-topics/wiki/raw/archived/...` — verify with `readlink -f` (symlink to canonical repo, do NOT move). Confirmed again 2026-08-11.
