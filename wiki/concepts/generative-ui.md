---
title: Generative UI (Claude Visualizer)
created: 2026-05-29
updated: 2026-05-29
type: concept
tags:
  - developer-tooling
  - anthropic
  - streaming
  - progressive-disclosure
  - reverse-engineering
  - terminal
  - webview
  - agent-tooling
  - methodology
sources: [raw/articles/2026-03-13_michaellivs_reverse-engineering-claude-generative-ui.md]
---

# Generative UI (Claude Visualizer)

Anthropic's **generative UI** system (internally called "Visualizer" or "Imagine") is a mechanism that allows [[claude-models|Claude]] to render **interactive HTML widgets inline** in claude.ai conversations — sliders, charts, diagrams, mockups — as live DOM elements rather than static images or code blocks.

The system was introduced in March 2026. Michael Lively ([michaellivs.com](https://michaellivs.com)) reverse-engineered the implementation and recreated it for **pi**, a terminal-based coding agent, using Glimpse (macOS WKWebView windows).

## Architecture

### Tool Call, Not Markdown

The core insight: generative UI is **not** HTML embedded in markdown output. It's a **tool call** (`show_widget`) where the HTML is passed as a JSON parameter payload. This is the same mechanism as web search or file operations — just with HTML content.

```
show_widget parameters:
  i_have_seen_read_me: boolean   — guard; must call read_me first
  title: string                  — snake_case identifier
  loading_messages: string[]     — 1–4 short strings shown during render
  widget_code: string            — raw HTML fragment (no <html>/<head>/<body>)
```

### The `read_me` Pattern: Progressive Disclosure

Before using `show_widget`, Claude must call `visualize:read_me` with a `modules` parameter selecting from five modules: `diagram`, `mockup`, `interactive`, `chart`, `art`.

Each module returns **different design guidelines**. For example, `chart` returns Chart.js patterns; `art` returns SVG illustration rules; `mockup` returns UI component tokens. This is **progressive disclosure applied to the model's own instructions** — keeping the system prompt lean by loading specialized knowledge only when needed.

The base system prompt stays compact (~few thousand tokens). When Claude needs to render a chart, it loads the chart module (~22K tokens). When it needs to draw a diagram, it loads the diagram module (~59K tokens). The modules share a common core (philosophy, streaming rules, typography, CSS variables, `sendPrompt()` docs).

### Rendering: Direct DOM Injection, Not Iframe

The widget renders **live as tokens stream in** — evidence against iframe-based sandboxing (iframes require complete HTML before rendering). Instead, the client:

1. Receives `widget_code` as streaming JSON string chunks
2. **Incrementally parses** the partial HTML
3. Injects DOM nodes into the parent page in real-time
4. CSS variables resolve immediately (same document, same cascade)
5. `style` blocks and HTML structure render as they arrive
6. `script` tags execute only **after** streaming completes (which is why scripts go last)
7. CDN libraries load asynchronously; charts/interactivity activate when scripts run

The "sandbox" is effectively a **Content Security Policy** allowing `<script src>` only from: `cdnjs.cloudflare.com`, `cdn.jsdelivr.net`, `unpkg.com`, `esm.sh`.

### Streaming Architecture

```
LLM generates show_widget tool call
  │
  ├─ widget_code streams token by token as JSON string chunks
  ├─ Client incrementally parses partial HTML
  ├─ DOM nodes inserted in real-time (innerHTML or similar)
  ├─ CSS variables resolve immediately (same document)
  ├─ style blocks + HTML render as they arrive
  └─ script tags execute after streaming completes

Design guideline: "Structure code so useful content appears early:
 style (short) → content HTML → script last."
```

## Differences from Artifacts

| Dimension | [[anthropic|Anthropic]] Artifacts | Visualizer (`show_widget`) |
|-----------|--------------------|-----------------------------|
| **Purpose** | Deliverables (downloadable, persistent) | Inline conversational enhancements |
| **Display** | Side panel with download button | Inline in chat, transparent background |
| **Libraries** | Fixed set of pre-bundled libraries | Any library from CDN allowlist (live download) |
| **Persistence** | Survives across sessions | Ephemeral, tied to the message |
| **Trigger** | Deliverable language ("build me a calculator") | Explanatory language ("show me how this works") |

## Design Guidelines (Extracted)

The guidelines are a **production design system** with hard rules extracted verbatim from claude.ai's `read_me` tool responses:

### Core Rules
- **Streaming-first**: `style` → HTML → `script` last
- **No gradients, shadows, blur** — they flash during streaming DOM diffs
- **No HTML comments** — waste tokens, break streaming
- **Two font weights only** (400, 500) — never 600 or 700
- **Sentence case everywhere**, never Title Case or ALL CAPS
- **CSS variables** for all colors (`--color-text-primary`, `--color-background-secondary`)
- **Dark mode mandatory** — every color must work in both modes
- **CDN allowlist**: `cdnjs.cloudflare.com`, `cdn.jsdelivr.net`, `unpkg.com`, `esm.sh`

### Color Palette
Nine color ramps, each with 7 stops from lightest to darkest. Color encodes meaning, not sequence. 2-3 ramps per widget max. Text on colored backgrounds uses the 800/900 stop from the same ramp — never black.

### SVG Diagram Engineering
- ViewBox safety checklist (5 verification steps)
- Font width calibration table with actual rendered pixel measurements
- Pre-built CSS classes (`c-blue`, `c-teal`, `box`, `node`, `arr`)
- Arrow markers that auto-inherit stroke color via `context-stroke`
- `fill="none"` on connector paths (SVG defaults to `fill: black`)
- Decision framework: route on verb, not noun ("how do LLMs work" → Illustrative, "transformer architecture" → Structural)
- Complexity budgets: ≤5 words per subtitle, ≤4 boxes per horizontal tier

## Terminal Reimplementation: pi + Glimpse

Michael Lively recreated the system for **pi**, a terminal-based coding agent, using [[glimpse|Glimpse]] — a native macOS WKWebView library.

### Key Challenges & Solutions

1. **Terminals can't render HTML/JS** → Glimpse opens a native WKWebView window in <50ms with bidirectional JSON communication
2. **Streaming smoothness** → `innerHTML` on every token causes full-page flashes; naive node appending fails because partial HTML parsing creates unpredictable tree structures. Solution: **morphdom** — a DOM diffing library that compares old/new trees and applies minimal patches, animating only genuinely new nodes with fade-in CSS
3. **Loading race condition** → morphdom loads asynchronously from CDN; calls before load are silently buffered and flushed when ready
4. **Script execution** → `innerHTML` doesn't execute `<script>` tags; on completion, scripts are cloned into fresh elements (which browsers execute) replacing the inert originals
5. **String escaping** → HTML injected as JS string via `win.send()` requires escaping backslashes, single quotes, newlines, and closing `</script>` tags

### Two Tools, Mirroring Claude

- `visualize_read_me` — Lazy-loads design guidelines; LLM calls silently before first widget
- `show_widget` — Opens native macOS window via Glimpse, returns user interaction data

### pi-ai Streaming Normalization

Pi's AI layer normalizes streaming events across all providers into:
```
toolcall_start → toolcall_delta → toolcall_end
```
with progressively-parsed `arguments`. This means the streaming approach works identically for Anthropic, OpenAI, Google, or any provider — no partial JSON parser needed.

## Why This Matters

1. **Generative UI is simpler than it looks** — it's a tool call returning HTML, injected into the DOM with incremental parsing. The sophistication is in the design guidelines, not the rendering engine.
2. **The `read_me` pattern is reusable** — lazy-loading documentation into the model's context on demand reduces baseline token cost while giving access to deep specialized knowledge.
3. **DOM diffing is the key to smooth streaming** — partial HTML creates unpredictable tree structures; morphdom-style minimal patching with animation callbacks is the correct approach.
4. **Terminal agents can be visual** — spawning lightweight WebView windows bridges the terminal/browser gap without leaving the terminal workflow.

## Related

- [[anthropic|Anthropic]] — company behind Claude and generative UI
- [[claude-models|Claude Models]] — the LLM family powering the visualizer
- [[claude-code|Claude Code]] — Anthropic's coding agent with different UI paradigm
- [[glimpse|Glimpse]] — macOS WKWebView library enabling the terminal reimplementation
- Agent tool design patterns: [[progressive-disclosure]], [[streaming]]
