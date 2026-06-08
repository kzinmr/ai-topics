---
title: "Build the Thing That Builds the Thing — Microsoft Build 2025 BRK245"
author: Peter Steinberger
date: 2026-06-02
date_ingested: 2026-06-08
source: https://build.microsoft.com/en-US/sessions/BRK245
type: article
video: https://medius.microsoft.com/Embed/video-nc/5a21e754-8418-4276-9e66-5041ed2f019d
tags:
  - agentic-engineering
  - openclaw
  - developer-tooling
  - ai-automation
  - build-2026
  - open-source
  - coding-agents
  - agent-infrastructure
---

# Build the Thing That Builds the Thing

**Session:** BRK245 — Microsoft Build 2025
**Speaker:** [[entities/peter-steinberger|Peter Steinberger]] (Creator of OpenClaw, OpenAI)
**Date:** June 2, 2026
**Duration:** 45 minutes
**Location:** Gateway Pavilion, Level 1, Cowell Theater
**Video:** [On-Demand](https://medius.microsoft.com/Embed/video-nc/5a21e754-8418-4276-9e66-5041ed2f019d) | [Download](https://medius.microsoft.com/video/asset/HIGHMP4/5a21e754-8418-4276-9e66-5041ed2f019d)

## Summary

Steinberger presents the meta-development philosophy behind OpenClaw's rapid evolution: **don't just use AI agents — build the tools that make AI agents more effective.** The talk walks through a concrete ecosystem of automation tools born from specific frustrations in maintaining a 10,000+ issue open-source project with AI agents.

## Core Philosophy

In the age of coding agents, the bottleneck shifts from "writing code faster" to "helping agents build faster and close feedback loops more efficiently." The central question: **how can developers build infrastructure that compounds agent productivity?**

> Each tool was born from a specific frustration — "annoyance signals opportunity for optimization and innovation."

## The Tool Ecosystem

### Close Reaper — Automated Issue Management
When OpenClaw's GitHub issues exploded beyond 10,000, Steinberger built **Close Reaper** to automatically review, group, and close issues. By integrating project vision documents and clear automated rules, the system closed ~15,000 issues autonomously. It updates weekly through continuous code-agent reevaluation, ensuring lingering issues are resolved without direct human review.

### Disk Crawl — Discord Community Crawler
To collect data from community chats, built a Discord crawler that stores structured outputs directly in GitHub repositories for transparency and safe backup. This enables better management dashboards integrating both GitHub and Discord discussions to highlight true maintenance contribution beyond code commits.

### Release Bar — Version Recency Tracker
Visually tracks version recency to guide release timing — a small helper tool that compounds to accelerate overall productivity.

### Octopus — GitHub API Token Balancer
A persistent issue was hitting GitHub's API rate limits when running multiple agents. **Octopus** is a token-balancing layer using both user and GitHub App tokens to prevent throttling across parallel agent sessions.

### Crab Box — Isolated Cloud Test Infrastructure
When tests became computationally expensive, introduced **Crab Box** — spins up isolated cloud instances to distribute testing workloads across platforms and providers (AWS, Azure). Added GUI capabilities using VNC and computer vision support so agents could autonomously interact with user interfaces.

### Mantis — Automated Test Failure Recording
Agents record videos of test failures and fixes, turning previously manual verification into automated visualization.

### Auto Review — Iterative Self-Review
Allows coding agents to iteratively self-review until code passes test criteria. Instead of human reviewers line-checking code, agents validate their own work against defined criteria in a loop.

### Core Patch — Parallel Agent Audits
Large projects are subdivided for parallel agent-based audits. This enables scaling code review across multiple agents working simultaneously on different sections.

### Crab Fleet — Multiplayer Agent Development
Enables co-working sessions between maintainers and their agents — effectively turning debugging and coding into multiplayer experiences. Team collaboration improved as agents become collaborative partners rather than solo tools.

## Key Principles

1. **"Slop is fine"** — Tools don't need to be polished. Small tools and prototypes accelerate future builds and free up focus for higher-level creativity.
2. **Irritation as signal** — Every automation tool was born from a specific frustration. The culture treats annoyance as opportunity.
3. **Compounding returns** — Each small helper tool compounds to accelerate overall productivity. The ecosystem is greater than the sum of its parts.
4. **Agent-first infrastructure** — Build infrastructure assuming agents are the primary consumers, not humans.

## Related

- [[entities/peter-steinberger]] — Speaker
- [[concepts/agentic-engineering]] — Parent concept
- [[concepts/agentic-loop]] — The loop pattern that these tools serve
- [[concepts/harness-engineering]] — Broader harness design discipline
- [[raw/articles/2026-02-24_openai_builders-unscripted-ep1-peter-steinberger]] — Previous talk (OpenAI Builders Unscripted Ep.1)
