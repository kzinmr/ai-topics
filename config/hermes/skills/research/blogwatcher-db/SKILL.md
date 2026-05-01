---
name: blogwatcher-db
description: Query the blogwatcher-cli SQLite database for RSS scan results. Use pre-verified column names and query templates to avoid errors.
category: research
verified: 2026-04-13
---

# Blogwatcher Database Query Skill

Pre-verified query templates for the blogwatcher-cli SQLite database.
**DO NOT guess column names** — use only the schema documented below.

## Database Location

- **Primary path:** `/opt/data/.blogwatcher/blogwatcher.db`
- **Legacy/previous path:** `/home/exedev/.blogwatcher-cli/blogwatcher-cli.db`
- **Type:** SQLite3
- **⚠️ DB name is `blogwatcher.db`, NOT `blogwatcher-cli.db`** — use `find / -name 'blogwatcher.db'` for discovery, not the CLI binary name.

### DB Discovery Fallback

If the expected path doesn't exist, discover the actual location:

```bash
find / -path '*.blogwatcher*' -name '*.db' 2>/dev/null
```

The database may be stored under `/opt/data/.blogwatcher/` rather than the user home directory, especially when blogwatcher-cli runs from `/opt/data/bin/`.

## Verified Schema

### Table: `blogs`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Blog ID |
| `name` | TEXT | NOT NULL | Blog name (e.g., "simonwillison.net", "r/LocalLLaMA") |
| `url` | TEXT | NOT NULL, UNIQUE | Blog homepage URL |
| `feed_url` | TEXT | nullable | RSS/Atom feed URL |
| `scrape_selector` | TEXT | nullable | CSS selector for HTML scraping fallback |
| `last_scanned` | TIMESTAMP | nullable | Last scan timestamp (ISO 8601) |

### Table: `articles`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Article ID |
| `blog_id` | INTEGER | NOT NULL, FK→blogs.id | Source blog ID |
| `title` | TEXT | NOT NULL | Article title |
| `url` | TEXT | NOT NULL, UNIQUE | Article URL |
| `published_date` | TIMESTAMP | nullable | When article was published (ISO 8601 from RSS) |
| `discovered_date` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When blogwatcher discovered it |
| `is_read` | BOOLEAN | DEFAULT FALSE (0/1) | Read/unread status |
| `categories` | TEXT | nullable | JSON array of tags, e.g. `["llms","machine-learning"]` |

### Table: `schema_migrations`

| Column | Type | Description |
|--------|------|-------------|
| `version` | uint64 | Migration version |
| `dirty` | bool | Migration state |

## ⚠️ Columns That Do NOT Exist

These are commonly guessed but **do not exist**:
- `published_at` → use `published_date` or `discovered_date`
- `source` → use `blog_id` JOIN `blogs.name`
- `author` → not tracked
- `content` / `body` / `text` → not stored (URLs only)
- `tags` → use `categories` (JSON array)
- `created_at` → use `discovered_date`
- `updated_at` → not tracked

## Verified Query Templates

⚠️ **sqlite3 CLI may not be available** in the agent environment (no system `sqlite3` binary). Use Python's built-in `sqlite3` module instead for reliable queries (see Python Usage Pattern below). The SQL templates below are still correct — use them as SQL strings in Python's `conn.execute()`. 

### Daily scan — articles discovered on a specific date

```sql
SELECT b.name, a.title, a.url, a.published_date, a.discovered_date, a.categories
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE DATE(a.discovered_date) = 'YYYY-MM-DD'
ORDER BY b.name, a.discovered_date DESC;
```

### Unread articles (triage queue)

```sql
SELECT b.name, a.title, a.url, a.discovered_date
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE a.is_read = 0
ORDER BY a.discovered_date DESC;
```

### Articles by specific blog

```sql
SELECT a.title, a.url, a.published_date, a.discovered_date, a.is_read, a.categories
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE b.name = 'simonwillison.net'
ORDER BY a.discovered_date DESC;
```

### Articles by blog + date range

```sql
SELECT a.title, a.url, a.published_date, a.discovered_date, a.categories
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE b.name = 'r/LocalLLaMA'
  AND DATE(a.discovered_date) BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'
ORDER BY a.discovered_date DESC;
```

### Count articles per blog (all time)

```sql
SELECT b.name, COUNT(*) as cnt
FROM articles a JOIN blogs b ON a.blog_id = b.id
GROUP BY b.name
ORDER BY cnt DESC;
```

### Count articles per blog on specific date

```sql
SELECT b.name, COUNT(*) as cnt
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE DATE(a.discovered_date) = 'YYYY-MM-DD'
GROUP BY b.name
ORDER BY cnt DESC;
```

### Filter by category (JSON contains tag)

