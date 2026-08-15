---
type: raw_article
title: "DeepSeek Harness (dsh): Everything is a Plugin"
source: "github.com/deepseek-ai/deepseek-harness"
source_url: "https://github.com/deepseek-ai/deepseek-harness"
date: 2026-08-13
date_ingested: 2026-08-15
author: "DeepSeek AI"
tags: [deepseek, ai-agents, agent-harness, agent-framework, agent-runtime, open-source, cli, plugins]
note: "GitHub repo README + architecture docs. Repo created 2026-08-13, 106,561 stars at crawl time, MIT license, default branch master. Powered by Cordis (github.com/cordiverse/cordis)."
---

# DeepSeek Harness (`dsh`)

DeepSeek Harness (`dsh`) is an open-source agent harness developed by DeepSeek AI. It uses an architecture where **everything is a plugin**, powered by [Cordis](https://github.com/cordiverse/cordis), whose design is described in *A Programming Paradigm for Spatiotemporal Composability*.

**Status:** developer preview — iterating rapidly, "THERE WILL BE COMPATIBILITY-BREAKING CHANGES."

**Repo metadata (at crawl):** 106,561 stars · MIT license · topics `[ai-agents, cordis, dsh, dsh-plugin]` · created 2026-08-13.

## Run

From npm (Node.js):
```sh
npx @deepseek-ai/dsh web
```
Serves the Web UI at `http://127.0.0.1:3080` by default.

From source:
```sh
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install && pnpm run build && pnpm dsh web
```

## Architecture (from docs/architecture.md)

**Cordis** is the framework under dsh: plugins contribute services, typed events, and reversible effects to a shared context. Every part of the product is a plugin — the model adapter, the tool registry, the session log, and the agent loop itself — so every part is replaceable from configuration. There is no privileged core to patch: you extend dsh by mounting a plugin beside the others, and registrations are effects that unwind when their plugin unloads.

**Profiles and bundles:** a running `dsh` is a plugin tree composed at boot from ordered layers.
- A **profile** is a named composition stored in the Harness home (lists bundles, out-of-tree plugins, and the user's `cordis.patch.yml`). `web` and `headless` ship as templates.
- A **bundle** is a distribution format for Cordis config rows and the code they mount.
- `dsh-base` is the first layer of every profile: model adapters, tools, persistence, sandbox and approval policy, settings, credentials, telemetry. `dsh-web-app` adds the browser application; `dsh-headless` adds a one-shot runner with no server.

Layers apply to an empty entry list in order: each bundle in the profile's listed order, then the profile's `cordis.patch.yml`, then the home-level one, then any `--patch` overlay. A patch targets a row by id and replaces its whole config, or inserts new rows.

## Community and support

- GitHub Discussions for feedback/bug reports
- Add the `dsh-plugin` topic to plugin repositories for discoverability
- DeepSeek Harness Discord community
