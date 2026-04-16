---
title: "OpenAI Sandbox Agents API Guide"
source: https://developers.openai.com/api/docs/guides/agents/sandboxes
published: 2026-04-15
scraped: 2026-04-16
tags: [article, openai, agents-sdk, sandbox, API, documentation, harness, compute, manifest]
---

# Sandbox Agents | OpenAI API (Python SDK)

## Core Architecture & Boundaries
A sandbox provides an **isolated, Unix-like execution environment** with a filesystem, shell, installed packages, mounted data, exposed ports, snapshots, and controlled external access. It solves workflow brittleness when agents need persistent workspace beyond prompt context.

> *"The key split is the boundary between the harness and compute. The harness is the control plane around the model... Compute is the sandbox execution plane where model-directed work reads and writes files, runs commands, installs dependencies, uses mounted storage, exposes ports, and snapshots state."*

- **Harness (Control Plane):** Agent loop, model calls, tool routing, handoffs, approvals, tracing, recovery, auth, billing. *Keep in trusted infrastructure.*
- **Compute (Execution Plane):** File I/O, commands, dependency installs, port exposure, provider-specific state. *Runs in sandbox.*
- ⚠️ Running the harness inside the sandbox is fine for prototypes but merges orchestration with execution, breaking security/isolation boundaries.

## When to Use (Decision Matrix)
| ✅ Use Sandbox When | ❌ Avoid When |
|---|---|
| Task requires directories of docs, not just prompt context | Short model response, no persistent workspace needed |
| Agent must write/inspect files, run commands, or install packages | Shell access is only occasional (use hosted shell tool) |
| Workflow produces artifacts (CSV, JSONL, screenshots, websites) | Workspace isolation/resumable state isn't part of product design |
| Need exposed ports for services/previews (notebooks, apps) | |
| Work pauses for human review & resumes in same workspace | |

## Key Components & Configuration
| Component | Purpose |
|---|---|
| `SandboxAgent` | Extends standard `Agent`. Holds instructions, tools, handoffs, guardrails, hooks + sandbox defaults |
| `Manifest` | Fresh-session workspace contract (files, dirs, repos, mounts, env vars, users/groups) |
| `Capabilities` | Sandbox-native behavior attached to the agent |
| `Sandbox client` | Provider integration (Unix-local, Docker, hosted) |
| `SandboxRunConfig` | Per-run session source, client options, fresh inputs |
| `Saved state` | `RunState`, `session_state`, snapshots for resumption |

> *"A turn is still a model step, not a single shell command or sandbox action. The agent runtime consumes another turn only when it needs another model response after sandbox work has happened."*

## Workspace & Manifest Design
- **Paths:** Workspace-relative only. No absolute paths or `..` escapes (ensures portability across providers).
- **Manifest Inputs:** `File`/`Dir` (synthetic), `LocalFile`/`LocalDir` (host materialization), `GitRepo`, Cloud mounts (`S3Mount`, `GCSMount`, `R2Mount`, `AzureBlobMount`, `S3FilesMount`), `environment`, `users`/`groups`.
- **Best Practices:**
  - Put repos, input artifacts, and output directories in the manifest.
  - Store long task specs in workspace files (e.g., `repo/task.md`, `AGENTS.md`).
  - Use relative paths in instructions.
  - Scope mounts to necessary inputs only; treat as **ephemeral** (snapshots skip remote mounts).

## Security & Credential Handling
- **Rule:** Treat credentials as runtime configuration, *never* prompt content.
- **Implementation:**
  - Prefer provider-native secret systems for hosted sandboxes.
  - Scope cloud storage credentials to specific mounts/provider options.
  - Use `Manifest.environment` for startup values; mark sensitive/generated entries as ephemeral.
  - Review artifacts before exporting, especially when agents access private documents.

## Capabilities & Skills
- **Default:** `Capabilities.default()` = `Filesystem()`, `Shell()`, `Compaction()`.
- ⚠️ Passing a custom `capabilities` list **replaces** defaults entirely; explicitly include needed ones.

| Capability | Use Case | Notes |
|---|---|---|
| `Shell` | Command execution, interactive input | Required for `Memory` reads |
| `Filesystem` | Edit files, inspect images | Adds `apply_patch`, `view_image` (workspace-root-relative) |
| `Skills` | Repeatable instructions/scripts/assets | Prefer over manual `.agents` mounts |
| `Memory` | Persist lessons across runs | Requires `Shell` (reads) & `Filesystem` (live updates) |
| `Compaction` | Long-running context trimming | Adjusts model behavior post-compaction |

### Loading Skills
```python
from agents.sandbox.capabilities import Capabilities, Skills
from agents.sandbox.entries import GitRepo

agent = SandboxAgent(
    name="Tax prep assistant",
    capabilities=Capabilities.default() + [
        Skills(from_=GitRepo(repo="owner/tax-prep-skills", ref="main")),
    ],
)
```
- `Skills(lazy_from=LocalDirLazySkillSource(...))` → Large local dirs, load-on-demand
- `Skills(from_=LocalDir(src=...))` → Small bundles, stage up-front
- `Skills(from_=GitRepo(...))` → Versioned, shared across sandboxes

### Port Exposure
Agent starts service inside sandbox → client exposes port → app shares/invites others to preview URL.

## Session Lifecycle & State
| State Source | Description | Use Case |
|---|---|---|
| Live session (default) | Current running session state | Multi-turn agent work |
| `RunState` | Serialized state from previous run | Resume after crash/restart |
| `session_state` | Explicitly saved/passed state | Cross-session continuity |
| New session | Fallback when no state available | Fresh start |

## Pricing & Limits
- **Billing:** Tokens used during agent execution (standard API pricing).
- **Sandbox Limits:** Provider-specific (check provider documentation).
- **Rate Limits:** Standard OpenAI API rate limits apply.
