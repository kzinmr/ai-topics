# X Article + Companion Note Tweet Combo Ingestion

Pattern: viral X content where a **Note Tweet** serves as a concise summary/checklist and an **X Article** (linked via quote tweet) contains the full detailed guide. Both are from the same author and published simultaneously. The Note Tweet often goes more viral (higher bookmarks/impressions) than the Article itself.

## Recognition Signals

- Note Tweet opens with attribution quote ("Andrej Karpathy: ...") followed by a numbered list
- Note Tweet ends with "what actually compounds instead:" followed by principles
- Note Tweet has `referenced_tweets[type: "quoted"]` pointing to an X Article
- X Article contains `article.title` and `article.plain_text` with full content
- Engagement ratio: Note Tweet bookmarks > Article bookmarks (summary is more shareable)
- Author is known for long-form educational content on X

## Workflow

1. **Fetch both** via xurl v2 API:
   - Note Tweet: `xurl "/2/tweets/{ID}?tweet.fields=note_tweet,public_metrics,created_at,entities&expansions=author_id,referenced_tweets.id"`
   - X Article: `xurl "/2/tweets/{QUOTED_ID}?tweet.fields=article,public_metrics,created_at,entities&expansions=author_id"`

2. **Save BOTH as raw articles** (different filenames, same date):
   - Note Tweet: `{date}_{handle}_{short-slug}.md` with `type: x_note_tweet`
   - X Article: `{date}_{handle}_{short-slug}.md` with `type: x_article`
   - Both share the same `author` and `author_id`

3. **Synthesize concept page from X Article** (full content is in the Article, not the Note Tweet):
   - Note Tweet provides structure/checklist for the concept page outline
   - X Article provides detailed techniques, benchmarks, configs, and rollout plan
   - Cross-reference both raw articles in concept page `sources`

4. **Enrich entity page**: Add both articles to Notable Works table. The Note Tweet's bookmark count is often the more impressive metric.

5. **Cross-enrich related concept pages**: Add a section comparing/contrasting the new material with existing concepts (e.g., Ronin's manual router vs Augment Prism in `model-routing.md`).

## Example (this session)

- Note Tweet: `2026-05-12_deronin_10-things-senior-ai-engineers-stopped-wasting-tokens.md` (1,012 bookmarks)
- X Article: `2026-05-12_deronin_how-to-cut-ai-coding-bill-80-percent.md` (264 bookmarks, but full system)
- Concept: `concepts/ai-coding-cost-optimization.md`
- Cross-enriched: `concepts/model-routing.md` (added Manual Router Architecture section)

## Pitfalls

- **Don't synthesize from the Note Tweet alone** — it's the teaser, not the full content. The X Article has the router config, benchmarks, techniques, and rollout plan.
- **Don't skip saving the Note Tweet** just because it's "just a summary" — it may have 4x more bookmarks and is the user-facing viral content.
- **Check if the X Article is quoted vs replied** — quoted tweets are intentional pairings; replies may be follow-ups published later.
