# newsletter-wiki-ingest recovery patterns — 2026-11-03 (run 20261103T101038Z)

Validated during a cron run where upstream `newsletter-triage` failed with
`"failed to parse JSON response from newsletter-triage output"` but
`triage_latest.json` at `${HERMES_HOME}/cron/data/newsletter/triage_latest.json`
was valid, fresh (`checkpoint_run_id` matched today's batch), and consumed as-is.

## 1. Checkpoint-first recovery (reconfirmed)

- The failed output file at `cron/output/<job-id>/<timestamp>.md` is NOT needed.
  Verify the checkpoint instead: `checkpoint_run_id` matches the day's
  `newsletter_<runid>.json`, git log has no prior consumption commit for that
  run_id, then proceed directly to Post-Recovery Verification.
- Verify with a hardcoded-path `python3 -c` (no pipes): decision counts, per-item
  `recommended_action`, `candidate_wiki_path`, `body_excerpt` presence.

## 2. Re-fetch post bodies at INGEST time for substack takes

Raw newsletter files under `wiki/raw/newsletters/` are **link-only digests**
(tracking URLs, no body). When the triage agent resolved post bodies during its
run but never persisted them, the ingest agent MUST re-fetch before writing
pages — never write a take page from `body_excerpt` alone (200-300 chars).

Working pattern (cron-safe: `write_file` to /tmp + `terminal python3`, no
subprocess-in-execute_code):
- `curl -sL` with a desktop User-Agent on the canonical publication domain
  (`www.lennysnewsletter.com/p/...`, `importai.substack.com/p/...`,
  `www.chatprd.ai/how-i-ai/...` — all resolved 200 with full text).
- Extract `<article>` block, then all `<p>` tags, strip tags, unescape common
  entities, keep paragraphs > 40 chars. Yield: Lenny post = 30 paragraphs,
  chatprd.ai Figma article = 44, Import AI = 17 (all sufficient for full pages).
- Podcast "How I AI" posts embed BOTH episodes' full summaries in one post page
  — one fetch covered two takes.
- For arXiv-backed takes, also fetch `arxiv.org/abs/<id>` to verify title,
  authors, date, abstract before quoting numbers (the triage's "36% pass rate"
  was actually the Pass^3 figure per the abstract's 44% success / 36% Pass^3 —
  caught and noted on the page rather than copied wrong).

## 3. Triage `candidate_wiki_path` is advisory — re-route to canonical locations

Triage suggested `concepts/realtime-bench.md` for a benchmark. AGENTS.md mandates
all benchmark pages under `concepts/ai-benchmarks/`. Downstream ingest must
override the triage path when it conflicts with repo layout rules, and update
index.md in the correct alphabetical section.

## 4. git pull --rebase blocked by sibling unstaged changes → plain commit

Sequence that worked (sibling pipelines running in parallel leave unstaged files):
1. `git pull --rebase` failed: "cannot pull with rebase: You have unstaged changes."
2. Do NOT stash (risks sweeping sibling work). Just `git add <targeted paths>` +
   `git commit` — succeeded because remote had no new commits.
3. `git push` — plain push works even when pull --rebase was blocked. If push is
   rejected afterwards, only then coordinate (fetch, re-check status).
Commit-first is the working order, not pull-first.

## 5. Sibling `_warning` on patch/write_file — false positives

`write_file`/`patch` return `"...was modified by sibling subagent <uuid> but this
agent never read it"` even when the file was read earlier in the session via
terminal `cat` (which the tracker doesn't count). If you genuinely inspected the
file's current content this session, proceed — the warning is advisory. Confirmed
twice (duet concept page, index.md) with no data loss.

## 6. Unresolved-lead pattern for Cloudflare-blocked beehiiv reference items

Reference items with unreachable bodies go into
`wiki/queries/unresolved-newsletter-leads.md` as a table block (Subject/Sent/Raw/
Links/Body access/Triage decision) + topic-level assessment + numbered
"To resolve this lead" steps; bump frontmatter `updated:` and append the raw file
to `sources:`. Newest-first placement directly under `## Open leads`.

## Yield this run
4 newsletters / 76 links → 3 takes (2 new pages, 1 existing-page section), 1
reference (durable lead), 8 batched skips. Archive: 9 items, dedup_skipped=1.
Commit 1e3e338d pushed; pre-commit hooks passed without --no-verify.
