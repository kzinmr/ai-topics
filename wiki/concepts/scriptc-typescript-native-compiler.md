---
title: scriptc — TypeScript-to-Native Compiler (Vercel Labs)
type: concept
created: 2026-10-03
updated: 2026-10-03
tags:
  - developer-tooling
  - programming-language
  - vercel
sources:
  - https://github.com/vercel-labs/scriptc
  - https://x.com/ctatedev/status/2105429831273902560
related:
  - entities/vercel-labs
  - entities/chris-tate
  - concepts/agent-first-design
---

# scriptc — TypeScript-to-Native Compiler

**scriptc** is an experimental compiler from [[entities/vercel-labs|Vercel Labs]] that compiles TypeScript and JavaScript into **native executables** and **WebAssembly**. It uses TypeScript's type information to lower supported code directly to native instructions, so static builds run **without Node.js or any JavaScript engine**. Announced publicly in late September 2026 by Vercel engineer [[entities/chris-tate|Chris Tate]] (`@ctatedev`).

## What it does

- Compiles TypeScript/JavaScript → standalone native executables and WebAssembly modules.
- Static builds have no runtime dependency on Node.js or a JS engine.
- For `npm` dependencies and fully-dynamic (`any`-typed) code, `--dynamic` embeds the **quickjs-ng** engine; dependency JavaScript is bundled at build time.
- Uses TypeScript type information to drive native codegen — the type system is the compiler's front-end signal.

## Installation & usage

- Install: `npm install -g scriptc` (requires Node.js 24+ for installation only; the *compiled output* needs no Node).
- Standalone compiler archives are shipped via GitHub Releases; native compile+run requires a platform linker and SDK/sysroot.
- Run in one step: `scriptc run hello.ts`
- Build a standalone binary: `scriptc build hello.ts -o hello` then `./hello`
- Coverage check: `scriptc coverage hello.ts` reports how much of a project is on the statically-compilable path.

## Self-hosting milestone (Sep 30, 2026)

On 2026-09-30 Tate announced that **scriptc now compiles itself** — the compiler that turns TypeScript into native executables can now turn its *own* TypeScript source into a native executable. This is the classic compiler self-hosting bootstrap signal, here applied to a typed-language-to-native pipeline rather than a hand-written bootstrap.

## Limitations

scriptc is explicitly **experimental** and supports only a **subset** of JavaScript, TypeScript, and Node.js APIs. The repo directs users to the limitations doc and Node.js compatibility reference before applying it to an existing project.

## Significance

scriptc extends Vercel Labs' bet on **agent-first / performance-native tooling** alongside the Zero language ([[concepts/agent-first-design]]). A native, engine-free TypeScript runtime path is relevant to AI agents that ship or execute generated code where a full Node runtime is heavyweight (sandboxes, edge, CI, small containers).

## Related

- [[entities/vercel-labs]] — parent R&D division (also ships Zero, fx)
- [[entities/chris-tate]] — Vercel engineer, lead public voice on scriptc
- [[concepts/agent-first-design]] — design philosophy behind Vercel Labs tooling
