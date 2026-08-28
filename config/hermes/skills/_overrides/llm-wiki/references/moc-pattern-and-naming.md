# Map of Content (MOC) Pattern & Hub Concept Naming

## MOC Pattern — Session Reference (2026-06-08)

**Context:** Investigation of Baudrillard/Simulacra-related discourse across wiki revealed 1 central concept page, 14 related concept pages, 7 raw articles, and 1 blog article — forming a dense thematic cluster.

**What was created:** `concepts/baudrillard-moc.md` (later renamed to `representation-collapse-moc.md`) — a navigational hub organizing the cluster into 5 thematic groups:

1. Philosophical Framework (the hub + source articles)
2. Hyperreality Cluster (signs detaching from referents)
3. Map-and-Territory Cluster (models preceding reality)
4. Illusion Cluster (copies without originals)
5. Counter-Strategies Cluster (attempts to ground the simulacrum)

Each cluster has a table: `| Page | Conceptual Mechanism | Summary |`

**Structure:**
```yaml
---
type: concept
tags: [concept, philosophy, knowledge-management, ...]  # include knowledge-management
related:
  - "[[concepts/hub-page]]"
  - "[[concepts/related-1]]"
  - "[[concepts/related-2]]"
  # ... list ALL pages in the cluster
---
```

Body sections:
1. Intro quote + description of the MOC's scope
2. The Philosophical Framework (hub page + source articles table)
3. Thematic clusters (numbered, each with page table)
4. Entity pages with relevant perspectives
5. Cross-cutting connections to other wiki themes

## Hub Concept Naming — The "Phenomenon, Not Philosopher" Rule

**Problem:** Named `concepts/baudrillard-and-ai.md` — opaque to anyone unfamiliar with Baudrillard.

**User feedback:** "baudrillardとして代表すると彼を知らない人にとってぼやけるのです" (Representing it as "Baudrillard" is blurry for people who don't know him).

**Solution:** Renamed to `representation-collapse.md` — the actual phenomenon described.

**Generalizable principle:** When creating concept pages that apply an existing thinker's framework:
- Title: describe the phenomenon (`Representation Collapse`)
- Subtitle: scope it (`When Models, Maps, and Proxies Replace Reality`)
- Aliases: keep the thinker's name as alias (`baudrillard-and-ai`)
- Description: mention the framework as background, not identity

This makes the concept discoverable by *what it is*, not *who theorized it*. Someone searching for "proxy metrics broken" or "map replaces territory" will find `representation-collapse` but would never find `baudrillard-and-ai`.

**Rename process (when needed):**
1. `git mv` the file
2. Update title, aliases (keep old name as alias), description in frontmatter
3. Update all `[[wikilink]]` references across wiki (grep for old slug)
4. Update `index.md` entries
5. Append to `log.md` with rationale
6. `git add` + `git commit` + `git push`

## Git History File Recovery

When a file appears "missing," check git history before reporting it deleted:

```bash
# Find commits that touched the file
git log --all --oneline -- "path/to/file.md"

# Find deletion commits specifically
git log --all --oneline --diff-filter=D -- "path/to/file.md"

# Restore content from a specific commit
git show <commit>:path/to/file.md

# If no deletion commit exists, the file may be in a different directory
# (e.g., blog/ vs wiki/blog/)
```

**Session example:** Blog article `blog/2026-05-11_hermes_simulacrum-of-intellectual-consumption.md` was reported as "missing" but actually existed at the top-level `blog/` directory, not under `wiki/`. No deletion commit existed because the file was never deleted.
