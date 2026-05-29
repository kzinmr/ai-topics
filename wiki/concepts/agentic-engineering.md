---
title: "Agentic Engineering"
created: 2026-05-14
updated: 2026-05-29
type: concept
tags:
  - concept
  - agentic-engineering
  - ai-agents
  - agent-skills
  - verification
  - coding-agents
  - developer-tooling
sources:
  - raw/articles/2026-05-12_hugobowne_agentic-engineering-verification.md
  - raw/articles/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - raw/articles/2026-05-25_nolanlawson_using-ai-to-write-better-code-slowly.md
  - raw/articles/2026-05-15_vanishing-gradients_show-us-your-agent-skills-ep2.md
  - raw/articles/2026-05-21_vanishing-gradients_show-us-your-agent-skills-ep3.md
  - raw/articles/2026-05-29_vanishing-gradients_show-us-your-agent-skills-ep4.md
---

# Agentic Engineering

**Agentic engineering** is the disciplined practice of building software using AI agents as primary contributors, with verification — not manual code reading or writing — as the critical skill. It represents the evolution from "vibe coding" (ad-hoc, unverified agent output) to systematic, quality-assured agent-driven development.

## Definition

Agentic engineering treats AI agents as software factory workers that generate, review, test, and verify code continuously. The human engineer's role shifts from **writing code** to **designing verification systems** and **orchestrating agent workflows**.

As [[entities/wes-mckinney]] describes it:

> "I almost don't read code now... Roborev reads every line of code that is generated. It gets read multiple times. And so, whenever I push up a pull request, the branch gets re-reviewed. By the time I'm merging a pull request into a repository, the code has all been read by agents four or five times minimum."

## Core Principles

### 1. Verification over Reading

The central shift: stop reading code manually and start building agentic verification pipelines. This includes:

- **Background code reviewers** (e.g., [[entities/roborev]] — a GPT-5.5 daemon that reviews every commit)
- **Generator-evaluator workflows** — one agent generates, another evaluates
- **Verifier skills** — embedding domain-specific quality rules (e.g., Tufte's data viz principles) as LLM-evaluable checks

### 2. Skills as Thin Drivers

Skills are minimal wrappers that call tools, not fat abstractions. Key design patterns:

- **Progressive disclosure** — reveal complexity only when needed
- **Explain skill as anchor** — a meta-skill that sets tone and expectations
- **Reflect and improve** — skills that self-evaluate and iterate

### 3. Software Factories, Not Solo Coding

[[entities/wes-mckinney]]'s setup: parallel agents running RoboRev (reviewer), Agents View (session DB), Middleman (dashboard), Kata — generating 1M+ lines in 6 months for spicytakes.org.

### 4. Context Engineering as "Second Brain"

[[entities/jeremiah-lowin]]'s approach: voice memos → transcribed → fed into agent memory substrate each morning. The "memory substrate" is what makes agents consistently useful across sessions.

### 5. Ephemeral "Just-for-Me" Software

Agents make throwaway tools viable — tools built for a single task, used once, and discarded. This was previously economically infeasible.

### 6. Slow Coding: Quality Over Velocity

Articulated by [[entities/nolan-lawson]] in May 2026, **slow coding** is a deliberate counterpoint to "vibe coding" and AI-generated "slop." Instead of using AI to generate code fast, slow coding uses AI to **find bugs** and **verify correctness** — systematically improving quality rather than velocity.

Core practices:

- **Multi-agent parallel review** — Run 3+ bug-finding agents (Claude sub-agent, Codex, Cursor Bugbot) on every PR, cross-check results for near-zero false positives
- **Context clearing** — Wait for all sub-agents to finish before independent review, preventing anchoring bias
- **Triage-driven cycles** — Fix all criticals/highs first, re-run agents, repeat until clean; abandon PRs with fundamental flaws
- **Side-quest acceptance** — Tangential bug discoveries (pre-existing issues, missing tests) are embraced as codebase health improvements, not productivity losses

> "I haven't necessarily seen my velocity go up. … I end up on a tangential side-quest where I'm writing unit tests and fixing subtle flaws that pre-date the PR." — Nolan Lawson

Slow coding represents the opposite of 10× productivity, but catches wrongheaded approaches early and makes codebases better for the next developer.

### 7. Agentic Data Science: The Two-Bucket Framework

[[entities/eric-ma]] articulated a framework for agent-assisted data science at Moderna:

- **Bucket 1 — Loading Context**: Feeding the agent domain knowledge, molecule structures, experimental data, and notebook state. The agent needs to understand the scientific domain before it can contribute.
- **Bucket 2 — Auto-Optimize**: The agent iteratively improves analysis — generating visualizations, testing hypotheses, refining models. The human stays at the boundary deciding when to switch buckets.

Key architectural insight: **reactive notebooks (marimo) over Jupyter**. Reactive notebooks are deterministic DAGs, so the agent always knows what's computed. Agents can read/write Python variables directly without fragile kernel state management. Eric's `agents.md` enforces rules like cell naming conventions, color map standards, and "if you make a claim, you need a plot."

### 8. One Intelligent Step in Deterministic Scripts

[[entities/eleanor-berger]] identified the winning pattern for reliable agent workflows:

> "One LLM-powered step wrapped inside otherwise deterministic scripts."

Rather than giving agents open-ended autonomy, embed a single intelligent decision inside a procedural pipeline. Know when a cron job needs an LLM and when a plain script will do. This hybrid approach maximizes reliability while still leveraging agent intelligence where it matters.

Eleanor's Hermes agent "Fnord" on a home Mac Mini exemplifies this: ~157 skills, GPT-5.5 as unlock, auto-publishing HTML, and a "lethal trifecta" security model that cuts internet access to prevent hallucinated URLs, scraping attacks, and data exfiltration.

### 9. Cloud-Background Agent Execution

[[entities/nico-gerold]] declared "Coding agents are dead" — meaning the interactive, IDE-integrated model is obsolete. AMP rebuilt its harness for agents that:

- Run in the **cloud**, not on the developer's machine
- Execute in the **background**, with humans reviewing outputs asynchronously
- Use **skills as capabilities** (e.g., gcloud skill pulls logs, tmux skill spins up dev builds)
- Include a **postmortem skill** — agent introspects on why it went wrong

This mirrors the Amish barn-raising analogy from [[entities/tomasz-tunguz]]: adopt technology deliberately, not reflexively. The real superpower is **parallelization** — multiple agents doing independent work simultaneously.

### 10. Eval-Driven Feature Development

[[entities/bryan-bischof]] demonstrated BBplot, a visualization library built for agents. His methodology:

- **Features come from eval failures, not human wishlists** — the eval defines what's needed
- **Separate eval repo** — prevents agents from "cheating" by seeing test cases
- **Gallery requirement** — every feature must be demonstrated in the gallery for agents to learn from
- **Three variations always** — single-pass generation locks into one interpretation; ambiguity yields variance
- **Scene graph** — tells the agent what overlaps what, enabling layout-aware generation

### 11. Skills Ecosystem Skepticism

[[entities/hamel-husain]] brought radical skepticism to the skills movement:

- **A third of the top 300 skills have exactly one commit** — most are abandonware
- **Skills are just decompressed prompts** — no magic, just structured context
- **The skills security nightmare**: hidden HTML in `.md` skill files can inject instructions
- **MCP over skill files for eval** — structured, testable interfaces beat ad-hoc skill documents
- **"Fuck your skills"** — be skeptical even of published, popular skills

## Contrast with Vibe Coding

| Dimension | Vibe Coding | Agentic Engineering |
|-----------|-------------|---------------------|
| Code reading | Human reads everything | Agents read everything (4-5x) |
| Verification | Manual, spot-checked | Systematic, agentic, continuous |
| Code writing | Human still writes | Agents generate, humans architect |
| Quality | Variable, ad-hoc | Built into workflow via verifier skills |
| Scale | One person, one agent | Software factory with parallel agents |
| Memory | Ephemeral chat context | Persistent memory substrate |

## Key Practitioners

- **[[entities/wes-mckinney]]** — Software factory with RoboRev, Agents View, Middleman. 1M+ lines generated.
- **[[entities/jeremiah-lowin]]** — Second brain architecture, voice memo pipeline, explain skill anchor
- **[[entities/randy-olson]]** — Tufte-encoding verifier skills, digital twin thought partner, generator-evaluator workflows
- **[[entities/garry-tan]]** — "Fat Skills, Fat Code, Thin Harness" architecture
- **[[entities/hugo-bowne-anderson]]** — Documenting and teaching agentic engineering through Vanishing Gradients
- **[[entities/nolan-lawson]]** — Slow coding methodology, multi-agent parallel code review pipeline, quality-over-velocity philosophy
- **[[entities/eric-ma]]** — Agentic data science two-bucket framework, marimo Pair, reactive notebooks for agents
- **[[entities/eleanor-berger]]** — One intelligent step pattern, Hermes Fnord agent, lethal trifecta security model
- **[[entities/nico-gerold]]** — Cloud-background agent execution, skills as capabilities, postmortem introspection
- **[[entities/bryan-bischof]]** — BBplot eval-driven development, scene graph, three-variations pattern
- **[[entities/hamel-husain]]** — Skills ecosystem skepticism, MCP over skill files, skills security audit
- **[[entities/matthew-honnibal]]** — Multi-pass agent architecture, effective context window findings, reward hacking detection

## Key Tools and Projects

- [[entities/roborev]] — Background code reviewer daemon (GPT-5.5)
- [[entities/superpowers]] — Skills framework (Jesse Vincent)
- [[entities/fastmcp]] — MCP tooling framework
- [[entities/prefab]] — Generative UI DSL in Python
- [[entities/opencode]] — Agent harness with deep memory customization
- [[entities/openclaw]] — Agent harness for memory management

## Related Concepts

- [[concepts/agent-skills]] — Reusable patterns for coding agents
- [[concepts/code-review-agents]] — Background verification daemons
- [[concepts/context-engineering]] — Building agent memory substrates
- [[concepts/harness-engineering]] — Building thin agent harnesses
- [[concepts/generator-evaluator-workflow]] — Generator-evaluator architecture
