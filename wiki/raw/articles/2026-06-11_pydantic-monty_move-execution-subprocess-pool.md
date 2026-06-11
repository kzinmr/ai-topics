---
source_url: https://github.com/pydantic/monty/pull/500
title: "Move execution to a subprocess pool (Monty PR #500)"
date: 2026-06-11
source_slug: pydantic-monty
author: Samuel Colvin
x_referrer: samuelcolvin
state: open
additions: 25642
deletions: 17879
changed_files: 158
---

# Move execution to a subprocess pool

**PR #500** — [pydantic/monty](https://github.com/pydantic/monty/pull/500)
**Author:** Samuel Colvin (@samuelcolvin)
**Created:** 2026-06-11
**State:** Open
**Stats:** +25,642 / -17,879 lines across 158 files

## Summary

Run Monty in crash-isolated worker subprocesses via a new protobuf protocol and pool APIs for Python and Node.js. Crashes kill only a worker, not the host process.

## New Features

- Added `monty-proto`: protobuf schema with checked-in prost output, 4-byte LE framing, and safe conversions.
- Added `monty --subprocess` mode: turn-based child process that streams `print`, handles child-local mounts, and cleanly reports fatal errors.
- Added `monty-pool`: elastic worker pool with prewarming, crash detection/replacement, and a watchdog enforcing per-request timeouts.
- Python API now uses pools and sessions: `Monty`/`AsyncMonty` → `pool.checkout(...).feed_run(code, ...)`, supports coroutine callbacks, streamed prints, and raises `MontyCrashedError` on worker death.
- Rebuilt `@pydantic/monty` as a pure TypeScript client: spawns `monty` subprocess workers over the same protocol, provides a `Monty` pool with `checkout().feedRun(...)`, streamed prints, async external functions, and `MontyCrashedError`. Platform npm packages ship the `monty` binary; the client auto-resolves it or accepts `binaryPath`.
- New `pydantic-monty-cli` package ships the `monty` binary; CI enforces proto sync (`make check-proto`) and Makefile adds proto generate/check targets.

## Migration

### Python: replace direct `.run()`/`.run_async()` with session calls
- Before: `m = pydantic_monty.Monty(code, ...) ; m.run(...)`
- Now: `with Monty() as pool: with pool.checkout(script_name=..., type_check=..., type_check_stubs=...) as s: s.feed_run(code, inputs=..., external_functions=...)`
- Async: `async with AsyncMonty() as pool: async with pool.checkout() as s: await s.feed_run(...)`

### Node.js: replace in-process runs with the pool API
- Before: `new Monty(code, opts).run({ inputs, externalFunctions })`
- Now: `const pool = await Monty.create(); const s = await pool.checkout({ scriptName, typeCheck, typeCheckStubs }); const out = await s.feedRun(code, { inputs, externalFunctions, printCallback });`
- The N-API binding is removed; the package is now a subprocess client. Errors map to `MontySyntaxError`/`MontyRuntimeError`/`MontyTypingError`, with `MontyCrashedError` on worker death.

### Other changes
- Script metadata and type-checking move to `checkout(...)` args (`type_check`, `type_check_stubs`, `script_name`).
- The `monty` binary is resolved automatically via `pydantic-monty-cli` (Python) or platform npm packages (Node); override with `MONTY_BIN`/`binaryPath` if needed.
- Legacy REPL/snapshot APIs and serialization modules were removed in favor of pool sessions; adjust imports and calls accordingly.
