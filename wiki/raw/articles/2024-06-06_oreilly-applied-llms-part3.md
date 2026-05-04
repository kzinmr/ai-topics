---
title: "What We Learned from a Year of Building with LLMs (Part III): Strategy"
source: "https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-iii-strategy/"
authors: ["Eugene Yan", "Bryan Bischof", "Charles Frye", "Hamel Husain", "Jason Liu", "Shreya Shankar"]
date: 2024-06-06
tags: [llm, production, strategy, product-market-fit, competitive-advantage, economics, oreilly]
---

# What We Learned from a Year of Building with LLMs (Part III): Strategy

Published by O'Reilly Media, June 2024. Co-authored by **Eugene Yan, Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, and Shreya Shankar**.

Strategy answers the "what" and "why" behind the "how." The core philosophy: **focus on the system, not the model**, and prioritize human-centric workflows over total automation.

---

## 1. Resource Allocation: "No GPUs Before PMF"
- **Training from scratch is a distraction:** Even BloombergGPT was outclassed by GPT-4 within a year.
- **Fine-tuning is "Heavy Machinery":** Don't fine-tune until proven necessary. It's a commitment to repeat every time a new base model releases.
- **The Build vs. Buy Spectrum:**
  - Start with APIs (OpenAI/Anthropic) to validate ideas quickly.
  - Self-host for Scale/Privacy (Llama 3) only when needed — e.g., BuzzFeed reduced costs 80% via fine-tuning.

---

## 2. Building a Durable Competitive Advantage
Models are the "least durable" component — rapidly replaced by newer versions.

### Focus on the "System Moat"
Invest in components that surround the model:
- **Evaluation Chassis:** Reliable measurement across different models.
- **Guardrails:** Safe outputs regardless of underlying model.
- **Caching:** Reduce latency and cost.
- **Data Flywheel:** Production data iteratively improves the system.

### Strategic Procrastination
Avoid building features model providers are incentivized to build themselves. "Don't point your shears at the same yaks that OpenAI or other model providers will need to shave."

---

## 3. Product Design: Human-Centered AI
Advocate for the **"Centaur" paradigm** — pairing capable humans with LLM tools rather than full replacement.

- **Narrow the Scope:** Generic "chat with your data" is shallow. Specialize in domain-specific formats.
- **AI in the Loop:** LLMs should accelerate workflows (like GitHub Copilot), not drive them.
- **Avoid "Sparkle" Features:** Don't build vanity AI features becoming commodities (documentation chatbots). Focus on core product alignment.

---

## 4. The Implementation Playbook
1. **Prompt Engineering First:** CoT, n-shot, structured I/O.
2. **Build Evals Early:** Start with unit tests and model-based evaluators.
3. **Kickstart the Data Flywheel:** Human eval → annotate → fine-tune/update prompts → repeat.

---

## 5. The Economics of "Low-Cost Cognition"
- **The 6-Month Halving:** Cost to run text-davinci-003-level performance dropped from $20 to $0.20 per million tokens in 18 months.
- **Strategic Forecasting:** Applications too expensive today ($60/hour for generative NPCs) will become economical in 12-24 months.
- **Insight:** "What is a completely infeasible floor demo today will become a premium feature in a few years and then a commodity shortly after."

---

## 6. From Demos to Products
The gap between a "magic" demo and a reliable product is vast. "The first neural-network-driven car was 1988... It took 35 years to go from prototype to commercial product."

**Key Takeaway:** Move beyond "0 to 1" (the demo) and focus on "1 to N" (the scalable, reliable product) by applying rigorous engineering and operational discipline.
