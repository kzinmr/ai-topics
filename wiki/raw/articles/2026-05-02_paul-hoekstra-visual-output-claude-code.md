# Visual Output with Claude Code: Beyond Claude Design

**Author:** Paul Hoekstra | **Source:** Paul's Pipeline (Substack)
**URL:** https://paulhoekstra.substack.com/p/visual-output-with-claude-code
**Published:** April 19, 2026

## Summary

How to achieve professional visual outputs (slides, video, UI design, architecture diagrams) using Claude Code skills/MCPs, bypassing Claude Design's harsh weekly usage caps.

## Key Concepts

### Core Argument: Code > UI
- Claude Design is a wrapper around capabilities Claude Code has had for months
- Visual output is "code one layer down" — HTML, React, XML

### Tool Comparison
| Output Type | Claude Design | Claude Code Tool |
|---|---|---|
| Slides | Interactive Slides | `frontend-slides` (HTML/JS) |
| Video | Motion/Animation | `remotion-best-practices` (React) |
| UI Design | Prototypes/Tweaks | Figma MCP (API-based) |
| Architecture | Not Supported | draw.io MCP (mxGraph XML) |

### Tool Deep-Dive

**frontend-slides:** Self-contained HTML with inline CSS/JS. Three-phase: content collection → style discovery (3 previews) → generation.

**Remotion:** React framework where video = components receiving frame props. `opacity: frame / 30` = 1s fade-in at 30fps. Renders via headless Chromium → MP4.

**Figma MCP:** Bidirectional — read frames to generate React, write running UI back to Figma. Used for non-UI tasks (year-plans, roadmaps) due to superior layout engine.

**draw.io (mxGraph XML):** Most useful for engineers. Reads `.tf` files, walks resource graph, generates `.drawio` diagram automatically. CI/CD automation: "Any PR that touches `.tf` files triggers a fresh diagram."

### Key Insight
> "Visual output will soon cease to be a 'special feature' and will become a default mode of technical work."
