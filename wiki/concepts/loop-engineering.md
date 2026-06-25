---
title: "Loop Engineering"
created: 2026-06-21
updated: 2026-06-25
type: concept
tags:
  - concept
  - ai-agents
  - coding-agents
  - agentic-engineering
  - harness-engineering
  - agent-loop
  - orchestration
  - claude-code
  - prompting
  - self-correction
  - loops
aliases:
  - loop-engineering
  - designing-loops
related:
  - "[[concepts/agent-loop-orchestration]]"
  - "[[concepts/harness-engineering/agentic-loop]]"
  - "[[entities/peter-steinberger]]"
  - "[[entities/boris-cherny]]"
  - "[[entities/elvis-saravia]]"
sources:
  - raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering.md
  - raw/papers/2026-06-24_huashu_loop-engineering-anthropic-playbook.pdf
---

# Loop Engineering

**Loop Engineering** is the discipline of designing autonomous loop systems that prompt, verify, and iterate with coding agents — moving the developer's role from writing prompts to writing the system that writes the code. Articulated as a paradigm shift by Peter Steinberger (@steipete) and Boris Cherny (@bcherny) in mid-2026, it represents the maturation of agentic coding from one-shot prompting to durable, self-correcting infrastructure.

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — Peter Steinberger, June 2026

> "I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and figuring out what to do. My job is to write loops." — Boris Cherny

## The Loop Paradigm

A loop is a small program that does four things:

1. **Prompts** the coding agent
2. **Reads** what it produced
3. **Decides** whether it is done
4. **Re-prompts** with the error or next step if not

The developer stops sitting inside the loop typing prompts; instead, the model becomes a subroutine the loop calls. The shape is always the same: set a goal → act → check → feed back → repeat until the check passes or the loop stops itself.

## Five Meanings of "Loop"

The term "loop" in AI coding carries at least five distinct meanings, in chronological order:

| # | Name | Era | Description |
|---|------|-----|-------------|
| 1 | **ReAct** | 2022 | Original research pattern: reason → act → observe → repeat |
| 2 | **AutoGPT** | 2023 | Self-prompting goal loop, notorious for not knowing when to stop |
| 3 | **ralph loop** | 2024–25 | Deliberate context reset between iterations to prevent history drowning |
| 4 | **/loop and /goal** | 2025–26 | Cadence and completion conditions built into the agent, carrying state across turns |
| 5 | **orchestration** | 2026 | One author fans out many agents that read GitHub, Slack, and chat, and decide what to build next |

## Six Building Blocks

Every production loop assembles six components, most of which now ship as built-in features of coding tools:

| # | Component | Description |
|---|-----------|-------------|
| 1 | **Trigger** | Schedule, webhook, file change, or PR label that starts the loop without manual intervention |
| 2 | **Isolation** | Private checkout per agent (git worktree) to prevent file conflicts between concurrent agents |
| 3 | **Written-down context** | Conventions, build steps, and rules in files the agent reads on every run (CLAUDE.md, AGENTS.md) |
| 4 | **Tool reach** | Connectors to issue tracker, CI, database, and chat for autonomous PR creation and notification |
| 5 | **Independent verifier** | A separate agent grades output — the producing agent cannot judge its own work |
| 6 | **State on disk** | Markdown file, board, or queue outside the conversation that survives between runs |

## The PR Babysitter Pattern

A canonical loop example that can be built today:

| Dimension | Setting |
|-----------|---------|
| Trigger | Every 15 minutes |
| Scope | Open PRs labeled `agent-watch` |
| Action | If CI red (deterministic), attempt one fix. If main moved, rebase once |
| Budget | One fix per PR, 5 minutes, 10 files |
| Stop | CI green or budget exhausted → ping human |

The same shape covers CI health monitoring, deploy verification, and feedback clustering.

## Claude Code /goal Loop

The `/goal` command in Claude Code is the smallest complete loop shipped inside an agent. It defines a verifiable end state and keeps taking turns until that state is true. A strong `/goal` specifies four things:

1. **End state** — what you want achieved
2. **Evidence** — how to prove it was reached (test result, exit code, file count)
3. **Constraints** — what the agent must not break
4. **Budget** — max turns, time, files, or cost

The evaluator step uses a fast model distinct from the coder, enabling role-based model selection: some models plan better, some execute cheaper, some judge more accurately.

## Unattended Multi-Agent Loops (Cherny's Five Steps)

Boris Cherny's setup for running Opus autonomously for hours:

```
claude --permission-mode auto                          # 1 · no approval prompts
ultracode  orchestrate sub-agents to ship the feature  # 2 · fan out
/goal all tests pass and the demo loads clean          # 3 · keep going
→ cloud / desktop app                                  # 4 · close the laptop
→ chrome ext · sim MCP · live server                   # 5 · self-verify, then halt
```

