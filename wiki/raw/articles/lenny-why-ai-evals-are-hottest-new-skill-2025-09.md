---
title: Why AI Evals Are the Hottest New Skill
category: other
status: active
---

# Why AI Evals Are the Hottest New Skill

Source: Lenny's Newsletter | Sept 25, 2025
Guests: Shreya Shankar, Hamel Husain

## Overview

AI evaluation (evals) has become the critical skill for product builders working with LLMs. Unlike traditional software with deterministic outputs, LLM applications produce non-deterministic responses that require new testing paradigms.

## The Problem with Traditional Metrics

> "If you are tracking a single metric like customer satisfaction score, you are almost certainly doing it wrong." — Shreya Shankar

Traditional software engineering has clear pass/fail criteria. LLM applications require:
- Multiple evaluation dimensions
- Understanding of failure modes, not just aggregate scores
- Continuous monitoring of production behavior

## Types of Evaluation

### Level 1: Unit Tests
- Deterministic checks on specific outputs
- Fast, cheap, reliable
- Example: "Does the response contain a date?"

### Level 2: Human & Model Eval
- Human review of output quality
- LLM-as-judge for scalable evaluation
- Most common approach for AI products

### Level 3: A/B Testing
- Compare different system versions with real users
- Gold standard but slow and expensive
- Requires significant traffic

### Evaluating RAG Systems
- Retrieval quality vs. generation quality
- Context relevance measurement
- Ground truth fact checking

## Key Frameworks and Approaches

### The "Vibes" Problem
- Traditional engineering relies on tests
- LLM engineering often relies on "vibes" (feeling)
- Need systematic approaches to replace subjective judgment

### Hamel's Evals Philosophy
- Start with binary (pass/fail), not 5-star ratings
- Focus on specific failure modes
- Build evaluation around real user traces
- Iterate based on what breaks in production

## The Research Behind Evals

Shreya Shankar's UC Berkeley research on ML evaluation systems:
- "Who Validates the Validators?" paper on AI-powered data pipelines
- Building effective evaluation frameworks
- Understanding annotation quality and consistency

## Industry Context

- GitHub Copilot team developed extensive eval frameworks
- Companies are hiring dedicated "AI Quality Engineers"
- Evals becoming a prerequisite for production AI deployment

## Sources
- Lenny's Newsletter: "Why AI evals are the hottest new skill for product builders"
- https://open.substack.com/pub/lenny/p/why-ai-evals-are-the-hottest-new-skill
