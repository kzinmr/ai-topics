---
title: "Cursor IDE"
type: concept
tags: [cursor, ide, coding-agent, ai-development]
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Cursor, Cursor Editor, Cursor AI]
related: [[entities/cursor-3]], [[concepts/harness-engineering]], [[concepts/claude-code]], [[concepts/coding-agents]]
sources: [https://cursor.com/, https://docs.cursor.com/]
---

# Cursor IDE

## Summary

Cursor is an AI-first code editor built on a modified VS Code foundation, designed from the ground up for agent-driven development. It integrates AI coding agents, predictive autocomplete (Tab), inline chat, and codebase-aware commands directly into the editing experience. In 2025-2026, Cursor has evolved significantly — the Cursor 3.0 rewrite replaced the VS Code backend with a unified workspace architecture optimized for agent execution, and features like Visual Editor/Design Mode (late 2025) and Predictive Autocomplete powered by Supermaven have set new standards for AI-assisted development.

## Key Ideas

- **AI-Native Editor**: Unlike VS Code with AI extensions bolted on, Cursor is built with AI as a first-class citizen — the editor, agent, and model are deeply integrated rather than layered
- **Cursor 3.0 (2025)**: Complete ground-up rewrite replacing the VS Code foundation with a unified workspace architecture designed for multi-agent collaboration, persistent agent memory, and agent-aware code indexing
- **Visual Editor & Design Mode**: Late 2025 feature enabling visual component editing — users can drag, drop, and visually modify UI elements while the AI maintains the underlying code, bridging design and development
- **Predictive Autocomplete (Tab)**: Powered by Supermaven, Cursor's Tab feature predicts not just the next word but entire multi-line code changes — the most frictionless form of AI assistance, working silently in the background
- **Agent Mode**: Cursor's agent can execute commands, edit multiple files, run tests, and interact with the terminal — operating as a collaborative coding partner rather than just an autocomplete tool
- **Codebase-Aware Context**: Cursor maintains a persistent index of the user's codebase, including git history, file relationships, and recent edits, enabling AI features that understand the full project context

## Terminology

- **Cursor 3**: The 2025 major version rewrite replacing VS Code foundation with a unified agent-optimized workspace
- **Supermaven**: The AI model provider powering Cursor's Predict Autocomplete (Tab) — known for ultralow latency inference
- **Visual Editor**: Component-level visual editing where users see and modify UI representation while AI syncs with source code
- **Agent Context**: The codebase-aware index that Cursor maintains — embeddings of project code, git history, file structure, and editor state
- **Composer**: Cursor's multi-file editing interface for making changes across many files simultaneously with AI guidance

## Examples/Applications

- **Full-Stack Prototyping**: A single prompt can generate a complete web application — frontend, backend, database schema, and deployment config — with the agent managing all file creation and dependencies
- **Bug Fixing**: Highlighting a buggy function and asking the agent to fix it — the agent reads the code, identifies the bug, tests the fix, and applies the correction
- **Code Migration**: Using the agent to refactor a codebase from one framework to another (e.g., React to Vue), with the agent understanding dependencies and managing all file changes
- **Visual Design Integration**: Editing UI component styles visually in Design Mode, with the AI maintaining pixel-perfect code correspondence
- **Multi-File Refactoring**: Renaming a class or function across hundreds of files, with the agent handling imports, tests, and documentation updates

## Related Concepts

- [[harness-engineering]]
- [[claude-code]]
- [[coding-agents]]
- [[entities/cursor-3]]

## Sources

- [Cursor Official Site](https://cursor.com/)
- [Cursor Documentation](https://docs.cursor.com/)
- [Cursor 3.0 Launch Blog](https://cursor.com/blog/cursor-3)
