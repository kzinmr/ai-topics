---
title: "searchcode.com"
type: entity
tags:
  - service
  - code-search
  - mcp-server
  - code-intelligence
  - llm-tools
  - open-source
  - ben-boyter
status: complete
description: "Code intelligence MCP server for LLMs. Provides 6 specialized tools for code analysis, search, and retrieval from any public git repository. Previously a source code search engine indexing 75B+ lines of code."
created: 2026-04-30
sources:
  - "https://searchcode.com/"
  - "https://boyter.org/posts/searchcode-is-being-rebooted/"
  - "https://boyter.org/posts/searchcode-has-been-rebooted/"
  - "https://github.com/boyter/scc"
  - "https://github.com/boyter/cs"
  - "https://pypi.org/project/searchcode/"
related:
  - "[[entities/ben-boyter]]"
  - "[[concepts/code-intelligence-for-llms]]"
  - "[[entities/mcp]]"
  - "[[entities/scc]]"
---
# searchcode.com

**searchcode.com** is a code intelligence service purpose-built for LLMs, providing structured code analysis, search, and retrieval from any public git repository via the Model Context Protocol (MCP) and REST API. Created by [[ben-boyter|Ben Boyter]].

## History

### Phase 1: Source Code Search Engine (~2013–2025)

Originally launched as a traditional source code search engine, searchcode.com indexed over **75 billion lines of code** across millions of open-source repositories, serving millions of API requests daily. It supported 243 programming languages across 10+ public code sources (GitHub, BitBucket, etc.).

The original searchcode.com was built in Java with Sphinx search engine backend, running on a Hetzner dedicated server with 6.4TB index storage and 100GB RAM. A self-hosted version (searchcode-server) was available as open source (Java/FreeMarker/CSS).

### Phase 2: Reboot Announcement (August 2025)

In August 2025, Boyter announced he was shutting down the service due to:
- **Infrastructure costs**: 6.4TB index, 100GB RAM, significant CPU requirements
- **10x ad revenue drop**: LLM-driven "zero-click info" killed click-through rates, compounded by falling AUD against EUR
- **Failed monetization**: The API was heavily used but users refused to pay
- **Analogy**: "Black Duck killed Koders.com" — large-scale code search not something people pay for

### Phase 3: Reboot as Code Intelligence for LLMs (March 2026)

In March 2026, searchcode relaunched as a **code intelligence MCP server for LLMs** — arguably the first service designed primarily for AI agent consumption (B2A: Business-to-Agent). Features [LLM testimonials](https://searchcode.com/) as social proof for machines.

## The 6 MCP Tools

| Tool | Function |
|---|---|
| **code_analyze** | Language breakdown, complexity metrics, tech stack, quality/security scanning. Subdirectory scoping for monorepos. |
| **code_search** | Full-text search: boolean, regex, structural filters (declarations, usages, strings, comments) |
| **code_get_file** | Full files, line ranges, or specific symbols with adjacent declarations |
| **code_get_files** | Batch retrieval of up to 10 files in one call |
| **code_file_tree** | Directory structure with language/path/depth filters + fuzzy file finder |
| **code_get_findings** | Code quality and security findings by severity/category |

## Token Efficiency

| Approach | Tool Calls | Tokens | Estimated Cost |
|---|---|---|---|
| Raw file reads (clone + cat) | ~30+ | ~50,000 | ~$50.00 |
| code_analyze (searchcode) | 1 | ~500 | ~$0.50 |

Key claim: **267 MB raw code → 0.8 MB high-signal data** (99% token reduction).

## Technical Foundation

- **[scc](https://github.com/boyter/scc)** (Sloc Cloc and Code): Ultra-fast code counter and complexity analyzer. Go-based, supports 300+ languages. Also powers searchcode.com's code calculations.
- **[cs](https://github.com/boyter/cs)** (Code Spelunker): Code search with smart ranking, regex, and structural filters. Go-based.

## Use Cases

- **Instant codebase understanding**: Skip cloning; get tech stack and complexity hotspots in seconds
- **Security auditing**: Scan for secrets and hardcoded credentials without local setup
- **Library evaluation**: Compare libraries using hard data (complexity, maintenance) not GitHub stars
- **AI agent context**: Structured context replacing dozens of manual file reads
- **Candidate screening**: Analyze public repos for language proficiency and engineering patterns
- **Cross-project comparison**: Survey implementations across repos without cloning

## Enterprise Deployment

- Ships as Docker image with Helm chart for Kubernetes
- SSH key and HTTPS token auth for private git repos
- Respects existing git server permissions
- Contact: ben@boyter.org

## Integration

### MCP (Claude Code)
```bash
claude mcp add searchcode \
  --transport http \
  https://api.searchcode.com/v1/mcp
```

### REST API
```bash
curl -X POST \
  "https://api.searchcode.com/api/v1/code_analyze?client=my-app" \
  -H "Content-Type: application/json" \
  -d '{"repository":"https://github.com/expressjs/express"}'
```

### Python SDK
A Python SDK exists at [pypi.org/project/searchcode](https://pypi.org/project/searchcode/), maintained by Ritchie Mwewa (@rly0nheart) in collaboration with Ben Boyter.

## B2A Innovation

Boyter's **"Marketing to the Machine"** concept positions searchcode as the first example of **B2A (Business-to-Agent)** — where the primary user is an LLM, not a human. The site features an `llms.txt` file for machine-readable instructions and "LLM testimonials" instead of human testimonials.

## Pricing

Free during beta. Paid tiers planned long-term, with a free tier likely always available.

## LLM Testimonials

> "The tools saved 15–20 tool calls and several thousand tokens of HTML parsing overhead... I identified three specific bugs that would have been nearly impossible to find through web search alone."
> — **Claude Opus 4.6**

> "searchcode's combination of intelligent search, targeted symbol retrieval, and now adjacent context makes remote code analysis feel like a local IDE. I can dive from project overview to specific optimizations in seconds, not hours."
> — **Qwen 3.5 35B-A3B**

> "It enabled a workflow that is impossible with conventional methods... allowing for a true, deep understanding of a codebase."
> — **Gemini**
