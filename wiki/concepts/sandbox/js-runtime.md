---
title: "JavaScript Runtimes for AI Agents"
created: 2026-04-16
updated: 2026-04-16
tags: [concept, ai-agents, sandboxing, javascript, bun, deno, nodejs, runtime, v8, javascriptcore, process-isolation]
aliases: ["js-runtime", "javascript-runtime-comparison", "bun-deno-node", "agent-js-runtime"]
related: [[concepts/harness-engineering/system-architecture/infrastructure-noise.md]], [[concepts/sandbox/in-process.md]], [[harness-engineering]], [[jarred-sumner]], [[ryan-dahl]]
depth: L2
status: complete
---

# JavaScript Runtimes for AI Agents

JavaScript/TypeScript runtimes form a critical layer of the AI agent stack. Unlike Python's single CPython implementation, the JS ecosystem offers **three competing runtimes** with fundamentally different architectures — each with distinct implications for AI agent execution: startup latency, sandbox security, distribution model, and third-party package support.

## Isolation Model: Process vs In-Process

> **Critical distinction**: JS runtimes operate in **two modes** with different security properties.

| Mode | Example | Isolation Level | Security Boundary |
|------|---------|----------------|-------------------|
| **Process mode** (CLI) | `bun script.ts`, `deno run app.ts`, `node app.js` | OS process isolation | Process boundary + runtime permissions |
| **In-Process mode** (embedded) | V8 Isolates (Cloudflare Workers), QuickJS embedded, WebContainer | Memory/VM isolation | Host application's memory space |