## crabfleet: Loop Infrastructure as Product

Peter Steinberger's **crabfleet** (an [[entities/openclaw|OpenClaw]] project) packages loop engineering as product infrastructure:

- **Kanban board as loop queue** — tasks move through todo → running → human review → done
- **Durable execution** — heartbeats and state survive closed laptops
- **Agent fan-out** — child sessions spawn from within sandboxes with on-disk memory
- **Disposable cloud sandboxes** — browser-based terminals for safe unattended runs

## Economics of Loop Engineering

Loop engineering shifts the cost model from per-call to per-task:

- **Iterations are the budget line, not tokens.** A cheaper model that loops twice as often is not cheaper. Track cost per finished task.
- **A weak verifier is the most expensive bug.** If the "done" check is loose, the loop stops early on broken work or grinds indefinitely.
- **Failing fast is cost control.** A loop with no cap on consecutive failures eventually drains the account, not succeeds.

## When NOT to Loop

Loops only pay off when a task repeats and a machine can tell when it's done:

| Anti-pattern | Why |
|-------------|-----|
| One-shot edits | Pure overhead if a single pass suffices |
| Unscoped/exploratory work | No pass condition → never converges |
| No automated check | If the only verifier is human eyes, you are still inside the loop |

## Failure Modes

- **Human verification debt** — the loop writes faster than you can review; not reviewing defers work, doesn't remove it
- **Comprehension gaps** — shipping unread code erodes system understanding, surfacing during incidents
- **Silent drift** — a weak verifier lets wrong-but-passing work through, making the loop look productive while digging a hole

## The Four-Layer Stack (HuaShu, June 2026)

HuaShu's conference-style synthesis places loop engineering as the fourth layer in a stack where each layer minds something larger than the one below:

| Layer | What it minds | Core question |
|-------|---------------|---------------|
| **Prompt eng.** | Writing one good prompt | What should I tell the model? |
| **Context eng.** | What goes in the window now | What to retrieve, summarize, clear out? |
| **Harness eng.** | Arming a single run | Which tools, which actions, what counts as done? |
| **Loop eng.** | Scheduling on the harness | How to make it run itself over and over? |

Each layer up, the unit of concern grows: from one sentence → one window → one run → a loop that runs itself. Loop engineering automates the "waiting for you" that the harness leaves behind.

### Failure Blast Radius by Layer

The same underlying bug (e.g., an agent misreads what a function returns) manifests differently at each layer:

| Layer | Blast radius |
|-------|-------------|
| **Prompt** | One wrong answer in one exchange; caught immediately |
| **Context** | Wrong answer from stale docs; noticed when answer is confidently wrong |
| **Harness** | One file edit; run ends, diff visible, human reviews |
| **Loop** | Misreading written to state file, read back as fact, built upon across turns; by the time anyone looks, the wrong assumption is load-bearing |

> "The cost of a mistake scales with the number of turns it survives before someone catches it, and a loop is, by construction, a machine for maximizing the number of turns." — HuaShu

## The Five Moves of One Loop

Each turn of a loop does five concrete things. Drop any one and the loop will not turn, or will turn in place:

| Move | What it does | Example (morning triage loop) |
|------|-------------|-------------------------------|
| **Discovery** | Find this turn's work on its own | Skill reads CI failures, issues, commits |
| **Handoff** | Hand the task off, isolated | Each finding opens a git worktree |
| **Verification** | Swap in another agent to say "no" | Second sub-agent reviews vs. tests |
| **Persistence** | Write state outside the conversation | PR + inbox + state file on disk |
| **Scheduling** | Make it turn round after round | Morning automation runs on its own |

**Discovery** sets the ceiling on the whole loop's quality: surface work of no value and the other four moves are done beautifully in service of nothing. Crucially, automation should trigger a **skill** (knowledge made permanent), not a wall of instructions in a cron job nobody will update.

**Verification** is the easiest move to cut corners on and the least affordable to skip. The agent that wrote the code grades its own homework too softly; a dedicated hole-picker catches what the first talked itself into letting through.

## Generator / Evaluator Separation

The hardest part of a loop is putting something inside that can say "no" — and the agent writing the code is the one least likely to say it.

### Why Self-Grading Fails

Ask an agent to grade its own output and it tends to praise it confidently. The context in which the code was written is stuffed with reasons it was written that way — the agent sees the chain of self-persuasion, not the result. Inside a loop, if every "is this good enough?" is decided by the agent that just wrote it, each round nods at itself and the longer it runs the further it drifts.

### The Skeptic Remedy

Tuning a standalone evaluator to be skeptical is far more tractable than making a generator critical of its own work. The difference is structural: one cannot ask an author to step outside its own perspective, but one can swap in another agent with entirely different instructions. The idea is borrowed from **GANs** — one network builds, one picks faults.

