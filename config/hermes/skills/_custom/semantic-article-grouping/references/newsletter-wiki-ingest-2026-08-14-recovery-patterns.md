# Newsletter Wiki-Ingest 2026-08-14 Recovery & Reference-Verification Patterns

Session: newsletter-wiki-ingest cron, 2026-08-14, recovered from checkpoint after triage JSON render failure.

## Checkpoint recovery (re-confirmed)

- Upstream `newsletter-triage` agent response failed `failed to parse JSON response from newsletter-triage output`, but `triage_latest.json` at `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` was valid (19 decisions, run `20260814T102346Z`). Read it directly — no extraction, no re-run. This is the known pattern (also seen in dreaming Jun 17, newsletter Jun 22, blog Aug 10).
- The triage agent had ALREADY committed the archive (`d79e6d87`, `wiki/raw/archived/triage/newsletter/2026-08-14_20260814T102346Z.json`) before its render failure. Do NOT re-run `archive_triage.py` when a same-run archive commit exists — verify with `git show <commit> --stat` first.

## Reference false-positive — triage grep claims are not proof of absence

- Triage reference [8] (seangoedecke "How to keep thinking") said `entities/seangoedecke-com.md` had no mention ("grepで該当ファイル未確認"), but the entity page **already contained** a full "How to Keep Thinking (August 2026)" section (lines 438-450, sourced from `raw/articles/seangoedecke.com--how-to-keep-thinking--faf73de6.md`).
- **Lesson**: even when the triage explicitly states it grep-verified absence, the wiki-ingest must independently read the reference target page's content sections. When content is present → no-op (skip silently, do not touch the page). When genuinely absent → add a reference entry.
- Corollary: a triage reference that names an entity page with a real gap may be the *only* action for that item — always read the target page before deciding "nothing to do".

## Reference → missing page: create minimal skeleton entity

- Triage reference [7] (Lovable $13.3B valuation) pointed at `entities/lovable.md` which did NOT exist. Triage rated it ★★★☆☆ (reference-level, thin technical depth) but explicitly noted "スケルトン作成候補".
- **Lesson**: a `reference` with a `candidate_wiki_path` whose page is missing still warrants a **minimal skeleton entity page** (~30-40 lines: frontmatter + funding facts + significance + related wikilinks), NOT zero action and NOT a full take-level deep dive. Register it in index.md (alphabetical position + header count bump) and log.md.
- Skeleton must still meet SCHEMA rules: valid tags from taxonomy, ≥2 wikilinks to existing pages, sources frontmatter.

## Self-inflicted `|-` pipe corruption in index.md (agent-caused variant)

- When patching `wiki/index.md`, I copied the surrounding lines from `read_file` output (which shows `NNN|-` line-number prefixes) into the `new_string` — producing `|- [[entities/...]]` instead of `- [[entities/...]]`.
- **Detection**: the `patch` tool's returned diff shows `+|-` on the added lines. Check every `+|-` in the diff — if you didn't intend pipe-prefixed list items, fix immediately with a corrective patch (`- ` instead of `|- `). The pre-commit `validate_index.py` catches this too (`✓ wiki/index.md clean` message only appears when 0 `|- [` occurrences — verify with `grep -c "|- \[" wiki/index.md`).
- This is the agent-caused variant of the known read_file display trap; both manifest identically and must be fixed before commit.

## Superintel+ uid=502 variant

- Raw newsletter frontmatter `source_label: "uid=502"` for the "xAI's Grok 4.6 Released" issue — a uid not in the reference list (known: 266, 383, 386, 438, 443, 470, 480). Same characteristics as uid=443: beehiiv `v2/c/` tracking URLs resolving to `read.getsuperintel.com` article content, ~19-20 links with ~30% duplicate density, Link 1 = full article (~824KB), Link 3 = author X profile.
- All 19-20 links resolved HTTP 200 at ~15h after send (consistent with uid=443/470/480 Aug 2026 batch-resolvable pattern).

## Take verification: AINews-created event page lacking Superintel+ specifics

- `events/grok-4-6-launch.md` (created Aug 13 from AINews) was a genuine take because it lacked Superintel+ specifics: API pricing $2/$6 per M (vs Sol $5), AA Index 61 exact tie, AA-Briefcase Elo 1577, Cursor training-data contamination/CursorBench rebuild. The AINews page said "pricing materially below frontier peers" with no numbers.
- **Lesson**: "event page exists" ≠ "event page has the specifics". Same-event dual-source take-as-update applies (see `newsletter-triage-2026-08-14-patterns.md`). The specialized source (Superintel+) carries concrete numbers the bulletin lacked.
