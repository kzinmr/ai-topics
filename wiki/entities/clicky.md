---
title: Clicky
created: 2026-05-21
updated: 2026-05-21
type: entity
tags:
  - product
  - coding-agents
  - tool
  - voice-ai
  - hardware
aliases: []
sources:
  - raw/newsletters/2026-05-20-clicky.md
---

# Clicky

**Clicky** is a free macOS AI assistant built by Farza in 3 weeks. It demonstrates a novel interaction paradigm combining voice input, screen capture, and visual pointing — independently developed in the same week as Google's [[entities/deepmind|Magic Pointer]].

## How It Works

Clicky lives in the macOS menu bar. The interaction flow:

1. **Activation**: Hold `Ctrl+Option` (a keyboard chord similar to common launcher shortcuts)
2. **Input**: Speak a question out loud — Clicky captures both the voice input and a screenshot of the current screen
3. **Processing**: Sends both to Claude (Anthropic's model) for understanding
4. **Response**: Claude responds via voice, with a **blue animated triangle** pointing at the exact spot on the screen relevant to the answer

## Key Design Decisions

| Decision | Implementation |
|----------|---------------|
| **Setup** | None — no account, no API key, no model selection |
| **Privacy** | Screenshots taken on activation; always-on screen monitoring is a noted concern |
| **Model** | Claude (Anthropic) — fixed, not user-selectable |
| **Output** | Voice response + visual pointer (blue triangle) |
| **Build Time** | 3 weeks |

## Significance

Clicky is notable because it independently discovered the **screen + voice + pointing** interaction pattern in the same week as Google DeepMind's [[entities/deepmind|Magic Pointer]] (May 2026). This convergence suggests the pattern — activating AI by pointing at screen elements using natural modalities — is a natural UI evolution, not a specific lab's invention.

The no-setup, no-cost approach (free app, no API key) lowers the barrier to entry dramatically compared to assistant platforms that require subscriptions and configuration.

## Privacy Considerations

Clicky captures the current screen only when activated via the keyboard shortcut. However, the app runs persistently in the menu bar with screen-recording permissions, which raises the question of whether it could theoretically be triggered or monitored without the user's awareness.

## Related Pages
- [[entities/deepmind]] — Google DeepMind's Magic Pointer (same week, same concept)
- [[concepts/agent-native-cloud]] — Infrastructure paradigm for agent-native apps
