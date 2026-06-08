---
title: "Show Us Your (Agent) Skills Episode 2 — Hilary Mason, Bryan Bischof, Eric Ma, Tomasz Tunguz"
created: 2026-05-29
updated: 2026-05-29
author: Hugo Bowne-Anderson, Thomas Wiecki (hosts)
guests: [Hilary Mason, Bryan Bischof, Eric Ma, Tomasz Tunguz]
source: YouTube (Vanishing Gradients)
url: https://www.youtube.com/watch?v=l37PR-OkYKA
type: talk
duration: "139:00"
tags: [ai-agents, agent-skills, data-science, context-engineering, developer-tooling, agent-safety, local-llm, developer-tooling, harness-engineering]
---

# Show Us Your (Agent) Skills — Episode 2

## Video Info

- **Channel**: Vanishing Gradients
- **Published**: 2026-05-15
- **Duration**: 139:00
- **Hosts**: Hugo Bowne-Anderson, Thomas Wiecki (PyMC Labs)
- **Guests**: Hilary Mason (CEO, HiddenDoor), Bryan Bischof (Theory Ventures), Eric Ma (Research DS Lead, Moderna Therapeutics), Tomasz Tunguz (Theory Ventures)
- **GitHub**: https://github.com/hugobowne/show-us-your-agent-skills

## Episode Overview

Episode 2 continues the live demo format with four guests spanning creative AI, venture capital, pharma data science, and local-model agent workflows. The unifying thread: how practitioners at the top of their fields are wiring agents into real work, not demos.

## Chapter Summary

| Timestamp | Topic |
|-----------|-------|
| 00:00 | Adversarial Testing and Token-Maxing |
| 01:00 | Welcome to Show Us Your Skills Episode 2 |
| 04:42 | Warm-Up: What Do You Love About AI Agents? |
| 07:24 | Frustrations and the Hunt for Cheap Intelligence |
| 09:50 | "I Don't Do Git Commit on the Terminal Anymore" |
| 11:35 | **Eric Ma's Demo: Marimo Pair for Agentic Data Science** |
| 15:35 | Why Reactive Notebooks Beat Jupyter for Agents |
| 18:39 | Markdown Cells Auto-Generated Inside the Notebook |
| 20:51 | Heatmaps for Single Point Mutations |
| 22:52 | Voice-First and the Human-in-the-Loop Boundary |
| 24:15 | Two Buckets of Data Science: Loading Context vs. Auto-Optimize |
| 25:55 | agents.md Rules: Cell Names, Color Maps, Literate Style |
| 28:22 | "If You're Going to Make a Claim, You Need a Plot" |
| 30:19 | Building a 3D Protein Viewer with anywidget |
| 34:40 | Coloring the Ribbon by Mutational Effect |
| 40:44 | **Welcome Hilary Mason** |
| 43:25 | Hamming: Bringing Science Back Into Engineering |
| 46:18 | "Aspirationally Very Mid": Why LLMs Need Sharp Context |
| 50:42 | Hidden Door Product Demo: World-Building with Agents |
| 55:56 | How Do You Get Off-the-Shelf LLMs to Kill a Character? |
| 57:55 | Agentic Loops for Creative Work, Not Software |
| 01:02:00 | Ask for Three Variations, Not One |
| 01:05:14 | Does Anyone Still Use an IDE? |
| 01:07:53 | When Slash Commands Beat Skill Auto-Triggering |
| 01:12:20 | Deep Copy That Plays Music (And Found a Real Bug) |
| 01:13:55 | Gremlins: Cron-Scheduled Agents for Bad Ideas |
| 01:18:35 | Bryan Quest: Cosmic Run Surprise Demo |
| 01:20:16 | **Welcome Bryan Bischof** |
| 01:22:58 | Bryan's Demo: BBplot, A Grammar of Graphics for Agents |
| 01:26:08 | Manifesto: Package the Context With the Content |
| 01:27:18 | Ambiguity Yields Variance: Always Generate Three Versions |
| 01:29:07 | Scene Graph: Telling Agents What Overlaps What |
| 01:30:53 | Every Feature Must Be Demonstrated in the Gallery |
| 01:31:57 | BBplot Eval: A Separate Repo So Agents Can't Cheat |
| 01:34:21 | Features Generated From Eval Failures, Not Human Wishlists |
| 01:42:30 | Skills That Tell the Agent to Update Itself |
| 01:47:15 | **Welcome Tomasz Tunguz** |
| 01:49:30 | The Real Superpower Is Parallelization |
| 01:50:04 | What AI Builders Can Learn From the Amish |
| 01:52:08 | Memory: The Frustration Skills Are Just Starting to Solve |
| 01:55:57 | BYOD Agents: Will Grads Bring Their Own Stack to Work? |
| 02:00:09 | Tom's Demo: Public Company Analysis on a Local Model |
| 02:01:57 | Rediscovering HTML as an Agent Output Format |
| 02:04:40 | Supply Chain Paranoia: Don't Install npm Packages Under 14 Days Old |
| 02:07:35 | Why Tom Defaults to Local Models (Latency, Secrets, Planes) |
| 02:11:48 | A 2-3K-Token System Prompt Beats a 40K Stuffed One |
| 02:13:22 | Pi's Four-Tool Philosophy: Read, Write, Edit, Bash |
| 02:14:18 | BBplot Eval Live: First Attempt on a New Chart |
| 02:17:54 | Wrap Up and Next Week's European Special |

