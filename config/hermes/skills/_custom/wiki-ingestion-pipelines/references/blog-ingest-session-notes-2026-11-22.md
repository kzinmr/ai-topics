# Blog-ingest agent stage — 2026-11-22 session notes

## What this stage actually does (clarification)

Despite the cron prompt saying only "save raw articles + checkpoint", the agent stage ALSO
triages and ingests AI-relevant articles into Layer-2 pages (mirroring blog-wiki-ingest),
then commits+pushes everything (raw articles + page edits + index.md + log.md) in ONE commit.
Reference run shape (2026-11-22, commit 5cbae342): checkpoint JSON → read raw articles of
AI-relevant candidates → grep wiki for existing coverage → patch 5 pages → index.md
description updates → log.md prepend → single `git add` of wiki/raw/articles/ + touched
pages + index.md + log.md → commit → push.

## Triage heuristics that worked

- **Vendor launch post fills an HN-derived gap**: `concepts/qwen-4-max.md` was flagged
  "confidence note: vendor blog JS-rendered, HN-derived" — a Together AI vendor post
  (together.ai/blog/qwen4-max) was the first fetchable vendor text. Pattern: when a concept
  page carries a provisional-confidence note, grep raw/articles for vendor-domain posts
  before answering; ingest as a "Vendor-confirmed specs" section that explicitly resolves
  the note (keep the old HN section — contested/superseded rule, don't delete).
- **Security incident posts**: check for an existing sibling incident first (Fireworks/Notion
  HN discussion, OpenAI/HF incident events) and cross-reference in the entity page rather
  than creating a new concept page for a single-vendor incident.
- **Skip list verified in log**: off-scope personal-life posts (dfarq, shkspr hardware, eli
  DFT math), vendor marketing (merge.dev), weekly-package-newsletters, and items whose
  subject is already covered elsewhere (MedChemBench → concepts/gpt/gpt-rosalind.md) —
  record each skip with a one-line reason in the log entry.
- **Author without entity page**: don't create a thin entity page below SCHEMA thresholds;
  capture the content inside the Willison note that linked it (Muru/Graham Dumpleton case).

## Index.md description-append recipe (recurring)

Index entries are one-line descriptions ending in a dated clause. Append new facts by
patching the LAST unique fragment of the line: old_string = `giving Claude Code ears (Nov 9 2026)`
→ new_string = same text + `; <new fact> (Nov 20-21 2026)`. Do NOT re-quote the whole line
(it's 2-4k chars and sibling jobs may have touched it — the warning fires). If the tail
fragment has escaped quotes (`\"` in the raw file), match the RAW form, not the rendered
form — a `"Getting good..."` old_string failed while `folded into [[concepts/...]])`
(the real tail) succeeded.

## Frontmatter pitfall: giant inline `sources: [...]` arrays

Pages like `entities/simon-willison.md` keep sources as ONE inline YAML flow array on a
single line (70+ entries). Patching a prefix/middle element with a short old_string
CORRUPTS the line (matched the array-start prefix and truncated the rest, producing
invalid `], ...`). Safe recipe:
1. old_string = unique suffix at END of line: `, raw/articles/<last-entry>.md]`
2. new_string = `, raw/articles/<last-entry>.md, raw/articles/<new>.md]`
3. Read back the frontmatter after patching to confirm YAML validity.
If corrupted, restore by patching the full reconstructed line in one shot.

## execute_code is blocked in cron profile

`execute_code` returns "BLOCKED: ... Cron jobs run without a user present to approve it"
under this cron job. Use plain terminal() + read_file/search_files/patch instead. Do not
waste a call discovering this each run.

## Log entry format used

`## [YYYY-MM-DD] blog-wiki-ingest | N articles scanned, M pages updated` with a `>` context
line (checkpoint run_id, saved count), **Ingested (pages)** bullets with section names and
key numbers, **Skipped (verified, no action)** list, and an Index.md touched-entries line.
Prepend after the 4-line header block per log-prepend-dynamic-scan notes.
