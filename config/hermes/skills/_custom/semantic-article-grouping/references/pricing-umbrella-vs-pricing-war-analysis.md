# Pricing/comparison umbrella pages ≠ pricing-war analysis (Oct 2026 blog triage)

Validated 2026-10-26 (run_id 20261026T100303Z, blog-triage).

## Pattern 1: `comparisons/llm-api-pricing.md` is a sticker table, not an analysis page

The page (476 lines) contains: per-provider/model rows with Base In $/1M, Cache Read $/1M, Discount, and an "Effective (80% hit)" column computed as `20% × base + 80% × cache_read`. That's it — no narrative, no timeline, no causality.

Therefore a blog/newsletter article that presents a **timeline of price CUTS with causal explanation** is a genuine ★★★★☆/★★★★★ take against that page even though every model named has its own entity page and every sticker price appears in the table. Concrete gap-check questions that decided minimaxir's "OpenAI and Anthropic cut their LLM prices by up to 80%" as a take:

- Does the page contain the **retaliatory tit-for-tat framing** (each cut is a response to the competitor's cut)? No.
- Does it have the **cache-read share-of-spend fact** (96-99% of agentic coding token expenditure; hit rate 90-100% → a 75% cache-read cut ≈ 70-75% real cost reduction)? No.
- Does it have **inference-provider competition data** (DeepSeek V4.1 Flash 1017: 13 OpenRouter providers in May → 29 by Oct; Cloudflare/DeepInfra within 10% of DeepSeek's own price)? No.
- Does it have **aggregate-gateway data** (Vercel AI Gateway: cost/token down to 43.3% of April 2026 while total spend rises)? No.
- Does it have the **IPO-timing paradox** (cuts right before S-1; reported ~80% inference margins; Codex $200-tier usage cut 50% "to reflect increasingly efficient models") or the **loss-leading rebuttal** (not a duopoly, negligible switching cost → price converges to marginal cost)? No.

`concepts/token-economics.md` (361 lines) is the other obvious target and has the same limitation from the opposite direction: it carries Epoch AI's "The plunging price of thought" cohort-analysis lens (≈47%/quarter cost-of-capability decline, 725× o3→GPT-5.6 Luna GPQA example). That macro-cohort framing ≠ lab-vs-lab retaliatory-cut timeline. So an article can be a real gap even though BOTH the table and the macro curve exist.

## Pattern 2: adjacent-dimension gap check via targeted grep on the top 2 update targets

When an article's thesis is an *adjacent dimension* of an existing concept page, don't stop at "page exists, keyword appears once". Grep the thesis's vocabulary across the two most plausible update targets and cite the near-zero hit count inside `reason_ja` — it converts "page exists for the umbrella" into defensible take evidence.

Worked example (jyn.dev "A rising tide raises all rents"):
- Target `concepts/ai-economics-post-scarcity.md` (122 lines) covers Imas relational sector, Trammell network-adjusted factor shares, Kaldor fact, lump-of-labor, O-Ring, elasticity, Jevons, plus a UBI / negative-income-tax / universal-basic-capital / wealth-tax / sovereign-wealth-fund table.
- Grep `rent|landlord|land value|georg|UBI|Moretti|Hornbeck|cash-flow` → single hit ("rents flow to users not producers"). So the article's core theses are absent: UBI absorbed by housing rent (Yudkowsky Poverty-Equilibrium overridden by rent-seeking), Land Value Tax + cash-flow tax (UK IFS full-expensing = zero deadweight loss, government as "compulsory silent partner", loss-making firms get refunds) + Citizen's Dividend with Alaska/Norway precedents, non-landlord rentiers (MSP authorization example), transition compromise (defer LVT increase until sale with interest, one-time unlike CA Prop 13), Acemoglu-Restrepo reinstatement effect / Butlerian Jihad outcome. → take as existing-page section addition, not skip.

## Pattern 3: never ship a `candidate_wiki_path` that doesn't exist

Reference items get their natural-looking path auto-guessed ("optical fiber shortage" → `concepts/ai-data-center-supply-chain.md`). That page did not exist. Verification step worth keeping: after saving triage JSON, print the non-skip `candidate_wiki_path` list and `ls`/grep each one; if absent, re-grep the specific keyword (e.g. `optical|fiber|supply constraint`) across the nearest existing candidates and repoint to the page with a 0-hit proof in the reason.

This run: `concepts/subprime-data-center-crisis.md` (173 lines) and `concepts/ai-supply-chain-security.md` (128 lines) both had **0** hits for optical/fiber → repointed the construction-physics reference to `subprime-data-center-crisis.md` with the grep evidence, then re-saved the JSON with a small `/tmp/fix_*.py` patch script (no rewrite of the whole builder).

## Misc confirmations from this run

- `archive_triage.py blog --keep-reference` prints the nested-looking `/opt/data/.hermes/home/ai-topics/...` path — symlink to the canonical repo, safe to `git add`.
- The builder script with CJK `reason_ja`/`body_excerpt` was written via `write_file` to `/tmp/build_blog_triage_<date>.py` and run via `terminal python3`, gated first by `python3 -c "import ast; ast.parse(...)"`. Zero scanner blocks, zero syntax surprises.
- unsaved_articles YouTube batch: single consolidated skip decision with `body_excerpt: "（unsaved_articles — 抽出不可）"` plus a named re-evaluation shortlist (DeepMind Managed Agents, Arize AI Eval → future `transcripts/` candidates). Keeps the decisions array compact while preserving the signal.
- `archive_triage.py` leaves `wiki/raw/archived/triage/archive_index.json` modified as well as writing the date-stamped file — stage BOTH in one or two commits (`git add wiki/raw/archived/triage/<date>_<runid>.json wiki/raw/archived/triage/archive_index.json`), otherwise the index change lingers uncommitted for the next run.
