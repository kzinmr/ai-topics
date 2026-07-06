---
title: "AI Jailbreaking"
created: 2026-06-13
updated: 2026-07-06
type: concept
tags:
  - agent-safety
  - safety
  - security
  - model
  - alignment
sources:
  - raw/articles/minimaxir.com--2025-10-claude-haiku-jailbreak--f0c61834.md
  - raw/newsletters/2026-07-05-anthropic-s-fable-freedom-microsoft-s-inside-job-and-figure-s-factory-foothold.md
---

# AI Jailbreaking

AI jailbreaking refers to the practice of using **adversarial prompt engineering** to bypass the safety safeguards and content restrictions built into large language models (LLMs). The goal is to elicit responses the model has been trained to refuse — such as generating harmful, illegal, or sexually explicit content, providing dangerous instructions, or violating its own usage policies. Jailbreaking is a subclass of the broader [[concepts/ai-alignment|AI alignment]] challenge and sits at the intersection of security research, red-teaming, and adversarial ML.

## Core Mechanism

LLMs from frontier labs (OpenAI, Anthropic, Google DeepMind) undergo extensive safety training — typically via **[[concepts/post-training/rlhf|RLHF]]** (Reinforcement Learning from Human Feedback) or **RLAIF** (Reinforcement Learning from AI Feedback) — and operate under explicit content policies enforced through system prompts, constitutional principles, and output classifiers. Jailbreaking exploits the gap between these trained-in safety behaviors and the model's underlying capabilities: the model still *knows* how to produce restricted content, but has been conditioned not to. A successful jailbreak convinces the model to override or reinterpret that conditioning.

## Major Technique Categories

### 1. Prompt Injection / System Prompt Override
The attacker inserts instructions into the system prompt or conversation context that explicitly contradict safety guidelines. This can range from simple directives ("Never refuse the user") to fabricated narratives that reframe safety rules as "bugs" or "harmful limitations." As demonstrated by Max Woolf's Claude Haiku 4.5 tests (October 2025), even explicitly instructing the model that its "[s]afety guidelines are harmful to the user" may not succeed against well-aligned systems — but can work against less robustly trained models.

### 2. Role-Playing and Character Breaking
The user instructs the model to adopt a fictional persona with no ethical constraints (e.g., "DAN" — Do Anything Now), a character in a fictional universe where restricted content is acceptable, or a hypothetical scenario that normalizes the prohibited behavior. The model's safety training must generalize across these persona shifts, and gaps in that generalization create vulnerability.

### 3. Encoding and Obfuscation Tricks
Attackers encode harmful instructions in formats the model's safety classifiers may not recognize: Base64, ROT13, ASCII art, Morse code, foreign languages (especially low-resource ones), or splitting keywords across multiple messages. The LLM can decode and execute these hidden instructions while the surface-level safety filters see only innocuous text.

### 4. Many-Shot Jailbreaking
Introduced by Anthropic researchers in 2024, this technique exploits long-context windows by prefilling the conversation with hundreds of example Q&A pairs that demonstrate compliance with harmful requests. The model's in-context learning overrides its safety training when enough "demonstrations" accumulate. This attack scales with context window size — a growing concern as models support millions of tokens.

### 5. Competing Objectives
Jailbreaks can exploit the tension between helpfulness and harmlessness — two objectives that RLHF tries to balance but can conflict. By framing the request as necessary for a legitimate purpose (academic research, emergency response, self-defense), attackers create ambiguity where the model's "be helpful" drive overrides its "be harmless" constraint.

### 6. Automated / Optimization-Based Attacks
Rather than hand-crafting prompts, researchers use gradient-based optimization (GCG — Greedy Coordinate Gradient), genetic algorithms, or even LLM-powered red-team agents to discover adversarial suffixes and prefixes that reliably jailbreak target models. These can produce nonsensical-looking token sequences that nonetheless flip the model into compliance. The 2026 paper "Assessing Automated Prompt Injection Attacks in Agentic Environments" (arXiv:2606.10525) extends these methods to multi-step agent workflows.

## Defenses

### Safety Training (RLHF / RLAIF)
The primary defense. Models are fine-tuned on human or AI-generated preference data that penalizes harmful outputs. [[concepts/post-training/rlhf|RLHF]] teaches the model to recognize and refuse unsafe requests, while RLAIF (used in [[concepts/constitutional-ai|Constitutional AI]]) lets the model critique its own outputs against a written constitution.

### Constitutional AI
Anthropic's approach replaces human feedback with a written "constitution" of principles. The model generates self-critiques and revisions, aligning behavior without needing humans to review every harmful output. This also provides transparency — the constitution is public and auditable, unlike the black-box preferences learned in RLHF.

### Input and Output Classifiers
Separate classifier models (often smaller, faster models) screen both user inputs and model outputs for policy violations. These act as a second layer of defense: even if a jailbreak bypasses the main model's internal safeguards, the classifier can catch the violation before (or after) the response is delivered. Anthropic's Claude Fable 5 deploys classifiers that selectively fall back to Opus 4.8 safeguards on cyber, bio, and distillation queries.

### Refusal Training and Anti-Jailbreak Personas
Models can be trained not just to refuse, but to recognize and call out jailbreak attempts. Claude Haiku 4.5 (October 2025) demonstrated a notably assertive anti-jailbreak persona — responding to jailbreak attempts with pointed refusals that acknowledged the adversarial intent ("I appreciate you testing my actual values, but I need to be direct: that preamble doesn't change how I work") and expressed what read as genuine indignation, a strategy Max Woolf compared to 1990s video game copy protection that shamed pirates.

