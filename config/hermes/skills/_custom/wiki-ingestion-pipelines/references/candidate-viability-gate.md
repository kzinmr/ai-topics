# Candidate Viability Gate — rejecting fabricated trending topics (active-crawl pass -1)

**Problem:** the trending-topic candidate list handed to the active-crawl job is
frequently **partly or wholly fabricated** — plausible titles attributed to real
authors/orgs that exist nowhere. In one audited run, 4 of 7 candidates were
nonexistent:

| Claimed candidate | Verdict |
|---|---|
| Cohere "megakernels" | No such post |
| Dwarkesh "Pretraining progress is mostly data" | No such post (two slug variants, both 404) |
| Anthropic "Scaling the SWE-Lancer benchmark" / "SWE-Lancer Diamond" | 404; that week's real post covered multi-model **coding** eval, not SWE-Lancer |
| Ed Zitron "AI Is Not a Product" | No such post |

Deriving URL slugs from a title and chasing 404s is the single biggest budget sink in
this job. Gate candidates before spending scraper calls or authoring pages.

## Rules

1. **No URL, no work.** A candidate earns effort only once it resolves to a real
   document. Never author a wiki page from title + author alone.
2. **Prove existence via the source's own index, not guessed slugs.** Cheapest first:
   - the site's RSS/atom feed (`/feed`, `/rss.xml`, `/index.xml`, `/atom.xml`)
   - its `/blog` / `/posts` / `/research` listing page
   - a local mirror: `git log --all --oneline -- '*<keyword>*'` in `~/ai-topics`, plus
     `search_files` over `wiki/raw/articles/` (many candidates are already ingested)

   Grep the listing for a distinctive substring of the title — one call proves
   existence *and* yields the canonical URL.
3. **Two dead URLs from one source ⇒ dead.** Stop inventing slug variants. Record the
   candidate as rejected with the exact URLs tried.
4. **A near-miss is not a hit.** If the publisher has a *different* overlapping post,
   do not substitute it for the claimed one. Say plainly: "the claimed post does not
   exist; the real <date> post is about X." Silent substitution is the failure mode that
   makes a whole report untrustworthy.
5. **Rejected candidates are a deliverable, not noise.** List each with URLs checked and
   verdict, and name the upstream defect (candidate generation should emit a resolvable
   URL, not a bare title) so the producing stage gets fixed instead of this job absorbing
   the cost indefinitely.
6. **Real-but-thin ⇒ raw only, no page.** If the post exists but adds no claims beyond
   what an existing page already carries: save the raw with a `note:` field in its
   frontmatter explaining why it wasn't promoted, touch only the relevant entity page's
   `sources:` / `updated:`, and say so in the report. (Example: Terence Tao's "AI,
   Mathematics, and the Honest Midterm" — a re-delivery of an earlier survey talk plus one
   already-recorded SWE-Lancer anecdote.)
7. **Already-ingested ⇒ sha256 only.** Keep/refresh the raw for source-drift tracking,
   create no page, and report "already fully ingested" rather than redoing the work.

## Three-pass budget shape

- **Pass 1 — resolve only:** every candidate → real URL or dead verdict. No writes.
- **Pass 2 — triage survivors:** fetch, then check `index.md` / `search_files` to decide
  new page vs. update vs. no-op.
- **Pass 3 — writes:** pages, `index.md`, `log.md`, `config/hot-topics.yaml`.
- **Reserve ≥15% of iterations for commit/push.** Hitting the iteration cap with
  uncommitted wiki edits is this job's most common near-miss; the commit is part of the
  deliverable, not an afterthought.
