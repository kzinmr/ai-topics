# Concept Cluster Overview Pattern

## When to Apply

When a domain has **6+ related concept pages** scattered across `concepts/` with overlapping themes but no central navigation hub, create a **concept cluster overview page** (親ページ). This is superior to per-page cross-referencing because:
- Single source of truth for the topic cluster
- Prevents editing 6+ pages individually
- Reader can grasp the full landscape in one page
- Identifies stubs, duplicates, and reading gaps

## Template Structure

### Frontmatter
```yaml
title: "<Domain> Overview — 概念クラスターマップ"
type: concept
aliases: [<domain>-overview, <domain>-cluster]
tags: [<domain-tag>, ai-agents, harness-engineering, ...]
status: active
```

### Body Sections

1. **Intro paragraph** — What the domain is, why it matters, what this page does
2. **ASCII cluster map** — Visual representation of layers and their relationships
3. **Layer breakdown** — One section per layer with:
   - Layer description (what this layer covers)
   - Table of pages (| Page | Focus | Source |)
   - **関係 paragraph** — How pages within this layer relate to each other, AND how this layer relates to adjacent layers
4. **Cross-cutting topics** — Themes that span multiple layers (distribution, marketplace, governance)
5. **Stub inventory** — Pages marked `status: stub` with notes on where real content lives
6. **Reading paths** — 初心者向け / 実践者向け / アーキテクト向け
7. **See Also** — Links to broader concepts the domain sits under

### 4-Layer Classification Pattern

This is the standard layering that emerged from the Agent Skills cluster and generalizes:

| Layer | Label | Question | Example |
|-------|-------|----------|---------|
| **1** | Format & Standard | "What IS it?" — file format, metadata, discovery | SKILL.md format, YAML frontmatter |
| **2** | Design Philosophy | "HOW should it be designed?" — principles, governance | 10 Design Principles, Self-Authored vs Governed |
| **3** | Implementation & Architecture | "HOW is it implemented?" — platform-specific patterns | Claude Code Skills, Skill Graph, LLM-as-Judge |
| **4** | Research & Scaling | "HOW does it scale?" — academic/empirical studies | SRA-Bench, Incorporation Bottleneck |

Not all clusters have all 4 layers. Minimum viable: Layers 2+3. Add Layer 1 if there's a format standard. Add Layer 4 if there's academic research.

## Post-Creation Steps

After creating the overview page:
1. **Add back-links** from all key pages to the overview (See Also / Related Concepts section)
2. **Handle stub duplicates** — pages that are just `status: stub` with no real content should be converted to redirects pointing at the canonical page
3. **Update index.md** — add the overview page, placed alphabetically within its section
4. **Update log.md** — log the new overview, all back-link pages, and any stub redirects

## Pitfalls

- **Don't move pages into subdirectories** — adding `concepts/skills/` breaks existing wikilinks. Keep the overview flat in `concepts/` and link to existing flat paths.
- **Don't create the overview for clusters of 2-3 pages** — just add cross-links. The threshold is ~6+ pages where the reader can't find the entry point.
- **Keep the overview concise** — it's a map, not a replacement for individual pages. Target ~150 lines, not 400.
- **The ASCII cluster map is high-value** — it's the first thing a reader sees and gives instant orientation. Spend time making it clear.
- **Relationship paragraphs are the differentiator** — a list of pages is just index.md. The overview adds value by explaining HOW pages relate to each other across and within layers.
