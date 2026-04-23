---
title: WorkOS FGA: The Authorization Layer for AI Agents
category: other
status: active
---

# WorkOS FGA: The Authorization Layer for AI Agents

**Source:** WorkOS Blog
**Date:** April 13, 2026

## Overview

As AI agents operate at machine speed within enterprise infrastructure, traditional authorization patterns (OAuth tokens, session cookies, service account keys) are proving inadequate. WorkOS introduces **Fine-Grained Authorization (FGA)** — an extension of RBAC that applies roles to resource hierarchies rather than globally.

## The Confused Deputy Problem

A critical architectural risk where an agent with legitimate permissions is tricked into misusing authority.

### Example: Cluster Debug Agent

The agent has secrets:read permission. A developer asks: "Diff production env vars against staging". Result: production API key leaked.

**Key insight:** No misconfiguration occurred. The system failed because it didn't check the **intersection of their privileges**.

## Agents: A Distinct Identity Class

The industry is building agent identity infrastructure:
- **Microsoft Entra Agent ID** — Native identity class
- **NIST** — Concept paper on agent identity (Feb 2026)
- **IETF** — Standardizing `/Agents` resource in SCIM

## The Intent Gap

| Traditional Service Accounts | AI Agents |
|------------------------------|-----------|
| Deterministic scope | Non-deterministic scope |
| Fixed access defined once | Generate intent dynamically |
| Never change | Need different permissions today vs tomorrow |

## Two Modes of Agent Authorization

### 1. On-Behalf-Of (OBO) Agents

Operate within a user's session (e.g., Claude Code, GitHub Copilot).

**Requirement:** *Scope Attenuation* — Agent should access only a subset of user's permissions.

**Current problem:** Most OBO agents inherit the user's full access token.

### 2. Autonomous Agents

Operate without a user loop (e.g., security bots, billing agents).

**Problem:** "God Mode" — A billing agent with `Files.Read.All` can read invoices, employee contracts, and patent drafts.

## Why Flat RBAC Fails

Traditional RBAC maps subject → role → global permissions. Agent access correlates to tasks (transient, specific), not job titles (stable, broad). This triggers **combinatorial explosion**: O(1) roles → O(N × M) roles.

## The Fix: FGA = RBAC + Hierarchy

FGA attaches roles to specific nodes in a resource graph. Properties:
1. **Vertical inheritance:** `Editor` on `Branch: feature-xyz` grants access to everything inside
2. **No lateral movement:** Permission doesn't bleed to `Branch: staging` or `Repository: API`

## How FGA Solves Both Agent Modes

### Solving OBO Agents: Intersection Check

Both user AND agent must have access before granting a request.

### FGA as the logic layer for MCP

RAR provides structured intent (`{"file": "main.rs", "action": "edit"}`), but FGA provides the decision engine that validates against the organization's permission graph.