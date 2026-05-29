---
title: Michael Lively
created: 2026-05-29
updated: 2026-05-29
type: entity
tags: [person, blogger, reverse-engineering, terminal, generative-ui, anthropic, coding-agents, developer-tooling]
sources: [raw/articles/2026-03-13_michaellivs_reverse-engineering-claude-generative-ui.md]
---

# Michael Lively

Michael Lively (michaellivs.com) is a software engineer and blogger focused on **reverse-engineering AI products** and building **terminal-based developer tooling**. He is the creator of [[glimpse|Glimpse]]-based generative UI extensions for coding agents.

## Notable Work

### Reverse-Engineering Claude's Generative UI (March 2026)

Lively reverse-engineered [[anthropic|Anthropic]]'s `show_widget` generative UI system on claude.ai by interrogating [[claude-models|Claude]] about its own implementation. He extracted the complete design guidelines verbatim from browser devtools network payloads, mapped the module system (`diagram`, `mockup`, `interactive`, `chart`, `art`), and documented the streaming DOM injection architecture.

He then **recreated the system** for **pi**, a terminal-based coding agent, using [[glimpse|Glimpse]] (macOS WKWebView) and morphdom (DOM diffing) — achieving the same progressive streaming widget rendering in a native window launched from the terminal.

Key discoveries:
- Generative UI is a **tool call** (`show_widget`), not inline markdown
- The `read_me` pattern implements **progressive disclosure** for model instructions
- Rendering uses **direct DOM injection** (not iframes), streaming HTML as tokens arrive
- The "sandbox" is a Content Security Policy allowlisting four CDN domains
- Design guidelines are a production-grade system with hard rules on typography, colors, dark mode, and streaming structure

### Previous Work

Lively has also reverse-engineered Anthropic's **sandbox architecture** for Claude (referenced in the generative UI article).

## Writing Style

Lively's blog posts combine hands-on reverse engineering with working code implementations. His approach: interrogate the AI about its own internals, extract ground truth from network payloads, then build a working clone. The generative UI article includes the complete TypeScript extension code (~350 lines) and verbatim design guidelines extracted from claude.ai.

## Related

- [[generative-ui|Generative UI (Claude Visualizer)]] — concept page for the system Lively reverse-engineered
- [[glimpse|Glimpse]] — macOS WKWebView library he used for the terminal reimplementation
- [[anthropic|Anthropic]] — company behind Claude and the generative UI system
- Blog: [michaellivs.com](https://michaellivs.com)
