---
title: OpenAI Codex (AI coding agent)
type: entity
aliases: [codex-cli, openai-codex, codex-agent]
created: 2026-05-07
updated: 2026-06-02
status: L3
tags:
  - entity
  - coding-agent
  - openai
  - open-source
  - developer-tooling
  - ai-agents
  - enterprise-ai
  - case-study
  - mcp
  - figma
  - frontend
  - skyscanner
  - dagster
sources:
  - https://github.com/openai/codex
  - https://developers.openai.com/codex/cli
  - https://openai.com/codex/
  - https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)
  - https://developers.openai.com/codex/changelog
  - https://openai.com/index/introducing-codex/
  - https://openai.com/index/gartner-2026-agentic-coding-leader
  - https://openai.com/index/virgin-atlantic
  - raw/articles/simonwillison.net--2026-apr-28-openai-codex--558b4b74.md
  - raw/articles/2026-04-30_codex-cli-0-128-0-goal.md
  - raw/articles/openai.com--index-work-with-codex-from-anywhere--2026-05-16.md
  - raw/articles/openai.com--index-gartner-2026-agentic-coding-leader--3f8a2c71.md
  - raw/articles/openai.com--index-virgin-atlantic--7b2d9e41.md
  - raw/articles/2025-10-10_openai-developers-blog_codex-at-devday.md
  - raw/articles/2025-10-27_openai-developers-blog_codex-for-documentation-dagster.md
  - raw/articles/2026-03-01_openai-developers-blog_building-frontend-uis-with-codex-and-figma.md
  - raw/articles/2026-01-11_openai-developers-blog_skyscanner-codex-jetbrains-mcp.md
  - raw/concepts/openai-codex-superapp.md
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
related:
  - "[[concepts/openai-codex-superapp]]"
  - "[[entities/claude-code]]"
  - "[[entities/opencode]]"
  - "[[entities/pi]]"
  - "[[entities/openai]]"
  - "[[comparisons/agent-harnesses]]"
  - "[[concepts/gpt-models]]"
---

# OpenAI Codex (AI coding agent)

> **OpenAI Codex** is a lightweight, open-source AI coding agent that runs locally in your terminal — available as CLI, desktop app (macOS/Windows), IDE extensions, and web interface (chatgpt.com/codex). Built in **Rust** (96.2%), Apache-2.0 licensed, 79.3K GitHub stars. Supports **multi-model** via config.toml including GPT-5, custom providers, and local models.

## Basic Information

