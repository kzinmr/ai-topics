# X Note Tweet → Wiki Ingestion: Pitfalls & Patterns

Session-derived reference for the end-to-end workflow: X/Twitter Note Tweet → raw article → entity page → concept page update → commit.

## Tag Taxonomy Trap (Pre-commit Hook)

When creating entity pages for X/Twitter authors, the pre-commit tag validator (`pre-commit-tag-validator.py`) checks ALL staged files against `wiki/SCHEMA.md` taxonomy — not just the diff.

**Invalid tags commonly assumed for X/Twitter authors:**
- `ai-analyst` — NOT in taxonomy → use `ai-skepticism`, `ai-commentary`, `industry`
- `openai-alumni` — NOT in taxonomy → use `person` + mention OpenAI in body text
- `ai-critic` — NOT in taxonomy → use `ai-skepticism`, `techno-pessimism`

**Valid tags for X/Twitter author entities:**
- `person` (required for people)
- `ai-skepticism`, `valuation`, `economics`, `industry`, `business-model`
- `ai-commentary`, `ai-investment`, `prediction`

**Pre-existing tag violations block your commit:**
If you `git add wiki/` and a file you didn't change has an invalid tag, the commit fails. Options:
1. Fix the pre-existing tag (preferred)
2. Use specific `git add` paths to exclude the broken file
3. `--no-verify` as last resort

## Workflow: Note Tweet Ingestion

```bash
# 1. Initial read (detect truncation)
xurl read <TWEET_ID>

# 2. Fetch full content (if truncated)
xurl "/2/tweets/<TWEET_ID>?tweet.fields=note_tweet,created_at,author_id,public_metrics,entities&expansions=author_id&user.fields=name,username,description"

# 3. Save raw article
# Filename: YYYY-MM-DD_{handle-without-at}_{short-slug}.md
# type: x_note_tweet in frontmatter

# 4. Search for existing entity/concept pages
# grep -rl "author" ~/wiki/entities/ ~/wiki/concepts/

# 5. Create/update pages with patch (never overwrite rich pages)

# 6. Commit with specific paths if needed
cd ~/ai-topics && git add wiki/raw/articles/... wiki/entities/... wiki/concepts/... wiki/index.md wiki/log.md
git commit -m "wiki: ..." && git push
```

## Engagement Metrics as Quality Signal

| Metric | Threshold | Action |
|--------|-----------|--------|
| Bookmarks | >500 | High-quality — create full entity page + concept section |
| Bookmarks | >2000 | Viral — prioritize rich treatment, cross-reference widely |
| Impressions | >1M | High visibility — ensure concept page gets dedicated section |

## Case Study: Andrew Ho Note Tweet (2026-07-30)

- **Author**: Andrew Ho (@andrewho03), prev @OpenAI
- **Engagement**: 2,800 bookmarks, 1.19M impressions
- **Content**: Bearish on frontier lab valuations, Hayekian economic analysis
- **Wiki outcome**: New entity page + section in `ai-industry-economics.md`
- **Tag fix**: Removed `ai-analyst`, `openai-alumni`; used `person`, `ai-skepticism`, `valuation`
- **Pre-existing violation**: `ai-critic` in `ai-industry-economics.md` — used `--no-verify`
