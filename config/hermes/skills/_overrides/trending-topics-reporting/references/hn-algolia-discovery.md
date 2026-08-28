# HN Algolia API Discovery for Trending AI Stories

Use HN Algolia's `search_by_date` endpoint as a complementary trending-source alongside RSS/blogwatcher/raw articles. Particularly useful for major AI events (model launches, policy announcements, Show HN tools) that generate concentrated HN discussion.

## API Endpoint Selection

| Endpoint | Purpose | When |
|----------|---------|------|
| `search_by_date` | Recency-ordered results | **Always use this** for trending discovery |
| `search` | Relevance-ranked results | Older/more-general queries, not for recency |
| `/items/{id}` | Single story metadata | **Avoid** — returns `num_comments=0` even for hot stories |

**Critical quirk**: The `/items/{id}` endpoint returns `num_comments: 0` for all stories. To get accurate comment counts, use `search_by_date` with title keywords and match by `objectID`.

## Multi-Query Strategy

HN Algolia's search is keyword-based, not semantic. A single query misses relevant stories. Run **8-15 keyword queries** in parallel, collect all hits, deduplicate by `objectID`:

```python
queries = [
    'AI+agent+LLM',
    'OpenAI+Claude+Anthropic',
    'DeepSeek',
    'inference+model+release',
    'coding+agent',
    'MCP+protocol',
    'AI+safety+sandbox',
    'LLM+benchmark',
    'fine-tuning+training',
    'RAG+vector+embedding',
    'speculative+decoding',
    'AI+open+source',
    'agent+framework+harness',
]
```

Use `+` for spaces in URLs (NOT `%20`). Python urllib handles this natively.

## Python urllib Pattern (Required)

`curl | python3` pipes are blocked by tirith. Always use inline Python:

```python
import json, urllib.request

all_hits = []
seen_ids = set()

for q in queries:
    url = f'https://hn.algolia.com/api/v1/search_by_date?query={q}&tags=story&hitsPerPage=50'
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = json.loads(resp.read().decode())
    for h in data.get('hits', []):
        oid = h.get('objectID')
        if oid and oid not in seen_ids:
            seen_ids.add(oid)
            all_hits.append(h)
```

## Filtering Pipeline

```python
# 1. Date cutoff (e.g., last 3 days)
cutoff = '2026-06-25T00:00:00.000Z'
filtered = [h for h in all_hits if h.get('points', 0) >= 5 and h.get('created_at', '') >= cutoff]

# 2. AI relevance keyword filter (avoid non-AI stories like housing, shipping, retrocomputing)
ai_terms = ['ai', 'llm', 'gpt', 'claude', 'openai', 'anthropic', 'deepseek',
            'agent', 'neural', 'model', 'inference', 'transformer', 'diffusion',
            'embedding', 'rag', 'fine-tun', 'finetun', 'benchmark', 'eval',
            'mcp', 'coding+ai', 'ai+coding', 'cursor+ai', 'codex',
            'safety+ai', 'alignment', 'jailbreak']

# 3. Sort by points descending, take top 15
filtered.sort(key=lambda h: h.get('points', 0), reverse=True)
top = filtered[:15]
```

## Point Threshold Rules

| Day Type | Threshold | Rationale |
|----------|-----------|-----------|
| Weekday (Mon-Thu) | ≥8 | Normal submission volume |
| Weekend (Fri-Sun) | ≥5 | Lower submission volume; drop to catch enough stories |
| Major event day | ≥20 | Flood of submissions; raise to filter noise |

## Deduplication Beyond objectID

The same news event spawns multiple submissions with different objectIDs. After initial dedup by objectID, **manually review** for duplicate topics:

- **Model announcements**: OpenAI GPT release → 5+ HN submissions from different outlets (WaPo, Verge, TechCrunch, etc.). Keep only the highest-points entry per angle (official blog post + top news coverage).
- **Policy stories**: Same government action covered by multiple outlets. Keep highest-points unique angle.
- **Show HN projects**: Usually unique, rarely duplicated.

**Rule of thumb**: If two stories share the same core event, keep only the highest-pointed one unless they provide genuinely different perspectives (e.g., official announcement vs. third-party analysis).

## Getting Accurate Comment Counts

After selecting final stories, fetch comment counts via `search_by_date` with title keywords:

```python
# For each selected story, search by its title keywords
oids_to_fetch = [('48690101', 'U.S. government will decide'), ...]
for oid, keyword in oids_to_fetch:
    q = keyword.replace(' ', '+')[:80]
    url = f'https://hn.algolia.com/api/v1/search_by_date?query={q}&tags=story&hitsPerPage=5'
    with urllib.request.urlopen(url, timeout=10) as resp:
        data = json.loads(resp.read().decode())
    for h in data.get('hits', []):
        if h.get('objectID') == oid:
            # h.get('num_comments') is now accurate
            break
```

**Pitfall**: Title keywords may match multiple stories. Always verify by `objectID` match, not just first result.

## Wiki Relevance Tagging

Assign relevance tags for downstream wiki ingestion:

| Tag | When |
|-----|------|
| `LLM/model` | Model announcements, comparisons, releases (GPT, Claude, Gemini, DeepSeek, Mythos) |
| `AI agent` | Agent frameworks, tooling, harnesses, agent-specific models |
| `AI policy` | Government regulation, export controls, staggered releases |
| `AI safety` | Guardrails, sandboxing, alignment research |
| `open-source` | Open-weight releases, OSS tools, open datasets |
| `coding/dev tools` | IDE plugins, coding agents, developer workflows |
| `model routing` | LLM routers, hybrid local/cloud inference |
| `inference/reasoning` | Speculative decoding, optimization, serving |
| `AI+society` | Backlash, job impact, economic analysis |
| `AI business` | Startup funding, pricing changes, enterprise adoption |
| `benchmark/eval` | New benchmarks, evaluation methodologies |
| `MCP/protocol` | Model Context Protocol, agent communication standards |

## Weekend Slow-Week Heuristic

When weekday queries return < 3 stories with ≥8 points, the weekend threshold (5 points) still applies. In very slow periods, consider expanding to 4-day windows or lowering to 3 points for niche Show HN projects.

## Example: June 2026 GPT-5.6 / Mythos Week

The GPT-5.6 Sol announcement and government gatekeeping dominated HN (4+ stories >500 pts). Anthropic's Mythos restricted release was the second wave. Combined, these two stories drove >3000 points of HN activity. Non-AI stories (housing crisis, farmer arrest, retrocomputing) had to be manually filtered out.
