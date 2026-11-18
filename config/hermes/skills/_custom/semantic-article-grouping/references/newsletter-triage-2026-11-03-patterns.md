# Newsletter Triage Patterns — 2026-11-03 (run 20261103T101038Z)

Batch: 4 newsletters / 76 links → 3 takes, 1 reference, 8 batch-skips. Downstream: newsletter-wiki-ingest.

## 1. Superintelligence (getsuperintel) — Cloudflare-403 variant ⇒ direct-slug recovery DOES NOT apply

Two distinct beehiiv failure modes, with DIFFERENT recovery paths — do not conflate:

| Failure mode on tracking URL | Direct-slug probe (`read.getsuperintel.com/p/{slug}` / `getsuperintel.site/p/{slug}`) | Action |
|---|---|---|
| HTTP 403 (expired token) | Returns 200 for ANY slug → JSON-LD description + free-preview `<p>` = usable triage body (see `getsuperintel-403-direct-slug-recovery.md`) | Use JSON-LD recovery |
| HTTP 200 + `<title>Just a moment...</title>` (Cloudflare challenge) | Returns a ~203KB beehiiv GENERIC 404 template: title "Superintelligence — The Daily AI Briefing", ZERO `application/ld+json` blocks, single `<p>` = "Please check the URL in the address bar and try again." | **Stop. Do not iterate slug guesses.** Every guessed slug hits the same generic template. |

Confirmed 2026-11-03 (uid≈869 "Who Is Hacking Europe's Supermarket Freezers?"): Links 1 and 2 both Cloudflare-challenged; three slug variants (`who-is-hacking-europes-supermarket-freezers`, trailing-dash, `.site` domain) all returned the identical 203,149-byte generic template. With no inbox pre-triage summary for the day, escalate directly to: subject-line-level assessment + `reference` decision with `candidate_wiki_path: queries/unresolved-newsletter-leads.md` (durable lead for later canonical-URL discovery).

Detection one-liner for the generic template: html contains "Please check the URL in the address bar and try again." and `html.count('application/ld+json') == 0`.

## 2. Import AI 479 (pub 1317673) — full body via `importai.substack.com/p/{slug}` curl

`open.substack.com/pub/importai/p/...` was not needed; the custom-domain `importai.substack.com/p/import-ai-479-spacewar-low-latency` returned 186KB with 17 substantive `<p>` paragraphs via `<article>` extraction — enough for BODY-READING MANDATE on all sections. Jack Clark's per-section intros (2-4 paragraphs each) are sufficient for take/reference decisions without fetching each curated URL.

Take from this issue: **Realtime-Bench** (arXiv:2610.22155, realtimeagents.org) — low-latency dynamic tasks (games, online auctions) where LLMs fail; zero wiki hits for "realtime-bench" (do not confuse with `concepts/openai/realtime-api.md`, which is the voice API). Genie 4 section was a false take-signal: `concepts/genie-4.md` (Oct 28, 66 lines) already carries native audio, Gemini 3.8 Flash guiding-agent-in-loop, real-time steering — reference, not take.

Non-AI skips inside Import AI: DIA space-security report section (space-based directed energy, Cosmos 2542/2543) — geopolitical/military, out of scope despite being in a flagship AI newsletter. Always section-scope newsletter takes, don't take the issue as a unit.

## 3. Lenny's "How I AI" (pub 10845) — one post = TWO independent takes

The Nov 2 How I AI post bundled two segments (Claire Vo's 4-agent 9-task benchmark + Ezra Mechaber's Figma PM OS). The post page returned 28 substantive paragraphs covering BOTH segments with concrete data (Grok Bot 93% score, Claude Duet 4 approval prompts vs 1, Muse missing Slack/GitHub connectors; PM OS = AGENTS.md + 31 skills + hooks + version check for 60-70 PMs). This is the pure-podcast counter-nuance in action — do NOT auto-skip Lenny's-adjacent podcast posts.

Pattern: when one post page yields multiple distinct topics, emit one decision per topic with distinct `item_id` suffixes (`-2`, `-2b`) — the item_id-based dedup (not URL dedup!) keeps them separate, since both share the same post URL and same checkpoint item_id otherwise. URL-based dedup would have collapsed them.

Coverage-check specifics: `entities/figma.md` was a stale "Figma AI Challenge" page (sources empty, May update) — existence of the entity page said nothing about PM OS coverage. `concepts/duet-style-hierarchical-assistant.md` covers the authorization-hierarchy pattern only, not cross-agent benchmarks. Read the section, not the filename.

## 4. Irrational Analysis (pub 1509468) — financial-semiconductor skip rule

"Marvellous Value Destruction" had a fully fetchable 38-paragraph body (uVCSEL NPO/CPO, OCS link retraining, Lumentum Cloudlight spin-off, 300mW laser RIN specs) but is a semiconductor stock thesis — author's own disclosure "heavily invested... not financial advice". Skip category: **optical/semiconductor component supply-chain investment analysis** does not connect to LLMs/agents/dev-tooling/inference-infra, even when the topic is AI-adjacent hardware (optics for GPU clusters). Only take such sources when they make concrete claims about AI systems themselves (e.g., NVIDIA's inference architecture choices), not M&A motives.

## 5. Operational notes

- Builder script pattern worked: write_file → /tmp → `python3 -c "import ast; ast.parse(...)"` gate → run. One CJK typo ("CONTENTO") slipped through; grep the summary/reason strings in the verification pass.
- item_id collision between two takes from the same checkpoint link (Lenny Link 2) needed a `-2b` suffix — the item_id dedup silently dropped the second take on first run (12→11 decisions was the tell; verify takes count against intent, not just JSON validity).
- `git pull --rebase` failed (sibling unstaged changes) but plain `git push` succeeded — matches `pre-commit-new-page-tags-workflow.md` guidance; skip the rebase attempt when nothing local to rebase.
- archive_triage.py printed the `/opt/data/.hermes/home/ai-topics/...` nested path; `readlink -f` confirmed the canonical repo — symlink, do not move.
