# Newsletter Wiki Ingest 2026-08-20 — Recovery Run

Session: newsletter-wiki-ingest run 2026-08-20, checkpoint 20260820T101038Z (2 newsletters: AINews/swyx Substack + beehiiv uid=526). Pre-run script reported `failed to parse JSON response from newsletter-triage output` (output `/opt/data/.hermes/cron/output/4e8b0d92c6a1/2026-08-20_10-41-27.md`).

## Outcome

Takes=1 (enriched `concepts/glm-5-3.md`), reference=1 (beehiiv "OpenAI Hits the Brakes on Itself" — all 20 links unresolvable, no wiki change), skip=2 (UI noise). Commit `3be32389`, pushed to main.

## Recovery details

1. Triage checkpoint `triage_latest.json` was valid and same-day (checkpoint_run_id=20260820T101038Z matched `latest.json` run_id) — proceeded directly from it; no upstream re-run.
2. Verify-take: `concepts/glm-5-3.md` existed (created Aug 14, updated Aug 15/16 with Lambert analysis + Superintel+ post-training economics) and `grep "Death of Params\|Jie Tang\|Post-training Scaling Law"` returned 0 hits in the page body — genuine gap, not a false-positive sources-ref.
3. Body fetch: raw newsletter digest contained only Substack tracking URLs; fetched canonical `https://www.latent.space/p/ainews-death-of-params-zai-ceo-jie` via curl + `<article>` extraction → 42 paragraphs (first para = chat-UI noise). Full Jie Tang quote + AINews analysis available.
4. Enrichment: `patch` (NOT write_file — page was 163 lines) inserted new section "Death of Params: Jie Tang on the Post-Training Scaling Law (Aug 2026)" before `## Related Pages`; frontmatter `updated: 2026-08-15 -> 2026-08-20` + raw digest appended to `sources`. No index.md line needed (page already indexed; summary still accurate).
5. log.md entry inserted after the subtitle block via /tmp script (English-only policy).
6. `archive_triage.py newsletter --keep-reference` → 3 new archived items (total 2,755 URLs). Script printed a path under `/opt/data/.hermes/home/ai-topics/...` — confirmed symlink to canonical repo, did not move.
7. Git: targeted `git add` of the 5 wiki files (concepts page, log, 2 raw digests, archive JSON + archive_index.json). Commit passed tag validation. `git pull --rebase` FAILED with "cannot pull with rebase: You have unstaged changes" — sibling blog-wiki-ingest job had unstaged entity pages (cursor-ai, decagon, harvey, nvidia, openai, together-ai). `git push` succeeded anyway (e7248f63..3be32389, no remote divergence) — no action needed.

## Lessons

- Checkpoint-first recovery worked exactly as the skill prescribes; the parse failure was response-rendering only.
- Targeted `git add` was essential: 6 sibling entity-page modifications stayed out of the commit.
- pull-rebase failure + successful push is a benign end state in the parallel pipeline window — do not stash/commit sibling work.
