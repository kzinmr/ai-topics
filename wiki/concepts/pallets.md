---
title: "Pallets"
type: concept
aliases:
  - Pallets
  - Pallets Projects
  - pallets
  - Pocco
created: 2026-04-25
updated: 2026-11-24
tags:
  - open-source
  - organization
  - python
  - developer-tooling
  - web-framework
sources:
  - https://github.com/pallets/flask
  - https://palletsprojects.com
  - https://github.com/pallets
status: active
---

# Pallets

**Pallets** is the open-source organization behind some of the most widely used
Python web-development libraries, most famously **Flask**. Its projects form the
de facto toolkit for building Python web applications and CLIs, and are depended
on by millions of developers and countless production services.

## Flagship Projects

| Project | Purpose | Notes |
|---------|---------|-------|
| **Flask** | Micro web framework | ~75k GitHub stars; BSD-3-Clause; `flask.palletsprojects.com` |
| **Werkzeug** | WSGI toolkit / WSGI web application library | The underlying layer Flask is built on |
| **Jinja** | Templating engine | Used by Flask for HTML rendering |
| **Click** | Command-line interface toolkit | Dominant Python CLI library |
| **ItsDangerous** | Safe data signing | Token/data signing used by Flask sessions |
| **Blinker** | In-process signal/slot messaging | |

Flask's design philosophy is deliberately minimal: it ships a small core (routing
via Werkzeug + templating via Jinja) and relies on a large extension ecosystem
rather than bundling an ORM, form validation, or admin — the "microframework"
contrast with batteries-included frameworks like Django.

## Governance & Sustainability

Pallets is organized as a non-profit-style open-source collective (historically
associated with the **Pocco** foundation / Pallets LLC) that accepts sponsorships
and grants. It has been a notable beneficiary of the broader "sustain open-source"
movement, receiving funding via GitHub Sponsors and the Python Software
Foundation ecosystem to maintain critical-but-underfunded infrastructure.

The core maintainers most associated with the org include **Armin Ronacher**
(`@mitsuhiko`, Flask/Werkzeug/Jinja creator) and **David Lord**, who has led much
of the modern maintenance and release work.

## Relevance to LLM / AI agent work

Pallets libraries sit underneath a large fraction of AI/ML Python tooling: FastAPI
and Flask both build on **Werkzeug/ASGI** patterns, **Click** powers the CLIs of
many agent and dev tools, and **Jinja** is the templating engine used for prompt
templating in LLM libraries (including parts of LangChain and numerous prompt
management systems). Understanding the Pallets stack is therefore foundational to
reading the source of much Python AI tooling.

## Related Pages

- [[concepts/fastapi]] — ASGI framework in the same Python web ecosystem
- [[concepts/python-packaging]] — modern Python packaging complements this ecosystem
- [[entities/armin-ronacher]] — Armin Ronacher, Flask creator

## Sources

- [pallets/flask — GitHub](https://github.com/pallets/flask) — "The Python micro framework for building web applications." ~75k stars, BSD-3-Clause (scraped 2026-11-24)
- [palletsprojects.com](https://palletsprojects.com) — org homepage
