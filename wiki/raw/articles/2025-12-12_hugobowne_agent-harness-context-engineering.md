---
title: "AI Agent Harness, 3 Principles for Context Engineering, and the Bitter Lesson Revisited"
source: "Vanishing Gradients (Hugo Bowne-Anderson, Duncan Gilchrist)"
source_url: "https://hugobowne.substack.com/p/ai-agent-harness-3-principles-for"
date_published: 2025-12-12
date_scraped: 2026-05-13
authors:
  - Hugo Bowne-Anderson
  - Duncan Gilchrist
featured_guest: Lance Martin
guest_affiliation: LangChain
type: article
tags:
  - agent-harness
  - context-engineering
  - ai-agents
  - llm
  - anthropic
  - langchain
---

# AI Agent Harness, 3 Principles for Context Engineering, and the Bitter Lesson Revisited

**Published**: Dec 12, 2025 | **Authors**: Hugo Bowne-Anderson, Duncan Gilchrist | **Guest**: Lance Martin (LangChain)

## Summary

Hugo Bowne-Anderson and Duncan Gilchrist distill key insights from their High Signal podcast conversation with Lance Martin (LangChain), covering the shift from model training to orchestration, the importance of agent harnesses and the need to re-architect them as models improve, 3 key principles for mastering context engineering (Reduce, Offload, Isolate), and navigating the agentic spectrum.

## Key Themes

### From Training to Orchestration

Three major shifts reshaping AI landscape:
1. **Architectural Consolidation**: Transformer architecture has become dominant, absorbing CNNs and RNNs
2. **Model APIs >> Training Models**: Industry moved from everyone training proprietary models to few foundation model providers offering APIs
3. **Higher Level of Abstraction**: Core engineering challenge shifted to orchestration — prompt engineering, context engineering, building agents

### Classic ML Principles Still Apply

- **Simplicity Remains Essential**: Start with simplest approach (prompt engineering, structured workflow), progressively add complexity
- **Observability and Evaluation**: Non-deterministic systems require rigorous new evaluation beyond traditional unit tests
- **Verifier's Law** (from Jason Wei): Ability to train AI for a task is proportional to how easily verifiable it is

### Agent Harness and the Bitter Lesson

- Rich Sutton's "Bitter Lesson" applies at the application layer: architectural assumptions baked into applications today will be obsolete in 6 months
- **Agent Harness**: The scaffolding around the LLM managing tool execution, message history, and context. Must be continually simplified as models improve
- **Manus re-architected 5 times since March 2024**
- **LangChain's Open Deep Research rebuilt multiple times in a year**
- **Anthropic rips out Claude Code's agent harness as models improve**

### The 3 Principles: Reduce, Offload, Isolate

Lance Martin outlines the playbook used by leading agentic systems (Manus, Claude Code):

1. **Reduce**: Actively shrink context passed to the model — compacting older tool calls, trajectory summarization
2. **Offload**: Move information and complexity OUT of the prompt — save full tool results to filesystem, offload action space (give bash terminal instead of 100 tools)
3. **Isolate**: Multi-agent architectures to delegate token-heavy sub-tasks — sub-agent works in own isolated context, returns only concise result

Key insight on "context rot": even models with million-token context windows suffer degraded instruction-following as context grows. The effective context window is often lower than the stated technical one.

### Workflows vs. Agents: A Spectrum of Autonomy

- **Workflows**: Systems with predefined, predictable steps (A → B → C). Ideal for known structure tasks
- **Agents**: LLM dynamically chooses tools and processes. Best for open-ended, adaptive tasks
- This is a spectrum, not binary. Common to embed an agent as one step within a larger workflow

### Key Takeaways for Leaders

1. **Start Simple**: Exhaust prompt engineering and simple workflows before agents. Fine-tuning as last resort
2. **Build for Change**: Accept that "Bitter Lesson" is real — what you build today will need re-architecture
3. **Don't Fear Rebuilding**: Cost/time to rebuild is dramatically lower with powerful code-generation models
4. **Patience Pays Off**: Application not viable today may be unlocked by next generation of models (Cursor after Claude 3.5 Sonnet)
5. **Be Wary of Premature Training**: Don't rush to fine-tune — frontier models often acquire capabilities teams spend months building

## Resources
- Context Engineering for Agents by Lance Martin
- Learning the Bitter Lesson by Lance Martin
- Context Engineering in Manus by Lance Martin
- Context Rot: How Increasing Input Tokens Impacts LLM Performance by Chroma
- Building effective agents by Anthropic
- Effective context engineering for AI agents by Anthropic
- How we built our multi-agent research system by Anthropic
- Measuring AI Ability to Complete Long Tasks by METR
- Your AI Product Needs Evals by Hamel Husain
- Introducing Roast: Structured AI workflows made easy by Shopify
