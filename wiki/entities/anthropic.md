---
title: Anthropic
created: 2026-04-09
updated: 2026-04-09
tags:
- company
- ai-safety
- llm
- active
aliases:
- Anthropic PBC
---

# Anthropic

AI safety research company, developer of the Claude model family.

## Key Facts

- Founded by former OpenAI researchers focused on AI alignment and safety
- Known for cautious model release practices — will withhold models deemed too risky
- Headquarters: San Francisco, CA

## Model Lineup (as of Apr 2026)

| Model | Status | Notes |
|-------|--------|-------|
| [[claude-mythos]] | **Withheld** | Too risky for public release; limited access via [[project-glasswing]] |
| [[claude-opus-4.7]] | Released (GA, Apr 16) | Latest flagship — improved coding, cyber safeguards, better vision |
| [[claude-opus-4.6]] | Released | Previous generation |
| [[claude-sonnet-4]] | Released | Mid-tier |

## Claude Opus 4.7 (Apr 2026)

Released GA Apr 16, 2026. Notable improvements in advanced software engineering:
- 13% lift on 93-task coding benchmark (Replit eval), 4 tasks neither Opus 4.6 nor Sonnet 4.6 could solve
- Catches own logical faults during planning phase
- Substantially better vision (higher resolution image understanding)
- First Claude model with cyber safeguards (auto-detects and blocks prohibited cybersecurity use)
- Low-effort Opus 4.7 ≈ medium-effort Opus 4.6
- Pricing: $5/M input, $25/M output tokens (same as Opus 4.6)
- Available on all Claude products, API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry
- Cyber Verification Program for legitimate security research

## Claude Design by Anthropic Labs (Apr 17, 2026)

New product powered by Claude Opus 4.7 vision model. Allows collaborative design creation:
- Describe what you need, Claude builds first version
- Refine through conversation, inline comments, direct edits, custom sliders
- Can apply team's design system automatically
- Export to Canva, PDF, PPTX, or standalone HTML
- Handoff to Claude Code for implementation
- Research preview for Pro, Max, Team, Enterprise subscribers
- Integration with Canva (Melanie Perkins co-founder endorsement)

## AI Safety Initiatives

### Project Glasswing (2026-04)
Anthropic committed $100M in model usage credits + $4M in donations to open-source security organizations. See [[project-glasswing]] for details.

### Model Withholding Decision
Anthropic chose not to release [[claude-mythos]] publicly after discovering its vulnerability exploitation capabilities far exceeded safety thresholds. On Firefox exploit generation:
- Opus 4.6: 2 working exploits out of hundreds of attempts
- Mythos: **181 working exploits**

Mythos also discovered decades-old bugs in critical software: OpenBSD (27-year-old bug), FFmpeg (16-year-old bug).

## Sources
- [[raw/articles/substack.com--app-link-post--40004939.md]] (Ben's Bites, 2026-04-09)

## Related
- [[claude-mythos]]
- [[project-glasswing]]
- [[claude-opus-4.6]]
- [[openai]]
- [[meta]]
