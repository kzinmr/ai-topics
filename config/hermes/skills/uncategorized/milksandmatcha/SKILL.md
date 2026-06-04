---
name: wiki-git-sync
description: Workflow for committing, rebasing, and pushing wiki changes to remote, handling common conflicts.
---

# Wiki Git Synchronization Workflow

Use this skill whenever committing and pushing changes to the `~/ai-topics` wiki repository.

## Context
The wiki is actively updated by multiple sessions, cron jobs, and the email watcher. Direct `git push` often fails with "rejected" errors due to remote changes. Merging via rebase is preferred to keep history linear, but conflicts frequently occur in `wiki/log.md` and `wiki/index.md`.

## Procedure

1. **Stage Changes**:
   ```bash
   cd ~/ai-topics
   git add wiki/ inbox/ config/feeds/x-@MilksandMatcha (Sarah Chieng) @0xSero co- "Back of House" (BOH) multi-agent orchestration patterns.
- **Role**: AI Agent Educator, Developer Advocate.
- **Key Concepts**: Back of House patterns, Single-Agent Ceiling, Kitchen Metaphor (Head Chef/Line Cook), Sloperator anti-pattern.
- **Notable Works**: Co-author of "Single-agent AI coding is a nightmare for engineers" (with @0xSero, April 2026).
- **Collaborators**: @0xSero (engineering lead), Zhenwei Gao, James Wang, @brickywhat (term 'sloperator'), @halleychangg (illustrations).

## Current Status
- **Depth**: L2 (Comprehensive entity with contributions and key concepts)
- **Last Updated**: 2026-04-18

## Contributions
- Co-authored "Single-agent AI coding is a nightmare for engineers" (April 2026).
- Systematized "Back of House" multi-agent patterns (5 workflows: Prep Line, Dinner Rush, Courses in Sequence, Prep-to-Plate, Gordon Ramsay).
- Identified and named the "Sloperator" anti-pattern (relying on prompt tweaking over architectural separation).
- Advocated for strict Build/Verify separation in agent workflows (Gordon Ramsay pattern).

## Related Concepts
- [[back-of-house-patterns]]
- [[single-agent-ceiling]]
- [[agent-vs-rlm-comparison]] (BOH vs RLM)