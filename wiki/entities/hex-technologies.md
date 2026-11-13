---
title: "Hex Technologies"
type: entity
created: 2026-05-08
updated: 2026-11-13
tags:
  - company
aliases: ["Hex", "Hex Tech"]
sources:
  - https://hex.tech
  - raw/articles/2026-05-23_hex-technologies_evaluate-data-agents.md
  - raw/articles/2026-05-10_hex-technologies_notebook-agent-prompting-guide-agentic-analytics.md
  - raw/articles/2026-08-14_hex-technologies_databench-agentic-analytics-benchmark.md
  - raw/articles/2026-10-28_hex-technologies_hex-new-era.md
  - raw/articles/2026-10-28_hex-technologies_introducing-hex-4-0.md
  - raw/articles/2026-11-05_hex-technologies_ai-sorcerers-stone.md
  - raw/articles/2026-11-13_hex-technologies_what-we-learned-working-with-robots-to-rewrite-hex.md
  - raw/articles/2026-05-10_hex-technologies_beginners-guide-to-python-notebooks.md
---

# Hex Technologies

Hex is an AI analytics platform that combines collaborative notebooks, conversational self-serve analytics, and data apps in one connected workspace. It unifies the traditionally fragmented data stack — notebooks, BI, and dashboards — with AI woven throughout.

