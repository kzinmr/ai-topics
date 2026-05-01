# Google Cloud Next 2026: Sundar Pichai Keynote

**Source:** https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/
**Date:** April 22, 2026
**Author:** Sundar Pichai, CEO of Google and Alphabet

## Key Themes

### Business Momentum
- First-party models process 16 billion tokens per minute (up from 10 billion)
- Over 50% of Google's total ML compute investment allocated to Cloud business in 2026
- Gemini Enterprise saw 40% growth in paid monthly active users QoQ in Q1

### The Agentic Gemini Era
- Google shifting from building individual AI agents to managing thousands at scale
- Gemini Enterprise Agent Platform: "mission control for the enterprise" — full-stack environment to build, scale, govern, and optimize agents
- Provides "connective tissue" between data, people, and organizational goals

### 8th Generation TPUs (Dual-Chip Approach)
- **TPU 8t** (Training): Up to 9,600 TPUs in a superpod, 2PB shared HBM, 3x processing power of Ironwood, 2x more performance/watt
- **TPU 8i** (Inference): 1,152 TPUs per pod, 3x more on-chip SRAM, optimized for low latency at millions-of-agents scale

### AI-Powered Cybersecurity
- Partnership with Wiz: Google Threat Intelligence + Wiz Cloud Security
- AI Application Protection Platform (AI-APP): autonomous protection from code to cloud

### Google as "Customer Zero" (Internal AI Adoption)
- **75% of all new code at Google is AI-generated** (up from 50% in late 2025)
- Agent-led code migrations 6x faster than manual engineering
- Security agents triage tens of thousands of reports, reducing mitigation time by over 90%
- CodeMender: internal AI agent to find and fix critical software flaws
- Gemini app for macOS: idea → native Swift prototype in "a few days" using Antigravity

### Upcoming
- Google I/O: May 19, 2026

---

# Introducing Gemini Enterprise Agent Platform

**Source:** https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
**Date:** April 22, 2026
**Key Shift:** Vertex AI evolving into Gemini Enterprise Agent Platform

## Four Core Pillars

### 1. Build: Development Environments
- **Agent Studio:** Low-code visual interface for rapid prototyping
- **Agent Development Kit (ADK):** Code-first framework supporting graph-based sub-agent networks
- **Agent Garden:** Pre-built agent templates (financial analysis, invoice processing, code modernization)
- **Multimodal Streaming:** Live audio and video cues

### 2. Scale: Performance & Persistence
- **Agent Runtime:** Sub-second cold starts, rapid provisioning
- **Long-running Agents:** Autonomous workflows running for days
- **Memory Bank:** Persistent long-term context across sessions
- **Agent Sandbox:** Hardened isolated environment for code/browser execution

### 3. Govern: Security & Control
- **Agent Identity:** Unique cryptographic ID per agent
- **Agent Registry:** Central source of truth for approved agents, tools, skills
- **Agent Gateway:** Air traffic control with Model Armor (prompt injection defense)
- **Anomaly Detection:** LLM-as-judge for unusual reasoning or malicious activity

### 4. Optimize: Quality Assurance
- **Agent Simulation:** Synthetic user interaction testing
- **Agent Evaluation & Observability:** Full execution traces, real-time dashboards
- **Agent Optimizer:** Automatic failure clustering, system instruction refinement

## Model Access
- 200+ models via Model Garden: Gemini 3.1 Pro, Gemini 3.1 Flash Image, Lyria 3, Gemma 4, Anthropic Claude (Opus, Sonnet, Haiku)
- Native integrations: BigQuery, Pub/Sub, MCP

## Case Studies
- L'Oréal: ADK for autonomous orchestration via MCP
- Comcast: Multi-agent Xfinity Assistant
- PayPal: Agent Payment Protocol (AP2)
- Payhawk: Memory Bank reduced expense submission by 50%
- Gurunavi: Proactive restaurant suggestions targeting 30% satisfaction increase
