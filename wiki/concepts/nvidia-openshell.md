---
title: "NVIDIA OpenShell (agent runtime)"
type: concept
redirect: ../entities/nvidia-openshell
aliases:
  - NVIDIA OpenShell
  - OpenShell
created: 2026-10-25
updated: 2026-11-02
tags:
  - ai-agents
  - agent-platform
  - sandbox
  - security
  - open-source
  - infrastructure
  - developer-tools
sources:
  - "https://github.com/NVIDIA/OpenShell"
  - "https://news.ycombinator.com/item?id=50198675"
  - "[[raw/articles/2026-10-22_nvidia-openshell_readme-launch]]"
---

# NVIDIA OpenShell

> **Redirect**: The canonical page is [[entities/nvidia-openshell]].

Duplicate created 2026-10-25 alongside the richer 2026-04-30 entity page. Merged 2026-11-02; the launch-specific details below are preserved here and are also covered on the canonical page.

## Unique facts preserved from this page

- **License / implementation**: Apache-2.0, written in Rust
- **Enforcement model**: kernel-level syscall / file / network enforcement
- **Policy diffs**: formal verification of policy diffs (declarative YAML policy engine)
- **Egress credential injection**: credentials injected at the egress boundary so agents never hold them
- **Launch**: October 2026 README launch, discussed on HN (item 50198675)

## Related Pages

- [[entities/nvidia-openshell]] — **canonical**
- [[entities/nvidia-nemoclaw]] — NemoClaw reference stack (OpenShell is the runtime layer below it)
- [[concepts/harness-engineering]] — Open Runtime layer
- [[concepts/security-and-governance/agent-sandboxing]] — Level 2-3 sandboxing
