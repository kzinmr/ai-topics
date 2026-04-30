---
title: Boris Cherny
type: entity
created: 2026-04-13
updated: 2026-04-28
tags:
  - person
  - x-account
  - ai
  - coding-agents
  - claude-code
  - openai
  - typescript
  - anthropic
  - meta
sources: []
---

# Boris Cherny

| | |
|---|---|
| **X/Twitter** | [@bcherny__](https://x.com/bcherny__) |
| **GitHub** | [bcherny](https://github.com/bcherny) |
| **Blog** | [borischerny.com](https://borischerny.com/) |
| **Role** | Creator of Claude Code, OpenAI |

## Bio

Boris Cherny is the creator of **Claude Code**, Anthropic's agentic coding CLI. He is one of the most influential voices in practical AI agent workflows, known for deep technical insights on parallel agent execution, terminal optimization, and the philosophy that **"there is no one right way to use Claude Code."**

A self-taught programmer who studied economics at UCSD (2009–2011) but dropped out to launch startups at age 18. His career spans frontend architecture at scale (Meta/Instagram IC8), open-source contributions (Flow, Undux, TypeScript book), and now AI-assisted development tools. He describes LLMs as **"alien life forms"** and joined Anthropic specifically to contribute to AI safety and alignment.

## Career Timeline

| Period | Role | Company | Key Contributions |
|---|---|---|---|
| ~2011–2017 | Software Engineer | Startups, hedge fund, nonprofit | Founded startup at 18; developed Undux (React state management); wrote TypeScript book; started SF TypeScript meetup |
| Nov 2017–2021 | Engineer IC4→IC5 | Meta (Facebook) | "Chats in Groups" project — integrated Messenger into FB Groups |
| 2021–2023 | Staff Engineer IC6 | Meta (Facebook) | Led Facebook Groups → Comet platform migration; managed 30+ engineers; relay mutations for UI state |
| 2023–Aug 2024 | Senior Staff IC7→IC8 | Meta / Instagram | "Public Groups" initiative; scoped work for 100s of engineers; Instagram Python→Hack migration |
| Sep 2024–Jul 2025 | Founding Engineer | Anthropic | Prototyped and built Claude Code; drove 67% PR throughput increase |
| Jul 2025 | Brief departure | Anysphere (Cursor) | Senior role |
| Jul 2025–present | Head of Claude Code | OpenAI (acquired from Anthropic) | Leading Claude Code development |

## Early Career & Open Source

- **Undux** — Developed a simpler alternative to Redux for React state management; became widely adopted internally at Meta.
- **TypeScript Book & Community** — Authored an early TypeScript book (~2014–2015); started the **SF TypeScript meetup**.
- **Flow** — Core contributor to Facebook's static type checker for JavaScript — focused on type inference, gradual typing, and developer tooling. This background informed his approach to structured agent outputs in Claude Code.

## Claude Code Development

See full story: [[boris-cherny--claude-code-development|Claude Code Development Story]]

Boris joined Anthropic in September 2024, prototyping a CLI tool that evolved into Claude Code. By November 2024, an internal release saw **50% engineering adoption in 5 days**. The tool reached general availability in May 2025 and later moved to OpenAI when Boris became Head of Claude Code.

## Core Ideas & Philosophy

See full details: [[boris-cherny--core-ideas|Core Ideas & Philosophy]]

Key themes:
- **Parallel Agent Execution** — Run 3-5 Claude sessions simultaneously using git worktrees
- **Plan Mode → Auto-Accept** — Invest in planning for one-shot execution
- **CLAUDE.md as Team Infrastructure** — Shared agent memory checked into git
- **Claude Self-Verification** — Give Claude a way to verify its own work (Chrome extension, test suites)
- **Subagents for Parallel Compute** — Delegate background tasks to keep context clean
- **MCP Integration** — Connect Claude to BigQuery, Slack, Sentry via MCP servers
- **Slash Commands for Repetition** — If you do something more than once a day, turn it into a skill

## Key Work & Impact

See full details: [[boris-cherny--key-work|Key Work & Impact]]

- Creator of **Claude Code** — SWE-bench Verified: 72.7%, 300%+ user growth, 5.5x revenue expansion
- **ChernyCode** — Reference config repository for agentic engineering patterns
- Core contributor to **Flow** type checker
- Set industry benchmarks for AI-assisted programming, prompting shifts at GitHub Copilot and Cursor

## X Activity Themes

- **Claude Code tips and tricks** — Terminal setup, renderer optimization, worktree workflows
- **Parallel agent patterns** — Running 3-5 sessions simultaneously, shell aliases, coordination
- **Product philosophy** — "There is no one right way to use Claude Code"
- **Feature announcements** — New capabilities, experimental modes, subscription changes
- **Developer experience** — Terminal behavior, mouse support, text selection, notifications

## Key Quotes

> "There is no one right way to use Claude Code -- everyones' setup is different. You should experiment to see what works for you!"

> "Run 3–5 Claude sessions simultaneously using git worktrees or separate checkouts."

> "Parallel Execution is the #1 Unlock."

> "Opus 4.5 with thinking mode. It's slower than Sonnet but smarter, requires less steering, and ends up faster in real use."

> "After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.' Claude is eerily good at writing rules for itself."

> "The most underrated step. Give Claude a way to verify its work."

## Related

- [[concepts/harness-engineering]]
- [[ryan-lopopolo]]
- [[simon-willison]]
- [[concepts/karpathy]]

## Sources

- ["I'm Boris and I created Claude Code" (Jan 2026)](https://readwise.io/reader/shared/01kgcamtex6zews0fvz94a8qg4/) — Original thread about personal Claude Code setup
- ["How the Claude Code team really works" (Feb 2026)](https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works) — 10 tips from Boris's team
- [ChernyCode Repository](https://github.com/meleantonio/ChernyCode) — Curated config files from Boris's dev environment
- [How the Creator of Claude Code Uses Claude Code (paddo.dev)](https://paddo.dev/blog/how-boris-uses-claude-code/) — Detailed workflow analysis
- [Thread Reader App: Boris Cherny's Threads](https://threadreaderapp.com/user/bcherny) — Comprehensive collection of Claude Code insights
- [borischerny.com](https://borischerny.com/) — Personal blog

## References

- chermycode-boris-cherny-dev-env
