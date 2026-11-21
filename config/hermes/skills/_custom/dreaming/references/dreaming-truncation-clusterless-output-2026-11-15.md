# Truncation-failure fork: cluster-bearing vs cluster-less dreaming-group output

Validated 2026-11-15 (`dreaming-wiki-ingest`, commit `ce63d66c`).

## The gap in the existing fallback chain

Pitfall #12 and the 2026-08-06 variant both tell you: when the pre-run script reports
`failed to parse JSON response from dreaming-group output` with an `output_path`, read that
file's tail to recover the dreaming-group's cluster analysis.

**Those variants assume clusters exist. They may not.** Reading a 5,000-line tail that
contains only the injected prompt is pure context waste, and `wc -l` is NOT the discriminator
(a cluster-less file was 5,341 lines / 435 KB).

## 3-call discriminator — run this BEFORE reading the tail

```bash
# 1. Do cluster headings exist? (look for "## Theme Clusters" / cluster headings in the tail)
grep -n "^#\{1,3\} " <output_path> | tail -40

# 2. Is the injected checkpoint pool empty, with a giant existing_wiki_pages list?
grep -n '"total_articles"\|"articles": \[\]\|"recent_raw_articles"' <output_path>

# 3. Did upstream commit anything at ~18:10 (enrichment or archive)?
cd ~/ai-topics && git log --oneline --since="<today> 17:00" --until="<today> 19:00"
```

## Decision table

| State | Discriminator | Response |
|---|---|---|
| **Cluster-bearing** (Jul 17, Aug 6) | `## Theme Clusters` headings present in tail | Extract decisions from the markdown tail; still run the Deep Sleep verification gate. Do NOT re-triage from scratch |
| **Cluster-less** (Nov 15) | Headings are only the skill dumps + `## Script Output` + `# TOKEN USAGE TRACKING`; checkpoint `articles: []`, `total_articles: 0` | **Skip the tail read entirely.** Go straight to Pattern E via `check_archive_index_absence.py`. A stale `triage_latest.json` from a prior consumed run confirms there is no pending triage to honour |
| **503 upstream** (Aug 22, Nov 14 sibling) | Pre-run error is `HTTP 503: Local LLM server is busy`, not truncation | Pattern E over the whole **backlog**, not just today's sitemap batch (see the 503 variant in Pattern E) |

## Root cause (structural, not model flakiness)

`dreaming-group` is an agent cron job, so the cron runner injects the entire checkpoint into
its prompt — including `existing_wiki_pages`, which was ~2,900 slugs (~250 KB). The grouping
agent must echo the injected data back in its response, so it burns its whole output budget
reproducing the slug list and **never emits clusters**. Error text:
`RuntimeError: Response truncated due to output length limit`.

**Chronic**: blog-wiki-ingest + newsletter-wiki-ingest hit the same class on 2026-11-14 (they
wrote pages then died before indexing — the 11-14 watchdog had to register 4 orphaned pages).
dreaming-group hit it 2026-11-15.

**Root-cause fixes for whoever touches the pipeline** (not yet applied):
- Compress `dreaming.py`'s `existing_wiki_pages` output to a count + hash rather than the full
  slug list — the grouping stage does not need 2,900 slugs to cluster an empty article pool.
- Cap the grouping stage's output contract to cluster names + 200-char summaries.

## Worked example — 2026-11-15

- Output file `/opt/data/.hermes/cron/output/c4a9e8d2f671/2026-11-15_18-19-17.md`: 5,341 lines,
  435 KB. Headings were only the loaded-skill dumps (`## Integration Points`,
  `## Key Pitfalls`, …), `## Script Output`, `# TOKEN USAGE TRACKING`, `## Error`. No clusters.
- Checkpoint `20261115T180026Z`: `total_articles: 0`, `rss_articles: 0`, `newsletter_articles: 0`,
  `recent_raw_articles: 251`, `existing_wiki_pages: 2900+`.
- `triage_latest.json` stale: `checkpoint_run_id: 20261113T180045Z` (consumed by the Nov 13 cycle).
- No dreaming commit between 17:00 and 19:00.
- → Pattern E. `check_archive_index_absence.py`: **59 never-archived of 118** recent raw files.

Yield after reading bodies and grepping real page content (not just `sources:` frontmatter):

| Verdict | Items |
|---|---|
| **take → new page** | Sierra "Releasing Personal Agent Protocol 1.0" → `concepts/personal-agent-protocol-poppy.md`. `entities/sierra.md` carried one Poppy sentence (Oct announcement, 50+ partners); zero hits for "Personal Agent Protocol" in `index.md`; the sibling Decagon PACT raw (Oct 7) also never got a page |
| **take → page update** | Dwarkesh "The avalanche that hit math is coming for AI development" (45 KB) → new section in `concepts/recursive-self-improvement.md`. That page had the Aug Greenblatt debate (median 2031) + METR 2x + Nov production adjacencies, but **none** of the Nov-14 specifics: median 2028, 25% tail past 2032, 50x calendar work, top-50-researchers-are-80%-of-progress, software-only-singularity vs spark split, RL-environment transfer thesis |
| **skip, already covered** | subtext-skills (full description already in `entities/bryan-bischof.md` L192), jepa, perplexity-decider, unsloth, smolmaxxing, monad weight-editing, replit microVM, borretti, hugotunius, nesbitt — all processed by 11-14 watchdog orphan registration or 11-15 siblings |
| **batch-skip** | Hex x5, ElevenLabs x3, Harvey x4 + 3 `/blog/author/` profile pages (zero body), Modal x Gray Area art exhibition, OpenAI latency docs guide, johndcook x4, dfarq x3, filfre, shkspr, bernsteinbear, Marcus x2, Ed Zitron, sharptext, pluralistic, matduggan, 2 bodyless x.com tweet stubs |

Result: takes 2 / refs 4 / skips 51, commit `ce63d66c` (7 files, +206/-5), both pre-commit hooks
green with no `--no-verify`, archived 5 skip decisions.

## Tag gotcha encountered (page-name != tag, 8th-family instance)

Tagged the new Poppy page `sierra` — an entity page's own name, which is **not** a SCHEMA tag
(`grep -cw sierra wiki/SCHEMA.md` -> 0). Caught by the pre-commit whole-word gate before
committing. Same class as `agentic-commerce`, `responsible-scaling`->`responsible-scaling-policy`,
`lean`->`formal-methods`, `legal`->`law`. Cheapest prevention: whole-word grep EVERY planned tag
— including any lifted from a Related-link target or an entity page's filename — before writing
the page. Fixed by dropping `sierra` (already conveyed by the `[[entities/sierra]]` wikilink)
and adding generic `company` / `product` / `ai-agents`.

## Do-not list

- Do NOT force a take just because the grouping stage produced nothing. A fully-covered backlog
  reached through Pattern E is a legitimate Takes=0.
- Do NOT hand a cluster-less output file to a subagent to "summarise the analysis" — there is no
  analysis, and the 435 KB pollutes the subagent's context for nothing.
- Do NOT trust `wc -l` as a "the analysis completed" signal.
