# Paper Deep-Enrichment Pattern

## When to Use

When a paper's arXiv URL is already listed as a source in an existing entity page, but:
- The page has only a **high-level summary** (2-4 bullet points) rather than the paper's full theoretical and experimental depth
- No raw paper file exists in `wiki/raw/papers/`
- The paper introduces or formalizes **named concepts** that deserve their own concept pages (e.g., drowning-in-documents paradox)
- The user says "この論文をwikiに取り込んで" and the paper is "already there" but shallowly

**Do NOT skip** just because the entity page exists. The user is asking for deep ingestion, not existence check.

## Workflow

### Step 1: Dedup + Save Raw Paper
```bash
python3 scripts/papers_index.py --check <arxiv-url>
```
If DUPLICATE → update existing raw file. Otherwise:
1. Save full paper content to `wiki/raw/papers/YYYY-MM-DD_arxiv-id_short-title.md`
2. Register: `python3 scripts/papers_index.py --add <file> <url>`

### Step 2: Read Existing Entity Page
Read the current entity page end-to-end. Identify:
- What's already covered (briefly)
- What's missing: theoretical bounds, experimental tables, formal definitions, mathematical derivations
- What named concepts within the paper deserve separate concept pages

### Step 3: Extract Full Paper Content
Prefer `web_extract` on PDF URL first (arxiv.org/pdf/ID). If truncated or HTML-only, try `web_extract` on abs page. Key content to extract:
- Theoretical bounds and propositions
- Experiment result tables
- Formal definitions (goodness metrics, paradox formulations)
- Comparative claims (single-vector vs multi-vector)

### Step 4: Enrich Entity Page (Comprehensive Rewrite)
Replace the high-level summary with a deep treatment:
- Add the theoretical bounds with proof sketches
- Add experiment tables
- Add formal definitions
- Add a comparative summary table (single vs multi vector, or equivalent)
- Expand related concepts and cross-references
- Bump `updated` date, add raw paper to `sources`

### Step 5: Create Derived Concept Pages
For each **named concept/paradox** the paper formalizes:
1. Search for dangling wikilinks: `grep -rn 'concepts/<proposed-slug>' wiki/ --include='*.md' -l`
2. Check SCHEMA.md for needed tags; add if missing
3. Create the concept page with:
   - Intellectual genealogy (trace the concept through prior literature)
   - Formal definition from the paper
   - Why it matters (implications for the field)
   - Connection to existing wiki knowledge
   - Mitigations/alternatives if applicable

### Step 6: Cross-Link
Update related pages (minimum 2) to reference the new concept pages. Update Related Concepts/Pagess sections and frontmatter `related:` fields.

### Step 7: Index, Log, Commit
Standard commit workflow. Watch for sibling subagent interference — after `write_file`, verify with `git status` that files weren't already committed by a parallel process.

## Example Session

**Paper**: arXiv:2603.29519 "On Strengths and Limitations of Single-Vector Embeddings"
**Existing entity**: `entities/embeddings.md` (4 bullet points, no raw paper)
**What was added**:
- Raw paper: `raw/papers/2026-03-31_2603.29519_single-vector-embeddings-limitations.md`
- Entity enrichment: 67→123 lines (Observation 2.3/2.4, Proposition 2.5, Atomic LIMIT table, G metric, toy model, 6-dimension comparison table)
- New concept: `concepts/drowning-in-documents-paradox.md` (intellectual genealogy, G metric, √n vs √log n scaling, mitigations)
- Cross-links: `concepts/colbert.md` (Why ColBERT section + related), `concepts/modern-retrieval-toolkit.md` (Related Concepts)
- Tag: `drowning-in-documents` added to SCHEMA.md Techniques

## Pitfall: Sibling Subagent Commits

`write_file` creates files visible to parallel subagents. After writing key files:
```bash
git status <file-path>
```
If "nothing to commit, working tree clean" → file already committed by sibling. Check `git log --oneline -3` to find which commit. If bundled into an unrelated commit (e.g., "Palantir research infrastructure"), the content is correct but the commit message is misleading. Note this in your log.md entry but don't rewrite history.
