---
title: "Production-Ready Agent Engineering — Office Hours with Kyle Corbitt (Lecture Transcript)"
author: Kyle Corbitt
date: 2025-06-27
date_ingested: 2026-06-11
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: transcript
tags:
  - reinforcement-learning
  - reward-hacking
  - rlhf
  - ai-agents
  - context-engineering
  - fine-tuning
  - agent-evaluation
  - education
  - transcript
related_article: articles/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours.md
participants:
  - Kyle Corbitt (host, OpenPipe CTO)
  - Phlo (participant)
  - Jhordan (participant)
  - Hendrik Reh (participant)
  - Steve James (participant)
  - Ari (participant)
  - Darren (participant)
  - Anoop (participant)
  - Nick (participant)
---

# Production-Ready Agent Engineering — Office Hours with Kyle Corbitt (Lecture Transcript)

**Host:** Kyle Corbitt (CTO, OpenPipe)
**Date:** June 27, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]

---

## Overview

Unscripted office hours covering: reward function design and reward hacking mitigation, RLHF workflow for low-volume human feedback, custom reward model training (Hacker News title predictor), agent framework tradeoffs (Agents SDK vs custom loops), RL vs prompt engineering decision criteria, and model customization via training tags.

---

## 1. DSPy and GRPO

**[00:02:30]** Fernando asks: what role will DSPy play in RL next steps? Kyle's take: DSPy is an interesting project but requires full ecosystem buy-in, making it hard to combine with other tools. They have prompt optimizers (MerPO v2 is the most popular) and a GRPO optimizer, but Kyle hasn't heard of people getting good results with the GRPO optimizer yet — prompt optimizer yes, GRPO less so far.

---

## 2. Reward Function Design & Reward Hacking

**[00:03:24]** Jordan asks: when designing reward functions for RL, what frameworks or methodologies determine appropriate reward signals? How do we systematically identify reward hacking?

**[00:10:47]** Kyle's general-purpose answer for larger training runs without purely verifiable reward functions:

**It's very common for the model to go off the rails.** The typical pattern: the model starts learning something real, then figures out a hack — "this is a much easier way to solve the problem" — and exploits it super hard for a big reward.

**Practical mitigation approach:**
1. **Reframe as iterative process** — start with your best guess reward function, observe rollouts
2. **Eyeball rollouts** — reward hacking is usually not subtle. Once the model finds a hack, it applies it as much as possible. Filter for highest-reward outputs and look at them
3. **Add LM judge checks** — explicitly say "if you see X behavior, that's bad, return a fail," then penalize outputs that fail
4. **Checkpoint rollback** — grab a checkpoint from before it went off the rails, restart from there with the patched reward function (not the most principled approach, but saves time)

**[00:37:23]** Kyle is getting "much more bullish on not needing to do any of this stuff" — getting really good results with almost ungrounded LM judges as reward models for RL. Some tasks need custom reward models, but many don't.

---

## 3. Agent Frameworks: Custom Loops vs SDKs

**[00:04:51]** Phlo asks: what do you lose using the Agents SDK vs writing your own loop? Would Hugging Face's Small Agents make sense for OSS models?

