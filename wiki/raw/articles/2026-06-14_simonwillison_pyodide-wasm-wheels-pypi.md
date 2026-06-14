---
title: "Publishing WASM wheels to PyPI for use with Pyodide"
source_url: "https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/"
date: "2026-06-13"
source_type: blog-post
author: "Simon Willison"
language: en
---

# Publishing WASM wheels to PyPI for use with Pyodide

13th June 2026

The Pyodide 314.0 release announcement (via Hacker News) includes news I've been looking forward to for a long time:

You can now publish Python packages built for Pyodide (or any Python runtime compatible with the PyEmscripten platform defined in PEP 783) directly to PyPI and install them at runtime.

Previously, the Pyodide maintainers had to maintain, build, and host over 300 packages ourselves. This created a significant burden on our maintainers and became a major bottleneck for the community, as every new package required manual review.

Moving forward, package maintainers can simply build and publish Pyodide wheels to PyPI, just as they do for native wheels on Linux, macOS, or Windows.

Here's the PR to PyPI itself supporting this, which landed on April 21st.

I adore Pyodide, and have been frustrated in the past by this limitation. It's possible to compile C or Rust extensions to WASM in a wheel file, but before now there was no easy way to distribute them.

Thanks to the efforts of a whole lot of people, that's now been fixed!

## Trying it out with luau-wasm

I decided to celebrate by finding something I could package. I have quite a few experimental Pyodide projects lying around, but the best fit for this looked to be my Luau WebAssembly research spike from 9th March.

Luau is a "small, fast, and embeddable programming language based on Lua with a gradual type system", developed by Roblox and released under an MIT license.

It's written in C++. I already knew it was possible to compile it to WebAssembly and get it running inside of Pyodide, so I set Codex + GPT-5.5 xhigh the task of packaging my experiment up and publishing it to PyPI using GitHub Actions.

It took some iteration, but here's the result: luau-wasm is a brand new PyPI package which publishes a 276KB luau_wasm-0.1a0-cp314-cp314-pyemscripten_2026_0_wasm32.whl file which can be used in Pyodide like this:

```
import micropip
await micropip.install("luau-wasm")
import luau_wasm
print(luau_wasm.execute(r'''
local animals = {"fox", "owl", "frog", "rabbit"}
table.sort(animals, function(a, b) return #a < #b end)
for i, name in animals do print(i .. ". " .. name .. " (" .. #name .. ")") end
'''))
```

You can run that code in the Pyodide REPL demo to see it in action.

The GitHub repo for luau-wasm includes all of the build and deploy scripts (using the latest cibuildwheel) and also deploys an HTML demo page which loads Pyodide, installs luau-wasm and provides an interface for trying it out: https://simonw.github.io/luau-wasm/

## How many packages are using this so far?

I was curious to see how many packages are currently publishing wheels for this platform.

After some tinkering with ChatGPT I got to this BigQuery SQL which I ran against PyPI's public dataset on BigQuery. Here's the raw JSON of query results and here's a SQLite SQL query in Datasette Lite which dedupes packages by most recent upload date.

If the query is right, there are currently 28 PyPI packages publishing with the new pyemscripten_202*_wasm32 tags:

luau-wasm, uuid7-rs, cmm-16bit, pyOpenTTDAdmin, imgui-bundle, numbertoolkit, bashkit, geoarrow-rust-core, arro3-io, arro3-core, arro3-compute, onnx, powerfit-em, tcod, chonkie-core, tokie, robotraconteur, pydantic_core, yaml-rs, cadquery-ocp-novtk-OCP.wasm, uuid_utils, base64_utils, pycdfpp, lib3mf-OCP.wasm, typst, toml-rs, onnx-weekly, dummy-pyodide-ext-test

Here's hoping we see a whole lot more of those showing up over the coming months and years.
