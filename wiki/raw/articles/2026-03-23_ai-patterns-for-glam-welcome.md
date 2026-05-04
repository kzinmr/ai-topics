---
title: "AI Design Patterns for Information Professionals (Welcome)"
source: https://danielvanstrien.xyz/ai-patterns-for-glam/
author: Daniel van Strien
date: 2026-03-23
tags:
  - GLAM
  - design-patterns
  - boring-ai
  - structured-extraction
  - information-professionals
  - cultural-heritage
  - huggingface
url: https://danielvanstrien.xyz/ai-patterns-for-glam/
---

# AI Design Patterns for Information Professionals (Welcome + Introduction)

> Work in progress. Early draft. Published March 23, 2026.

## Welcome

This book documents practical AI design patterns for information professionals — librarians, archivists, journalists, charity analysts, records managers, and anyone working with large collections of documents or data without a dedicated machine learning team.

The examples come from GLAM (Galleries, Libraries, Archives and Museums) and specifically from work with the National Library of Scotland, but the patterns apply to any information-rich organisation working with collections at scale.

### About the Author

Daniel van Strien is a Machine Learning Librarian at Hugging Face, where he focuses on datasets and bridging machine learning with the cultural heritage sector. Previously worked as a librarian and digital curator at the British Library and other institutions.

## Introduction

### Why patterns?

Most discussions about AI focus on chatbots, generative AI, and autonomous agents. But for information professionals, the most impactful uses of AI are often far more mundane: extracting structured data from scanned documents, classifying items in a backlog, or pulling metadata from thousands of PDFs.

These tasks represent real bottlenecks:
- A library sitting on 250,000 unindexed manuscript cards
- A charity with decades of case files that need categorising
- A newsroom with thousands of leaked documents to sift through

AI tools and models change rapidly, but the *problems* information professionals face — and the broad strategies for solving them — are far more stable.

The idea of design patterns comes from architecture — Christopher Alexander's *A Pattern Language* (1977) — later adopted in software engineering. This book applies the same idea to AI in information work: reusable approaches to common challenges.

### What this book covers

Organised around the key stages of an AI project:

- **Discovery**: How to identify where AI can genuinely help, and how to avoid common pitfalls when scoping projects.
- **Design patterns**: Reusable approaches to common tasks, starting with structured information extraction.
- **Evaluation**: How to measure whether AI outputs are good enough for your use case.
- **Infrastructure**: Practical guidance on hardware, hosting, and cost — including when to run models locally versus using cloud APIs.

### How to use this book

Each pattern includes:
- The **problem** it addresses
- A **worked example** with real data
- Guidance on **evaluation** — how to know if it's working
- **Trade-offs** and things to watch out for

The examples draw on work with the National Library of Scotland, but are designed to be adapted to other collections and contexts.