## Key Insights

### Eric Ma — Agentic Data Science at Moderna with Marimo Pair

Eric demonstrated a live agentic data science workflow using **Marimo** (reactive notebooks) paired with an AI agent. Key architectural decisions:

- **Marimo over Jupyter**: Reactive notebooks allow agents to read/write Python variables directly without fragile kernel state management. The notebook is a deterministic DAG, so the agent always knows what's computed.
- **Markdown auto-generation**: The agent writes markdown cells explaining its own reasoning — literate programming for agent-human collaboration.
- **agents.md rules**: Eric enforces cell naming conventions, color map standards, and literate style through agents.md. "If you're going to make a claim, you need a plot" — the agent must produce visual evidence.
- **anywidget integration**: Building a 3D protein viewer with anywidget, coloring molecular ribbons by mutational effect — the agent orchestrates complex visualization libraries.
- **Two buckets of data science**: (1) Loading context (feeding the agent domain knowledge, molecule structures, experimental data), (2) Auto-optimize (the agent iteratively improves analysis). The human stays at the boundary deciding when to switch buckets.

### Hilary Mason — Agentic Loops for Creative Work at HiddenDoor

Hilary brought a creative-industry perspective on agents, building narrative worlds at HiddenDoor:

- **Agentic loops ≠ coding loops**: Creative work needs agentic iteration on narrative, not code. The loop is: interview the creative → generate variations → eval against editorial criteria → iterate.
- **"Aspirationally very mid"**: LLMs need extremely sharp context to avoid mediocre output. The difference between great and mid is entirely in how precisely you frame the ask.
- **Three variations, not one**: Always ask for 3+ distinct variations with different magnitudes of change and risk. One variation is samey; three creates real choice.
- **Evaluator framework**: Define editorial criteria upfront, score each variation against criteria, compare to the baseline eval from the beginning of the process.
- **Hermes agent harness**: Hilary uses Hermes for creative workflows — slash commands over auto-triggering, deep copy skills, and "Gremlins" (cron-scheduled agents for deliberately bad ideas to surface edge cases).
- **Hidden Door's Justfile**: Heavily uses Just command runner to orchestrate agent scripts — LLM tasks for background story monitoring.

### Bryan Bischof — BBplot: A Grammar of Graphics for Agents

Bryan demonstrated BBplot, a visualization library designed for LLM agents rather than human programmers:

- **Package context with content**: Every chart output includes the data, config, and scene graph alongside the image — the agent needs full context to iterate.
- **Scene graph**: Tells the agent what overlaps what, enabling layout-aware chart generation.
- **Ambiguity yields variance**: Always generate 3 chart variations. Single-pass generation locks into one interpretation of ambiguous specs.
- **Eval-driven feature development**: Features come from eval failures, not human wishlists. A separate eval repo prevents agents from "cheating" by seeing test cases.
- **Gallery requirement**: Every feature must be demonstrated in the gallery — agents learn by example.
- **Self-updating skills**: Skills that tell the agent to update itself — the meta-skill pattern.

### Tomasz Tunguz — Local Models, Supply Chain Paranoia, and HTML Output

Tom brought a VC/investor perspective with strong opinions on infrastructure:

- **Local models as default**: Latency, secrets, and airplane mode — Tom defaults to local models (via Ollama) for all agent work. Cloud only when necessary.
- **HTML renaissance**: Rediscovering HTML as the ideal agent output format — portable, self-contained, universally renderable.
- **Supply chain paranoia**: Never install npm packages under 14 days old. The agent supply chain is an unexamined vulnerability.
- **2-3K token system prompts**: A tight, focused system prompt beats a 40K-token stuffed one. Precision > volume.
- **Pi's four-tool philosophy**: Read, Write, Edit, Bash — minimal tool surface maximizes reliability.
- **Parallelization is the real superpower**: The Amish analogy — adopt technology deliberately, not reflexively. Parallel agents doing independent work beat sequential chains.
- **Memory frustration**: Skills are just starting to solve the memory problem. BYOD agents (Bring Your Own Device) — will new grads bring their personal agent stacks to work?

## Connection to Wiki Concepts

- [[concepts/agentic-engineering]] — Eric's Marimo Pair workflow as a new agentic data science pattern; Bryan's eval-driven development as verification methodology
- [[concepts/agentic-data-science]] — Eric Ma's two-bucket framework for agent-assisted science
- [[concepts/ai-safety]] — Tom's supply chain paranoia and 14-day npm rule
- [[concepts/local-models]] — Tom's local-first agent philosophy
- [[concepts/creative-ai]] — Hilary's agentic loops for creative vs. engineering work
- [[entities/marimo]] — Reactive notebooks as agent substrate
