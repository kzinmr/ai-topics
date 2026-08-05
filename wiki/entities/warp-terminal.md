---
title: Warp Terminal
created: 2026-05-01
updated: 2026-08-05
type: entity
tags: [product, tool, coding-agents, open-source, platform]
sources:
  - raw/articles/2026-05-27_openai_warp-open-source-gpt-5-5.md
  - https://www.warp.dev/blog/warp-is-now-open-source
  - https://open.substack.com/pub/bensbites/p/building-gets-easier
  - raw/articles/2026-05-20_warp_multi-harness-cloud-agent-orchestration.md
  - raw/articles/2026-05-23_warp_bring-your-own-inference-to-warp.md
  - raw/articles/2026-06-23_warp-dev_self-improvement-loop-for-skills.md
  - raw/articles/2026-06-26_warp_we-are-now-factory-engineers-not-product-engineers.md
  - raw/articles/2026-07-17_warp_how-to-build-a-cloud-software-factory-self-improving-code-review.md
  - raw/articles/2026-08-04_warp_how-to-build-a-cloud-software-factory-computer-use-verification.md
  - raw/articles/2026-08-05_warp_introducing-the-warp-agent-cli-coding-agent.md
---

# Warp Terminal

**Warp** is an AI-native terminal and **Agentic Development Environment (ADE)** used by nearly a million developers. Built in Rust, it combines a modern terminal UX with integrated AI agents. In April 2026, Warp open-sourced its client under AGPLv3 with OpenAI as the founding sponsor.

## Key Facts

