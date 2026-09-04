## arXiv Paper Ingestion via Jina Reader

For academic papers, prefer `arxiv.org/html/` (experimental HTML version) over the abstract page or PDF. Combined with Jina Reader, this gives clean full-text markdown in a single call:

```bash
# Get abstract page (titles, authors, metadata)
curl -sL "https://r.jina.ai/https://arxiv.org/abs/2502.05364"

# Get full paper text (HTML version — much richer than abstract)
curl -sL "https://r.jina.ai/https://arxiv.org/html/2502.05364v2"
```

**Output can be large** (80-120K chars for full papers). Use `head -N` for initial scan, then `wc -c` to check total size, and fetch remaining sections if needed:

```bash
curl -sL "https://r.jina.ai/https://arxiv.org/html/2502.05364v2" > /tmp/paper_full.txt
wc -c /tmp/paper_full.txt          # check size
sed -n '100,250p' /tmp/paper_full.txt  # read specific sections
```

**Metadata extraction from abstract page HTML** (authors, dates, venue, DOI) — grep for `<meta name="citation_*">` tags:

```bash
curl -sL "https://arxiv.org/abs/2502.05364" | grep 'citation_'
```

**Version suffix**: Use `v2` (latest) in the HTML URL. The abstract page always redirects to latest.

**Workflow**: (1) Fetch abstract page → extract metadata, (2) Fetch HTML version → save raw article, (3) Create concept page from full text, (4) Update index.md + log.md, (5) Check SCHEMA.md tags exist before writing frontmatter.

**Tag validation pitfall**: Before committing, grep SCHEMA.md for every tag in your frontmatter. Technology-specific names like `cuda`, `triton`, `cudnn` are NOT in the taxonomy — use broader canonical tags (`gpu`, `hardware`) and put specificity in the page body. See `references/tag-taxonomy-pitfalls.md` for the full mapping table.
