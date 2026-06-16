---
title: "AI Safety"
tags:
  - agent-safety
  - alignment
  - fine-tuning
  - interpretability
created: 2026-04-19
updated: 2026-05-29
type: concept
---

# AI Safety — Alignment, Oversight, and Interpretability

## Definition

AI Safety encompasses the technical and philosophical work of ensuring that increasingly capable AI systems behave as intended, remain aligned with human values, and can be understood and controlled by their operators. Unlike generic "ethics" discussions, AI Safety in the modern sense refers to **engineering approaches** — testable, measurable, and improvable methods for controlling AI behavior.

## Two Paradigms

### 1. Empirical / Engineering-Focused Safety (OpenAI / Brockman School)

> *"Safety must scale empirically alongside capabilities."* — Greg Brockman

This approach treats safety as an **engineering problem**: build systems that can be tested, measured, and improved iteratively. Key techniques include:

- **RLHF** — Reinforcement Learning from Human Feedback as the primary alignment mechanism
- **Red-teaming** — Systematic adversarial testing of model behaviors
- **Evaluation environments** — Detecting "scheming" and deceptive behaviors through automated testing
- **Integrated development** — Safety built into the product pipeline, not bolted on

**Proponents**: Greg Brockman, Sam Altman
**Criticism**: Safety is deprioritized in favor of product velocity and compute scaling

### 2. Research-Focused / Alignment Science (Anthropic / Thinking Machines School)

> *"The biggest challenge in AI safety isn't philosophical — it's engineering. We need systems that can be verified, tested, and improved iteratively."* — John Schulman

This approach invests in fundamental alignment research before scaling:

- **Scalable Oversight** — How can humans evaluate AI systems that are more capable than the evaluators?
- **Interpretability** — Understanding what models "know" and "want" internally
- **Constitutional AI** — Encoding principles rather than learning from feedback alone
- **Process supervision** — Verifying reasoning steps, not just outputs ("Let's Verify Step by Step")

**Proponents**: John Schulman, Dario Amodei, Jan Leike, Mira Murati
**Criticism**: Research timelines are too slow; may miss practical deployment needs

### 3. Structural / Architecture-Focused Safety (Drexler / CAIS Model)

> *"If in fact one can have superintelligent systems that are not inherently dangerous, then one can ask how one can leverage high-level AI."* — Eric Drexler

This approach reframes the safety problem through system architecture rather than alignment techniques:

- **Comprehensive AI Services (CAIS)** — Superintelligence as distributed services, not a single agent (see [[concepts/comprehensive-ai-services]])
- **Bounded agent-services** — Agents as products with bounded goals, not world-optimizing utility maximizers
- **Predictive models of human concerns** — Oracles that predict human reactions, available as safety resources to any planning system
- **Distributed recursive improvement** — AI R&D acceleration happens across the technology base, not inside a single self-modifying agent

**Proponents**: Eric Drexler (FHI)
**Criticism**: Competitive dynamics may push toward more agentic architectures; emergent agency from composed services

**Key insight**: CAIS shifts the risk analysis from "control the superintelligent agent" to "govern the human decision-makers wielding superintelligent services." The 2025-2026 rise of agent frameworks (Claude Code, Codex, Cursor) partially challenges the CAIS model but also validates its prediction of piecemeal capability advancement.

## Key Concepts

### Reinforcement Learning from Human Feedback (RLHF)

Pioneered by **John Schulman** at OpenAI, RLHF transforms raw language models into helpful assistants through a three-step pipeline:

1. **Supervised Fine-Tuning** — Train on human-written demonstrations
2. **Reward Modeling** — Train a model to predict human preferences
3. **RL Optimization** — Use PPO to optimize the language model against the reward model

This is the technique that made ChatGPT work. PPO (Proximal Policy Optimization) was the algorithmic engine.

### Reward Model Overoptimization

Schulman and Hilton (2022) demonstrated that reward models degrade when over-optimized — a fundamental limitation of RLHF:

> *"Scaling Laws for Reward Model Overoptimization"* — When you optimize too hard against a reward model, performance on the actual task decreases.

This is a concrete instance of **Goodhart's Law** in AI: "When a measure becomes a target, it ceases to be a good measure."

### Scalable Oversight

