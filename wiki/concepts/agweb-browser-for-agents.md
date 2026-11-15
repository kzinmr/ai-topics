---
title: "Agweb (Browser for Coding Agents)"
created: 2026-11-15
updated: 2026-11-15
type: concept
tags: [agent-tooling, browser-automation, coding-agents, browser, cli]
sources:
  - raw/articles/2026-11-14_agweb-browser-for-agents.md
  - https://github.com/paul-nameless/agweb
  - https://news.ycombinator.com/item?id=50497147
confidence: medium
---

# Agweb

**agweb** is an open-source macOS browser purpose-built for coding agents, built on **WebKit (Safari's engine)** rather than Chromium/Playwright. Shown on HN as a Show HN (Nov 14, 2026, 100 pts), it addresses three recurring complaints about agent browser automation: focus-stealing browser windows, headless browsers being blocked by anti-bot systems, and Chromium's idle-resource cost.

## Design position

- **Never takes focus.** Agents drive a single window from the shell via the `agweb` CLI (a playwright-cli-style command); a human watches all agents live in a dashboard (⌘D) showing every tab of every agent with each agent's last command. Because it is always a real window, sites that block headless browsers still work — and failures are observable.
- **Idle-tab suspension**: five idle pages sit at 0% CPU vs Chrome's GPU process keeping 5–7 cores busy. Memory at 5 idle pages: agweb 590 MB vs headless Chrome 730 MB vs Playwright Chrome 1.6 GB.
- **Multi-agent isolation**: each agent works in its own workspace with its own tabs; named login profiles (`-p work`) are shared concurrently by every agent using them.
- **Human-like input**: clicks/keys are native macOS events with pointer movement that "moves like a hand," so hover menus and drag-and-drop work.
- **Agent-native CLI ergonomics**: snapshots tag elements with durable `[ref=eN]` handles; `snapshot --diff` and `find` return only what changed, and every action reports its own diff so no second snapshot is needed.
- **Secret hygiene**: `fill --secret-cmd 'pass show site'` types a secret that never enters the agent's transcript; 1Password/Bitwarden CLIs supported.
- **Ad/tracker blocking** via uBlock Origin lists (refreshed every 4 days), per-workspace toggleable for analytics testing.
- Session recording to MP4 with pointer/clicks drawn in (`video-start`).

Requires macOS 26+; Swift/SwiftUI app, installs a CLI and an agent skill for Claude Code/Codex.

## Significance

- A concrete instance of the **agent-native browser** category forming in late 2026 — alternative to Playwright-for-agents and computer-use loops; see [[concepts/agent-sandbox-patterns]] for the isolation-side counterpart.
- WebKit-over-Chromium is a deliberate counterpoint to the Playwright ecosystem's Chrome monoculture; native-event input sidesteps `navigator.webdriver`-style headless fingerprinting rather than fighting it.
- The "one window many agents, human supervises via dashboard" pattern matches the multi-agent parallel-worker direction Anthropic is shipping in [[concepts/anthropic/claude-code-projects]].

## Related

- [[concepts/rodney-browser-automation-cli-for-agents]] — sibling CLI browser-automation tool
- [[concepts/browser-use-production-architecture]] — production agent-browser architecture
- [[concepts/agent-sandbox-patterns]] — where browser automation runs
- [[concepts/programmatic-tool-calling]] — CLI-as-tool pattern
- [[concepts/coding-agents/_index]] — consumers of the tool
