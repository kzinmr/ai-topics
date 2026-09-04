# Dreaming — Knowledge Consolidation Cycle (Full Reference)

## Step 0: Duplicate Check (MANDATORY)
Before processing, review adjacent scheduled jobs:
1. Daily Inbox Update (23:00 JST) — RSS scan + Newsletter triage + Wiki ingest
2. Daily Wiki Update Report (20:00 JST)
3. Daily Active Knowledge Crawl (00:00 JST)
4. Skill Inventory Check (01:00 JST)

Rules: Don't re-process, don't duplicate concept pages, reference existing assessments.

## Phase 1: Light Sleep — Screening & Grouping
Group articles by semantic themes. Flag articles appearing in multiple sources (higher significance).

## Phase 2: REM — Flat Synthesis
Weighted scoring WITHOUT newsjacking bias:
- relevance (0.30), frequency (0.25), query_diversity (0.15), recency (0.15), consolidation (0.10), conceptual_richness (0.05)
- ≥ 0.65: Create/update wiki page
- 0.45-0.65: Add to existing page or log for review
- < 0.45: Skip

## Phase 3: NJ Delivery Filter
| Score | Presentation |
|-------|-------------|
| ≥ 4 | Lead story |
| 3 | Secondary |
| 2 | Brief mention |
| ≤ 1 | Omit from delivery (wiki still updated) |

## Phase 4: Deep Sleep — Replay-Safe Integration
Check existing pages, create/update, cross-references (≥2), index/log update, commit.

## Sub-Patterns
- **A (Depth check)**: Read existing page before updating — don't update if already covered
- **B (Newsletter noise)**: Filter Substack UI elements before scoring
- **C (Batch entity)**: Create missing entity pages for recurring people/companies
- **D (Dedup matrix)**: Check filename, index entry, content grep, session_search before creating

## 0-Article Recovery Workflow (Shell Commands)

When the dreaming checkpoint reports `collected_articles=0`, raw articles may still exist that other pipelines didn't consume.

### Step 1: Count recent raw articles
```bash
find ~/wiki/raw/articles -name "*.md" -mtime -3 -size +500c | wc -l
```

### Step 1.5: Cross-pipeline dedup check (FIRST — saves the most time)
Before scanning raw articles, check the latest blog triage JSON. This immediately rules out the entire blog-ingest batch (typically 15-20 articles already decided as skip/reference), catching ~70% of raw articles from the blog pipeline.

```bash
ls -la ~/.hermes/cron/data/blog_ingest/triage_latest.json
ls -la ~/.hermes/cron/data/newsletter/triage_latest.json
```

### Step 2: Find genuinely unprocessed articles
```bash
find ~/wiki/raw/articles -name "*.md" -size +500c -mtime -3 | while read f; do
  base=$(basename "$f" .md)
  count=$(grep -rl "$base" ~/ai-topics/wiki/entities/ ~/ai-topics/wiki/concepts/ ~/ai-topics/wiki/log.md 2>/dev/null | wc -l)
  if [ "$count" -eq 0 ]; then
    size=$(stat -c%s "$f")
    echo "UNPROCESSED: $base ($size bytes)"
  fi
done
```

### Step 3: Filter by AI relevance
Read each unprocessed article's first 50+ lines. Skip non-AI content.

### Step 4: Check existing entity page coverage
```bash
ls ~/ai-topics/wiki/entities/<entity>.md 2>/dev/null && echo "EXISTS" || echo "MISSING"
grep -E "^##" ~/ai-topics/wiki/entities/<entity>.md
grep -i "keyword-from-article" ~/ai-topics/wiki/entities/<entity>.md
```

### Step 5: Build triage JSON
Use `write_file` to `/tmp/dreaming_triage.py` then `terminal python3 /tmp/dreaming_triage.py`. Use `None` (Python) not `null` (JS) for optional fields.

### Step 6: Archive skip/reference items
```bash
cd ~/ai-topics && python3 scripts/archive_triage.py dreaming --keep-reference
```

## Pitfalls
- Duplicate detection is MANDATORY
- Pre-commit hook blocks on unknown tags
- Always check existing pages first
- Log.md corruption via patch (accidental `|` prefix)
- Pre-run script timeout → fallback file at `/opt/data/.hermes/cron/data/dreaming/grouped_themes_latest.json`
- Stale dreaming themes (2-3 days old) may already be processed by daily pipelines
- 0-article doesn't mean nothing to do
- Cross-pipeline dedup order matters
- `execute_code` blocked in cron mode
- `-mtime` window must match

## Dreaming Triage Checkpoint Recovery

**Pre-run script format**: `{"ok": false, "error": "failed to parse JSON response from dreaming-group output", "output_path": "..."}`

**Recovery**: Check `${HERMES_HOME}/cron/data/dreaming/triage_latest.json` first. If it exists and contains valid JSON with `decisions` array, the triage agent saved the checkpoint before attempting the render. Just read it and proceed.

**Verification**: Always verify reference item recommendations by reading the target entity/concept page. The triage agent may over/under-rate content. In a June 2026 run, 2/8 reference items were false positives (already covered in existing pages).
