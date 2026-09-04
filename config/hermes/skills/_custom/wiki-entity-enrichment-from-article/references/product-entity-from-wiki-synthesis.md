# Product Entity Page from Multi-Source Wiki Synthesis

> **Note**: This reference is NOT linked from the main SKILL.md trigger because the
> SKILL.md is at the 100K character limit and the frontmatter is tightly constrained.
> If you are creating a product entity page and there is no raw article to anchor on,
> load this reference via `skill_view(name='wiki-entity-enrichment-from-article',
> file_path='references/product-entity-from-wiki-synthesis.md')`.

When a user asks about a product that has no dedicated wiki page but is mentioned
across multiple wiki pages, the workflow is different from article-driven
enrichment. There is no single raw article to anchor on — instead, you synthesize
from all existing wiki references.

## When This Applies

- User asks "tell me about X" where X is a product mentioned in 2+ wiki pages
- No raw article exists for X in `wiki/raw/articles/`
- Existing pages (company, sibling product, related concept) already have sections about X
- You need to create a dedicated entity page for X without a primary source

## Workflow

### 1. Comprehensively Scan the Wiki for All Mentions

Do NOT just check `index.md` or `entities/`. A product's information is scattered:

```bash
# 1a. Find all pages that mention the product name
cd ~/ai-topics/wiki
grep -ril "perplexity computer" entities/ concepts/ raw/ log.md index.md 2>/dev/null

# 1b. Check index.md for existing entries
grep "perplexity" index.md

# 1c. Check log.md for history of what was enriched when
grep -i "perplexity" log.md

# 1d. Check archived triage JSON (newsletter/blog triage may have skipped it with context)
grep -ril "perplexity computer" raw/archived/triage/ 2>/dev/null

# 1e. Check raw articles (even if not about the product directly)
ls raw/articles/ | grep -i "perplexity\|realtime"
```

**Key sources to read in full**:
- Company entity page (e.g., `entities/perplexity.md`) — has product sections
- Sibling product pages (e.g., `entities/perplexity-comet.md`) — has cross-references
- Related concept pages (e.g., `concepts/openai/realtime-api.md`) — has case study sections
- Raw articles that mention the product (even if the article is about something else)
- Archived triage JSON — may contain `reason_ja` explaining why the product was skipped before, with useful context

### 2. Attempt Primary Source Fetch (with Graceful Fallback)

Try to fetch the product's official site or documentation:

```bash
# Official product page
curl -sL --max-time 25 "https://r.jina.ai/https://www.productname.com" -H "Accept: text/markdown" | head -80

# Wikipedia (if it exists)
curl -sL --max-time 25 "https://r.jina.ai/https://en.wikipedia.org/wiki/Product_Name" -H "Accept: text/markdown" | grep -iE "key term" | head -20
```

**Common failures**:
- Vendor sites block anonymous Jina Reader access (DDoS protection) — note this and move on
- Wikipedia may not have the page yet (new products)
- If all primary sources fail, **do NOT block on this** — the wiki-internal synthesis is sufficient for a first page. Note in the page that primary source details (pricing, exact specs) are pending.

### 3. Verify All Outbound Wikilinks EXIST Before Writing

This is the #1 failure mode for new pages. Before writing the "Related Entities" section:

```bash
cd ~/ai-topics/wiki
for p in entities/perplexity entities/perplexity-comet concepts/openai/realtime-api concepts/ai-agent-memory concepts/self-evolving-agents; do
  [ -f "$p.md" ] && echo "OK  $p" || echo "MISS $p"
done
```

**Common broken link patterns**:
| Guessed (BROKEN) | Actual |
|---|---|
| `concepts/agent-memory` | `concepts/ai-agent-memory` |
| `concepts/vertical-agent` | (no standalone page — downgrade to plain text or link to company page) |
| `concepts/autonomous-agents` | (no standalone page — omit or link to concept MOC) |
| `concepts/browser-agent` | `concepts/browser-agent/death-of-browser` (subdirectory) |

**Fix pattern**: When a concept link is BROKEN, either:
1. Find the closest existing page and link to it
2. Downgrade to plain text (remove the `[[...]]`) if no suitable target exists
3. Link to the parent entity page instead (e.g., `[[entities/perplexity]]` instead of a non-existent concept)

### 4. Write the Page

Structure for a product entity page synthesized from multiple sources:

```markdown
---
title: Product Name
type: entity
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
- entity
- product
- <other-tags-from-SCHEMA>
aliases:
- product-name
sources:
- <raw article paths>
- <URLs>
- <sibling entity page paths>
---

# Product Name

<2-3 sentence overview: what it is, who makes it, positioning>

## Overview
| Field | Details |
|---|---|
| Developer | ... |
| Category | ... |
| ... | ... |

## Ecosystem Position
<ASCII diagram or explanation of where it sits in the company's product stack>

## <Major Feature/Area>
<Synthesized from 2+ wiki sources, each with inline source attribution>

## <Vertical/Variant>
<If the product has domain-specific variants>

## <Memory/Architecture/Other Distinguishing Feature>
<Technical details that differentiate from competitors>

## Related Entities
- [[entities/company]] — Parent company
- [[entities/sibling-product]] — The sibling product
- [[concepts/related-concept]] — Relevant concept
- [[entities/competitor]] — Competitor context

## Sources
- [Source 1 URL](url)
- [Source 2 URL](url)
- [[entities/company]] — <what it contributes>
```

**Tag validation**: Before writing, verify each tag exists in SCHEMA.md:
```bash
grep -qi "tag-name" ~/ai-topics/wiki/SCHEMA.md && echo OK || echo MISSING
```
Use plain keyword grep, NOT backtick-anchored grep (see pre-write-verification.md).

### 5. Add Back-Links from Sibling Pages

After creating the new page, add a wikilink to it from:
- The company entity page (in Related Concepts or Related Entities)
- The sibling product page (in Related Entities)
- Any concept page that had a case study section about the product

```bash
# Patch company page to add back-link
patch wiki/entities/company.md \
  "old: - [[entities/sibling]] — sibling description" \
  "new: - [[entities/sibling]] — sibling description\n- [[entities/new-product]] — new product description"

# Patch sibling page to add cross-link
patch wiki/entities/sibling.md \
  "old: - [[entities/last-related]]" \
  "new: - [[entities/last-related]]\n- [[entities/new-product]] — cross-reference"
```

### 6. Update index.md + log.md + Commit

```bash
# index.md: insert alphabetically in entities section
# log.md: append entry at top

cd ~/ai-topics
git add wiki/entities/new-product.md wiki/entities/company.md \
        wiki/entities/sibling.md wiki/index.md wiki/log.md
git commit -m "wiki: new entities/new-product page + cross-links"
git push
```

## Pitfalls

- **No primary source ≠ no page**: If the vendor blocks all scraping, synthesize from wiki-internal sources. Note in the page that primary source details are pending. Do NOT block the page creation on fetching the vendor site.
- **Wikilink verification is MANDATORY**: 3 out of 6 outbound links were broken in the Perplexity Computer session (concepts/agent-memory, concepts/vertical-agent, concepts/autonomous-agents all did not exist). Always run the `for p in ...; do [ -f ... ]; done` check BEFORE writing the Related Entities section.
- **Aliases in frontmatter**: Include the product name variations (e.g., `perplexity-computer`, `perplexity-digital-worker`) so future searches can find the page.
- **Source field in frontmatter**: List BOTH raw article paths AND URLs AND sibling entity pages. This makes the page's knowledge provenance traceable.
- **Do NOT duplicate content from sibling pages**: If `perplexity-comet.md` already has a detailed "Brain" section, the new `perplexity-computer.md` should have a concise Brain section with a wikilink back to Comet, not a full copy. Use "See [[entities/perplexity-comet]] for the full X section."
- **Pre-commit tag validation runs on ALL staged files**: If you're also touching sibling pages that have pre-existing tag violations, the commit will be blocked. Check sibling page tags before patching them (see pre-write-verification.md "Enriching a Page Validates Its PRE-EXISTING Tags Too").

## Session Example: Perplexity Computer (2026-08-26)

**Context**: User asked "perplexity computerについて詳しく教えて" — no dedicated page existed.

**Sources synthesized from**:
- `entities/perplexity-comet.md` (115 lines) — ecosystem diagram, Brain section, security
- `entities/perplexity.md` (102 lines) — Professional Finance vertical, Bumblebee
- `concepts/openai/realtime-api.md` — Perplexity case study section
- `raw/articles/2026-03-25_openai-developers-blog_realtime-perplexity-computer.md` — full voice engineering details
- `raw/archived/triage/newsletter/2026-06-13_*.json` — triage context for why Computer was skipped before
- Jina Reader on `comet.perplexity.ai/` — basic product description
- Jina Reader on `perplexity.ai/hub/blog/perplexity-computer` — BLOCKED (DDoS)

**Page created**: `entities/perplexity-computer.md` (~130 lines)
- 5 valid outbound wikilinks (perplexity, perplexity-comet, openai/realtime-api, ai-agent-memory, self-evolving-agents)
- 3 back-links added to perplexity.md and perplexity-comet.md
- index.md entry inserted after perplexity-comet
- log.md entry appended at top
- Committed as `312e8ffe`, pushed to main

**Broken links caught and fixed before commit**:
- `concepts/agent-memory` → `concepts/ai-agent-memory`
- `concepts/vertical-agent` → removed (no suitable target, downgraded to plain text)
- `concepts/autonomous-agents` → removed (no suitable target, downgraded to plain text)
- Added `concepts/self-evolving-agents` as replacement (exists, relevant)
