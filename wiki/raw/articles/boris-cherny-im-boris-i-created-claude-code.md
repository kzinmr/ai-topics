# I'm Boris and I created Claude Code

**Author:** Boris Cherny
**Date:** January 2, 2026
**Source:** https://readwise.io/reader/shared/01kgcamtex6zews0fvz94a8qg4/
**Annotated by:** Antonio Mele

I'm Boris and I created Claude Code. Lots of people have asked how I use Claude Code, so I wanted to show off my setup a bit.

My setup might be surprisingly vanilla! Claude Code works great out of the box, so I personally don't customize it much. There is no one correct way to use Claude Code: we intentionally build it in a way that you can use it, customize it, and hack it however you like. Each person on the Claude Code team uses it differently.

But here's my personal setup:

## 1. Parallel Sessions
I run 5 Claude Code sessions in parallel via terminal (numbered tabs 1-5). System notifications alert me when Claude needs input.

I also run 5-10 sessions on claude.ai/code. I pass tasks between local and web using & and --teleport. I launch sessions from my iPhone every morning and check in later.

## 2. Opus 4.5 with Thinking
It's slower than Sonnet but smarter, requires less steering, and ends up faster in real use.

## 3. Shared CLAUDE.md
The team maintains a living doc checked into git. Every mistake Claude makes = logged and avoided in future. Each team member can @claude on PRs to update guidelines as part of code review.

## 4. Plan Mode
Sessions start in Plan Mode (Shift+Tab twice). Once the plan is solid, I switch to auto-accept edits. Claude usually completes the task in one shot.

## 5. Slash Commands
I create slash commands for repeat tasks I do many times a day. Commands live in .claude/commands/ and are checked into git.
Example: /commit-push-pr

## 6. MCP Integration
Claude runs logs, BigQuery queries - via MCP server. Config lives in .mcp.json.

## 7. Handle Long Tasks with Agents + Sandbox
I use background agents, stop hooks, and plugins for long-running tasks.

## 8. Claude Verifies Its Own Work
The most underrated step. Claude uses the Chrome extension to test every change it lands.

## 9. PostToolUse Hooks
Auto-formats Claude's code after edits.
