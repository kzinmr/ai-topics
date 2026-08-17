---
type: raw_article
title: "Mole — a deep-research agent with an enforced budget, verified quotes, and a privacy boundary"
source: "github.com/lajosdeme/mole"
source_url: "https://github.com/lajosdeme/mole"
date: 2026-08-13
date_ingested: 2026-08-17
author: "Lajos Deme (lajosdeme)"
tags: [deep-research, research-agent, agents, verification, privacy, cost-optimization, go, cli, mcp, local-first]
note: "GitHub README. Repo created 2026-08-01, last pushed 2026-08-13, 224 stars at crawl time. Show HN 2026-08-14 (100 points). Written in Go; ships as a single static binary; MCP-exposed."
---

# Mole — a deep-research agent with an enforced budget, verified quotes, and a privacy boundary

> "A deep-research agent with an enforced budget, verified quotes, and a privacy boundary for local data." — Go, single static binary, exposed over MCP.

Ask a question. `mole` decomposes it, searches, reads sources, extracts claims, checks each claim against the text it came from, looks for contradictions between them, and writes an answer with citations. Every model call is reserved against a budget before it happens and settled after, so the ceiling you set is the ceiling it hits.

It runs as a single static binary on your machine, uses your own API keys, and speaks MCP so a coding agent can drive it — either by handing `mole` a question and collecting the answer, or, in **toolkit mode**, by doing the reasoning with its own model while `mole` supplies the parts that are not model calls.

## Why mole (three things a chat interface with web search does not do)

1. **The budget is enforced, not estimated.** Every call is reserved before it is made and settled after, against a ledger with non-negative constraints in the database schema itself. `--usd 0.50` means the run stops at fifty cents. Measured overshoot across the test corpus is 0%.

2. **Every claim carries a quote, checked against the source.** A claim whose quote does not appear verbatim in the page it was mined from is discarded at extraction, before it can reach an answer. Claims that survive can be re-read against their source afterwards, and one that turns out not to be supported is marked as such in the report rather than quietly dropped.

3. **Your local data stays local.** Point mole at a CSV or a folder and it will analyse it without the contents leaving your machine: the model chooses a hypothesis template and column names, mole renders and runs the SQL, and only aggregates — counts, means, test results, buckets covering at least five records — are allowed back. `mole crossings` shows you exactly what left.

## Install

- **Script** — `curl -fsSL https://raw.githubusercontent.com/lajosdeme/mole/main/install.sh | sh` (Linux/macOS, amd64/arm64). Verifies SHA-256, installs `mole` and `mole-mcp` into `~/.local/bin`.
- **Homebrew** — `brew install lajosdeme/mole/mole` (fully-qualified; an unrelated `mole` macOS cleanup tool occupies `homebrew/core`).

## Demo (from README)

Researching a question: planning → 39 claims → two contradictions found → $0.0149 spent.
