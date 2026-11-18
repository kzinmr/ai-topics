# Blog Triage Patterns — 2026-11-18 (run 20261118T100050Z)

Outcome: 20 candidates → 6 takes, 5 references, 10 skips (batch entry). No user interaction (cron). Notable patterns:

## 1. Model-release triage: check BOTH lineage pages AND whole-wiki grep

GPT-6.2 Astra/Sol release: Simon Willison post was the substantive source (OpenAI official raw was RSS-fallback 1-sentence only, `scrape_status: "rss-fallback — openai.com returns 403 to scraper UA"`). Coverage verification that worked:

1. `grep -rin "gpt-6.2\|gpt6.2" concepts/ entities/ events/` across the WHOLE wiki — found only ONE incidental mention (ethan-mollick.md "hard to steer" verdict). Zero mentions in the lineage pages `entities/openai-astra.md` and `entities/gpt-6-1-sol.md`.
2. Conclusion: greenfield take (★★★★★ into `entities/openai-astra.md`), NOT a skip just because lineage pages exist.

Rule: for model-family releases, "ancestor entity page exists" ≠ "release covered". The test is whether the SPECIFIC version string appears anywhere with substance. A rich ancestor page (186 lines on Astra) with zero 6.2 mentions is a genuine gap.

## 2. openai.com 403 RSS-fallback raws: reference, never take

Three OpenAI News raws arrived as 600-700B files containing only the RSS description one-liner (GPT-6.2 launch, ChatGPT for Sales, Le Figaro partnership). Pattern: when the same topic has a richer third-party raw in the same batch (Simon Willison, newsletter), the official stub → `reference` with `candidate_wiki_path` = the page the richer take writes to, so downstream attaches it as a primary-source in `sources:`. Standalone stubs with no third-party companion (ChatGPT for Sales, Le Figaro) → reference with `candidate_wiki_path: None`, archived for future aggregation pages.

## 3. Event-page saturation vs new-beat gap (NVIDIA Bubble case)

`events/nvidia-ceo-transition-2026.md` existed (132 lines, updated 11-16, covered resignation/testimony/smuggling-report beats). Ed Zitron's 56KB "The NVIDIA Bubble" was NOT a duplicate — its core data (Megaspeed $4.8B→$7.5B→$12B escalation, Culper $43bn+ short report, Supermicro Wally Liaw arrest, Alice Huang→DeepSeek investment) had ZERO grep hits wiki-wide (`grep -ril "megaspeed\|alice huang\|culper\|supermicro" events/ concepts/ entities/`). Decision: take-as-existing-page-update (★★★★☆), not skip despite the fresh `updated:` date. Standard dual-source take-as-update test applied: does the existing page contain the SPECIFIC numbers/entities? No → take.

## 4. Author-entity running-series gap (George Hotz case)

`entities/george-hotz.md` meticulously documented the "singularity is nearer" essay series through Nov 17 ("My Empire of Dirt") but the Nov 18 essay ("My Empire of Sunshine and Roses") was a new installment with distinct theses (differential history / counterfactuals, agent-swarm exponential-cost, millions-of-power-centers). When an entity page tracks a RECURRING essay series, each new installment with new argument structure is a take — check whether the page's series table ends at the previous installment.

## 5. Pattern-taxonomy pages: new pattern member ≠ covered topic

`concepts/security-and-governance/agent-sandboxing-patterns.md` covers Browser Use's Isolate-the-Tool / Isolate-the-Agent patterns. Simon's "external sandbox" pattern (agent OUTSIDE, executed code INSIDE; allow-list proxy + credential replacement, with Prime Radiant) is a third pattern family — zero grep hits for "external sandbox|prime radiant". A pattern-taxonomy page covering patterns A and B does not cover pattern C.

## 6. Batch-skip entry for heterogeneous non-AI items

10 non-AI/low-value items (SetShot macOS utility, Apple outage flash report, HAOS qcow2 howto, Old New Thing BASIC history, stacked-diffs git tool, Paul Brainerd obit, DF ad link, iPhone Duo X post, Pluralistic link roundup) were collapsed into ONE skip decision with comma-joined item_id and a `|`-joined body_excerpt sampling each file's opening. Each was still body-read per BODY-READING MANDATE before batching. Kept the decisions array at 12 entries.

## 7. Cross-pipeline dedup hit in practice

sitemap-monitor had already scraped Harvey's "GPT-6.2 coming soon to Harvey" blog post into `raw/articles/2026-11-18_harvey_...md` (06:00). Harvey's version is a vendor mention → did not create a separate take; Simon Willison's post is the primary source for the model-release take.

## 8. Builder-script hygiene (reconfirmed)

- `write_file` → `/tmp/build_blog_triage_20261118.py` → `terminal python3`, gated with `python3 -c "import ast;ast.parse(...)"`. No CJK heredocs. ASCII `*` stars via `("*" * stars) + " " + reason` (no ★ glyph in literals). ASCII quotes avoided inside Japanese reason strings (used 「」 or bare text).
- A vestigial unused `make()` helper was removed pre-run via patch — lint only checks syntax, so dead code with latent bugs passes; eyeball before executing.
- `HERMES_HOME` env fallback to hardcoded `/opt/data/.hermes` (no `expanduser`).
- Dedup guard keyed on `item_id` (not URL) — batch entries share empty URL.
- archive_triage.py printed the symlinked `/opt/data/.hermes/home/ai-topics/...` path — `readlink -f` canonical, do NOT move (known pattern, reconfirmed).
- archive_index.json is modified by archive_triage.py but not auto-committed → needs a second targeted `git add wiki/raw/archived/triage/archive_index.json` commit.
