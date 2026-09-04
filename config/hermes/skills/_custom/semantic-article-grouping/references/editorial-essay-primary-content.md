# Editorial Essay Variant — Newsletter Post Body as Primary Content

Not all newsletters with links are link roundups. When a newsletter post is a **standalone editorial essay**, the post body itself IS the primary content. External links serve as supporting citations, not as the main event to triage.

## Detection

| Signal | Essay | Roundup |
|--------|-------|---------|
| Subject line | Thesis language ("The good, the bad and the ugly of X", "Why X matters", "What we get wrong about X") | List language ("This week in X", "X things to know", "Top stories", numbered list) |
| Paragraphs | 30-50+ cohesive argument paragraphs | 5-15 per-section summaries (bullet-like structure) |
| Argument structure | Thesis → development → conclusion | Section headings → 1-2 sentence summary → link |
| External links | 2-10, serving as citations | 10-20+, each link is a distinct "article" to triage |
| Author voice | First-person editorial throughout | Neutral curation ("here's what happened this week") |
| Decision pattern | **1 decision** for the newsletter post itself | **N decisions** (one per unique external topic) |

## Known Publications That Sometimes Send Essays

### The Signal (Alex Banks, publication_id=293154)
- **Most weeks**: Editorial roundup (~14 external links, ~47 paragraphs, "top 3 picks" format, ~85-90% already in sitemap-monitor)
- **Some weeks**: Editorial essay (e.g., "The good, the bad and the ugly of AI writing" — 40 paragraphs, 7 citations, standalone argument about Substack's new AI text detection)
- **Tel**: Subject line containing explicit thesis or value-judgment language ("good/bad/ugly") → essay. Topic-list subject line → roundup.

## Triage Strategy

1. **Read the full post body** — this IS the content to assess, not a table of contents to external links
2. **Evaluate the essay's wiki value** on its own merits:
   - Platform-policy documentation (Substack's new "Scan for AI text" + Pangram partnership)
   - New concept introduction ("Claudefishing" as a named phenomenon)
   - Social-impact analysis (false positives, cheating accusations, the detection paradox)
   - Critique/debate framing that adds context missing from technical wiki pages
3. **External links are supporting evidence** — do NOT create separate triage decisions for each citation. The essay is the unit of assessment.
4. **Typical rating**: ★★★☆☆ / `reference` — essays contribute analysis and context, not new factual discoveries. They enrich existing concept pages (e.g., adding Substack to `concepts/ai-content-transparency.md` alongside YouTube/Meta/TikTok/X).
5. **Create exactly ONE decision** for the newsletter post URL with `body_excerpt` drawn from the essay body.

## Contrast with Editorial Roundup

| Dimension | Editorial Essay | Editorial Roundup |
|-----------|----------------|-------------------|
| Primary content | The essay itself | The curated external links |
| External links | Supporting citations (2-10) | Main event (10-20+) |
| Decision count per newsletter | 1 (the essay) | N (one per unique topic) |
| Body extraction | Read and assess the full essay | Extract section headings + link titles |
| Star rating ceiling | ★★★☆☆ (reference / enrichment) | ★★★★★ (new page if link is genuinely novel) |
| Existing page match | Check concept pages for platform/policy coverage | Check entity pages for author/organization coverage |

## Concrete Example (July 2026)

**Newsletter**: The Signal — "The good, the bad and the ugly of AI writing"
- 40 paragraphs, 7 external citations
- Topic: Substack's "Scan for AI text" button (Pangram partnership), Claudefishing concept
- Wiki gap: `concepts/ai-content-transparency.md` covers YouTube/Meta/TikTok/X but not Substack
- **Decision**: 1 reference item for `concepts/ai-content-transparency.md` enrichment
- **What was NOT done**: Creating 7 separate decisions for each external citation (OpenAI classifier, Bloomberg on false accusations, Atlantic Pangram article, NYT quiz, etc.)

## Pitfall: Mixed-format Newsletters

Some publications (Latent Space, AINews) mix essay sections with link roundup sections in the same post. When you find both patterns in one newsletter:
- Essay sections: assess as per this reference
- Roundup sections: assess as per `references/editorial-roundup-per-article-triage.md`
- Create separate decisions: 1 for the essay (reference), N for the roundup articles (per-article triage)
- The two assessment types coexist in the same decisions array
