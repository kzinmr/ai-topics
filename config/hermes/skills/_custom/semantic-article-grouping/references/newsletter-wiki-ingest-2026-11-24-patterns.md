# newsletter-wiki-ingest patterns — 2026-11-24 (Import AI 482, run 20261124T101044Z)

## 1. Inbox item completely ABSENT from triage candidates (undisclosed triage drop)

The inbox pre-triage summary (`wiki/raw/inbox/newsletter-ingest/<run_id>.json`) classified a
second newsletter ("History made: math's biggest problem solved, with Claude's help", beehiiv
uid=937) as **critical**, but the triage `decisions` array contained ONLY Import AI 482 items —
the critical item was silently never triaged. The triage summary count (`total=9 takes=3 refs=2
skips=4`) matched its own decisions array, so internal consistency does NOT prove inbox coverage.

**Checklist every ingest run (adds ~1 min):**
1. Read inbox summary JSON; extract `items[].subject` set.
2. For each inbox item, confirm at least one decision shares its `raw_path` or subject keyword.
3. Missing item → attempt rescue: resolve tracking links (batch-test ONE beehiiv link; 403 =
   whole batch expired, do not retry per existing guidance).

## 2. Check the actual tool list BEFORE attempting web research

In this cron profile `web_search` and `web_extract` do not exist as invokable tools (the tool
error lists what IS available: terminal, execute_code, read_file, etc.). Calling them blindly
wastes blocked-call attempts. Before any "search for the source" step, look at the tool-error
list once and fall back to `terminal` + curl.

**Also: DuckDuckGo html via curl is unreliable** — `https://duckduckgo.com/html/?q=...` returned
an empty page (zero result anchors) for a news query. Don't loop on scraper variants; one curl
probe, then declare the source unrecoverable in this session.

## 3. Degraded critical-item path: beehiiv-403 + no search tools → LOG, don't force

When ALL of: (a) every beehiiv tracking link 403s (expired tokens, batch-validated),
(b) inbox summary has `reason`/`suggested_wiki_targets` but no article body/key_claims,
(c) no web search/extract tools in the cron profile,
(d) the topic is adjacent to existing rich coverage (e.g. AI-math: erdos-unit-distance-problem,
claude-fable-jacobian-conjecture, alpoge-riemann-hypothesis event page) —

Do NOT create a speculative page from the subject line. Instead write a dated
"Unresolved / manual follow-up" bullet in the log.md entry naming the subject, uid, why it's
unrecoverable, and which existing pages cover adjacent ground. Same discipline as the skill's
"subject-line-only assessment" sub-case for triage — extended to the ingest stage.

## 4. index.md alphabetical insertion: verify neighbors, expect two-pass fix

`patch` anchored on the *following* line inserts BEFORE it — correct for alphabetical order — but
anchoring on a guessed neighbor can land the entry at the wrong spot (ascendgym landed between
benchjack and benchmaxxing on pass 1). Cheap protocol: `grep -n` the two neighboring slugs first,
insert after the true predecessor line, then `grep -n` to confirm placement in the same terminal
call. Re-patch (delete + re-insert) is fine and cheap.

## 5. Git: `git status --short --cached` is invalid

`--cached` is not a `git status` option. To inspect what is staged before committing:
`git diff --cached --stat`. Targeted `git add <paths>` + that stat is the safe pre-commit gate.

## 6. Session outcome (for archive cross-reference)

- 3 takes applied as greenfield pages: `concepts/ai-benchmarks/ascendgym.md`,
  `concepts/ai-benchmarks/sciresearch-eval.md`, `entities/noeri.md` (all took-recommended paths
  confirmed absent via find+grep before creation; no overwrite risk).
- 2 references: A2A-UAV section added to `concepts/physical-ai.md`; Machine Hermeneutics Tech
  Tales section added to `concepts/monitorability-metrics.md` (triage had suggested
  `concepts/monitorability.md` — page absent, `monitorability-metrics.md` is the real slug;
  per post-recovery rule, never trust `candidate_wiki_path`, `find` first).
- Both page writes drew sibling-subagent warnings; re-verified each patch survived via
  `git diff HEAD | grep '^+'` per existing sibling-write guidance.
- Commit `913b2fd9f` pushed; index counts Entities 976→977, Concepts 2388→2390; log.md prepended
  via head-1/tail-+2 merge (log.md has no H1 issue avoided by anchoring on the `# Wiki Log`
  first line with explicit reconstruction).
