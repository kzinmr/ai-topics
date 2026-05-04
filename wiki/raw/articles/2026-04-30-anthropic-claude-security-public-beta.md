---
title: "Claude Security Public Beta — Anthropic"
source: "https://claude.com/blog/claude-security-public-beta"
date: 2026-04-30
type: raw-article
tags: [anthropic, claude, security, opus-4.7, enterprise]
---

# Claude Security Public Beta

**Date:** April 30, 2026
**Product:** Claude Security (formerly Claude Code Security)
**Status:** Public Beta for Claude Enterprise customers
**Model:** Claude Opus 4.7

## Overview
Claude Security uses Claude Opus 4.7 to scan codebases, validate findings (reducing false positives), and generate proposed patches. It operates like a human security researcher — tracing data flows, reading source code, examining interactions across files and modules.

## Key Features
- **Deep Code Reasoning:** Beyond pattern matching — traces data flows and analyzes interactions across files
- **Vulnerability Insights:** Confidence ratings, severity/impact, reproduction steps
- **Targeted Patching:** Generate fix instructions, open and apply directly in Claude Code on the Web
- **Scheduled Scans:** Move from one-off audits to regular cadence
- **Directory Targeting:** Scope scans to specific branches or folders
- **Export & Triage:** CSV/Markdown exports, dismiss findings with documented reasons
- **Webhooks:** Send results to Slack, Jira, and other tools

## Security Partner Ecosystem
Technology partners integrating Opus 4.7:
- CrowdStrike (Falcon platform)
- Microsoft Security
- Palo Alto Networks
- SentinelOne (Wayfinder AI)
- TrendAI
- Wiz (Red Agent)

Services partners: Accenture, BCG, Deloitte, Infosys, PwC

## Performance
- Claude Mythos found 271 zero-day vulnerabilities in Firefox in one sweep (~4x what Mozilla patched in all of 2025)
- Early users report moving from "scan to applied patch" in a single sitting
- Multi-stage validation pipelines ensure high-confidence findings

## Availability
- Now: Public Beta for Enterprise customers
- Coming Soon: Team and Max customers
- Available via claude.ai sidebar or claude.ai/security
