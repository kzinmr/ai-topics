---
title: "Thomas Ricouard (Dimillian)"
description: "iOS/SwiftUI developer turned Codex Developer Experience engineer at OpenAI; author of Ice Cubes (Mastodon) and CodexMonitor, with widely-read articles on agentic iOS workflows and on-device Apple Foundation Models"
type: entity
created: 2026-09-26
updated: 2026-09-26
aliases:
  - Dimillian
  - Thomas Ricouard
  - dimillian.app
tags:
  - person
  - ai-agents
  - coding-agents
  - open-source
  - developer-tools
  - ai-coding
  - timeline
sources:
  - https://dimillian.app
  - https://dimillian.app/apps
  - https://dimillian.app/articles
  - https://dimillian.app/talks
  - https://github.com/Dimillian
  - https://x.com/Dimillian
---

# Thomas Ricouard (Dimillian)

**Thomas Ricouard**, known online as **Dimillian**, is a French iOS/macOS engineer who moved from a decade of high-profile Apple-platform app work (Google Chrome iOS, Medium iOS, Glose) into **Developer Experience / Codex at OpenAI**. He is one of the most visible bridge figures between the Swift/apple developer world and the agentic-coding world: he builds open-source tools that orchestrate coding agents, and writes practitioner-level guides on agentic iOS development.

GitHub bio: *"Developer Experience, Builder, Codex @openai. Previously: @medium, @glose, @google, Co-Founded @MySeeen, @RobinBrowser."*

## Overview

