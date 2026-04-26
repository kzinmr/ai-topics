---
title: "Main-Branch Development"
type: concept
created: 2026-04-13
updated: 2026-04-13
tags: [git, main-branch, branching-strategy, agentic-engineering, atomic-commits]
aliases: ["main-branch-ai-development", "worktree-anti-pattern", "atomic-commits-with-agents", "steipete-git-patterns"]
related: , [[concepts/inference-speed-development]], [[concepts/direct-prompting-philosophy]], [[concepts/claude-code-best-practices]]
sources:
  - url: "https://steipete.me/posts/2025/live-coding-session-building-arena"
    author: "Peter Steinberger (@steipete)"
    date: "2025-09-06"
    title: "Live Coding Session: Building Arena"
  - url: "https://steipete.me/posts/2025/optimal-ai-development-workflow/"
    author: "Peter Steinberger (@steipete)"
    date: "2025-08-25"
    title: "My Current AI Dev Workflow"
---

# Main-Branch Development

**Main-Branch Development** is an AI-assisted software development pattern where developers work directly on the `main` branch instead of using feature branches or worktrees. This approach leverages Git's safety net (frequent atomic commits, easy rollback) while eliminating the coordination overhead of branching — particularly effective when AI agents handle implementation.

> "Yes, all of these work on main. I tried the whole worktree setup, just slows me down." — Peter Steinberger

---

## Why Main-Branch with AI Agents

### Traditional Branching vs. Main-Branch

| Aspect | Feature Branches | Main-Branch |
|--------|-----------------|-------------|
| **Merge conflicts** | Frequent, complex | None (single branch) |
| **Context switching** | High (branch per feature) | Low (atomic commits per feature) |
| **Review overhead** | PR process required | Post-commit review |
| **Agent coordination** | Complex (which branch?) | Simple (always main) |
| **Rollback** | Branch delete | `git revert` |
| **Testing** | Branch-specific deploys | Always deployable main |

### The AI Advantage
AI agents excel at **atomic, focused work**. When given a clear task scope, they produce self-contained changes that can be committed immediately. The traditional branching rationale (isolating incomplete work) becomes less relevant when:
- Agents produce working code in single sessions
- Human review happens post-generation
- Rollback is one command away

---

## The Pattern in Practice

### 1. Task Scoping
Break work into **small, independent chunks** that can be completed in one agent session:
- "Add the arena_cache table" (database)
- "Implement the compatibility scoring algorithm" (logic)
- "Build the results table UI" (frontend)
- "Add streaming response handling" (infrastructure)

### 2. Atomic Commits
Each chunk gets its own commit:
```bash
# Agent completes task → human reviews diff → commit
git add arena_cache.sql
git commit -m "feat: add arena compatibility scoring cache table"

# Next task → next commit
git add scoring.py
git commit -m "feat: implement pairwise and team scoring algorithm"
```

### 3. Safety Nets
- **Git history** provides unlimited undo
- **Frequent commits** mean small rollback scope
- **Atomic changes** make `git revert` clean and safe

---

## Anti-Patterns Steipete Avoids

### 1. Worktree Complexity
> "I tried the whole worktree setup, just slows me down. If you pick areas of work carefully you can work on multiple areas without much cross-pollination."

**Why worktrees fail with AI agents:**
- Context switching between worktrees is slow
- Agents don't benefit from parallel branch isolation
- Merge conflicts still happen when integrating
- Single dev server works better with one working directory

### 2. Manual Approval Gates
> "Manual approvals for agent actions? No. That becomes 'Windows Vista prompts.' Use Git + backups; review diffs; move fast."

**The friction problem:**
- Each approval breaks the agent's flow
- Human review time > agent generation time
- Git provides safety without gating

### 3. Elaborate Branch Strategies
> "Work on main, commit surgically. You still get speed with safety. Backups + Git are your safety net."

Traditional git flow (feature → develop → main) adds overhead that AI agents don't need. The agent produces working code; human validates; commit.

---

## When Main-Branch Works Best

| Condition | Why It Helps |
|-----------|--------------|
| **Solo developer** | No team coordination overhead |
| **AI-generated code** | Small, atomic changes |
| **Frequent commits** | Easy rollback if needed |
| **Good test coverage** | Safety net for direct commits |
| **CI/CD pipeline** | Automated validation on each commit |

### When to Use Branches Instead
- **Team collaboration** (multiple developers on same codebase)
- **Long-running features** (weeks of work, not sessions)
- **Experimental refactors** (high risk of breaking changes)
- **Release management** (staged rollouts, hotfixes)

---

## The Arena Case Study

Steipete's **Arena** feature demonstrates the pattern:

**Task:** Build a live compatibility scoring feature for 2-4 Twitter/X users
**Time:** ~1 hour from concept to deployed feature
**Approach:** Direct main-branch development

### Breakdown:
1. **Database**: `arena_cache` table migration (atomic commit)
2. **API**: Tweet fetching pipeline (atomic commit)
3. **Logic**: Profile analysis + scoring (atomic commit)
4. **UI**: User picker + results table (atomic commit)
5. **Infrastructure**: Background worker + streaming (atomic commit)

Each step was completed, committed, and moved to the next — no branching, no PRs, no merge conflicts.

---

## Connection to Other Patterns

### [[concepts/inference-speed-development]]
Main-branch development enables the fast iteration cycle:
- **No branch switching** → faster task transitions
- **Atomic commits** → clear iteration boundaries
- **Git safety** → confidence to move fast

### [[concepts/direct-prompting-philosophy]]
Both patterns reject unnecessary complexity:
- Skip the orchestration → direct prompting
- Skip the branching → main commits
- Trust the agent + git to keep things safe

### [[concepts/claude-code-best-practices]]
Complements Claude Code patterns:
- Sub-agents work on isolated tasks → atomic commits
- Human reviews output → post-commit validation
- Session hygiene → clean commit history

---

## Practical Checklist

### Before Starting a Task
- [ ] Is this task self-contained enough for one commit?
- [ ] Do I have a backup (git history, remote)?
- [ ] Can I test this independently?

### During Development
- [ ] Am I making atomic changes?
- [ ] Is the commit message descriptive?
- [ ] Should I break this into smaller commits?

### After Completion
- [ ] Did I review the full diff?
- [ ] Do tests pass?
- [ ] Is the deploy successful?

---

## Related Concepts

- [[concepts/inference-speed-development]] — Why fast iteration requires simple branching
- [[concepts/direct-prompting-philosophy]] — Anti-complexity mindset applied to Git
- [[concepts/claude-code-best-practices]] — Atomic commits enable sub-agent delegation
-  — How AI changes traditional development workflows

## Sources

- [Peter Steinberger: Live Coding Session: Building Arena](https://steipete.me/posts/2025/live-coding-session-building-arena) — Arena feature built in ~1 hour on main
- [Peter Steinberger: My Current AI Dev Workflow](https://steipete.me/posts/2025/optimal-ai-development-workflow/) — "Yes, all of these work on main"
- [Peter Steinberger: Just Talk To It](https://steipete.me/posts/2025/just-talk-to-it) — "I tried the whole worktree setup, just slows me down"
