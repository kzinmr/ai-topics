# Newsletter triage patterns — 2026-11-22 (run 20261122T101113Z)

## Case: third newsletter in the same Anthropic-IPO series, body unreachable

Checkpoint: 1 beehiiv newsletter, 18 links, subject
"Anthropic just had the biggest IPO ever. How long will its lead last?" (uid=932, sent 2026-11-21).

### What happened
- No inbox pre-triage summary existed for this run (latest was `20261121T101055Z.json`, covering the
  *previous* day's uid=930/931 pair). So the degraded path applied: subject-line-only assessment.
- Sampled Link 1–4 via `curl -sL`: **all HTTP 403** with Cloudflare `Just a moment...` (6,853 bytes,
  0 paragraphs). Per the Cloudflare rule, no retry. This confirms the earlier finding that
  previous-day beehiiv tokens can be dead — trust the verdict, don't retry.
- Publisher could not be identified at all (raw file is pure opaque v2/c/ hashes).

### Decision shape that worked: 1 reference + 2 batch skips, 0 takes
Key signal: this was the **third** newsletter on the same Anthropic IPO story
(uid=930 The Signal → full body recovered, take; uid=931 → reference lead; uid=932 → this run).
The event pages were already saturated:
- `events/anthropic-nasdaq-debut-2026.md` (89 lines: $83 pricing, $81.3B/$107.3B raised, ~$1.5T valuation,
  $111.53 first-day peak, RSP "met" flip, NRR ~900%, SpaceX $120.5B compute, day-2 collapse / $4T wipeout,
  contestation section with Gary Marcus / Ed Zitron / protest coverage)
- `events/anthropic-ipo-roadshow-2026.md`, `concepts/ai-bubble-economics`

→ Subject-inferable topics ((a) record IPO, (b) "how long does the lead last" skepticism) were both
already covered. **Reference** → append to the existing uid=931 entry in
`queries/unresolved-newsletter-leads.md` rather than minting a new lead per issue. Skips collapsed into
one batch entry for the 16 remaining v2/c/ links + one for the `beehiivstatus.com/hclick` pixel.

### Reusable rule
When a checkpoint is the **Nth issue of the same story** (check `log.md` + `unresolved-newsletter-leads.md`
for prior uids on the same subject) AND bodies are unreachable: do not create a new lead entry per issue.
Attach to the existing lead, keep takes=0, and use batch-skip grouping so the decisions array stays ~3 entries.

### Also validated this run
- `candidate_wiki_path` must be verified against the **absolute** wiki root `/opt/data/ai-topics/wiki/`
  (cwd-relative checks give false negatives).
- `archive_triage.py newsletter --keep-reference` prints a nested-looking
  `/opt/data/.hermes/home/ai-topics/...` path — it is a symlink to the canonical repo; leave it alone.
- `archive_index.json` is left modified after archiving and needs its **own** targeted `git add` + commit
  (it was not picked up by the first commit).
- Triage builder written via `write_file` → `terminal python3` (cron mode), gated with
  `python3 -c "import ast; ast.parse(...)"` first. Japanese literals used 「」 instead of ASCII quotes.