- **Location**: France (entrepreneur; founder of MySeeen and RobinBrowser early in his career)
- **Current role**: Codex — Developer Experience, **OpenAI** (GitHub profile company: `@OpenAI`)
- **Stack**: Swift / SwiftUI, iOS / macOS, plus Tauri/TypeScript for cross-platform agent tooling
- **GitHub**: 175 public repos, ~4.4k followers — a prolific open-source app author rather than a library author
- **Handles**: X [@Dimillian](https://x.com/Dimillian) (31,984 followers) · Bluesky `@dimillian.app` · Mastodon `@dimillian` · Threads/Medium `@dimillian`
- **Site**: https://dimillian.app (About / Talks / Articles / Open Source / Snippets / Games)

## Career

| Period | Role | Notes |
|---|---|---|
| early career | Co-founder, MySeeen; RobinBrowser | Movie-sharing app and "smart browser" experiments |
| Google | iOS engineer | Chrome for iOS |
| Glose | iOS | Reading/social highlighting app |
| Medium | iOS engineer | Authored the Medium Engineering SwiftUI architecture series |
| 2023→ | Indie open source | Ice Cubes (Mastodon), RedditOS/Curiosity, ACHelper |
| 2025–2026 | **Codex Developer Experience, OpenAI** | Shifted focus to agent tooling and agentic workflows |

## Open-source apps

### CodexMonitor (2026) — flagship agent tool
macOS/Linux **Tauri** app for *orchestrating multiple Codex agents across local workspaces* ("An app to monitor the (Codex) situation"). MIT, TypeScript. **4,338 stars / 417 forks**, ~2 months after creation (2026-01-11), homepage codexmonitor.app. The most-starred third-party Codex orchestration UI, and the clearest example of a practitioner building *agent fleet management* on top of a vendor CLI.

### Codex Skill Manager
macOS SwiftUI app to manage local **Codex and Claude Code skills** — an early GUI for the skills format shared by both agent ecosystems.

### Ice Cubes
SwiftUI **Mastodon** client (iOS + macOS). 7,066 stars, on the App Store; his largest pre-AI project and the codebase the "Snippets" pages (SwiftUI patterns for `TabView` bindings, geometry modifiers, visionOS ornaments) are drawn from.

- **Icy Sky** (SwiftUI Bluesky client / custom-UI playground) · **Curiosity / RedditOS** (macOS SwiftUI Reddit client) · **ACHelper** (Animal Crossing companion, App Store) · **RunewordsApp** · **MovieSwiftUI** (6,529 stars — canonical SwiftUI+Combine+Redux tutorial app).

### Snippets (SwiftUI patterns)
dimillian.app/snippets collects reusable SwiftUI patterns from Ice Cubes — custom `TabView` bindings for side effects on tab selection, `onGeometryChange`-based modifiers, and visionOS `.ornament` vs `.safeAreaInset` cross-platform composition.

## Writing — AI and agentic workflows

Published at dimillian.medium.com and Medium Engineering. Recurring themes: **how far coding agents can be pushed on Apple platforms**, and honest assessment of their limits.

- **Agentic iOS Workflow with XcodeBuildMCP and Cursor** — end-to-end agent loop for iOS builds via an Xcode MCP server
- **Vibe Coding: An iOS App with Claude 4** — first-hand vibe-coding experiment on a native app
- **Working on an Xcode Project with Cursor/VSCode**; **How to use VSCode/Cursor for iOS development** — pushing iOS dev out of Xcode
- **Bringing On-Device AI to your app: Using Apple's Foundation Models**; **FoundationChat: Building an AI Chat App with iOS 26's On-Device Models** — among the earliest hands-on Apple Foundation Model tutorials
- **Is Software Engineering Over as We Know It?** / **Where is Swift Assist?** — practitioner skepticism and platform critique
- **Top 5 AI Tools for iOS Developers**; **GitHub Copilot for Xcode**
- Medium Engineering: *Building a ChatGPT Plugin for Medium*; the SwiftUI adoption and iOS architecture evolution series

## Conference talks

Swift Connection (2025), FrenchKit (2020, 2022), DotSwift (2020), UIKonf (2020, plus interview) — SwiftUI and app-architecture topics; talks listed at dimillian.app/talks.

## Notable / key ideas

- **Agent orchestration is a UX problem, not a CLI problem.** CodexMonitor exists because a fleet of parallel agents needs a control surface — monitor, diff, review, promote. This is the "harness" instinct applied to OpenAI's own tool.
- **MCP is how agentic development reaches closed ecosystems.** His XcodeBuildMCP workflow is the template for giving agents a compile/test loop in a toolchain (Xcode) that vendors did not expose to them.
- **On-device models over API dependency.** His Apple Foundation Models writing argues for local inference for privacy, cost, and offline capability — a position that sits deliberately apart from the cloud-API default.
- **Ship the tool you need.** Ice Cubes, RedditOS, ACHelper, CodexMonitor — every project started as his own requirement, which is why the tooling is unusually practical.

## Related

- [[entities/simon-willison]] — fellow practitioner-writer on agentic coding workflows
- [[entities/boris-cherny]] — Codex lead at OpenAI; Ricouard works on the Codex Developer Experience side of the same product
- [[entities/openai]] — current employer (Codex)
- [[concepts/harness-engineering]] — CodexMonitor is a concrete orchestration/harness layer around a coding agent
- [[concepts/ai-coding-tools]] · [[concepts/ai-coding-workflows]] — surfaces his articles evaluate hands-on
- [[concepts/vibe-coding]] — his "Vibe Coding: An iOS App with Claude 4" is a first-hand case study
- [[concepts/model-context-protocol]] — his XcodeBuildMCP workflow is the iOS instantiation
- [[concepts/agent-skills]] — Codex Skill Manager manages skills for Codex *and* Claude Code

## Sources

- [dimillian.app](https://dimillian.app) — About / Apps / Articles / Talks / Snippets (scraped 2026-09-26)
- [GitHub @Dimillian](https://github.com/Dimillian) + [CodexMonitor](https://github.com/Dimillian/CodexMonitor), [CodexSkillManager](https://github.com/Dimillian/CodexSkillManager), [IceCubesApp](https://github.com/Dimillian/IceCubesApp) (GitHub API 2026-09-26)
- [X @Dimillian](https://x.com/Dimillian)
