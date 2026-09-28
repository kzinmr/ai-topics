---
source_url: https://github.com/google/ax
ingested: 2026-09-28
sha256: 253b405e645d7d8439108c02f87477531150535537555d6e0d7f2c56691a9946
---

# google/ax — README (excerpt)

AX is a high-throughput, declarative orchestrator to run billions of autonomous agent workloads in a cluster. It runs on top of Agent Substrate for sandboxed execution and is built to run billions of tasks per cluster. If you have used Kubernetes, ax will feel similar.

Note: AX and several of its features are in heavy development. The project is actively refining its core concepts, protocols, and specifications, and will likely introduce major breaking changes prior to a stable release.

## Core idea

Declare an agentic task with workspaces and model specifications. AX sandboxes it, wires up its workspace, fences its network, and helps you run a large number of them per cluster. Either use a single task per agent, or compose as many as your agent needs.

## Declarative task spec (task.yaml)

```yaml
apiVersion: ax.io/v1alpha1
kind: Workspace
metadata:
  name: golang
spec:
  git:
    - repo: https://github.com/golang/go.git
      branch: "my-fix"
---
apiVersion: ax.io/v1alpha1
kind: Task
metadata:
  name: test
spec:
  workspaces:
    - name: golang
  # ... model specification, sandbox/network policy per task
```

Key primitives visible in the landing/docs page:
- **Workspace** — declarative source of truth for what an agent operates on (git repos, branches).
- **Task** — a unit of agent work bound to workspaces and model specs.
- **Sandbox + network fencing** — per-task execution isolation, provided by Agent Substrate underneath.
- Kubernetes-like semantics (declarative specs, cluster-scale reconciliation) applied to agent workloads rather than containers.

Landing page tagline: "Declare an agentic task. AX runs it at scale."
