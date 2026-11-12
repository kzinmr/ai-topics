---
title: "Modal becomes a gVisor maintainer"
type: raw-article
source_url: https://modal.com/blog/modal-gvisor-maintainer
authors: [Ayush Ranjan, Luis Capelo]
publisher: Modal Blog
published: 2026-11-11
fetched: 2026-11-12
tags: [ai-infrastructure, sandbox, security, kubernetes, virtualization]
---

# Modal becomes a gVisor maintainer (Modal Blog, Nov 11 2026)

## Key facts

- At KubeCon (Salt Lake City), **Google is donating gVisor — including name and trademarks — to the CNCF**, moving to a **maintainer-led governance model**.
- **Modal, Ant Group, and Tines** commit to join gVisor's maintainers; **OpenAI, Tencent, and NVIDIA** continue contributing.
- gVisor has been Modal's major container runtime since inception. Modal launches **upwards of 40 million gVisor containers a day** (GPU inference, multi-node training, AI coding agents, sandboxes).

## What gVisor is

- A separate **application kernel ("Sentry")** written in Go, sitting between container and host. It implements the Linux syscall interface itself and asks the host only for a small, filtered set of operations. "Your program sees Linux. The host sees one well-behaved process."
- Defense in depth: Sentry handles all app syscalls; the Sentry itself is hardened with namespaces, pivot_root (empty root fs), cgroups, and a tight seccomp filter validating many arguments. Attack requires breaking Sentry AND the hardening.
- **No hardware virtualization needed** — runs on any Linux machine, including cloud VMs without nested virt and bare-metal GPU servers.

## Why Modal runs on gVisor (requirements)

1. **Multi-tenancy needs a real boundary** — "A shared host kernel is not an acceptable boundary when the code might have been written a minute ago by a model someone prompted."
2. **GPUs have to just work** — gVisor's **nvproxy** lets a sandboxed process use NVIDIA GPUs via a proxy that understands/validates the driver's ioctl interface, instead of exposing the raw driver. GPU memory/compute stay native.
3. **Startup has to be fast** — boots a sandbox in **~25 ms with ~12 MB memory overhead**.
4. **State has to be portable** — checkpoint an entire sandbox (every process, file, socket, and with cuda-checkpoint, GPU memory too) and restore on another machine. Foundation of Modal memory snapshots and GPU memory snapshots.
5. **Runs everywhere** — no nested virtualization, no custom host kernel; same sandbox on every cloud and bare-metal box.

## Context

- Modal scaling claim: zero to a million sandboxes in a minute.
- Related: Modal Infra is "Infrastructure rebuilt for AI, from the container runtime and storage to a multi-cloud capacity pool."
