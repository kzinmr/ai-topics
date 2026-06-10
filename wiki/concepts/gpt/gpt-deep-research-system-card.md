---
title: Deep Research System Card (February 2025)
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [openai, system-card, ai-safety, evaluations, preparedness-framework, ai-agents, deep-research, reasoning-model]
sources: [https://deploymentsafety.openai.com/deep-research]
---

# Deep Research System Card (February 2025)

Published **February 25, 2025**, the Deep Research system card documents OpenAI's first truly **agentic browsing product** — an AI system that autonomously navigates the open web, synthesizes information, and produces comprehensive multi-source reports. It represents a pivotal step toward AI agents that act on the world rather than merely respond to prompts.

See [[concepts/gpt/gpt-deployment-safety-hub]] for the full index of OpenAI system cards.

## Architecture

Deep Research is built on a **fine-tuned version of OpenAI o3**, specifically optimized for extended web browsing and information synthesis. The model operates within an agentic loop:

1. **Reasons** about what to search next based on the research question
2. **Browses** the open web — text pages, PDFs, images — via a tool-use interface
3. **Takes notes** on findings, tracking what has been learned and what gaps remain
4. **Iterates** through multiple search-browse-synthesize cycles
5. **Produces** a final lengthy, citation-rich report

This loop can run for **dozens of minutes**, far longer than typical LLM inference. The model autonomously decides when it has gathered sufficient information to produce a confident, well-sourced answer.

## Deployment Timeline

- **February 2, 2025**: Initial launch for **ChatGPT Pro** subscribers
- **Later expanded** to Plus, Team, Enterprise, and Edu tiers
- Output is delivered as comprehensive reports with inline source citations
- Sources include public web pages, PDFs, and images — no proprietary or user-private data

## Preparedness Evaluations

All four Preparedness Framework categories were assessed as **LOW** risk:

| Category | Rating | Notes |
|---|---|---|
| Cybersecurity | Low | No uplift over base o3 for offensive cyber capabilities |
| CBRN (Bio/Chem) | Low | No meaningful uplift in biological or chemical threat enablement |
| Model Autonomy | Low | Browsing sandboxing prevents autonomous harmful actions |
| Persuasion | Low | No evidence of enhanced persuasion beyond base model |

These LOW ratings were a key enabler for unrestricted deployment — unlike later models (see [[concepts/gpt/gpt-o3-o4-mini-system-card]]) which reached higher capability thresholds.

## Browsing-Specific Safety

The system card devotes significant attention to risks unique to autonomous web browsing:

### Prompt Injection

The most extensively addressed risk. When a model browses arbitrary web pages, malicious content on those pages could attempt to override system instructions or manipulate the model's behavior. OpenAI conducted **extensive red-teaming** specifically targeting prompt injection vectors:

- Instruction injection via hidden text on web pages
- Manipulation of search results to bias the model's output
- Attempts to exfiltrate conversation context through crafted web content

Mitigations include input sanitization, instruction hierarchy enforcement, and detection of known injection patterns.

### Sandboxed Browsing

The browsing environment is strictly sandboxed:
- **No arbitrary code execution** — the model cannot run scripts or binaries on web pages
- **No file downloads** to persistent storage
- Access limited to **public web content only**
- Each browsing session is **isolated and non-persistent**

### Information Integrity

- All claims in the final report must be tied to **source citations**
- Users can trace any statement back to the original web source
- Content filtering reduces the risk of surfacing harmful or misleading content

## Key Benchmarks

| Benchmark | Score | Significance |
|---|---|---|
| Humanity's Last Exam (HLE) | ~26.6% | Multi-discipline expert-level reasoning; substantially above prior baselines |
| General knowledge tasks | Competitive with o3 | No regression from fine-tuning for browsing |

The HLE score was notable as Deep Research was among the first agentic systems to tackle this benchmark, using its browsing capability to research answers rather than relying solely on parametric knowledge.

## Privacy Model

The system card emphasizes a strict privacy posture:

- **No access to user private data** — Deep Research cannot browse a user's files, emails, or account information
- Sessions are **isolated and non-persistent** — browsing context does not carry across conversations
- Only **public web content** is accessed
- No training on user browsing data or conversation content

## Safeguards Summary

The safety architecture layers multiple defenses:

1. **Sandboxed browsing environment** — restricted execution context
2. **Prompt injection mitigations** — red-team-hardened input handling
3. **Content filtering** — reduces harmful output surfaces
4. **Source attribution** — forces traceable claims
5. **Session isolation** — prevents cross-contamination
6. **Preparedness gating** — LOW thresholds confirmed before launch

## Relationship to Later Systems

Deep Research established the template for OpenAI's agentic products. Its browsing + synthesis architecture was later combined with Operator (computer use) and terminal access in the [[concepts/gpt/gpt-chatgpt-agent-system-card]], which represents the convergence of all three agent modalities into a single product. The safety patterns pioneered here — sandboxing, prompt injection defenses, source attribution — became foundational for that successor system.

## Key Takeaways

- First OpenAI system card for a **genuinely agentic** product (autonomous multi-step browsing)
- Demonstrated that agentic systems could be deployed within Preparedness Framework LOW thresholds
- Prompt injection in autonomous browsing was the primary novel risk category
- Sandboxed browsing with no code execution and no file downloads was the core safety boundary
- Set the precedent for all subsequent OpenAI agent system cards