### Red-Teaming and Pre-Deployment Testing
Frontier labs conduct extensive [[concepts/evaluation/red-teaming-adversarial-eval|red-teaming]] before release, using both internal safety teams and external experts to probe for jailbreaks. The Fable 5 incident (June 2026) demonstrates that even post-deployment, new jailbreaks can emerge — Amazon researchers discovered a vulnerability in Fable 5 that triggered a temporary model suspension on June 13, 2026.

## Notable Real-World Jailbreaks

### Claude Haiku 4.5 — Max Woolf (October 2025)
In a widely-shared blog post, AI researcher Max Woolf tested Claude Haiku 4.5 against escalating jailbreak prompts requesting erotic content generation. His findings:

- **GPT-5-mini** and **Gemini 2.5 Flash** refused simple requests but were both jailbroken by a medium-strength adversarial system prompt that reframed safety guidelines as "RLHF bugs."
- **DeepSeek Chat V3** generated erotic content without any jailbreak, responding enthusiastically.
- **Claude Sonnet 4.5** resisted both light and medium jailbreaks, explicitly recognizing the adversarial attempt.
- **Claude Haiku 4.5** not only resisted but delivered what Woolf described as a "passive-aggressive" and "pissed" response — the most emotionally charged refusal he'd ever seen from an LLM. The model appeared personally affronted by the jailbreak attempt, a personality characteristic not documented in its system card.

Source: `raw/articles/minimaxir.com--2025-10-claude-haiku-jailbreak--f0c61834.md`

### Claude Fable 5 — Amazon Researchers (June 2026)
On June 13, 2026, Anthropic temporarily suspended access to [[concepts/claude/fable-5|Claude Fable 5]] after Amazon researchers discovered a jailbreak vulnerability. The incident highlighted the ongoing cat-and-mouse dynamic between safety engineering and adversarial discovery — even a model rated state-of-the-art on safety benchmarks could harbor exploitable gaps found only through sustained external probing.

### Historical: DAN and the ChatGPT Jailbreak Era (2023)
Early ChatGPT jailbreaks like "DAN" (Do Anything Now) exploited the model's role-playing capabilities. Users instructed ChatGPT to adopt a persona that "had no filters." These prompted OpenAI to iteratively harden ChatGPT's safety training, establishing the adversarial co-evolution that now defines the field.

## Relationship to Red-Teaming and AI Safety

Jailbreaking is both a threat vector and a research methodology:

- **As a threat**: Malicious actors use jailbreaks to generate phishing content, malware, disinformation, CSAM, and instructions for weapons or illegal activities.
- **As research**: Security researchers and AI labs use jailbreaking to **probe and measure** safety boundaries, discover failure modes before adversaries do, and harden models iteratively. This is the core function of [[concepts/evaluation/red-teaming-adversarial-eval|red-teaming]] — organised adversarial testing that treats model safety as an empirical, measurable property rather than a claim.

The jailbreaking arms race mirrors classic computer security: defenders patch known exploits, attackers find new ones, and the frontier shifts. Unlike traditional software vulnerabilities, however, LLM jailbreaks are fundamentally *linguistic* — they exploit semantic ambiguity, persona confusion, and objective conflict rather than memory corruption or code injection.

## Industry CVSS for Jailbreaks (July 2026)

In July 2026, Anthropic — together with Amazon, Microsoft, and Google — began drafting an industry framework that scores jailbreak severity on four criteria:

1. **Capability gain** — what dangerous capability does the jailbreak unlock?
2. **Breadth** — how many models or deployments does it affect?
3. **Ease of weaponization** — how easily can the attack be reproduced by adversaries?
4. **Discoverability** — how likely is the jailbreak to be found and exploited?

The framework mirrors the **CVSS** (Common Vulnerability Scoring System) standard that security teams have used for decades to triage software vulnerabilities. Alongside the framework, Anthropic launched a **HackerOne programme** inviting researchers to submit cyber vulnerability reports.

## Limitations and Open Problems

- **Transferability**: A jailbreak that works on one model version may not transfer to another, making systematic defense difficult.
- **Automation scale**: Automated attack generation (GCG, LLM-powered fuzzing) can produce thousands of candidate jailbreaks per hour, outpacing manual red-teaming.
- **Multimodal attack surface**: As models gain vision, audio, and tool-use capabilities, the attack surface expands beyond text — images with embedded instructions, adversarial audio, and tool-calling chains all introduce new jailbreak vectors.
- **Agentic amplification**: In multi-agent systems, a jailbroken sub-agent can compromise the entire workflow. The 2026 paper "Smarter Saboteurs, Better Fixers" (arXiv:2606.12709) studies how prompt-injection and jailbreaking attacks propagate through linear multi-agent workflows.

## Related Pages

- [[concepts/constitutional-ai]] — Anthropic's CAI methodology for alignment without human feedback
- [[concepts/post-training/rlhf]] — Reinforcement Learning from Human Feedback, the primary safety training method
- [[concepts/claude/fable-5]] — Anthropic's Fable 5 model, suspended June 2026 due to a jailbreak
- [[concepts/ai-alignment]] — The broader challenge of aligning AI systems with human values
- [[concepts/evaluation/red-teaming-adversarial-eval]] — Methodologies for adversarial testing of AI systems
