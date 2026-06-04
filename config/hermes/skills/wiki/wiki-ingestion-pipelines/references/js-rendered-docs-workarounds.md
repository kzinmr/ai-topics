# JS-Rendered Documentation Workarounds

## Problem
Modern documentation sites built with Next.js, Remix, or other SSR frameworks may serve full content on the landing page but return empty/placeholder content on sub-pages when scraped with `web_extract()`. The content is loaded client-side via JavaScript.

## Detection
- `web_extract(url)` returns only the site title + nav + footer, no main content body
- `curl -s url | grep -c 'next'` shows Next.js scripts
- Page works in a real browser but `web_extract` gets nothing

## Primary Solution: Companion GitHub Repo

Many documentation sites, especially:

- **Educational courses** (Braintrust Evals 101, fast.ai, FullStackOpen)
- **Tool documentation** (LangChain, DSPy cookbooks, Instructor)
- **Newsletter archives** (Substack `/archive`, Beehiiv)
- **Blog series**

...link to a companion GitHub repo containing the full course materials as markdown files, READMEs, and source code.

### Workflow

1. **Check the main page footer/header** for "View on GitHub", "Star on GitHub", or similar badges/links. The main landing page (which SSR'd fine) usually has this link.

2. **Extract the GitHub URL** from the main page content:
   - "GitHub Repository" button in the page
   - `github.com/{org}/{repo}` in links
   - The raw HTML may have `href="https://github.com/..."` even when web_extract strips it

3. **Clone the repo** (shallow clone is sufficient):
   ```bash
   cd /tmp && git clone --depth 1 https://github.com/{org}/{repo}.git
   ```

4. **Find markdown content** — the module directories often contain README.md files with the full lesson content:
   ```bash
   find /tmp/{repo} -name '*.md' -not -path '*/.git/*' | sort
   ```

5. **Read all module READMEs** — each module's README.md typically contains:
   - Module title and learning objectives
   - Setup instructions
   - Step-by-step walkthrough
   - Key technical details and lesson takeaways

6. **Extract source code** — the accompanying Python/JS files contain the actual implementation patterns with concrete APIs, parameters, and settings:
   ```bash
   find /tmp/{repo} -name '*.py' -o -name '*.js' -o -name '*.ts' | sort
   ```

7. **Read key source files** — focus on task definitions, scorer configurations, and experiment runners. The source code often reveals:
   - Concrete API signatures (e.g., `LLMClassifier(name=..., choice_scores=..., use_cot=True)`)
   - Parameter patterns (e.g., `trial_count=3`, `temperature=0`, `max_concurrency=1`)
   - Dataset structure (e.g., CSV format with 16 edge-case inputs)
   - Scorer prompt templates with the actual rubric text

## Fallback: Web Search for Mirrors

If no GitHub repo exists:

1. **Search for the article title + "2026"** (or current year)
2. **Check archive.org** for the URL
3. **Look for cross-posts** — authors often publish the same content on Substack, personal blogs, dev.to, etc.
4. **Use `browser_navigate`** if Chromium is available (falls back to JS rendering)

## Example: Braintrust Evals 101 Course

- Main page: SSR worked → full content extracted
- Sub-pages (`/foundations/datasets`, `/foundations/scorers`, etc.): JS-rendered → empty
- Solution: Found `https://github.com/braintrustdata/eval-101-course` in the main page footer
- Cloned repo → extracted 8 module directories with READMEs + source code
- Result: Full course structure (14 modules), concrete code examples (LLMClassifier with choice_scores, trial_count=3, temperature=0), and the critical Improvement Loop lesson

## Pitfalls

- **Not all repos have READMEs per module** — check for Jupyter notebooks (.ipynb) as an alternative
- **The repo may have fewer modules than the course** — the online version may have additional video content or interactive demos not in the repo
- **READMEs may be minimal** — the actual substance may be in code comments or Python docstrings
- **Commit history is rarely useful** — the repo may be a single commit containing all materials at once
- **Don't confuse the tool's product docs repo with the course repo** — Braintrust has both `braintrustdata/braintrust-sdk` (API docs) and `braintrustdata/eval-101-course` (course materials)
- **Don't spend time trying to fix web_extract on JS sites** — the JS-rendered pages won't render in a headless curl/wget/extract. The GitHub repo is the path of least resistance.
