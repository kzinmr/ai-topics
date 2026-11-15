# Trending batch run — 2026-11-15 (Sunday noon)

Clean run: ~30 tool calls, **1 commit (22 files), BOTH pre-commit hooks green on the FIRST try** (zero hook round-trips), 9/10 primaries fetched + 10/10 HN comment trees mined.

## What was new vs. sibling jobs

By 12:00 UTC the morning pipelines had already taken nearly everything:
- active-crawl 11:00 → Claude Code Projects, agweb, dual-DGX GLM-5.3, end-to-end 4-bit training, DRAM price-fixing (its log entry even lists deferred topics — read it, it saved re-proposing OpenAI robotics-team disbandment, which it had also deferred for the same paywall reason).
- newsletter-wiki-ingest 10:10 → Nvidia CEO transition + Nathan Lambert "Open-source AI without Jensen" (so the Lambert HN reception was an *append to an existing section*, not a new page).
- hot-post 09:30 → Replit microVM; health-fix 11-14 → Unsloth/Qwen3.8.

Genuinely new (3 pages): Lovable data-exposure audit, EFF ambient-surveillance essay, Google Search AI-free-schools cutoff. Updates (5): circular financing (WSJ Kress profile), ai-slop (No AI Slop Manifesto), google-antigravity (/teamwork), nathan-lambert, claude-code-projects (syllabus-deletion incident note).

## Working recipes confirmed

- **Combined fetch+mine script** (`fetch_and_mine.py`): TARGETS list + IDS dict in ONE write_file, one terminal run → 9/10 OK + 10/10 comment trees. techpowerup.com returned 239 chars (chrome-only) → the TechSpot mirror of the same WSJ report is the usable carrier; do not retry techpowerup.
- **Weekend points-only sweep** (`points>100`, last 24h) was again the higher-yield half: caught EFF-privacy (558), Italy/Meta, IRS Direct File, Lean tax code, Antigravity /teamwork — none matched the keyword list.
- Guardian paywalled → saved as HN-thread reconstruction raw with a "article body not fetched" gloss in **English** inside the raw, JP form only in the report.
- SCHEMA mints inside the batch script (regex the category line, whole-word dedup, append) → zero hook fires. Two-pass sha256 with `sha256: pending` placeholder.

## New pitfall caught: the gate script's own key-extraction bug

When post-processing a Related-section fix script, the existence check was written as

```python
key = b.split(']]')[0][2:]        # b == '- [[concepts/ai-adoption]] — ...'
```

`b.split(']]')[0]` keeps the `[[`, so `[2:]` strips the **`- `** instead of the brackets → key becomes `[[concepts/ai-adoption`, the `os.path.isfile` check always fails, and every bullet silently prints "SKIP non-existent target" without inserting anything. Symptom: script reports "SKIP" for links whose targets definitely exist. Correct: `key = b.split(']]')[0].split('[[')[-1]` (or `re.search(r'\[\[([^\]|]+)', b)`).

Corollary: never trust a link-fix script's SKIP output — always re-run the independent wikilink sweep afterward (it is what caught this: `GHOST concepts/ai-adoption` survived two "successful" fix runs).

## Pre-existing wikilink damage observed

`entities/nathan-lambert.md` had several **empty wikilinks** in its Related list (`-  — Open post-training model family he leads`, `-  — Previous employer, Zephyr and TRL work`) — target text dropped by some earlier patch, bullet text orphaned. Also `[[concepts/post-training]]` → real page is `concepts/post-training/_index.md` (the documented subdir-hub shape, 4th sighting). Flag for wiki-graph-health: grep `wiki/ -n '^-  — '` (empty link) across entities/ for the blast radius.
