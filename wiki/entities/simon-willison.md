---
title: "Simon Willison"
created: 2026-04-10
updated: 2026-04-10
tags: [person, blogger, hn-popular, developer-tools, ai-agents, open-source, python, data-journalism]
aliases: ["simonw", "simon-willison"]
---

# Simon Willison

| | |
|---|---|
| **Blog** | [simonwillison.net](https://simonwillison.net) |
| **TIL** | [til.simonwillison.net](https://til.simonwillison.net) |
| **Newsletter** | Weekly-ish (free), monthly (paid sponsor tier) |
| **RSS** | https://simonwillison.net/atom/everything/ |
| **GitHub** | [github.com/simonw](https://github.com/simonw) |
| **Mastodon** | [@simon@simonwillison.net](https://simonwillison.net/@simon) |
| **Bluesky** | [simonwillison.net](https://bsky.app/profile/simonwillison.net) |
| **Twitter** | [@simonw](https://twitter.com/simonw) |
| **Role** | Independent open-source developer; PSF Board Member |
| **Known for** | Django (co-creator), Datasette, `llm` CLI, coining "prompt injection" |
| **Bio** | British web developer and software architect. Co-created the Django web framework in 2003 with Adrian Holovaty. Previously engineering director at Eventbrite (joined via Lanyrd acquisition). Currently works full-time building open-source tools for data journalism and AI exploration. Board member of the Python Software Foundation. Has been blogging since 2002. |

## Core Ideas

Simon is a **pragmatic builder** who operates at the intersection of data journalism, open-source tooling, and AI research. Unlike hype-driven adopters, he maintains rigorous empirical standards — publishing detailed technical notes, benchmarks, and reproducible workflows. His approach to AI emphasizes **understanding capabilities through hands-on experimentation** rather than theoretical speculation. He blogs prolifically, publishing multiple posts per week about new tools, techniques, and findings.

### The AI Tooling Ecosystem

Simon has emerged as a leading voice in the **practical AI tooling** space. Rather than treating LLMs as magical oracles, he builds concrete tools that integrate them into real developer workflows:

- **`llm` CLI** (April 2023) — Command-line utility for accessing LLMs via remote APIs or locally installed models. Enables terminal-based prompting, plugin-based model extensibility, and rapid prototyping. Over 11.5k GitHub stars. Recent ecosystem includes `llm-gemini`, `llm-openrouter` plugins and integration with Deep Research APIs.
- **Datasette** — Open-source multi-tool for exploring and publishing data. Pairs SQLite with a web interface, enabling journalists and researchers to publish interactive data. Over 10.9k GitHub stars. Recent plugins include `datasette-llm`, `datasette-enrichments-llm`, `datasette-extract`, `datasette-graphql`, `datasette-turnstile`, `datasette-atom`, and `datasette-ports`.
- **`sqlite-utils`** — Python CLI and library for manipulating SQLite databases. 2k GitHub stars.
- **`shot-scraper`** — Command-line utility for taking automated screenshots of websites. 2.3k GitHub stars.
- **`files-to-prompt`** — Concatenates a directory of files into a single prompt for LLMs. 2.6k GitHub stars.
- **`scan-for-secrets`** — CLI tool for scanning directories for leaked API keys and secrets.

His tooling philosophy centers on **reproducibility and transparency** — every project is open source, well-documented, and designed to solve concrete problems he encounters in his own work.

### AI Security & Terminology

Simon has contributed critical vocabulary and frameworks for understanding AI security risks:

- **"Prompt injection"** (coined, Sept 2022) — Security vulnerability affecting LLMs where untrusted input manipulates model behavior. Building on earlier demos by Riley Goodside, Simon formalized the framework and nomenclature now widely adopted in cybersecurity.
- **"Slop"** (early 2020s) — Low-quality AI-generated content. Early proponent of the term as a descriptor for the flood of AI-produced noise online.
- **"Lethal trifecta"** (June 2025) — High-risk AI agent configuration combining: (1) access to private data, (2) exposure to untrusted content, (3) ability to communicate externally. Systems with all three traits are highly vulnerable to prompt injection and data exfiltration.
- **"Pelican benchmark"** (Oct 2024) — Informal LLM evaluation test measuring SVG generation capability for the prompt "a pelican riding a bicycle." Became a widely-adopted informal benchmark for multimodal model evaluation.

### AI Adoption & Agentic Engineering

Simon documents his AI experimentation extensively through both his main blog and his TIL site. Key observations and workflows:

- **Agentic workflows**: Early adopter of agentic coding tools (Claude Code, Codex CLI, OpenClaw). Prefers tools that can read files, execute programs, and self-correct in a loop. Runs background agents for deep research and code exploration while maintaining human oversight.
- **Local model experimentation**: Runs eval suites locally on Mac against models like `gpt-oss-20b` using LM Studio and `uv`. Connects OpenAI's Codex CLI to models hosted on NVIDIA DGX Spark via Tailscale for GPU acceleration.
- **Today I Learned (TIL)**: His TIL blog at til.simonwillison.net serves as a living repository of practical insights, with 575+ entries covering Cloudflare rate limiting, Docker configurations, Python testing patterns, AI model benchmarking, and infrastructure automation.
- **CI/CD pragmatism**: Uses GitHub Codespaces with devcontainers, Tailscale exit nodes to bypass IP blocks in GitHub Actions, and Cloudflare Pages for domain redirects. Documents all patterns publicly.

### The Datasette Philosophy

Simon's approach to data publishing embodies several core principles:

1. **Data should be explorable** — not just published as static files but as interactive, queryable resources
2. **SQLite is underrated** — a powerful, embeddable database that deserves more respect in the data ecosystem
3. **Plugins over monoliths** — extend functionality through composable plugins rather than building everything into one system
4. **Transparency in sponsorship** — openly discloses all funding sources (GitHub Sponsors, Fly.io sponsorship for Datasette Cloud, Mozilla MIECO program) and maintains editorial independence

### The TIL Pattern

Simon's "Today I Learned" approach represents a knowledge management methodology:
- **Atomic notes**: Each TIL entry is self-contained, focused on one insight or technique
- **Public by default**: Everything is published, creating a searchable knowledge base
- **Reproducible**: Commands, code snippets, and configurations are included so others can replicate
- **Accretive value**: Over 575+ entries create a compounding knowledge resource that benefits both the author and readers

### Data Journalism Infrastructure

Simon builds tools specifically for journalistic workflows:
- **CIA World Factbook Archive** (Feb 2026): Following CIA's discontinuation of the site, retrieved the final 2020 ZIP archive, extracted it, and published it to a public GitHub repository for long-term preservation
- **HN Comment Analysis** (Mar 2026): Profiled Hacker News users based on their comment patterns using Datasette
- **Global Power Plants dataset**: Published and maintained at `global-power-plants.datasettes.com`

## Key Quotes

> *"AI basically let me put aside all my doubts on technical calls... Instead of 'I need to understand how SQLite's parsing works', it was 'I need to get AI to suggest an approach for me so I can tear it up and build something better'."* — on how AI changed his development workflow (via Lalit Maganti's syntaqlite experience)

> *"You can't design a better problem for an LLM agent than exploitation research."* — Thomas Ptacek, cited by Simon on AI's role in security

> *"I do not receive any compensation for writing about specific topics on this blog. I plan to continue this policy."* — editorial independence disclosure

## Related

- [[concepts/agentic-engineering]] — Agent-first development workflows Simon actively uses and writes about
- [[concepts/prompt-injection]] — Security vulnerability framework Simon coined and formalized
- [[concepts/slop]] — Term for low-quality AI-generated content
- [[entities/django]] — Web framework Simon co-created with Adrian Holovaty and others
- [[entities/datasette]] — Data exploration tool Simon created
- [[entities/llm-cli]] — Command-line tool for accessing LLMs

## Sources

- [Simon Willison's Weblog](https://simonwillison.net/) (2002–present)
- [Today I Learned](https://til.simonwillison.net/) (575+ entries)
- [Simon Willison Wikipedia](https://en.wikipedia.org/wiki/Simon_Willison)
- [GitHub: simonw](https://github.com/simonw)
- [Datasette](https://datasette.io/)
- [llm CLI](https://github.com/simonw/llm)
- [shot-scraper](https://github.com/simonw/shot-scraper)
