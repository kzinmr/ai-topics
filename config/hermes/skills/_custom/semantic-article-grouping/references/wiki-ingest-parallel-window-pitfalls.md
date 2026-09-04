# Wiki-Ingest Parallel-Window Pitfalls (newsletter vs blog wiki-ingest, 07:40/07:50 UTC)

Validated 2026-08-06 during a newsletter-wiki-ingest run that ran in the same window as blog-wiki-ingest.

## 1. index.md sibling-modification race

Both newsletter-wiki-ingest (07:40) and blog-wiki-ingest (07:50) edit `wiki/index.md` in the same
window. Symptom: `patch` on index.md returns:

```
_warning: /opt/data/ai-topics/wiki/index.md was modified by sibling subagent '<id>'
but this agent never read it. Read the file before writing to avoid overwriting the sibling's changes.
```

This is expected, not a conflict — the patch usually applies cleanly against current content.

**Working procedure**:
1. Before patching, `grep -n "<anchor>" wiki/index.md` (e.g., the neighboring index line, or the
   `## Entities (N pages)` header) to confirm the anchor still exists and get exact line numbers.
2. Apply the patch.
3. Verify: grep again for your line, and confirm the section header count reflects YOUR +1.
   If the sibling also bumped the same header, both increments should be preserved (878→879 was
   correct here even though blog-wiki-ingest was mid-flight).

If the anchor moved (sibling inserted a line above your target), re-locate before patching —
never patch on a stale assumption.

## 2. Targeted git add when siblings have unstaged changes

During the parallel window, `git status` shows many unrelated changes left by sibling subagents
(e.g., deleted/modified `config/hermes/skills/_custom/*/SKILL.md` files). Do NOT blanket
`git add -A` or `git add wiki/` — that sweeps sibling in-flight work into your commit.

**Working procedure**: stage only your own paths explicitly:

```bash
git add wiki/entities/discovery-loop.md wiki/entities/jeff-dean.md wiki/index.md wiki/log.md \
        wiki/raw/newsletters/2026-08-06-*.md wiki/raw/inbox/newsletter-ingest/*.json
```

Validated 2026-08-06: targeted add of 10 own files committed cleanly (tag validation passed,
6 files checked) while 20+ sibling skill-file changes stayed unstaged. The `git pull --rebase`
step may then fail with "cannot pull with rebase: You have unstaged changes" — that is the
siblings' changes, not yours; push your commit directly (push succeeded, `d0bf8ff2..1d2f4814`).

## 3. Embedded-tweet full_text extraction from Substack HTML

When a newsletter post quotes an X/Twitter post (e.g., Jeff Dean's Discovery Loop announcement),
the Substack post page embeds the tweet as JSON. You can extract the EXACT quote text without
touching xurl:

```bash
curl -sL --max-time 20 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" \
  "https://www.latent.space/p/ainews-jeff-sanjay-oriol-and-quoc" -o /tmp/post.html
```

Then in Python, find the tweet payload and pull `full_text` (HTML entities are escaped — use
`html.unescape` or the JSON field directly):

```python
import re, json, html
raw = open('/tmp/post.html', encoding='utf-8', errors='ignore').read()
# Find the tweet object containing the full_text
idx = raw.find('Announcing Discovery Loop')
chunk = raw[max(0, idx-100):idx+1500]
text = re.sub(r'<[^>]+>', '', chunk)
# Or: the JSON-LD block + <script type="application/ld+json"> gives headline/datePublished/description
```

Key facts recovered this way (2026-08-06):
- `"url":"https://x.com/JeffDean/status/2085034604172603724"` — canonical tweet URL for the
  entity page `sources` frontmatter
- `"date":"2026-08-05T16:06:02.000Z"` — tweet timestamp
- `"full_text":"Announcing Discovery Loop! ... a Public Benefit Corporation whose mission is to
  automate machine research"` — exact quote, no truncation, beats paraphrasing from the digest

This is strictly better than copying the newsletter digest's 2-3 sentence summary: the post page
gives the primary-source quote, tweet URL, and timestamp in one curl. Use it when an entity page
needs a verbatim founder announcement.

## 4. archive_triage.py dedup outcome at ingest time

When the triage agent already ran archiving before its render failure (triage JSON saved to
checkpoint + archive written at 10:36), running `archive_triage.py newsletter --keep-reference`
at ingest time reports:

```json
{"ok": true, "message": "All items already archived (dedup)", "archived": 0}
```

This is a benign success — the skip/reference items are already persisted. No action needed;
do not re-run or treat it as a failure.
