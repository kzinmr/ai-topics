---
title: Local-First Architecture
type: concept
status: draft
aliases:
  - local-first
  - local-first software
  - local-first sync
tags:
  - architecture
  - web-development
  - optimization
  - developer-tooling
sources: []
updated: 2026-07-10
---

# Local-First Architecture

Local-first architecture is a software design paradigm where the primary data store lives on the client device (browser IndexedDB, SQLite, etc.), and the server acts as a synchronization target rather than the source of truth for rendering.

## Core Principles

1. **Client as Source of Truth**: The UI reads from and writes to a local database first
2. **Optimistic Updates**: Mutations are applied locally immediately, then synced to the server asynchronously
3. **Offline-First**: The application remains fully functional without network connectivity
4. **Conflict Resolution**: CRDTs or operational transforms handle merge conflicts during sync
5. **Granular Reactivity**: Only changed fields trigger re-renders, not entire components

## How Linear Implements Local-First

Linear's speed comes from a foundational decision: **the database the UI reads from lives in the browser** (IndexedDB).

### Architecture Stack

```
┌─────────────────────────────────────────┐
│              UI Layer (React)           │
│  ┌─────────────┬──────────────────────┐ │
│  │  MobX Store │ Canvas Renderer      │ │
│  │ (In-Memory) │ (Large Lists)        │ │
│  └──────┬──────┴──────────┬───────────┘ │
│         │                 │             │
│  ┌──────▼─────────────────▼───────────┐ │
│  │        IndexedDB (Local)           │ │
│  │  • Issues, Comments, Users         │ │
│  │  • Transaction Journal             │ │
│  │  • Lazy Hydration (data-level)     │ │
│  └──────────────┬─────────────────────┘ │
│                 │                        │
│  ┌──────────────▼─────────────────────┐ │
│  │      Sync Engine (WebSocket)       │ │
│  │  • Delta protocol                  │ │
│  │  • Idempotent mutations            │ │
│  │  • Conflict resolution             │ │
│  └──────────────┬─────────────────────┘ │
└─────────────────┼───────────────────────┘
                  │
┌─────────────────▼─────────────────────┐
│           Server Layer                │
│  • GraphQL API                        │
│  • PostgreSQL (primary datastore)     │
│  • Real-time collaboration            │
└───────────────────────────────────────┘
```

### Key Implementation Details

**Optimistic Updates Pattern:**
```js
// Traditional (server-first)
const response = await fetch(`/api/issues/${id}`, { method: 'PATCH', body: ... });
setState(response); // UI waits for server

// Linear's approach (local-first)
issue.title = "Updated title"; // Instant UI update
issue.save(); // Async: IndexedDB → Queue → Server → Confirm
```

**Data-Level Code Splitting:**
- Heavy tables (Issue, Comment) lazy-hydrate on demand
- Only visible rows are rendered (virtual scrolling)
- 10K+ issues with zero jank

**Granular Re-renders:**
- Each property is its own MobX observable
- 50-issue update = 50 cell re-renders, not a full list re-render
- Server sends only changed fields (delta sync)

## Benefits

1. **Zero Perceived Latency**: UI updates instantly because data is local
2. **Offline Functionality**: App works without network, syncs when reconnected
3. **Reduced Server Load**: Only deltas are transmitted, not full objects
4. **Better User Experience**: No loading spinners, no "please wait" states
5. **Resilience**: Network failures don't block user actions

## Challenges

1. **Conflict Resolution**: Multiple devices editing same data requires CRDTs or OT
2. **Storage Limits**: Browser IndexedDB has quotas (~50-60% of disk on modern browsers)
3. **Security**: Sensitive data stored locally needs encryption
4. **Complexity**: Sync engines are harder to build than simple CRUD APIs

## Related Technologies

- **CRDTs**: Automerge, Yjs, GunDB
- **Local Databases**: RxDB, PouchDB, SQLite (WASM), IndexedDB
- **Sync Protocols**: ElectricSQL, PowerSync, Replicache
- **State Management**: MobX, Zustand, Jotai, Redux Toolkit
- **Build Optimization**: Vite, Rolldown, OXC, esbuild

## Case Studies

- **[[entities/linear]]**: Project management tool with exceptional performance via local-first architecture, IndexedDB sync engine, and granular MobX reactivity
- **Notion**: Document editor with offline support
- **Obsidian**: Local-first note-taking with Markdown files
- **Figma**: Collaborative design with local caching

## Sources

- [How's Linear so fast? A technical breakdown](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown)
- [Local-first software movement](https://www.inkandswitch.com/local-first/)
- [Replicache: Fast local-first sync](https://replicache.dev/)
