---
title: "Release: datasette-llm 0.1a8"
source_url: "https://simonwillison.net/2026/May/19/datasette-llm/"
blog: "simonwillison.net"
date: "2026-05-19"
published: "2026-05-19"
description: "LLM integration plugin for other plugins to depend on"
ingested: "2026-05-20"
---

# Release: datasette-llm 0.1a8

**Date**: 19th May 2026

**Source**: [Simon Willison's Weblog](https://simonwillison.net/2026/May/19/datasette-llm/)

Release datasette-llm 0.1a8 — LLM integration plugin for other plugins to depend on.

- Fix for bug where `llm_prompt_context()` hook did not fully collect chains of responses. [datasette-llm#7](https://github.com/datasette/datasette-llm/issues/7).
