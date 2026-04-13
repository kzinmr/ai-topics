---
title: "Ryan Lopopolo"
handle: "@_lopopolo"
created: 2026-04-13
updated: 2026-04-13
tags: [person, x-account, ai, harness-engineering, openai, codex, ai-agents, agentic-engineering, elixir, symphony]
aliases: ["ryan lopopolo harness engineering", "lopopolo", "openai frontier symphony", "harness engineering"]
depth: 16000
---

# Ryan Lopopolo

| | |
|---|---|
| **X/Twitter** | [@_lopopolo](https://x.com/_lopopolo) |
| **Blog** | [hyperbo.la](https://hyperbo.la) |
| **GitHub** | [lopopolo](https://github.com/lopopolo) |
| **Role** | Member of Technical Staff, OpenAI Frontier; creator of Artichoke Ruby |
| **Known for** | Coining "Harness Engineering"; leading OpenAI's 1M LOC, 0% human code experiment |
| **Bio** | Staff+ engineer specializing in systems for AI agent autonomy. Led the Frontier experiment that built and shipped an internal beta product with ~1 million lines of agent-generated code, zero human-written code, and zero human pre-merge review. Previously at Stripe, Brex, Citadel, Snowflake. Creator of Symphony, an internal Elixir-based multi-agent orchestration layer. |

## Overview

Ryan Lopopolo is the originator of **Harness Engineering** — the systematic practice of building the scaffolding, feedback loops, observability, and architectural constraints that allow AI coding agents to operate autonomously at scale. His work at OpenAI's Frontier team represents the most extreme public demonstration of agentic engineering to date:

> "Over five months, OpenAI engineers built and shipped an internal beta product with **zero lines of manually-written code**. The product has internal daily users and external alpha testers, contains approximately **one million lines of code** across application logic, infrastructure, tooling, and documentation, and was built in roughly **1/10th the time** of manual coding."

Previously, Ryan held engineering roles at Stripe, Brex, Citadel, and Snowflake, and created **Artichoke** — a Ruby implementation in Rust. His blog at [hyperbo.la](https://hyperbo.la) publishes his latest thinking on agent utilization, software architecture, and the economics of AI-native development.

## Core Ideas

### Harness Engineering — The System, Not the Prompt

Ryan's defining contribution is the distinction between *prompting* and *harness engineering*:

> "Prompting is asking an LLM to write code. Harness engineering is building the systems, feedback loops, and constraints that let agents operate autonomously at scale."

Key principles:

1. **Constraint-Driven Development** — Ryan deliberately refused to write any code himself in the Frontier experiment, forcing the team to build complete end-to-end agent capability. "If we're deploying agents into enterprises, they should be able to do all the things I do."

2. **Systems Over Prompting** — When agents fail, don't just prompt harder. Ask: "What capability, context, or structure is missing?"

3. **Fast Build Loops** — Enforced <1 minute inner loop. Progressively swapped build systems (Makefile → Bazel → Turborepo → Nx) to maintain speed. Background shells in newer models required retooling to avoid blocking.

4. **Human Bottleneck Shift** — Humans moved from code review to building systems, observability, and context. Post-merge review is now statistical sampling/auditing.

5. **Code is Disposable** — Worktrees and merge conflicts matter less when agents resolve them autonomously. "I almost don't care that there are merge conflicts."

### Symphony — Multi-Agent Orchestration Layer

Ryan built **Symphony**, an internal Elixir-based orchestration system for managing AI coding agents:

**Why Elixir/BEAM?** Native process supervision (gen_server), fault tolerance, and massive concurrency map perfectly to task-driven agent daemons.

**How Symphony Works:**
1. Spins up isolated git worktrees per ticket
2. Coordinates parallel coding agents (Codex instances)
3. Handles CI, flaky tests, and merge queues
4. **Rework State:** If PR fails review, Symphony trashes the entire worktree and restarts from scratch. Humans only intervene to fix systemic context gaps.

### The $land Skill — Autonomous PR Lifecycle

Full delegation via a custom `$land` skill:

```bash
$land → push PR → wait for human/agent review → wait for CI → fix flakes → merge upstream → resolve conflicts → merge to main
```

- **Review Agents** bias toward merging. Only flag issues >P2 (P0 = "mute the codebase if you merge this")
- **Author Agents** can defer or push back on scope-creeping review comments
- Agents attach compressed trajectory videos (FFmpeg screen recordings) to PRs, proving work completion without human shoulder-surfing

### Agent Utilization Is the New Performance Ceiling

From his March 2026 blog post:

> "As implementation ceases to be the bottleneck, the limiting factor in software systems shifts to how effectively agents can be allowed to observe, act, and operate continuously across the entire lifecycle."

### Stop Treating Code as the Artifact

> "When agents write most of the code, review and authorship stop being the right control surfaces. Quality scales only through systems design, not individual code review."

### Context Engineering for Agent Legibility

Ryan's approach to making codebases agent-friendly:

- **AGENTS.md as Table of Contents** — Keep it to ~100 lines with pointers to deeper docs in a structured docs/ directory. Monolithic instruction files crowd out task-specific context.
- **Inverted Dev Workflow** — Spawn the agent first (Codex), then give it scripts/skills to boot the local observability stack on demand.
- **Encoding Engineering Taste** — Non-functional requirements, guardrails, and team preferences persisted in markdown:
  - `core_beliefs.md`
  - `tech_tracker.md`
  - `quality_score.md`
- **Self-Improving Loops** — Agent session logs, PR comments, and failed builds are slurped into blob storage. Daily agent loops distill learnings back into repo context.

### The Frontier Enterprise Vision

Ryan's work at OpenAI Frontier points to safe, observable, governable agent deployment at enterprise scale:

- Native IAM, security tooling, and workspace integrations
- **Safety Specs** that prevent data exfiltration and respect internal code names
- **Data Ontology/Semantic Layer** — critical for business-aware agents (aligning definitions of "revenue," "active user," etc.)

## Key Work

### OpenAI Frontier (2025–Present)
- Member of Technical Staff working on new product development for deploying agents safely at enterprise scale
- Led the 5-month experiment: 1M+ LOC, 0% human-written code, ~1,500 PRs across GPT-5.0 → 5.4 generations
- Scaled throughput from 3.5 → 5-10 PRs/engineer/day
- Built Symphony orchestration layer in Elixir/BEAM
- Token consumption: >1B tokens/day (~$2-3k/day at market rates + caching)

### Stripe
- Engineering role in payments infrastructure

### Brex
- Engineering role in fintech infrastructure

### Citadel
- Systems engineering in high-frequency trading

### Snowflake
- Data infrastructure engineering

### Artichoke Ruby (Creator)
- A Ruby implementation in Rust
- Maintained for 6 years (2020–2026), now archived
- Demonstrated deep systems programming expertise

## Blog / Key Writings

### Harness Engineering & Agent Systems (hyperbo.la)

- **[Harness Engineering the Blog Build (Again)](https://hyperbo.la/w/harness-engineering-blog-build/)** (Feb 2026) — Vite-native SSR and assets, MDX posts, typed React composition, and static output that still deploys to GitHub Pages. Demonstrates applying harness principles to blog infrastructure.

- **[What Does It Mean to Do a Good Job?](https://hyperbo.la/w/what-does-it-mean-to-do-a-good-job/)** — Ryan's deepest philosophical post on verification as the central problem of AI-assisted development. Every real task is downstream of unwritten non-functional requirements: tone, taste, risk tolerance, polish level, what counts as done. Historically these were smuggled in through shared context — hiring, onboarding, repeated exposure. But *"you do not get to run your AI through a hiring pipeline."* Because models have seen trillions of documents embodying every possible permutation of those choices, basically every task is under-specified. Concrete example from OpenAI: implementation agents and reviewer agents needed explicit rules (accept and fix, accept and defer, or push back). Without guidance, *"reviewers endlessly bully the implementer and nothing converges."* Human reviewers know to unblock while providing high-signal feedback — models don't unless you say it. Post-training optimizes for helpfulness, not task-specific expertise, creating inherent tension between instruction-following fidelity and creativity. Key insight: *"If you want the models and agents to do a good job, write down what that means, then add nuance only when the coarse instructions start to overfit."*

- **[Coding Agents for Technical Non-Engineers](https://hyperbo.la/w/coding-agents-for-technical-non-engineers/)** — Practical playbook for enabling scientists, analysts, user ops, and security researchers with coding agents. These folks are *"technical enough to have success"* — they need data-science-quality code, not production-ready. Strategy: (1) One paved lane — Python, with IT deploying `uv` everywhere; (2) Ship enterprise-managed `AGENTS.md` saying `use Python`, `use uv`, `prefer small scripts`; (3) Provide "boring batteries" by default — pandas, numpy, poppler. *"Domain experts already have the hard part. They know the data, the detection, the investigation, or the support workflow. Coding agents help them encode that work in code. Give them a paved lane and permission."* This reflects Ryan's belief that agent adoption is an organizational design problem, not just a technical one.

- **[A Lazy Prompt Turned Into a RustSec Advisory](https://hyperbo.la/w/lazy-prompt-rustsec/)** — Security hardening workflow using Codex. Pointed at his Rust crate `intaglio` with a simple prompt: *"you are red teaming this repo to look for security vulnerabilities. do a complete analysis. you must prove impact or exploitability for anything you report."* Found RUSTSEC-2026-0078 — a cross-cutting unwind-safety bug in the `intern` implementation where write ordering was wrong (pushed into backing `Vec` before inserting into `HashMap`). The key insight: *"The useful part was the bar: do a complete analysis and prove impact or exploitability."* By forbidding speculative bug reports, the model had to build a reproducer, show bad behavior, and narrow claims to what it could actually prove. *"This turns the output from security-flavored vibes into engineering work: reproducer, tests, fix, release, advisory."* Same prompt found issues in every active Artichoke crate. Agent did the full job end-to-end — identification, fix, and vuln publication.

- **[Debazeling the Blog](https://hyperbo.la/w/debazeling/)** — Ryan's journey away from over-engineered blog builds. Converted from hand-spun JS SSG to Bazel in 2022 to learn the build system (his org's focus at Brex), but the repo became 25% Starlark. *"I certainly did not do the simplest thing that could possibly work."* History of the blog: WordPress/MySQL (hacked) → Django/SQLite (rm -rf'd DB) → Django/Bootstrap (boredom) → Terraform/Packer/Ansible (high cost) → Webpack SSG (crashed on page count) → Custom JS SSG (dependency hell) → Golang+Bazel (constantly breaking rules) → Vite+Tailwind. Key lesson: modern frontend tech made the switch take hours instead of days.

- **[Winding Down Artichoke Ruby](https://hyperbo.la/w/winding-down-artichoke-ruby/)** — Reflection on 6 years of building a Ruby implementation in Rust, now archived. Not built to "fix Ruby" but as an exploratory toy/Rube Goldberg machine that became tangible after implementing `Regexp` (missing in mruby) and presenting at RubyConf 2019. Applied the Strangler Fig pattern to gradually replace mruby with native Rust ("oxidizing"). Key technical achievements: pure Rust `String` implementation fully spec-compliant on `bstr` crate (contributed back to Rust ecosystem); modular capability-oriented VM design with deliberate crate separation. Critical insight from refactoring: the Rust borrow checker forced nearly every API to take `&mut self`, making mutability boundaries explicit and demonstrating why YARV/CPython converge on GIL-shaped designs — *"aliasing and shared mutable state in an interpreter are brutally hard to model otherwise."* Wound down because modern AI coding agents now handle tasks that previously provided the "can I figure this out?" joy. *"Archiving does not feel like failure. Artichoke served its purpose for me. It pushed boundaries. It forced growth. It left artifacts that I'm proud of."* *"Build things. Even weird things. Even things that might not last forever. The act of building changes you."*

- **[Agent Utilization Is the New Performance Ceiling](https://hyperbo.la/w/agent-utilization-new-performance-ceiling/)** (Mar 2026) — As implementation ceases to be the bottleneck, the limiting factor shifts to how effectively agents can observe, act, and operate continuously across the entire lifecycle.

- **[Stop Treating Code as the Artifact](https://hyperbo.la/w/stop-treating-code-as-the-artifact/)** (Mar 2026) — When agents write most of the code, review and authorship stop being the right control surfaces. Quality scales only through systems design.

- **[Software Work Is No Longer Scheduled](https://hyperbo.la/w/software-work-is-no-longer-scheduled/)** (Mar 2026) — The production function has changed.

- **[It's Not Codex, It's Codex/GPT-5-Codex](https://hyperbo.la/w/its-not-codex-its-codex-gpt-5-codex/)** (Dec 2025) — Naming clarification for the agent model.

- **[MCP Solves Tool Discovery for LLMs](https://hyperbo.la/w/mcp-solves-tool-discovery-for-llms/)** (Aug 2025) — Coding agents fail on tools they can't see. MCP exposes a model-readable catalog—names, schemas, and prompts—so agents can discover, understand, and safely call your tools on the first try.

- **[Service Meshes Are Organization Tools, Not Technical Ones](https://hyperbo.la/w/service-meshes-are-organization-tools/)** (Aug 2025) — Service meshes are less about technology and more about enforcing org-wide defaults without slowing teams down.

- **[Ruby Enumerable: Manifest Destiny](https://hyperbo.la/w/ruby-enumerable-manifest-destiny/)** (Aug 2025) — Ruby's Enumerable mixin set the gold standard for elegant, composable iteration. With ECMAScript 2025's new Iterator type, JavaScript is finally catching up.

- **[Scaling Myself by Letting My Team Fail](https://hyperbo.la/w/scaling-myself-by-letting-my-team-fail/)** (Jul 2023) — As a Staff+ engineer, learning to delegate by allowing controlled failure.

- **[Do the Simplest Thing That Could Possibly Work](https://hyperbo.la/w/do-the-simplest-thing/)** (Aug 2023) — To build iteratively and shed complexity, start with the simplest possible solution.

### Latent Space Podcast Interview (Apr 2026)

- **"Extreme Harness Engineering for Token Billionaires"** — Comprehensive interview with swyx covering:
  - The origin of "harness engineering" and the constraint-driven experiment
  - Building Symphony with zero human-written code over 5 months
  - Why Elixir/BEAM is ideal for agent orchestration
  - The shift from code review to systems design
  - Frontier's enterprise vision for safe, observable agent deployment
  - Model capabilities and limitations (GPT-5.0 → 5.4)

### InfoQ Feature (Feb 2026)

- **"OpenAI Introduces Harness Engineering: Codex Agents Power Large-Scale Software Development"** — InfoQ's coverage of Ryan's methodology, including the 7-tier framework for agent-assisted development and the shift from implementation to environment design.

### Engineering.fyi Article (Mar 2026)

- **"Harness engineering: leveraging Codex in an agent-first world"** — Comprehensive article detailing how to structure a repository and documentation system optimized for AI agent legibility using progressive disclosure patterns.

## X Activity Themes

- **Harness Engineering principles** — Systems thinking for agent autonomy
- **Agent utilization patterns** — Observability, feedback loops, performance ceilings
- **Symphony orchestration** — Multi-agent coordination, Elixir/BEAM architecture
- **Frontier enterprise vision** — Safe deployment, governance, data ontology
- **Developer tooling** — MCP, tool discovery, agent legibility
- **Open source contributions** — Artichoke Ruby, Rust systems programming
- **Conference talks** — AI Engineer Summit keynotes, podcast appearances

## Key Quotes

> "Prompting is asking an LLM to write code. Harness engineering is building the systems, feedback loops, and constraints that let agents operate autonomously at scale."

> "As implementation ceases to be the bottleneck, the limiting factor in software systems shifts to how effectively agents can be allowed to observe, act, and operate continuously across the entire lifecycle."

> "When agents write most of the code, review and authorship stop being the right control surfaces. Quality scales only through systems design, not individual code review."

> "If we're deploying agents into enterprises, they should be able to do all the things I do."

> "I almost don't care that there are merge conflicts."

## Related People

- **[[karpathy]]** — Shared interest in AI-assisted development; Ryan's work represents the enterprise-scale realization of Karpathy's vision
- **[[simon-willison]]** — Overlapping focus on agentic engineering patterns and practical AI workflows
- **[[jason-liu]]** — Complementary perspectives: Jason on structured outputs, Ryan on agent orchestration
- **[[boris-cherny]]** — Both work on agent workflow optimization at scale; Ryan's enterprise focus vs. Boris's CLI focus

## Sources

- [Latent Space: Extreme Harness Engineering for Token Billionaires](https://www.latent.space/p/harness-eng) — Comprehensive interview transcript
- [InfoQ: OpenAI Introduces Harness Engineering](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/) — News coverage
- [Engineering.fyi: Harness Engineering Article](https://www.engineering.fyi/article/harness-engineering-leveraging-codex-in-an-agent-first-world) — Technical deep-dive
- [hyperbo.la](https://hyperbo.la/w/) — Ryan's blog with latest thinking
- [GitHub: lopopolo](https://github.com/lopopolo) — Open source contributions
