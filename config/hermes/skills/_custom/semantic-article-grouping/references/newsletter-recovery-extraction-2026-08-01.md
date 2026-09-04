# Newsletter-Wiki-Ingest Recovery & Extraction Patterns (2026-08-01)

Validated 2026-08-01 during a newsletter-wiki-ingest run that recovered from a
triage render failure. Three durable lessons:

## 1. Archive dedup on checkpoint recovery is a SUCCESS signal, not an error

When the upstream triage agent's render fails but `triage_latest.json` survives,
run `archive_triage.py newsletter --keep-reference` during ingest. Expected
output when triage already archived before failing to render:

```json
{"newsletter": {"ok": true, "message": "All items already archived (dedup)", "archived": 0}}
```

This is the **success path** — the triage agent completed archiving (section 8 of
SKILL.md) before the render failure. Do NOT re-run, re-archive, or treat
`archived: 0` as a failure. Just verify exit and proceed to enrichment.

## 2. read.getsuperintel.com (beehiiv uid=443): NO `<article>` tag — use full-HTML `<p>` extraction

The Superintel+ canonical post domain resolves 200 (~830KB HTML) but is
Next.js/beehiiv-rendered and contains **no `<article>` tag** — the standard
`<article>` extraction path returns nothing. JSON-LD gives `headline`,
`datePublished`, `description` only (no `body_html`).

Working extraction (cron-safe: write script to /tmp, run via terminal):

```python
import subprocess, re, json
html = subprocess.run(
    ["curl", "-sL", "-A", "Mozilla/5.0 ...Chrome/126.0...", url],
    capture_output=True, text=True, timeout=25).stdout
# metadata
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL):
    try:
        data = json.loads(m)
        if isinstance(data, dict) and data.get('headline'):
            print(data.get('headline'), data.get('datePublished'))
    except json.JSONDecodeError:
        pass
# body: extract ALL <p> tags from full HTML (no <article> wrapper)
paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
texts = [re.sub(r'<[^>]+>', '', p).strip() for p in paras]
texts = [t for t in texts if t]
```

2026-08-01 result: 69 paragraphs extracted from the "DeepSeek Answered OpenAI's
Price Cut Overnight" post — full pricing-war content (Luna -80% to $0.20/$1.20,
V4-Flash $0.14/$0.28, Opus 4.8 comparison, SB 942 timeline).

Distinct from Substack: no `<article>` boundary, so filter nav/footer chrome
manually (first ~10 paragraphs are site chrome: Search/Home/Tags/About links).

## 3. Wikilink targets are NOT validated by pre-commit hooks — verify before commit

The ai-topics pre-commit hooks validate `index.md` structure and tag taxonomy
ONLY. A new page can reference a non-existent `[[concepts/foo]]` and commit
cleanly. After creating/enriching pages, verify every wikilink target exists:

```bash
for f in concepts/screen-recording.md concepts/computer-use.md; do
  [ -f "wiki/$f" ] && echo "OK $f" || echo "MISSING $f"
done
```

2026-08-01: `[[concepts/screen-recording]]` was referenced from the new
prompt-engineering page but the file does not exist — caught by this check and
reworded to plain text before commit. Subagents often add speculative wikilinks;
verify their link targets too (e.g. a subagent linked
`[[concepts/multi-agents/agent-team-swarm]]` — that path DID exist under
`concepts/multi-agents/`, but check rather than assume).

## 4. Sibling-process races during the 07:40-07:50 parallel window

- `wiki/index.md` is shared with blog-wiki-ingest (07:50) — expect
  `_warning: ...modified by sibling subagent` on patch. The patch still applies
  cleanly to current state; re-grep your line after patching to confirm.
- `/tmp/fetch_*.py` scripts collide with sibling agents — use unique filenames
  with the run date (`/tmp/ainews_fetch_20260801.py`), and re-read before running
  if a sibling-modification warning fires.
- Unstaged non-wiki changes (skill drift files) make `git pull --rebase` fail
  with "unstaged changes", but `git push` still succeeds — commit only your
  `wiki/` files with a targeted `git add wiki/`.
