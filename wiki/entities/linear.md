---
title: "Linear"
type: entity
created: 2026-05-08
updated: 2026-05-29
tags:
  - company
  - developer-tooling
  - product-management
  - code-intelligence
  - optimization
  - coding-agents
aliases: ["Linear.app"]
sources:
  - https://linear.app
  - raw/articles/2026-05-14_linear_code-intelligence-linear-agent.md
  - raw/articles/2025-xx-how-is-linear-so-fast-technical-breakdown.md
  - raw/articles/linear.app--code-review-should-be-fast--2026-05-28.md
---

# Linear

Purpose-built project management and issue tracking tool designed for high-performance software teams. Known for exceptional design quality, speed, and opinionated workflows. Pioneering agent-native product development with Linear Agent, including [[concepts/linear-agent-code-intelligence|Code Intelligence]] (May 2026) for codebase-aware reasoning.

| | |
|---|---|
| **Type** | Private (VC-backed, Unicorn) |
| **Founded** | 2019 |
| **Leadership** | Karri Saarinen (Co-Founder & CEO), Jori Lallo (Co-Founder & CPO), Tuomas Artman (Co-Founder & CTO), Cristina Cordova (COO) |
| **Key Products** | Linear (issue tracking, sprints, roadmaps), Linear Agent, Linear Asks, **Linear Diffs (May 2026)** |
| **Website** | [linear.app](https://linear.app) |
| **Tech Blog** | [linear.app/blog](https://linear.app/blog) ("Now") |

## Key Facts
- Founded by ex-Airbnb, Coinbase, and Uber engineers frustrated with existing project tools
- 25,000+ companies use Linear including OpenAI, Coinbase, Ramp, Vercel, and Cursor
- Valued at $1.25B+; Series C; 51-100 employees distributed across North America and Europe
- Known as "the Apple of project management" for relentless focus on craft and quality

## Products & Technology
- **Linear**: Fast issue tracking, sprint planning, and roadmap management
- **Linear Agent**: AI agent integrated into workflows for automated issue resolution; includes [[concepts/linear-agent-code-intelligence|Code Intelligence]] (May 2026) for codebase-aware reasoning
- **Linear Asks**: Structured intake for product requests
- **Linear Diffs**: Code review inside Linear (launched May 28, 2026). Pull requests reviewed directly within the Linear workspace, attached to issues and projects. Key features: guided reviews (structural chapter-based diff navigation), structural diff highlighting (strips formatting noise), fast near-instant loading. Designed for the agent era where PR volumes are growing rapidly.
- Linear for Microsoft Teams, MCP support, multi-level sub-teams

## Code Review: Linear Diffs (May 2026)

Linear Diffs is a new code review experience built directly into the Linear workspace, launched May 28, 2026. It addresses the pain that "code review has stayed painfully slow while everything else sped up" — especially as AI coding agents increase PR volume.

### Design Philosophy
- **Fast**: Reviews should open near-instantly
- **Focused**: Show what matters, strip out the noise
- **In context**: Code sits next to the issue, project, and customer signal behind the change

### Key Features
- **Guided reviews**: Breaks diffs into chapters that follow the order the work was reasoned through. Core change first, then consequences, auxiliary changes and glue code kept separate.
- **Structural diff highlighting**: Strips formatting-only changes, leaving only the actual logic change visible.
- **Integrated context**: Issue, project, and customer signal that inspired the change are visible alongside the diff.
- **Priority-aware review queue**: Reviews sit inside Linear's task system where priority is visible next to all other work.

### Strategic Implications
Diffs positions Linear as an end-to-end software development workspace competing directly with GitHub's PR review flow. This, combined with Linear Agent and Code Intelligence, creates a unified issue → code → review pipeline within a single tool. The launch announcement explicitly frames agents' growing PR volume as a key driver: "the speed gained from using agents gets swallowed in review."

Source: [Code review should be fast](https://linear.app/now/code-review-should-be-fast) (May 28, 2026)

## Performance Architecture

Linear's speed is not a single optimization, but a system-level design philosophy. Source: [How's Linear so fast? — performance.dev](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)

### Core Philosophy: Local-First

The database the UI reads from lives in the browser via IndexedDB. The server is a sync target, not the source of truth for rendering.

- **In-Memory MobX Observables** – All data hydrates into MobX objects; UI reads directly, no server round-trip
- **Local-First Writes** – `issue.title = "New title"; issue.save();` updates in-memory state synchronously, persists to IndexedDB, queues async network sync. No spinners.
- **Granular Re-renders** – Each property is its own observable; changing one field re-renders only that cell, not the whole list
- **Offline Support** – Queued mutations flush when connectivity returns

### Three Pillars of the Sync Engine

1. **Data is already there** – Hydrates from IndexedDB; no "loading issues" state. Heavy tables (Issue, Comment) lazy-hydrate on demand (data-level code splitting).
2. **Mutations don't wait** – UI updates instantly, queued in transaction journal
3. **One delta, one cell** – Server confirms with small JSON; MobX only re-renders components that read changed fields. 50-issue update = 50 cell re-renders, not a full list re-render.

### Frontend Optimizations

- **Bundler Evolution**: Parcel → Rollup → Vite → Rolldown (Rolldown-Vite + plugin-react-oxc)
- **Results**: 50% less code; 30% smaller after compression; 59% drop in time-to-first-paint on Safari
- **Target `esnext`** – no legacy polyfills or ES5 transpilation
- **Per-package chunking** – each npm package > ~3KB gets its own chunk, reducing cache invalidation
- **Module preloading** – `<link rel="modulepreload">` for critical chunks, fetched in parallel before to collapse import waterfall
- **Service Worker precaching** – ~1,200 hashed assets cached after first load; app works offline
- **Custom Canvas renderer** – large tables use Canvas 2D instead of DOM nodes; 10K+ issues with zero jank
- **Virtual scrolling** – only visible rows rendered
- **No CSS-in-JS** – avoids runtime style computation overhead
- **Total shipped**: ~21 MB minified, split into hundreds of route-level chunks

### Render First, Authenticate Second

- No blocking session validation on startup
- If `localStorage.ApplicationStore` exists → workspace data in IndexedDB → render immediately
- Server validates session passively (first WebSocket/HTTP request) and redirects to login if needed
- Philosophy: **assume happy path, verify in background**

### Keyboard-First UX

- Every action has a shortcut (single letters for common, two-letter combos for navigation)
- ⌘K Command Palette searches local MobX pool, contextual — entire app navigable from one panel

### Backend Architecture

- **GraphQL API** – strongly typed, efficient data fetching
- **Delta sync protocol** – server sends only changed fields, not full objects
- **WebSocket-first** – real-time collaboration, no polling
- **PostgreSQL** – primary datastore, but UI never queries it directly
- **Idempotent mutations** – safe to retry, handles network failures gracefully

## Related
- [[entities/openai]] — Customer and partner; uses Linear for product development
- [[entities/factory]] — Factory Droids integrate with Linear for agentic development
- [[entities/atlassian]] — Jira is Linear's primary incumbent competitor
- [[concepts/linear-agent-code-intelligence]] — Linear Agent Code Intelligence (May 2026)
- [[concepts/code-review]] — Code review as a concept and its evolution in the AI agent era
- [[concepts/gemini/managed-agents]] — Competing managed agent infrastructure from Google
