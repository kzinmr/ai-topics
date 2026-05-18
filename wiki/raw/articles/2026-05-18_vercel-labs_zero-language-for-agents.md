# Zero — The Programming Language for Agents

- **Source:** https://github.com/vercel-labs/zero
- **Homepage:** https://zerolang.ai
- **Created:** 2026-05-15 (Vercel Labs)
- **Latest Release:** v0.1.2 (2026-05-17)
- **License:** Apache 2.0
- **Saved:** 2026-05-18

## Overview

Zero is a systems language designed so humans and AI agents can read, repair, inspect, and ship small native programs together. It keeps effects explicit, memory predictable, and compiler output structured.

Built by Vercel Labs (lead contributor: ctate). Written primarily in C (65.9%).

## Core Design

- **No mandatory GC or event loop** — allocation, cleanup, outside-world access visible in code
- **Capability-based I/O** — functions declare what they touch (`World` capability). Compiler rejects unavailable capabilities at compile time
- **Explicit effects** — `raises` keyword, `check` for fallible operations
- **Local reasoning** — no hidden allocator, implicit async, or magic globals
- **Cross-target checks** — compiler checks target-neutral code for multiple targets
- **C boundary support** — C ABI exports, target-aware interop metadata

## Agent-First Tooling

- `zero check --json` — structured diagnostics with repair metadata (`{"repair": {"id": "declare-missing-symbol"}}`)
- `zero graph --json` — dependency graph facts
- `zero size --json` — artifact size reports
- `zero routes --json` — web handler routes
- `zero doctor --json` — environment diagnostics
- `zero skills get zero --full` — machine-readable skill manifest
- Stable diagnostic codes (NAM003, TAR002, MET001, etc.)

## Language Features

- Braced syntax, no significant whitespace
- `shape` for named records, `enum`/`choice` for tagged unions
- Generics with static value parameters, static interfaces (comptime-constrained)
- Integer types: i8-i64, u8-u64, usize, isize; floats: f32, f64
- No implicit conversions between types
- Compile-time constants with bounded evaluation sandbox
- `meta` reflection facts at compile time
- `match` with exhaustive checking
- Module system with `use` imports
- Package manifests (`zero.json`)
- Built-in test runner (`zero test`)
- Web handlers (routes) support

## Repository Stats
- Stars: 2,045 (as of 2026-05-18)
- Forks: 130
- Open Issues: 43
- Contributors: 1 (ctate)
- Releases: 3 (v0.1.0, v0.1.1, v0.1.2)
