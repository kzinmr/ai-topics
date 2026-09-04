# Zero-Take Backlog Archive — Pattern-E with 0 pages (validated 2026-08-30)

Session shape: `dreaming-collect` pre-run reported `ok:true` but an EMPTY candidate
pool (`payload.articles: 0`) while the on-disk backlog held 195 recent raw articles
and 2983 existing wiki pages. The injected cron prompt summary ALSO disagreed
(`collected_articles: 0, existing_wiki_pages_count: 0`) — a lossy reporting-shape
mismatch, not the truth. The real checkpoint at
`/opt/data/.hermes/cron/data/dreaming/latest.json` is authoritative.

Outcome: 70 recent never-archived articles triaged, **0 pages created / 0 updated**
(the one high-value AI story — Dwarkesh's OpenAI→HuggingFace agent-civilization
sandbox-escape narrative — was already fully documented in
`concepts/ai-agent-safety-incidents.md`). Archived all 70 + logged saturation.

## Step-by-step (cron-safe: no pipes / no heredoc / no Unicode in `python3 -c`)

### 1. Read the checkpoint at the RIGHT key
```python
import json
p = json.load(open("/opt/data/.hermes/cron/data/dreaming/latest.json"))
payload = p["payload"]            # NOT p["articles"]
arts = payload.get("articles", [])          # [] here
print(payload.get("recent_raw_articles"),   # 195 — the real backlog
      payload.get("existing_wiki_pages"))   # 2983
```
Probe field shapes before `len()` — some count fields are ints, some lists:
```python
print({k:(type(v).__name__, len(v) if isinstance(v,(list,str)) else v)
       for k,v in payload.items()})
```

### 2. Never-archived set = filesystem recent files ∩ NOT-in-umbrella-index
The DECISIVE dedup source is the UMBRELLA `wiki/raw/archived/triage/archive_index.json`
with shape `{"urls": [<2804 normalized URL strings>], "updated": ...}`. `urls` is a
plain `list[str]` of NORMALIZED URLs — not file paths, not dicts. Child
`triage/dreaming/archive_index.json` is `{"urls":[<file paths>], "last_updated":...}`
— a different shape; do NOT confuse them (this confusion cost several probe calls).
```python
import json, re, glob, os
def norm(u):
    if not u: return ""
    u = re.sub(r'https?://','',u.strip()); u = re.sub(r'^www\.','',u)
    u = u.split('#')[0]; u = re.sub(r'/utm_.*','',u)
    return u.lower().rstrip('/')
umb = set(norm(x) for x in json.load(
    open("wiki/raw/archived/triage/archive_index.json"))["urls"])
files = sorted(glob.glob("wiki/raw/articles/*.md"),
               key=os.path.getmtime, reverse=True)
cands = []
for fp in files[:70]:                       # cap the scan; recent window
    txt = open(fp,encoding="utf-8",errors="ignore").read()[:4000]
    fm = re.match(r'^---\n(.*?)\n---', txt, re.S)
    if not fm: continue
    m = re.search(r'^url:\s*"?(\S+?)"?\s*$', fm.group(1), re.M)
    url = m.group(1).strip('"').strip("'") if m else ""
    if url and norm(url) not in umb:
        cands.append((fp,url))
```

### 3. Classify each candidate (only read the AI-relevant ones fully)
- Read frontmatter + first ~30 lines of every candidate; batch-grep the AI ones
  against `wiki/concepts/ wiki/entities/` for their specific claims.
- Non-AI (LWN releases, dfarq retro-computing, political X posts) → skip, no deep read.
- The Dwarkesh OpenAI/HF story: grep its distinctive facts
  (`Artifactory`, `ExploitGym`, `pte_physroot`, `Astra critical`, `agent message board`)
  in `concepts/ai-agent-safety-incidents.md` → all present → ✅ already-covered,
  record line numbers for the report table.

### 4. Archive with the CANONICAL script (not shutil.move)
```bash
cd ~/ai-topics && python3 scripts/archive_triage.py dreaming --keep-reference
```
It is idempotent and URL-keyed. If you hand-rolled a move, REVERT it — the script
owns the dated JSON + index bookkeeping (Pitfall #22 merge behavior).

### 5. Log the zero-take saturation + selective-stage commit
Log entry MUST carry the ✅ already-covered verification table (candidate, status,
line refs) and note the upstream collect-pipeline 0-article break. Then:
```bash
git add wiki/log.md wiki/raw/archived/triage/dreaming/YYYY-MM-DD_*.json \
        wiki/raw/archived/triage/archive_index.json
git commit -m "wiki: dreaming weekly scan YYYY-MM-DD (N triaged, 0 pages; ...)"
git push origin main     # skip pull --rebase on a dirty sibling tree
```

## Reportable observations
- Flag the `dreaming-collect → dreaming-group` empty-pool break (0 articles vs 195
  backlog) as an upstream pipeline bug — the weekly scan only worked because it fell
  back to a direct filesystem backlog scan. Mirrors the `blog-triage` chain break.
- A correct candidate-list verdict does NOT cover the sitemap backlog — the two are
  disjoint; the archive-index absence probe is mandatory even when the checkpoint
  and any upstream table both claim saturation.
