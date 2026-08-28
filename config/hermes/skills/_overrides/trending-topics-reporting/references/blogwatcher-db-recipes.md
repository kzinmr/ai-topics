# Blogwatcher DB Query Recipes for Trending Topics

These are the exact SQL queries to run against `/opt/data/.blogwatcher/blogwatcher.db` during Phase 1 data collection.

## Overview

The `trending_topics.py` script produces a *topic-frequency table* (which terms appear across many articles). But it does NOT give you article-level detail — titles, source blogs, URLs, or publication dates. That's where direct DB queries come in. The pattern is:

1. **Run `trending_topics.py --days 3`** → get topic frequency table
2. **Query blogwatcher DB** → get article titles, URLs, source blogs for deep reading
3. **Find raw article files** → read the actual content

## Pitfall: Keyword List Blind Spots

The core AI keyword list below is good for catching technical AI/ML content (models, training, agents, safety) but systematically misses:

- **Conference/event coverage** (WWDC, Google I/O, GTC, Data+AI Summit)
- **Product-specific names** (Siri AI, North Mini Code, DiffusionGemma)
- **CEO/thought-leader essays**: CEO blog posts and X articles (Satya Nadella, Cory Doctorow, George Hotz) are often missed by the tech keyword list because their titles don't contain 'AI' or 'LLM' explicitly. The 'Nadella', 'Doctorow', 'Karp', 'Altman' keywords in Query 3a help, but the catch-all Query 3b (essay, manifesto, why I, thoughts on) is essential for catching these. CEO essays with >5,000 X bookmarks or >1M impressions should be treated as stronger signals than their raw source count suggests — see the **CEO/Thought-Leader essay weighting** heuristic in the main SKILL.md.
- **Socio-economic AI topics** (deflation, regulation, national security)

The primary workhorse query (3a) uses the tech keyword list. Always also run the broader event catch-all (3b) to surface conference, product, and opinion content that the tech list misses.

## Standard Queries

### 1. Total articles in last N days

```python
cur.execute("SELECT COUNT(*) FROM articles WHERE published_date >= date('now', '-3 days')")
```

### 2. Top blogs by article count (last 3 days)

Useful for identifying which sources are most active:

```python
cur.execute('''
SELECT b.name, COUNT(*) as c
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE a.published_date >= date('now', '-3 days')
GROUP BY b.name ORDER BY c DESC LIMIT 20
''')
```

### 3a. AI-relevant articles with details (primary workhorse)

```python
ai_keywords = ['AI', 'LLM', 'agent', 'model', 'GPT', 'Claude', 'OpenAI', 'Anthropic',
               'RL', 'fine-tun', 'reasoning', 'safety', 'inference', 'multimodal',
               'embedding', 'transformer', 'diffusion', 'Llama', 'Gemini', 'Mistral',
               'coding', 'RAG', 'MCP', 'training', 'RLHF', 'alignment', 'open source',
               'synthetic', 'RL', 'scale', 'evals', 'sandbox', 'prompt',
               # Event/product names that the basic tech keyword list misses
               'WWDC', 'Siri', 'Gemma', 'Nemotron', 'Codex', 'Augment', 'Cosmos',
               'Qwen', 'Cursor', 'Windsurf', 'Copilot', 'Mythos', 'Fable',
               'Cohere', 'North', 'Hotz', 'geohot', 'Amodei', 'Karpathy',
               # CEO / thought-leader essay authors
               'Nadella', 'Doctorow', 'Karp', 'Altman', 'Amodei', 'Raskin',
               # Conference / platform keywords
               'conference', 'GTC', 'Data + AI', 'Summit', 'launch', 'announce',
               'release', 'platform', 'ecosystem', 'integration',
               # Socio-economic AI topics
               'deflation', 'economics', 'regulation', 'policy', 'governance',
               'military', 'defense', 'national security', 'surveillance',
               'section 230', 'liability', 'open model', 'open weight']
conditions = ' OR '.join([f"a.title LIKE '%{kw}%'" for kw in ai_keywords])
cur.execute(f'''
SELECT a.title, b.name, a.url, a.published_date
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE a.published_date >= date('now', '-3 days')
AND ({conditions})
ORDER BY a.published_date DESC LIMIT 60
''')
```

