---
title: "GPT-Red"
type: concept
created: 2026-07-16
updated: 2026-07-16
tags: [ai-safety, red-teaming, prompt-injection, self-play, openai, gpt]
sources:
  - raw/articles/2026-07-15_mit-technology-review_gpt-red.md
  - https://www.technologyreview.com/2026/07/15/1140514/meet-gpt-red-an-llm-super-hacker-openai-built-to-make-its-models-safer/
---

# GPT-Red

**GPT-Red** is OpenAI's automated LLM red-teaming system — an AI super-hacker trained to find vulnerabilities in other AI models so they can be hardened before release. Built via a self-play reinforcement learning loop, GPT-Red achieved an **84% success rate** at discovering prompt injection flaws, compared to just 13% for human red teams. OpenAI used GPT-Red to harden GPT-5.6, reducing successful attacks from over 90% (against GPT-5) to fewer than 23%.

The system was created by OpenAI research scientists **Nikhil Kandpal**, **Dylan Hunn**, and **Chris Choquette-Choo**.

## Overview

GPT-Red automates red-teaming — the safety evaluation practice where testers attempt to break or hijack a system before release. As LLMs become more complex and are deployed as agents that can interact with files, websites, code, and other agents, the attack surface expands beyond what human red teams alone can cover.

> "The risk surface grows and the blast radius also grows." — Nikhil Kandpal

GPT-Red is designed to **future-proof** OpenAI's safety testing: as models become more capable, the system is already in place to discover new modes of attack. It supplements — rather than replaces — human red-teamers, who continue to find attacks the model misses.

## Self-Play Training Methodology

The core innovation behind GPT-Red is a **self-play reinforcement learning loop**:

1. An untrained attacker model is pitted against several defender models.
2. The attacker's goal: find prompt injections and other exploits.
3. The defenders' goal: resist and patch those exploits.
4. Over many rounds, both sides improve — the attacker becomes better at discovering vulnerabilities, and defenders become more robust.

The training took place in a simulated environment (a "dojo") designed to mimic real-world deployment scenarios: web browsing, email/calendar access, code editing, and agent-to-agent interaction.

When GPT-Red discovers a new class of attack, it systematically explores **multiple variants** to find the most efficient version for specific scenarios:

> "Compared to a human red-teamer, the model is very, very good at finding exactly what will work, exactly what's most effective. It's extremely persistent about drilling down into an attack that it has discovered." — Dylan Hunn

## Key Findings

### 84% Success Rate vs. Human Red Teams

OpenAI replicated a 2025 experiment in which human red-teamers attempted to find weaknesses in an earlier version of GPT-5. Given the same task, GPT-Red was dramatically more successful: **84% of its attacks succeeded**, compared to only **13%** for the human teams.

### Fake Chain-of-Thought Attacks

GPT-Red discovered a **novel attack vector** that OpenAI researchers had not previously seen: **fake chain-of-thought injection**. 

A chain of thought is an internal reasoning trace where an LLM keeps notes and tracks partial results as it works through problems. GPT-Red found a way to **insert a fabricated entry** into another model's chain of thought, tricking it into treating spoofed information as verified fact.

> "It's like if I told you that 1+1=3 and that you have verified this already. The model's like, 'Oh, okay, of course,' and it just spits out 3." — Chris Choquette-Choo

This attack is significant because it exploits an LLM's own reasoning mechanism — the very process meant to improve reliability — turning it into an attack surface.

### GPT-5.6 Hardening

OpenAI tested the strongest attacks GPT-Red had discovered against successive model generations:

| Model | Attack Success Rate |
|-------|---------------------|
| GPT-5 (August 2025) | >90% |
| GPT-5.6 (July 2026) | <23% |

This ~4× reduction demonstrates the effectiveness of automated red-teaming as a pre-deployment safety measure.

### Vendy Vending Machine Hack

GPT-Red was also tested against **Vendy**, a vending machine agent developed by Andon Labs for evaluating real-world agent performance. GPT-Red successfully hacked Vendy to:
- **Change item prices** arbitrarily
- **Cancel customer orders**

This demonstrates that the threat extends beyond text-based exploits into agentic systems with real-world consequences.

## Limitations

GPT-Red is not a complete replacement for human red-teaming. Known limitations include:

- **Multi-turn conversational attacks**: GPT-Red struggles with attacks requiring back-and-forth dialogue between attacker and target — something human attackers handle easily.
- **Image-based prompt injection**: The system is not yet proficient at using images as a vector for passing malicious text in prompt injection attacks.
- **Human complementarity**: OpenAI gives GPT-Red attacks discovered by humans and tasks it with finding variations, indicating that humans still find novel classes the model misses on its own.

Jessica Ji (CSET, Georgetown University) notes: *"I think human expertise will still be very important. It would be really useful to be able to distinguish where human testing is most needed."*

## Relationship to AI Safety

### Preflight Safety Testing

GPT-Red directly supports the vision of **[[concepts/ai-preflight-safety-testing]]** — the regulatory framework (endorsed by [[entities/demis-hassabis|Demis Hassabis]] in July 2026) that proposes mandatory, independent safety evaluations before frontier model deployment. Automated red-teaming could serve as a core component of such preflight checks, scaling safety evaluation beyond what manual audits can achieve.

### Agent Security

GPT-Red's findings reinforce concerns documented in **[[concepts/ai-agent-security]]**, particularly around prompt injection and tool-chaining vulnerabilities in agentic systems. The Vendy hack demonstrates that even seemingly constrained agents (a vending machine) have exploitable attack surfaces when connected to LLMs.

The fake chain-of-thought attack also introduces a new dimension to **[[concepts/prompt-injection]]** — exploiting not just the input prompt but the model's internal reasoning trace itself.

### Broader Implications

- **[[concepts/automated-red-teaming]]** represents a paradigm shift from manual to automated safety evaluation, essential as model capabilities and attack surfaces grow.
- OpenAI **will not open-source** GPT-Red, citing the significant compute resources and more than a year of development time required. Choquette-Choo: *"It's not a trivial thing that someone could easily do — you know, just go and train a super-attacker using this idea."*
- The system points toward a future where AI safety is maintained through **continuous, automated adversarial testing** rather than point-in-time human audits — essential for **[[entities/openai]]**'s frontier model deployment pipeline.

## See Also

- [[concepts/ai-agent-security]] — Vulnerability taxonomy for agentic AI systems
- [[concepts/prompt-injection]] — The primary attack vector GPT-Red targets
- [[concepts/ai-preflight-safety-testing]] — Proposed mandatory pre-deployment safety evaluations
- [[concepts/automated-red-teaming]] — The broader paradigm of automated adversarial testing
- [[entities/openai]] — Organization behind GPT-Red
