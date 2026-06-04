# Grokipedia Entity Enrichment — Full Reference

Use Grokipedia (grokipedia.com) to enrich wiki entity pages.

## How to Extract Content
Grokipedia is JS-heavy. Use Jina Reader API:
```bash
curl -s -L --max-time 30 "https://r.jina.ai/http://grokipedia.com/page/{Person_Name}"
```
Replace spaces with underscores.

## What to Extract
1. Early Life & Education
2. Career Timeline with dates
3. Key Projects with dates
4. Quantitative Metrics
5. Interview Quotes with attribution
6. Industry Impact
7. Philosophy/Worldview
8. References with numbered citations

## Enrichment Process
1. Extract via Jina Reader
2. Cross-reference with existing entity page
3. Add new sections for missing data
4. Add specific quotes with source
5. Add metrics and numbers
6. Update Sources section with Grokipedia URL
7. Update index.md and log.md

## Quality Checks
- Quotes must have source attribution (podcast name, date)
- Metrics must have citation numbers
- Career dates specific (month + year)
- Cross-link to other wiki entities
- Maintain existing page structure (add sections, don't replace)

## Known Strengths
Citation-numbered references, interview summaries, competitive context, quantitative data, timeline precision

## Known Weaknesses
AI-generated content (verify claims), may lag behind, JS-heavy (MUST use Jina Reader API)
