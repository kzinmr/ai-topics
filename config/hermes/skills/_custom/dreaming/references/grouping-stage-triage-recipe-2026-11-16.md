# Dreaming-GROUP stage role & cluster schema (validated 2026-11-16)

When invoked as **dreaming-group** (18:10 UTC stage, between dreaming-collect and dreaming-wiki-ingest), the job is GROUP + triage only.

## Role boundary
- Do NOT create/update wiki pages, run archive_triage.py, or edit log.md/index.md — the downstream dreaming-wiki-ingest consumes `grouped_themes_latest.json` and executes enrichment + archiving.
- Healthy saturation-day output: 0 takes, 3-5 reference candidates, batch-skips. Do not manufacture a take.

## Cluster JSON schema that downstream reads
Save via write_file→`terminal python3 /tmp/dreaming_group_<date>.py` to `/opt/data/.hermes/cron/data/dreaming/grouped_themes_latest.json` (NEVER a heredoc — CJK `summary_ja` in a heredoc trips tirith:confusable_text; write_file does not):

```json
{"checkpoint_run_id": "...", "triage_timestamp": "...", "source": "dreaming",
 "summary_ja": "...",
 "clusters": [{"id": "...", "summary": "<=200 chars", "articles": ["<raw basenames>"],
               "coverage": "which pipeline/log entry covers it", "recommended_action": "skip|reference|batch-skip"}],
 "takes_expected": 0,
 "reference_candidates": ["<raw basenames>"]}
```

## Workflow that got 45 raws → 9 clusters → 0 takes / 4 refs in ~10 calls (2026-11-16)
1. **Prior triage check first**, no pipes:
   `python3 -c "import json;d=json.load(open('/opt/data/.hermes/cron/data/dreaming/triage_latest.json'));print(d['checkpoint_run_id'], d['triage_timestamp'], len(d['decisions']))"`
2. **Empty checkpoint (`total_articles: 0`, `recent_raw_articles: N`) → fast filesystem scan**: `ls -t wiki/raw/articles | head -80` covers the 3-day sitemap/active-crawl window; count with `find wiki/raw/articles -name "2026-11-1[456]*" | wc -l`.
3. **One grep sweep is the saturation proof**: `grep -in "<kw1>\|<kw2>\|<kw3>" wiki/log.md | head -15` — the trending-topics and active-crawl entries name the EXACT pages they created/updated per topic (incl. per-article "Raw:" lists), so a single grep per cluster answers covered-vs-gap. If a cluster's topics appear in a same-day/next-day log entry → saturated, skip. Only zero-log-hit articles become reference_candidates.
4. Spot-read heads of uncertain raws (`head -c 500 <file>`) to classify before deciding take/reference/skip — sitemap raws with nav chrome still need a peek (Hex x6 marketing batch-skip, but Hex robots-rewrite had real substance).
5. Verify every `cluster articles` basename exists (`ls wiki/raw/articles/<basename>`) before saving — downstream enrichment scripts die on FileNotFoundError for hallucinated basenames.
6. Post-save verify: `python3 -c "import json;d=json.load(open(PATH));print('clusters',len(d['clusters']))"`.

## 2026-11-16 outcome (reference example)
45 raws (Nov 13-16) → 9 clusters: NVIDIA-Huang-exit-saga, model-releases-2026H2, inference-training-research, agent-tooling-sandboxes, ai-slop-backlash, ai-code-open-source-ethics, enterprise-vendor-sitemap-batch, education-bookmarks, non-ai. 0 takes; 4 references: pinecone-mcp-server check/load, hex robots-rewrite, harvey ethical-wall, guardian godel-notebooks.
