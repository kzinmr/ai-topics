---
title: Hynek Schlawack
type: entity
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - python
  - open-source
  - devops
  - software-engineering
  - attrs
  - structlog
  - testing
  - packaging
sources: []
---


# Hynek Schlawack (@hynek)

| | |
|---|---|
| **X** | [@hynek](https://x.com/hynek) |
| **Blog** | [hynek.me/articles](https://hynek.me/articles) |
| **GitHub** | [github.com/hynek](https://github.com/hynek) |
| **Newsletter** | [Hynek Did Something](https://hynek.me/newsletter) |
| **Role** | Senior Software Engineer at Variomedia AG; Open-source maintainer |
| **Known for** | Creator of attrs, structlog; Python packaging advocate; DevOps practices |
| **Bio** | Berlin-based Pythonista and Go developer who writes production software keeping a web host and domain registrar online. A prolific conference speaker, YouTuber, and open-source maintainer who believes in practical, production-tested tooling over theoretical purity. |

## Overview

**Hynek Schlawack** is one of the most respected voices in the Python ecosystem — not for building flashy AI products, but for creating the **infrastructure-level libraries** that millions of Python developers depend on daily. His two flagship projects, **attrs** and **structlog**, address fundamental problems in Python development: reducing boilerplate and making logging actually useful in production.

Born from a late-night IRC session in January 2015, attrs has since surpassed **1 billion downloads** and directly inspired Python 3.7's `dataclasses` module. structlog, launched in 2013, is the production-ready structured logging solution used across the Python industry. Hynek's philosophy is deeply pragmatic: "Is all fun and game until you need to put it in production."

What sets Hynek apart from many Python luminaries is his **production-first perspective**. He doesn't build tools in an ivory tower — he runs them at Variomedia AG, a German web host and domain registrar, where reliability and predictability matter more than elegance. This gives his opinions on packaging, testing, Docker, and CI/CD a grounded authority that resonates across the community.

Hynek is also a prominent conference speaker and keynote presenter from California to Tokyo, a YouTuber who shares practical Python and DevOps tutorials, and the author of the **Hynek Did Something** newsletter — a low-volume, no-tracking publication where he shares technical insights and behind-the-scenes stories about open-source maintenance.

In the AI era, Hynek's influence extends to the Python ML/AI stack through attrs (used by many ML libraries) and his broader work on software engineering practices. He is one of the few maintainers who has **directly shaped Python's standard library** through the attrs → dataclasses pipeline, and his advocacy for sustainable open-source maintenance is increasingly relevant as AI-generated code floods projects.

## Core Ideas

### The attrs Philosophy: Classes Without Boilerplate

Hynek's most influential contribution, attrs, was born from frustration with Python's verbose class patterns. The original `characteristic` library evolved into attrs after an IRC conversation with Glyph, with the design goal of eliminating boilerplate while maintaining full flexibility.

Key design principles:
- **Brevity matters** — the original `@attr.s`/`@attr.ib` syntax was deliberately short
- **Production-first defaults** — sensible choices out of the box, not academic purity
- **Evolution over revolution** — the library grew through real-world usage, not theoretical design

The modern `import attrs` namespace (v21.3.0+) introduced `@define`, `@mutable`, and `@frozen` decorators with slotted classes and MRO-correct attribute collection as defaults. As Hynek wrote:

> *"dataclasses were always a strict subset of attrs."*

This wasn't mere rivalry — attrs provided type hint support before Python 3.7 existed, through the undocumented `@attr.dataclass` alias and later `@attr.s(auto_attribs=True)`.

### Fighting Misinformation in Open Source

Perhaps the most emotionally resonant piece of Hynek's writing is his 2021 post **"import attrs"**, which details what he calls "constant erasure and revisionism, bordering on abuse" surrounding attrs after dataclasses entered the standard library:

> *"To this day I'm baffled by what happened and it sucked every bit of fun and joy that I had with Open Source for a long time."*

Despite attrs being labeled "legacy" or "deprecated" by community members who simply didn't understand the relationship, the library crossed 1 billion downloads, gained IDE support in PyCharm and VS Code/pyright, and earned a NASA GitHub badge. Hynek's response wasn't to fight every mischaracterization — he acknowledges the futility — but to **document the truth clearly** and keep improving the library.

### Python Packaging: Standards Over Convenience

Hynek is a vocal advocate for **reproducible, predictable Python packaging**. His key positions:

- **Virtual environments in Docker** — despite frequent pushback, he argues: *"Whenever I publish something about my Python Docker workflows, I invariably get challenged about whether it makes sense to use virtual environments in Docker containers. As always, it's a trade-off, and I err on the side of standards and predictability."*
- **Static metadata over `setup.py`** — pip 21.2+ enables optional dependency combinations without executing arbitrary code, a security and reproducibility improvement
- **`uv` for production workflows** — he's adopted Astral's `uv` for cross-platform lock files (`uv.lock`) that enable fast, production-ready container builds
- **SemVer pragmatism** — the `cryptography` library's shift to a Rust backend sparked debate; Hynek argues rigid Semantic Versioning can harm users by ignoring practical ecosystem evolution

### Testing and CI/CD: Native Over Third-Party

Hynek increasingly advocates for moving away from external CI services toward **native GitHub Actions**:

- **tox parallelization** can cut local test runtime by 75% with the right configuration
- **Nox over tox** for cross-version testing due to greater flexibility and modern workflow alignment
- **Native coverage enforcement** through GitHub Actions matrix builds, replacing unreliable third-party services like Codecov — *"Codecov's unreliability breaking CI on my open source projects has been a constant source of frustration for me for years."*
- **Azure Pipelines** as a viable alternative for projects that need more than GitHub Actions' free tier

### Python Language: Underappreciated Gems

Hynek consistently highlights Python's overlooked standard library features:

- **`functools.singledispatch`** — "The Python standard library is full of underappreciated gems" — essential for type-based dispatch and JSON serialization
- **`asyncio` concurrency patterns** — multiple patterns for awaiting concurrent coroutine results, with production caveats
- **Decorator correctness** — most online decorator implementations are broken; proper decorators must preserve callable signatures and support class methods
- **`hasattr()` dangers** — avoid unless writing Python 3-only code with full understanding of its behavior

### Sustainable Open-Source Maintenance

Hynek funds all his open-source work — attrs, structlog, and numerous other projects — **entirely through donations**. He's transparent about the costs:

> *"All my writing, mentoring, conference speaking, and open-source work I do for free. In many cases, it even costs me money for stickers, travel visas, et cetera."*

He advocates for:
- **GitHub Sponsors** and **Tidelift Subscriptions** as sustainable funding models
- **Conference speaking** as a way to share knowledge and build community
- **Documentation investment** — updated good-faith comparisons between attrs and dataclasses help users make informed choices

## Key Work

### Libraries & Tools

| Project | Description | Impact |
|---------|-------------|--------|
| **attrs** | Classes without boilerplate; inspired Python 3.7 dataclasses | 1B+ downloads, PEP 557 lineage |
| **structlog** | Production-ready structured logging for Python | 4.6K+ GitHub stars, used since 2013 |
| **PyOpenSSL** | Python wrapper for OpenSSL | Core cryptography infrastructure |
| **Twisted** | Event-driven networking engine | Long-time contributor and committer |
| **cryptography** | Python cryptographic primitives | Rust backend advocate |

### Notable Blog Posts

| Post | Date | Topic |
|------|------|-------|
| **"import attrs"** | 2021 | The history of attrs, its relationship to dataclasses, and the fight against misinformation |
| **"Python's True Superpower"** | 2024 | Why Python's ecosystem strength lies in its practical tooling |
| **"Production-ready Python Docker Containers with uv"** | 2024 | Cross-platform reproducible builds using Astral's uv |
| **"Why I Still Use Python Virtual Environments in Docker"** | 2024 | The case for venv in containers despite pushback |
| **"Don't Start Pull Requests from Your Main Branch"** | 2023 | Contribution workflow best practices |
| **"Better Python Object Serialization"** | 2017 | Using `functools.singledispatch` for clean serialization |
| **"How I'm a Productive Programmer With a Memory of a Fruit Fly"** | 2023 | Personal productivity systems for developers |
| **"Two Ways to Turbo-Charge tox"** | 2023 | 75% runtime reduction in local test execution |

### Conference Talks & Keynotes

- Speaker at PyCon US, EuroPython, PyCon DE, and numerous other conferences from California to Tokyo
- Keynote presentations on Python packaging, testing strategies, and open-source sustainability
- YouTube tutorials on Python and DevOps topics
- Regular contributor to the Python community through talks, blog posts, and newsletter

## Blog / Recent Posts

Hynek's blog at [hynek.me/articles](https://hynek.me/articles) covers Python development, DevOps, and open-source maintenance:

- **Python's True Superpower** — Why Python's ecosystem strength lies in practical, production-tested tooling
- **Design Pressure** — How production requirements shape better software design
- **Why I Still Use Python Virtual Environments in Docker** — Trade-offs between convenience and predictability
- **Production-ready Python Docker Containers with uv** — Using Astral's uv for cross-platform reproducible builds
- **Python Project-Local Virtualenv Management Redux** — Updated approach to local environment management
- **Don't Start Pull Requests from Your Main Branch** — Contribution workflow best practices
- **Two Ways to Turbo-Charge tox** — Cutting local test runtime by 75%
- **Subclassing, Composition, Python, and You** — OOP design patterns in modern Python
- **Why I Like Nox** — Preferring Nox over tox for cross-version testing
- **How to Ditch Codecov for Python Projects** — Native GitHub Actions coverage enforcement
- **import attrs** — The cathartic history of attrs and its relationship to dataclasses

## Related People

- [[samuel-colvin]] — Fellow Python ecosystem maintainer (Pydantic, Pydantic AI, Monty)
- [[mitsuhiko]] — Python/Rust developer (Flask, Sentry, Jinja2) with complementary focus on web frameworks
- [[sebastien-ramirez]] — FastAPI creator, fellow OSS maintainer dealing with AI-generated PR challenges
-  — Python's creator; Hynek's attrs work directly influenced PEP 557 (dataclasses)
-  — attrs co-conspirator from the original IRC session; Twisted project leader
- [[eugeneyan]] — ML practitioner who shares Hynek's focus on production-first practices
- [[andrew-nesbitt]] — Ruby developer with similar open-source maintenance philosophy

## X Activity Themes

Hynek uses X/Twitter (@hynek) to share:
- **Python packaging debates** — venv in Docker, uv adoption, setuptools vs. modern alternatives
- **Open-source maintenance** — The realities of sustaining popular libraries, funding models, dealing with misinformation
- **Conference announcements** — Speaking engagements, keynote presentations, community events
- **DevOps practices** — CI/CD optimization, testing strategies, deployment workflows
- **Technical tutorials** — YouTube video promotions, blog post announcements
- **Community advocacy** — Support for PyLadies and diversity initiatives, sustainable OSS funding
- **Tool recommendations** — Nox vs. tox, GitHub Actions vs. Travis/Azure, singedispatch patterns

His posting style is characterized by **pragmatism and directness** — he doesn't shy away from unpopular opinions (venv in Docker, attrs vs. dataclasses) and backs them up with production experience rather than theoretical arguments.
