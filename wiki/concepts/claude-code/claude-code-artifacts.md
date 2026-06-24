---
title: "Claude Code Artifacts"
type: concept
created: 2026-06-24
updated: 2026-06-24
tags:
  - claude-code
  - anthropic
  - developer-tooling
  - artifacts
sources:
  - https://claude.com/blog/artifacts-in-claude-code
---

# Claude Code Artifacts

**Claude Code Artifacts** is a feature (beta, Team/Enterprise plans) that allows Claude Code to generate functional HTML pages that can be shared with others. Artifacts go beyond static documentation — they are interactive, live HTML pages with embedded functionality.

## Overview

Artifacts in Claude Code enable users to create:

- **PR walkthroughs** — Interactive summaries of pull request changes with visual diffs and explanations
- **Living project dashboards** — Real-time status pages for project health, build status, and milestones
- **Shareable prototypes** — Functional UI mockups that team members can interact with
- **Documentation with functionality** — Technical docs that include live examples, calculators, or interactive diagrams

## Key Characteristics

- **HTML-based**: Artifacts are standard HTML pages with embedded JavaScript functionality
- **Shareable**: Can be shared with teammates (unlike transient Claude Code outputs)
- **Functional**: Not just static content — artifacts can include interactive elements, data visualization, and logic
- **Beta/Enterprise**: Currently in beta for Team and Enterprise plan subscribers

## Relationship to Claude Code Ecosystem

Artifacts integrate with Claude Code's broader feature set:

- Complements [[concepts/claude-code/claude-code-skills]] — skills provide reusable instruction bundles; artifacts provide shareable output
- Related to [[concepts/claude-code/claude-code-auto-mode]] — auto-mode can generate artifacts as part of automated workflows
- Extends Claude Code's output capabilities beyond terminal/Slack into persistent web pages
- See also: [[concepts/claude-code/claude-code-goal]] — artifacts can serve as deliverables for delegated tasks
