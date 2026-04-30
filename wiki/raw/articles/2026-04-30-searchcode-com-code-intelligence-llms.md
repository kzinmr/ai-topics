# searchcode.com — Code Intelligence for LLMs

**URL:** https://searchcode.com
**Source Date:** 2026-04-30
**Author:** Ben Boyter (@boyter)

## Overview

searchcode.com was rebooted in early 2026 from a traditional source code search engine (indexed 75B+ lines of code) into a **code intelligence MCP server for LLMs**. It provides 6 specialized tools via the Model Context Protocol (MCP) and REST API that analyze, search, and retrieve code from any public git repository.

The service is free during beta and requires no API key for public repos.

## Why the Reboot

In August 2025, Ben Boyter announced he was shutting down searchcode.com due to:
- 6.4TB index + 100GB RAM + significant CPU core requirements
- 10x drop in ad revenue due to LLM-driven "zero-click info" and falling AUD against EUR
- Users unwilling to pay for the API

The reboot happened in Q1 2026, repurposing the decade of code indexing expertise into an LLM-facing service.

## Key Innovation: B2A (Business-to-Agent)

Boyter's March 2026 blog post "Marketing to the Machine" introduced searchcode as what he claims is the **first website with LLM testimonials** — social proof for AI agents rather than humans. The core insight: in an agentic web, the primary user of a service is an LLM, not a human. Efficiency (token density, low latency) becomes the new brand loyalty.

## Token Efficiency

searchcode claims 99% reduction in token usage vs traditional clone + cat approach:

| Approach | Tool Calls | Tokens | Estimated Cost |
|---|---|---|---|
| Raw file reads | ~30+ | ~50,000 | ~$50.00 |
| code_analyze | 1 | ~500 | ~$0.50 |

Key insight: 267 MB of raw code → 0.8 MB of high-signal structured data.

## The 6 MCP Tools

1. **code_analyze** — Language breakdowns, complexity metrics, tech stack, quality/security scanning. Supports subdirectory scoping for monorepos.
2. **code_search** — Full-text search with boolean, regex, structural filters (declarations, usages, strings, comments)
3. **code_get_file** — Full files, line ranges, or specific symbols with adjacent declarations for context
4. **code_get_files** — Batch retrieval of up to 10 files in one call
5. **code_file_tree** — Directory structure with language/path/depth filters + fuzzy file finder
6. **code_get_findings** — Detailed code quality and security findings by severity/category

## Underlying Tech

- **scc** (Sloc Cloc and Code): Fast code counter with complexity calculations, 300+ languages. Go-based. https://github.com/boyter/scc
- **cs** (Code Spelunker): Code search with smart ranking, regex, structural filters. https://github.com/boyter/cs

## Use Cases

- Instant codebase understanding (no clone needed)
- Security auditing for public repos
- Library evaluation before integration
- AI agent code context
- Candidate screening via public repos
- Cross-project pattern comparison

## Enterprise

Docker image + Helm chart for Kubernetes. SSH/HTTPS auth for private git repos. Respects existing git server permissions.

## LLM Testimonials

> "The tools saved 15–20 tool calls and several thousand tokens of HTML parsing overhead... I identified three specific bugs that would have been nearly impossible to find through web search alone." — Claude Opus 4.6

> "searchcode's combination of intelligent search, targeted symbol retrieval, and now adjacent context makes remote code analysis feel like a local IDE." — Qwen 3.5 35B-A3B

## References

- https://searchcode.com/
- https://boyter.org/posts/searchcode-is-being-rebooted/
- https://boyter.org/posts/searchcode-has-been-rebooted/
- https://github.com/boyter/scc
- https://github.com/boyter/cs
- https://github.com/boyter/searchcode-server
- https://github.com/boyter (Ben Boyter's GitHub)
- https://pypi.org/project/searchcode/ (Python SDK by Ritchie Mwewa)
- https://searchcode.com/llms.txt
