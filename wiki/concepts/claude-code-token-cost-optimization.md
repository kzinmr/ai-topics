---
title: "Claude Code Token Cost Optimization"
created: 2026-11-10
updated: 2026-11-10
type: concept
tags:
  - concept
  - claude-code
  - coding-agents
  - cost-optimization
  - token-economics
  - inference-cost-controls
  - developer-tooling
  - case-study
sources:
  - raw/newsletters/2026-11-10-spotify-s-claude-code-token-trick-tested-the-real-savings.md
  - https://www.aibyaakash.com/p/spotifys-90-trick
---

# Claude Code Token Cost Optimization

How organizations cut Claude Code token spend without degrading output quality. The canonical first-party case is **Spotify** (engineering.atspotify.com, Sept 2026, "Portal by Spotify: cut my Claude Code token usage by 90%"), independently re-tested by Aakash Gupta (*AI by Aakash*, Nov 2026) on two real codebases. The core finding is conditional: the savings are large for **read-heavy** workloads and negative for search-and-edit workloads that the Claude Code harness already optimizes.

## The Spotify case

- **Honk** — Spotify's internal coding agent. Engineers tag `Honk` in Slack; Honk reads the codebase, writes the change, and opens the PR. Honk now merges **~1,000 code changes every 10 days**, a pace that previously took ~3 months at Spotify (7,300 employees). All that reading produced a very large Claude bill.
- **Shunt** — a plugin built by a Spotify PM that **blocks Claude from reading any file over 350 lines in full**; instead a cheaper model (they use Gemini Flash) reads the file and returns a distilled answer. Reported **82–94% token reduction on big files**; **~90% average across a 162K-line Java monorepo**.
- **Open source**: Spotify released the plugin on GitHub (~3,186 stars at time of writing).
- **Organizational context**: Spotify's co-CEO said on an earnings call that most senior engineers "haven't written a single line of code since December" — the usage profile (agents reading whole monorepos on demand) is exactly the read-heavy case the plugin targets. See [[concepts/enterprise-ai-cost-management]] for the contrasting top-down approach (Uber's per-tool caps, Devin's efficiency-graded allocation).

## Where the bill actually goes (Aakash's breakdown)

A Claude Code bill decomposes into four priced elements: **input, cache write, cache read, output**. On Opus 5.5, answering four questions over a large open-source Java codebase:

| Component | Share of bill |
|-----------|---------------|
| Cache write | **85%** |
| Cache read | 9% |
| Output | 6% |
| Input | ~rest |

The first read of every big file is a cache write — exactly the cost Shunt hands to a cheaper model. Output, despite its high unit price, is a rounding error. This inverts the intuition that long model answers drive the bill.

## Independent replication results

Aakash re-tested the trick (simple "use a cheaper model for big files" sentence vs. Spotify's hook ported to Claude Code; search on vs. off) on two codebases:

| Codebase | Search on (Claude Code harness) | Search off (forced whole-file reads) |
|----------|-------------------------------|--------------------------------------|
| **Apache Commons Lang** (max file 9,800 lines) | cost −76% (sentence) / **−87% (Spotify hook)** | largest wins |
| **Personal repo** (78K lines) | hook **backfired** (+cost); sentence −53% | sentence still saved |
| **Pure search-and-edit runs** | sentence **added** 19–36% cost | n/a |

All model answers passed quality review in the runs, i.e. the savings came with no measurable quality drop.

## Decision rule

1. **Mostly search-and-edit?** Claude Code already fetches only the lines it needs — skip the trick; it added cost in every such run.
2. **Claude reads whole files** (agents built on the API without a search tool; code reviews; migrations; anything forced to read end-to-end)? Start with the sentence (it saved money on both codebases), then A/B the hook for a week — it won big on Commons Lang but backfired on the personal repo.
3. **Rollout**: commit the sentence to `CLAUDE.md` and the hook to `.claude/settings.json` so the whole team inherits it. See [[concepts/claude-md-rules]].
4. **Audit cheap answers**: one early run's "91% saving" was the model refusing to do the job. Open every cheap answer before trusting the number.
5. **Sizing**: per-run saving × monthly read-heavy run count. Example given: $0.72 × 3 runs/day × 20 engineers × 21 workdays ≈ **$900/month** — measure a week before and after.

## Related

- [[entities/claude-code]] — the harness whose internal search already performs the "cheap thing" for search-driven usage
- [[concepts/enterprise-ai-cost-management]] — org-level cost controls (caps, gateways, efficiency grading); Shunt/Honk is the engineering-level counterpart
- [[concepts/token-economics]] — pricing structure across input/cache/output
- [[entities/aakash-gupta]] — author of the independent replication
- [[concepts/caching-performance-cost-optimization]] — prompt caching mechanics behind the 85% cache-write share

## Sources

- Aakash Gupta, ["Spotify's Claude Code Token Trick, Tested: The Real Savings"](https://www.aibyaakash.com/p/spotifys-90-trick), *AI by Aakash*, Nov 9, 2026. Raw: `raw/newsletters/2026-11-10-spotify-s-claude-code-token-trick-tested-the-real-savings.md`
- Spotify Engineering, "Portal by Spotify: cut my Claude Code token usage by 90%" (Sept 2026) — primary source cited by the above.
- Shunt plugin on GitHub (~3.2K stars) — linked from the newsletter article.
