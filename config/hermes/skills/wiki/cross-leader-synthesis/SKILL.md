---
name: cross-leader-synthesis
description: Synthesize perspectives from multiple opinion leaders on a shared topic into a cross-referenced wiki index page. Use when the user wants to consolidate different viewpoints on the same concept.
category: wiki
version: 1.0.0
metadata:
  hermes:
    tags: [wiki, synthesis, opinion-leaders, cross-reference]
    homepage: https://github.com/kzinmr/ai-topics
---

# Cross-Leader Synthesis

## Purpose
When multiple opinion leaders discuss the same topic (e.g., Agentic Engineering, AI Evaluation), consolidate their perspectives into a single **synthesis index page** that maps convergences, divergences, and unresolved questions.

## When to Use
- User asks to "集約" (aggregate) different leaders' views on a topic
- Multiple wiki pages exist for the same concept from different sources
- The topic is emerging and has no single authoritative source
- Building a cross-reference hub for a subdirectory of concept pages

## Workflow

### 1. Identify the Theme and Leaders
```bash
# Search wiki for pages on the topic
search_files "<theme>" path="~/wiki/" target="content"
# Check entity pages for related opinion leaders
```

### 2. Extract Per-Leader Perspectives
For each leader's entity page or concept pages:
- Core philosophy/stance on the topic
- Named frameworks or patterns they've coined
- Direct quotes (>30% for L3 quality)
- Practical examples or implementations
- Sources and dates

### 3. Build Synthesis Structure
Create `<theme>/_index.md` with:
- **リーダー別コンセプト一覧** — table mapping each leader to their key concepts
- **テーマ別議論** — group by sub-themes (e.g., evaluation, cognitive load, autonomy)
- **収束点** — what everyone agrees on
- **対立点** — where opinions diverge
- **未解決課題** — open questions across all leaders
- **概念マップ** — ASCII/mermaid diagram showing relationships
- **関連ページ** — links to deeper concept pages

### 4. Cross-Reference
Every synthesis page must:
- Link to each leader's entity page via `[[wikilinks]]`
- Link to related concept pages in the subdirectory
- Be linked FROM each concept page back to the synthesis index
- Be added to `wiki/index.md` under the appropriate section
- Be logged in `wiki/log.md`

### 5. Update Navigation
- Add `_index.md` to the top of the subdirectory as the entry point
- Update parent concept page (if exists) to link to the synthesis index
- Run lint check: no orphan pages, all wikilinks resolve

## Template Structure
```markdown
---
title: "Topic Name — Cross-Leader Synthesis"
aliases: [topic-index, topic-synthesis]
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [concept, index, topic-name]
status: draft
---

# Topic Name — 主要オピニオンリーダーの視点統合

## リーダー別主要コンセプト
| リーダー | コアコンセプト | 関連ページ |
|---------|--------------|-----------|
| [[person-a]] | ... | ... |

## 主要テーマ別議論
### 🧪 Theme 1
- **Person A**: [summary](link.md)
- **Person B**: [summary](link.md)
- **共通教訓**: "..."

## 議論の収束点
### ✅ 全員が同意していること
1. ...
2. ...

### ⚡ 意見が分かれる領域
1. ...

### 🔍 未解決の課題
- ...

## 概念マップ
(ASCII/mermaid diagram)

## 更新履歴
| 日付 | 変更内容 |
```

## Pitfalls
- **Don't create synthesis without substantive content** — each leader needs actual sourced perspectives, not just names
- **Don't claim consensus without evidence** — only list convergences that are directly stated by multiple leaders
- **Don't paraphrase quotes** — use exact wording with source URLs for L3 quality
- **Always update index.md and log.md** — synthesis pages are navigational hubs
- **Frontmatter must include `status: draft`** until all leader perspectives are filled in
- **Subdirectory convention** — place `_index.md` at the root of the concept subdirectory (e.g., `concepts/agentic-engineering/_index.md`)