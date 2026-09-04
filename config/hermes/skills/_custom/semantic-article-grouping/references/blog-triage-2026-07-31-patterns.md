# Blog Triage Patterns — 2026-07-31 run (reference-heavy day)

Validated in a 19-candidate + 1-unsaved blog-triage run that produced **1 take / 9 references / 10 skips** (~45% reference rate — well above the usual 20-25%). The reference-heavy outcome came from a multi-article simonwillison.net day (5 posts) plus genuine entity-enrichment opportunities (Giles Thomas series, Sean Goedecke, Ibrahim Diallo, Cory Doctorow). When a single well-documented source (simonwillison) contributes 5+ posts, references legitimately dominate — do not over-correct to skip.

## Cross-lingual same-essay dedup (NEW pattern)

An entity page may document the ORIGINAL-language version of an essay, and the translated English version later arrives via blog-ingest. **This is NOT a coverage gap.**

Concrete case (July 2026): `entities/berthub-eu.md` documented Bert Hubert's Dutch essay *"AI: Overwegingen voor wie erover gaat"* (July 2026, presented at NPD + AWTI) with full key-concerns coverage (FOMO adoption, environment, IP, digital sovereignty, bubble, junior/senior pipeline, cognitive offloading, measurement recommendation). The English article *"AI: Considerations for people who make decisions"* (berthub.eu, same essay translated — the post even says "mostly translated into English by ChatGPT") arrived via blog-ingest. Correct decision: **skip** (content already captured), optionally add the English URL to the entity page's `sources`.

Detection test: do the entity page's documented concerns/context (dates, venues, specific recommendations) match the article body? If yes, language change alone is not new content.

## Duplicate entity pages during triage

Two entity pages can exist for the same person under different filename spellings. Observed July 2026: `entities/giles-thomas.md` (92 lines, older) AND `entities/gilesthomas.md` (201 lines, richer, `updated: 2026-07-30`). Both were real pages.

Handling:
1. Use the RICHER page (longer, more recently updated, more sources) as `candidate_wiki_path` for references.
2. Note the duplicate in the triage summary / downstream report for wiki-health consolidation — do NOT enrich both pages.
3. This is a triage-time signal only; the fix (merge/redirect) belongs to wiki-health, not the triage agent.

## Manual-ingest same-day concept creation (dedup variant)

The standard same-day log.md grep checks pipeline names (blog-wiki-ingest, newsletter-wiki-ingest, raw-backlog-ingest). **Also check `manual-ingest` lines.** On 2026-07-31, log.md showed `manual-ingest | Ingested Anthropic cybersecurity evaluation incidents article` — the concept page `concepts/anthropic-cybersecurity-eval-incidents.md` was created same-day by a manual/user-driven ingest. The blog candidate (Simon Willison's quote-post of the Anthropic disclosure) was therefore downgraded from take to **reference** (only Simon's "spectacularly risky business" commentary was missing from the concept page → enrich `entities/simon-willison.md` instead). This mirrors the existing "blog triage take already handled by newsletter-wiki-ingest" pattern but with manual-ingest as the winning pipeline.

## Pricing-change pages go stale fast (partial-coverage re-confirmation)

`concepts/gpt/gpt-5-6.md` was updated 2026-07-15 but missed OpenAI's 2026-07-30 price change (Luna −80% to $0.20/$1.20, Terra −20%, Sol kernel optimization in Triton/Gluon cutting serving cost 20%). Pricing/availability changes are a common stale-page trigger for model concept pages — when a model-release news item is a price drop, the existing concept page's pricing table is the first place to check for a gap.

## Archive path display variant (cron context)

`archive_triage.py` uses `expanduser`, so in cron terminal context (`HOME=/opt/data/.hermes/home`) the printed `archive_path` shows the nested variant: `/opt/data/.hermes/home/ai-topics/wiki/raw/archived/triage/blog/<run>.json`. The file STILL lands at the canonical path (`/opt/data/ai-topics/wiki/raw/archived/...`) because the symlink chain resolves. Verified July 2026: identical files at both paths.

Handling:
- Don't panic at the nested path; verify with `ls` on the canonical path.
- Don't re-run the archive "to fix the path" — a second run returns `{"ok": true, "archived": 0, "message": "All items already archived (dedup)"}`.
- The archive file content can be verified with a direct `python3 -c` that opens the canonical path and counts decisions per `recommended_action` (expect `references + skips`, no takes).

## Pipe scanner nuance: python3 | python3 also blocked

The `tirith:pipe_to_interpreter` scanner blocks not just `cat file | python3 -c` but also `python3 script.py 2>&1 | python3 -c ...` — any pipe whose consumer is an interpreter. Workaround used successfully: run the archive script plainly with `2>&1 | tail -12` (tail is not an interpreter), and verify with a separate direct `python3 -c "json.load(open(...))"` call (no pipe).
