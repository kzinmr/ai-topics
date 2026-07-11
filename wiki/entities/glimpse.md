---
title: Glimpse
created: 2026-05-29
updated: 2026-05-29
type: entity
tags: [tool, macos, webview, terminal, developer-tooling, open-source]
sources: [raw/articles/2026-03-13_michaellivs_reverse-engineering-claude-generative-ui.md]
---

# Glimpse

**Glimpse** (npm: `glimpseui`) is a native **macOS micro-UI library** that opens WKWebView windows from Node.js/TypeScript applications. Created by Daniel Griesser, it provides a lightweight bridge between terminal-based applications and full browser rendering engines.

## Key Capabilities

- **Native WKWebView** — full browser engine (CSS, JavaScript, Canvas, CDN libraries) in a native macOS window
- **Sub-50ms startup** — feels instant; no Electron, no runtime dependencies
- **Bidirectional JSON** — `window.glimpse.send(data)` sends data from the WebView back to Node.js
- **Window modes** — floating, frameless, transparent, click-through, follow-cursor
- **`setHTML()`** — replace page content at runtime
- **`send(js)`** — evaluate JavaScript in the WebView from Node.js

## Use Case: Generative UI for Terminal Agents

Glimpse was used by [[entities/michael-lively|Michael Lively]] to recreate [[entities/anthropic|Anthropic]]'s [[concepts/generative-ui|generative UI]] system for **pi**, a terminal-based coding agent. The challenge: terminals can't render interactive HTML/JS. Glimpse solves this by spawning a native WKWebView window in <50ms with bidirectional JSON communication, letting the terminal agent open interactive widgets (charts, sliders, diagrams) while staying in the terminal workflow.

The integration uses:
1. `open(wrapHTML(html), {width, height, title})` to spawn the window
2. `win.setHTML()` / `win.send(js)` for progressive streaming updates (DOM diffing via morphdom)
3. `win.on("message", data)` to receive user interaction data back
4. `win.on("closed")` to detect window dismissal

## Architecture

Glimpse consists of a **tiny Swift binary** with a **Node.js wrapper**. The Swift binary handles WKWebView lifecycle; the Node.js wrapper exposes a clean API for spawning windows, sending messages, and receiving events.

```
pi extension (TypeScript)
  │
  ├─ import('glimpseui')
  ├─ open(html, options) → Window
  ├─ window.setHTML(html)     // replace content
  ├─ window.send(js)           // eval JS in WebView
  ├─ window.on("message", cb)  // receive data from page
  └─ window.on("closed", cb)   // handle dismissal
```

## Related

- [[concepts/generative-ui|Generative UI (Claude Visualizer)]] — the system Glimpse helped recreate for terminal agents
- [[entities/michael-lively|Michael Lively]] — developer who used Glimpse for the pi generative UI extension
- [[entities/anthropic|Anthropic]] — whose Claude generative UI inspired the terminal reimplementation
- npm: [glimpseui](https://www.npmjs.com/package/glimpseui)
