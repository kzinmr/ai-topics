---
title: "OpenAI Deployment Safety Hub: System cards & other updates"
created: 2026-06-10
updated: 2026-06-10
type: article
source_url: https://deploymentsafety.openai.com/
---

# OpenAI Deployment Safety Hub

Source: https://deploymentsafety.openai.com/

## Overview

OpenAI's Deployment Safety Hub is the central portal for all of OpenAI's system cards and safety updates for deployed AI systems. The site describes itself as:

> Sharing the technical work we do to make our systems safe, including how deployed models perform in evaluations, the risks we measure, and the steps we take to improve over time.

## Hub Structure

The site serves as a unified index of all OpenAI system cards, organized chronologically. Each system card links to a detailed multi-page document covering:

- Model capabilities and training
- Preparedness Framework evaluations (Biological & Chemical, Cybersecurity, AI Self-Improvement)
- Safety mitigations (model-level and product-level)
- Red teaming results
- External evaluations

## Linked Resources

The hub also links to three related areas:
- **Safety approach** — https://openai.com/safety/
- **Trust and transparency** — https://openai.com/trust-and-transparency/
- **Research** — https://openai.com/research/index/

## RSS Feed

An RSS feed is available at https://deploymentsafety.openai.com/posts.xml (currently empty editorial posts).

## Technical Notes

- Built with Astro (static site generator)
- Hosted on Cloudflare (deployment ID: dpl_JAoNKtuHo9uubp3QDwFtEWr8S4ej)
- Uses MathJax for rendering mathematical notation in system cards
- Sitemap exposes all sub-pages per system card