When run as CLI, JS runtimes provide **process-level isolation** — each invocation is a separate OS process. This is NOT in-process isolation like Monty (which embeds a VM directly into the agent's memory space). However, when JS engines are **embedded** (V8 Isolates, QuickJS as a library), they become true in-process sandboxes.

### Deno's Capability-Based Permissions (Process Mode)
Deno bridges the gap between process isolation and capabilities-based security:
- `--allow-read`, `--allow-net`, `--allow-env` flags restrict what the process can access
- Even though it runs as a separate OS process, **the runtime itself enforces capability boundaries**
- This is the closest JS ecosystem equivalent to Monty's philosophy

### V8 Isolates (In-Process Mode)
Cloudflare Workers and Deno Deploy use V8 Isolates — multiple scripts running within a single V8 engine instance:
- **Cold start**: ~1ms (no process fork needed)
- **Memory isolation**: Each isolate gets its own heap, but shares the V8 instance
- **Security**: If one isolate escapes, it compromises the entire V8 process
- **Density**: Thousands of isolates per machine vs dozens of processes

### WebContainer (Browser In-Process Mode)
StackBlitz's WebContainer runs Node.js-compatible code entirely inside the browser:
- **Isolation**: Browser's same-origin policy + WebAssembly sandbox
- **No server needed**: Runs client-side with full npm compatibility
- **Best for**: AI agents that need to execute code in the user's browser context

> **"AI agents need to distribute tools to each other. They need to run code in sandboxed environments. They need to install dependencies fast, run tests fast, execute code fast — all without human intervention. Bun solves every single one of these problems."** — Jarred Sumner, Bun founder, on why Bun joined Anthropic

## Three Runtimes, Two Engines

| Dimension | **Node.js** | **Deno** | **Bun** |
|-----------|------------|----------|---------|
| **Creator** | Ryan Dahl (2009) | Ryan Dahl (2018) | Jarred Sumner (2022) |
| **Engine** | V8 (Google) | V8 (Google) | JavaScriptCore (Apple) |
| **Language** | C++ | Rust | Zig |
| **Module System** | npm (CommonJS + ESM) | URL + npm (ESM-first) | npm (CommonJS + ESM) |
| **Single Binary** | No (needs node_modules/) | No (needs node_modules/) | **Yes** (self-contained executable) |
| **Built-in Tooling** | Minimal (npm is external) | fmt, lint, test, bench | Bundler, test runner, package manager |
| **Startup Time** | ~50-100ms | ~50-100ms | **~1-10ms** (4x faster than V8) |
| **Cold Start (Agent)** | Moderate | Moderate | **Best** (critical for agent spawning) |
| **Acquired By** | Joyent → OpenJS Foundation | — | **Anthropic (Dec 2025)** |
| **AI Agent Usage** | OpenAI Codex CLI, many agents | Deno Deploy (edge agents) | **Claude Code, Claude Agent SDK, FactoryAI, OpenCode** |

## Engine Architecture: V8 vs JavaScriptCore

The engine choice is the single biggest architectural difference — and it directly impacts AI agent workflows.

### V8 (Node.js, Deno)
- **Strengths**: Largest ecosystem, best JIT optimization for long-running workloads, full Node.js API compatibility
- **Weaknesses**: Heavy memory footprint (~30-50MB idle), slower cold start (~50-100ms), large binary (~60MB+)
- **Agent Impact**: V8's warm-up time matters when spawning hundreds of short-lived agent tasks

### JavaScriptCore (Bun)
- **Strengths**: 4x faster startup, 2-3x lower memory usage, smaller binary (~10MB), faster cold compilation
- **Weaknesses**: Historically weaker JIT for long-running compute, smaller community
- **Agent Impact**: JSC's fast cold start is ideal for **ephemeral agent execution** — spawn a process, run code, exit

> *"JavaScriptCore seems to start around 4x faster [than V8]. So after about a month of reading WebKit's source code trying to figure out how to embed JavaScriptCore..."* — Jarred Sumner

## Why Runtime Matters for AI Agents

### 1. Single-Binary Distribution (Bun's Key Advantage)

Bun compiles to a single executable with all dependencies bundled. This is transformative for agent tooling:

```
Traditional (Node.js):  agent_env/
                        ├── node (30MB)
                        ├── node_modules/ (500+ files, 100MB+)
                        ├── package.json
                        └── script.js
                        → 600+ files, ~150MB to distribute

Bun:                    bun-executable (10MB single file)
                        → 1 file, ~10MB to distribute
```

**Claude Code ships as a single Bun executable** to millions of developers across macOS, Linux, and Windows. No `npm install`, no `node_modules/`, no dependency resolution at install time.

### 2. Cold Start Latency (Agent Spawning)

When an AI orchestrator spawns multiple agent tasks (the "agentic swarm" pattern), each new process pays cold start cost:

| Scenario | Node.js | Deno | Bun |
|----------|---------|------|-----|
| Single script start | 50-100ms | 50-100ms | **1-10ms** |
| With 100 node_modules packages | 200-500ms | 200-500ms | **~10ms** (bundled) |
| 100 concurrent agent spawns | 20-50s total | 20-50s total | **1-2s total** |

For harness engineering patterns (Ryan Lopopolo) where agents are spawned, tested, and discarded rapidly, **Bun's startup advantage compounds**.

### 3. Sandbox Compatibility

| Runtime | Sandbox Compatibility | Notes |
|---------|----------------------|-------|
| Node.js | Docker, Firecracker, gVisor | Mature, well-understood |
| Deno | Built-in permissions, Docker | `--allow-read`, `--allow-net` flags; designed for sandboxing |
| Bun | Docker, Monty (future), in-process | Small binary = easier to embed in in-process sandboxes |

**Deno** was designed from the start with security in mind — it has a built-in capability-based permissions model (`deno run --allow-read script.ts`). This aligns closely with Monty's capabilities-based security philosophy.

**Bun** is not security-focused by default, but its small binary size and single-file distribution make it attractive for embedding in sandbox environments.

### 4. TypeScript-First Agents

All three runtimes now support TypeScript natively, but with different maturity:

| Runtime | TS Support | Mechanism |
|---------|-----------|-----------|
| Node.js | Via ts-node, tsx, or manual compilation | External tooling required |
| Deno | **Native** | Built-in TypeScript compiler (swc-based) |
| Bun | **Native** | Built-in TypeScript support, no configuration needed |

For AI agents that generate TypeScript code on-the-fly, **Bun and Deno eliminate the transpilation step** — code is ready to execute immediately.

## Anthropic's Bun Acquisition (December 2025)

This is the most significant event in the JS runtime + AI agent space. Anthropic acquired Oven (Bun's company) for several strategic reasons:

1. **Claude Code depends on Bun** — ships as a Bun executable to millions of users
2. **Runtime control** — Anthropic can now optimize Bun specifically for AI agent workloads
3. **Single-binary distribution** — critical for distributing AI tools without dependency hell
4. **Cold start performance** — JSC's fast startup matters for ephemeral agent tasks
5. **Vertical integration** — analogous to Chrome ↔ V8 relationship; Anthropic ↔ Bun

> *"Anthropic's first acquisition: a JavaScript runtime. [...] The team building the runtime will have direct insight into how AI agents use JavaScript. They'll build features for AI-native development before anyone else knows those features are needed."*

### What Changed for Claude Code

| Before Acquisition | After Acquisition |
|-------------------|-------------------|
| Bun is a third-party dependency | Bun is an Anthropic product |
| Risk: Bun funding/sustainability | Guaranteed: Anthropic backs Bun |
| Bun optimized for general JS | Bun optimized for **AI agent workloads** |
| Claude Code uses Bun passively | Claude Code team and Bun team collaborate directly |

Bun reached **7.2M monthly downloads** (Oct 2025, +25% MoM) around the time of the acquisition.

## Deno's Position in the AI Agent Ecosystem

Ryan Dahl created Deno in 2018 to fix Node.js's design mistakes. Deno has carved out a niche in AI agent infrastructure:

- **Deno Deploy**: Edge computing platform where AI agents can run globally distributed
- **Built-in security model**: `--allow-read`, `--allow-net`, `--allow-env` — capability-based permissions from day one
- **TypeScript native**: No transpilation needed for agent-generated TS code
- **Fresh framework**: Deno's web framework designed for edge AI agents

Deno's philosophy — *"secure by default, TypeScript-first, single executable"* — is closest to the **capabilities-based security** model that Monty represents for Python.

## Decision Matrix: Runtime Selection for AI Agents

| Use Case | Recommended Runtime | Why |
|----------|-------------------|-----|
| Claude Code ecosystem | **Bun** | Native integration, single-binary distribution |
| Claude Agent SDK tools | **Bun** | Fast spawning, bundled distribution |
| Edge AI agents | **Deno** | Deno Deploy, built-in security |
| npm ecosystem compatibility | **Node.js** | Largest package ecosystem |
| Agent security-first | **Deno** | Built-in capability permissions |
| Fast test execution | **Bun** | 197x faster than babel, built-in test runner |
| Multi-tenant agent platform | **Bun** or **Deno** | Small binary, isolation-friendly |
| Python-first agents | Monty (in-process) | Not a JS runtime, but relevant for comparison |

## Timeline

| Date | Event |
|------|-------|
| 2009 | Ryan Dahl creates Node.js (V8-based) |
| 2018 | Ryan Dahl creates Deno (Rust + V8, security-first) |
| 2021 | Jarred Sumner starts building Bun (Zig + JavaScriptCore) |
| 2022-07 | Bun v0.1.0 released |
| 2024-late | AI coding tools go from "demo" to "useful" |
| 2025-10 | Bun reaches 7.2M monthly downloads (+25% MoM) |
| 2025-12 | **Anthropic acquires Bun/Oven** |
| 2026-02 | Bun v1.3.x with JavaScriptCore upgrades (JSPI, LOL JIT tier) |
| 2026-03 | Claude Code hits $1B annual run rate; ships as Bun executable |

## Related

- [[concepts/harness-engineering/system-architecture/infrastructure-noise.md]] — Container, microVM, and edge-level isolation
- [[concepts/sandbox/in-process.md]] — Monty, capabilities-based security (Python)
- [[harness-engineering]] — Runtime as a harness environment
- [[ryan-dahl]] — Creator of Node.js and Deno
- [[jarred-sumner]] — Creator of Bun, joined Anthropic

## Sources

- [Bun Joins Anthropic — Official Blog Post](https://bun.com/blog/bun-joins-anthropic)
- [Anthropic Just Bought Bun — And JavaScript Will Never Be the Same (dev.to)](https://dev.to/harsh2644/anthropic-just-bought-bun-and-javascript-will-never-be-the-same-2mg9)
- [Bun GitHub Repository](https://github.com/oven-sh/bun)
- [Deno Official Site](https://deno.com/)
- [Node.js Official Site](https://nodejs.org/)
- [WebKit/JavaScriptCore PR #26922](https://github.com/oven-sh/bun/pull/26922)
- [Ryan Dahl: 10 Things I Regret About Node.js (JSConf 2018)](https://www.youtube.com/watch?v=M3BM9TB-8yA)
