# Hermes vs. OpenClaw, Cybersecurity Alarms Ring, More-Interactive Conversations, Can Agents Do Human Work?

**Source:** DeepLearning.AI Newsletter (The Batch)
**URL:** https://info.deeplearning.ai/hermes-vs.-openclaw-cybersecurity-alarms-ring-more-interactive-conversations-can-agents-do-human-work
**Date:** 2026-05-22

---

## Hermes Agent Challenges OpenClaw

**Open-source agent Hermes** (Nous Research, Feb 2026) has recently overtaken OpenClaw on OpenRouter's daily token-consumption leaderboard. Its standout features are **self-improving skill creation** and a sophisticated memory architecture.

### Core Capabilities
- Runs locally or in the cloud; supports a wide variety of LLMs; integrates with ~20 messaging services.
- Works with IDEs via the Agent Communication Protocol.
- Agentic loop: assembles a prompt (personality + tools + skills + memory + conversation history) → summarizes old messages if needed → sends to LLM → executes tool/skill call or responds → repeats until a final response.

### Skill System
- Uses `SKILL.md` instruction files; comes with built-in skills and an (as yet smaller) Skills Hub.
- **Creates new skills automatically** after long problem-solving or successful error fixes.
- A background **Curator** system archives skills unused for >90 days and uses an LLM to decide whether to keep, merge, or archive each skill.

### Memory & Goal Tracking
- Two general memory files: user preferences, and workflows/lessons learned.
- Memory tool checks for duplicates/vagueness before appending; merges related entries when files become too long.
- External memory providers like Honcho can analyze user identity.
- **Persistent goal tracking**: the agent calls a judge model after a response to see if a goal is completed; if not, it continues until completion or max turns. (Similar to Claude Code, OpenAI Codex, OpenClaw.)

### Context
OpenClaw's immense popularity and initial security issues spawned a wave of agents. Hermes's self-improving capabilities point toward a shift from stateless assistants to agents that accumulate experience and automate ongoing work.

> "It points toward a shift from stateless AI assistants to agents that accumulate experience, adapt to users, and automate ongoing work beyond isolated tasks."

### Token Efficiency Concern
Some users note Hermes Agent is **less token-efficient** than OpenClaw.

---

## Built-In Conversational Interactivity: TML-Interaction-Small

**Thinking Machines Lab's** first public model is a multimodal system that processes audio, video, and text **concurrently**, not turn-by-turn.

### Key Specs
- **Architecture:** Mixture-of-experts transformer, 276B total params / 12B active per token; separate background reasoning model (undisclosed).
- **Input/Output:** concurrent audio, video, text in → concurrent audio and text out.
- **"Micro-turns":** interleaves 200 ms chunks of processing/generation, eliminating the boundary between input and output.
- **Training:** "Encoder-free early fusion" – the transformer, hierarchical MLP (for image patches of 40×40 px), and flow-matching decoder were trained together from scratch, skipping large pretrained encoders.
- **Background model** handles reasoning, web browsing, and tool calls asynchronously; the interaction model weaves its output into the conversation.

### Performance Benchmarks
- **Audio latency (FD-bench V1):** 0.40 s (vs. Gemini-3.1-flash-live-preview minimal 0.57 s, GPT-Realtime-2 minimal 1.18 s).
- **Interruptions/interjections (FD-bench V1.5):** 77.8 average quality (GPT-Realtime-2 xhigh 47.8, Gemini 45.5).
- **Multi-turn audio reasoning (Audio MultiChallenge):** 43.4% APR – behind GPT-Realtime-2 xhigh (48.5%), ahead of Gemini (36.1%).
- **Audio reasoning (BigBench Audio):** 96.5% accuracy (with background model) – nearly tied with GPT-Realtime-2 and Gemini (both 96.6%).

---

## Cybersecurity Alarms Grow Louder (Google Report)

Hackers used an LLM to find a previously unknown vulnerability in a widely used web administration tool, enabling them to bypass **two-factor authentication**. Google's cybersecurity report catalogs accelerating LLM-assisted attacks while also noting LLM-assisted defense improvements.

---

## Can Agents Do Human Work?

Analysis of whether AI agents can truly replace human knowledge workers, examining current capabilities and fundamental limitations.
