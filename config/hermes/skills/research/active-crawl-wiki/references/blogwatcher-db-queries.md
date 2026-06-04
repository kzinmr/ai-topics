# Blogwatcher DB Query Patterns

Canonical blogwatcher DB path: `/opt/data/.blogwatcher/blogwatcher.db`
(Fallback: `/opt/data/ai-topics/blogwatcher.db` — may be empty/initial)

## Schema

```sql
-- Tables: blogs, articles

-- blogs columns: id, name, url, feed_url, scrape_selector, last_scanned
-- articles columns: id, blog_id, title, url, published_date, discovered_date, is_read
```

## Verified Query Patterns

### Recent articles (last N days)
```python
import sqlite3
conn = sqlite3.connect('/opt/data/.blogwatcher/blogwatcher.db')
rows = conn.execute("""
    SELECT b.name, a.title, a.url, a.published_date, a.discovered_date
    FROM articles a JOIN blogs b ON a.blog_id = b.id
    WHERE DATE(a.discovered_date) >= date('now', '-3 days')
    ORDER BY a.discovered_date DESC
    LIMIT 100
""").fetchall()
```

### Activity by blog
```python
rows = conn.execute("""
    SELECT b.name, COUNT(*) as cnt, MAX(a.discovered_date) as latest
    FROM articles a JOIN blogs b ON a.blog_id = b.id
    WHERE DATE(a.discovered_date) >= date('now', '-3 days')
    GROUP BY b.name ORDER BY cnt DESC
""").fetchall()
```

### Total article count
```python
total = conn.execute('SELECT COUNT(*) FROM articles').fetchone()[0]
```

## Environment Notes

- **`sqlite3` CLI is not available** — use `python3 -c "import sqlite3"` for all queries
- **Column names are snake_case**: `published_date`, `discovered_date` (not `published`, `discovered_at`)
- **URL verification**: The `url` column may contain incorrect slugs. If a URL returns 404, check the RSS feed at the blog's `/blog/rss.xml` or `/rss.xml` endpoint for the correct URL.
