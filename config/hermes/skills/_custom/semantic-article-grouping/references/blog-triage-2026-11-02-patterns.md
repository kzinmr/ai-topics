# Coverage-Gap Take Patterns Beyond Fresh Concept Pages

Validated 2026-11-02 blog-triage run (`20261102T101809Z`, 10 candidates + 10 unsaved
→ 3 takes / 4 refs / 6 skips). All three patterns below produced a `take` that a
naive keyword-existence dedup check would have skipped.

## 1. Yesterday's NEW concept page ≠ the underlying EVENT's page

**Symptom of a false skip**: a prior run (dreaming / active-crawl / sibling triage)
created a brand-new concept page about event E *yesterday*, and a blog post published
today by the event's primary commentator hits the same topic keyword in `concepts/`.
Grepping the keyword returns a hit → the instinct is "already captured, skip."

**Why that's wrong**: the prior page was built from a *different* primary source
(often a vendor/analyst report), and the commentator's post adds a distinct
**policy/causation layer** plus concrete facts the report never contained.

**Test — per claim, not per topic**: enumerate 3-5 specific claims the article makes
(numbers, named targets, named victims, the causal thesis) and grep each in the
existing page. If ≥2 are absent, it's a ★★★★☆ take-as-existing-page-update, not a skip.

**Concrete case (Nov 2 2026)**:
- Existing: `concepts/volta-infostealer-llm-victim-appraisal.md`, created **2026-11-01**
  from the Cisco Talos report ("Appraisal by AI: Model-driven victim prioritization in
  the VOLTA infostealer").
- New article: Pluralistic "Autodoxing" (Cory Doctorow, Nov 2) — the commentator's
  lead essay on the same malware.
- Facts absent from the Talos-sourced page: explicit targeting of
  **Discord/Telegram/Steam/Roblox sessions** (youth focus); merge with **Ticketmaster /
  Disney / AT&T** breach data; "**Black October → Black November**" catastrophe-framing;
  the core thesis *"AI capabilities have made infostealers much worse, but the reason for
  that new potency lies in how AI capabilities are supercharged by breach data"* (root
  cause = generations of anti-privacy policy, AI is the accelerant); total rejection of
  "age verification"; Canada Bill C-22 / UK / EU encryption bans as *current* policy;
  UK Labour discarding the Goldacre Report and handing NHS data to Palantir.
- Decision: `take`, `candidate_wiki_path = concepts/volta-infostealer-llm-victim-appraisal.md`
  (add a policy section) **+** `entities/cory-doctorow.md` (last updated Oct 19 — the
  essay was absent from the author entity too).

**Corollary**: always check the *author entity's* last-updated date and section headings
separately from the concept page. A fresh concept page and a stale author entity routinely
coexist — both may need the same article.

## 2. Quote-post by a curator quoting an author with NO entity page

The standard author-quote dedup check says: "if a curator (Simon Willison, Daring
Fireball) quote-posts another author's work, check the original author's entity page —
it may already carry the content."

**The uncovered branch**: what if the original author has **no entity page at all**?

Detection:
```bash
# wiki-wide, excluding raw/articles/
grep -rin "kingsbury\|jepsen\|particledb" --include=*.md wiki/ | grep -v "raw/articles"
ls wiki/entities/ | grep -i "kingsbury\|aphyr"
```
If the result is ≤1 *incidental* mention (the name appears inside someone else's page
as a case study) and no author entity exists, the quote-post is a legitimate **take**
whose `candidate_wiki_path` is a **new author entity page**.

Concrete case: `simonwillison.net--2026-nov-1-kyle-kingsbury--e4fc43e0.md` (831 bytes)
quoting Kyle Kingsbury's *Jepsen results for ParticleDB 1.1.4*:

> "the use of LLMs erodes trust in documentation, in software, and in the organizations
> which produce them … the signals we used to rely on as markers of a mature system are
> now easier to counterfeit. … In the age of LLMs, what can maintainers do to ensure
> correct software and accurate documentation?"