```sql
SELECT b.name, a.title, a.url, a.discovered_date, a.categories
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE a.categories LIKE '%"AI%"%'
   OR a.categories LIKE '%"llm%"%'
   OR a.categories LIKE '%"machine-learning%"%'
ORDER BY a.discovered_date DESC;
```

### Recent articles across all blogs (last N days)

```sql
SELECT b.name, a.title, a.url, a.published_date, a.discovered_date, a.categories
FROM articles a JOIN blogs b ON a.blog_id = b.id
WHERE a.discovered_date > datetime('now', '-N days')
ORDER BY a.discovered_date DESC;
```

## Python Usage Pattern

```python
import sqlite3
import json
import os

DB_PATH = "/opt/data/.blogwatcher/blogwatcher.db"
# Fallback: discover DB if not at primary path
if not os.path.exists(DB_PATH):
    import subprocess
    result = subprocess.run(
        ["find", "/", "-path", "*.blogwatcher*", "-name", "*.db"],
        capture_output=True, text=True, timeout=15
    )
    candidates = [p.strip() for p in result.stdout.strip().split("\n") if p.strip()]
    if candidates:
        DB_PATH = candidates[0]
        print(f"Discovered DB at: {DB_PATH}", file=__import__("sys").stderr)

def query_daily_scan(date_str):
    """Get all articles discovered on a specific date, grouped by blog."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT b.name, a.title, a.url, a.published_date, a.discovered_date, a.categories
        FROM articles a JOIN blogs b ON a.blog_id = b.id
        WHERE DATE(a.discovered_date) = ?
        ORDER BY b.name, a.discovered_date DESC;
    """, (date_str,)).fetchall()
    
    # Group by blog
    blogs = {}
    for row in rows:
        if row['name'] not in blogs:
            blogs[row['name']] = []
        blogs[row['name']].append({
            'title': row['title'],
            'url': row['url'],
            'published_date': row['published_date'],
            'discovered_date': row['discovered_date'],
            'categories': json.loads(row['categories']) if row['categories'] else []
        })
    conn.close()
    return blogs

def generate_daily_report(date_str, blogs):
    """Generate markdown report for inbox/rss-scans/."""
    total = sum(len(arts) for arts in blogs.values())
    md = f"""# Daily RSS Scan Report — {date_str}

> Source: blogwatcher-cli RSS scan
> Total articles: {total}

"""
    # Sort: individual blogs first, then Reddit subs
    order = sorted(blogs.keys(), key=lambda x: (x.startswith('r/'), x.lower()))
    for blog_name in order:
        md += f"## {blog_name}\n\n"
        for art in blogs[blog_name]:
            md += f"- [{art['title']}]({art['url']})\n"
        md += "\n"
    return md
```

## Report Output Path

- Directory: `~/ai-topics/inbox/rss-scans/`
- Filename: `daily-scan-YYYY-MM-DD.md`
- After creation, commit: `cd ~/ai-topics && git add inbox/rss-scans/ && git commit -m "wiki: daily RSS scan YYYY-MM-DD" && git push`

## Execution Tips

### Write a standalone .py script, not inline `-c`

Passing Python code inline via `terminal("python3 -c ...")` is **prone to quote-escaping failures** — especially when the code contains triple-quoted strings or nested single quotes. Instead, write the script to `/tmp/` first, then execute it:

```bash
# Write script first (using write_file or echo)
python3 /tmp/query_blogwatcher.py
```

### Quick one-liner for counting articles

For a simple count (no complex SQL), this pattern works in a single terminal call:

```python
python3 -c "import sqlite3; print(sqlite3.connect(DB_PATH).execute('SELECT COUNT(*) FROM articles').fetchone()[0])"
```

Replace `DB_PATH` with the actual path.

## Pitfalls

1. **`published_at` does not exist** → use `published_date` or `discovered_date`
2. **`source` does not exist** → JOIN `blogs.name` via `blog_id`
3. **`categories` is JSON, not comma-separated** → use `LIKE '%"tag"%'` or parse with `json.loads()`
4. **`is_read` is 0/1** → use `WHERE is_read = 0` not `WHERE is_read = FALSE`
5. **`DATE()` function** → `DATE(a.discovered_date) = 'YYYY-MM-DD'` for date filtering
6. **No article content stored** → only URLs; scrape with `web_extract` if needed
7. **`published_date` can be NULL** → articles without RSS pub date have this set to NULL
8. **`last_scanned` on blogs** → ISO 8601 format, use to check freshness
9. **sqlite3 CLI may not be installed** — use Python's sqlite3 module instead
10. **DB may not be at the expected path** — run DB Discovery Fallback (see above) before assuming location
11. **DB filename is `blogwatcher.db`, not `blogwatcher-cli.db`** — adjust `find` patterns accordingly
