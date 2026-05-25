---
type: x_article
x_article_title: "How to Build a Software Factory with Claude Code That Ships Features While You Sleep"
x_article_author: "@sairahul1"
x_article_id: "2058805590043009024"
x_tweet_id: "2058832033628241931"
date: 2026-05-25
getxapi: false
source: https://x.com/i/article/2058805590043009024
tags: [claude-code, ai-agents, software-factory, agentic-workflows, vibe-coding, coding-agents, agent-team, agent-pipeline]
---

# How to Build a Software Factory with Claude Code That Ships Features While You Sleep

**Author**: @sairahul1
**Date**: 2026-05-25

## Summary

The article describes a methodology for transforming Claude Code usage from "vibe coding" (prompt → generate → error → patch → repeat) into a structured "software factory" using 7 specialized agents. Each agent has a focused role, clean context window, and scoped tools. The result: one developer + seven focused agents = a coordinated team.

## The Problem: Vibe Coding's Ceiling

The loop that feels productive but isn't:
→ Ask Claude to build a feature → It generates code → Something breaks → Paste the error back → It patches it → Something else breaks → Ask again

Day 1: feels like magic. Day 30: spending more time supervising AI than writing code.

Root cause: asking one AI session to be Product analyst + Architect + Backend engineer + Frontend engineer + Test engineer + Code reviewer — all in the same messy conversation. Wrong assumptions compound silently.

## The 7 Agents

### Agent 1: Codebase Researcher
- **Job**: Inspect codebase and explain how things work — before any code is written
- **What it does**: Maps relevant files, documents existing patterns, finds similar features, flags risks (timezone, multi-tenant, retry logic), lists tests needed
- **Tools**: Read, Grep, Glob only (read-only)
- **Rule**: Explore before you build, every single time. Runs first. Always.

### Agent 2: Story Writer
- **Job**: Turn rough feature idea into a real user story before technical decisions
- **Input**: Rough feature description + Researcher's findings
- **Output**: User story ("As a [role], I want [behavior], so that [outcome]"), acceptance criteria, edge cases, out of scope, open questions
- **Tools**: Read only
- **Rule**: Human checkpoint — read and approve story before anything else happens

### Agent 3: Spec Writer
- **Job**: Turn approved story into technical brief (blueprint)
- **Input**: Approved story + Researcher's findings + CLAUDE.md rules
- **Output**: Data model changes, API changes, frontend changes, tests required, risks, every file that will change
- **Tools**: Read, Grep, Glob only
- **Rule**: Second human checkpoint — catch architectural mistakes before any file is touched

### Agent 4: Backend Builder
- **Job**: Implement backend half — and only the backend half
- **Input**: Approved technical brief + Researcher's findings + CLAUDE.md
- **Builds**: API routes, services, business logic, database access/migrations, background jobs, unit tests
- **Cannot**: Touch React components, pages, or client-side hooks; invent new dependencies; modify outside agreed scope
- **Tools**: Read, Edit, Write, Bash — scoped to backend folders only

### Agent 5: Frontend Builder
- **Job**: Implement UI half — and only the UI half
- **Input**: Approved brief + Researcher's findings + Backend Builder's API summary
- **Builds**: React components/pages, client-side hooks/state, loading/error states, component/unit tests
- **Cannot**: Touch services, API routes, workers, migrations; invent endpoints
- **Tools**: Read, Edit, Write, Bash — scoped to frontend folders only

### Agent 6: Test Verifier
- **Job**: Prove feature actually does what the user story said (acceptance tests, not unit tests)
- **Input**: Approved story + brief + both builders' summaries
- **Output**: Acceptance test file + report (which criteria passed/failed/cannot be covered)
- **Cannot**: Modify backend or frontend code; invent workarounds for untestable criteria
- **Tools**: Read, Edit, Write (test files only), Bash

### Agent 7: Implementation Validator
- **Job**: Compare implementation against story and brief — report gaps (never fixes)
- **Checks**: Missing criteria, uncovered failure paths, security issues, files outside scope, pattern inconsistency, duplicate logic, skipped concerns
- **Output**: Grouped by severity (Critical / Important / Minor), with file path and line number
- **Tools**: Read, Grep, Glob only
- **Rule**: A self-graded paper is worthless. A validator that sees only what's on disk is honest.

## The Full Chain

```
You type: "Build invoice reminders for invoices unpaid for more than 7 days."

Step 1 → Researcher maps invoice, payment, email code
Step 2 → Story Writer produces user story + acceptance criteria
⏸ PAUSE: You approve
Step 3 → Spec Writer → technical brief
⏸ PAUSE: You approve
Step 4 → Backend Builder → API, service, BullMQ job, unit tests
Step 5 → Frontend Builder → Admin UI tile, reminder button, component tests
Step 6 → Test Verifier → Acceptance tests (7 passing, 1 failing — manual trigger missing tenant check)
Step 7 → Validator → Reports critical gap with file path + line number
→ Loop back to Backend Builder → Fix → All 8 tests pass → Validator: clean
⏸ PAUSE: You review and open PR
```

**3 human checkpoints**: Approve story → Approve brief → Approve PR

## Foundation: CLAUDE.md

A Markdown file at repo root loaded every session:
- Stack (Next.js, Node.js, Prisma, BullMQ, Resend)
- Commands (npm run dev, npm test, npx prisma migrate dev)
- Architecture rules ("Business logic lives in services. API routes stay thin.")
- What not to do ("Do not add cron — use BullMQ. Do not log raw payment payloads.")
- Pointers to deeper docs (docs/billing.md, docs/architecture.md)

Keep 100-300 lines. Every time AI makes a mistake, add a rule.

## Context Drift Rule

Small typo → correct inline. Wrong architectural assumption → throw conversation away and start fresh with right assumption baked into first prompt. A clean session with the right mental model beats a patched session every time.

## Setup Checklist (2-3 hours)

1. Install Claude Code (code.claude.com)
2. Create folder structure: .claude/agents/, .claude/skills/feature-factory/, .claude/skills/build-with-tests/, .claude/hooks/
3. Write CLAUDE.md (100-300 lines)
4. Create 7 agents via /agents command
5. Create feature-factory orchestrator skill
6. Create build-with-tests skill
7. Add pre-commit hook (blocks .env, .key, .pem, secrets.json)
8. Run one real feature through the full chain
