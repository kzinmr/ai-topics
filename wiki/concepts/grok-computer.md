---
title: Grok Computer
created: 2026-05-02
updated: 2026-05-02
type: concept
tags: [ai-agents, computer-use, automation, grok, desktop-agent, inference]
sources:
  - raw/articles/2026-05-01_xai-grok-4-3-launch.md
---

# Grok Computer

**Grok Computer** is xAI's autonomous desktop AI agent that operates computers by reading screen pixels and controlling mouse/keyboard input — analogous to how Tesla's FSD uses cameras to navigate physical roads. It entered private beta on April 13, 2026.

## How It Works

- **Pixel reading**: Continuously processes the last 5 seconds of screen video to understand context and application state
- **Universal compatibility**: Works with ANY software by reading pixels — no API access needed, including legacy programs from decades ago
- **Actions**: Opens applications, navigates UIs, clicks buttons, types into fields, fills forms, executes multi-step workflows
- **Chained workflows**: Can research data → create spreadsheet → format report → send via email, all autonomously

## Architecture

Grok Computer is the **execution/action layer** paired with Grok 4.3 (the reasoning layer):
- **Grok 4.3** = Brain (reasoning, document generation, analysis, planning)
- **Grok Computer** = Hands (execution, automation, desktop control, UI manipulation)

Together they form xAI's vision of AI that actively does computer-based work — distinct from OpenAI's Codex (focused on coding) and Anthropic's Claude Code (terminal-based coding agent).

## Comparison with Other Computer Use Agents

| Feature | Grok Computer | [[concepts/claude-computer-use|Claude Computer Use]] | [[concepts/anthropic-computer-use|Anthropic Computer Use]] |
|---------|--------------|----------------------|--------------------------|
| Method | Pixel reading | Screenshot + coordinates | Screenshot + coordinates |
| Legacy SW | Full support (pixel-based) | Limited | Limited |
| Scope | Full desktop automation | Browser + desktop | Browser + desktop |
| Release | Beta Apr 2026 | Research preview Oct 2024 | GA with Sonnet 4.6 |
| Integration | Grok 4.3 reasoning | Claude model | Claude model |

## Timeline

- **Mar 20, 2026**: Feature flag `enable_grok_computer` discovered in Grok web source code
- **Mar 20, 2026**: Elon Musk confirms: "Coming Out Soon"
- **Apr 13, 2026**: Private beta goes live for select SuperGrok accounts
- **Apr 17, 2026**: Wider beta access alongside Grok 4.3 launch
- **Sep 2026 (target)**: Full rollout with "Macrohard" integration

## Access & Pricing

- Currently: Select SuperGrok accounts during beta
- Expected: Included with SuperGrok ($30/month) or higher-tier subscription
- Enterprise: "Macrohard" version with separate pricing (targeted Sep 2026)
- Grok Build: xAI's AI coding agent (separate product, announced Feb 2026)

## Strategic Significance

Grok Computer represents a fundamentally different product vision from competitors:
- **OpenAI**: ChatGPT + Codex (text/code-focused)
- **Anthropic**: Claude Code + Computer Use (developer/enterprise-focused)
- **xAI**: Grok 4.3 + Grok Computer (universal desktop automation for consumers and enterprises)

## Related Pages
- [[entities/grok-4-3]] — Reasoning engine powering Grok Computer
- [[entities/xai]] — Parent company
- [[entities/anthropic-computer-use]] — Anthropic's computer use capability
- [[entities/anthropic-computer-use]] — Anthropic's screen-based GUI agent
- [[entities/anthropic]] — Competitor company
- [[entities/claude-code]] — Anthropic's terminal-based coding agent
