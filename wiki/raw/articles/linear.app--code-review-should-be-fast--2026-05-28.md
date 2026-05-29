# Code review should be fast — Linear Diffs Launch

**Source:** https://linear.app/now/code-review-should-be-fast
**Retrieved:** 2026-05-29
**Via:** X post by @karrisaarinen (2026-05-29)
**Archived for:** wiki knowledge base

---

## Summary

Today we're launching **Diffs**, a new way to review pull requests inside Linear.

## Why Diffs

Code review has stayed painfully slow while everything else sped up. Growing PR volumes from coding agents are putting further strain on an already creaking process. So much so that the speed gained from using agents gets swallowed in review.

**Design beliefs:**
- **Fast**: Reviews should open near-instantly
- **Focused**: Reviews should show what matters and strip out the noise
- **In context**: Code should sit next to the issue, project, and customer signal behind the change

## Core Features

### 1. Knowing what to review first
Review requests sit inside Linear next to the rest of your work, where priority is visible because everything else competing for your attention is right there too. Each Diff is attached to the issue and project that produced it.

### 2. Getting through a huge diff
**Guided reviews** break the diff into chapters that follow the order the work was reasoned through — shows the core of the change first, then walks through consequences, with auxiliary changes and glue code kept separate.

**Structural diff highlighting** strips the formatting changes that have nothing to do with what the program does, so what is left on the page is the actual change rather than the noise around it.

### 3. Piecing together why it matters
Because reviews live inside Linear, the issue, project, and customer signal that inspired the change are right there alongside them. No chase across tools.

## The new shape of review

Agents have absorbed most of the line-by-line correctness work that used to take up reviewers' time. What's increasingly left is the layer above the code itself — whether the change fits the architectural system and solves the problem the customer actually reported. **Diffs removes the friction around reviews, giving the reviewer the time and attention to do that judgement work.**

## Availability
Available on all Linear plans starting today (May 28, 2026).

---

## Key Takeaway

Linear is entering the code review space with a differentiated product — **Diffs** — designed specifically for the agent era where PR volumes are growing. The product integrates review directly into the issue/project context, uses "guided reviews" to structure large diffs logically, and strips formatting noise. This positions Linear as an end-to-end software development workspace (issues → code → review), competing with GitHub's PR review flow.
