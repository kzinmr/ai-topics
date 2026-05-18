---
title: Zero (Programming Language)
type: entity
aliases: [zerolang, zero-lang]
created: 2026-05-18
updated: 2026-05-18
tags:
  - programming-language
  - open-source
  - company
  - agentic-engineering
  - agent-ergonomics
  - coding-agents
  - tool
  - developer-tooling
sources: [raw/articles/2026-05-18_vercel-labs_zero-language-for-agents.md, https://github.com/vercel-labs/zero, https://zerolang.ai]
---

# Zero — The Programming Language for Agents

**Zero** is an experimental systems programming language by **Vercel Labs**, designed from the ground up for human-AI agent collaboration. Launched May 15, 2026 (v0.1.0), it directly addresses many of the agent-oriented language design principles articulated in [[entities/armin-ronacher|Armin Ronacher's]] "A Language For Agents" essay and complements [[concepts/agent-ergonomics]] theory.

- **Repository:** [vercel-labs/zero](https://github.com/vercel-labs/zero)
- **Homepage:** [zerolang.ai](https://zerolang.ai)
- **License:** Apache 2.0
- **Lead:** ctate (sole contributor as of May 2026)
- **Implementation:** C (65.9%), JavaScript (27.9%), Shell (5.6%)
- **Stats:** 2,045★ | 130 forks | 3 releases (v0.1.2 latest)

## Design Philosophy

> *"A systems language designed so humans and AI agents can read, repair, inspect, and ship small native programs together."*

Zero's tagline embodies the agent ergonomics thesis: **language tooling must serve both human and agent consumers equally**, with structured, machine-readable output as a first-class design goal — not an afterthought.

### Core Design Principles

| Principle | Implementation |
|-----------|---------------|
| **Explicit effects** | `raises` keyword, `check` for fallible ops, `World` capability |
| **Capability-based I/O** | Functions declare what they touch; unavailable capabilities rejected at compile time (`TAR002`) |
| **No hidden runtime** | No mandatory GC, no event loop, no implicit allocator |
| **Structured compiler output** | JSON diagnostics with repair metadata; graph, size, routes all JSON-queryable |
| **Local reasoning** | Function signatures expose fallibility and capabilities; no magic globals |
| **Braced syntax** | No significant whitespace — aligned with agent token efficiency needs |
| **No macros** | Generics + static interfaces instead; produces recognizable patterns |

## Agent-First Tooling

Zero's CLI serves dual audiences through structured output:

```bash
zero check --json     # {"ok": false, "diagnostics": [{"code": "NAM003", "repair": {"id": "declare-missing-symbol"}}]}
zero graph --json     # Dependency graph as structured data
zero size --json      # Artifact size breakdown
zero routes --json    # Web handler route table
zero doctor --json    # Environment diagnostics
zero skills get zero --full  # Machine-readable skill manifest
```

- **Diagnostic codes are stable** (`NAM003`, `TAR002`, `MET001`, `STC001`, `IFC001`, etc.) — agents can rely on them programmatically
- **Repair metadata** is embedded in diagnostics — agents receive fix plans, not just error messages
- **Humans read messages, agents read JSON** — same CLI, dual output paths

## Language Features

### Entry Point & Effects
```zero
pub fun main(world: World) -> Void raises {
    check world.out.write("hello from zero\n")
}
```

- `World` is a capability object, not a global singleton
- `raises` declares fallibility; `check` handles fallible calls
- Targets can reject unavailable capabilities at compile time

### Data Modeling
```zero
shape Point { x: i32, y: i32 }           # Named records
enum Status { ready, failed }             # Discriminated unions (no payload)
choice Result { ok: i32, err: String }    # Tagged unions with payloads

match result {
    .ok => value { ... }                  # Exhaustive matching required
    .err => message { ... }
}
```

### Type System
- **Integers:** `i8`–`i64`, `u8`–`u64`, `usize`, `isize`
- **Floats:** `f32`, `f64` (no implicit mixing with integers)
- **`char`** — byte-sized, does not cast to/from integers
- **`Bool`** — no truthy integers
- **No implicit conversions** between any types
- **Explicit casts** with `as` (integer-to-integer only)

### Generics & Compile-Time
```zero
fun identity<T>(value: T) -> T { return value }          // Monomorphized generics
shape FixedVec<T, static N: usize> { ... }                // Static value parameters
interface Readable<T> { fun read(self: ref<T>) -> i32 }   // Compile-time constraints
```

Compile-time constants (`const`) run in a bounded evaluation sandbox — no filesystem, network, or environment access. `meta` facts expose target info at compile time.

### Module System
```zero
use std.codec        # Package-qualified imports (grep-able!)
use std.parse
```

Packages use `zero.json` manifests with explicit target declarations.

### Web Handlers
Zero supports web route definitions queryable via `zero routes --json`.

## Relationship to Agent Ergonomics Theory

Zero is the **first language to directly implement Armin Ronacher's eight agent-language design principles** in a coherent package:

| Ronacher's Principle | Zero's Implementation |
|---------------------|----------------------|
| 1. Context without LSP | JSON diagnostics work without editor tooling |
| 2. Braced syntax | `{}` blocks, no significant whitespace |
| 3. Explicit flow context | `World` capability + `raises` keyword |
| 4. Results over exceptions | `check` + `raises` + `choice` types |
| 5. Minimal diffs | Braced syntax, explicit types = stable formatting |
| 6. Grep-ability | `use std.codec` — package-qualified imports |
| 7. Local reasoning | Signature declares all effects and capabilities |
| 8. Dependency-aware builds | Package manifests, explicit targets |

This is a remarkable validation of the agent-ergonomics thesis: within 3 months of Ronacher's essay, Vercel shipped a language that checks nearly every box.

## Current Status

- **Experimental** — language is still changing, not production-stable
- **v0.1.2** (May 17, 2026) — 3 releases in first 2 days
- Single contributor, but rapid iteration
- Growing community interest (2,045 stars in 3 days)

## Related
- [[entities/armin-ronacher]] — Author of "A Language For Agents" — Zero implements his design principles
- [[concepts/agent-ergonomics]] — Agent-oriented language design theory
- [[entities/vercel]] — Vercel Inc., the company behind Zero
- [[concepts/programming-languages]] — Broader programming language design
