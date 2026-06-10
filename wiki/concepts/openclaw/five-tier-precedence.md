---
title: "Five-Tier Skill Precedence"
type: concept
aliases:
  - skill-precedence
  - openclaw-skill-governance
  - five-tier-precedence
created: 2026-04-18
updated: 2026-05-26
tags:
  - concept
  - openclaw
  - developer-tooling
  - architecture
  - governance
related:
  - concepts/skill-architecture-patterns
  - comparisons/hermes-vs-openclaw-architecture
  - entities/peter-steinberger
  - entities/openclaw
sources:
  - "OpenClaw VISION.md"
  - "elvis analysis (April 2026) — 9-hour side-by-side source code study"
---

# Five-Tier Skill Precedence Model

A **hierarchical precedence model** adopted by OpenClaw's skill loading system. One of the most important architectural differences when contrasted with Hermes Agent's self-authoring approach.

## Five-Tier Structure

```
1. Workspace skills     (highest priority — project-specific skills)
2. User global skills   (user global settings)
3. Managed skills       (managed skills)
4. Bundled skills       (baseline only — minimal bundled skills)
5. Extra skills         (lowest priority — additional skills)
```

## Design Principles

### Explicit > Implicit
> "Tool activation correctness is better on OpenClaw than Hermes for tasks where the agent has to pick the right CLI/API from ~50 options." — elvis

Hermes decides at runtime whether to load a given skill. OpenClaw **does not need runtime decisions because load order is determined by priority**.

### Deterministic Debugging
> "When something breaks at 3am, you can trace it in one grep instead of guessing which skill the agent triggered." — elvis

Since the five-tier hierarchy is fixed, tracing which skill fired is a single grep away. With Hermes's self-authoring skills, tracking "which skill from which folder was applied" can become difficult.

### Self-Modification Impossibility
OpenClaw's skill system does **not allow agents to create or modify skills themselves**. Explicit user intent is required. This:
- Prevents skill corpus rot (contamination)
- Minimizes security risks
- Ensures predictable agent behavior

## Anti-Bloat Policy

From OpenClaw VISION.md:

> "Bundled skills are baseline only. New skills go to ClawHub first. Core additions should be rare and require a strong product or security reason."

### Implementation Mechanisms

| Mechanism | Description |
|-----------|------|
| **Byte caps** | Byte size limits on skill content |
| **Candidate caps** | Limits on skill load candidates |
| **Symlink rejection** | Rejects symbolic links (security) |
| **Verified file opens only** | Only permits verified file opens |
| **Eligibility checks ≠ discovery** | Eligibility checks and discovery are separate — different agents can see different skill subsets |

## Comparison with Hermes

| Dimension | OpenClaw (Five-Tier) | Hermes (Self-Authored) |
|------|---------------------|------------------------|
| **Priority** | Fixed five tiers | Dynamic judgment |
| **Skill creation** | User-explicit | Agent-autonomous |
| **Debugging** | Single `grep` | Cross-skill investigation |
| **Corpus growth** | Limited (via ClawHub) | Unlimited (Skill Explosion Problem) |
| **Security** | Symlink rejection, verified files only | Prompt-based creation |

## Relationship with ClawHub

The Five-Tier model integrates with the **ClawHub marketplace**:
- New skills are submitted to ClawHub first
- Core additions require "a strong product or security reason"
- Users select and install needed skills from ClawHub
- Installed skills are placed in the appropriate tier

## Product Positioning

This model embodies OpenClaw's **"Primitives First"** philosophy:

> "You're not getting defaults, you're getting guarantees. OpenClaw does exactly what you told it to do, nothing more, nothing less."

Analogy to Linux/Kubernetes: the OS provides minimal primitives, and users assemble what they need. In contrast to opinionated full-stack frameworks like Rails.

## Related

- [[concepts/skill-architecture-patterns]] — Comparison of skill architectures with Hermes
- [[comparisons/hermes-vs-openclaw-architecture]] — Detailed architecture comparison
- [[concepts/openclaw]] — OpenClaw framework
- [[concepts/anthropic/openclaw-conflict]] — Platform risk context
- [[entities/peter-steinberger]] — Designer
