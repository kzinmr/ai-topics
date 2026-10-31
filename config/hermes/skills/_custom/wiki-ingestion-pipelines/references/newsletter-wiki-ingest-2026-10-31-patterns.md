# Newsletter wiki-ingest session notes — 2026-10-31 (run 20261031T101822Z)

Recovery case: `newsletter-triage` output failed to parse (`failed to parse JSON response`),
but `triage_latest.json` was valid and fresh. Executed ingest from checkpoint; committed 3a8e3612.

## Technique 1: Ingest-side full-body re-fetch for take-as-update items

The triage JSON's `body_excerpt` is only 200–300 chars — NOT enough to write a quality
enrichment section. Re-fetch full bodies yourself before editing wiki pages:

- **Substack canonical-domain curl + `<p>` extraction**: `curl -sL` with a browser
  User-Agent against the publication's custom domain (e.g.
  `robotic.substack.com/p/was-i-wrong-about-open-models-and`,
  `www.aibyaakash.com/p/claude-duet-review`), then regex `<p[^>]*>(.*?)</p>`,
  strip tags + entities (`&amp; &#x27; &quot; &nbsp; &gt; &lt;`), keep paragraphs
  > 60 chars. Returned the FULL body (27 and 104 paragraphs) on the first try for both
  publications. Note: the `open.substack.com/pub/{pub}/p/{slug}` variant also returned
  the same 104 paragraphs — either works; custom domain is preferred.
- JSON-LD `<script type="application/ld+json">` extraction yielded nothing useful here
  (headline not parsed) — the `<p>` extraction alone was sufficient. Don't waste time
  on JSON-LD first when you only need the body.
- Cron-mode safe pattern: write the fetch script to `/tmp/` via write_file (unique
  filename, e.g. `/tmp/fetch_bodies_1031.py`), run via `terminal python3`. One script,
  multiple URLs, results dumped to `/tmp/*.json` for inspection.

## Technique 2: Upgrade raw tracking-URL stubs in place

The checkpoint `raw_path` files (e.g. `wiki/raw/newsletters/2026-10-30-was-i-wrong...md`)
were 94-byte-style stubs containing ONLY lists of substack redirect/app-link URLs — zero
article content. After re-fetching bodies, overwrite the stub with the extracted content +
proper frontmatter:

```yaml
---
title: "..."
date: 2026-10-30
author: ...
publication: ... (Substack pub id if known)
canonical_url: https://...
source_label: "uid=858"
processed_at: 2026-10-31
retrieved_via: curl + <p> extraction from ... (full body, ~N paragraphs)
tags: [newsletter, raw]
---
```

This gives future dedup (archive_index.json, cross-pipeline grep) real text to match on.
For unreachable beehiiv content: keep a subject-line-only capture file with
`tags: [newsletter, raw, paywalled]` and an explicit "do NOT cite for technical claims"
warning + follow-up-needed note.

## Technique 3: Beehiiv 403 at ingest time = confirm-and-record, don't grind

A single re-test of one beehiiv v2/c/ tracking link (curl with browser UA) returning
HTTP 403 + `<title>Just a moment...</title>` + no redirect chain confirms the triage
verdict. Per skill guidance this is an expired token / Cloudflare wall — do not retry
the rest. Convert the reference decision into an "unresolved lead" bullet on the target
concept page (what the subject line implies + which wiki event it likely responds to +
retry-when instructions) instead of leaving it as a bare archive entry.

## Technique 4: Sibling-subagent `_warning` handling

Multiple patches returned `was modified by sibling subagent '<uuid>' but this agent
never read it`. The parallel sibling pipelines (blog-wiki-ingest etc.) touch overlapping
entity pages (simon-willison, andrew-nesbitt appeared as pre-existing uncommitted edits
in git status). Resolution that worked: check `git status --short -- <file>` +
`git diff --stat` BEFORE and AFTER each patch — if the line delta matches exactly what
your patch added, proceed. Do NOT re-read whole 900-line entity pages; verify via diff.
Commit with a TARGETED `git add` file list (never `git add wiki/`) so sibling
work-in-progress is not swept into your commit. In this run ~40 modified/untracked wiki
files from siblings coexisted in the tree; targeted add committed cleanly.

## Technique 5: Secondary-source financial claims in entity pages

When ingesting newsletter analysis of a primary document (S-1 filing) that the wiki
already has as a raw article: create a subsection under the existing primary-source
section, open with an explicit `⚠️ secondary source, newsletter commentary, not verified
against the filing itself` marker + wikilink to the raw file, and add a reconciliation
sentence tying the numbers to any contested valuation threads already on the page
(here: $65B run-rate vs the FT/Superintel+ $100–120bn projection vs $1.5–2T IPO range).

## log.md

Prepended per the no-H1-title anchor rule (file starts directly with `## [` entries;
the "# Wiki Log" heading mid-file is an artifact — anchor on the newest `## [` heading,
write entry to /tmp via write_file, merge with a heredoc-free python one-liner through
terminal). Consolidated single pipeline entry.

## Index

No new pages → index.md untouched (verified `duet-style-hierarchical-assistant` already
registered). Pre-commit hooks (validate_index + tag validator) passed without --no-verify.
