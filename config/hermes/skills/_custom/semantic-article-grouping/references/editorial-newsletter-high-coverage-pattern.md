# Editorial Newsletter with High Coverage Rate

Some newsletters (e.g., The Signal, Superintel) act as **curators of original source announcements** rather than original research publishers. Their primary value is editorial synthesis — selecting, summarizing, and commenting on the week's major AI stories. The actual article links they provide point to company blogs (Microsoft, NVIDIA, OpenAI, Anthropic) that are already captured by sitemap-monitor (06:00 UTC) and blog-ingest pipelines before newsletter-triage runs (07:20 UTC).

## Identifying the Pattern

A newsletter fits this pattern when:

1. **All external links point to official company/blog announcements**, not to original analysis or research papers
2. **The newsletter's editorial content is opinion/commentary** on already-public news, not exposing new information
3. **The newsletter is published weekly** (not daily), with a roundup format
4. **The author identifies their role as "curator" or "analyst"** rather than "reporter" or "researcher"
5. **The newsletter's value proposition is "saving you time"** — reading the news so you don't have to

## Known High-Coverage-Rate Publications

### The Signal (Alex Banks, `publication_id=293154`)
- **Format**: Weekly Sunday newsletter. Two variants:
  - **Roundup weeks**: ~47 paragraphs, "top 3 picks" format, ~14 external links (most weeks)
  - **Essay weeks**: 30-50 paragraph standalone argument with 2-10 supporting citations (e.g., "The good, the bad and the ugly of AI writing")
- **Distinction by subject**: Thesis/value-judgment language → essay. Topic-list language → roundup
- **Links**: 14 external links → all company/blog announcements (roundup weeks)
- **Coverage rate**: 12/14 links already captured by sitemap-monitor/blog-ingest pipelines
- **Remaining value**: 1 genuinely new topic (e.g., Project Solara) + 1 supplementary reference (e.g., AI bioweapon letter)
- **isAccessibleForFree**: `true` (full body accessible)
- **Expected yield**: ~1 take + ~1 reference per issue, rest skip

## Triage Strategy for High-Coverage-Rate Newsletters

When you've identified this pattern:

1. **Expect ~85-90% skip rate** — most topics will already be covered by other pipelines
2. **Focus triage effort on the ~10-15% of content that might be genuinely new**:
   - Niche product announcements not covered by sitemap-monitor (e.g., Project Solara)
   - Industry open letters / policy developments not yet in wiki (e.g., bioweapon DNA screening)
   - Emerging trends the author identifies that span multiple stories
3. **Do NOT treat editorial commentary as new wiki content**:
   - Alex Banks's take ("I was in SF for Microsoft Build…") = opinion, not data
   - "This is a smart play" / "This was a big shift" = editorial framing
   - Only capture verifiable new facts (model names, specs, product features, policy details)
4. **Cross-reference aggressively**: For each link the newsletter mentions, check:
   - Is the original source in `~/wiki/raw/articles/` (sitemap-monitor)?
   - Is the topic in wiki log.md (blog-ingest or earlier newsletter runs)?
   - Does a concept or entity page already cover the specific facts?
5. **The newsletter's unique value is the editorial gap analysis** — identifying which topics the wiki already covers and which it doesn't. Even if most items are skip, the single uncovered topic justifies the triage investment.

## Contrast with Low-Coverage-Rate Newsletters

| Dimension | High-Coverage (The Signal) | Low-Coverage (Superintel, AINews) |
|-----------|---------------------------|-----------------------------------|
| Link sources | Company blogs, major announcements | Niche startups, new papers, X posts |
| Coverage rate | ~85-90% already captured | ~30-50% already captured |
| New content yield | 1-2 takes per issue | 3-8 takes per issue |
| Editorial value | Commentary on known news | Discovery of unknown news |
| Triage approach | Rapid skip + deep dive on survivors | Full analysis of each link |