### The Evaluator Should Act, Not Just Read

If the evaluator only reads code, it judges "does this look right," not "does it run right." Hook the evaluator to Playwright MCP so it can open pages, click buttons, take screenshots, and inspect the DOM. Shift the basis from "this JSX looks fine" to "I clicked the button, the page navigated, here is the screenshot."

A common calibration: tell the evaluator to **assume the code is broken until proven otherwise** — the default stance should be doubt, not trust.

### Claude Code /goal as Maker–Checker

```
# Evaluator agent (.claude/agents/reviewer.md)
ROLE: Adversarial code reviewer.
ASSUME: this code is BROKEN until proven otherwise.
DO NOT praise. Find what fails.
CHECK, in order:
1. Does it run? (execute, don't read)
2. Tests: run them, paste real output.
3. Edge cases the author skipped.
4. Does behavior match the ticket?
VERDICT: PASS only if every check holds. Otherwise REJECT + list each reason.
```

After each turn, a small fast model checks whether the stop condition holds; if not, another turn runs. Completion is decided by a fresh model, not the one doing the work. This is the **maker–checker principle** — decades old in banking — applied to the stop condition.

## Five Ways a Loop Goes Wrong

Each anti-pattern corresponds to one of the five moves being skipped:

| Anti-pattern | Skipped move | Symptom | Fix |
|-------------|-------------|---------|-----|
| **Nodding loop** | Verification | Never once said "no" across hundreds of turns | Generator/evaluator split |
| **Amnesiac loop** | Persistence | Each morning starts from the same place; no cumulative progress | State file on disk |
| **Manual loop** | Scheduling | Works impressively the day it's built, silently stops when attention wanders | Real trigger (timer/event) |
| **Blind loop** | Discovery | Human still decides what the loop should do each morning | Teach discovery into a skill |
| **Tangled loop** | Handoff | Parallel agents edit the same directory; merge is a mess | One isolated worktree per task |

These cluster: the disciplined loop installs all five moves, and the hasty loop installs only discovery and handoff — the two that produce visible output — and skips the three that produce safety.

## Three Loops Running in Practice

### One Engineer's Morning (Osmani)

Osmani's triage loop runs automatically every morning. A triage skill reads yesterday's failing CI tests, open issues, and recent commits. For each finding worth acting on, it opens an isolated worktree; one sub-agent drafts the fix, a second reviews. A connector opens the PR and updates the ticket. Anything it cannot handle goes to an inbox. No step needs a hand, yet it stops to wait for a human exactly where it should.

### Stripe's Minions: 1,300 PRs a Week

Stripe's enterprise-scale pipeline merges over 1,300 machine-written pull requests per week. The trigger is light (@bot in Slack or emoji reaction). What makes it reliable is the stretch **before** the model wakes up: a **deterministic orchestrator** assembles context (scanning links, pulling Jira, finding docs via Sourcegraph + MCP). Anything deterministic logic can solve never goes to a probabilistic model.

The architecture interleaves deterministic gates and creative LLM steps: the agent writes code → hard-coded linter runs (agent cannot skip it) → agent fixes lint → hard-coded commit step. The sandbox is Devbox on EC2, "cattle not pets." Notably, those 1,300 PRs are still **reviewed by humans** — the human changed desks, from writing to reviewing.

### Scheduling: Local vs. Cloud

| | Cloud | Desktop | /loop |
|---|---|---|---|
| Where it runs | cloud | machine | machine |
| Machine on? | no | yes | yes |
| Min. interval | 1 h | 1 min | 1 min |
| See local files? | no | yes | yes |

Local scheduling buys frequency and local file access at the cost of requiring the machine on. Cloud scheduling buys true autonomy at the cost of a coarser interval and a fresh clone each run. A mature loop often uses both — local for tight inner checks, cloud for the overnight sweep.

## Four Silent Costs

Four costs accrue while the loop runs, none of which sounds an alarm:

| Cost | Description | Guard |
|------|-------------|-------|
| **Verification debt** | Saved time turns into unverified output waiting to be paid back | Independent evaluator |
| **Comprehension rot** | Gap between what exists and what you actually understand grows | Read a sample daily; force yourself to explain |
| **Cognitive surrender** | Temptation to stop having an opinion and accept whatever the loop produces | Keep at least one human checkpoint |
| **Token blowout** | A bug spinning idle all night produces an unfamiliar bill | Hard caps: per-run budget, daily budget, max retries |

These four reinforce one another: unverified output → erodes understanding → invites surrender → loop runs unwatched longer → bigger bill → more unverified output.

> "The most fascinating thing about loop engineering is that it lets one person do a team's work; the most dangerous thing is the same spot, because a team argues with itself and one person plus a pile of loops easily becomes an echo chamber." — HuaShu