**Kyle's take:**
- It's unlikely in 6 months we'll be writing our own agentic loops — a canonical abstraction will emerge
- Current problem: existing frameworks limit flexibility, and we don't yet know what the right patterns are
- Example: if you want to experiment with context summarization, sub-agents, or custom message pruning, frameworks that don't anticipate those patterns force you to tear everything out
- For RL training specifically, combining frameworks with RL is possible (engineer on Kyle's team has a demo using Art with LangGraph)
- The limitation is flexibility in getting results you want, not RL compatibility

> **Phlo feedback:** The live coding session was extremely valuable — "you guys could just live code the entire time and I'd get so much value out of it."

---

## 4. RLHF for Low-Volume Human Feedback

**[00:13:52]** Hendrik asks: working on an agent-based sales quoting system — agent drafts quotes, salesperson edits them. How to turn this feedback into usable reward signal for RL?

**Hendrik's context:** Sales agent looks up product catalog, availability, pricing, identifies upselling/cross-selling opportunities, presents draft to salesperson. Heavy personal context in long-term customer relationships that isn't captured anywhere.

**Kyle's framework — 2 phases:**

**Phase 1 (before RL): Focus on context extraction.** The biggest issue is that the human has context the agent doesn't have access to. Before thinking about RL, extract that context — customer history, personal preferences, relationship baggage. This is the lowest-hanging fruit and where you'll see the biggest improvement.

**Phase 2 (after context is solved): Use feedback for optimization.**

For **low volume** (POC stage, few dozen examples):
- Train a judge prompt to predict "given inputs and this output, would the human have already edited this?"
- Use your small set of before/after examples to tune the prompt
- Once calibrated, use that judge as your reward model for RL

For **high volume** (thousands per week):
- Train a classifier model on before/after pairs (human-edited vs raw output)
- These classifiers can be "surprisingly effective"
- Use as reward model in the RL loop — classic RLHF

**[00:45:10]** Fernando follows up: how much volume for reliable reward model training? Kyle's answer: **20,000+ examples** for a classical classification reward model. Continued improvement up through hundreds of thousands. Potentially much more sample-efficient with reasoning models + few-shot RFT approach (unproven but promising).

---

## 5. Custom Reward Model Training: Hacker News Title Predictor

**[00:21:33]** Steve asks about the reward model design from Kyle's reward hacking blog post / lightning lesson.

**Project:** Build a model that generates good Hacker News titles.

**Pipeline:**
1. **Data collection:** HN API → scrape ~1M stories (title, upvotes, URL)
2. **Content extraction:** Scrape actual article content using [Readability](https://github.com/mozilla/readability) library (TypeScript) — same library that powers Firefox reader mode
3. **Data cleaning:** LM judges (Gemini 1.5 Flash, <$100 for 1M stories) to filter for complete, non-paywalled content. Heuristic filters (>200 chars body text)
4. **Reward model training:** Classification model (Llama 3.1 8B) to predict HN score from story body + title

**Key design decisions:**
- **Log scores** — HN scores follow power law; predicting log(score) normalizes errors (off by 2x on a 100-point story vs off by 100x on a 1-point story)
- **Batch size 32** — smaller batches didn't converge well
- **Liger Kernel** — ~50% training speedup from fused layers (LinkedIn's library). Unsloth now also supports sequence classification
- **LoRA** — for relatively small training runs (1-2 hours), LoRA doesn't get saturated; works fine vs full fine-tuning
- **55% correlation** between predicted and actual scores on validation set

**Architecture:** `AutoModelForSequenceClassification` — takes autoregressive LLM, replaces final token prediction layer with single-number output. Fine-tunes all layers to reshape embeddings toward the specific task.

**[00:48:06]** Ari asks: what if you freeze the LLM and just train on embeddings? Kyle tried this — just a single classification layer on top of frozen embeddings. **Didn't get good results.** There's value in updating earlier layers to modify representations toward the specific prediction task.

---

## 6. Training Tags for Custom Behavior

**[00:41:39]** Jordan asks: how are tags (like DeepSeek's thinking tags) used in post-training? Can tags encode custom behaviors?

**Kyle's answer:**
- No standard — each model/company defines what tags mean during their post-training process
- Read the model card (HuggingFace page) to understand what tags a model was trained with
- For custom models: absolutely yes, you can introduce tags during training. Models are "shockingly good" at picking up tag semantics from just a few examples — you don't need to explicitly tell it the rule

---

## 7. RL vs Prompt Engineering Decision

**[00:38:52]** Nick asks: how do you know when you need RL vs more context engineering?

**Kyle's mental framework:**
1. **Ask:** If I gave this context to a smart generalist (non-domain-expert), could they produce a good result?
2. If **no** → focus on context engineering first. Identify what information a human would need and make it available via tools
3. If **yes** (model has the info but isn't using it correctly, maybe 50% of the time) → **this is where RL helps.** Reinforce correct interpretation of ambiguous information

---

## 8. Context Engineering Principles

**[00:50:50]** Darren asks: are there fundamental principles of context engineering (information order, chunking, etc.)?

**Kyle's honest answer:** Not an area he's done much research in. His sense from the meta-discussion: it's very model-dependent. Some models work better with instructions before context, others after. Sometimes repeating components helps. "Ripe for being turned into more of a science" — would be a great publication topic.

---

## 9. Jailbreaking via Fine-Tuning

**[00:52:43]** Jordan asks: how to change DeepSeek R1 to answer questions about Tiananmen Square without affecting other abilities?

**Kyle's answer:** Relatively straightforward. Even ~10 SFT examples of answering such questions appropriately is usually enough to bypass alignment. The safety alignment is usually "pretty superficial" — a late-stage RL or SFT loop that's easy to override. Meta published research on making this harder, but it's not where open-source model publishers are focused.

---

## 10. Meta-Optimization of Agent Architecture

**[00:55:52]** Ari asks: has there been work on using RL to optimize agent architecture itself (e.g., which tools to use, control flow)?

**Kyle's take:**
- Sakana (Japanese AI lab) published a paper on pseudo-genetic algorithms where agents spawn sub-agents with different architectures
- Interesting but too many degrees of freedom for current approaches
- The real trend is toward **less structure** in agents — letting them drive control flow at runtime rather than pre-defining workflows

---

## 11. Model Selection for Experimentation

**[00:58:30]** Anoop asks: what model/parameter size for experimentation?

**Kyle's go-to:** Qwen 2.5 14B — his standard model for new tasks. Step up/down from there as needed. For tasks that work with prompted models (even o3), Qwen 2.5 14B can also work well after RL.

---

## Companion Resources

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [Reward Hacking blog post](https://openpipe.ai/blog/reward-hacking) (Kyle Corbitt)
- [HN title generator code](https://github.com/OpenPipe) (shared during session)
- [Readability](https://github.com/mozilla/readability) — Mozilla's HTML-to-structured-content library

## Related

- [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
- [[concepts/reward-hacking]]
- [[concepts/grpo-rl-training]]
- [[concepts/agentic-rl]]
- [[concepts/context-engineering]]
- [[concepts/corbett-kyle-corbitt]]
- [[entities/openpipe]]
