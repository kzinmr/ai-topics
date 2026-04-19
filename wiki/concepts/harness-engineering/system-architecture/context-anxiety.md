---
title: "Context Anxiety"
status: draft
type: concept
tags: [context-management, cognition, claude, models]
related: [cognition-devin-philosophy, context-window-management]
sources:
  - https://cognition.ai/blog/devin-sonnet-4-5-lessons-and-challenges
---

# Context Anxiety — Model-Specific Context Limits

Discovered during Cognition's integration of Claude Sonnet 4.5 into Devin.

## What is Context Anxiety?

Agents become unreliable when context windows exceed **model-specific thresholds**. This is NOT a hard limit — it's a degradation pattern where:

- Response quality drops
- Agents lose track of earlier instructions
- Error rates increase
- Behavior becomes unpredictable

## Key Findings

1. **Single-tasked agents** are more reliable than multi-purpose agents
2. **Explicit context management** is critical for long-running sessions
3. **Model-specific limits exist** — different thresholds for each model/provider
4. **Context anxiety** appears gradually, not as a hard cutoff

## Mitigation Strategies

- **Context pruning** — Remove irrelevant history
- **Session splitting** — Start fresh sessions for new tasks
- **Task bounding** — Keep agent scope narrow
- **Model awareness** — Know your model's context anxiety threshold

## Comparison with Other Approaches

| Approach | Cognition | Anthropic | OpenAI |
|----------|-----------|-----------|--------|
| Context limit | Model-specific anxiety threshold | 60% rule (Sankalp) | Dynamic compaction |
| Mitigation | Session splitting | Context pruning | Token curation |
| Philosophy | "Respect the anxiety" | "Stay under 60%" | "Compact as needed" |

## See Also

- [[concepts/cognition-devin-philosophy]] — Main Cognition philosophy
- [[concepts/context-window-management]] — General context management patterns
- [[concepts/agentic-engineering/context-window-management]] — Simon Willison's context patterns