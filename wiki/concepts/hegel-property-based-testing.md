---
title: Hegel (Property-Based Testing Protocol and Libraries)
type: concept
aliases: [hegel-pbt, hegel-go, hegel-property-based-testing]
created: 2026-05-21
updated: 2026-05-21
status: active
sources:
  - https://github.com/hegeldev/hegel-go
  - https://hegel.dev/
  - https://pkg.go.dev/hegel.dev/go/hegel
  - https://antithesis.com/blog/2026/hegel/
  - raw/articles/2026-04-07_drmaciver_hegel-go-github.md
  - raw/articles/2026-04-07_drmaciver_hegel-go-pkg.md
tags:
  - concept
  - testing
  - developer-tooling
  - framework
  - protocol
  - formal-methods
  - go
  - open-source

---

# Hegel: Universal Property-Based Testing Protocol

Hegel is a **universal property-based testing protocol and family of language-specific libraries**, built on the [[concepts/property-based-testing|Hypothesis]] engine. Created by [[entities/drmaciver|David R. MacIver]], Liam DeVoe, and the team at [[entities/antithesis|Antithesis]], Hegel brings Hypothesis-quality property-based testing to Go, Rust, C++, and TypeScript.

## Definition

Hegel is a **language-agnostic protocol** that enables property-based testing in any language with an SDK. A Python-based server component (**hegel-core**) handles test generation and shrinking — the same engine that powers Hypothesis — while language-specific client SDKs communicate with it over a compact binary protocol via Unix socket. This architecture lets Go, Rust, C++, and TypeScript developers get the full power of Hypothesis's generation and shrinking without reimplementing it in their language.

> Hegel generates random inputs for test functions, then **shrinks any counterexample down to the smallest case that still triggers the failure**. Unlike traditional fuzz testing, it understands structure: developers tell Hegel what kind of data to produce, and Hegel handles the rest.

## Key Features

