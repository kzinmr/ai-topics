---
title: "Mermaid to Unicode box art (grok-mermaid)"
url: "https://simonwillison.net/2026/Jul/16/grok-mermaid/#atom-everything"
fetched_at: 2026-07-16T07:01:38.898418+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Mermaid to Unicode box art (grok-mermaid)

Source: https://simonwillison.net/2026/Jul/16/grok-mermaid/#atom-everything

While
exploring the codebase
for the newly open-sourced Grok CLI coding agent I came across
xai-grok-markdown/src/mermaid.rs
, a "self-contained terminal renderer for Mermaid diagrams" written in Rust.
I figured it would be fun to try that out in a browser via WebAssembly. Here's
the prompt
I ran in Claude Code for web (Fable 5), and this is what the resulting tool looks like:
