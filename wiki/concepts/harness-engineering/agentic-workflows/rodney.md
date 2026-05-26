---
title: "Rodney — Browser Automation CLI for Agents"
type: concept
aliases:
  - rodney
  - rodney-cli
created: 2026-04-12
updated: 2026-05-26
tags:
  - tool
  - agentic-engineering
  - browser-agent
  - testing
status: draft
sources:
  - "https://simonwillison.net/2026/Feb/10/showboat-and-rodney/"
  - "https://simonwillison.net/2026/Feb/17/rodney/"
  - "https://github.com/simonw/rodney"
---

# Rodney

A **CLI browser automation tool based on the Chrome DevTools Protocol** developed by Simon Willison. Designed for coding agents to test and validate Web UIs.

## Background

> "I went looking for good options for managing a multi-turn browser session from a CLI and came up short, so I decided to try building something new."

Existing browser automation tools (Playwright, Selenium) were not suitable for agent CLI use, so Willison built his own.

## Tech Stack

- **Base**: [Rod](https://go-rod.github.io/) Go library — Comprehensive Chrome DevTools Protocol wrapper
- **CLI**: Go binary (compiled to a few MB), or via Python using `uvx rodney`
- **Namesake**: Rod library + homage to Only Fools and Horses

## Design Philosophy

> "This tool is not designed to be used by humans! The goal is for coding agents to be able to run `rodney --help` and see everything they need to know to start using the tool."

**Agent-First CLI**: Help text is structured for LLM consumption.

## Key Commands

| Command | Description |
|----------|------|
| `rodney start` | Launch Chrome in the background |
| `rodney start --show` | Show browser window (debugging) |
| `rodney open URL` | Open a page |
| `rodney waitstable` | Wait until page load stabilizes |
| `rodney js '...'` | Execute JavaScript and return results |
| `rodney click SELECTOR` | Click an element |
| `rodney exists SELECTOR` | Check if element exists |
| `rodney visible SELECTOR` | Check if element is visible |
| `rodney assert` | Run JavaScript test, exit code 1 on failure |
| `rodney connect PORT` | Connect to an existing Chrome instance |
| `rodney reload --hard` | Hard reload |
| `rodney clear-cache` | Clear cache |

## Showboat Integration

Rodney can be used with [[concepts/showboat]] to record agent Web UI tests as **verifiable and auditable artifacts**.

```bash
showboat exec demo.md bash 'rodney start && rodney open https://example.com && rodney waitstable && rodney exists "h1"'
```

This combination enables:
1. The agent actually operates the browser
2. Operations and results are recorded in Markdown documents
3. Verifiable and reviewable later

## Test Patterns

### Basic Web App Test Script
```bash
#!/bin/bash
set -euo pipefail

FAIL=0
check() {
    if ! "$@"; then
        echo "FAIL: $*"
        FAIL=1
    fi
}

rodney start
rodney open "https://example.com"
rodney waitstable

# Assert elements exist
check rodney exists "h1"
# Assert key elements are visible
check rodney visible "h1"
check rodney visible "#main-content"

if [ "$FAIL" -ne 0 ]; then
    echo "Some checks failed"
    exit 1
fi
echo "All checks passed"
```

## Relationship to Context Management

Rodney's commands are **context-window-friendly**:
- Text-based output only (directly interpretable by LLMs)
- Screenshots are saved as files and referenced via URL
- No need to put Playwright's full API into the context

## Comparison: Browser Automation Tools

| Tool | Developer | Features |
|--------|--------|------|
| Playwright | Microsoft | Multi-language bindings, full features |
| agent-browser | Vercel | Playwright CLI wrapper |
| **Rodney** | Simon Willison | Agent-optimized, Showboat integration |
| shot-scraper | Simon Willison | Screenshot-focused (Rodney's predecessor) |

## Version History

- **v0.4.0** (February 17, 2026): Added `rodney assert`, `--local`/`--global` sessions, `reload --hard`, etc.
- **v0.3.0** (February 10, 2026): Initial release

## Related Concepts

- [[concepts/showboat]] — Test artifact recording tool (used with Rodney)
- [[concepts/agentic-manual-testing]] — Rodney's primary use case
- [[concepts/harness-engineering/agentic-engineering]] — Higher-level concept

## References

- [[entities/simon-willison]] — Developer
- [Rodney v0.4.0 Release Notes](https://simonwillison.net/2026/Feb/17/rodney/)
- [Introducing Showboat and Rodney](https://simonwillison.net/2026/Feb/10/showboat-and-rodney/)
