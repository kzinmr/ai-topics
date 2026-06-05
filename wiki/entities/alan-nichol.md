---
title: Alan Nichol
type: entity
created: 2026-05-29
updated: 2026-05-29
tags:
  - person
  - ai-agents
  - agent-skills
  - conversational-ai
  - open-source
  - enterprise-ai
aliases:
  - Dr. Alan Nichol
  - amn41
sources:
  - raw/transcripts/2026-05-21_vanishing-gradients_show-us-your-agent-skills-ep3.md
  - https://alannichol.com/
  - https://pydata.org/global2024/schedule/speaker/AJT8R7/
  - https://councils.forbes.com/profile/Alan-Nichol-Co-Founder-CTO-Rasa/
  - https://rasa.com/
---

# Alan Nichol

**Dr. Alan Nichol** is the Co-Founder and CTO of **Rasa**, the leading open-source conversational AI platform. He holds a PhD in machine learning from the University of Cambridge and has been building chatbot and conversational AI systems since 2015. In 2024, he was named one of Europe's 100 most influential people in AI. He's known for coining the slogan **"Prompt and Pray"** as a critique of undisciplined LLM usage and for advocating structured, reliable enterprise AI.

## Overview

| Field | Detail |
|-------|--------|
| **Location** | Berlin, Germany (formerly) |
| **Role** | Co-Founder & CTO @ Rasa |
| **Education** | PhD in Machine Learning, University of Cambridge; MChemPhys, University of Edinburgh |
| **Founded** | Rasa (2016) — open-source conversational AI platform |
| **Recognition** | Forbes Technology Council, Europe's 100 most influential in AI (2024) |
| **Known For** | "Prompt and Pray" critique, intent-free conversational AI, enterprise-grade AI assistants |

## Key Contributions

### Rasa (2016–present)
Rasa is the enterprise-grade conversational AI platform combining LLMs with strong business logic. Key innovations:
- **Open-source infrastructure**: Widely adopted standard for conversational AI development
- **Intent-free dialogue**: Popularized building chat/voice bots without relying on rigid intent classification
- **Emergent personalization**: Agents that build memory autonomously across skills, channels, and conversations — learning what matters without predefined variables
- **Enterprise trust**: Fortune 500 customers; backed by Accel, Andreessen Horowitz, Basis Set Ventures

### Thought Leadership
- **"Beyond Prompt-and-Pray"** (Forbes, May 2025): Argued structured automation is the future of enterprise AI — reducing inefficiencies, ensuring cost-effectiveness and operational predictability
- **"AI Reliability at Scale"** (Forbes, Jun 2025): Outlined common failure points and architectural patterns for enterprise AI that meets standards
- **"No code is dead, Vibe code is in"**: Platform philosophy — natural language as the universal abstraction layer, enabling both domain experts (vague intent) and power users (spear-fishing with precise edits)

## Show Us Your (Agent) Skills Episode 3 (2026-05-21)

Alan demonstrated **programmatic video generation** with Claude and Remotion, using it as a lens to discuss deeper agent design principles:

### Remotion Video Generation Workflow
- **Everything-is-code thesis**: "Everything that can be code will be code" — productivity gains from making things agent-editable are so massive nothing survives as GUI-only
- **Remotion + Claude**: JavaScript library for programmatic video; Claude needs zero help writing Remotion code — it just knows the library
- **Real voice + AI avatar**: Records audio into computer, Whisper generates timestamps, AI generates face/animations synced to speech
- **Pure vibe experience**: Never wrote a line of Remotion code by hand; never looks at the code — only evaluates the output video
- **Solo production**: Videos that would require studio time, lighting, and video collaborators are produced between meetings from audio snippets

### Design Principles Over Code Syntax
- **Conceptual rules > technical instructions**: The skill contains design principles (don't animate three things at once, no slow fades — "sucks the energy out"), not just code syntax
- **Encoding judgment without vocabulary**: Lacks video editing jargon (jump cuts, easing, transitions) but can specify intent: "make it more high energy, don't go full influencer"
- **Claude reasons about what makes a video feel a certain way** and translates to technical decisions (e.g., "quantum easing of a bezier curve")
- **Levels of abstraction**: Natural language lets collaborators operate at their level — from vague intent ("make this friendlier") to precise edits ("change this transition")

### One Agent with Full Context
- **Single collaborator**: Agent that has the full picture — content refinement, technical domain, design rules — is a "super collaborator" unmatched by human creative partners who don't know your technical domain
- **Macro conversations possible**: Can spar on whether entire scenes are unnecessary, not just micro-edits

### Platform Design Philosophy
- **No code is dead**: Time-to-value of learning a no-code UI with custom primitives can't compete with coding agent velocity
- **The challenge**: How to build the equivalent of a coding agent for non-coders — diffs, branches, confidence in changes
- **Beginner's mindset**: Used to pick a new framework monthly to stay in learning mode; now gets that from working in unfamiliar domains via agents

### Vibe Coding Discussion
- Self-identifies as truly "vibe coding" his Remotion work — doesn't look at code, only output
- Distinction from agentic engineering: doesn't need code quality because no one else ever runs it — single-use video generation
- The question: at what point does "not looking at code" transition from vibe coding to robust agentic engineering? Answer: depends on verification rigor.

## Related
- [[entities/matthew-honnibal]] — spaCy founder; Episode 3 co-guest
- [[entities/vincent-warmerdam]] — marimo engineer, former Rasa researcher; Episode 3 co-guest
- [[entities/eleanor-berger]] — Agentic engineering educator; Episode 3 co-guest
- [[entities/hugo-bowne-anderson]] — Vanishing Gradients host; co-creator of chatbot education workshops
- [[concepts/agent-skills]] — Agent skill design patterns
- [[concepts/vibe-coding]] — Vibe coding debate
