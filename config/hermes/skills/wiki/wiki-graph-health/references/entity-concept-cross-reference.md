# Entity/Concept Duplicate Cross-Referencing

Procedure for resolving entity/concept pairs that share the same slug but serve different purposes.

## When to Apply

When wiki-graph-analysis or wiki-health reports pages existing in BOTH `entities/` and `concepts/` with the same basename (e.g., `entities/autoreason.md` + `concepts/autoreason.md`).

These are NOT always true duplicates — entity pages document people/orgs/products, while concept pages document ideas/analysis. Both can validly coexist.

## Decision Matrix

| Condition | Action |
|-----------|--------|
| Partner is skeleton stub (<500 chars) | Replace stub with redirect to richer page |
| Both comparable (>500 chars, <70% word overlap) | Add cross-links: `## See Also` on each pointing to the other |
| Near-duplicate (>70% word overlap) | Merge unique content, redirect thinner to richer |

## Redirect Format

```markdown
---
title: "Page Name (redirect)"
type: concept
status: redirect
redirect: entities/<slug>
created: 2026-01-01
updated: 2026-05-08
---

# Page Name

> **Redirect**: This page has been merged into [[entities/<slug>]].
```

## Cross-Link Format

For entity pages, add to the end:
```markdown
## See Also

- [[concepts/<slug>]] — Analysis and discussion of this topic
```

For concept pages, add to the end:
```markdown
## See Also

- [[entities/<slug>]] — Organization/person/product details
```

## Batch Script

```python
import os, re

wiki = "/opt/data/ai-topics/wiki"
pairs = ["autoreason", "claude-design", "claude-perfect-memory", ...]

for slug in pairs:
    e_path = os.path.join(wiki, 'entities', slug + '.md')
    c_path = os.path.join(wiki, 'concepts', slug + '.md')
    
    for path, other_type, other_slug in [(e_path, 'concepts', slug), (c_path, 'entities', slug)]:
        if not os.path.exists(path): continue
        with open(path) as f: content = f.read()
        
        link_text = f"[[{other_type}/{other_slug}]]"
        if link_text in content: continue  # already linked
        
        see_also = re.search(r'^## (?:See Also|Related(?: Pages)?)', content, re.MULTILINE)
        if see_also:
            insert_pos = content.find('\n', see_also.end()) + 1
            new_content = content[:insert_pos] + f"- {link_text}\n" + content[insert_pos:]
        else:
            new_content = content.rstrip() + f"\n\n## See Also\n\n- {link_text}\n"
        
        if new_content != content:
            with open(path, 'w') as f: f.write(new_content)
```

## 2026-05-08 Session Results

17 pairs found, resolved as:
- **3 redirects**: `ramp` (concept: 240B stub → entities), `the-silicon-underground` (concept: 316B stub → entities), `thinking-machines-lab` (concept: 308B stub → entities)
- **14 cross-linked**: `autoreason`, `claude-design`, `claude-perfect-memory`, `coding-agents`, `company-ai-pilled`, `content-engine`, `dspy`, `gemini`, `gpt-5.5`, `mac-studio-local-ai`, `openclaw`, `reflexive-ai`, `solo-founder-stack`, `telegram-managed-bots`

## Pitfalls

- **Don't assume same slug = same content**: `entities/dspy.md` and `concepts/dspy.md` had 6,312B vs 4,856B with different content — they're complementary, not duplicates
- **Check word overlap, not just size**: `company-ai-pilled` had nearly identical sizes (2,842B vs 2,837B) but only 7.9% word overlap — genuinely different perspectives
- **Prefer entity as canonical for orgs/products**: When one is a redirect, redirect concept→entity for people/orgs, concept as canonical for pure topics
- **Remove from index.md if redirecting**: Redirected stubs should NOT remain in index.md (they're navigation dead-ends). The batch script above handles file-level changes; clean up index.md separately.
