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
| [[claude-sonnet-4]] | Released | Previous generation |
| [[claude-opus-4.6]] | Released | Previous flagship |
| [[claude-mythos]] | **Withheld** | Too risky for public release; limited access via [[project-glasswing]] |

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
