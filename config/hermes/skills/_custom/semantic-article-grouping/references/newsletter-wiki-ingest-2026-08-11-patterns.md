# Newsletter Wiki-Ingest 2026-08-11 Patterns

Run: newsletter-wiki-ingest 2026-08-11 (Case C2 recovery — triage checkpoint valid). 5 newsletters, 24 decisions (3 take, 11 reference, 10 skip).

## Recovery → Ingest full path (validated end-to-end)
1. Pre-run script reported `failed to parse JSON response from newsletter-triage output`.
2. Read `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` directly — valid, saved 10:40 (before the response-render failure). No extraction, no re-run.
3. Archive already written by the triage agent (`wiki/raw/archived/triage/newsletter/2026-08-11_20260811T101956Z.json`) — do NOT re-archive; verify existence first with `ls wiki/raw/archived/triage/newsletter/2026-08-11*`.
4. Post-Recovery Verification of all 3 takes via section-grep (not filename-existence): jack-clark.md had no IFP/PostTrainBench+; openai.md Daybreak section stopped at GPT-5.5-Cyber; openai-astra.md "Critical" appeared only in the Gary Marcus critique context. All three were genuine gaps → proceed.
5. Parallel enrichment: takes in one block of 3; references in blocks of 3. Here 11 references → 4 delegate calls (3+3+3+1). Two references targeting the SAME page (claude-code.md: Grace Clarke + Boris Cherny) were combined into ONE task to avoid parallel same-file write conflicts.

## log.md consolidation (new technique — parent-level entry)
- Parallel enrichment subagents MAY append their own log.md entries even when instructed not to (observed: 4 of 9 subagents appended — trusted-access-biodefense, personal-superintelligence, sonnet-5, jack-clark+recursive-self-improvement; anthropic added a per-page `## Log` section instead).
- The parent then prepends ONE consolidated pipeline entry: `## [YYYY-MM-DD] newsletter-wiki-ingest (HH:MM) | N takes + N references (Case C2 recovery — triage checkpoint valid)` listing all takes+references, closing with a note that some reference log entries were appended individually by enrichment subagents (avoids confusion when future sessions grep log.md).
- **Marker-based insertion, not raw prepend**: insert after the `_Log of all wiki changes. Newest entries at top._` header line (find marker, insert at marker+len). Raw prepend would push the entry ABOVE the header and break the file's structure.
- The `/tmp` unique-filename rule extends to log-prepend scripts too: `/tmp/prepend_newsletter_log.py` hit the sibling-race warning; use `/tmp/prepend_newsletter_log_<runid>.py` (this was in the blog-wiki-ingest pipeline window — blog-ingest/newsletter-ingest siblings share /tmp).

## Beehiiv tracking URL version bump: v2/c/ (Aug 2026)
- Superintel+ (uid=489, "The Model OpenAI Won't Release", Aug 10 2026) used `link.mail.beehiiv.com/v2/c/...` tracking URLs — NOT the `v1/c/` documented in the main SKILL.md table.
- Resolution succeeded (triage produced body excerpts: Astra Critical rating, Evo viruses, Gemini revenue, ABN AMRO/Mistral, Cherny account suspension). v2/c/ URLs are resolvable, not expired-token 403.
- Treat `v1/c/` and `v2/c/` identically in the beehiiv filtering table.

## Raw newsletter files remain link stubs
All 5 raw files were link-only digests (substack redirect UUIDs / beehiiv v2 tracking). Triage facts + body_excerpts in the triage JSON were the sole content source for enrichment — pass them in the subagent context (per `newsletter-triage-enrichment-facts.md`) and have subagents verify frontmatter + target page structure independently.

## Commit stats
15 files changed, +273/−22, tag validation passed. Commit 0634ee94 pushed to main.
