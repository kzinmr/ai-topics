---
title: "json-render — Generative UI フレームワーク"
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - developer-tooling
  - framework
  - ai-agents
  - company
  - open-source
  - tool
aliases: [json-render, vercel-json-render]
related:
  - concepts/ai-agent-engineering
  - entities/vercel
sources:
  - raw/articles/2026-05-07_vercel-labs_json-render.md
  - https://github.com/vercel-labs/json-render
---

# json-render — Generative UI Framework

## Overview

**json-render** is a Generative UI framework developed by **Vercel Labs**. It generates dynamic, personalized UI from natural language prompts. It ensures generative UI reliability by **constraining** AI output to a predefined catalog of components and actions.

## Core Philosophy

> "Let AI build the UI, but only use the parts you define"

- **Guardrailed**: Limits AI output to a developer-defined component catalog
- **Predictable**: JSON output always conforms to defined schemas
- **Fast**: Progressive streaming + sequential rendering based on model response
- **Cross-Platform**: Single catalog supports React, Vue, Svelte, Solid, React Native, and more
- **Batteries Included**: 36 pre-built shadcn/ui components

## Architecture

```
Natural Language → AI Model → JSON Spec → Renderer → UI
                ↑
         Component Catalog (Zod schema constrained)
```

### 3-Step Workflow

1. **Catalog Definition**: Constrain components and actions available to AI using Zod schemas
2. **Component Implementation**: Map the catalog to actual UI implementations
3. **AI-Generated Spec Rendering**: `<Renderer spec={spec} registry={registry} />`

## Ecosystem

| Category | Package |
|----------|-----------|
| **Core** | `@json-render/core`, `@json-render/codegen`, `@json-render/yaml` |
| **Web Frameworks** | React, Vue, Svelte, Solid |
| **UI Libraries** | `@json-render/shadcn`, `@json-render/shadcn-svelte` |
| **Special Purpose** | Next.js (full app), React Native (mobile), Remotion (video), React PDF, React Email, Ink (terminal TUI) |
| **3D/Graphics** | `@json-render/react-three-fiber` (3D, Gaussian Splatting), `@json-render/image` (SVG/PNG) |
| **State Management** | Redux, Zustand, Jotai, XState adapters |

## Advanced Features

### Dynamic Props & Expressions

Expressions can be embedded in component props:
- `$state`: Read value from state model
- `$cond`: Ternary logic (`$then` / `$else`)
- `$template`: String interpolation (`"Hello, ${/user/name}!"`)
- `$computed`: Call registered functions

### Conditional Display
```json
{
  "type": "Alert",
  "visible": [
    { "$state": "/form/hasError" },
    { "$state": "/form/errorDismissed", "not": true }
  ]
}
```

### SpecStream (Streaming AI)
Process partial JSON chunks to progressively update the UI:
```typescript
const compiler = createSpecStreamCompiler<MySpec>();
const { result } = compiler.push(chunk);
setSpec(result); // Update UI with partial results
```

### Automatic Prompt Generation
```typescript
const systemPrompt = catalog.prompt();
// Includes component descriptions, prop schemas, and available actions
```

## Differentiation from Competitors

| Dimension | json-render | Vercel AI SDK | Traditional Generative UI |
|--------|-------------|---------------|-------------------|
| **Constraint Method** | Zod catalog (strict) | Tool calling | Free-form |
| **Cross-Framework** | 12+ renderers | React-centric | Single |
| **Component Count** | 36 pre-built | DIY implementation | — |
| **License** | Apache-2.0 | — | — |

## Related Pages

- [[concepts/ai-agent-engineering]] — AI agent UI generation context
- [GitHub: vercel-labs/json-render](https://github.com/vercel-labs/json-render)