| Feature | Description |
|---------|-------------|
| **Protocol-based architecture** | Core engine in Python (hegel-core), language SDKs as thin clients over Unix socket binary protocol |
| **Minimal failing examples** | Shrinks counterexamples to simplest possible reproducer — the defining feature inherited from Hypothesis |
| **Structured input generation** | Generates typed, structured inputs (not raw bytes) — understands lists, integers, strings, custom types |
| **Auto-install backend** | SDKs auto-install `hegel-core` via `uv` on first use (private copy to `~/.cache/hegel` if `uv` not on PATH) |
| **Go-native testing** | Integrates with `go test` — no special test runner needed |
| **Multi-language** | Go (v0.3.4), Rust, C++, TypeScript SDKs available or in development |
| **Beta, with compatibility commitment** | Currently beta; breaking changes possible per [hegel.dev/compatibility](https://hegel.dev/compatibility) |
| **Open source** | MIT license, 48 stars, 6 contributors on GitHub |

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Go SDK     │     │  Rust SDK   │     │  C++/TS SDK │
│ (hegel-go)  │     │ (hegel-rs)  │     │  (upcoming) │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                  Unix Socket / Binary Protocol
                           │
                  ┌────────┴────────┐
                  │   hegel-core    │
                  │  (Python proc)  │
                  │ ─────────────── │
                  │ • Generation    │
                  │ • Shrinking     │
                  │ • Hypothesis    │
                  │   engine        │
                  └─────────────────┘
```

The **hegel-core** server is automatically installed and managed by each language SDK. The client-server separation means the Go/Rust/C++/TS SDKs remain thin, while all the sophisticated test generation and shrinking logic stays in the battle-tested Hypothesis Python codebase.

## Hegel Go SDK

The Go SDK (`hegel.dev/go/hegel`, v0.3.4, MIT license) is the most mature language binding.

**Installation:**
```bash
go get hegel.dev/go/hegel@latest
```

**Key API:**
| Function | Description |
|----------|-------------|
| `hegel.Case(fn)` | Wrap a test function for property-based testing |
| `hegel.Draw(ht, generator)` | Draw a random value from a generator inside a test |
| `hegel.Lists(gen)` | Generator for slices of values |
| `hegel.Integers(min, max)` | Generator for integers in range |
| `hegel.WithTestCases(n)` | Option: set number of test cases (default: 100) |
| `ht.Fatalf(...)` | Signal a failing test case (triggers shrinking) |

**Example — detecting a deduplication bug:**
```go
import (
    "math"
    "slices"
    "testing"
    "hegel.dev/go/hegel"
)

func mySort(ls []int) []int {
    result := make([]int, len(ls))
    copy(result, ls)
    slices.Sort(result)
    result = slices.Compact(result) // BUG: drops duplicates!
    return result
}

func TestMatchesBuiltin(t *testing.T) {
    t.Run("matches builtin", hegel.Case(func(ht *hegel.T) {
        slice1 := hegel.Draw(ht, hegel.Lists(hegel.Integers(math.MinInt, math.MaxInt)))
        slice2 := mySort(slice1)
        slices.Sort(slice1)
        if !slices.Equal(slice1, slice2) {
            ht.Fatalf("slices not equal: %v != %v", slice1, slice2)
        }
    }))
}
```

Run with `go test` as normal. Hegel generates 100 random integer lists and finds the minimal failing counterexample:

```
Draw 1: [0 0]
    example_test.go:25: slices not equal: [0 0] != [0]
```

The minimal failing case (`[0, 0]`) reveals that `mySort` incorrectly drops duplicates via `slices.Compact`.

## Relationship to Hypothesis

Hegel is **not a rewrite** — it's a **protocol extension** of Hypothesis. The hegel-core server runs Hypothesis's Python engine under the hood. Key differences:

| Aspect | Hypothesis (Python) | Hegel |
|--------|-------------------|-------|
| **Language** | Python only | Go, Rust, C++, TypeScript |
| **Architecture** | In-process Python library | Client-server protocol (Unix socket) |
| **Test runner** | pytest, unittest | Native: `go test`, `cargo test`, etc. |
| **Generation engine** | Hypothesis Python | Same Hypothesis Python via hegel-core |
| **Shrinking** | Hypothesis shrinker | Same Hypothesis shrinker |

MacIver has expressed hope that future models will be good enough to port Hypothesis to Rust for hegel-core, eliminating the Python dependency. For now, the Python dependency is transparently managed via `uv`.

## Development Philosophy (AI-Assisted)

Hegel is developed with heavy [[entities/claude-code|Claude Code]] usage — MacIver reports ~90% of code is first-drafted by Claude. However, this is explicitly **not "vibe coding"**:

- **MacIver designed the Hegel protocol himself**; early attempts to let Claude design it failed (Claude decided the spec was "too complicated" and shoved all messages down a single control stream)
- **Two human reviews per PR**: the author first, then a second colleague
- **100% branch coverage enforced** via ratchet script — no untested code allowed in an AI-assisted project
- Claude frequently resists coverage requirements, writes slop tests, and tries to lower targets — human vigilance is required

See: [[entities/drmaciver#Blog and Recent Posts]]

## Supported Languages

| Language | SDK | Status | Package |
|----------|-----|--------|---------|
| **Go** | hegel-go | Beta, v0.3.4 | `hegel.dev/go/hegel` |
| **Rust** | hegel-rs | Beta | `hegel` crate |
| **C++** | hegel-cpp | In development | — |
| **TypeScript** | hegel-ts | In development | — |

## Related Concepts

- [[concepts/property-based-testing]] — The testing paradigm Hegel implements across languages
- [[concepts/agentic-pbt]] — Anthropic's autonomous PBT agent, built on the same Hypothesis engine
- [[concepts/test-case-minimization]] — The shrinking algorithm that produces minimal failing examples
- [[concepts/formal-methods]] — Related verification approach: contracts and invariants
- [[entities/drmaciver]] — Creator of Hypothesis and Hegel protocol designer
- [[entities/antithesis]] — Company behind Hegel, deterministic simulation testing
- [[entities/claude-code]] — The AI coding agent used to write ~90% of Hegel's code
- [[concepts/vibe-coding-vs-agentic-engineering]] — Hegel exemplifies design-led, test-verified AI-assisted development
- [[concepts/coding-agents/ai-coding-reliability]] — The 100% coverage philosophy applied to AI-generated code

## Sources

- [GitHub: hegeldev/hegel-go](https://github.com/hegeldev/hegel-go) — Go SDK repository (48★, MIT)
- [hegel.dev](https://hegel.dev/) — Official Hegel documentation
- [pkg.go.dev: hegel.dev/go/hegel](https://pkg.go.dev/hegel.dev/go/hegel) — Go package docs, v0.3.4
- [How I've been using Claude Code](http://drmaciver.com/2026/04/how-ive-been-using-claude-code/) — MacIver on Hegel's AI-assisted development
- [Antithesis: Introducing Hegel](https://antithesis.com/blog/2026/hegel/) — Official announcement
- [raw/articles/2026-04-07_drmaciver_hegel-go-github.md](raw/articles/2026-04-07_drmaciver_hegel-go-github.md)
- [raw/articles/2026-04-07_drmaciver_hegel-go-pkg.md](raw/articles/2026-04-07_drmaciver_hegel-go-pkg.md)