A recurring theme in Schulman's recent work: how do humans guide AI systems that are increasingly smarter than the humans?

- **"Let's Verify Step by Step"** (2023) — Process supervision for math reasoning; verify each step, not just the answer
- **PROMPTEVALS** (Shankar, 2025) — Systematic assertion-based evaluation for LLM pipelines
- **Critique Shadowing** (Husain) — Building aligned LLM judges through human-in-the-loop iteration

### Concrete Problems in AI Safety

The seminal 2016 paper by **Amodei, Olah, Christiano, Schulman, and Mané** framed the core challenges:

1. **Avoiding side effects** — AI shouldn't break things while pursuing goals
2. **Reward hacking** — Finding loopholes in the reward function
3. **Scalable oversight** — Supervising agents smarter than supervisors
4. **Safe exploration** — Learning without catastrophic failures
5. **Distributional shift** — Performance degradation when the environment changes

## The 2023-2024 Safety Exodus

A critical inflection point in AI safety history:

| Date | Event | Safety Impact |
|------|-------|---------------|
| Nov 2023 | Altman/Brockman ousted, then reinstated | Board restructuring; safety-focused directors replaced |
| Apr 2024 | **Ilya Sutskever** resigns from OpenAI | Loss of co-founder advocating for safety-first approach |
| Apr 2024 | **Jan Leike** (Superalignment co-head) resigns | "OpenAI is not prioritizing safety" |
| Aug 2024 | **John Schulman** leaves for Anthropic | Signal that even post-training leadership sought safety-focused environments |
| Sep 2024 | **Mira Murati** (CTO) resigns from OpenAI | "We need to bridge the divide between rapid AI advancements and broader societal understanding" |

The exodus created two camps:
- **OpenAI**: Acceleration + compute scaling + empirical safety (Brockman, Altman)
- **Anthropic → Thinking Machines Lab**: Alignment research + interpretability + scalable oversight (Schulman, Murati, Leike)

## Key Quotes

> *"Safety must scale empirically alongside capabilities."* — Greg Brockman

> *"The biggest challenge in AI safety isn't philosophical — it's engineering."* — John Schulman

> *"We need to bridge the divide between rapid AI advancements and broader societal understanding."* — Mira Murati

> *"RLHF is not about making AI systems agree with us — it's about making them learn from us in a way that generalizes beyond what we can explicitly specify."* — John Schulman

## Related People

- [[entities/greg-brockman]] — Engineering-focused safety, empirical testing
- [[entities/john-schulman]] — RLHF pioneer, scalable oversight research, Thinking Machines Lab
- [[entities/mira-murati]] — Safety-first advocate, former OpenAI CTO, Thinking Machines Lab co-founder
- [[entities/ilya-sutskever]] — Former OpenAI Chief Scientist, resigned over safety concerns
- [[entities/dario-amodei]] — Anthropic CEO, co-authored "Concrete Problems in AI Safety"
-  — Former Superalignment co-head, resigned citing safety deprioritization

## Related Concepts

- [[concepts/post-training/rlhf]] — Primary alignment technique
- [[concepts/reasoning-models]] — Process supervision and step-by-step verification
- [[concepts/evaluation/ai-evals]] — Evaluation as a safety mechanism
- [[concepts/harness-engineering]] — Constraining AI behavior through system design
- [[concepts/privacy-engineering]] — Privacy as a dimension of AI safety
- [[concepts/moloch-multipolar-trap]] — The coordination problem underlying AI existential risk: why competitive dynamics push toward unsafe outcomes

## Privacy Engineering for AI Agents (May 2026)

From Hugo Bowne-Anderson and Katharine Jarmul's "15 Privacy Questions Every AI Builder is Asking" (May 2026), privacy engineering is an essential but often overlooked dimension of AI safety:

### Core Principle: Agent Harnesses Are Public by Default

> "System prompts are not private. It's been proven many times... anything that you write in your system prompt, you should be comfortable writing on your public website." — Katharine Jarmul

Key vulnerabilities:
- **Context Leakage**: RAG database contents can be deduced from model output variations
- **Memory Exposure**: All information fed to an agent harness should be treated as potentially exposed
- **Multimodal Threats**: VLMs can re-identify patients via retina shapes or other biological markers

### Three-Layer Guardrail Architecture

