# Reference-List-Only Entity Pages (2026-07-18 Validation)

## Pattern

An entity page may list many source filenames in its frontmatter `sources` or body `References` section but contain **zero content sections**. These are **reference-collection skeletons** — distinct from stubs:

| Property | Stub | Reference-collection skeleton | Comprehensive |
|----------|------|------------------------------|--------------|
| Lines | <30 | 40-60+ | 100+ |
| Has content sections? | No | No | Yes |
| Has references? | Minimal | Many | Many |
| Signal | Take | Take | Depends |

## Detection

The test: does the page have any `## Section Title` headings beyond the frontmatter and a bare `## References` list? If every heading is a source/URL entry with no analytical text below it, the page is effectively absent for triage purposes.

## Validation (July 2026)

`entities/hyperbo.md` was 52 lines with 25 reference entries but zero content sections and `tags: []`. Both new articles (Code Reds Need Maintenance Loops → take, Please Go Brr on Token Mandates → reference) were correctly scored despite the page existing and being non-trivial in size. Confirms that page length alone is insufficient — content section presence is the deciding factor.

## Implementation Note

Treat these pages as genuine takes (★★★★☆) even when the page is 50+ lines. The presence of accumulated references without synthesis means the entity is known to the wiki but not yet documented. This is a stronger enrichment signal than a pure stub because the person/company has been repeatedly captured as a source — the raw material for enrichment exists.
