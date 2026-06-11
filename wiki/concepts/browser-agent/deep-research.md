---
title: "Deep Research — Agentic Browsing for Autonomous Research"
type: concept
aliases:
  - deep-research
  - openai-deep-research
  - agentic-research-browsing
created: 2026-06-11
updated: 2026-06-11
tags:
  - concept
  - browser-agent
  - openai
  - ai-agents
  - reasoning-model
status: active
sources:
  - "https://deploymentsafety.openai.com/deep-research"
---

# Deep Research — Agentic Browsing for Autonomous Research

**Deep Research** is OpenAI's first truly **agentic browsing product** — an AI system that autonomously navigates the open web, synthesizes information from multiple sources, and produces comprehensive citation-rich reports. Built on a fine-tuned version of **OpenAI o3**, it represents a distinct browser agent pattern focused on **autonomous information gathering and synthesis** rather than UI interaction or transaction execution.

## Core Architecture

Deep Research operates within an **agentic browsing loop**:

```
Research question
    → Reason about search strategy
        → Browse web (text pages, PDFs, images)
            → Take notes on findings
                → Iterate search-browse-synthesize cycles
                    → Produce comprehensive report
```

### Key Characteristics

| Characteristic | Description |
|---|---|
| **Base Model** | Fine-tuned OpenAI o3 |
| **Execution Time** | Dozens of minutes (far longer than typical LLM inference) |
| **Autonomy** | Model decides when it has gathered sufficient information |
| **Output** | Lengthy, citation-rich reports with inline source citations |
| **Sources** | Public web pages, PDFs, images — no proprietary or user-private data |

## Technical Distinction

Deep Research represents a **fifth category** of browser agent approaches:

| Approach | Representative | Focus | Execution Pattern |
|---|---|---|---|
| Screenshot-Based | Anthropic Computer Use, OpenAI CUA | UI interaction | Click/type/scroll cycle |
| DOM-Based | browser-use, Playwright | Element manipulation | DOM analysis → action |
| Structured Protocol | WebMCP, Stagehand | Declarative API calls | Tool discovery → invocation |
| Hybrid | ChatGPT Agent, Stagehand v3 | Multi-modal fallback | DOM → vision → structured API |
| **Agentic Browsing Loop** | **Deep Research** | **Information synthesis** | **Search → browse → note → iterate → report** |

### Research-First vs Action-First

While most browser agents focus on **"action-first"** patterns (performing transactions, filling forms, clicking buttons), Deep Research employs a **"research-first"** pattern:

- **Goal**: Gather and synthesize information from multiple sources
- **Process**: Autonomous decision-making about what to search next
- **Output**: Comprehensive reports with traceable citations
- **Value**: Reduces research time from hours to minutes

This pattern complements rather than replaces action-first approaches. Deep Research handles the "what should I know?" question, while Operator/Computer Use handles the "how do I do this?" question.

## Safety Architecture

### Preparedness Evaluations

All four Preparedness Framework categories were assessed as **LOW** risk:

| Category | Rating | Notes |
|---|---|---|
| Cybersecurity | Low | No uplift over base o3 for offensive cyber capabilities |
| CBRN (Bio/Chem) | Low | No meaningful uplift in biological or chemical threat enablement |
| Model Autonomy | Low | Browsing sandboxing prevents autonomous harmful actions |
| Persuasion | Low | No evidence of enhanced persuasion beyond base model |

### Browsing-Specific Safeguards

1. **Sandboxed browsing environment** — No arbitrary code execution, no file downloads
2. **Prompt injection mitigations** — Extensive red-teaming against instruction injection
3. **Content filtering** — Reduces harmful output surfaces
4. **Source attribution** — Forces traceable claims in final reports
5. **Session isolation** — Prevents cross-contamination between conversations
6. **Preparedness gating** — LOW thresholds confirmed before deployment

### Prompt Injection Defense

The most extensively addressed risk. When browsing arbitrary web pages, malicious content could attempt to override system instructions. OpenAI conducted **extensive red-teaming** targeting:

- Instruction injection via hidden text on web pages
- Manipulation of search results to bias output
- Attempts to exfiltrate conversation context through crafted web content

## Deployment Timeline

- **February 2, 2025**: Initial launch for **ChatGPT Pro** subscribers
- **Later expanded** to Plus, Team, Enterprise, and Edu tiers
- Output delivered as comprehensive reports with inline source citations

## Key Benchmarks

| Benchmark | Score | Significance |
|---|---|---|
| Humanity's Last Exam (HLE) | ~26.6% | Multi-discipline expert-level reasoning; substantially above prior baselines |
| General knowledge tasks | Competitive with o3 | No regression from fine-tuning for browsing |

The HLE score was notable as Deep Research was among the first agentic systems to tackle this benchmark, using its browsing capability to research answers rather than relying solely on parametric knowledge.

## Relationship to Other Systems

### Evolution Path

```
Deep Research (Feb 2025)
    ↓ Browsing + synthesis architecture
ChatGPT Agent (Jul 2025)
    ↓ Combined with Operator (computer use) + terminal access
    ↓ Safety patterns inherited: sandboxing, prompt injection defenses, source attribution
```

Deep Research established the template for OpenAI's agentic products. Its safety patterns became foundational for the successor ChatGPT Agent system.

### Complementary Patterns

| Pattern | Use Case | Example |
|---|---|---|
| **Research-First** (Deep Research) | Information gathering & synthesis | "Research the current state of quantum computing" |
| **Action-First** (Operator/CUA) | Transaction execution | "Book a flight to Berlin next week" |
| **Hybrid** (ChatGPT Agent) | Both research and action | "Find the best flight to Berlin and book it" |

## Browser Agent Ecosystem Position

Deep Research occupies a unique niche in the browser agent ecosystem:

- **Not a replacement** for UI automation tools (browser-use, Playwright)
- **Not a competitor** to structured protocols (WebMCP)
- **A complement** to action-first agents (Operator, Computer Use)
- **A precursor** to hybrid systems (ChatGPT Agent)

Its value lies in handling complex, multi-source research tasks that would take humans hours to complete, while maintaining strict safety boundaries through sandboxing and source attribution.

## Related Concepts

- [[concepts/browser-agent/death-of-browser]] — Browser dehumanization trend and technical approach classification
- [[concepts/gpt/gpt-deep-research-system-card]] — Detailed system card with safety evaluations
- [[concepts/gpt/gpt-chatgpt-agent-system-card]] — Successor system combining browsing, computer use, and terminal access
- [[concepts/gpt/gpt-o3-o4-mini-system-card]] — Base model capabilities
- [[concepts/agent-driven-development]] — Software development using agents

## Related Entities

- [[entities/openai-cua]] — OpenAI's Computer-Using Agent (action-first pattern)
- [[entities/anthropic-computer-use]] — Anthropic's screenshot-based approach
- [[entities/browser-use]] — Open-source DOM-based automation
- [[entities/browserbase]] — Browser infrastructure for agents

## Sources

- [Deep Research System Card (OpenAI, Feb 2025)](https://deploymentsafety.openai.com/deep-research)
- [When will browser agents do real work? (InfoWorld, Nov 2025)](https://www.infoworld.com/article/4081396/when-will-browser-agents-do-real-work.html)
