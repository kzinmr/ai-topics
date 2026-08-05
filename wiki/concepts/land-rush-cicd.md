---
title: "Land Rush CI/CD"
type: concept
tags:
  - ci-cd
  - agentic-engineering
  - devops
  - agent-orchestration
  - software-engineering
  - prediction
created: 2026-08-05
updated: 2026-08-05
aliases: [Land Rush, Continuous Thunderdome, Game DevOps, Thunderdome CI/CD]
sources:
  - raw/articles/2026-08-04_yegge-ai_shape-of-things-to-come.md
  - https://yegge.ai/essays/the-shape-of-things-to-come/
---

# Land Rush CI/CD

## Overview

**Land Rush** is a CI/CD pattern for agentic development where, instead of sequential merge-queue processing with bisection on failure, all accumulated commits are **smashed onto main in a single megabatch** and then repaired via **swarm diagnosis** — multiple agents simultaneously diagnosing and fixing the resulting failures.

The term was coined by [[entities/steve-yegge]] in "The Shape of Things to Come" (Aug 2026). The subtitle "The Continuous Thunderdome" evokes the Mad Max metaphor: just slam everything in and deal with it.

## The Problem: CI/CD Breaks Under Agent Load

Traditional CI/CD uses a **Merge Queue (MQ)** with batched builds and bisection on failure:

- 100 commits/day × 30 min build = 50 hours of sequential builds → solved by batching (10 batches of 10 = 5 hours)
- Failed batch → bisect, rerun each half → log(N) recovery

But with **40+ agents producing 175-250 commits/day**, the MQ grows without bound. Yegge observed the queue hitting 100+ MRs and entering infinite bisection loops with no forward progress.

### The Pigeonhole Principle

> "If you have more pigeons than holes, some hole ends up holding more than one pigeon."

Once commit rate >> build slots, one-commit-per-green-build becomes **mathematically impossible**. Agents multiply commit rate by orders of magnitude while build time stays fixed.

## The Solution: Land Rush

1. **Threshold trigger**: When MQ hits 100, abandon bisection
2. **Megabatch**: Smash all accumulated commits onto main at once
3. **Swarm diagnosis**: Multiple agents simultaneously diagnose red-main problems (not bisection)
4. **Roll forward**: Fix and commit; don't roll back

### Results (Yegge, Aug 2026)
- Successfully cleared batches of 120-150 commits
- Running daily for ~1 week at time of writing
- 166-deep MQ observed and cleared

## Historical Precedent: Game DevOps

The game industry independently arrived at the same pattern:

- Modern games have **extraordinarily long builds** (huge asset pipelines, C++ linking)
- Many developers committing all day
- Traditional MQ doesn't work → **"Game DevOps"**: everyone blasts commits to main, cut release branches, fixes propagate forward
- Perforce game-dev docs: "HEAD is never stable at AAA scale"
- Done **multiple times per day**

Game DevOps = Land Rush, discovered independently at scale.

## Why This Works

| Factor | Traditional CI/CD | Land Rush |
|--------|-------------------|-----------|
| Failure diagnosis | Bisection (sequential, log(N)) | Swarm (parallel, agents diagnose simultaneously) |
| Commit rate | Human-limited (~10-100/day) | Agent-limited (~175-250/day) |
| Main branch | Must stay green | Expected to be red; repaired in bulk |
| Recovery | Find the bad commit | Fix forward, don't blame |
| Applicability | Low commit rates | High commit rates (agent-generated) |

## Predictions

Yegge predicts:
- **CI/CD as we know it will be dead by 2027**
- The Land Rush / Game DevOps pattern becomes the norm as agent-generated commit rates increase industry-wide
- SOC 2 compliance will survive but "review" will mean rounds of **agentic code review**, not human approval

## Related

- [[entities/steve-yegge]] — Described and named the pattern
- [[concepts/wheelhouse]] — Where Land Rush was first implemented
- [[concepts/wish-factory]] — Pattern that generates even more commits
- [[concepts/agentic-engineering]] — Broader engineering discipline
- [[concepts/agent-orchestration]] — Orchestration patterns that generate high commit rates

## Sources

- https://yegge.ai/essays/the-shape-of-things-to-come/ (Aug 2026, §"The Metamorphosis of CI/CD")
