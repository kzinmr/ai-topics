---
name: grokipedia-entity-enrichment
description: Enrich wiki entity pages using Grokipedia as a source. Grokipedia provides structured biographical data (education, career timeline, quotes, interviews, metrics) that complements X/blog sources.
category: wiki
---

# Grokipedia Entity Enrichment

Use Grokipedia (grokipedia.com) to enrich wiki entity pages with biographical data, career timelines, interview quotes, and quantitative metrics.

## When to Use

- **Person entity pages** need biographical depth (education, early career, timeline)
- **Missing structured data** like dates, company transitions, specific metrics
- **Cross-referencing** quotes from podcasts, interviews, webinars
- **Initial page creation** when you have a name but limited other sources

## How to Extract Content

Grokipedia is a JS-heavy site. Use Jina Reader API for clean text extraction:

```bash
curl -s -L --max-time 30 "https://r.jina.ai/http://grokipedia.com/page/{Person_Name}"
```

Replace spaces with underscores in the URL (e.g., `Boris_Cherny`, `Andrej_Karpathy`).

The Jina Reader strips JS/CSS and returns clean markdown-like text with citations.

## What to Extract

1. **Early Life & Education** — schools, degrees, dropout stories, self-taught paths
2. **Career Timeline** — company transitions with dates, role evolution
3. **Key Projects** — specific products, features, innovations with dates
4. **Quantitative Metrics** — adoption numbers, benchmarks, performance stats
5. **Interview Quotes** — podcast appearances, webinar statements, media quotes
6. **Industry Impact** — competitor responses, market influence, paradigm shifts
7. **Philosophy/Worldview** — hiring philosophy, safety views, public statements
8. **References** — numbered citations that link to primary sources

## Enrichment Process

1. Extract content via Jina Reader
2. Cross-reference with existing entity page
3. Add **new sections** for missing biographical/career data
4. Add **specific quotes** with source attribution
5. Add **metrics and numbers** (adoption rates, benchmarks, growth)
6. Update **Sources** section with Grokipedia URL + specific interview links
7. Update `wiki/index.md` and `wiki/log.md`
8. Commit and push

## Quality Checks

- All quotes must have source attribution (podcast name, date, publication)
- Metrics must have citation numbers matching Grokipedia's references
- Career dates must be specific (month + year when available)
- Cross-link to other wiki entities where relevant
- Maintain existing page structure — add new sections, don't replace

## Known Grokipedia Strengths

- **Citation-numbered references** — each claim has a [[N]] marker
- **Interview summaries** — podcasts, webinars, media appearances with dates
- **Competitive context** — how the person's work compares to rivals
- **Quantitative data** — specific numbers (growth %, benchmark scores, revenue)
- **Timeline precision** — month-level granularity for career moves

## Known Grokipedia Weaknesses

- **AI-generated content** — "Fact-checked by Grok" — verify critical claims
- **May lag behind** — not real-time; recent events may be missing
- **Citation links** — numbered references [[N]] may not always resolve
- **JS rendering** — direct curl returns empty; MUST use Jina Reader API

## Example Usage

```bash
# Extract Boris Cherny's full Grokipedia page
curl -s -L --max-time 30 "https://r.jina.ai/http://grokipedia.com/page/Boris_Cherny"

# Extract Andrej Karpathy's page
curl -s -L --max-time 30 "https://r.jina.ai/http://grokipedia.com/page/Andrej_Karpathy"
```

## Post-Enrichment Steps

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: enrich {name} from Grokipedia" && git push
```
