# Large HTML Article Extraction (when web_extract times out)

`web_extract` with LLM summarization reliably times out on articles >10K chars of content
(~50K+ chars of HTML). The browser fallback (`browser_navigate`) may also fail if Chrome
isn't installed. Use this curl + Python pipeline instead.

## Step 1: Download the HTML

```bash
curl -sL '<URL>' -o /tmp/article.html
wc -c /tmp/article.html   # verify download
```

## Step 2: Strip HTML to plain text

**Do NOT inline Python in `terminal`** — escaping issues with multiline strings are common.
Write a Python script via `write_file`, then execute it with `terminal`.

### Preferred approach: Preserve block elements as newlines

Simple tag-stripping collapses everything into one line (all whitespace between
paragraphs, headings, list items is lost). Instead, inject newlines at block-level
closing tags first, then strip all remaining tags.

```python
import re
import html as html_mod

with open('/tmp/article.html', 'r', encoding='utf-8') as f:
    raw = f.read()

# Remove script/style elements (they contain inline code with angle brackets)
raw = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', raw, flags=re.DOTALL)
raw = re.sub(r'<noscript[^>]*>.*?</noscript>', '', raw, flags=re.DOTALL)

# Inject newlines at block-level closing tags BEFORE stripping all tags
# This preserves paragraph/list/heading/section boundaries
raw = re.sub(r'</(p|div|h[1-6]|li|section|article|header|footer|main|nav|ul|ol|table|tr)>', '\n', raw)
raw = re.sub(r'<br\s*/?>', '\n', raw)

# Now strip all remaining HTML tags
text = re.sub(r'<[^>]+>', '', raw)

# Decode HTML entities (&amp; &lt; &mdash; etc.)
text = html_mod.unescape(text)

# Normalize whitespace (collapse runs, trim per-line)
lines = [l.strip() for l in text.split('\n')]
lines = [l for l in lines if l]  # remove blank lines
text = '\n'.join(lines)

with open('/tmp/article.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# Quick summary
print(f"Total: {len(text)} chars, {len(lines)} lines")
```

This typically produces ~200 lines of clean, navigable text for a 200KB+ HTML page,
making `read_file(offset=N, limit=200)` chunked reading simple.

### Fallback: simpler approach (may collapse to few lines)

Use only when the article structure doesn't benefit from block-element boundaries:

```python
import re

with open('/tmp/article.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL)
html = re.sub(r'<noscript[^>]*>.*?</noscript>', '', html, flags=re.DOTALL)

text = re.sub(r'<[^>]+>', ' ', html)
text = re.sub(r'\n{3,}', '\n\n', text)
text = re.sub(r'[ \t]{2,}', ' ', text)

with open('/tmp/article.txt', 'w', encoding='utf-8') as f:
    f.write(text)
```

## Step 3: Find the article section

Use `read_file` on `/tmp/article.txt` to find the article start marker (title, subtitle,
or opening sentence). Skip nav/header/footer boilerplate.

```bash
# Check positions of key markers
python3 -c "
t = open('/tmp/article.txt').read()
for marker in ['Article Title', 'opening phrase']:
    idx = t.find(marker)
    if idx >= 0: print(f'{marker}: position {idx}')
"
```

## Step 4: Read in chunks with read_file

Use `read_file(offset=N, limit=300)` in 300-line increments until you've covered the full
article. This avoids the LLM context explosion of reading the whole file at once.

## Step 5: Save as raw article

Write a Python script to add YAML frontmatter, filter to the article body (start marker →
end marker), and save:

```python
start = text.find('Article Title')
end = text.find('Related posts', start)  # or 'About the Authors', 'Comments'
article = text[start:end].strip()

frontmatter = f"""---
title: "Article Title"
date_published: YYYY-MM-DD
source: <URL>
type: article
author: Author Name
---

"""
with open('/tmp/article-clean.md', 'w') as f:
    f.write(frontmatter + article)
```

Then copy to wiki:
```bash
cp /tmp/article-clean.md ~/wiki/raw/articles/YYYY-MM-DD_source_slug.md
```

## Pitfalls

- **Don't inline Python in terminal**: escaping quotes/backslashes/newlines causes syntax errors. Always write a script file via `write_file` first.
- **532KB HTML → ~95K chars text** is typical for large technical blogs. Expect 5-6 `read_file` passes at 300 lines each.
- **End markers**: try `'Related posts'`, `'About the Authors'`, `'Comments'`, `'Share this'`, or `'Tags'` (in that order).
- **Nav menus**: the first 300+ lines will be nav/header/sidebar noise. Find the article title and jump there directly.
- **Single-line collapse**: Simple tag-stripping without block-element preservation produces 1-line output from any modern web page (all paragraph/heading boundaries vanish). The preferred approach above avoids this — it produced 197 lines from a 239KB Anthropic page.
