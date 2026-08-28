#!/usr/bin/env python3
"""Combined blogwatcher DB query for trending-topics runs.

Replaces the hand-written /tmp script pattern: one pass outputs
(1) total articles last 3 days, (2) top blogs by count, (3) AI-relevant
article titles+URLs (combined 3a technical + 3b event/product keyword
lists), (4) unread-count health check.

Usage:
    python3 trending_db_query.py [days]
    # default window = 3 days; pass e.g. 7 for weekly-digest mode

Cron-safe: write via write_file then run with terminal(); do NOT pipe
curl into python, and do NOT use execute_code (blocked in cron).
"""
import sqlite3
import sys
import os

days = int(sys.argv[1]) if len(sys.argv) > 1 else 3
DB_PATH = "/opt/data/.blogwatcher/blogwatcher.db"
if not os.path.exists(DB_PATH):
    import subprocess
    r = subprocess.run(["find", "/", "-path", "*.blogwatcher*", "-name", "*.db"],
                       capture_output=True, text=True, timeout=15)
    cands = [p.strip() for p in r.stdout.strip().split("\n") if p.strip()]
    if cands:
        DB_PATH = cands[0]
        print(f"Discovered DB: {DB_PATH}", file=sys.stderr)

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# 1. Total articles
cur.execute("SELECT COUNT(*) FROM articles WHERE DATE(discovered_date) >= DATE('now', ?)", (f'-{days} days',))
print(f"TOTAL_ARTICLES_{days}D: {cur.fetchone()[0]}")

# 2. Top blogs by count
cur.execute("""
    SELECT b.name, COUNT(*) as c FROM articles a JOIN blogs b ON a.blog_id = b.id
    WHERE DATE(a.discovered_date) >= DATE('now', ?)
    GROUP BY b.name ORDER BY c DESC LIMIT 25
""", (f'-{days} days',))
print(f"\nTOP_BLOGS_{days}D:")
for row in cur.fetchall():
    print(f"  {row['name']}: {row['c']}")

# 3. AI-relevant articles (combined 3a + 3b keyword lists)
ai_keywords = ['AI', 'LLM', 'agent', 'model', 'GPT', 'Claude', 'OpenAI', 'Anthropic',
    'RL', 'fine-tun', 'reasoning', 'safety', 'inference', 'multimodal',
    'embedding', 'transformer', 'diffusion', 'Llama', 'Gemini', 'Mistral',
    'coding', 'RAG', 'MCP', 'training', 'RLHF', 'alignment', 'open source',
    'synthetic', 'scale', 'evals', 'sandbox', 'prompt', 'Cursor',
    'Windsurf', 'memory', 'agentic', 'distillation', 'quantization',
    'Nemotron', 'Codex', 'augment', 'cosmos',
    'Hotz', 'Amodei', 'Nadella', 'Doctorow', 'Karp', 'Altman',
    # 3b event/product catch-all
    'Gemma', 'Qwen', 'DeepSeek', 'Muse', 'Grok', 'Sierra', 'Perplexity', 'Mistral',
    'NVIDIA', 'Google', 'Meta', 'Microsoft', 'xAI', 'Anthropic',
    'launch', 'release', 'announce', 'open-weight', 'open weight', 'weights',
    'essay', 'interview', 'thoughts on', 'benchmark', 'SWE-bench', 'τ-bench', 'tau-bench',
    'price', 'pricing', 'cost', 'GPU', 'chip', 'datacenter', 'inference',
    'lawsuit', 'legal', 'regulation', 'policy', 'security', 'vulnerab', 'hack',
    'OpenClaw', 'Clawdbot', 'Fable', 'Mythos', 'Sol', 'Astra', 'MCP-Atlas',
    'speech', 'voice', 'audio', 'watermark', 'SynthID', 'RLVR', 'reasoning trace']

conditions = ' OR '.join([f"a.title LIKE '%{kw}%'" for kw in ai_keywords])
cur.execute(f"""
    SELECT a.title, b.name, a.url, a.published_date, a.discovered_date
    FROM articles a JOIN blogs b ON a.blog_id = b.id
    WHERE DATE(a.discovered_date) >= DATE('now', ?) AND ({conditions})
    ORDER BY a.discovered_date DESC, b.name
    LIMIT 120
""", (f'-{days} days',))
rows = cur.fetchall()
print(f"\nAI_RELEVANT_ARTICLES ({len(rows)}):")
for r in rows:
    print(f"  [{r['discovered_date'][:10]}] {r['name']}: {r['title']} | {r['url']}")

# 4. Unread count by blog (health check)
cur.execute("""
    SELECT b.name, COUNT(*) as c FROM articles a JOIN blogs b ON a.blog_id = b.id
    WHERE a.is_read = 0 GROUP BY b.name ORDER BY c DESC LIMIT 10
""")
print("\nUNREAD_BY_BLOG:")
for row in cur.fetchall():
    print(f"  {row['name']}: {row['c']}")

conn.close()
