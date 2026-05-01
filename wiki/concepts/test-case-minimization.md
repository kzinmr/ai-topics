---
title: "Test Case Minimization"
tags: [testing]
created: 2026-04-24
updated: 2026-04-24
type: concept
---

# Test Case Minimization

## Overview

**Test case minimization** is the process of finding the smallest possible test case that still reproduces a bug. This technique is essential for efficient debugging, especially in property-based testing and formal verification contexts.

This article describes a minimal property-based testing (PBT) library in ~256 lines of Zig that uses **binary search on entropy size** to automatically minimize failing test cases.

## Core Concept: FRNG (Finite Random Number Generator)

The key innovation is using a **pre-generated, finite PRNG** where all random bytes are consumed upfront. This enables measuring test complexity by tracking entropy consumption.

```zig
const FRNG = @This();
entropy: []const u8,
pub const Error = error{OutOfEntropy};

pub fn init(entropy: []const u8) FRNG {
    return .{ .entropy = entropy };
}
```

**Why finite?** When entropy runs out, the test naturally terminates. This gives a direct measure of test complexity.

## Random Generation API

The library provides:
- `bytes(size)` — Consume N random bytes
- `int(Int: type)` — Generate integer with proper endianness handling
- `int_inclusive(max)` — Unbiased range generation using `mulWide` to avoid modulo bias
- `weighted(weights)` — Reflection-based weighted random field selection

### Key Implementation: Unbiased Range Generation

> Simple modulo (`x % (max + 1)`) produces biased results. The implementation uses `mulWide` for proper distribution.

```zig
pub fn int_inclusive(frng: *FRNG, Int: type, max: Int) Error!Int {
    // Uses std.math.mulWide to avoid modulo bias
    // Handles edge cases for unbiased random generation
}
```

## The Key Insight: Binary Search on Entropy

> "The amount of entropy in FRNG defines the complexity of the test."

If a 16KiB entropy slice causes a failure:
1. Try 8KiB — does it still fail?
2. If not, try 12KiB?
3. **Binary search** for the minimal failing size

### Why This Works

- **Smaller examples are rarer** — easier to find when searching randomly
- **No mutation needed** — fresh random generation often finds smaller failures
- **Universal applicability** — works for any system, not just distributed systems

## The Searcher: Process Isolation

Since crashes don't unwind in Zig, the search runs in a **separate process**:

### Reproducing a Run

Only **two numbers** needed to reproduce any test:
- `size`: entropy length
- `seed`: random seed for entropy generation

### Binary Search Algorithm

```
Start: size=16, step=16, pass=true

Phase 1 (expand): Double step until failure found
 - size += step while pass
 - Double step each iteration

Phase 2 (refine): Halve step to find minimum
 - size -= step while still failing
 - Halve step each iteration
```

## Two Operation Modes

| Mode | Purpose |
|------|---------|
| `replay` | Reproduce a specific failure given size/seed |
| `search` | Binary search for minimal failing case |

## Related Concepts

- [[concepts/agentic-pbt]] — Agentic property-based testing
-  — Test harnesses for LLM evaluation- [[concepts/harness-engineering/agentic-workflows/first-run-the-tests]] — Test-first development patterns

## References

- [matklad.github.io: 256 Lines or Less: Test Case Minimization](https://matklad.github.io/2026/04/20/test-case-minimization.html)