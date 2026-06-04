# papers_index.py Workflow

Full pipeline for adding a new paper to the wiki. Run from `~/ai-topics/`.

## Step 1: Determine Publication Date

```bash
# For arXiv papers:
curl -sL 'https://arxiv.org/abs/<arxiv-id>' | grep -oP '(?:Submitted|submitted).*?(?=<|$)' | head -1
# Example output: "Submitted on 22 May 2026"
```

Alternative: check the arxiv abstract page HTML for `<meta name="citation_date">` or parse from the URL path.

## Step 2: Check for Duplicates

```bash
python3 scripts/papers_index.py --check <arxiv-id-or-url>
# OK: No duplicate found         → proceed
# DUPLICATE: <existing-filename>  → update existing file instead
```

## Step 3: Save Raw Paper

Filename: `wiki/raw/papers/{YYYY-MM-DD}_{arxiv-id}_{short-title}.md`

- `arxiv-id` = without version suffix (e.g., `2512.24601`, NOT `2512.24601v2`)
- `short-title` = 2-5 hyphenated keywords, lowercase, 40 chars max
- Frontmatter fields: `arxiv_id`, `title`, `authors`, `affiliation`, `submitted`, `code` (if any), `source`, `type: paper`, `tags`

## Step 4: Register in Index

```bash
python3 scripts/papers_index.py --add "<filename>" "<arxiv-url>"
# Example: python3 scripts/papers_index.py --add "2026-05-22_2605.24220_polar-agent-rl-harness.md" "https://arxiv.org/abs/2605.24220"
```

## Step 5: Create Entity/Concept Page (if warranted)

Apply the page threshold rule from SCHEMA.md: create when the entity/concept appears in 2+ sources or is central to one source.

## Step 6: Update wiki/index.md and wiki/log.md

- Add entity to index under correct section
- Bump counts: Total pages, Indexed entries, section count
- Append to log.md with paper details and entity links

## Step 7: Commit and Push

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ingest <title> paper" && git push
```

Pre-commit hooks auto-validate index.md and tag taxonomy.
