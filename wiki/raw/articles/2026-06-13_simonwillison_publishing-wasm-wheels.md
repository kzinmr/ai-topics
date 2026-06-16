---
title: "Publishing WASM wheels to PyPI for use with Pyodide"
type: article
source: simonwillison.net
author: Simon Willison
date: 2026-06-13
url: https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/
scraped_at: 2026-06-15T22:30:00Z
---

# Publishing WASM wheels to PyPI for use with Pyodide

The Pyodide 314.0 release announcement (via Hacker News) includes news Simon's been looking forward to for a long time: You can now publish Python packages built for Pyodide (or any Python runtime compatible with the PyEmscripten platform defined in PEP 783) directly to PyPI and install them at runtime.

Previously, the Pyodide maintainers had to maintain, build, and host over 300 packages ourselves. This created a significant burden on maintainers and became a major bottleneck for the community, as every new package required manual review.

Moving forward, package maintainers can simply build and publish Pyodide wheels to PyPI, just as they do for native wheels on Linux, macOS, or Windows.

## Trying it out with luau-wasm

Luau is a "small, fast, and embeddable programming language based on Lua with a gradual type system", developed by Roblox and released under an MIT license. It's written in C++. Simon compiled it to WebAssembly and got it running inside of Pyodide, then used Codex + GPT-5.5 xhigh to package the experiment and publish it to PyPI using GitHub Actions.

The result: luau-wasm is a brand new PyPI package which publishes a 276KB wheel file which can be used in Pyodide. The GitHub repo includes all of the build and deploy scripts (using the latest cibuildwheel) and also deploys an HTML demo page which loads Pyodide, installs luau-wasm and provides an interface for trying it out.

## How many packages are using this so far?

Using BigQuery SQL against PyPI's public dataset, there are currently 28 PyPI packages publishing with the new pyemscripten_202*_wasm32 tags, including: luau-wasm, uuid7-rs, cmm-16bit, pyOpenTTDAdmin, imgui-bundle, numbertoolkit, bashkit, geoarrow-rust-core, arro3-io, arro3-core, arro3-compute, onnx, powerfit-em, tcod, chonkie-core, tokie, robotraconteur, pydantic_core, yaml-rs, cadquery-occ-novtk-OCP.wasm, uuid_utils, base64_utils, pycdfpp, lib3mf-OCP.wasm, typst, toml-rs, onnx-weekly, dummy-pyodide-ext-test.

Key tags: lua, pypi, python, sandboxing, webassembly, github-actions, pyodide
