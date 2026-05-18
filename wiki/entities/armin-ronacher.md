---
title: Armin Ronacher
type: entity
aliases: [mitsuhiko]
created: 2026-05-18
updated: 2026-05-18
tags:
  - person
  - open-source
  - developer-tooling
  - blogger
  - model
  - agentic-engineering
  - infrastructure
sources: [raw/articles/2026-05-18_armin-ronacher_a-language-for-agents.md, https://lucumr.pocoo.org/about/]
---

# Armin Ronacher (@mitsuhiko)

Austrian software engineer, creator of the **Flask** web framework, **Jinja2** templating engine, **Werkzeug** WSGI toolkit, and many other foundational Python libraries. Currently Principal Architect at **Sentry**, where he works on observability infrastructure. Writes at [lucumr.pocoo.org](https://lucumr.pocoo.org/).

## Key Projects

- **[Flask](https://flask.palletsprojects.com/)** — Micro web framework; one of the most popular Python web frameworks alongside Django
- **[Jinja2](https://jinja.palletsprojects.com/)** — Templating engine used widely across the Python ecosystem (Ansible, Salt, Pelican, etc.)
- **[Werkzeug](https://werkzeug.palletsprojects.com/)** — WSGI utility library that underpins Flask
- **[Click](https://click.palletsprojects.com/)** — Command-line interface creation toolkit
- **[Sentry](https://sentry.io/)** — Principal Architect; observability and error tracking platform
- **[Rye](https://github.com/astral-sh/rye)** — Python package manager (later merged into Astral's `uv`)

## AI & Agentic Programming

In February 2026, Ronacher published a landmark essay *"A Language For Agents"* arguing that the rise of AI coding agents will drive the creation of **new programming languages** optimized for agentic workflows. Key observations:

### Why New Languages Can Succeed
- **Cost of writing code is dropping** → breadth of ecosystem matters less. Ronacher now uses TypeScript/JavaScript where he'd have used Python because agents perform better.
- Missing functionality can be **reimplemented by the agent** from another language's library.
- **Agent performance depends more on tooling and language stability** than on presence in training data.
- Languages with rapid churn (Zig) or painful tooling (Swift) degrade agent success, even with good training data representation.

### What Agents Need from a Language
Detailed design principles explored in [[concepts/agent-ergonomics#armin-ronachers-language-design-principles]]:

1. **Context without LSP** — A single coherent experience with and without language server protocol
2. **Braced syntax** — Significant whitespace (Python) causes token inefficiency and surgical edit errors
3. **Explicit flow context (effect markers)** — Declare required effects (time, rng, db) in function signatures, auto-propagated by formatter
4. **Results over exceptions** — Agents fear exceptions; typed result types preferred
5. **Minimal diffs & line-friendly syntax** — Agents read files line-by-line; multi-line strings confuse them
6. **Grep-ability** — Go-style package-qualified symbols, discouraged aliasing
7. **Local reasoning** — Code must be understandable in isolation, without hidden global deps
8. **Dependency-aware build tools** — Clear package structure, forbidding circular imports, cached test results

### What Agents Hate
- **Macros** — Confusing for both humans and agents
- **Re-exports & barrel files** — Break the one-to-one mapping between declaration and import location
- **Aliasing** — Agents complain about many aliases; encourage good naming instead
- **Flaky tests & dev env divergence** — Agents both create and suffer from flaky tests

## Philosophy

Ronacher argues we're entering an era where facts about language design matter more than ever because **agents don't care about surveys** — we can measure what works by seeing how well agents perform. He calls for:

1. **Outsider art** — People who haven't built languages before trying their hand, bringing fresh perspectives
2. **Deliberate documentation** — A systematic effort to document what works from first principles, moving beyond opinion wars to hard facts

> *"The cost of writing code is going down, but because we are also producing more of it, understanding what the code does is becoming more important."*

## Blog
- **URL:** [lucumr.pocoo.org](https://lucumr.pocoo.org/)
- **RSS:** [Atom](https://lucumr.pocoo.org/feed.atom) | [RSS](https://lucumr.pocoo.org/feed.xml)
- **Topics:** Programming languages, Python, Rust, observability, AI agents, software engineering

## Social
- **X/Twitter:** [@mitsuhiko](https://x.com/mitsuhiko)
- **Mastodon:** [@mitsuhiko@hachyderm.io](https://hachyderm.io/@mitsuhiko)
- **GitHub:** [mitsuhiko](https://github.com/mitsuhiko)
- **Bluesky:** [@mitsuhiko](https://bsky.app/profile/mitsuhiko.bsky.social)

## Related
- [[concepts/agent-ergonomics]] — Agent-oriented language design (includes Ronacher's design principles)
- [[concepts/programming-languages]] — Type systems, compilers, language design
- [[entities/wes-mckinney]] — Author of the agent ergonomics thesis from the ecosystem/tooling perspective
- [[concepts/harness-engineering/agentic-engineering]] — Professional patterns for coding agent usage
