---
title: "With — an ergonomics-first systems language"
source_url: https://withlang.org
repo: https://github.com/withlang-dev/with
captured: 2026-11-17
captured_by: x-accounts-scan (@quixiai, Eric Hartford)
type: raw-article
status: scraped
---

# With — an ergonomics-first systems language

> close to the machine, without the suffering

Captured 2026-11-17 from https://withlang.org (landing page, full scrape). Announced
on X the same day by **Eric Hartford** ([@QuixiAI](https://x.com/quixiai)) in a reply
to @ohmypy's "talk me out of releasing an alternative stdlib for C" post — Hartford
pitched With as the answer and asked @ohmypy to help build its standard library,
describing "a really slick system where I mechanically migrate C libraries to with and
then wire up Withy adapters to them."
Source tweet: https://x.com/quixiai/status/2122738133309505750

## Positioning (verbatim from the landing page)

- Tagline: "The systems language that **writes less** so it can prove more."
- "With is native by default, exactly as safe as Rust, and allergic to ceremony. Every
  character the compiler can infer is a character you never type."
- "With pays compiler complexity so you don't pay it in ceremony — the guardrails stay,
  the boilerplate goes."
- Install: `curl -fsSL https://withlang.org/installer/install.sh | sh`, "macOS · Linux ·
  Windows. One binary. No system LLVM required." Claimed "empty folder to native window
  in 28s".

## Three pillars

1. **No ceremony** — "If the compiler can infer, import, bind, prove, or generate it,
   you don't spell it out. No `Ok(())`, no `let _ =`, no trailing return. *Every
   unnecessary character is a compiler failure.*" Return types and locals are inferred
   from the body (`fn shout(s: str): s ++ "!"`).
2. **"Exactly as safe as Rust"** — single ownership, consuming destructors, and
   **generational references**, credited as "the best of Vale" (the Vale language).
   "A resource lives in its scope and is released when the scope ends. **Leaking is a
   defect, not a convenience.**"
3. **C is first-class** — `c_import` a header and call the library directly: "no shim,
   no bindings, no becoming the build system. Raw C stays explicit; modeled C becomes
   humane. **The migrator brings whole libraries across.**"

## Getting-started flow (also a release smoke test)

```
with init spiral      # scaffold with.toml + src/main.w
with get c.raylib     # fetch raylib, read headers, model the C API, link → typed fns
with check src/main.w # ok
with run              # native build; a window opens with a living colored spiral
```

The page states this exact three-command flow is one of With's **release smoke tests**,
run on every published build, rendering the spiral "to verify the pixels actually
appear. The getting-started path can't quietly rot."

Interop sample uses `use c_import("raylib.h")` plus `extern fn sin(x: f64) -> f64`,
with raw C calls wrapped in an explicit `unsafe { … }` block and `.ptr` for C strings.

## Feature list on the page

Inference (return types/locals the body implies), exhaustive pattern matching on tuples
and values, C interop from headers, and ownership ("Owned from creation, released by its
scope"). Every sample is stated to compile and run on the current release.

## Built with With (shipped demos)

- **WIPE: SURVIVAL** — twin-stick survival prototype, With + raylib, native desktop.
  Arena with Gaussian bloom, directional sparks, reactive grid, bass-led ambient house
  soundtrack; automatic fire, one-hit kills, immediate retries; keyboard/mouse or
  twin-stick controller. Published on GitHub with a showcase capture, intended as a
  readable source-to-pixels tour of With's simulation, rendering, shaders, and audio.

## Context: the @ohmypy parent post Hartford is answering

@ohmypy (Nov 17, 07:55 UTC): "I want a high-level standard library for C with powerful
abstractions like those in Go and allocator-based memory management like in Zig. I don't
like Zig's standard library choices, its lack of documentation, and the massive breaking
changes in every release. I don't want to write C bindings in Odin to interact with C
libraries. I don't like that C3 keeps adding features to the language that I don't need.
I don't like Hare's mutable global state everywhere in the stdlib, and the lack of OS
support. I don't want behemoths like C++, Rust, Nim, or D. Please talk me out of
releasing an alternative stdlib for C. No one wants it, right?"
https://x.com/ohmypy/status/2122599554910437790

## Notes / gaps

- Landing page only; the GitHub README was not scraped this run. License, author list,
  release cadence, and compiler implementation language are **unverified**.
- No benchmark or comparison data published on the page — safety claim ("exactly as safe
  as Rust") is a first-party claim, not third-party evaluated.
- Relationship to the Vale language (generational references, consuming destructors) is
  acknowledged on the page but the degree of code/design reuse is not stated.
