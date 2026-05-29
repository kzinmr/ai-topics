---
title: Tomasz Tunguz
type: entity
handle: "@ttunguz"
created: 2026-05-29
updated: 2026-05-29
tags:
  - person
  - ai-agents
  - agent-skills
  - vc
  - investor
  - local-llm
  - supply-chain
  - ai-safety
  - blogger
  - ai-adoption
  - youtube
sources:
  - raw/articles/2026-05-15_vanishing-gradients_show-us-your-agent-skills-ep2.md
---

# Tomasz Tunguz (@ttunguz)

| | |
|---|---|
| **X** | [@ttunguz](https://x.com/ttunguz) |
| **Blog** | [tomtunguz.com](https://tomtunguz.com) |
| **GitHub** | — |
| **Role** | General Partner at Theory Ventures |
| **Known for** | Venture capital investing in data infrastructure (eight unicorns incl. Looker, Monte Carlo, Dremio, Hex, Omni, MotherDuck), blog driving millions of monthly pageviews, former Google PM on AdSense |
| **Bio** | Tomasz Tunguz is a General Partner at Theory Ventures, an early-stage VC fund investing $1-25M in software companies that leverage technology discontinuities into go-to-market advantages. He has worked with eight unicorns predominantly in data and data infrastructure. Before venture capital, he was a product manager at Google managing a billion-dollar business unit on the AdSense team. He writes a widely-read blog at tomtunguz.com covering AI, startups, and technology strategy. |

## Overview

Tomasz Tunguz occupies a unique position at the intersection of venture capital, data infrastructure, and AI agent engineering. Unlike most VCs who observe AI from a distance, Tunguz is a hands-on practitioner who builds his own agent workflows, defaults to local models, and writes about the implications for enterprise adoption. His blog at tomtunguz.com is one of the most influential in the VC/tech space, driving millions of pageviews per month.

As General Partner at Theory Ventures (alongside [[entities/bryan-bischof]], Head of AI), Tunguz invests in early-stage companies leveraging technology discontinuities. His portfolio spans data infrastructure (Looker, Monte Carlo, Dremio, Hex, Omni, MotherDuck) and emerging AI-native platforms. His background as a Google PM on AdSense gives him a product-minded approach to evaluating AI companies — he thinks about go-to-market mechanics, not just technology.

Tunguz's agent philosophy is distinctive for its **local-first, supply-chain-conscious, and deliberately minimalist** approach. He uses Pi as his harness, runs Qwen 35B locally via Ollama, and advocates for 2-3K token system prompts over 40K stuffed ones. His analogy of the Amish approach to technology adoption — deliberate, community-coordinated, parallel — captures his view that AI adoption requires thoughtfulness, not reflex.

## Show Us Your (Agent) Skills Episode 2 (2026-05-15)

Tomasz (referred to as "Tom" throughout) appeared alongside his Theory Ventures colleague Bryan Bischof. His segment (from approximately 1:47:15 to 2:17:54) combined live demos, investment theses, and strong opinions on AI infrastructure.

### Demo: Public Company Analysis on a Local Model

Tom demonstrated a skill for analyzing publicly traded companies. The workflow:

1. Pulls down CSVs from a data source
2. Finds the earnings transcript using Excel
3. Uses R libraries to generate charts
4. Dynamically assembles an HTML presentation with a narrative about the company's business performance

The demo used **Figma's earnings announcement** as the example. The system generated a complete analysis within 2.5 minutes on a local model, covering revenue growth (41%), net dollar retention, cash position, and AI-related quotes from the earnings call. Tom noted he has this running as a LaunchDaemon every morning to check for newly announced earnings.

### Local Models as Default

Tom is the first guest on the show to use local models for the majority of his workflow. His reasons:

- **Latency**: Local models on an M5 Mac deliver 120-140 tokens/sec with a 256K context window — faster than cloud
- **Secrets**: No fear of pasting secrets into a local model — it's not going anywhere
- **Planes**: When there's no internet, local models keep working
- **Multi-agent parallelization**: Can run five local models at once with modern inference servers

He uses **Qwen 3.6 35B** as his daily driver via Ollama. He also uses Gemma 4 4B for lightweight tasks (like Super Whisper alternatives), achieving 300ms latency vs. 3,000ms for cloud. He only goes to cloud models for "large-scale coding challenges, particularly multi-files or re-architectures of bugs."

### HTML Renaissance

Tom has rediscovered HTML as the ideal agent output format:

> "We've kind of rediscovered HTML as a great way for agents to present information to us."

His public company analysis skill generates HTML presentations rather than markdown or PDF. HTML is portable, self-contained, universally renderable, and can include rich CSS styling and JavaScript charting (he uses D3 and PresentJS). The downside: it's "really hard to share privately" without converting to PDF.

### Supply Chain Paranoia: The 14-Day npm Rule

Tom raised supply chain security as an underexamined vulnerability in agent workflows. When his agent started installing npm packages during the demo, he "panicked because I haven't pinned my npm packages and the amount of supply chain attacks is pretty significant." His heuristic:

> **Don't install anything that's newer than 14 days.**

This is a reasonable proxy for secure npm packages — enough time for the community to flag malicious packages. The open question: where does this knowledge live? Within a skill? A plugin? agents.md? QMD?

### BYOD Agents: The Next Enterprise Tension

Tom introduced the **Bring Your Own Device (BYOD) for agents** problem, based on a CIO's question at an event:

> "If I hire an undergraduate who's just recently graduated and they have spent four years embedding literally all of their education within an agent, do I allow that on my network?"

The graduate will say "if you want me to be as productive as I represent, I need that." The CISO will say "what is this thing doing?" This creates tensions around:

- **Security**: What does a personal agent do on the enterprise network?
- **IP ownership**: If an agent learns at work for years, does the enterprise own it?
- **Portability**: Leaving a job means leaving agent context behind — already "starting to feel frightening"

### 2-3K Token System Prompts Beat 40K Stuffed Ones

Tom is a strong advocate for minimal system prompts:

> "Certain harnesses, right out of the gate, you'll have 25 or 40,000 tokens as part of the system prompt. And there, you really have a hard time getting the tokens per second to a place where it feels interactive."

He praised Pi's system prompt at ~3,000 tokens — "you can literally strip almost to the bone and it'll still work." He noted you can even build robust agents without a system prompt at all if you have good tool definitions and names.

### Pi's Four-Tool Philosophy

Tom uses **Pi** as his primary agent harness. Its philosophy:

- **Four tools only**: Read, Write, Edit, Bash
- **Minimal tool surface** maximizes reliability — fewer tools mean fewer tool-calling errors
- **Self-extending**: If the agent needs a tool, it "celebrates the idea of creating it in code itself" — it writes its own tools and hot reloads them in the same session
- **Passive session saving**: All sessions are saved, enabling ripgrep-style search across past conversations to resume work

### Parallelization Is the Real Superpower

Tom's opening thesis:

> "The great power of agents is parallelization. In order to take advantage of that, you really have to think differently about how do you equip parallel processes with enough context and enough planning in the workflows that they actually save you time."

He drew an analogy to the Amish: "They have coordination down. The technology is arguable, but they've got being able to coordinate distributed efforts down without a doubt." The Amish barn-raising approach — dozens of people in parallel with clear coordination — is the model for effective multi-agent systems.

### Memory: The Key Unsolved Problem

Tom identified memory as his biggest frustration. Agents "demonstrate such a level of intelligence and then they forget." The challenge is multi-layered:

- **Agent memory**: What does the agent remember across sessions?
- **Human memory**: "I've forgotten which tab, like what is this agent doing and what is that agent doing?"
- **Boundary problem**: What goes in plugins vs. skills vs. QMD? "They don't have clean demarcated lines."
- **Granularity**: Different levels of memory granularity are "obvious to a person" but not to an agent

He speculated whether future models might encode memories in a different memory space that is "unique and better for information retrieval for these systems."

## Core Ideas

### Local-First Agent Philosophy

Tunguz's local-first approach is pragmatic, not ideological. The decision tree:

1. **Default to local** (Qwen 35B via Ollama) for single-file coding, tool calling, daily workflows
2. **Fall back to cloud** for multi-file coding, re-architecture, and creative writing (Kimi K26)
3. **Run multiple models in parallel** when inference servers support it
4. **Use small models for latency-sensitive tasks** (Gemma 4B at 300ms for ASR post-processing)

### Minimal Tool Surface

The four-tool philosophy (Read, Write, Edit, Bash) maximizes reliability by minimizing the attack surface for tool-calling errors. When more capability is needed, the agent writes it — creating a virtuous cycle of self-extension.

### Supply Chain Awareness

Tunguz is one of the few practitioners publicly discussing the supply chain implications of agent workflows. The 14-day npm rule is a practical heuristic for a larger problem: agents autonomously installing packages, pulling dependencies, and executing code create new attack surfaces that existing security models don't address.

### The Amish Approach to Technology Adoption

Tunguz's recurring analogy: adopt technology deliberately, not reflexively. The Amish don't reject technology — they evaluate each innovation for its impact on community coordination. Similarly, AI teams should evaluate each agent capability for its impact on workflow coherence, not adopt every new tool by default.

## Key Work

### Theory Ventures (2023–present)
General Partner at an early-stage VC fund investing $1-25M in software companies leveraging technology discontinuities. Portfolio includes data infrastructure companies and AI-native startups.

### Blog at tomtunguz.com
One of the most widely-read VC/tech blogs, driving millions of monthly pageviews. Covers AI strategy, startup metrics, go-to-market dynamics, and technology adoption patterns.

### Google AdSense (pre-VC)
Product manager managing a billion-dollar business unit. Built product intuition for go-to-market mechanics at scale.

## Related Concepts

- [[concepts/local-models]] — Tom's local-first agent philosophy and Qwen 35B workflow
- [[concepts/ai-safety]] — Supply chain paranoia, 14-day npm rule, and BYOD agent security
- [[entities/bryan-bischof]] — Fellow Episode 2 guest and Theory Ventures colleague; Tom's BBplot eval demo was run during Tom's own segment

## Related People

- **[[entities/bryan-bischof]]** — Head of AI at Theory Ventures; collaborator on agent workflow philosophy and the "package context with content" thesis
- **[[entities/hilary-mason]]** — Fellow Episode 2 guest
- **[[entities/eric-ma]]** — Fellow Episode 2 guest
- **Zach (Pi creator)** — Created the Pi harness with its minimalist system prompt and four-tool philosophy
- **Ivan Leo** — Formerly at Manas, now at DeepMind; collaborated with Tom on a workshop building a minimal version of Pi in Python