| Field | Value |
|------|------|
| Developer | OpenAI |
| Repository | [openai/codex](https://github.com/openai/codex) |
| Language | Rust (96.2%), TypeScript, Python |
| License | Apache-2.0 |
| GitHub Stars | ~79.3K (May 2026) |
| Initial Release | April 2025 (Codex CLI) |
| Desktop App | February 2026 (macOS, Windows) |
| Installation | `npm i -g @openai/codex` or `brew install --cask codex` |
| Official Site | [openai.com/codex](https://openai.com/codex) |

> **Important distinction**: This entity is about the **Codex AI agent** (CLI/desktop coding tool). Do not confuse with the older **Codex language model** (GPT-3-derived code model, now deprecated). Also distinct from Codex Web (the cloud agent at chatgpt.com/codex).

## Key Features

### CLI Features
- **TUI** — Interactive terminal UI with syntax highlighting, themes, `/model` switching
- **Multi-model** — GPT-5.5, GPT-5.4, GPT-5.3-Codex-Spark, plus **custom providers** via config.toml (DeepSeek, Qwen, Ollama, LM Studio, MLX)
- **Image inputs** — Screenshots, design specs read alongside prompts
- **Image generation** — Generate/edit images directly in CLI
- **Local code review** — Each run as its own transcript turn
- **Forking** — Fork sessions into new threads preserving transcript
- **`/goal` command** (v0.128.0+) — Autonomous looping until goal completion (Ralph loop pattern)

### Desktop App (macOS/Windows)
- **Parallel agent threads** — Project sidebar, thread list, review pane
- **Built-in worktrees** — Cloud environments for multi-project work
- **Thread automations** — Scheduled wake-up of same thread preserving context
- **Handoff** — Transfer context between CLI and desktop
- **Computer use** — Operate macOS apps by seeing, clicking, typing

### Mobile Launch (May 2026)

Codex launched in the **ChatGPT mobile app** (preview, May 14, 2026), making it the first major coding agent on iOS and Android. Connects to host machines via secure relay layer; full feature parity (threads, approvals, model switching). **4M+ weekly active users** confirmed at launch. Enterprise-ready: connects to managed remote environments with compliance controls.

> Source: [Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere/) (May 2026)

### Multi-Agent Features
- **Sub-agents** — Parallel worktrees for weeks of work in days
- **Auto-Review Mode** — Guardian agent for code and PR review
- **Skills System** — Agent Skills standard (agentskills.io), progressive disclosure
- **Plugin Marketplace** — Workflow packaging for skills and apps
- **MCP dual support** — Sub-agents use MCP

## Model Support

**Common misconception**: Codex is frequently reported as single-model/closed-source. **It is not.** Codex CLI is Apache-2.0 and supports:

| Tier | Models | How |
|------|--------|-----|
| 🥇 Native | GPT-5.5, GPT-5.4, GPT-5.3-Codex-Spark | Included with ChatGPT Plus/Pro/Team/Enterprise |
| 🥇 Custom API | DeepSeek, Qwen, Gemini, Claude (via API key) | `config.toml` custom providers |
| 🥇 Local | Ollama, LM Studio, MLX | Local endpoint configuration |
| 🥇 Codex-mini | o4-mini tuned for Codex CLI | Faster, low-latency, default model |

## Running Codex Safely (May 2026)

OpenAI published detailed guidance on deploying Codex safely within enterprise environments, covering **sandboxing, approval policies, managed network access, and agent-native telemetry**. Key principles: bounded execution (sandbox defines write/network boundaries), frictionless low-risk actions, explicit approval for dangerous commands, and agent-native telemetry via OpenTelemetry logs feeding into Compliance API. Security features include auto-review mode, managed network policies, command-level rules, and OAuth credentials stored in OS keyring. A detailed Windows sandbox post covers the evolution to a multi-binary elevated sandbox with `CreateRestrictedToken` + Windows Firewall isolation.

> Sources: [Running Codex safely](https://openai.com/index/running-codex-safely) | [Windows sandbox](https://openai.com/index/building-codex-windows-sandbox) (May 2026)

## Pricing

- **ChatGPT Free/Go**: Codex included (limited)
- **ChatGPT Plus/Pro ($20-200/mo)**: Double rate limits for Codex
- **Business/Enterprise**: $0 seat fee through June 2026 promotion
- **BYOK**: Use own API keys for custom providers

## Enterprise Recognition

OpenAI was named a **Leader** in the Gartner Magic Quadrant for Enterprise AI Coding Agents (May 2026). Enterprise adoption: **4M+ weekly active users**, customers include Cisco, Datadog, Dell, NVIDIA. GSI partners: Accenture, Capgemini, Cognizant, Infosys, PwC, TCS. Recent features: Codex Security + GPT-5.5-Cyber, Remote SSH, HIPAA compliance, Codex on Amazon Bedrock.

> Source: [Gartner 2026 agentic coding leader](https://openai.com/index/gartner-2026-agentic-coding-leader) (May 2026)

## Case Studies

### Virgin Atlantic (May 2026)

Virgin Atlantic used Codex to ship a revamped mobile app with **near-complete unit test coverage and zero P1 defects at launch** -- hitting the critical Christmas travel window. Neil Letchford (VP of Digital Engineering) reported:

| Metric | Result |
|--------|--------|
| Codebase size reduction on legacy refactors | 78-80% |
| Unit test coverage on new app | ~100% |
| Legacy refactoring time | 30 min (down from 2 weeks) |

**Key outcomes:**
- **Mobile app launch**: Beta over Christmas, production within weeks, zero P1 tickets
- **Legacy code modernization**: Multi-year codebases refactored in hours instead of weeks
- **Front-end velocity**: Lead developer built complete working app from Figma prototype in one week
- **Data platform**: Analyst teams now prototype internal apps directly against the data warehouse in hours -- teams across network planning, customer experience, and maintenance build their own tools with Codex

> "The trajectory of Codex is thinking beyond pure engineers. It's moving into a real tool for everyone." -- Richard Masters, VP of Data and AI, Virgin Atlantic

> Source: [How Virgin Atlantic ships faster with Codex](https://openai.com/index/virgin-atlantic) (OpenAI Blog, May 22, 2026)

### OpenAI DevDay 2025 (October 2025)

The OpenAI team used Codex across **every aspect of DevDay 2025** -- from stage demos to arcade cabinets. Key examples:

- **Venue control MCP**: Romain Huet had Codex implement the VISCA protocol for a network-enabled camera and build an MCP server to control stage lighting -- all in a single afternoon without touching the keyboard
- **Beat pad app**: Katia Gil Guzman used [[entities/codex|Codex Cloud]] with best-of-N to iterate on multiple beat pad designs in parallel for the Apps SDK demo
- **Arcade game prototyping**: Kevin Whinnery ran **7 parallel Codex CLI instances** -- each building a single-file Phaser game -- to produce the ArcadeGPT game library asynchronously
- **Demo app rebuild**: A Streamlit app was converted to FastAPI + Next.js by firing off the task to Codex and returning to a working application after lunch
- **Booth demo + evals**: Erika Kettleson fed a sketch into Codex to build the UI, wrote evals to select the best model for SVG generation, refactored to a single-agent architecture, and generated Mermaid diagrams for booth documentation
- **Documentation at scale**: Codex Cloud split fragmented Google Docs/Notion files into structured MDX docs with navigation and deploy previews

> Source: [How Codex ran OpenAI DevDay 2025](https://developers.openai.com/blog/codex-at-devday/) (OpenAI Developers Blog, October 10, 2025)

### Dagster Labs -- Documentation Automation (October 2025)

At [[entities/dagster|Dagster Labs]], the documentation team uses Codex to accelerate technical content for data engineers across multiple formats:

- **CONTRIBUTING.md as AI scaffolding**: A well-structured CONTRIBUTING.md file serves as both human guidelines and AI context, enabling Codex to understand the monorepo hierarchy and writing conventions
- **Monorepo leverage**: File references (`@`) give Codex entry points into subdirectories; having framework code alongside docs lets Codex read source and draft documentation scaffolds automatically
- **PR explanation for writers**: Developer advocates use Codex with the `gh` command to review pull request diffs and summarize how new features should be documented for end users (e.g., [dagster-io/dagster #32558](https://github.com/dagster-io/dagster/pull/32558))
- **Content translation**: Tutorials are translated into YouTube transcripts, blog posts, and other formats -- saving hours of rewriting while keeping messaging consistent
- **Documentation coverage evaluation**: Codex generates code purely from docs, and if test suites pass on the generated code, it signals that documentation has adequate coverage for human developers too

> Source: [Using Codex for education at Dagster Labs](https://developers.openai.com/blog/codex-for-documentation-dagster/) (OpenAI Developers Blog, October 27, 2025)

### Skyscanner -- JetBrains MCP Integration (January 2026)

At [[entities/skyscanner|Skyscanner]], engineers integrated Codex CLI with JetBrains IDEs via the [[concepts/model-context-protocol|MCP]] server, giving the AI access to the same feedback loops developers use:

- **Immediate error detection**: When Codex generated incorrect Java code (e.g., a Databricks SDK constructor mismatch), the JetBrains MCP's `get_file_problems` tool caught the compilation error instantly -- instead of the default multi-step loop of generating code, running tests, parsing failures, and retrying
- **Predefined run configurations**: Codex discovers and executes IDE-defined test, lint, and format commands directly, eliminating the need for the agent to figure out how to run tooling from scratch
- **Agent instructions pattern**: A custom instruction block tells Codex to run problems check, formatting, and linting after every code edit -- creating a tight generate-check-fix cycle that reduces back-and-forth prompts

**Results**: Higher first-try success rates, fewer user interventions, and Codex feeling "much more like collaborating with an AI pair programmer that can see what we see."

> Source: [Supercharging Codex with JetBrains MCP at Skyscanner](https://developers.openai.com/blog/skyscanner-codex-jetbrains-mcp/) (OpenAI Developers Blog, January 11, 2026)

### Figma-to-Code Frontend Generation (March 2026)

OpenAI launched the **Figma MCP server** for Codex, enabling bidirectional design-to-code workflows:

- **Design to code**: Copy a Figma frame selection URL, paste it into Codex, and the `get_design_context` MCP tool extracts layouts, styles, and component information to generate code that respects existing design systems
- **Code to canvas**: The `generate_figma_design` tool captures live application UI and converts it into fully editable Figma frames -- enabling teams to bring real, functioning UI onto the canvas for collaborative exploration
- **Roundtrip iteration**: Designers refine UI in Figma (adjusting styles, adding components, exploring alternatives), then pull changes back into code via the same MCP server -- creating a fluid loop between design exploration and working code

> Source: [Building frontend UIs with Codex and Figma](https://developers.openai.com/blog/building-frontend-uis-with-codex-and-figma/) (OpenAI Developers Blog, March 1, 2026)