| | |
|---|---|
| **Type** | AI Analytics Platform |
| **Founded** | 2020 |
| **Leadership** | Barry McCardel (Co-Founder & CEO), Caitlin Colgrove (Co-Founder & CTO), Glen Takahashi (Co-Founder & Chief Architect) |
| **Key Products** | Hex platform (agentic notebooks, conversational analytics, Context Studio, Hex CLI) |
| **Website** | [hex.tech](https://hex.tech) |
| **Tech Blog** | [hex.tech/blog](https://hex.tech/blog) |

## Key Facts
- Founded in 2020 by former Palantir engineers frustrated with fragmented data tools.
- Raised $70M in May 2025; total funding ~$172M.
- Trusted by Reddit, StubHub, HubSpot, Cisco, Figma, Anthropic, Rivian, and the NBA.
- Acquired Hashboard (BI platform) to expand analytics capabilities.

## Products & Technology
- **Agentic Notebooks**: Polyglot notebooks (SQL, Python, R) with a built-in AI agent for deeper analysis.
- **Conversational Self-Serve**: Business users ask questions in plain language against a shared semantic layer.
- **Context Studio**: AI governance and semantic models for trusted, consistent answers.
- **Hex CLI**: Terminal-based analytics control.
- Graph-based execution model for reproducibility at scale.

### Notebook Agent Prompting Guide (September 2025)

Authored by Alex Brumas (Product), September 24, 2025 (Olivia Koshy was PM of the team that built the Notebook Agent). The guide codifies prompting patterns for Hex's Notebook Agent — an "analytical partner" that knows data-project best practices and is "really good at writing SQL, Python, and configuring viz." The author's framing explicitly transfers vibe-coding learnings (from Lovable, a Hex customer) to agentic analytics.

**Four key capabilities:**
- **Agentic search** — discovers the right data sources without remembering exact table names/schemas (planned: search across docs, projects, components)
- **Building a plan** — translates business questions into a structured analytical approach
- **Executing analysis** — writes and runs code to transform, visualize, and model data
- **Summarizing results** — explains insights in plain language

**Mental models for prompting:**
- **Structured prompting**: Context / Task / Guidelines / Constraints template (e.g., "You are analyzing customer transaction data to help improve marketing targeting...")
- **Conversational prompting**: DM-style prompts that implicitly carry the same structure — fine for most interactions
- **Meta-prompting**: the biggest piece of advice — have the agent craft a concrete plan, critique/refine it, then feed the plan back to the agent for step-by-step execution
- **Scoping context**: deliberately scope the agent with `@` tags — `@customer_transactions` table references or `[@Prophet Model Components Analysis]` cell references focus the agent on the right context
- **Specify analysis methods**: state the model/technique explicitly (e.g., "Build a random forest classifier... using feature importance") or ask for suggestions first, then narrow down
- **Business-impact framing**: tie analysis to decisions (e.g., "which channels to increase investment in for our Q4 campaign planning")
- **Workspace rules file**: organization-level injected context applied to every agent interaction — PII handling, source-of-truth tables, business definitions (MRR, churn, LTV), required analysis patterns (YoY+MoM together, 13-week rolling forecast baseline), data quality warnings (duplicate rows, delayed feeds), stakeholder preferences, industry benchmarks
- **Treat the agent like an expert consultant**, not a code jockey — ask it for advice, industry standards, and technique explanations

**Copy-paste template categories:** data discovery, notebook cleanup & dependency mapping (orphaned/duplicative cell detection), analyzing teammates' work, **cross-project prompt chaining** (have the agent generate a portable context prompt in one notebook, paste it into a new notebook to seed context), and template-replication prompts (k-means/hierarchical clustering, LTV modeling, geospatial viz, EDA, e-commerce KPIs, cohorts, market basket analysis).

Source: raw/articles/2026-05-10_hex-technologies_notebook-agent-prompting-guide-agentic-analytics.md (published 2025-09-24)

### Repos as Agent Context (May 2026)
Hex added the ability to attach Git repos to workspaces, enabling the Hex Agent to analyze dbt models and application code. This bridges the gap between data warehouse context and code-level understanding.

- **dbt repo use case**: Self-service users can query high-level tables while the agent crawls upstream dbt logic to understand filtering, collapsing, and category definitions
- **Application repo use case**: Answers questions about tracking implementation, untracked events, and how features relate in the codebase
- **Compounding context**: Repos, projects, warehouse metadata, guides, and semantic models are synthesized by the agent to answer questions that previously only the data team could address
- **Customers**: Underdog (Camden Willeford), Stubhub (Alan Peters) report significantly improved ability to handle "nebulous" queries

Authored by Andrew Lee (May 15, 2026).

### Python Notebooks Beginner's Guide (2022)

Hex's earliest educational post (Sep 22, 2022) — a Jupyter/IPython tutorial predating the agent era. Documents the notebook paradigm Hex builds on: cells + kernel architecture, the "run code, explore data, present results" loop (Fernando Perez quote on IPython's origin as an "afternoon hack"), and production notebook use at Netflix (most data access via notebooks), Bloomberg (notebooks in the terminal), PayPal (Jupyter as a platform), and Lyft (LyftLearn, Jupyter in Kubernetes). Low AI-specific content; kept as context for the notebook lineage behind Hex's agentic notebooks.

Source: raw/articles/2026-05-10_hex-technologies_beginners-guide-to-python-notebooks.md

## Data Agent Evaluation Lab (Shoebox)

In May 2026, Hex engineer Izzy Miller detailed how Hex evaluates data agents with a custom internal lab called **Shoebox** — originally a hacky trace viewer, evolved into a full-fledged agent observability and evaluation platform.

### Shoebox Architecture

- **Pairwise experiment model**: Every evaluation is designed as a pairwise comparison between a "candidate" run and a "baseline" run, not a standalone test. This biases teams to report treatment matrices and side-by-side trajectories rather than aggregated numbers in isolation.
- **Local + remote hybrid**: Shoebox runs as part of the local Hex dev stack but connects to a shared internal Hex workspace where eval sets run daily to establish "production baselines." Engineers compare locally-executed candidate runs against remotely-executed baselines, with painstaking care to sync environments for apples-to-apples comparison.
- **Custom rubric system**: Core eval sets ship with preconfigured rubrics (ToolEfficiency, SemanticLayerUsage, WorkspaceGuideAdherence) and ground truths. Anyone can configure deterministic, LLM-judged, or hybrid rubrics. Run-scoped "hypothesis objective" rubrics allow pairwise evaluation specific to a single experiment — these consider candidate and baseline trajectories side-by-side at judge time, with access to post-run metadata for speed/cost evaluation.
- **Auto-research loop**: Shoebox exposes agent skills that let coding agents experiment against evals in an auto-research-like loop.

### Shorelane Commerce — Synthetic Evaluation Business

Hex created a fully synthetic B2B2C office-supplies platform called **Shorelane Commerce** to serve as a realistic evaluation environment:

- **Scale**: ~$129M yearly revenue, three revenue streams (direct-to-consumer, business subscriptions with net-30 terms, third-party marketplace with 15-25% cut)
- **Realistic data debt**: Migrated platforms in 2021 losing customer IDs, acquired a competitor (never fully merged data), renamed a sales channel in 2022 without backfilling, restructured plans in 2023 with grandfathered customers, five columns that could plausibly be called "revenue"
- **Source systems**: Stripe, Salesforce, legacy Shopify (mostly red herring), three ad platforms with different conversion totals
- **30,000 lines** of handcrafted data generators, dbt models, warehouse documentation, events, triggers, and stakeholder personas producing six years of realistic data across millions of rows and dozens of tables
- **Evals look like**: "How many support refund requests in the last 30 days haven't been processed yet?" rather than contrived prompt tricks

### Key Design Decisions

- **No eval-reality drift**: Shoebox integrates deeply with the actual Hex application — product improvements automatically take effect in evaluations
- **LLM judge calibration challenges**: Hex biases toward being overly harsh, but struggles with calibration (e.g., a 0.01pp difference accepted 35% of the time by the LLM judge)
- **Environment sync is the hardest problem**: Maintaining consistent eval environments across local dev, shared baselines, and production configs requires a careful maze of export/reset scripts

Authored by Izzy Miller, Engineering (May 22, 2026).

### DataBench — Agentic Analytics Benchmark (August 2026)

In August 2026, Hex released **DataBench**, a frontier benchmark for agentic analytics built on the Shorelane environment (see above). It addresses the gap between existing analytics benchmarks (which Hex calls "overspecified pub trivia" — e.g., Sonnet 4.5 at 90% on Spider 2.0, Claude Haiku 4.5 at 89% on DABstep) and realistic user prompts, which are vague, directional, and often unanswerable with the available data.

**Design**: 100 realistic analytical tasks (Q&A + open-ended) in the Shorelane Commerce workspace, judged by a GPT-5.6 Sol LLM judge with plain-language rubric briefs (majority of 3 judge runs, 96% agreement). Ten tasks are deliberately crafted "signature traps" with obvious-but-wrong answers.

**Key findings**:
- No model/effort pair scores below 50%; the analytical floor is higher than expected
- **GPT-5.6 Luna** forms the entire pre-elbow of the Pareto frontier — near-Sol performance at ~1/14th the cost
- **Test-time scaling regressions**: unlike coding benchmarks (CursorBench), higher effort can *hurt* — Opus 5 "gets devastated" at xhigh/max, talking itself past correct simple answers
- **Claude Fable 5 is the exception**: only model where scaling effort consistently buys better outcomes (85/100 top score)
- Task breakdown: 75% Q&A, 66% open-ended, 54% traps — the gap is *judgment*, not evidence gathering
- Failure mode: "manufacturing certainty" — Opus 5 at max effort produced 11 minutes of correct arithmetic then promoted correlation into a causal law and wrote a confident (wrong) recommendation

Hex plans to open-source the Shorelane analytical environment (DataBench itself stays private to avoid training contamination). Full details: [[concepts/ai-benchmarks/databench]].

Source: raw/articles/2026-08-14_hex-technologies_databench-agentic-analytics-benchmark.md

### Hex in Codex Integration (June 2, 2026)

Hex launched as an **OpenAI Codex plugin**, enabling Codex users to invoke Hex for analytics without leaving the coding agent. Three integration modes:

- **Kick off analysis from Codex**: Ask a natural language question → Codex invokes Hex → Hex runs the query and returns results (churn by segment, pipeline performance, product usage trends)
- **Pull Hex Threads into Codex**: MCP connection lets Codex pull existing Hex threads as context for reports and meetings — prior work is available without redoing it
- **CLI control**: Programmatic Hex project/cell creation for automated workflows; Codex can also migrate existing BI projects to Hex

Hex's thesis: "Without context, an agent won't use the right data to answer a business question." The integration extends Hex's Context Studio philosophy — when working in Codex, your Hex analyses, data, and context inform whatever you build. Codex admins can enable the plugin in their workspace.

Hex previously launched **Agent, everywhere** (October 2025) with Slack integration and MCP support, allowing the Hex Agent to operate inside Slack, Claude, and Cursor.

Source: raw/articles/2026-06-03_hex-technologies_hex-in-codex.md

## Hex 4.0 — clean-sheet rewrite "for the era of agents" (October 27, 2026)

Hex rewrote its 6-year-old, 2,500-customer product from scratch and announced a fundraising alongside it. The post is unusually valuable as a **first-party post-mortem on bolting agents onto a legacy architecture** — the failure modes it names are the ones [[concepts/agent-native-tool-fallacy]] and [[concepts/harness-engineering/agent-native-architecture]] discuss in the abstract.

**The diagnosis (Hex's own words).** Despite shipping text-to-SQL before ChatGPT, Magic (Feb 2023), "the first really good data agent," and generative apps, the company concluded it was **"far from 'agent native', no matter how much we liked saying it"** because its data model, architecture, and user assumptions were baked in 2020–21. Three concrete failure modes followed:

1. **Tool-count bloat in the harness** — "our agent harness was becoming bloated with hundreds of tools, which were required to teach agents about how to use Hex," something "emphatically out of distribution."
2. **Keyhole external-agent compatibility** — external agents could only reach Hex "through a keyhole via MCP versus being able to work with something more native."
3. **Wrong compute shape** — the engine "wasn't built to support the high-speed, high-concurrency, iterative workflows agents seem to like."

Concurrent market pressure: users were "vibe coding" dashboards in Cursor, Codex, Cognition and Claude, emailing HTML files "without provenance, context, or permissions" — sprawl nobody could govern or observe.

**The architectural bet: everything is code.** Project core logic and visualizations are now fully backed by **plain code files rather than a proprietary YAML spec**, "rooted in governed context" with consistent logic, visual standards, and organization. Code is chosen for both directions: it's what makes the platform legible to agents, and it's what gives humans full build flexibility. Because the agent specifies every dependency and the **full DAG**, any number in a published app is inspectable end-to-end — click inspect, see the lineage, the full logic, and the data sources, so a non-technical user can tell whether a KPI rests on a trusted semantic model or a tangle needing data-team review. The Notebook is reframed as a **human/agent collaboration surface** where most of the job is navigating what an agent wrote rather than writing code.

**Execution engine rebuilt from scratch**, with three named wins: parallel execution of independent queries; results streaming as ready; **incremental recomputation** — a changed input reruns only the affected step and its dependents, everything else stays cached. Hex reports a large full-app runtime improvement on internal critical apps and claims hover/click-live filter states that "would have taken minutes" under 3.0. Status: private beta, staged rollout, migration workflow promised; alpha testers **StubHub** (Nova Wang) and **Ro** (Nick Hardy).

**Meta-observation**: the rewrite itself "was greatly accelerated by using agents to write all of the code." The strategic read for this wiki is that **MCP proved insufficient as an agent-integration substrate for data platforms** — Hex's own account is that keyhole MCP plus tool-harness bloat was a reason to rebuild, which is evidence against treating MCP exposure as a finish line. Cross-reference [[concepts/agent-native-cloud]].

Sources: [[raw/articles/2026-10-28_hex-technologies_hex-new-era]], [[raw/articles/2026-10-28_hex-technologies_introducing-hex-4-0]]

## Hero — Self-Improving Agent Observability (November 2026)

"The AI sorcerer's stone" (Deena Sun, summer 2026 intern, updated Nov 4, 2026) describes **Hero** (**He**x **R**ecursive-self-improvement and **O**bservability): an agent that analyzes real production threads from Hex's own agents and rebuilds the Hex agent harness — "an agent in Hex designed to rebuild the agent in Hex." It is an instance of the agentic-observability + autoresearch pattern: a real-time, bottom-up complement to offline evals ("realistic evaluations are hard! … nothing beats actually evaluating the real thing").

**The Hero cycle (3 steps):**
1. **Analyzer agents** autonomously deep-dive individual agent trajectories from real usage, hunting hard failures (errors, exceptions, crashes) and *soft* failures (agent doesn't do what the user expected).
2. An **aggregator agent** hierarchically clusters findings — connecting issues across interactions, grouping recurring failures into themes, tying them to root causes (from conflicting tool instructions up to subagent handoff flow).
3. Each cluster becomes a **triageable call-to-action / PR**; agents collaborate on remediation using the cluster findings as evidence and test cases. The cycle repeats.

The recursion is literal: analyzer and aggregator reuse the same harness and agent-platform code as Hex's production agents, so Hero's improvements are changes to parts of itself — "the code I merged will probably be changed by the very code I merged."

**Negative result worth keeping**: chunking threads into disjoint parts for parallel subagent analysis "wasn't worth the squeeze" — multi-turn Hex trajectories have many causal steps, and error-tracing needs full context over how an agent stumbles *but recovers*. A "knowledge bank of lessons from experiments that didn't work" was maintained as a first-class artifact.

**AI-accelerated engineering velocity (self-reported, summer-over-summer):** 215.9 PRs merged/week (+35%), 105.2K lines written/deleted per week (+133%); per-engineer PR throughput +23% even accounting for team growth; weekly LoC per engineer more than doubled.

The essay's framing — "what is stone and what is sand?" — argues code's ephemerality (accelerated by agents into an "ouroboric cycle" visible within a single internship) shifts research value from artifacts to ideas: anchor weeks around questions/hypotheses, not lines of code. The intern project succeeding means its current form shouldn't be recognizable in six months.

Source: raw/articles/2026-11-05_hex-technologies_ai-sorcerers-stone.md (https://hex.tech/blog/ai-sorcerers-stone/)

## Rewriting Hex with coding agents — practitioner playbook (November 12, 2026)

Charlie Imhoff's post-mortem on the Hex 4.0 rewrite is the operational companion to the October launch post above: **~250,000 lines touched (~10% of a 6-year-old codebase) in a four-month push**, and the first fully explicit set of rules Hex derived for what agents may and may not decide. Its own framing is self-deprecating — "I'll probably be looking back on this post like it's a 2024-era prompt engineering guide in about six months" — which makes it a dated-practice artifact rather than a claimed law.

**The seven rules, with the concrete mechanism named in each:**

1. **No one-shotting into production.** "The robot will almost never one-shot anything" is not a prompt or intelligence failure — software complexity is *discovered during implementation*, so enumerating it upfront is usually impossible. Counter-intuitive tactic: keep the same thread rather than restarting fresh after a revert, unless context is "truly poisoned". The robot's speed should buy *more* iterations, not fewer.
2. **Vigilance about coupling — "AI agents have no respect for an API boundary."** Agents will thread a low-level parameter through a high-level function to influence one log line, duplicate logic between two implementations and hope it stays in sync, or bypass a structured API for a raw untyped request to a hardcoded port. Abstractions do not emerge unless explicitly commanded. **Concrete control adopted at Hex: the agent is disallowed from adding or modifying any exported function signature or data type** — the human authors signatures, the robot fills in bodies.
3. **"No TODO left behind."** Humans scaffold with TODOs and defer edge cases so the first review can target structure; robots are "more than happy to build the whole hog at once" — every edge case, optimization and test — which hides the key decisions. Root cause stated plainly: agents are trained to produce production code *immediately*, not code that ladders up into production over time, and "they never say no, even when 'I shouldn't worry about this right now' is the correct answer." Mitigation: withhold the full plan so the agent cannot jump the gun, and instruct liberal TODOs while prototyping.
4. **DRY becomes DAMP ("Damn, A Massive Program").** Engineers are lazy and not paid by lines, so a written snippet is evidence it was deemed necessary; robots are neither, and their small context windows plus expensive searches mean they do not look for pre-existing patterns unless told. Robots can spot duplicated symbols but are weak at finding a coherent path to unifying them — so review must recall the whole system, not just the diff. "Few of these [structural refactors] are agent-initiated. When it comes to refactoring, it still takes a human Eagle Scout to leave things better than they found them."
5. **Give agents statically verifiable exit criteria.** The standout case study: unifying file-path semantics to relative-from-`project/`. Because paths were plain strings, no reader/writer could be statically checked, and the agent looped with ever-broader greps unable to verify completion. Fix: **change the APIs to accept a wrapped string type so all callers statically break**, converting the task into "fix the build" with a deterministic exit criterion and a checkable tool call; a second thread later removed the wrapper. Generalizable pattern — manufacture a compile-time failure to give an agent a termination condition.
6. **One thing at a time.** Codex Cloud agents and Worktree buttons are "a siren's song": ten concurrent agents do not multiply throughput, they produce stress. Imhoff caps himself at one, absolute maximum two; waiting time goes to reading output, steering, queuing follow-ups as if reviewing, writing docs/plan architecture.
7. **Declare where YOLO-ing is acceptable.** Hex labels algorithmically dense but systemically simple code "procedural" (the Hex 4.0 token-stream parser: hundreds of lines, single entry point, no side effects, trivially testable) and designates **narrow "black box" regions** where agent-written mess is acceptable because it stays contained. The governance point is team-wide agreement — nobody should mark as "full send vibes" code others consider important, or burn time refactoring code the team has no stake in.

**Authorship and review etiquette (the social half of the playbook).** "The robots are not people. You can call them 'robot.'" But a PR is still something a human attached their name to: calling it "slop" may attack a colleague's own work, and "don't diminish the impact of a colleague by attributing their successes to Anthropic." Authors should state which parts they are proud of and which they invite criticism on.

**Strategic read for the wiki**: this is the *process* layer beneath the October architecture post — the two together make Hex the most complete first-party case study in this wiki of a large agent-driven rewrite (architecture rationale + review discipline + failure taxonomy). Rule 2's signature-freeze and rule 5's wrapper-string trick are concrete harness-engineering controls; the DAMP observation and the non-agent-initiated-refactor finding are evidence for the human-ownership half of [[concepts/agentic-engineering]]. Cross-reference [[concepts/coding-agents/agentic-coding]], [[concepts/harness-engineering/agent-native-architecture]], [[concepts/agent-native-tool-fallacy]].

Source: [[raw/articles/2026-11-13_hex-technologies_what-we-learned-working-with-robots-to-rewrite-hex]]

## Related
- [[entities/anthropic]] — customer using Hex for data analytics
- [[entities/palantir]] — founders' previous employer
- [[concepts/data-notebooks]] — notebook paradigm evolution
- [[concepts/ai-benchmarks/databench]] — Hex's agentic analytics benchmark (August 2026)