| Field | Detail |
|-------|--------|
| **Tech Blog** | [warp.dev/blog](https://www.warp.dev/blog) |
| **Founded** | 2020 (New York, NY) |
| **CEO & Co-Founder** | Zach Lloyd (former Principal Engineer at Google, Google Sheets/Docs) |
| **Total Raised** | ~$73M across 3 rounds |
| **Funding Rounds** | Seed: $6M (2020) • Series A: $17M (Apr 2022, led by Dylan Field) • Series B: $50M (Jun 2023, led by Sequoia) |
| **Notable Investors** | Sequoia, GV, BoxGroup, Neo, Sam Altman, Jeff Weiner, Marc Benioff, Elad Gil |
| **Estimated Valuation** | $200–300M (Dealroom) |
| **Employees** | ~44 (2026) |
| **License** | AGPLv3 (core), MIT (UI framework) — open-sourced April 2026 |
| **Founding Sponsor** | [[entities/openai]] |

### Paraform Context

Warp operates in the hypercompetitive developer tools space, vying for senior engineering talent in New York and San Francisco against well-funded peers. The company's lean team (~44 employees serving nearly 1M developers) reflects an engineering-heavy headcount typical of companies recruiting through platforms like [[entities/paraform]]. Warp's open-source pivot and "agent-first" contribution model also create demand for niche roles — DevRel, Rust systems engineers, and AI/agent infrastructure engineers — which are the kind of hard-to-fill positions that Paraform's recruiter marketplace specializes in. With OpenAI as founding sponsor, Warp also competes for talent against [[entities/openai]], [[entities/cursor-3]], and [[entities/anthropic]].

## GPT-5.5 Efficiency & Growth (May 2026)

In a May 2026 OpenAI customer story, Warp detailed its partnership with OpenAI and GPT-5.5-powered agent workflows:

**Key Metrics**:
- **Nearly 1 million developers** use Warp; **56% of the Fortune 500** are customers
- **90% of Warp's internal pull requests** are now co-created by agents
- **ARR grew 35×** in the last year; **enterprise revenue up >500%** since Q4 2025
- **GPT-5.5** uses **30% fewer tokens** per agentic coding task compared to GPT-5.4 in internal benchmarks

**Open Agentic Development Model**: Warp's thesis is that development will shift from individual assistants to coordinating persistent, parallelized agents:
- Agents write the code; developers **specify intent, verify outputs, and decide what ships**
- Decisions become **reusable context** for future agents, improving the system over time
- With sufficient orchestration, agents can produce **more consistent code than a loosely coordinated group of humans**
- Open source transforms from individual contribution to **collective product judgment and shared vision**

**Model Usage Strategy**:
- GPT-5.5 is used for **complex, long-horizon agentic coding tasks** requiring reasoning across large problem spaces
- OpenAI models are used as **LLM-as-a-judge** in evaluation pipelines
- Warp routes tasks by difficulty, sending the toughest work to GPT-5.5

### Zach Lloyd Quotes

> *"We think we can ship a better Warp, more quickly, by working with our community to supervise a fleet of agents. OpenAI models help make that sustainable for the long-horizon coding work these systems require."*

> *"We've found that OpenAI models regularly provide frontier-level intelligence while taking fewer tokens and turns to complete the same tasks. The models are especially strong for coding tasks that require reasoning across large problem spaces."*

> *"No one knows exactly what the future of agentic development will look like. We think the community ought to be able to participate in shaping it."*


## Products

### Warp Terminal

The core terminal client with:
- **Terminal and Agent modes**: Switch between clean command-line and dedicated agent conversation view
- **Modern UX**: Block-based navigation, multi-line editing, syntax highlighting, rich completions
- **Code editor**: File tree, LSP support, interactive code review
- **Third-party CLI agents**: Run Claude Code, Codex, OpenCode with Warp's agent toolbelt

### Oz

**Oz** is Warp's cloud agent orchestration platform, powering the agent-first contribution model for the open-source repository. It provides:
- Skills and verification loops baked in for Warp development
- Multi-agent orchestration for code review, testing, and deployment
- Rules and context management for consistent agent behavior


### Oz Upgrade (May 2026)

On May 19, 2026, Warp launched major upgrades to Oz, making it the first truly **multi-harness control plane** for cloud agents. Key capabilities:

| Feature | Description |
|---------|-------------|
| **Multi-harness orchestration** | Launch, track, and control Claude Code, Codex, and Warp Agent in a single unified control plane. Oz sits a level above, enabling cross-harness comparison and task-to-harness matching. |
| **Automatic multi-agent orchestration** | Deploy and track multiple parallel subagents (across harnesses) for long-horizon tasks: large feature builds, code migrations, production deployments. Includes auto-tracking and progress dashboard. |
| **Cross-harness Agent Memory** | An index over organizational knowledge that Oz pulls into context for any agent task. Supports pluggable data sources (files/skills, MCPs, databases, enterprise apps) and is writable — Oz auto-adds to knowledge as it completes tasks. Agents learn team coding style, deployment topology, data structure across sessions and harnesses. In research preview. |
| **Kubernetes self-hosting** | Run agents in Kubernetes pods or via direct execution, with or without Docker. No development setup changes required. |
| **Granular cost controls** | Per-team billing, individual credit caps, visibility into team usage and outcomes. |
| **Least-privilege permissions** | Individual agents get granular permissions to internal services — production agents have different access than CRM agents. |
| **API/SDK-first** | Extended API with return values from agent sessions (artifacts, raw conversations); session handoff across local/remote/cloud environments. |

This positions Oz as a **harness-agnostic orchestration layer** — the company's philosophy is that teams shouldn't bet their future on a single model or harness.
## Open Source (April 2026)

On April 28, 2026, Warp open-sourced its client at [github.com/warpdotdev/warp](https://github.com/warpdotdev/warp):

- **License**: AGPLv3 for core, MIT for UI framework (warpui_core, warpui crates)
- **Founding sponsor**: OpenAI
- **Agent workflows**: Powered by GPT models (GPT-5.5)
- **Contribution model**: Agent-first — agents handle implementation; humans focus on speccing, direction, and verification

> "Open source has long been central to how developers learn, build, and push the field forward. We're excited to support experiments that explore how AI can help maintainers and contributors collaborate more effectively at scale." — Thibault Sottiaux, Engineering Lead, OpenAI

## Agent-First Contribution Model

Warp's open-source process inverts traditional contribution:
- GitHub issues are the source of truth for feature tracking
- Oz agents handle implementation (coding, planning, testing)
- Human contributors focus on ideas, direction, and verifying agent output
- Public roadmap and technical discussions happen in the open

This model exemplifies the [[concepts/agentic-engineering]] thesis: humans provide taste and direction, agents handle implementation.

## Self-Improvement Loop for Skills (June 2026)

Warp published a detailed technical blog post describing its **self-improvement loop for skills** — a system where agent skills (reusable YAML-defined procedures) automatically improve through execution feedback without human manual editing.

### Core Concept

A **skill** in Warp is a YAML-defined reusable procedure containing steps, context requirements, decision points, and guardrails. Unlike prompt templates, skills are executable units that the agent loads and follows, separating *what to do* (agent reasoning) from *how to do it* (skill definition).

### The Loop

```
Execute → Evaluate → Revise → Execute
```

1. **Execute**: Agent runs a task using a skill
2. **Evaluate**: System automatically assesses three signals — did it complete successfully, did output match expected format, did the agent need to intervene/retry
3. **Revise**: When signals indicate problems, Warp updates the skill's YAML definition (steps, context, error handling) — **not** model weights or fine-tuning
4. **Repeat**: Each iteration makes the skill more robust

### Why It Works at Scale

- **Context load reduction**: A skill that took 50 lines of reasoning compresses to a 10-line YAML definition
- **Failure localization**: Failures are isolated to the specific skill; no cascade into broader context
- **Compounding feedback**: Unlike static documentation that degrades, skills stay current via continuous execution data

### Comparison with Other Approaches

Warp's approach differs from both Hermes Agent and OpenClaw:

| Dimension | Warp | Hermes Agent | OpenClaw |
|-----------|------|-------------|----------|
| **Improvement trigger** | Automatic post-execution evaluation | Agent self-authoring via prompt nudges | Manual/user-governed |
| **Skill format** | YAML (steps, context, decision points) | SKILL.md (markdown with frontmatter) | Skills + primitives |
| **Human role** | Reviewer of proposed changes | Passive (agent decides) | Active governor |
| **Scope** | Per-skill YAML revision | New skill creation + patching | Governance-first, bounded growth |

This positions Warp between Hermes (fully autonomous self-authoring) and OpenClaw (fully governed) — the agent proposes improvements, but a human approves or rejects them.

### Developer Role Shift

The loop shifts the developer's role from **instruction author** to **skill reviewer**: write minimal skill definitions upfront, let execution fill in gaps, review proposed changes as they accumulate.

### Factory Engineering Shift (June 2026)

In a June 18, 2026 internal memo, Warp CEO Zach Lloyd declared a fundamental shift in how the company approaches software development: **"We are now factory engineers, not product engineers."** The memo outlines a transition from product engineering to building a cloud software factory.

**Core Principles**:

- **Factory efficiency** = shipped product / (inference cost + human time cost). Success is measured by the percentage of changes shipped automatically and at what cost — NOT by features shipped.
- Companies will eventually treat software production as **COGS (variable cost)**, not an R&D expense.
- **Automation mandate**: every engineer must approach everything automation-first; using interactive agents is framed as a failure to learn from.

**The Factory Workflow**:

```
Triage agent → Spec agent → Implementation agent → Code review agent → Verification agent → CI/CD → Ship → Monitor agent
```

- **Oz** records human interventions, and self-improvement agents learn from them.
- The primary job of engineers is to **ensure the factory workflow runs smoothly**; Oz provides the best experience for this.
- The ultimate goal is **recursive self-improvement** — the golden path where the factory optimizes itself.

**Industry Context**:

- The era of unlimited token budgets for interactive agents is ending.
- The future is **ROI-driven automation** — token spend must justify itself in terms of factory efficiency.

This shift embodies [[concepts/agentic-engineering]] applied at the organizational level, treating the entire engineering org as an [[concepts/agent-team-swarm]] with Oz as the orchestration layer. The factory model also relates to [[concepts/harness-engineering]], where Oz provides the multi-harness control plane for this automated pipeline.

### Self-Improving Code Review (July 2026)

The third post in Warp's software factory series detailed a **self-improving code review agent** — an outer-loop agent that observes the code reviewer and improves its review capabilities over time.

**How it works**:

- **Outer-loop observation**: The agent monitors code review outputs — accepted/rejected changes, human feedback, post-merge defects — and analyzes where the reviewer fell short.
- **Skill format**: Unlike Warp's YAML-based skills, the code review skill uses **text instructions + deterministic Python scripts** (not on-the-fly generation). This makes review behavior auditable and testable — not a black-box LLM prompt.
- **Spec comparison & validation**: The agent compares code against specifications, validates suggestions before they reach the recommendation stage, and runs builds to verify changes before recommending.
- **Multi-model/multi-harness cost management**: Cheap models handle routine linting and style checks; expensive models are reserved for complex semantic analysis and architectural review. The outer-loop tracks cost-per-review and optimizes routing over time.
- **CI/CD integration**: The review pipeline runs as a **GitHub Action** producing structured `review.json` output for programmatic consumption by downstream tools and Oz's orchestration layer.

This is an example of [[concepts/agentic-engineering]] at the meta-level — an agent that improves other agents. The approach contrasts with [[entities/claude-code]]'s more conversational review style.

### Computer Use Verification (August 2026)

The fourth post in Warp's software factory series (August 3, 2026) added **computer use and browser use verification** to the factory flow — a capability provided to other agents rather than a standalone agent. Computer/browser use lets agents control a running application directly with mouse clicks and keyboard presses; Warp argues it is valuable at three points in the factory pipeline:

- **Triage phase**: reproduce bugs before attempting fixes
- **Implementation**: verify fixes and confirm new features match specs
- **Review**: prove to a human reviewer that code matches expected behavior

**The `verify-behavior` skill** defines how agents use computer and browser use:

- **Mode selection**: computer use for desktop and mobile-native apps; browser use for webapps
- **Capture**: video preferred, screenshots acceptable
- **Two modes**: `reproduce` (confirm a reported bug occurs) and `verify` (confirm a new behavior)
- **Install**: `npx skills add warpdotdev-demos/cloud-factory-demo --skill oz-cloud-factory-demo`

**Key design points**:

- **Spec-driven debug loop**: with a detailed `PRODUCT.md` spec, the agent runs computer use at every implementation pass to measure how close the implementation is to spec, iterating until it converges. Cost monitoring is required — this loop is expensive but increases success likelihood.
- **Video as review evidence**: seeing a video of a feature working reduces code review burden; for low-risk pure UI changes, watching the video may be sufficient without reading the code.
- **Cloud subagent fan-out**: for complex/new behaviors, the orchestrator fans out to verify all user stories independently in parallel. Computer use is single-threaded, so fanning out cloud agents across machines improves throughput. Local computer use is a worse experience (steals focus); cloud machines avoid agents acting on the user's local apps.
- **Skill integration**: the existing Triage, Review, and Implementation skills are updated to invoke `verify-behavior` when it helps.

**Demo**: Using a Nano Banana agentic image editor demo repo, Warp showed (1) reproducing a bug where image previews render at thumbnail size instead of gallery size, with the agent auto-generating screenshots of the broken behavior, and (2) implementing a "clear"/"replace" UI feature end-to-end with acceptance criteria checked by the verifier and a video proving the controls work.

The series' next post previews **monitoring agents** that observe features/fixes after release and feed back into the Triage phase, completing the factory loop.

### Warp Agent CLI (August 2026)

On August 4, 2026, Warp launched the **Warp Agent CLI**, a standalone CLI version of the Warp Agent usable in any terminal — Ghostty, iTerm 2, VS Code, and the built-in Windows and Mac Terminals. It is a multi-model, cost-optimizing harness built on Warp's terminal infrastructure, positioned as a "built-in mux'er across agent sessions" to fix the shell-integration gaps of other agentic CLIs.

**Mux PTY architecture**: Within an agent session, Warp runs and manages pty connections with a layer of indirection between the agent and the underlying shell (tmux-like architecture). Because the mux is managed by Warp's terminal infrastructure, the agent is natively aware of terminal inputs/outputs (Warp's "blocks"), enabling:

- **Persistent sessions and remote agents** — switch directories mid-session; run agents on remote machines over ssh without installing remote binaries; the agent session persists even as the base "state" changes (useful for multi-repo projects and cloud machines with limited install permissions)
- **Agent-driven full-screen/interactive apps** — drive sqlite, python REPLs, gdb, htop, and vim through the agent session (e.g., generate SQL queries inside a REPL and interactively debug, set gdb breakpoints, or ask the agent to quit vim)
- **Seamless terminal input** — `!` for shell commands plus a natural-language classifier that auto-distinguishes shell commands from agent prompts; includes Warp Terminal's tab-completion menu for arguments and flags

**Model routing**: built-in auto-routing based on task complexity, with frontier and US-hosted open-weight models out of the box; first-class support for custom model routers where users define which models handle which tasks.

**Multi-agent orchestration & cloud handoff**: the CLI supports orchestration agents delegating to subagents (arrow-key switching between subagent and orchestrator sessions), running cloud agents, and — unique to Warp — delegating across entirely different harnesses like Claude Code and Codex via the cloud platform. Work started in the CLI can be handed off to cloud agents, tracked centrally and steered via the web.

**Pricing**: Warp subscription from $18/month ($20 of inference included); ad hoc credits from $10 without a subscription; or bring-your-own API key / OpenAI-compatible endpoint / SuperGrok login.

The CLI release extends the [[concepts/agentic-engineering]] software factory trajectory — the agent now travels with the developer across any terminal rather than living only inside Warp Terminal.

## Strategic Context

Warp's open-sourcing is framed as "how software will be built in the future" — humans managing agents at scale to build production-grade software. The founding sponsorship by OpenAI signals alignment with GPT models as the underlying agent runtime.

Warp is competing in the **agentic development environment** space alongside:
- [[entities/cursor-3]] — IDE-native agent platform
- [[entities/openai-codex]] — OpenAI's coding agent platform
- [[entities/claude-code]] — Anthropic's CLI coding agent

## Relationships

- [[entities/openai]] — Founding sponsor; GPT-5.5 powers agent workflows
- [[entities/cursor-3]] — Competitor in agentic development environments
- [[entities/anthropic]] — Competitor via Claude Code; shares talent pool
- [[entities/google]] — Zach Lloyd's former employer (Google Sheets/Docs)
- [[entities/paraform]] — Recruiting platform context; Warp competes for niche developer-tool talent
- [[entities/ghostty]] — Mitchell Hashimoto's terminal; Ghostty left GitHub as Warp went open-source
- [[concepts/agentic-engineering]] — Embodies the agent-first workflow pattern
- [[concepts/harness-engineering]] — Oz provides the orchestration harness

## Sources

- [Warp: Warp is now open-source](https://www.warp.dev/blog/warp-is-now-open-source)
- [Warp Documentation](https://docs.warp.dev/)
- [Ben's Bites: Building gets easier (Apr 30, 2026)](https://open.substack.com/pub/bensbites/p/building-gets-easier)
- [PitchBook: Warp Company Profile](https://pitchbook.com/profiles/company/455184-10)
- [Tracxn: Warp Company Profile](https://tracxn.com/d/companies/warp/)
- [Dealroom: Warp Company Profile](https://app.dealroom.co/companies/warp_1_2)
- [raw/articles/2026-07-17_warp_how-to-build-a-cloud-software-factory-self-improving-code-review.md](raw/articles/2026-07-17_warp_how-to-build-a-cloud-software-factory-self-improving-code-review.md)
