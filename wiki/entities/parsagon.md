---
title: Parsagon
created: 2026-05-13
updated: 2026-07-08
type: entity
tags:
  - company
  - product
  - tool
  - web-scraping
  - browser-automation
  - open-source
aliases:
  - "Parsagon, Inc."
  - parsagon-sdk
sources:
  - https://parsagon.io/
  - https://pypi.org/project/parsagon/
---

# Parsagon

**Parsagon** is an AI-powered browser automation and web scraping platform that enables users to create browser automations using natural language. Created by **Sandy Suh** (sandy@parsagon.io), it provides a Python CLI and SDK for creating, running, and managing browser-based data extraction workflows without writing code.

> **Note**: As of mid-2026, parsagon.io appears to have pivoted to a **Global Policy Intelligence** platform (monitoring legislation across 70+ countries). The original browser automation/web scraping product remains available as a Python package (`pip install parsagon`) and via the Parsagon SDK.

## Getting Started

```bash
pip install parsagon
parsagon setup  # copy-paste API key when prompted
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `parsagon create` | Create a new browser automation program |
| `parsagon run 'My program'` | Run an existing program by name |
| `parsagon detail` | List all programs with details |
| `parsagon delete 'My program'` | Delete a program |

## Python API

```python
import parsagon

# Create a program with natural language
parsagon.create('Go to https://www.google.com/...')

# Run a program
parsagon.run("My program")

# Batch executions
parsagon.batch_runs("My batch name", "My program", runs=[...])

# List and delete
parsagon.detail()
parsagon.delete("My program")
```

The natural language interface accepts instructions like:
> "Go to google.com. Type 'the meaning of life' into the search bar and hit enter. Scroll down and click 'More results' 3 times. Scrape structured data."

## Technical Details

- **Package**: `parsagon` (Python, PyPI)
- **Latest Release**: June 15, 2026 (v1.0.1)
- **License**: MIT
- **Maintainer**: Sandy Suh (sand1929)
- **Repository**: `github.com/Sand1929/parsagon-sdk`
- **Python**: >= 3.10
- **Requires**: Google Chrome (up-to-date)

## Related Pages

- [[concepts/scraping]] — Web scraping techniques and tools
- [[concepts/data-engineering]] — Data engineering patterns
- [[entities/brightdata]] — Similar web scraping platform

## References

- [PyPI: parsagon](https://pypi.org/project/parsagon/)
- [Parsagon SDK Documentation](https://parsagon.io/docs/pipelines/overview)
- [Parsagon Website](https://parsagon.io/)
- [NPM: @parsagon/sdk](https://www.npmjs.com/package/parsagon)
