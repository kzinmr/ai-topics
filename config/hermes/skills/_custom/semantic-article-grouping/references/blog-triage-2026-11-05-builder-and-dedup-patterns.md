# Builder-script crashes + coverage-check shortcuts (blog triage, Nov 2026)

Learned in run `20261105T100028Z` (blog-triage, 20 candidates → 7 take / 5 reference / 8 skip).

## 1. `d()`/`make()` helper: `raw_path=None` TypeError for `unsaved_articles`

Regular candidates and `unsaved_articles` need different argument handling, but a single shared
dict-builder helper usually assumes both. Passing `f=None` (unsaved item, no raw file) raises
**after** most of the decisions array is already built:

```
TypeError: can only concatenate str (not "NoneType") to str
  line 22: "raw_path": "~/ai-topics/wiki/raw/articles/" + f
```

This is the same family as the documented `stars=None` TypeError (`can't multiply sequence by
non-int of type 'NoneType'`). Both are helper-argument bugs that are legal for regular candidates
and illegal for unsaved ones — and both surface only at *runtime*, not at lint.

**Guard every `f`-dependent expression in the helper, not just the star count:**

```python
def d(item_id, title, url, f, action, stars, reason, cwp=None):
    return {
        "item_id": item_id, "source": "blog", "source_name": SRC[item_id],
        "title": title, "url": url,
        "raw_path": ("~/ai-topics/wiki/raw/articles/" + f) if f else None,
        "recommended_action": action,
        "reason_ja": ("★" * stars) + " " + reason,      # int, never None
        "candidate_wiki_path": cwp,
        "body_excerpt": read_raw(f) if f else "（unsaved_articles — 抽出不可）",
    }
```

**Three-stage gate for cron builder scripts** (each catches what the others miss):
1. `python3 -c "import ast;ast.parse(open('/tmp/x.py').read())"` → CJK quote/ternary syntax errors
2. `python3 /tmp/x.py` → None-arithmetic, NameError (`null` vs `None`), missing-dict-key
3. `python3 -c "import json; d=json.load(open(P)); print(...)"` with hardcoded path → downstream
   parse safety + field completeness
   (`missing = [x["item_id"] for x in d["decisions"] if not x["body_excerpt"] or not x["reason_ja"]]`)

Stage 2 is the one that gets skipped when you trust the lint result — `write_file`'s lint reported
`ok` for the script that then crashed at stage 2.

## 2. Fast archive-index dedup probe (better than log.md grep alone)

`wiki/raw/archived/triage/archive_index.json` is a flat URL collection (~3,000 entries as of
Nov 2026) covering every previously triaged skip/reference. Probing it is a cheaper and more
complete dedup signal than grepping log.md, because log.md only records *takes* and pipeline
events, not prior skips.

```python
import json
d = json.load(open('/opt/data/ai-topics/wiki/raw/archived/triage/archive_index.json'))
urls = d if isinstance(d, list) else list(d.get('urls', d))
for t in ['pierre', 'thousand-fewer', 'polymorphic', 'genius-scan']:
    print(t, [u for u in urls if t in u][:2])
```

Handle both shapes (bare list vs `{"urls": ...}`) — the loader has appeared in both forms.

Interpretation: **0 hits = genuinely novel**, so a take isn't a re-triage. Nonzero hits that are
*different URLs on the same topic* (e.g. `datasette-apps` matched 3 prior entries at
`simonwillison.net/2026/Aug/1/...` plus a Substack post) still allow a take for the new article —
compare specific URLs, don't just check topic presence.

## 3. `scrape_status: "rss-fallback"` frontmatter = thin-body signal (openai.com)

`openai.com` returns **403 to the scraper UA**, so sitemap-monitor falls back to RSS descriptions.
These raw files are ~600 B and carry a marker in frontmatter:

```yaml
scrape_status: "rss-fallback — openai.com returns 403 to scraper UA; body = RSS description only"
```

Triage guidance that differs from the general paywall section:
- **Still valid takes** — the RSS description of an official announcement usually contains the
  concrete new fact (a new product brand name, a count like "948 privilege-escalation
  vulnerabilities", a distribution channel like "AWS GovCloud via Amazon Bedrock"). That single
  sentence is enough to prove a coverage gap against an entity page.
- **Do NOT re-fetch openai.com** in the triage job (403 again, wasted call). Flag downstream to
  corroborate via HN/X instead.
- **Unverified-entity caveat**: an acquisition whose target is unknown from the RSS line (e.g.
  "acquire Pierre Computer Company, Inc.") must be written with explicit confidence qualification
  (`confidence: medium`, target identity unverified). Don't let downstream invent the target.
- Dedup caveat: prior Daybreak-related URLs may already be archived
  (`openai.com/index/daybreak-securing-the-world/`) while the *new* brand
  (`index/daybreak-red-aws-govcloud`) is not. Probe by full slug, not by initiative name.

## 4. Release-cluster batch take for the same entity page

When one author/source posts several same-day release notes that all land on **one** entity page
(Simon Willison: `datasette-agent 0.5a0` + `datasette-apps 0.3a0` + `datasette-llm 0.1a10`), split
by body substance rather than batching all identically:
- releases with new capability + concrete API/permission detail → **take** (0.5a0 `panel`,
  0.3a0 `app_add_stored_queries()` / write-query approval gate)
- pure bugfix notices → **reference** (0.1a10 model-allowlist fix; llm 0.37.1 "bugfix release")

Always check where the page's release history actually *stops* — this one was frozen at 0.1a4 +
0.1a9 despite `updated: 2026-11-01`. A recent `updated:` date does not mean recent releases are
recorded. Tell downstream to batch same-page items into one `patch` to avoid edit races.

## 5. Same-event ≠ same-role pair (implementation vs paradigm declaration)

Two articles from one company on one topic can both be takes with *different* destinations:
Together AI's `Together Compiler (TKCC)` (implementation + benchmark numbers) →
`entities/together-ai.md`, while `Polymorphic Inference` (paradigm framing, market data, and a
self-reversal of the lab's own prior megakernel position) → new `concepts/polymorphic-inference.md`.
Cross-wikilink them; don't merge. The self-reversal case must be recorded as contested/superseded
with date + source, never as a silent rewrite of the older claim.

## 6. SKILL.md size ceiling — route new learnings to references/

`semantic-article-grouping/SKILL.md` is at the 100,000-char hard limit (101,472 chars as of
2026-11-05). `skill_manage(action='patch')` on SKILL.md **fails outright** with
`SKILL.md content is 101,472 characters (limit: 100,000)`. All new learnings for this skill must
go into `references/*.md`; a SKILL.md pointer line is only possible if space is freed elsewhere.
Don't burn a turn attempting a SKILL.md patch — write the reference first.
