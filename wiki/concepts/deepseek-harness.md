---
title: DeepSeek Harness
created: 2026-08-15
updated: 2026-08-15
type: concept
tags:
  - ai-agents
  - agent-harness
  - agent-framework
  - agent-runtime
  - agent-architecture
  - open-source
  - deepseek
  - coding-agents
  - cli
  - plugins
  - extensibility
  - orchestration
  - multi-agent
  - developer-tooling
  - harness-engineering
sources:
  - raw/articles/2026-08-13_deepseek-harness-agent-runtime.md
  - https://github.com/deepseek-ai/deepseek-harness
---

# DeepSeek Harness

DeepSeek Harness (`dsh`) is an open-source agent harness by DeepSeek AI, released August 13, 2026, built on the "everything is a plugin" architecture. It reached ~106,000 GitHub stars within 48 hours of release — an unusually fast rise for an open-source agent runtime. MIT-licensed, currently in developer preview.

## Core architecture: "everything is a plugin"

`dsh` is powered by **Cordis** (github.com/cordiverse/cordis), a framework whose design is described in *A Programming Paradigm for Spatiotemporal Composability*. Plugins contribute services, typed events, and reversible effects to a shared context. Every part of the product is a plugin — the model adapter, tool registry, session log, and the agent loop itself — so every part is replaceable from configuration. There is no privileged core to patch.

This contrasts with the "less you build, the more it works" philosophy of [[concepts/agent-harnesses|agent harnesses]] and the [[concepts/harness-commoditization|harness commoditization]] trend: DeepSeek Harness embraces a maximally *composable* harness rather than a minimal one.

## Profiles and bundles

A running `dsh` is a plugin tree composed at boot from ordered layers:
- **Profile** — a named composition (lists bundles, out-of-tree plugins, and a `cordis.patch.yml`). `web` and `headless` ship as templates.
- **Bundle** — a distribution format for Cordis config rows and the code they mount.
- `dsh-base` is the first layer of every profile (model adapters, tools, persistence, sandbox and approval policy, credentials, telemetry). `dsh-web-app` adds the browser app; `dsh-headless` a one-shot runner.

Layers apply in order (bundle list → profile patch → home-level → `--patch` overlay); a patch targets a row by id and replaces its config or inserts new rows.

## Usage

```sh
npx @deepseek-ai/dsh web   # Web UI at http://127.0.0.1:3080
```

Plugins are discoverable via the `dsh-plugin` GitHub topic.

## Related

- [[concepts/agent-harnesses|Agent Harnesses]]
- [[concepts/harness-commoditization|Harness Commoditization]]
- [[concepts/why-harness-development-boom|Why Harness Development Boom]]
- [[concepts/open-source-stewardship|Open Source Stewardship]]
- [[entities/deepseek|DeepSeek]]
