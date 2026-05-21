---
title: "How's Linear so fast? A technical breakdown"
source_url: https://performance.dev/how-is-linear-so-fast-a-technical-breakdown
source_site: performance.dev
author: performance.dev team
date: 2025
tags: [performance, frontend, local-first, indexeddb, optimistic-ui, code-splitting]
---

# How's Linear so fast? A technical breakdown

A deep dive into the architectural decisions that make Linear one of the fastest web applications.

## Core Philosophy: Eliminate the Network

Linear's speed comes from a foundational decision: **the database the UI reads from lives in the browser** (IndexedDB). Mutations apply locally first, then sync to the server asynchronously. The server is a sync target, not the source of truth for rendering.

> "The secret to building incredible web apps is by hiding all the network requests from the user."

## 1. Database in the Browser

- **In-Memory MobX Observables** – All data hydrates into MobX objects; UI reads from them directly, no server round-trip.
- **Local-First Writes** – `issue.title = "Faster ..."; issue.save();` updates in-memory state synchronously, persists to IndexedDB, and queues a network transaction. No spinners.
- **Granular Re-renders** – Each property is its own observable; changing one issue field re-renders only that cell, not the whole list.
- **Offline Support** – Queued mutations flush when connectivity returns.

**Optimistic Updates for Everyone**  
Even without a custom sync engine, libraries like **Tanstack Query / SWR** can deliver a similar feel:

```js
// Optimistic mutation with SWR
mutate(
  `/api/issues/${issue.id}`,
  { ...issue, title: "Faster app launch" },
  false
);
// vs Linear
issue.title = "Faster app launch";
issue.save();
```

## 2. Making the First Load Instant

### a. Aggressive Code Reduction & Splitting

- **Bundler Evolution**: Parcel → Rollup → Vite → Rolldown (now Rolldown-Vite + plugin-react-oxc).
- **Results**: 50% less code; 30% smaller after compression; 10–30% faster cold loads; 59% drop in time-to-first-paint on Safari.
- **Key Techniques**:
  - Target `esnext` – no legacy polyfills or ES5.
  - **Per-package chunking** – each npm package > ~3 KB gets its own chunk, reducing cache invalidation.
  - `modulePreload: { polyfill: false }`.

```js
// Reconstructed Vite config
manualChunks(id) {
  if (id.includes("node_modules")) {
    const pkg = id.match(/node_modules\/([^/]+)/)?.[1];
    if (pkg) return `vendor-${pkg}`;
  }
},
```

- **Total shipped: ~21 MB minified**, but split into hundreds of route-level chunks.

### b. Preloading Critical Chunks

- In `index.html`, `<link rel="modulepreload">` for every critical chunk.
- The browser fetches them in parallel *before* parsing JavaScript, collapsing the import waterfall.
- All preloads use `crossorigin` to match the entry script's mode, preventing double fetches.

### c. Service Worker for Precaching

- After first load, a service worker lazily downloads ~1,200 hashed assets (route chunks, icons, fonts).
- Subsequent navigations serve from cache; the app works **offline**.
- Combined with local IndexedDB, you can create/edit issues offline.

### d. Font Loading Done Right

```html
<link rel="preload"
      href="https://static.linear.app/fonts/InterVariable.woff2?v=4.1"
      as="font" type="font/woff2" crossorigin="anonymous">
```

- Variable font (single woff2 for all weights), `font-display: swap`.
- `crossorigin="anonymous"` prevents duplicate fetches.

### e. Inlined App Shell

- Inline critical CSS in `<head>` to paint loading state without external stylesheets.
- Inline JavaScript reads `localStorage` to apply:
  - Dark/light mode
  - Sidebar width & background color
  - Electron context
  - **Whether `ApplicationStore` exists** – determines if user has been here before (auth signal).

```html
<style>
  :root { --bg-color: #f5f5f5; --sidebar-width: 244px; … }
  html { background: var(--bg-color); height: 100%; }
  #appBorders { margin: 8px 8px 8px var(--sidebar-width); … }
</style>
<script>
  if (localStorage.getItem("ApplicationStore") === null)
    document.documentElement.classList.add("logged-out");
  // apply splashScreenConfig …
</script>
```

### f. Render First, Authenticate Second

- No blocking session validation on startup.
- If `localStorage.ApplicationStore` exists → workspace data is in IndexedDB → render immediately.
- The server validates the session passively (first WebSocket/HTTP request) and redirects to login if needed.
- Same philosophy: **assume happy path, verify in background**.

## 3. The Sync Engine – Three Speed Pillars

1. **Data is already there** – Hydrates from IndexedDB; no "loading issues" state.  
   - Heavy tables (Issue, Comment) lazy-hydrate on demand – **data-level code splitting**.
2. **Mutations don't wait** – UI updates instantly, queued in transaction journal.
3. **One delta, one cell** – Server confirms with small JSON; MobX only re-renders components that read changed fields. 50-issue update = 50 cell re-renders, not a list re-render.

> "Linear's speed isn't a property of any single layer. It's a property of the system."

## 4. Designed for Speed

- **Keyboard-first**: every action has a shortcut (single letters for common, two-letter combos for navigation).
- **⌘K Command Palette** – one keystroke, searches local MobX pool, contextual. Entire app navigable from one panel.
- **Custom Canvas renderer** – list rendering uses Canvas 2D instead of DOM nodes for large tables.
- **Virtual scrolling** – only visible rows rendered; 10K+ issues, zero jank.
- **No CSS-in-JS** – avoids runtime style computation overhead.
- **Electron optimizations** – native frames, custom titlebar, GPU rasterization, direct Vulkan renderer on Linux.

## 5. Backend Architecture

- **GraphQL API** – strongly typed, efficient data fetching.
- **Delta sync protocol** – server sends only changed fields, not full objects.
- **WebSocket-first** – real-time collaboration, no polling.
- **PostgreSQL** – primary datastore, but UI never queries it directly.
- **Idempotent mutations** – safe to retry, handles network failures gracefully.

## Key Takeaways for System Design

1. **Local-first is the ultimate caching strategy** – if the data is already in the browser, there's no latency to hide.
2. **Code splitting at every level** – route-level, package-level, and even data-level (lazy hydration).
3. **Optimistic everything** – assume success, reconcile in background.
4. **Granular reactivity** – MobX's field-level observables vs React's component-level re-renders.
5. **The network is the bottleneck** – hide it, preload around it, or eliminate it entirely.
6. **Progressive enhancement** – the app shell renders before auth completes.

## Related Technologies

- **Local-first software movement**: Automerge, CRDTs, ElectricSQL, RxDB
- **State management**: MobX, Zustand, Jotai, Redux Toolkit
- **Build tools**: Vite, Rolldown, OXC, esbuild
- **Offline-first patterns**: Service Workers, IndexedDB, Background Sync API
