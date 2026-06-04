# Stub Detection, Separation, and Cross-Reference Pattern

## When This Applies

When the user asks to "separate X as a concept and cross-reference with related pages," and the wiki has stubs or thin pages for X or its subordinate techniques. Typical trigger phrase: 「〜はコンセプトとして分けて整理し、それぞれの技術を厚くして。関連する既存コンセプトとも横断分析してほしい」

## The Pattern (3-Step)

### Step 1: Detect Stubs and Plan the Hierarchy

Run `search_files` for the concept name and all related technique names. Check each page:
- **Stub**: <30 lines, status: stub, or TODO markers → needs full rewrite
- **Thin page**: Has some content but <100 lines → needs enrichment
- **Missing page**: No file exists → needs creation
- **Existing rich page**: Already substantial → may need minor cross-reference updates only

Map the hierarchy:
```
Canonical concept (test-time-scaling) ← CREATE
  ├── Sub-technique 1 (chain-of-thought) ← ENRICH from stub
  ├── Sub-technique 2 (rlvr) ← Already exists, minor cross-ref
  ├── Sub-technique 3 (grpo) ← Already exists, minor cross-ref
  └── Alias page (inference-time-scaling) ← REDIRECT to canonical
```

### Step 2: Create/Enrich in Order

1. **Create the canonical concept page first** — it defines the framework that subordinate pages link to
2. **Enrich subordinate technique pages** — each gets full treatment with historical context, variants, comparison tables, limitations
3. **Replace alias stubs with redirects** — when two terms are synonymous (test-time-scaling = inference-time-scaling), make the deprecated stub a clean redirect:
   ```markdown
   ---
   status: redirect
   redirect: <canonical-slug>
   ---
   > This page has been merged into **[[<canonical-slug>]]**.
   ```
   Do NOT delete the stub file — existing wikilinks from other pages reference it.

### Step 3: Cross-Reference All Related Pages

After creating/enriching the core pages, update all related pages that link to them:

1. **Update wikilinks**: `grep -rn '<old-slug>' wiki/ --include='*.md' -l` → patch each to use the canonical slug
2. **Update frontmatter `related:` fields**: Add the new canonical page to related pages' frontmatter
3. **Update internal references**: Pages that had inline references to the old alias page need link text updates
4. **Update index.md**: Add new entries, enrich thin descriptions for enriched pages

### Real Example: test-time-scaling + chain-of-thought

**Initial state**:
- `concepts/inference-time-scaling.md` — 24-line stub
- `concepts/chain-of-thought.md` — 24-line stub
- `concepts/scaling-hypothesis.md` — 407-line rich page, had `inference-time-scaling` in related/links
- No `concepts/test-time-scaling.md`

**Actions**:
1. Created `concepts/test-time-scaling.md` (14KB, 250+ lines) — 7 techniques, compute-optimal allocation, cross-comparisons
2. Rewrote `concepts/chain-of-thought.md` (5.5KB, 130+ lines) — emergent property, 5 variants, comparison table
3. Redirected `concepts/inference-time-scaling.md` → test-time-scaling
4. Updated `concepts/scaling-hypothesis.md`: `inference-time-scaling` → `test-time-scaling` in `related:` and inline link
5. Updated `index.md`: added test-time-scaling entry, enriched chain-of-thought entry

**Key insight**: The alias page (inference-time-scaling) was NOT deleted because `scaling-hypothesis.md` had a wikilink to it. The redirect preserves those links while guiding readers to the canonical page.

## Pitfalls

- **Don't delete alias stubs**: Other pages wikilink to them. Use redirects instead.
- **Check for dangling wikilinks first**: `grep -rn 'concepts/<proposed-slug>' wiki/ --include='*.md' -l`. If wikilinks exist to your new canonical slug, create the page with that exact slug — you're fulfilling existing navigation promises.
- **Create canonical before subordinates**: The subordinate pages wikilink to the canonical. If you create them first, you'll need to go back and add the links.
- **Don't forget index.md for EACH page**: Every new or significantly enriched page needs its index entry created or updated.
- **Use `patch` with enough context for log.md**: The log.md file has many identical trailing lines ("- `~/wiki/log.md` — updated"). Include 2-3 lines of unique preceding context in `old_string` to avoid "Found N matches" errors.
