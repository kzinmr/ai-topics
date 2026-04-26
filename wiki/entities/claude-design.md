---
title: "Claude Design"
type: entity
created: 2026-04-25
updated: 2026-04-25
tags: [product, anthropic, design, vision, labs]
aliases: ["Claude Design by Anthropic Labs"]
sources: []
---
# Claude Design

Anthropic Labs product for collaborative visual design, powered by Claude Opus 4.7's vision model. Released April 17, 2026 in research preview.

## Overview

Claude Design lets users collaborate with Claude to create polished visual work — designs, prototypes, slides, one-pagers, and more. It is the first product launched from [Anthropic Labs](anthropic-labs) (Anthropic's experimental product division).

Powered by Claude Opus 4.7's vision capabilities, Claude Design represents a convergence of frontier model vision understanding and creative tooling.

## Key Features

### Brand System Auto-Build
During onboarding, Claude builds a design system for your team by reading your codebase and design files. Every project uses your colors, typography, and components automatically. Teams can maintain more than one design system.

### Interactive Prototypes
Turn static mockups into shareable interactive prototypes without code review or PRs. Complex pages that took 20+ prompts in other tools only require 2 prompts in Claude Design.

### Design-to-Code Handoff
When a design is ready to build, Claude packages everything into a handoff bundle that can be passed to [Claude Code](claude-code) with a single instruction — creating a seamless bridge from visual design to implementation.

### Fine-Grained Refinement
- Inline comments on specific elements
- Direct text editing
- Adjustment knobs for spacing, color, and layout
- Ask Claude to apply changes across the full design

### Export Options
- Internal URL within organization
- Folder save
- Export to Canva, PDF, PPTX, or standalone HTML files

## Use Cases

| Use Case | Primary Users | Output |
|----------|--------------|--------|
| Realistic prototypes | Designers | Interactive prototypes (user-testable) |
| Product wireframes | Product Managers | Feature flows → Claude Code handoff |
| Design explorations | Designers | Wide range of directions |
| Pitch decks | Founders, AEs | Complete on-brand decks → PPTX/Canva |
| Marketing collateral | Marketers | Landing pages, social assets → designer polish |
| Frontier design | Anyone | Code-powered prototypes with voice, video, shaders, 3D |

## Partnership

Canva is an early integration partner. [Melanie Perkins](https://www.canva.com) states: *"We're excited to build on our collaboration with Claude, making it seamless for people to bring ideas and drafts from Claude Design into Canva."*

## Availability

- **Research preview** as of April 17, 2026
- Available for Claude Pro, Max, Team, and Enterprise subscribers
- Gradual rollout throughout release day
- Runs on Claude Code's web infrastructure (no local compute required)

## Technical Basis

Claude Design is powered by Claude Opus 4.7's vision model, which supports images up to 2,576 pixels on the long edge (~3.75 megapixels) — more than 3× prior models. This high-resolution vision capability is critical for analyzing design files, screenshots, and technical diagrams with precision.

## Related

- [[concepts/claude-opus-4-7]] — Vision model powering Claude Design
- [[claude-code]] — Handoff integration for design-to-code
- [[anthropic]] — Parent company
- [[anthropic-labs]] — Experimental product division
- [[concepts/canva]] — Integration partner
- [[concepts/vision-models]] — Vision capability overview

## Sources

- [Anthropic: Introducing Claude Design by Anthropic Labs](https://www.anthropic.com/news/introducing-claude-design-by-anthropic-labs) (2026-04-17) — official announcement
