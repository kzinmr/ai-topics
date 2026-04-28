---
title: "Pydantic — Data Validation Using Python Type Hints"
tags: [data-validation-python-type-hints-rust-web-frameworks-fastapi]
created: 2026-04-16
updated: 2026-04-24
type: concept
---

# Pydantic — Data Validation Using Python Type Hints

## Definition

Pydantic is a Python data validation library that uses type hints to validate, serialize, and document data. It has become the de facto standard for data validation in the Python ecosystem, with 27.3K+ GitHub stars and 46M+ monthly PyPI downloads.

**Repository**: github.com/pydantic/pydantic (MIT License)

## Origin Story

Created by Samuel Colvin in 2017 out of frustration that Python type hints "do nothing at runtime." He noticed existing validation libraries (Marshmallow, Django REST framework, Cerberus) all predated the type hints world and asked: *"can we use type annotations to validate data?"* The answer was yes, and Pydantic was born.

## Key Principles

1. **Developer Experience First**: Make validation intuitive and ergonomic
2. **Leverage Existing Knowledge**: Use Python type annotations developers already understand
3. **Performance Matters**: V2 rewritten in Rust (Pydantic Core) for ~17x speed improvement

## Architecture

### Pydantic V1 (Python-only)
- Pure Python validation
- Good enough for most use cases
- Limited performance for high-throughput scenarios

### Pydantic V2 (Rust Core)
- **Pydantic Core**: Rust implementation for performance-critical validation
- **Pydantic**: Python wrapper with developer-facing API
- **pydantic-settings**: Environment variable and config file support
- **pydantic-extra-types**: Extended type support (payment cards, coordinates, etc.)

## Ecosystem Integration

| Framework/Library | Integration Type | Notes |
|------------------|-----------------|-------|
| **FastAPI** | Deep symbiosis | Uses Pydantic for request/response validation; ~6% of all professional web developers use FastAPI |
| **SQLModel** | Built on Pydantic | SQLAlchemy + Pydantic combined |
| **LangChain** | Uses Pydantic | Tool definitions, output parsing |
| **Pydantic AI** | Same team | Type-safe agent framework extending Pydantic principles |
| **Django Ninja** | Compatible | Alternative to Django REST framework using Pydantic |
| **Beanie** | ODM | MongoDB ODM built on Pydantic |

## Impact

> *"Pydantic is used by 12% of professional web developers!"* — Samuel Colvin (Feb 2023 company announcement)

Based on StackOverflow 2022 survey (FastAPI at 6.01%) and PyPI download ratios (Pydantic:FastAPI ≈ 4:1), Colvin estimated ~12% of professional web developers use Pydantic indirectly through FastAPI and other frameworks.

## Timeline

- **2017**: First release by Samuel Colvin
- **2018-2020**: Rapid adoption through FastAPI ecosystem
- **Apr 2023**: V2 pre-release announcement
- **Jun 2023**: V2 released (Rust core, 17x faster)
- **2024-2026**: Foundation for Pydantic AI, Monty, Logfire

## Related

- [[concepts/structured-outputs]] — Pydantic validates structured data
- **[[jason-liu]]** — Instructor library creator; "Pydantic is all you need" advocate; Applied LLMs Guide co-author
- [[concepts/pydantic-ai]] — Next evolution of Pydantic for AI agents
- [[samuel-colvin]] — Creator
-  — FastAPI creator, close collaborator
