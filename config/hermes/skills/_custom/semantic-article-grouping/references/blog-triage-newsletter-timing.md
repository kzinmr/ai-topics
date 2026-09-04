# Blog Triage → Newsletter Triage Timing Cross-Reference

Validated July 2026: blog-triage (07:30) runs 10 minutes AFTER newsletter-triage (07:20) but 10 minutes BEFORE newsletter-wiki-ingest (07:40). This creates a specific cross-pipeline dedup window unique to blog triage.

## What Blog Triage Can Check

### ✅ Newsletter triage JSON (available)
The file at `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` IS from today's run (07:20). It contains:
- `recommended_action: take` for model releases (Sonnet 5, GPT-5.6, Fable 5, etc.)
- The newsletter's topics and priority classifications
- `candidate_wiki_path` — where the newsletter pipeline plans to create concept pages

**How to use it**: Before marking a model-release blog article as `take` (new concept needed), grep the newsletter triage JSON for the model name. If the newsletter already classified it as `take`, downgrade your blog article to `reference` (the model concept page is being created by the newsletter pipeline; your article becomes entity enrichment for the author's page).

### ❌ Newsletter wiki-ingest output (NOT available)
The pipeline at `${HERMES_HOME}/cron/data/newsletter/triage_latest.json` feeds into `newsletter-wiki-ingest` which runs at 07:40 — 10 minutes AFTER blog-triage. Concept pages (e.g., `concepts/claude/sonnet-5.md`) may NOT exist on disk yet even though the newsletter triage decided to create them.

**Do NOT** check `find ~/wiki/concepts -name "*sonnet-5*"` at blog-triage time — a missing concept page does NOT mean the topic is ungathered. It means the wiki-ingest pipeline hasn't run yet.

## Concrete Example (July 1, 2026)

Blog-triage found Simon Willison's "What's new in Claude Sonnet 5" article with detailed tokenizer measurements (English 1.42x, Chinese 1.01x token growth). Checking the newsletter triage JSON revealed AINews "Sonnet 5 Today and Fable 5 Tomorrow" classified as a model-release take. Decision: downgrade from ★★★★★ to ★★★☆☆ (entity enrichment for `entities/simon-willison.md`).

## Verification Technique

```bash
# At blog-triage time (~07:30), check:
python3 -c "
import json
f = '/opt/data/.hermes/cron/data/newsletter/triage_latest.json'
d = json.load(open(f))
takes = [x for x in d.get('decisions',[]) if x.get('recommended_action')=='take']
model_takes = [t for t in takes if any(k in (t.get('title','')+t.get('reason_ja','')).lower() for k in ['sonnet','fable','gpt-','model','release'])]
for t in model_takes:
    print(f'{t[\"title\"]}: take → {t.get(\"candidate_wiki_path\",\"?\")}')"
```

If model_takes is non-empty, those concept pages are being created by the newsletter pipeline. Your blog articles covering the same models should be entity enrichment only.
