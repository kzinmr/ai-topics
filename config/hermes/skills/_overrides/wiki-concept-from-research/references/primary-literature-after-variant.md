# Primary Literature Ingestion After Variant Page Exists

## When This Happens

A variant/specialized concept page already exists in the wiki (e.g., `multi-teacher-on-policy-distillation.md`) that **aliases** the foundational concept name. The variant page has `aliases: [OPD, On-Policy Distillation]` in its frontmatter. Then the user provides the **primary literature** — the original paper/blog post that defined the foundational concept (e.g., Thinking Machines' Oct 2025 OPD article).

This is the **reverse** of the normal flow (normally the foundational page is created first, then variants branch off).

## Detection

When scanning for existing coverage (Step 1), pay special attention to pages that **alias** the concept you're about to create. If `search_files` finds `aliases: [<your-concept-name>]` on an existing page, you have this pattern.

## Workflow

### 1. Create the foundational concept page
- Use the **exact slug** that existing dangling wikilinks expect (`grep -rn 'concepts/<slug>' wiki/`)
- This page should be authoritative — grounded in the primary literature
- Include the full mechanism, experimental results, and intellectual lineage from the primary source

### 2. Differentiate from the variant in the foundational page
Add a **distinction table** comparing the foundational concept vs the variant:

```markdown
## Distinction from <Variant Name>

| Aspect | OPD (Foundational) | MOPD (Variant) |
|--------|-------------------|----------------|
| **Introduced** | Oct 2025 | May 2026 |
| **Teachers** | Single teacher | Multiple teachers |
| **Primary Use** | Post-training efficiency, continual learning | Capability consolidation across domains |
...
```

### 3. Add disambiguation note to the variant page
Add a note at the **top** of the variant page (after the title, before the body):

```markdown
> **Note**: This page covers the <variant description>. For the foundational single-teacher technique introduced by <Author/Org> in <Date>, see [[concepts/<foundational-slug>]].
```

### 4. Enrich the author/org entity page
Add the publication to the entity's "Publications & Research" section with DOI, abstract summary, and wikilink back to the new concept page.

### 5. Keep the variant's aliases
Do NOT remove "OPD" or "On-Policy Distillation" from the variant's `aliases:` — aliases serve as search aids. The disambiguation note handles navigation.

## Example: OPD → MOPD

- **Variant existed first**: `concepts/multi-teacher-on-policy-distillation.md` with `aliases: [OPD, On-Policy Distillation]`
- **Primary literature arrived**: Thinking Machines "On-Policy Distillation" (Oct 2025, DOI: 10.64434/tml.20251026)
- **Dangling wikilinks found**: `entities/nrehiew.md` and `concepts/post-training-distributional-view.md` already linked to `[[concepts/on-policy-distillation]]`
- **Created**: `concepts/on-policy-distillation.md` with distinction table vs MOPD
- **Updated**: MOPD page with disambiguation note, TML entity with publication entry
