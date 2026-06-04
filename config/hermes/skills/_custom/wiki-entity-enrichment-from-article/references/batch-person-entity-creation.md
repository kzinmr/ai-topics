# Batch Person Entity Page Creation from X Handles

When creating multiple person entity pages from a list of X/Twitter handles (e.g., for cross-linking
to a company entity page), use this pattern for efficient parallel research and creation.

## Workflow

### 0. CHECK FOR EXISTING PAGES (MANDATORY — BEFORE ANY WRITES)

**This is the most important step. Skipping it causes catastrophic data loss: user pages are 100-200+ lines of detailed content, and `write_file` silently overwrites them.**

Before creating any entity page, check ALL of the following:

1. **search_files** for the slug in the entities directory:
   ```python
   # Check for exact slug match AND partial matches
   search_files(path="/opt/data/wiki/entities", pattern="will-brown")
   search_files(path="/opt/data/wiki/entities", pattern="Will Brown")
   ```

2. **grep index.md** for the entity name:
   ```bash
   grep -i "entity-name" /opt/data/wiki/index.md
   ```

3. **If page exists**: DO NOT use `write_file`. Use `patch` to add ONLY the new cross-links/sections. Read the existing page first to understand its structure, then make targeted edits.

4. **If page does NOT exist**: Proceed to creation. Use `write_file` only for genuinely new pages.

> ⚠️ **Catastrophic failure**: On 2026-05-13, three 140-203 line entity pages (Will Brown, Florian Brand, Elie Bakouch) were overwritten with 43-70 line stubs because this check was skipped. Had to git-restore from `dd724453`. Never skip this step.

Use `execute_code` with `terminal()` to batch-fetch X profiles via xurl:

```python
from hermes_tools import terminal

handles = ["vincentweisser", "willccbb", "xeophon", "eliebakouch", "Grad62304977"]
results = {}

for h in handles:
    r = terminal(f"/opt/data/bin/xurl user @{h}", timeout=15)
    results[h] = json.loads(r["output"]) if r["exit_code"] == 0 else None
```

Key profile fields: `name`, `description`, `public_metrics` (followers, following, tweet_count),
`created_at`, `profile_image_url`, `verified`, `id`.

**Pitfall**: The name field may be a display name (e.g., "elie", "Grad"), not the full legal name.
Cross-reference with LinkedIn, personal websites, and web search for the full name.

### 2. Web Research (Parallel Per Person)

For each person, search:
- `"Full Name" prime intellect role`
- Their personal website (often linked in the X bio or discoverable via web search)
- LinkedIn profile
- GitHub profile
- Podcast appearances (Latent Space, etc.)

```python
from hermes_tools import web_search, web_extract

for person in people:
    r = web_search(f"{person['name']} {person.get('role_hint','')} prime intellect", limit=3)
    # Extract relevant pages
    urls = [item['url'] for item in r['data']['web']]
    content = web_extract(urls)
```

### 3. Entity Page Template

Use this template for person entity pages:

```yaml
---
title: "Full Name"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [person, relevant-tags, x-account]
sources:
  - https://x.com/handle
  - https://personal-website.com
---

# Full Name

One-line role summary at [[parent-company]].

## Bio

| Fact | Detail |
|------|--------|
| **Role** | Title, Company |
| **X/Twitter** | [@handle](https://x.com/handle) (XK followers) |
| **Website** | [domain.com](https://domain.com) |
| **Education** | University, Year (if known) |
| **Previous** | Previous Company (if notable) |

## Research Focus / Key Work

- Key project 1
- Key project 2

## Media

- Podcast appearances, notable talks

## Related Pages

- [[parent-company]] — company page
- [[colleague-1]]
- [[colleague-2]]
- [[relevant-concept]]
```

### 4. Parallel Page Creation

Create all entity pages in **one batch** using parallel `write_file` calls:

```python
# All pages created simultaneously — no dependency between them
write_file(path="entities/vincent-weisser.md", content=vincent_page)
write_file(path="entities/will-brown.md", content=will_page)
# ... etc.
```

### 5. Cross-Link to Parent Entity

Update the parent company entity page to link all new people:
- Replace bare name list in "Key People" section with `[[wikilinks]]`
- Add all people to "Related Pages" section
- Use `patch` to do targeted replacements

### 6. Update index.md (Batch Insertion)

For multiple entity page insertions into `index.md`:

1. Process slugs in **reverse alphabetical order** (Z→A) to keep earlier line numbers stable
2. For each slug, find the line number of the first existing entity whose slug is alphabetically AFTER it
3. Use `sed -i 'N i\...'` to insert before that line
4. Re-read the file after each insertion to get updated line numbers

```python
for slug in sorted(new_slugs, reverse=True):
    # Find insertion point
    with open(index_path) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        existing = line.split("[[entities/")[1].split("]]")[0] if "[[entities/" in line else ""
        if existing > slug:
            insert_at = i + 1  # 1-indexed for sed
            break
    subprocess.run(["sed", "-i", f"{insert_at}i{entry_text}", index_path])
```

### 7. Tag Taxonomy Check

Before committing, scan new pages' tags against `SCHEMA.md`. Common new tags for people:
- `researcher` — add to **People/Orgs** category if not present
- `pseudonymous` — add to **People/Orgs** category if not present

Add missing tags to SCHEMA.md first, then `git add wiki/SCHEMA.md` before committing.

### 8. x-accounts.yaml

Add any new X handles to `config/feeds/x-accounts.yaml` for tracking:
```bash
echo "- handle" >> config/feeds/x-accounts.yaml
```

Check for duplicates first — many handles may already be tracked.

## Pitfalls

- **⚠️ OVERWRITING EXISTING PAGES (CRITICAL)**: The #1 mistake. Always run Step 0 (search_files + grep index.md) before ANY write_file. User entity pages are frequently 100-200+ lines of detailed research. `write_file` silently destroys them. If a page exists, use `patch` for targeted additions only. (Example: Will Brown 203 lines → 70 line stub, had to git-restore from `dd724453`.)
- **Pseudonymous accounts**: Handles like "Grad62304977" may have no description or personal website.
  Search their tweets for context clues (RTs of the company, technical discussions).
- **Display name ≠ full name**: "elie" → Elie Bakouch, "Grad" → unknown. Web search is essential.
- **Tag violations on commit**: The pre-commit hook catches unknown tags. Add `researcher` and
  `pseudonymous` to SCHEMA.md proactively when creating person pages.
- **SCHEMA.md patch fuzzy matching**: When adding tags to long comma-separated category lines
  via `patch`, fuzzy matching can place a tag in the WRONG category (e.g., `llm-proxy` landed
  in Engineering AND Infrastructure). **Always re-read the patched area immediately** and check
  for misplaced or duplicated tags. Fix duplicates before creating any pages that use those tags.
- **sed insertion order**: Always reverse alphabetical. Forward order causes line number drift
  and misplacements.
- **xurl timeout**: Set timeout=15s. The `/2/users/by/username/` endpoint is fast; the
  `user` subcommand includes public_metrics.
