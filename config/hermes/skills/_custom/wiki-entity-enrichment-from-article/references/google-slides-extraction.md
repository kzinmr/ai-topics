# Google Slides Content Extraction

## Problem
User shares a Google Slides URL (e.g., `https://docs.google.com/presentation/d/<ID>/edit`). Need to extract slide text content for wiki ingestion.

## Method: Export as Plain Text

Google Slides supports direct export via URL:

```bash
curl -sL "https://docs.google.com/presentation/d/<SLIDE_ID>/export?format=txt" > /tmp/slides_raw.txt
```

### How it works
- `/export?format=txt` returns plain text of all slides concatenated
- Each slide's content is separated by blank lines
- Speaker notes, if any, are included inline
- No authentication required for public slides

### Extraction pattern (execute_code)

```python
from hermes_tools import terminal, read_file

# Extract
result = terminal("curl -sL 'https://docs.google.com/presentation/d/<ID>/export?format=txt' > /tmp/slides_raw.txt")
raw = read_file("/tmp/slides_raw.txt")
# Process raw['content'] into structured wiki page
```

### Pitfalls
- **Private slides fail silently**: Returns empty or redirect HTML. Check `wc -l` on output to verify content was extracted.
- **Emoji/unicode**: Slide text exports may contain emoji (😀, 🤖, 🚶). Strip or preserve depending on context.
- **Format is bare text**: No slide boundaries, no formatting. Treat as continuous text and manually identify section breaks.
- **Rate limiting**: Bulk extraction of many slides may hit rate limits. Add delays between requests.
- **Alternative formats**: `format=pdf` returns a PDF, `format=pptx` returns the original. `format=txt` is simplest for wiki ingestion.

## After extraction

Follow the standard wiki ingestion workflow:
1. Save raw text as `~/wiki/raw/articles/YYYY-MM-DD_<source>_<slug>.md` with YAML frontmatter
2. Analyze content for new concepts vs. updates to existing pages
3. Create concept/entity pages as needed
4. Cross-reference with existing pages (check index.md, agent-steering.md, etc.)
5. Update index.md + log.md
6. Commit + push
