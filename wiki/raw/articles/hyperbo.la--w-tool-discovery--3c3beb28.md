---
title: "MCP Solves Tool Discovery for LLMs"
url: "https://hyperbo.la/w/tool-discovery/"
fetched_at: 2026-04-29T07:02:15.226121+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# MCP Solves Tool Discovery for LLMs

Source: https://hyperbo.la/w/tool-discovery/

Coding agents like Claude Code and OpenAI Codex don’t struggle with terminals;
they struggle
to discover
tools that exist. If a command isn’t in the
model’s training set or post-training hill climbing, they won’t even know to try
it. MCP fixes discovery by giving models a live, machine-readable catalog of
tools with names, descriptions, input schemas, and example calls.
MCP gives
the models tokens.
Unix pipes and man pages gave humans both composition and discovery. In agentic
systems, LLMs provide composition and MCP gives LLMs discoverability +
affordances.
MCP is the universal plugin interface
, but LLM behavior is
fundamentally driven by, and constrained by, input tokens. MCP offers something
that CLIs ambiently available in
$PATH
(or training data) never could: a
built-in mechanism to automatically prompt the model so it doesn’t have to guess
or hunt for tools.
The CLI your developer productivity team built to accelerate human developers is
illegible to a coding agent.
Agent-first development means prompting the model
from the start — and MCP bakes that into tool authorship.
