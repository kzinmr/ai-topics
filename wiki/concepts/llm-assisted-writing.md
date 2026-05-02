---
title: "LLM-Assisted Writing"
created: 2026-05-02
updated: 2026-05-02
tags:
  - concept
  - ai-writing
  - human-in-the-loop
  - llm-usage-patterns
  - content-creation
aliases:
  - AI-assisted writing
  - LLM drafting
  - AI voice preservation
related:
  - [[entities/idiallo-com]]
  - [[concepts/harness-engineering/agentic-workflows/vibe-coding]]
  - [[concepts/coding-agents]]
sources:
  - raw/articles/idiallo.com--byte-size-editing-llm-assisted-articles--5e32cb82.md
  - https://idiallo.com/byte-size/editing-llm-assisted-articles?src=feed
---

# LLM-Assisted Writing

**LLM-Assisted Writing** refers to the workflow where authors use Large Language Models to draft, structure, or refine written content, then apply human editing to restore personal voice and authenticity. This pattern has emerged as a practical response to the tension between AI-generated efficiency and human authorial identity.

## The Voice Problem

A consistent challenge reported by practitioners is that LLM-generated content often:

- Sounds **generic** and lacks the author's distinctive voice
- Contains **awkward phrasings** that feel disconnected from the author's actual thoughts
- Produces content that is **functional but not quotable** — authors cringe when re-reading their own AI-assisted work
- Struggles to capture **personal anecdotes** and **specific memories** that give writing its human texture

## The Editing Workflow

Practitioners who successfully use LLM-assisted writing follow a multi-stage process:

1. **Use AI for structure, not voice** — LLMs are good at organizing ideas and creating frameworks
2. **Aggressive human editing** — Remove generic metaphors, "AI-speak," and formulaic phrases
3. **Restore personal sentiment** — Add back specific memories, anecdotes, and authentic reactions
4. **Verify quotability** — Ensure the final text reflects thoughts the author would actually stand behind

## Case Study: Ibrahim Diallo's Experience

Ibrahim Diallo (idiallo.com) documented his journey with LLM-assisted writing in early 2025:

- Used DeepSeek to draft a blog post about "building useless tools"
- AI produced a structured draft titled "Why Building Useless Tools is the Secret Sauce of Developer Growth"
- Published an edited version in March 2025
- Re-edited in May 2026 to remove AI-isms and restore his authentic voice
- Concluded: "While functional, it wasn't my human experience with the subject"

Key insight from his case: **The AI captured the idea structure but missed the personal texture** — the specific memory of recording audio at a red light, the real-world context that makes writing feel alive.

## Relationship to Vibe Coding

This pattern mirrors the **vibe coding** critique in software development:

| Dimension | LLM-Assisted Writing | Vibe Coding |
|-----------|---------------------|-------------|
| Initial output | Structured draft from prompt | Code from natural language |
| Human role | Heavy editing required | Review and iterate |
| Risk | Loss of authentic voice | Loss of architectural understanding |
| Mitigation | Aggressive human editing | Maintain oversight, understand code |
| Core insight | AI captures structure, not soul | AI captures syntax, not intent |

Both patterns highlight that **AI excels at scaffolding but struggles with authenticity** — whether that's the "voice" in writing or the "intent" in code.

## Best Practices

- **Treat AI as a junior writer** — it produces first drafts, not final content
- **Preserve personal anecdotes** — these are the "monkey bars" of writing
- **Edit for quotability** — can you stand behind every sentence in public?
- **Remove formulaic phrases** — "The only thing better than X is Y" patterns
- **Keep the human experience central** — specific memories, real emotions, actual context

## Graph Structure Query

```
[llm-assisted-writing] ──relates-to──→ [concepts/vibe-coding]
[llm-assisted-writing] ──author──→ [entities/idiallo-com]
[llm-assisted-writing] ──contrasts──→ [concepts/ai-generated-content]
[llm-assisted-writing] ──part-of──→ [concepts/human-in-the-loop]
[llm-assisted-writing] ──teaches──→ [concepts/ai-writing-workflow]
```

## Related Concepts

- [[concepts/harness-engineering/agentic-workflows/vibe-coding]]
- [[concepts/coding-agents]]
- [[concepts/human-in-the-loop]]
- [[concepts/ai-generated-content]]

## Sources

- [Editing my LLM assisted Articles](https://idiallo.com/byte-size/editing-llm-assisted-articles) — Ibrahim Diallo's practical experience and case study