### 3b. Broader event/product catch-all

```python
event_keywords = ['Apple', 'Google', 'Microsoft', 'Meta', 'NVIDIA', 'Amazon',
                  'introduces', 'announces', 'launches', 'unveils',
                  'WWDC', 'Build', 'IO', 'conference', 'keynote',
                  'interview', 'essay', 'manifesto', 'why I',
                  'thoughts on', 'reflections', 'lessons',
                  'enterprise', 'startup', 'funding', 'acquisition']
conditions = ' OR '.join([f"a.title LIKE '%{kw}%'" for kw in event_keywords])
cur.execute(f'''
SELECT a.title, b.name, a.url, a.published_date
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE a.published_date >= date('now', '-3 days')
AND ({conditions})
AND a.title NOT LIKE '%sponsor%'
ORDER BY a.published_date DESC LIMIT 30
''')
```

### 4. Unread article count by blog

```python
cur.execute('''
SELECT b.name, COUNT(*) as unread
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE a.is_read = 0
GROUP BY b.name ORDER BY unread DESC LIMIT 20
''')
```

## Raw Article Discovery

### By date (newer than N days ago)

```bash
find /opt/data/ai-topics/wiki/raw/articles -name "*.md" -mtime -3 2>/dev/null | sort | head -60
```

### By keyword in filename

```bash
find /opt/data/ai-topics/wiki/raw/articles -name "*keyword*" 2>/dev/null
```

### Dual-path search (canonical + cron HOME)

```bash
find /opt/data/ai-topics /opt/data/.hermes/home -path "*/raw/articles/*" -name "*keyword*" 2>/dev/null
```

Note: The cron HOME path (`/opt/data/.hermes/home/wiki/raw/articles/`) is often empty or has a time lag — new articles from today's blog-ingest go there first, but the `trending_topics.py` script scans both paths.

## Integration Pattern

Updated end-to-end flow from the 2026-06-12 run:

```text
1. trending_topics.py --days 3
   → Shows: Claude (55), Anthropic (41), evals (40), Google (33),
     OpenAI (26), MCP (20), Simon Willison (18), Gemini (14),
     coding agents (11), fine-tuning (11), Cursor (8), Qwen (8),
     RAG (8 NEW), sandboxing (8), red teaming (8), GPT (7 NEW),
     Gemma (7), Cognition (6), Dario Amodei (6), Gary Marcus (6)
   → Hot topics (4+ sources): 28 items
   → New page candidates: RAG, GPT, voice/speech

2. Blogwatcher DB queries 3a + 3b (60+30 = 90 articles)
   → Query 3a surfaces tech keywords (Claude, Anthropic, OpenAI, MCP, etc.)
   → Query 3b catches: Apple Siri AI WWDC, George Hotz deflationary essay,
     Dario Amodei policy post, Cohere North Mini Code launch

3. Deep reads:
   → Fable 5 guardrail controversy: simonwillison, jonready, theverge
   → Apple Siri AI: apple newsroom, techcrunch, daringfireball
   → Dario Amodei policy essay (~15K words)
   → George Hotz "AI will be massively deflationary"
   → Cohere North Mini Code (30B MoE, Apache 2.0)
   → Modal FlashAttention-4 inference optimization
   → NVIDIA Cosmos 3 + DiffusionGemma

4. Curation (event-driven signals the keyword list nearly missed):
   → Apple Siri AI: only matched via "AI" keyword; needed "WWDC" + "Apple" catch-all
   → George Hotz: "deflationary" not in original keyword list
   → Cohere North Mini: "North" + "Cohere" added from this session
   → Dario Amodei: "essay" + "policy" only from catch-all query
```
