---
source: https://x.com/DeRonin_/status/2056083767333163044
title: "Agentic Project Setup: direnv + Secrets Manager"
author: "@DeRonin_"
date: 2026-05-17
type: x_bookmark
tags: [agentic-security, ai-agents, security, devops]
---

# Agentic Project Setup: direnv + Secrets Manager

> anybody who uses or learns agentic systems, SHOULD READ THIS
>
> the install order I run before any new agentic project:
>
> 1. PRIVACY: direnv + a real secrets manager
>
> install direnv, then plug it into your team's password manager (1Password CLI via op run, doppler, infisical, vault, ...

*[Tweet truncated — photo attachment contains remaining list items]*

## Context

A tweet thread by @DeRonin_ arguing that direnv + a real secrets manager should be the first step before starting any agentic project. The thesis is that agentic systems — which often have broad filesystem and tool access — need privacy/security guardrails from the start, not as an afterthought.

The recommended setup: use direnv to manage environment variables per-project, and integrate with a team secrets manager (1Password CLI via `op run`, Doppler, Infisical, or HashiCorp Vault) to avoid hardcoding credentials or exposing secrets to agents.
