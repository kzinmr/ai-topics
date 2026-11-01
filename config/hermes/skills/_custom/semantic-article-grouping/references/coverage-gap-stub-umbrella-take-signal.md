# Coverage-gap verification: stub umbrella + absent sibling = strong take

**Pattern (2026-11-01 blog-triage, Parameter Labs ChatGPT HTML-preview account takeover):** When a security / vulnerability / incident article arrives and `search_files` finds no dedicated page, do NOT downgrade to "already covered by an entity page" just because a *related* entity page mentions an analogous incident. Run a two-sided check:

1. **Token-level direct-coverage grep.** Grep the incident's distinctive tokens (attacker org name, product surface, exploit primitive — e.g. `parameter labs`, `html-preview`, `postmessage`, `oembed`) across `entities/ concepts/ events/`. Zero hits = no direct coverage, regardless of what adjacent pages contain.

2. **Sibling-cluster existence probe.** Check whether the *class* of page already exists — e.g. `ls concepts/ | grep -i cve` finds `cve-2026-55607-claude-code-sandbox-escape.md`, and `ls concepts/ | grep -i sandbox` returns dozens. Presence of the sibling cluster proves:
   - the taxonomy has an established home (`events/YYYY-MM-DD-...` for incidents, `concepts/...` for mechanisms), so a `candidate_wiki_path` naming that convention is valid,
   - the wiki has an appetite for this class of article — don't skip just because this specific incident is niche.

3. **Stub-umbrella corroborator.** If the natural umbrella concept page is `status: stub` (frontmatter `status: stub`, <30 lines, body is only `> **TODO**: Enrich this page.` plus an `_index` wikilink), that is *corroborating* take evidence, not a skip signal. Observed: `concepts/browser-security.md` = 25 lines, `sources: []`, TODO placeholder — proof that browser-sandbox security class has never been synthesized in this wiki.

**Decision rule:** token-grep 0 hits + sibling cluster exists + umbrella stub → **take (new page)** at ★★★★☆, never downgrade to reference. Token-grep 0 hits + sibling cluster absent + no stub → likely greenfield concept, consider `wiki-concept-from-research` skill instead of an `events/` page.

**Concrete anti-pattern avoided this session:** an entity page (`entities/gergely-orosz.md`) carried a full "Instagram account-takeover exploit (June 2026)" subsection. A naive "account takeover already covered" heuristic would have skipped the ChatGPT incident. The token grep (`parameter labs` → 0 hits) plus the fact that Orosz's Instagram case is a *different product, different vendor, different attack chain* is what kept it a take. **Analogous-incident-in-entity-page ≠ incident covered.** Read what the entity page actually documents (product, vendor, primitive) before calling it coverage.

**Naming:** for a dated security incident, the wiki convention confirmed live is `events/YYYY-MM-DD-<subject-slug>` (e.g. `events/2026-10-30-nvidia-deepseek-v4.1-flash-nvfp4`, `events/2026-10-31-chatgpt-html-preview-account-takeover`) — grep log.md for the newest `events/` line before picking a path so the slug style matches.

---

## Freshness of the "stale checkpoint" signal vs. same-day raw-save commit

`triage_latest.json` staleness (mtime / `checkpoint_run_id` from a prior day) is the *primary* "batch not yet triaged" signal. Two same-day git signals that look like consumption but are NOT:

- A `wiki: blog-ingest ... N raw articles` commit → SAVING only. `git show --stat` will show only `raw/articles/*` files. Never treat as triage consumption.
- A `wiki: newsletter triage report <run_id>` commit → verify with `git show --stat` whether it committed only `raw/inbox/newsletter-ingest/<run_id>.json`. If yes, it's not downstream consumption.

Only a `wiki: blog triage report <matching-run-id>` commit that includes `raw/archived/triage/blog/<date>_<run_id>.json` + `archive_index.json` counts as batch consumed. Cross-check against `latest.json`'s `checkpoint_run_id`, not the file mtime.

## `search_files target='files'` regex gotcha (re-confirmed 2026-11-01)

Confirmed again: `search_files target='files'` is content-regex, NOT filename glob. `find ~/ai-topics/wiki/entities -maxdepth 1 -name "*keyword*"` via terminal remains the correct filename probe. For content-based existence of a topic keyword, use `grep -ril "keyword" entities/ concepts/ events/` via terminal — it distinguishes "file with keyword in body" from "filename contains keyword" cleanly, which the tool's dual-mode semantics blur.

## Batch-skip grouping for single-author low-value batches (worked cleanly)

When a single blog source contributes 8+ items and NONE are AI-relevant (observed 2026-11-01: 15 danielwirtz.com PKM/lifestyle/productivity posts in a 18-candidate batch), group them into 3-5 thematic batch-skip entries rather than 15 individual ones:

- `batch-{source}-{theme}` item_ids (e.g. `batch-danielwirtz-pkm`, `-productivity`, `-lifestyle`, `-indiebiz`)
- One `title` field joins the titles with ` / `
- `raw_path` points to the longest / most-representative file (the one whose body_excerpt you actually quote)
- `body_excerpt` comes from that representative file
- `reason_ja` enumerates each member briefly with its byte size (e.g. "Bottom-Up Note-Taking 9,990B / Audio notes 2,435B / Readwise 668B") so downstream verification can reconstruct the group

Result: 10 decisions for a 20-article batch, `archive_triage.py` accepted all 6 skip+reference entries cleanly (candidates=6, new_archived=6, dedup_skipped=0). This is well under the ~20 soft target and keeps the JSON readable.
