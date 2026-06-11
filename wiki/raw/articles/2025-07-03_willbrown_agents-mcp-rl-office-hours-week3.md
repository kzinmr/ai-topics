---
title: "Production-Ready Agent Engineering — Office Hours (Week 3)"
author: Will Brown
date: 2025-07-03
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: article
tags:
  - ai-agents
  - dspy
  - reinforcement-learning
  - grpo
  - agent-framework
  - multimodal
  - fine-tuning
  - structured-outputs
  - education
---

# Production-Ready Agent Engineering — Office Hours (Week 3)

**Lecture transcript:** [[transcripts/2025-07-03_willbrown_agents-mcp-rl-office-hours-week3]]
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Instructor:** Will Brown ([[entities/prime-intellect]])

---

## Summary

Final office hours session covering DSPy architecture and optimizers, multimodal RL challenges (images, audio, visual reasoning), SkyPilot GPU workflows, think-tag/XML parsing, reward curve debugging (gradient accumulation, reward diversity, dynamic resampling), experimentation scale guidance, and environment ideas for RL tasks.

## Key Topics

### DSPy Architecture

- **Modules**: Composable building blocks with input/output specs (signatures), structured as DAGs
- **Signatures**: Arrow notation (`question, answer -> output`) defining data flow, not prompts
- **DSPy vs LangGraph**: DSPy focuses on optimization/compilation; LangGraph focuses on enterprise readiness/deployment/logging
- **Optimizers**: Few-shot example selection, synthetic example generation + filtering, joint prompt + few-shot optimization
- **Compilation metaphor**: DSPy finds optimal prompts/examples through sampling + evaluation loop, like a compiler finds efficient code
- **GRPO integration**: Early but functional, similar to Verifiers optimizer; enables quick switching between GRPO and prompt tuning

### Multimodal Challenges

- **Tool-use workaround**: Offload image→text to a frozen small model (Moondream, GPT-4o Mini); agent works in text only
- **Visual reasoning**: VLMs are horrible at spatial reasoning ("VLMs are blind" paper); image must stay in context for fine-tuning
- **RL for multimodal**: Not user-friendly yet — requires forking repos; Verifiers multimodal PR under review (weeks away)
- **Audio**: RL ecosystem very underdeveloped; intelligence in language + speech/text as UI is the practical approach

### SkyPilot GPU Workflows

- Cloud-agnostic GPU provisioning (Prime Intellect, Lambda, RunPod, HyperStack)
- Typical workflow: small always-on debug machine → spin up large nodes for production runs → auto-stop
- Prime Intellect as cloud aggregator with unified credits

### Reward Curve Debugging

- **Oscillation**: Learning too fast or batch size too small → use gradient accumulation
- **Reward diversity**: Need variation within and across prompts; filter tasks where model gets 0% or 100% correct
- **Prompt reuse**: GRPO can reuse prompts across many epochs (100-200 prompts × 100 epochs works)
- **Dynamic resampling**: Keep sampling until you have diversity in completion quality (emerging technique)

### Structured Output Parsing

- **Think tags**: Parse everything after last `</think>` reward diversity, dynamic resampling), experimentation scale guidance, and environment ideas for RL tasks.

## Key Topics

### DSPy Architecture

- **Modules**: Composable building blocks with input/output specs (signatures), structured as DAGs
- **Signatures**: Arrow notation (`question, answer -> output`) defining data flow, not prompts
- **DSPy vs LangGraph**: DSPy focuses on optimization/compilation; LangGraph focuses on enterprise readiness/deployment/logging
- **Optimizers**: Few-shot example selection, synthetic example generation + filtering, joint prompt + few-shot optimization
- **Compilation metaphor**: DSPy finds optimal prompts/examples through sampling + evaluation loop, like a compiler finds efficient code
- **GRPO integration**: Early but functional, similar to Verifiers optimizer; enables quick switching between GRPO and prompt tuning

### Multimodal Challenges

- **Tool-use workaround**: Offload image→text to a frozen small model (Moondream, GPT-4o Mini); agent works in text only
- **Visual reasoning**: VLMs are horrible at spatial reasoning ("VLMs are blind" paper); image must stay in context for fine-tuning
- **RL for multimodal**: Not user-friendly yet — requires forking repos; Verifiers multimodal PR under review (weeks away)
- **Audio**: RL ecosystem very underdeveloped; intelligence in language + speech/text as UI is the practical approach

### SkyPilot GPU Workflows

- Cloud-agnostic GPU provisioning (Prime Intellect, Lambda, RunPod, HyperStack)
- Typical workflow: small always-on debug machine → spin up large nodes for production runs → auto-stop
- Prime Intellect as cloud aggregator with unified credits

### Reward Curve Debugging

- **Oscillation**: Learning too fast or batch size too small → use gradient accumulation
- **Reward diversity**: Need variation within and across prompts; filter tasks where model gets 0% or 100% correct
- **Prompt reuse**: GRPO can reuse prompts across many epochs (100-200 prompts × 100 epochs works)
- **Dynamic resampling**: Keep sampling until you have diversity in completion quality (emerging technique)

### Structured Output Parsing

- **Think tags**: Parse everything after last `</think>` Think tags: Parse everything after last `</think>`
    - XML tags: Top-level XML objects for tool calls; Beautiful Soup for complex nested XML
    - Regex structured generation: Enforce output schema via regex; good for few fixed schemas

    ### Experimentation Scale

    - Stable defaults: 7-14B models, <10 turns, <8K rollout
    - 1B models: SFT warmup + easier tasks more important
    - Scale up: Test at small scale, observe scaling laws, then go big

    ### Environment Ideas

    - Text Arena games (multi-agent RL)
    - Big model vs small model game-playing
    - Document search with synthetic QA
    - Interactive code execution for math (MATH benchmark)
    - Data generation: DeepSeek ~$1-2 for thousands of examples; GPT-4.1 for question generation

    ## Related

    - [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
    - [[transcripts/2025-07-03_willbrown_agents-mcp-rl-office-hours-week3]]
    - [[concepts/grpo-rl-training]]
    - [[entities/will-brown]]
    - [[entities/prime-intellect]]
    