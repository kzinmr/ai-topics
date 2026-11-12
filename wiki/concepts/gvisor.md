---
title: "gVisor (Sentry application kernel)"
created: 2026-11-12
updated: 2026-11-12
type: concept
tags: [infrastructure, sandbox, isolation, security, virtualization, ai-infrastructure, kubernetes, open-source]
sources:
  - raw/articles/2026-11-12_modal_gvisor-cncf-maintainer.md
  - https://modal.com/blog/modal-gvisor-maintainer
confidence: high
---

# gVisor

**gVisor** is an open-source container sandbox that inserts a userspace **application kernel ("Sentry")** — written in Go — between the container and the host Linux kernel. The Sentry implements the Linux system-call interface itself and requests only a small, filtered set of operations from the host. The tagline from Modal's writeup: *"Your program sees Linux. The host sees one well-behaved process."*

On **November 11, 2026 at KubeCon (Salt Lake City), Google donated gVisor — including its name and trademarks — to the CNCF**, moving the project to a maintainer-led governance model. [[entities/modal-labs|Modal]], **Ant Group**, and **Tines** committed to join the maintainers; **OpenAI, Tencent, and NVIDIA** continue their contributions.

## Architecture: defense in depth

1. **The Sentry** intercepts every syscall the app makes with its own implementation — the app never talks to the host kernel.
2. **The Sentry itself is hardened** with the same Linux primitives that protect ordinary containers, on the assumption layer 1 might fail:
   - **namespaces** — private view of processes, networking, mounts
   - **pivot_root** — empty root filesystem
   - **cgroups** — caps on CPU, memory, reachable devices
   - **seccomp** — tight filter allowing only the few host syscalls the Sentry needs, validating many arguments

To reach the host, an attacker must break the Sentry **and** break out of this hardening.

## Why it matters for AI workloads

gVisor has become a de facto runtime for AI sandboxing because it hits a specific requirement set that runc and microVMs each partially miss:

| Requirement | gVisor answer |
|---|---|
| Multi-tenant untrusted code | Real boundary vs shared host kernel — Modal: *"not an acceptable boundary when the code might have been written a minute ago by a model someone prompted"* |
| GPU access | **nvproxy** validates the NVIDIA driver's ioctl interface instead of exposing the raw driver; GPU memory/compute stay native |
| Cold start | ~**25 ms** boot, ~**12 MB** memory overhead |
| Portable state | Checkpoint/restore of an entire sandbox (processes, files, sockets — and GPU memory via `cuda-checkpoint`); foundation of Modal memory/GPU snapshots |
| Portability | **No hardware virtualization needed** — runs on any Linux machine, including cloud VMs without nested virt and bare-metal GPU servers |

Scale evidence: Modal launches **upwards of 40 million gVisor containers a day** (GPU inference, multi-node training, AI coding agents, sandboxes), and claims scaling zero → one million sandboxes in a minute.

## Position in the sandbox taxonomy

- vs **runc/plain containers**: shared host kernel = single kernel bug can escape the container; gVisor adds the Sentry layer.
- vs **microVMs (Firecracker etc.)**: no hardware virtualization dependency — works where nested virt is unavailable or slow (most cloud VMs) and on bare-metal GPU fleets.
- In the [[concepts/agent-sandbox-patterns|agent sandbox taxonomy]], gVisor is the canonical **infrastructure-level sandbox** ([[concepts/infrastructure-level-sandbox]]) used for **isolate-the-agent** deployments running untrusted, model-generated code.

## Related

- [[entities/modal-labs]] — primary AI-workload adopter and now CNCF maintainer
- [[entities/modal-sandbox]] / [[concepts/modal-sandboxes]] — gVisor-based product surface
- [[concepts/agent-sandbox-patterns]] — taxonomy this fits into
- [[concepts/cve-2026-55607-claude-code-sandbox-escape]] — why runtime-level isolation matters for coding agents
- [[entities/google]] — original creator, now donating to CNCF
