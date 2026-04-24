---
title: "Sandbox — AI Agent Code Execution Isolation"
type: concept
created: 2026-04-16
updated: 2026-04-16
tags: [concept, ai-agents, security, sandbox, index]
depth: L2
status: complete
sources: []
---

# Sandbox: AI Agent Code Execution Isolation

When AI agents execute code, **isolation is the security boundary between useful automation and catastrophic failure**. This section covers all layers of sandboxing in the AI agent ecosystem.

## Four Layers of Sandbox

Isolation exists on a spectrum from full OS-level separation to in-process VM embedding. Each layer trades security for performance and flexibility.

| Layer | Scope | Technologies | Latency | Isolation Mechanism | Best For |
|-------|-------|-------------|---------|-------------------|----------|
| **[[infrastructure]]** | OS/Hypervisor | Docker, Firecracker, gVisor, Kata, Zeroboot, OpenAI Agents SDK Sandboxes (Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel) | 0.8ms - 2s | Kernel namespaces, seccomp, VM boundaries, Harness/Compute separation | Full apps, GPU, multi-tenant |
| **[[js-runtime]]** (Process mode) | OS Process | Bun CLI, Deno CLI, Node.js CLI | 1ms - 100ms | OS process boundary + runtime permissions | Agent CLI tools, TS execution, single-binary distribution |
| **[[in-process]]** | VM/Memory space | Monty (Rust Python VM), Pyodide, QuickJS (embedded), V8 Isolates, WebContainer | 0.004ms - 2.8s | Memory isolation, bytecode VM, capabilities | Simple scripts, data transforms, zero-infra, code-mode |
| **WASM** (emerging) | Browser/Sandbox | WASM + WASI | ~1ms | Capability-based sandbox, no OS access | Edge execution, portable code |

> **Key distinction**: JS runtimes operate in **two modes**. When run as CLI (`bun script.ts`, `deno run app.ts`), they are **process-level isolation** — separate OS processes with their own memory space. When embedded (V8 Isolates in Cloudflare Workers, QuickJS in a C++ agent, WebContainer in a browser), they become **in-process isolation** — sharing the host process but separated by VM memory boundaries.


## The Isolation Spectrum (Infrastructure Layer)

Infrastructure sandboxing spans five isolation levels, each trading performance for security:

1. **Containers** (Docker/Podman) — Fastest (~90ms), lowest overhead, moderate isolation
2. **User-space kernels** (gVisor) — 10-30% I/O overhead, syscall filtering
3. **Micro-VMs** (Firecracker/Kata) — Hardware-level isolation, 125-500ms boot
4. **WebAssembly** — Near-native performance, emerging GPU support
5. **CoW Micro-VMs** (Zeroboot) — 0.79ms spawn, 480x density vs E2B

For detailed platform comparison, see [[infrastructure]].

## Capabilities-Based Security (In-Process Layer)

Monty demonstrates a different philosophy: instead of starting with a full VM and restricting down, **start with nothing and grant capabilities explicitly**.

| Dimension | Traditional Sandbox | Capabilities-Based |
|-----------|-------------------|-------------------|
| Default access | Everything (then restrict) | Nothing (then grant) |
| Attack surface | Large (full OS/container) | Minimal (only exposed functions) |
| Configuration | Complex (Docker flags, network rules) | Simple (function registration) |
| Escape vectors | Kernel exploits, container escapes | None (no kernel access) |
| Best for | Full applications, third-party packages | Scripts, data transforms, code-mode |

For detailed implementation, see [[in-process]].

## JS Runtime Layer (Bun, Deno, Node.js)

JavaScript runtimes form a critical but often overlooked layer of the AI agent stack. Unlike Python's single CPython implementation, the JS ecosystem offers **three competing runtimes** with fundamentally different architectures.

| Runtime | Engine | AI Agent Advantage | Key Fact |
|---------|--------|-------------------|----------|
| **Bun** | JavaScriptCore | 1-10ms cold start, single binary | Acquired by Anthropic (Dec 2025); powers Claude Code |
| **Deno** | V8 | Built-in security, TypeScript-native | Deno Deploy for edge AI agent execution |
| **Node.js** | V8 | Largest npm ecosystem | Foundation of most existing JS-based agents |

The **Anthropic × Bun acquisition** is strategically significant: Claude Code ships as a single Bun executable, and Anthropic now controls the runtime that AI agents depend on. For detailed runtime comparison, see [[js-runtime]].

## Decision Matrix: Which Sandbox for Your Agent?

| Scenario | Recommended Layer | Why |
|----------|------------------|-----|
| Simple data transform Python scripts | **In-Process** (Monty) | 0.004ms start, zero infra |
| Third-party package installation | **Infrastructure** (Docker/E2B) | Full environment support |
| GPU-intensive ML inference | **Infrastructure** (Modal/gVisor) | Native GPU passthrough |
| Multi-tenant SaaS agent platform | **Infrastructure** (Firecracker) | Hardware-level isolation |
| AI agent CLI tool distribution | **Process** (Bun CLI) | Single binary, fast cold start |
| Edge AI agent execution | **In-Process** (V8 Isolates / Deno Deploy) | V8 isolates, global distribution |
| Browser automation agents | **Infrastructure** (Daytona desktop) | Full display environment |
| Local-first AI development | **In-Process** (Monty) | No cloud dependency |

## Related Concepts

- [[harness-engineering]] — Monty as a harness environment (Ryan Lopopolo)
- [[concepts/harness-engineering/system-architecture/agent-security-patterns.md]] — OpenAI's Egress Proxy approach
- [[deep-agents]] — Deep agents consume all sandbox layers
- [[anthropic-managed-agents]] — Brain/Hands/Session separation architecture
- [[jarred-sumner]] — Bun creator, joined Anthropic (Dec 2025)
- [[entities/ryan-dahl.md]] — Node.js and Deno creator
