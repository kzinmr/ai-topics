# Wiki Entity Disambiguation

Resolve name collisions where two different people/entities share the same slug. Inverse of dedup — split different-entities-under-the-same-name.

## When This Activates
- Ingesting an article and the author's name matches an existing entity page but they are a different person
- Discovering an entity page conflates content about two different people
- A blog URL or X handle maps to a different person

## Detection
```bash
search_files "partial-name" path=~/wiki/entities target=files
search_files "full name" path=~/wiki target=content file_glob="*.md"
```
Telltale signs: URL mismatch, topic mismatch, bio contradictions, no cross-links.

## Resolution Procedure
1. Confirm it's a collision (not same person)
2. Choose disambiguated slugs (AI-relevant person keeps the natural slug)
3. Create migrated entity page: `cp old-slug.md new-slug.md`, add clarification note
4. Rewrite the original slug for the incoming entity
5. Update cross-references: `grep -rl '\[\[old-slug\]\]' wiki/`
6. Update raw article sources
7. Commit

## Example: tim-sh vs tim-sherratt
| Dimension | Original (`tim-sh`) | Incoming Article | Decision |
|-----------|-------------------|-------------------|----------|
| Domain | Digital humanities | AI coding | Collision |
| Full name | Tim Sherratt | Tim Sh | Different |
| AI relevance | Low | High | AI keeps slug |

## Relationship to Dedup
| | Dedup | Disambiguation |
|---|---|---|
| Problem | Same entity, multiple slugs | Different entities, same slug |
| Action | Merge → delete | Split → migrate one |
| Result | Fewer pages | Same number or +1 |