## Economics of Judgment

Loops make code, plans, fixes, and pull requests **abundant** — a single engineer with a well-built loop can produce the output of a small team. What stays **scarce** is the judgment that decides which of the abundant outputs to keep.

> "Loops make generation nearly free and leave judgment as the scarce resource." — HuaShu

An engineer whose value was in fast typing and API memorization finds that value evaporating. An engineer whose value was in judgment finds it amplified. The same tool widens the gap — it multiplies whatever each person brings.

### The Amplifier Cuts Both Ways

A lapse in judgment is also amplified. In the old world a bad decision cost one hand-written stretch of wrong code. In the new world a bad decision is executed faithfully, in bulk, a hundred times, by a machine that will not pause to ask whether it is right. The loop removes the slow gear that used to bail engineers out.

## Operational Discipline

Three disciplines for spending judgment well:

1. **Read a sample, always** — not everything, but a representative sample every day. Force yourself to explain each sampled change. Inability to explain = mental map has fallen behind.
2. **Cap before you ship** — set hard ceilings (per-run budget, daily budget, max retries) before the loop runs unattended for the first time. A loop without caps has delegated its spending authority to its own bugs.
3. **Keep one door open** — build at least one checkpoint where the loop pauses for a human. The engineer who welds every door shut discovers on the day they must go in that they no longer hold the key.

## Build Your First Loop (5 Steps)

1. **Run a /loop** — reruns the same task on an interval (session-scoped, 7-day expiry, local machine)
2. **Read CI and issues; triage first** — scheduled + auto-discovery is loop entry level. Discovery logic lives in a **skill**, not the schedule.
3. **Add a state file** — write findings to markdown or a board. The agent forgets; the repo does not.
4. **Add an evaluator** — `/goal` with a different model judging whether the condition holds
5. **Add worktrees for parallelism** — `--worktree` per background agent so they don't step on each other

### First-Loop Checklist

| Element | Ask yourself |
|---------|-------------|
| Discovery source | What does it read on a timer? (CI / issues / commits / inbox) |
| State file | Which disk file holds the cross-round memory? |
| Evaluator | Is there an independent check that can say "no"? |
| Isolation | Does each parallel agent get its own worktree? |
| Token cap | Did you set a spending ceiling? Who stops it if it runs off? |
| Human review | Which step pauses for you to look? |

> "A first loop is better small, but with the 'no'-saying check and the human review point fully installed." — HuaShu

## The Same Capability, Two Toolchains

| Capability | Claude Code | Codex |
|-----------|-------------|-------|
| Scheduling | /loop worker | Automations tab |
| Run until met | /goal | automation rerun + judge |
| Parallel isolation | --worktree | background worktree |
| Sub-agents | .claude/agents/ | .codex/agents/ |
| External conn. | MCP + plugins | MCP connector |
| Explicit skill | SKILL.md | $skill-name |
| Machine-off run | Cloud Routines | cloud (planned) |

Loop engineering is a set of capabilities, not a product: scheduling, run-until-condition, parallel isolation, sub-agents, external connection, and explicit skill invocation.

## Relationship to Adjacent Concepts

- [[concepts/agent-loop-orchestration]] — The technical architecture of the think-act-evaluate cycle. Loop engineering is the engineering discipline that designs, budgets, and productionizes those cycles.
- [[concepts/harness-engineering/agentic-loop]] — The ralph loop pattern of deliberate context resets between iterations. Loop engineering's six building blocks extend this into full infrastructure.
- [[concepts/compound-engineering-every]] — Matt Van Horn's related framework for compound engineering loops.
- [[concepts/codex/codex-agent-loop]] — Codex CLI's specific loop implementation (user→model→tool→repeat).

## Sources

- [[raw/articles/2026-06-19_omarsar0_from-prompting-agents-to-loop-engineering]] — Elvis Saravia, "From Prompting Agents to Loop Engineering" (Jun 19, 2026). DAIR.AI Academy.
- [[raw/papers/2026-06-24_huashu_loop-engineering-anthropic-playbook.pdf]] — HuaShu, "Loop Engineering: The Anthropic Playbook for Designing Systems That Prompt Your Agents" (Jun 24, 2026). Conference-style synthesis of Osmani's Orange Book guide.
- Peter Steinberger (@steipete), "Design Loops, Don't Prompt Agents" (Jun 7, 2026). Original tweet: 2.2M views.
- Boris Cherny (@bcherny), on running agents autonomously and loop authoring.
- [Loop Engineering](https://x.com/i/article/2064127981161959567) — Addy Osmani, June 2026
- Prithvi Rajasekaran (Anthropic), "Building long-running agentic applications: the generator/evaluator pattern," 2026
- Steve Kaliski (Stripe), "Stripe's Minions: 1,300 PRs a week," How I AI podcast, 2026
