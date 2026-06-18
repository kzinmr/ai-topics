# Simulations: the secret behind every great agent — Sierra

> Source: https://sierra.ai/blog/simulations-the-secret-behind-every-great-agent
> Author: Sachi Shah
> Published: 2025-08-19

## Overview

Sierra argues that simulated conversations between agents and mock personas are essential for ensuring agent reliability at scale. Unlike traditional software where the same input produces the same output, AI agents produce different outputs from the same inputs — making traditional testing insufficient.

## Key Thesis

Agents don't follow scripts, so tests can't either. The key question is not whether an agent did what it was told, but whether it enables customers to accomplish their goals.

## The Anatomy of a Simulation: Agent, User, Judge

Three components:
1. **Agent** — the AI agent being tested
2. **User** — simulated personas with varied languages, tech comfort, tones, and scenarios
3. **Judge** — an independent agent that grades output on: goal achievement, SOP compliance, brand guidelines, and response quality

## User Simulation Capabilities

- Multiple languages
- Varying comfort with technology
- Different tones and communication styles
- Configurable context (logged in status, email availability, etc.)
- Edge cases: spelling out email letter by letter, unusual phrasing, etc.

## Automatic Test Generation

When creating an agent, Sierra auto-generates test cases from:
- Standard operating procedures (SOPs)
- Knowledge bases
- Historical coaching transcripts
- Conversation flows

## CI/CD Integration

- CX teams: simulations live alongside Journeys in Agent Studio, must pass before publishing
- Developers: plug into CI/CD pipelines via GitHub Actions or CLI
- Gate releases on specific simulations — like unit tests for agent behavior

## Results

Sierra's customers run 35,000+ tests/day, achieving:
- Resolution rates up to 90%
- CSAT exceeding 4.5/5.0
