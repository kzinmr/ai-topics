# X Article Retrieval Chain — Full Walkthrough (Garry Tan Case)

## The Article

- **Author:** Garry Tan (@garrytan), CEO of Y Combinator
- **Title:** "Meta-Meta-Prompting: The Secret to Making AI Agents Work"
- **Tweet URL:** https://x.com/garrytan/status/2053127519872614419
- **Article URL:** https://x.com/i/article/2052898104039657472
- **Date:** 2026-05-09
- **Stats:** 437 RT, 119 replies, 3,262 likes, 103 quotes, 10,284 bookmarks, 1,212,854 impressions
- **Importance:** Seminal article on AI agent architecture; ~1.2M views; referenced by YC Lightcone podcast, GitHub issues, startup ecosystem

## Retrieval Chain — Attempted in Order

### Attempt 1: xurl read (Tier 1) ✅ PARTIAL
```bash
xurl read 2053127519872614419
```
**Result:** Metadata only. Got title, author, engagement metrics. No body text. Confirmed it's an X Article (has `article.title` field).

### Attempt 2: web_extract on tweet URL (Tier 2) ✅ PARTIAL
```python
web_extract(urls=["https://x.com/garrytan/status/2053127519872614419"])
```
**Result:** ~5 paragraphs of preview text + metadata. Content truncated at ~5,000 chars. Got enough to understand the topic and extract some key quotes, but missing the majority of the article structure.

### Attempt 3: GetXAPI (Tier 3) ❌
```python
os.environ.get("GETXAPI_KEY", "")
```
**Result:** Key not set. `echo ${GETXAPI_KEY:-not set}` → `not set`. Skipped.

### Attempt 4: browser_navigate ❌
```python
browser_navigate(url="https://x.com/i/article/2052898104039657472")
```
**Result:** Chrome not installed. `agent-browser install` needed but not available in session context.

### Attempt 5: web_extract on article URL ❌
```python
web_extract(urls=["https://x.com/i/article/2052898104039657472"])
```
**Result:** Cookie wall — only returned "Accept cookies" prompt. Zero article content.

### Attempt 6: xcancel.com (nitter) ❌
```python
web_extract(urls=["https://xcancel.com/garrytan/status/2053127519872614419"])
```
**Result:** `http_error`. Nitter instance down or blocked.

### Attempt 7: web_search → secondary source (Tier 4) ✅
```python
web_search(query='Garry Tan "Meta-Meta-Prompting" AI Agents 2026', limit=3)
```
**Results found:**
1. **abmedia.io** — Chinese crypto/AI news outlet. Published comprehensive summary with all key concepts, quotes, architecture details, and the "Fat Skills, Fat Code, Thin Harness" framework in detail (~5,000 chars in Chinese).
2. **startuphub.ai** — English summary of Garry Tan's AI agent approach (less detailed).
3. **github.com/ruvnet/ruflo/issues/1887** — GitHub issue referencing the article, defining key vocabulary ("Thin Harness, Fat Skills", "Tokenmaxxing", "400 engineers / 1 person").

### Attempt 8: web_extract on ABMedia ✅
```python
web_extract(urls=["https://abmedia.io/garry-tan-meta-meta-prompting"])
```
**Result:** Full comprehensive summary. Article structure:
- YC CEO's thesis: future belongs to compound AI systems
- Book Mirror process (Buddhist book → personal mapping → 30K-word brain page in 40 minutes)
- Fat Skills, Fat Code, Thin Harness architecture
- Multi-model strategy (Claude Opus 4.7, GPT-5.5, DeepSeek V4-Pro, Groq+Llama, OpenClaw+Hermes Agent)
- Skillify meta-skill
- 100+ skills, ~100K pages knowledge base
- Compound effect philosophy

## Result

Successfully created:
- **Raw article:** `wiki/raw/articles/2026-05-09_garrytan_meta-meta-prompting.md` — with `getxapi: false`, `source_fallback: secondary`, `summary_source: https://abmedia.io/...`
- **Concept page:** `wiki/concepts/meta-meta-prompting.md` — full concept with architecture diagram, multi-model table, Hermes Agent mapping
- **Entity page:** `wiki/entities/garry-tan.md` — comprehensive person page with career timeline, G Stack, AI builder philosophy

## Key Takeaway

When an X Article is high-profile enough (YC CEO, 1.2M impressions), secondary coverage exists. The search query `"<exact title>" <author>` almost always finds at least one comprehensive summary. Chinese tech media (ABMedia, 鏈新聞, etc.) often produce the most detailed English-language summaries of Silicon Valley AI content due to their translation workflow — they must fully understand and restructure the content to translate it, resulting in high-fidelity summaries.