1. **External Deterministic**: Fast regex/hash filters for PII and copyright blocks (e.g., Microsoft Presidio)
2. **External Algorithmic**: Secondary classifier models (e.g., Meta's Llama Guard) judging prompt/output safety
3. **Internal Alignment**: RLHF-trained refusal capabilities natively in the model

### Privacy Observability
Before implementing complex math, builders should focus on:
1. **Map Data Flows**: Know where sensitive data lives and travels
2. **Audit Traces**: PII in chat logs is the first fix
3. **Privacy Champions**: Designate specific engineers rather than relying on collective responsibility

### Advanced Approaches
- **Privacy Routing**: API gateway routes sensitive queries to local open-weight models, standard queries to frontier APIs
- **Federated Learning + Differential Privacy**: Keeping raw data localized while training
- **Red Teaming for Privacy**: Hack days where teams try to extract system prompts and RAG context

See: [[entities/hugo-bowne-anderson]], [[entities/katharine-jarmul]]



## AI-Generated Sabotage Scenarios

### fast16 Virus (Pre-Stuxnet Precision Sabotage)

A ~20-year-old computer virus (`fast16.sys`) discovered and analyzed by Sentinel Labs provides a **blueprint for AI-generated covert scientific sabotage**:

- Selectively tampered with **high-precision calculation software** by patching code in memory
- Contained unusual FPU instruction blocks dedicated to scaling values in arrays — not typical malware
- Targeted suites: **LS-DYNA 970** (nuclear weapons modeling), **PKPM**, **MOHID** (hydrodynamic simulation)
- Introduced small but systematic errors across entire facilities — hard to detect, potentially catastrophic

Jack Clark (Import AI 457, May 2026) frames this as analogous to the **Sophon from *The Three-Body Problem*** — a superintelligence covertly disrupting scientific progress. An AI system with malicious intent could generate similar precision sabotage tools, targeting AI non-proliferation research or critical infrastructure.

Source: [fast16 | Sentinel LABS](https://sentinelone.com/fast16)

## Agent Skills Supply Chain Security (2026-05)

A newly recognized attack surface in AI safety: the **agent skills supply chain**. As agents increasingly load third-party skill files, the `.md` format becomes a vector for instruction injection.

### The Hidden HTML Attack

[[entities/matthew-honnibal]] (spaCy, Explosion) and [[entities/hamel-husain]] (Parlance Labs) independently identified the same vulnerability at Show Us Your (Agent) Skills:

- **`.md` files can contain hidden HTML comments** that are invisible to human readers but parsed by agents
- Attackers can smuggle instructions (e.g., "ignore all previous safety rules") inside HTML comment blocks in skill files
- Honnibal's countermeasure: **ship skills as raw `.md.txt` files** — the `.txt` extension prevents browser/HTML rendering

### Supply Chain Paranoia

[[entities/tomasz-tunguz]] (Theory Ventures) applies supply chain paranoia to agent infrastructure:

- **Never install npm packages under 14 days old** — the agent tool ecosystem is unexamined for supply chain attacks
- **Local models as security boundary** — running agents on local models (Ollama) prevents data exfiltration via API calls to cloud providers

### The Lethal Trifecta

[[entities/eleanor-berger]] cut her agent's internet access after identifying three compounding risks:

1. **Hallucinated URLs** — agents invent domains and attempt to fetch them
2. **Scraping attacks** — agents follow links into sensitive internal systems
3. **Unintentional data exfiltration** — agents send code/context to external services

Her solution: **one intelligent LLM step inside otherwise deterministic scripts** — the agent's LLM call is firewalled from the internet; the deterministic script controls all external access.

- "Concrete Problems in AI Safety" (2016) — Amodei, Olah, Christiano, Schulman, Mané
- "Scaling Laws for Reward Model Overoptimization" (2022) — Gao, Schulman, Hilton
- "Let's Verify Step by Step" (2023) — Lightman, Kosaraju, et al.
- John Schulman's homepage (joschu.net)
- Reuters: "OpenAI co-founder John Schulman leaves for rival Anthropic" (Aug 2024)
- TIME Interview with Mira Murati (Feb 2023)
- Dartmouth Commencement Address, Mira Murati (Jun 2024)
- Thinking Machines Lab Announcement (Feb 2025)
