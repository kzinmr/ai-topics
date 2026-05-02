# State of AI 2025: 100T Token LLM Usage Study

**Source:** [OpenRouter](https://openrouter.ai/state-of-ai)
**Authors:** Malika Aubakirova (a16z), Alex Atallah (OpenRouter), et al.
**Date:** December 2025
**Scope:** Analysis of 100 trillion tokens of real-world LLM interactions via the OpenRouter platform.

---

## 1. Executive Summary: The "Reasoning" Inflection Point

The study identifies **December 5, 2024** (the release of OpenAI's o1) as the true turning point in AI. The industry shifted from "single-pass pattern generation" to **multi-step deliberation inference**.

### Key Findings
- **Agentic Shift:** LLM usage is moving from simple Q&A to "agentic inference"—multi-step, tool-integrated workflows. Reasoning-optimized models now represent over **50% of all token usage**.
- **Open Source Growth:** Open-weight models (OSS) reached a **30% market share equilibrium**, driven largely by Chinese providers (DeepSeek, Qwen).
- **The "Glass Slipper" Effect:** Early users who find a perfect "workload-model fit" become "foundational cohorts" with extremely high long-term retention.
- **Dominant Use Cases:** Creative **Roleplay** and **Programming** dominate actual usage, contrary to the assumption that general productivity is the primary driver.

---

## 2. Open vs. Closed Source Dynamics

While proprietary models (Anthropic, OpenAI, Google) still serve the majority of tokens, OSS models have grown steadily to a **30% equilibrium** by late 2025.

### The Rise of Chinese OSS
- **Market Share:** Chinese OSS models grew from 1.2% weekly share in late 2024 to nearly **30% of total usage** in peak weeks of 2025.
- **Top OSS Players (by Trillions of Tokens):**
  1. **DeepSeek:** 14.37T
  2. **Qwen:** 5.59T
  3. **Meta LLaMA:** 3.96T
  4. **Mistral AI:** 2.92T
- **Market Fragmentation:** The OSS market shifted from a DeepSeek near-monopoly to a pluralistic mix where no single model exceeds 25% share.

### Model Size Trends: "Medium is the New Small"
The market is bifurcating away from very small models (<15B parameters):
- **Small (<15B):** Declining usage due to high fragmentation and churn.
- **Medium (15B–70B):** Rapid growth — "Model-Market Fit" (e.g., Qwen 2.5 Coder 32B, Mistral Small 3). Users seek a balance of capability and efficiency.
- **Large (>70B):** "Flight to quality" — users benchmark multiple frontier models rather than settling on one.

---

## 3. The Rise of Agentic Inference

Usage is evolving from "stateless requests" to "long-running conversations and execution traces."

- **Reasoning Models:** Tokens routed through reasoning-optimized models (e.g., Grok Code Fast, Gemini 2.5 Pro) rose from negligible levels in Q1 2025 to **over 50% of all usage** by year-end.
- **Tool Calling:** Successful tool invocations have trended upward consistently, with Claude 4.5 Sonnet rapidly gaining share.
- **Sequence Length Explosion:**
  - Average prompt tokens increased **4x** (from ~1.5K to >6K).
  - Average completion tokens nearly **tripled** (from ~150 to 400).
  - **Insight:** "The typical request today is less about open-ended generation... and more about reasoning over substantial user-provided material."

### Provider Specializations
- **Anthropic (Claude):** 80% Programming + Technology. Dominant in tool calling.
- **Google (Gemini):** Broadest usage mix (Legal, Science, Translation, General Q&A).
- **DeepSeek:** Dominated by Roleplay and casual chat (>66%).
- **xAI (Grok):** Overwhelmingly concentrated in Programming.

---

## 4. Category Analysis: What are people actually doing?

### The Programming Dominance
Programming queries grew from 11% to **over 50% of total token volume** in late 2025.
- **Market Share:** Anthropic (Claude) dominates coding with ~60% share.
- **Complexity:** Programming prompts are 3–4x longer than general-purpose prompts, often exceeding 20K tokens.

### The Roleplay Powerhouse
Roleplay accounts for **over 50% of all OSS token usage**.
- **Sub-tags:** 58% Role-Playing Games, 15.6% Writers Resources, 15.4% Adult.
- **Insight:** OSS models have an edge here because they are often less constrained by commercial safety filters, allowing deeper customization for fantasy/entertainment.

### Other Categories
- **Technology:** Commands the highest cost-per-token while maintaining high usage.
- **Science:** 80.4% is actually "Machine Learning & AI" meta-questions.
- **Health/Legal:** Highly fragmented; users explore rather than structure workflows.

---

## 5. The Cinderella "Glass Slipper" Phenomenon

The study introduces a new framework for understanding user retention:

> "When a newly released model happens to match a previously unmet technical and economic constraint, it achieves the precise fit — the metaphorical 'glass slipper.' For the developers... this alignment creates strong lock-in effects."

- **Foundational Cohorts:** Early adopters of Gemini 2.5 Pro and Claude 4 Sonnet show ~40% retention at Month 5, far higher than later cohorts.
- **The Boomerang Effect:** DeepSeek cohorts show "resurrection jumps" — users leave, test alternatives, and return, confirming DeepSeek as the optimal fit for their specific workload.

---

## 6. Geography & Economics

### Global Usage
- **North America:** <50% of total spend.
- **Asia:** Share doubled from 13% to **31%** in 2025.
- **Top Countries:** USA (47%), Singapore (9%), Germany (7.5%), China (6%).

### Cost vs. Usage Dynamics

**Price Inelasticity:** Demand is relatively price-inelastic; a 10% price drop only yields a 0.5–0.7% usage increase.

**Market Archetypes Table:**

| Segment | Examples | Characteristics |
|---------|----------|----------------|
| **Mass-Market Volume** | Programming, Roleplay | Low cost, high usage |
| **Premium Leaders** | Claude 3.7 Sonnet | ~$2/1M tokens, high usage. Users pay for reliability |
| **Efficient Giants** | Gemini 2.0 Flash, DeepSeek V3 | <$0.40/1M tokens, high volume. Default workhorses |
| **Premium Specialists** | GPT-5 Pro | ~$35/1M tokens, low volume. Niche high-stakes tasks |

**Jevons Paradox:** Making models cheaper and faster has led to users running longer contexts and more iterations, ultimately consuming *more* total tokens.

> **Key Quote:** "Closed source models capture high value tasks, while open source models capture high volume lower value tasks."

---

## 7. Methodology Notes

- **Platform:** OpenRouter's router infrastructure, providing unified access to 300+ models.
- **Data Scope:** 100 trillion tokens processed across billions of user interactions.
- **Categorization:** Automated classification of user prompts into taxonomic categories.
- **Collaborators:** a16z infrastructure team (Malika Aubakirova) and OpenRouter team (Alex Atallah).

## Related Pages
- [[concepts/openrouter-state-of-ai-2025]]
- [[concepts/glass-slipper-effect]]
- [[entities/openrouter]]
