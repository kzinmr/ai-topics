# Batch Skip Grouping in Triage JSON Output

## Problem

When triaging large article backlogs (200+ articles, common in dreaming-group runs), creating individual skip decisions for each article produces an unwieldy JSON file. 200 individual decisions = ~200KB of mostly repetitive skip entries where the `body_excerpt` and `reason_ja` are nearly identical within a source group.

## Pattern

Instead of individual skip decisions per article, group skip items by source or topic into **batch skip entries** in the triage JSON output. Each batch entry represents N articles that share the same skip reason.

### Example (June 2026 dreaming run — 233 articles)

**Without grouping**: 233 individual decisions (5 takes, 9 references, 219 skips)
**With grouping**: 23 decisions (5 takes, 9 references, 9 batch skips covering ~219 articles)

Batch skip groups used:
```python
skip_groups = {
    "Harvey企業ブログSEO記事（10件）": 10,
    "Glean企業ブログ記事（11件）": 11,
    "Gary Marcus AI批判（8件）": 8,
    "Simon Willison短い引用・リリース（15件）": 15,
    "Pluralistic/Cory Doctorow（4件）": 4,
    "Ed Zitron AI経済批判（3件）": 3,
    "非AIコンテンツ（25件）": 25,
    "企業ブログSEO・プロダクト紹介（20件）": 20,
    "短いAI記事・引用・重複（90件以上）": 90,
}
```

### JSON structure for a batch skip entry

```json
{
    "item_id": "skip-batch-Harvey企業ブログSEO記事",
    "source": "various",
    "source_name": "various",
    "title": "[Harvey企業ブログSEO記事（10件）] 10件のバッチスキップ",
    "url": "",
    "raw_path": "",
    "recommended_action": "skip",
    "reason_ja": "★☆☆☆☆ Harvey企業ブログのSEO記事。entities/harvey.mdで既に包括的にカバー済み。個別記事のbody_excerptはアーカイブ時に補完。",
    "candidate_wiki_path": null,
    "body_excerpt": "Harvey企業ブログSEO記事（10件）: 10 articles batch-skipped."
}
```

## When to Use

- **Dreaming-group runs** with 100+ undecided raw articles (common when daily pipeline hasn't saturated)
- **Blog triage** with single-source-dominated batches (e.g., 15 Harvey articles, 12 Glean articles)
- **Any triage** where >50 articles share the same skip reason

## When NOT to Use

- **Newsletter triage** (typically 6-20 candidates — individual decisions are fine)
- **Small batches** (<30 articles — individual decisions provide better auditability)
- **Mixed-content batches** where each article has a different skip reason

## Implementation

In the triage script, replace individual skip loops with grouped entries:

```python
# Instead of:
for article in harvey_articles:
    decisions.append(make(item_id=f"harvey-skip-{i}", ..., skip, ...))

# Do:
decisions.append(make(
    item_id="skip-batch-harvey",
    source_name="Harvey Blog",
    title=f"[Harvey企業ブログSEO記事（{len(harvey_articles)}件）] {len(harvey_articles)}件のバッチスキップ",
    url="", raw_path="",
    action="skip",
    reason="★☆☆☆☆ Harvey企業ブログのSEO記事。entities/harvey.mdで既に包括的にカバー済み。",
    wiki_path=None,
    excerpt=f"Harvey blog batch: {len(harvey_articles)} articles batch-skipped."
))
```

## Archive Consideration

The `archive_triage.py` script processes decisions individually. For batch skip entries with empty `raw_path`, the archive will log them as URL-less entries. The downstream `dreaming-wiki-ingest` pipeline reads decisions by `recommended_action` — batch skip entries with `action=skip` are correctly filtered out.

If individual archiving is needed (e.g., for URL dedup), run the archive script BEFORE grouping, or include a note that batch entries should be expanded during archive.

## Yield Expectations

| Batch Size | Without Grouping | With Grouping | Reduction |
|------------|-----------------|---------------|-----------|
| 100 articles | 100 decisions | ~15 decisions | 85% |
| 200 articles | 200 decisions | ~23 decisions | 88% |
| 500 articles | 500 decisions | ~30 decisions | 94% |
