---
title: "Claude Code uses Bun written in Rust now"
url: "https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/#atom-everything"
fetched_at: 2026-07-19T07:01:14.957266+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Claude Code uses Bun written in Rust now

Source: https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/#atom-everything

19th July 2026
In
Rewriting Bun in Rust
Jarred Sumner made the following claim:
Claude Code v2.1.181 (released June 17th) and later use the Rust port of Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed. Boring is good.
I decided to have a poke at my own Claude Code installation to see if I could find evidence that it was using Bun written in Rust.
I found these two commands convincing:
strings ~/.local/bin/claude | grep -m1 'Bun v1'
For me this outputs
Bun v1.4.0 (macOS arm64)
. The most recent release of
Bun on GitHub
is currently
v1.3.14
from May 12th, so that v1.4.0 version number in Claude supports them shipping a preview of a not-yet-released Bun version.
strings ~/.local/bin/claude | grep -Eo 'src/[[:alnum:]_./-]+\.rs'
This outputs a list of
563 filenames
, starting with these:
src/runtime/bake/dev_server/mod.rs
src/runtime/bake/production.rs
src/bundler/bundle_v2.rs
It looks like Bun in Rust is indeed being run in production across millions of different devices. Like Jarred said, "Boring is good".
