# Fresh `updated:` date ≠ Full Same-Day Coverage (coverage-gap variant)

Validated 2026-08-05 in blog-wiki-ingest.

## The trap

A wiki page whose frontmatter `updated:` is TODAY's date can still have a genuine coverage gap for a **newer same-day development on the same topic**. Fast-moving stories (legal conflicts, release clusters, policy reversals) receive multiple same-day updates from different pipelines:

- Earlier pipeline run (e.g. raw-backlog-ingest 04:00, sitemap-monitor 06:00, newsletter-wiki-ingest 07:40) captures development #1
- The article under triage covers development #2 — same topic, same day, genuinely new content

Observed: `events/openai-apple-conflict-2026.md` had `updated: 2026-08-05` because an earlier run added the **Aug 3 OpenAI rebuttal**. The blog article under triage covered the **Aug 4-5 preliminary-injunction stage** (Apple's PI motion, OpenAI's unbylined rebuttal, Che Chang letter facts, 37-doc Box download allegation, Quinn Emanuel Exhibit F email, tone shift to "we do not have, nor want, any of their trade secrets"). The fresh date made the page look covered; it was a genuine gap. The PI stage required a new section + timeline rows + significance bullet.

## The test

Never trust the `updated:` date alone. When a page's `updated:` is today:

1. Read the page's **content sections** — what specific developments do they enumerate?
2. Read the **log.md entry** for the page's last update — which development did it actually cover?
3. If the article under triage covers a later same-day development than the page's content, it's a **genuine gap** → enrich (take), not skip.
4. Same-day dedup still works for the *same* development — the check is content-scope, not date.

## Related

- Semantic-article-grouping: "sources listed ≠ content captured" (frontmatter refs without body claims)
- "mentioned ≠ covered" (URL in References without substance)
- This variant: **date freshness ≠ content scope** — the page WAS recently updated, just not for THIS development.