Wiki-wide grep found `kingsbury`/`jepsen` **only** inside `entities/dan-luu.md` (as a
case study in Luu's measurement essay). No Kingsbury entity, no Jepsen page, no page
carrying the quote → rated ★★★★☆ take → `entities/kyle-kingsbury.md`.

**Do not let the ~500B soft size guideline veto this.** The guideline is a heuristic for
"does this file have a body worth reading", not a coverage threshold. A sub-1KB quote-post
with zero wiki coverage outranks a 20KB page that's already captured. This is the second
named exception to the size filter (the first: Simon Willison quote-posts carrying
original data, e.g. the 931B Anthropic sycophancy quote).

## 3. Non-AI-looking posts that carry a load-bearing AI/agent fact — read before skipping

Three of this run's four `reference` calls were only reachable by reading bodies that
*looked* non-AI by title:

| Title (looks non-AI) | The AI/agent fact buried in the body |
|---|---|
| "Kernel prepatch 7.4-rc1" (LWN) | Greg Kroah-Hartman on AI-generated code: **"I'm *much* happier with the flood of AI triggered work going into the merge window than it showing up mainly as extra fixes during the -rc period"** + 18,591 non-merge changesets (record, ≈ the entire 7.3 cycle), 2,678 devs, 625 first-timers. Rare first-party observation of AI code flowing into *normal* OSS development rather than the stabilization tail. |
| "A Mastodon bot powered by iOS Shortcuts" (evanhahn.com) | "This used to be a short, hand-written Bash script. I used the **new AI-powered Shortcut creator** and prompted this into existence … Like a lot of LLM output, it wasn't quite right, but it was useful for getting started." Plus the platform-constraint workaround (no "run every 6h" primitive → four scheduler shortcuts calling one main shortcut). Small pragmatic-LLM case study. |
| "10 Years on Mastodon" (shkspr.mobi) | "**I'm even getting paid to develop ActivityBot!**" — the single-PHP-file ActivityPub server commercialized. Also "Mastodon's API is mostly a delight to use. There aren't weird and arbitrary restrictions," which is a useful **counter-example to Eden's own Jan-2026 "Are there any open APIs left?"** API-collapse thesis. |

Lesson: the filter is *title-suspicion*, never *title-verdict*. Titles that read as
kernel releases, retro hardware, or personal retros still get a body read; the AI angle is
frequently one paragraph deep and is exactly what an entity page needs.

Conversely, the same read confirms skips cheaply — johndcook's projective-geometry post,
the 7.2.15 EOL notice, and the IBM PC/XT drive-bay screws post each took one read to
dispose of.

## 4. unsaved_articles: skip is right, but record the future-transcript shortlist

`unsaved_articles` (YouTube talks, paywalled links) cannot generate a `take` — no body,
no BODY-READING MANDATE compliance. But **don't discard the titles**: 4 of 8 AI Engineer
talks this run were directly agent-ops relevant and should resurface when transcripts are
fetched (dreaming / active-crawl side):

- Sagar Batchu (Speakeasy) — "A Valid Key Let an AI Agent Delete Production" (agent
  permission boundaries, prod-deletion incident)
- Yijia Liang (Compound AI) — "Why We Rebuilt Microsoft Office From Scratch for AI Agents"
- Hahnbee Lee (Mintlify) + Lincoln Murr (Coinbase) — "Most of Your Docs Readers Are Now AI Agents"
- Ramakrishnan Lokanathan — "If Your AI Scores 100%, Your Eval Is Wrong" (eval design)

Encode them as a **single batched skip decision** with `body_excerpt:
"（unsaved_articles — 抽出不可）"` and list the titles inside `reason_ja`, so the
archive file preserves the lead without 8 separate rows. One row for the 8 talks, one for
the LWN security-updates link, one for the non-AI personal-website list → 3 decisions for
10 unsaved items.

## Run-local facts (for archive cross-reference)

- triage checkpoint: `/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json`,
  `checkpoint_run_id = 20261102T101809Z`, 13 decisions.
- archive: `wiki/raw/archived/triage/blog/2026-11-02_20261102T101809Z.json`
  (`archive_triage.py blog --keep-reference`, 10 items, running total 2,996 URLs).
- commit `9385f53d` "wiki: blog triage report 20261102T101809Z" — pushed, clean.
- The prior day's `triage_latest.json` (20261101T100049Z) was present and correctly
  treated as stale; the same-day `latest.json` `checkpoint_run_id` matched the injected
  batch, confirming freshness (priority-order step 0 in the SKILL.md worked as written).
