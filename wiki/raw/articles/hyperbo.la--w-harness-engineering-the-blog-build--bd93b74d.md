---
title: "Harness Engineering the Blog Build (Again)"
url: "https://hyperbo.la/w/harness-engineering-the-blog-build/"
fetched_at: 2026-04-29T07:02:15.129666+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Harness Engineering the Blog Build (Again)

Source: https://hyperbo.la/w/harness-engineering-the-blog-build/

In
Debazeling
, I said the build got simpler; then
@frantic
asked for an RSS feed, so I naturally rewrote the whole
thing without touching VS Code.
That immediately turned
add RSS
into a harness engineering exercise. I applied
the techniques from my
Harness Engineering
writeup to the
blog, trying out new technology in the small as I typically have in this repo.
If I am going to keep this blog static, no client-side rendering, and hosted for
free on GitHub Pages, then the developer workflow still needs to be excellent.
So the target became the
Vite
SSG build I actually want: Vite-native
rendering and asset pipeline,
MDX
posts, React composition, and static
dist output. I am doing that with Codex, and this is definitely the last rewrite
and yes, maybe this one even has snapshot tests. Hard constraints do not change:
free hosting on GitHub Pages, no client-side rendering fallback, and zero
interest in unsolicited internet takes.
What Changed
Big Structural Shift
This branch turns the repo into a pnpm workspace monorepo with explicit package
boundaries under
packages/*
and
hld/*
, and moves the build/tooling path to
TypeScript-first Node ESM. The old mixed-language build plumbing is gone. There
are no remaining Go or shell build scripts driving site generation here. The
shape is now one toolchain, one workspace graph, and one set of invariants.
Dive into
hld/
hld/
is where local development tools and policy enforcement live. It exists
because conventions rot unless they are executable. Code is free! That means we
codify repo contracts as tools and lints instead of tribal memory. Concrete
examples:
hld/eslint-plugin-hyperbola
ships custom rules like:
hyperbola/no-fs-imports
: require async fs API usage, with explicit allows
for
fs/constants
and various type-only imports.
hyperbola/require-eslint-disable-justification
: require coding models to
justify why they disable lints to permit human operators to add additional
guardrails or tweak lints to permit legitimate false positives.
hld/source-structure-lints
enforces rules like:
Ban
.mjs
and
.mts
files: require modern ESM tooling.
Forbid coverage-ignore pragmas: prevent coding models from hacking around code
that does not enable testability.
Enforce dependency hygiene across workspace packages: if a dependency appears
in multiple
package.json
files, it must be promoted to the pnpm workspace
catalog and referenced via
catalog:
(or
workspace:^
for workspace deps).
Enforce content/package placement: legacy blog markdown under
src/markdown/blog
fails lint; posts must live at
packages/blog/content/<slug>/post.mdx
.
You can just do things
The source structure lints and Codex mean low priority nice-to-haves are trivial
to pull above the line. I am now enforcing smart punctuation in blog prose:
apostrophes and quotes are linted so content style is statically checked.
Code is free! That made it cheap to add the smart punctuation lint and migrate
the existing post corpus in one sweep.
Utility Packages
The utility layer under
packages/
exists to centralize invariants that should
not be reimplemented in app code. Code is free!
@hyperbola/url
is a concrete example: humans often pass raw strings or mutable
URL
objects, but this repo uses
HyperUrl
, an immutable semantic type that
encodes URL intent and rejects invalid shapes at construction. That tiny domain
type removes a whole class of stringly-typed mistakes at package boundaries.
The same logic applies to
@hyperbola/frontmatter
: generic npm frontmatter
parsers are usually permissive and return untyped blobs, but this package
encodes exactly what this repo expects, then validates it with Zod into a typed
contract. It enforces explicit frontmatter fences, parses YAML with a
constrained schema, and returns path-aware errors when content is malformed.
Those guardrails make failures clearer and behavior more reliable where markdown
crosses into application data.
Package Layering, Content Colocation, Typed Domain Model for Blog
The package layering is explicit.
@hyperbola/blog
is the domain layer: it loads the manifest, validates
frontmatter, builds typed template contexts, and exposes canonical blog route
accessors and feed rendering.
@hyperbola/app-shell
is shared UI shell composition and assets, with no blog
domain logic.
@hyperbola/blog-vite
is the integration boundary that bridges domain data to
Vite SSR/build behavior.
Content is colocated per post in
packages/blog/content/<slug>/
with
post.mdx
and post assets side by side, which keeps authorship and rendering inputs in one
place.
React, MDX, SSR, Vite-Native
Blog post bodies are MDX React components, not string-injected HTML. Dev route
rendering and build prerendering both run through Vite’s native module graph and
SSR pipeline for
/w/
,
/w/<slug>/
, and
/w/feed.xml
. Post assets flow
through imports so Vite owns resolution and hashing for content assets, while
identity assets like favicons and
site.webmanifest
intentionally keep stable
filenames.
Tests
There are tests across the workspace, including domain packages, utility
packages, and tooling packages. Core package-level Vitest configs enforce 100%
thresholds for lines, functions, branches, and statements, and source-structure
lints explicitly reject coverage-ignore pragmas so test gaps are addressed in
code instead of hidden behind comments.
It is free to do so. Codex has knowledge on how to write testable, well-covered
code deep in the model weights. There is zero incremental effort to do 80%
coverage vs. 100%. In the world of human-authored code, less-than-100% coverage
is usually chosen as an organizational and effort tradeoff. There is no need to
make that trade when agents are writing the code and has the plus that
100%
is
non-negotiable.
Persona-oriented documentation
Tests catch regressions, but tests are only half of harness engineering. The
other half is making the repo legible to the agent.
In
Harness Engineering
, this maps directly to
We made
repository knowledge the system of record
,
Agent legibility is the goal
, and
Enforcing architecture and taste
. I encode those constraints in-repo as policy
docs instead of keeping them in my head or in chat scrollback.
For this codebase,
docs/FRONTEND_ARCHITECTURE.md
is one of the hard contracts
the agent is expected to follow. The snapshot below is included verbatim as a
concrete example of persona-oriented documentation at work.
Architecture snapshot: Vite-native /w/* rendering, explicit package boundaries, context-first React composition, MDX post rendering, and Vite-managed assets.
Frontend Architecture
Scope
This document is a hard architecture contract for frontend code in this
repository. If implementation diverges, code must be updated to match this
document. Do not add workaround layers.
North Star
All site routes, including dynamic blog routes under
/w/*
, must execute
through Vite’s native rendering and asset pipeline in both dev and build.
Required outcomes:
/w/*
behaves as if each route had a native Vite React entrypoint.
React SSR output is produced by modules loaded through Vite.
Asset URLs come from Vite/Rollup output, not ad-hoc hardcoded paths.
Non-Negotiable Rules
Fix architecture, do not work around architecture.
If blocked, report the concrete error and propose a proper architectural
solution.
Do not use
vite ... --configLoader runner
script-level workarounds.
Do not introduce custom asset filename convention helpers for blog output.
Resolve rendered asset URLs from Vite/Rollup emitted metadata, not from
inferred naming patterns.
Package Responsibilities
@hyperbola/app-shell
@hyperbola/app-shell
owns shared HTML shell composition and shared shell
assets.
Requirements:
Export composable primitives (
App
,
AppShell
,
Nav
,
Brand
,
Container
,
Link
, shell render helpers).
One React component per source file.
No component export barrels in
index.ts
.
Expose component entrypoints via explicit package export paths.
Keep app shell domain-agnostic (no blog domain logic).
Own shared shell runtime assets (brand marks, shared client entry, shared
styles) in source under this package.
Head metadata must be composed in React from typed data, not string
injection.
@hyperbola/blog
@hyperbola/blog
owns blog domain data and typed template contexts.
Requirements:
Load and validate blog manifest and posts.
Provide typed context builders for index/post pages and feed rendering.
Provide canonical route URL accessors for blog fixed routes (for example
blog index and feed) so UI does not reconstruct these URLs from string
manipulation.
Remain UI-agnostic.
@hyperbola/blog-vite
@hyperbola/blog-vite
is the integration bridge between
@hyperbola/blog
and
root Vite config.
Requirements:
Register Vite plugins for
/w/
,
/w/<slug>/
,
/w/feed.xml
.
Use
server.ssrLoadModule
for dev route rendering.
Prerender the same routes in build from the same SSR entry module path.
Keep dev/build route behavior and asset behavior aligned.
Virtual route entry modules must be SSR-safe and must not eagerly import
browser-only modules that access DOM globals.
Client asset graph modules and SSR route entry modules must be separated so
server-only route loaders are not bundled into browser chunks.
React Composition and Context
Use React context/hooks to avoid prop drilling where route-level domain data
is needed by multiple leaf components.
Requirements:
Route context stores domain/template data from
@hyperbola/blog
.
Hooks return domain data only.
Hooks must never return React nodes, JSX elements, or component functions.
Rendering components read domain data from hooks and render UI.
Do not pass transport-only props through multiple component layers when
context is the correct boundary.
A function may use a
use*
prefix only if it is a real React hook that
directly calls React hooks or hook-based abstractions.
Do not derive fixed route URLs by slicing or replacing strings (for example
deriving blog index from RSS URL text). Read route URLs from typed domain
context.
MDX Rendering Model
Blog post bodies must render as MDX React components.
Requirements:
No
dangerouslySetInnerHTML
for blog post content.
A dedicated post content component reads route domain data (for example
slug) from context hook and renders the matching MDX module.
Post content modules are loaded through Vite module loading.
Markdown/MDX image references, including HTML
<img>
and
srcset
entries,
must be transformed to imports so Vite manages emission and hashing.
Asset Pipeline Rules
All UI assets must flow through Vite imports.
Requirements:
Shell visual assets used in app-shell composition (for example wordmark and
RSS icon) must be imported from source modules.
Preload links must reference imported asset URLs managed by Vite.
Blog post images must not depend on custom static file serving.
Do not manually copy blog image assets as a primary path outside Vite
graph.
Do not hardcode CSS/JS bundle URLs in page renderers when Vite output can
provide them.
Preserve static, canonical root paths for web app identity assets where
stability is the feature (
/favicon.ico
,
/favicon.svg
, PNG favicon
sizes,
/site.webmanifest
, browser config files).
Social image metadata values (
twitter:image
,
og:image
) must be absolute
URLs with scheme and host.
Banned Patterns
The following are architecture violations:
Rendering post content with
dangerouslySetInnerHTML
.
Manual
/w/<slug>/<asset>
middleware as primary blog image strategy.
Component barrels in
index.ts
.
Hooks that return React nodes or component functions.
Prop drilling route domain state through intermediate presentation layers.
Script hooks that bypass Vite-native behavior.
Reconstructing route URLs via string operations when typed route/domain
accessors already exist.
SSR entry modules that import browser-only client modules at top level.
Validation Checklist
Before merging frontend architecture changes:
pnpm run lint
pnpm run test
pnpm run build
Confirm
/w/<slug>/
in dev is rendered through Vite SSR route path.
Confirm built
/w/<slug>/
HTML references Vite-emitted URLs for post
images and shell assets.
Confirm no blog post body path uses
dangerouslySetInnerHTML
.
