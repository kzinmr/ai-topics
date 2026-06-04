# Manual Cost Estimation Methodology

Fallback when `token_usage_collect.py` COST_REPORT parser produces unreliable data (most jobs show `input_tokens=0 output_tokens=0`).

## Quick Reference: Key Data Sources

| Source | Path | Use |
|--------|------|-----|
| Cron job list | `cronjob(action='list')` | Get all jobs with schedule, model, provider |
| COST_REPORT lines | `~/.hermes/cron/output/<job_id>/*.md` | Sample per-run token usage |
| Token DB (unreliable) | `~/.hermes/cron/data/token_usage/token_usage.db` | Only for jobs using strict `input_tokens=N output_tokens=N` format |
| Summary (unreliable) | `~/.hermes/cron/data/token_usage/summary.json` | Aggregated but ~80% data missing |
| Jobs definitions | `~/.hermes/cron/jobs.json` | Raw job configs (model, schedule, pre-run scripts) |
| Config | `~/.hermes/config.yaml` | Provider endpoints, fallback models |

## Methodology (Step by Step)

### 1. Identify LLM-consuming jobs
Run `cronjob(action='list')` and filter:
- Jobs with `model` set (not `null`) → LLM cost
- Jobs with `no_agent=true` or `script` only → $0 LLM cost

### 2. Separate by model/provider
Models observed in this deployment:
- `deepseek-v4-pro` ~ $1.00/M input, $4.00/M output (approximate)
- `deepseek-v4-flash` ~ $0.15/M input, $0.60/M output (approximate)
- `fireworks/qwen3.6-plus` ~ $0.30/M input, $0.90/M output (approximate)
- `deepseek-v4-pro` used for: newsletter-wiki-ingest, blog-wiki-ingest, active-crawl, slack-hot-posts, x-bookmarks-ingest, x-accounts-scan
- `deepseek-v4-flash` used for: newsletter-triage, blog-triage, trending-topics, dreaming-group, dreaming-wiki-ingest, wiki-health-fix, wiki-watchdog-fix, skeleton-enrich-daily, weekly-digest, tag-audit-weekly
- `fireworks/qwen3.6-plus` used for: wiki-health, wiki-graph-analysis, check-skill-inventory

### 3. Sample per-run costs from COST_REPORT lines
```bash
grep -r 'COST_REPORT' ~/.hermes/cron/output/<job_id>/ | tail -20
```
Extract token counts from the variety of formats. Common patterns:
- `input_tokens=~180K output_tokens=~4K` → 180K in, 4K out
- `total_tokens=45000` → roughly 40K in, 5K out
- `tokens_in=~85K tokens_out=~5.5K` → 85K in, 5.5K out
- `pages_created=5 pages_updated=3` → estimate from typical wiki ingest costs

### 4. Compute daily cost per job
```
daily_cost = per_run_cost × runs_per_day
```
Where `runs_per_day` is derived from the cron schedule expression.

### 5. Sum across jobs → monthly estimate
```
monthly = sum(daily_cost) × 30
```

## May 2026 Cost Estimate (Reference)

Built using this methodology on 2026-05-11, sampling last 7 days of COST_REPORT data.

### LLM API Costs

| Job | Model | Freq | Est tokens/run | Est $/day |
|-----|-------|------|:--:|:--:|
| newsletter-triage | v4-flash | daily | ~150K in + ~10K out | $0.15 |
| newsletter-wiki-ingest | v4-pro | daily | ~50K in + ~5K out | $0.30 |
| blog-triage | v4-flash | daily | ~150K in + ~5K out | $0.08 |
| blog-wiki-ingest | v4-pro | daily | ~40K in + ~5K out | $0.20 |
| trending-topics | v4-flash | daily | ~100K in + ~5K out | $0.05 |
| active-crawl | v4-pro | daily | ~45K in + ~5K out | $0.25 |
| dreaming-wiki-ingest | v4-flash | daily | ~30K in + ~3K out | $0.03 |
| wiki-health | qwen3.6-plus | daily | ~30K in + ~2K out | $0.12 |
| wiki-health-fix | v4-flash | daily | ~40K in + ~3K out | $0.04 |
| wiki-watchdog-fix | v4-flash | daily | ~20K in + ~2K out | $0.02 |
| skeleton-enrich-daily | v4-flash | daily | ~50K in + ~5K out | $0.04 |
| **slack-hot-posts** | **v4-pro** | **6×/day** | **~30K in + ~3K out** | **$0.90** |
| x-bookmarks-ingest | v4-pro | 2×/day | ~50K in + ~5K out | $0.50 |
| x-accounts-scan | v4-pro | q2d | ~60K in + ~5K out | $0.15 |
| dreaming-group | v4-flash | daily | ~5K in + ~2K out | $0.01 |
| Weekly digest | v4-flash | weekly | ~200K in + ~10K out | $0.03 |
| tag-audit-weekly | v4-flash | weekly | ~100K in + ~10K out | $0.02 |
| wiki-graph-analysis | qwen3.6-plus | weekly | ~60K in + ~5K out | $0.02 |
| check-skill-inventory | qwen3.6-plus | weekly | ~30K in + ~3K out | $0.01 |
| **TOTAL** | | | | **~$2.90/day** |

**Monthly LLM estimate: ~$87/month**

### Non-LLM Tools

| Category | Cost | Notes |
|----------|:----:|-------|
| X/Twitter API | $0–100/mo | Free tier if within rate limits; Basic tier $100/mo |
| Web search/extract | $0 | Hermes platform built-in, no external API cost |
| Gmail IMAP | $0 | Free tier |
| Git/GitHub | $0 | Free tier |
| Discord/Slack/Telegram | $0 | Bot API free |

### Cost Drivers (Largest to Smallest)
1. **slack-hot-posts** (v4-pro, 6×/day): ~$27/mo — single largest consumer
2. **x-bookmarks-ingest** (v4-pro, 2×/day): ~$15/mo
3. **newsletter-wiki-ingest** (v4-pro, daily): ~$9/mo
4. **active-crawl** (v4-pro, daily): ~$7.50/mo
5. **blog-wiki-ingest** (v4-pro, daily): ~$6/mo

### Caveats
- This is a **snapshot estimate** — token counts vary by day
- Interactive sessions (Discord chats like this one) are NOT included
- DeepSeek pricing may change — check `https://platform.deepseek.com/usage` for actual bills
- Model assignments may drift over time — verify with `cronjob list` before re-estimating
