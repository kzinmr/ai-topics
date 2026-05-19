---
title: "Firecracker"
type: concept
aliases:
  - firecracker
  - firecracker-microvm
created: 2026-04-25
updated: 2026-05-13
tags:
  - sandbox
  - isolation
  - aws
  - infrastructure
  - agent-safety
  - virtualization
status: full
sources:
  - raw/articles/2026-05-11_kylejeong_firecracker-agent-infra.md
---

# Firecracker

Firecracker is an open-source **Virtual Machine Monitor (VMM)** written in Rust (~50,000 lines) by AWS, designed to create and manage **microVMs** — lightweight virtual machines with minimal device emulation. It powers AWS Lambda and AWS Fargate, enabling VM-level isolation at near-container startup speeds (~125ms to init process).

## The Isolation Problem

Traditional Linux containers (Docker) rely on three kernel features for isolation:
- **Namespaces** — process/tree isolation
- **cgroups** — resource limits
- **seccomp** — system call filtering

These were designed for **resource management**, not security. Containers share the host kernel, making them vulnerable to kernel exploits and container breakout attacks. This is insufficient for running untrusted code — a critical requirement for AI agent infrastructure.

## Architecture

Firecracker uses **hardware virtualization** via Linux's KVM (Kernel-based Virtual Machine) to create microVMs:

- **Minimal device model**: Only virtio-net (network), virtio-block (storage), and a minimal serial console. No BIOS, no VGA, no USB.
- **Direct kernel boot**: Loads uncompressed `vmlinux` directly into guest memory, skipping the traditional boot sequence for ~125ms init process launch.
- **Per-vCPU threads**: One thread per virtual CPU plus a management thread. Memory overhead < 5MB per microVM (excluding guest memory).
- **No QEMU**: Eliminates the heavy QEMU emulation layer entirely.

## Why Agent Infrastructure Companies Care

AI agent companies need to run **arbitrary, untrusted user code** safely:

| Requirement | Container | Full VM | Firecracker |
|---|---|---|---|
| Isolation strength | Weak (shared kernel) | Strong | Strong |
| Cold start time | < 1s | 30-120s | ~125ms |
| Density per host | High | Low | High (4000+ microVMs on one host) |
| Over-provisioning | Yes | Limited | Yes |

Companies using or evaluating Firecracker for agent sandboxing:
- **Browserbase** — headless browser infrastructure for web agents
- **E2B** — code execution sandboxes for AI agents (managed API)
- **Daytona** — development environments as code
- **Modal** — serverless GPU compute with sandbox product
- **Northflank** — managed sandbox platform
- **Google Agent Sandbox** — Kubernetes-based sandbox using Firecracker or gVisor

## Firecracker vs. gVisor

Both are Layer 1 isolation primitives for AI agent sandboxing:

| Dimension | Firecracker | gVisor |
|---|---|---|
| Approach | Hardware virtualization (KVM microVMs) | User-space kernel (syscall interception) |
| Isolation | Stronger (separate kernel) | Strong (user-space kernel, shared host kernel) |
| Operational complexity | Higher (image distribution, networking, orchestration) | Lower (feels like containers) |
| Performance | Near-native, minor virtio overhead | Higher syscall overhead |
| Compatibility | Full Linux binary compatibility | Some syscall gaps (incomplete `/proc`, `/sys`) |

## History

- **2018**: AWS open-sources Firecracker to power Lambda and Fargate with stronger multi-tenant isolation
- **~2024-2025**: AI agent companies begin adopting Firecracker for code execution sandboxes as agent use cases demand running untrusted code

## Related Pages

- [[concepts/sandbox]] — AI agent sandboxing overview
- [[concepts/ai-infrastructure]] — AI infrastructure landscape
- [[entities/browserbase]] — Browser automation infrastructure
- [[concepts/gvisor|gVisor]] — Alternative isolation primitive
