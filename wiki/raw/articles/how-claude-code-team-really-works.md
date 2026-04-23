---
title: How the Claude Code team really works
category: other
status: active
---

# How the Claude Code team really works

**Source:** https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works
**Date:** Feb 5, 2026
**About:** Tips from Boris Cherny, the creator of Claude Code

## 10 Tips from Boris Cherny's Team

### 1. Do more in parallel
Spin up 3-5 git worktrees, each running its own Claude session. The team's single biggest productivity unlock.

### 2. Start every complex task in plan mode
Pour your energy into the plan so Claude can one-shot the implementation. If something goes sideways, stop and re-plan — don't keep pushing.

### 3. Invest in your CLAUDE.md
After every correction, end with: "Update your CLAUDE.md so you don't make that mistake again." Claude is eerily good at writing rules for itself.

### 4. Create your own skills and commands
If you do something more than once a day, turn it into a skill. Commit them to git.

### 5. Use subagents
Append "use subagents" to any request where you want more compute. Offload tasks to keep your main context window clean.

### 6. Don't micromanage how
Claude fixes most bugs by itself. Paste a Slack bug thread and say "fix." Or just say "go fix the failing CI tests."

### 7. Level up your prompting
Two patterns worth stealing:
- "Grill me on these changes and don't make a PR until I pass your test"
- "Knowing everything you know now, scrap this and implement the elegant solution."

### 8. Terminal setup matters
Use /statusline to show context usage and git branch. Color-code terminal tabs. Try voice dictation (fn x2 on Mac) — you speak 3x faster than you type.

### 9. Use Claude for data & analytics
The team has a BigQuery skill checked into the codebase. Boris hasn't written SQL in months.

### 10. Learn with Claude
Enable "Explanatory" output style in /config. Have Claude generate ASCII diagrams of unfamiliar codebases or visual HTML presentations of complex code.
