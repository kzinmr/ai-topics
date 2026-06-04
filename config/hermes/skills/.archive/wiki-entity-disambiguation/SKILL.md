---
name: wiki-entity-disambiguation
category: wiki
description: Detect and resolve name collisions where two different real-world entities share the same slug — migrate content to disambiguated slugs, rewrite originals, update all cross-references.
---

# Wiki Entity Disambiguation

Resolve name collisions where two different people/entities share the same slug in `~/ai-topics/wiki/entities/`. This is the **inverse** of dedup — instead of merging same-entity-under-different-names, you split **different-entities-under-the-same-name**.

## When This Skill Activates

Use when:
- Ingesting an article and the author's name matches an existing entity page, but they are a **different person** (e.g., "Tim Sh" the AI-coder vs "Tim Sherratt" the digital historian)
- Discovering an entity page conflates content about two different people
- A blog URL or X handle maps to a different person than the existing entity page
- A namesake collision is detected during triage or enrichment
- A user asks to add someone whose name collides with an existing entry

## Detection

### Before creating any entity page
```bash
# Search for partial/alias matches to detect potential collisions
search_files "tim-sh" path=~/wiki/entities target=files
search_files "tim sh" path=~/wiki target=content file_glob="*.md"
```

### Telltale signs of a collision:
1. **URL mismatch**: The article's domain (timsh.org) doesn't match what the existing page covers
2. **Topic mismatch**: Existing page covers GLAM/historical work; incoming article covers AI/ML
3. **Bio contradictions**: Different education, profession, or employer
4. **No cross-links**: Existing page doesn't link to other entities the article mentions (indicating different communities)
5. **Author field in article** references a different full name than the existing page

## Resolution Procedure

### Step 1: Confirm it's a collision, not the same person
Read the incoming article and the existing entity page. Compare:
- Professional domain (AI coder vs historian — different)
- Employer/affiliation
- Social media handles
- Publication context

If ANY of these conflict and there's no plausible connection, treat as a collision.

### Step 2: Choose disambiguated slugs
- **Occupant of the original slug**: The one most relevant to the wiki's focus (AI/agents/LLMs). They keep the short, natural slug.
- **Migrated entity**: Gets a more specific slug (e.g., `tim-sh` → `tim-sherratt` for the historian).

Priority rule: AI/agent/LLM relevance > historical relevance. The wiki is "AI Topics" — the AI person keeps the primary slug.

### Step 3: Create migrated entity page
```bash
# Copy content from old slug to new, more specific slug
cd ~/ai-topics/wiki/entities/
cp tim-sh.md tim-sherratt.md
```
Then edit `tim-sherratt.md` to:
- Remove any content that was actually about the incoming article's entity
- Update frontmatter title to the full disambiguated name
- Add `aliases: [tim-sh]` to capture the old slug
- Add explicit clarification note at top: "Not to be confused with [[tim-sh]] (AI coder, timsh.org)"

### Step 4: Rewrite the original slug for the incoming entity
Edit `tim-sh.md` (or whatever the original slug is):
- Strip ALL content belonging to the migrated entity
- Write fresh content based on the incoming article(s)
- Add clarification note: "Not to be confused with [[tim-sherratt]] (digital historian)"
- Update all frontmatter fields

### Step 5: Update cross-references across the wiki
```bash
# Find all wikilinks to the slug that changed meaning
cd ~/ai-topics
grep -rl '\[\[tim-sh\]\]' wiki/ --include='*.md'
# Review each — does it refer to the AI person (keep) or the historian (update to [[tim-sherratt]])?
```

Update:
- **`index.md`**: Update the original entry's description; add the new disambiguated entry
- **`SCHEMA.md`**: No changes needed unless new tags are required
- **All entity/concept pages** that linked to the old slug — update links that point to the migrated entity
- **`log.md`**: Log the disambiguation with all files created/updated

### Step 6: Update raw article sources
Check if any raw articles in `~/wiki/raw/articles/` were originally filed under the old entity. Update any metadata references that could confuse future processing.

### Step 7: Commit
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: disambiguate <slug> → <migrated-slug> (<reason>)" && git push
```

## Example: tim-sh vs tim-sherratt

| Dimension | Original (`tim-sh`) | Incoming Article | Decision |
|-----------|-------------------|-------------------|----------|
| Domain | Digital humanities, GLAM | AI coding, PM | Collision confirmed |
| Full name | Tim Sherratt | Tim Sh | Different people |
| Website | timsherratt.org | timsh.org | Different domains |
| AI relevance | Low (marginal) | High (primary) | AI person keeps slug |

**Result:**
- `tim-sh.md` → Rewritten for Tim Sh (timsh.org, AI coder)
- `tim-sherratt.md` → New page migrated from old content
- All wikilinks audited and updated

## Prevention

1. **Before creating a new entity page**, always search for existing pages by partial name match:
   ```bash
   search_files "sh" path=~/wiki/entities target=files limit=50
   ```
2. **Check the blog domain, not just the author name** — timsh.org is different from timsherratt.org
3. **When in doubt, verify the person** — search their bio, X profile, or GitHub
4. **Add clarification notes** to both entities (`Not to be confused with [[other-entity]]`) even if no collision is currently active — this prevents future conflation

## Relationship to wiki-entity-dedup

| | Dedup | Disambiguation |
|---|---|---|
| **Problem** | Same entity, multiple slugs | Different entities, same slug |
| **Action** | Merge → delete duplicate | Split → migrate one entity |
| **Result** | Fewer pages | Same number or +1 page |
| **Detection** | High text/content similarity | Contradictory bio/domain/topics |

## Pitfalls

- **Don't assume** the existing page is wrong — verify both identities independently
- **Don't forget** to check `SCHEMA.md` if new tags are needed for the new entity
- **Don't leave orphan wikilinks** — always grep for `[[old-slug]]` after rewriting
- **Don't conflate disambiguation with dedup** — if content genuinely overlaps, it's a merge, not a split. Assess carefully.
- **Log the decision** with the reasoning so future sessions understand why the slug was reassigned
