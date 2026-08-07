---
title: "Prime Agent: A self-improving RLM agent"
source: "https://x.com/i/article/2085608999110803456"
date: 2026-08-07
date_ingested: 2026-08-07
author: "Prime Intellect"
type: x_article
x_article_id: "2085608999110803456"
tweet_id: "2085612369154281546"
getxapi: false
source_fallback: false
tags: [prime-agent, rlm, coding-agent, harness, continual-harness, open-source]
---

Today, we are launching Prime Agent, our self-improving coding harness designed around two abstractions, the Recursive Language Model (RLM) [citation] and Continual Harness [citation]. Modern harness designs were built around the capabilities of earlier generations of models, and they do not reflect what frontier models can do today: fixed tool-calling schemas and context compaction force the model to work around its own scaffolding instead of leveraging it. Static, hand-engineered sub-agents, prompts, skills, and memory are set once at design time and never adapt to what the agent learns while running. We believe that harnesses should instead extrapolate on current model capabilities toward the next frontier of reasoning patterns.

Prime Agent is built around this principle through two main abstractions:
The Recursive Language Model (RLM) treats context as a variable and subagent delegation as function calls inside a REPL. The persistent REPL gives the model programmatic access to its history, sub-agents, and tools, allowing it to write language model programs as actions over its own context. This design allows the agent to process arbitrarily long sessions without losing access to its own past information stored in variables.
Continual Harness treats the harness's own state, abstracted as its prompts, skills, memory, and sub-agents, as something the agent can create, read, update, and delete (CRUD) from its own trajectory. When combined with agent-to-agent communication, this mechanism enables orchestration across sub-agents and even across Prime Agent sessions. For example, Prime Agent can spawn persistent sub-agents, message them later in the trajectory, and communicate directly with a different Prime Agent session.
These abstractions are powerful for bootstrapping model capabilities. Prime Agent is built to be effective as a general coding assistant, as a default runtime for long-horizon autonomous evaluation, and as a collaborator for research and autoresearch.

Prime Agent is fully open-source, and can be installed via:
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh

The performance of agent harnesses are tied to both the design of the harness and the capability of the model trained around the harness. We designed Prime Agent to be immediately usable with modern open and closed frontier models, while also providing a feature set that we expect to provide further performance gains as newer generations of models are trained around it.

At its core, Prime Agent is designed around programmatic tool and sub-agent calling. Models in Prime Agent use a persistent IPython kernel as their only tool. Other standard harness features are called as functions in the kernel, including sub-agents, which are each implemented as another prime-agent instance.

Prime Agent runs a background daemon that owns all live agent sessions over a local socket. You can attach and detach from the session without affecting the underlying agent loop. Each root session tree runs in a recoverable worker process; if a worker crashes, the daemon recovers it from the session JSONL and kernel state snapshot.

The Agents View allows you to see and select other live sessions from the daemon. It can be opened by pressing the Left Arrow key on an empty prompt, and lists sessions that are currently running, idle sessions with the daemon still active, and inactive sessions that are currently not loaded in memory. Any of these chats can immediately be entered and interacted with, and pressing space allows users to chat with a session in any state, including steering and queuing of prompts and commands such as /compact.

The Agents View is constructed as the central connecting point between agents and subagents, recursively. Any agent is discoverable in an Agents View. Users navigate from an Agents View into an agent's chat, then into the Agents View of its subagents, into a subagent chat, and so on.

Because subagents share the same Running-Idle-Inactive state machine as the root agents, they can be removed from memory after 30 minutes of inactivity, and the moment a user or agent addresses any of them, they are reloaded from disk. In highly nested chats, this can save a lot of memory.

The entire session history of the agent is stored as append-only JSONL files on disk. Each line is a JSON entry, which can include messages, model switches, compaction summaries, or extension entries. Branching, forking, and cloning all happen within the same file by moving the leaf pointer. The full history is always recoverable through /tree.

Compaction happens when the context hits a threshold or directly by the agent in the REPL with compact.run(). Compaction is primarily used to clean the main context of the agent, but the full history, including past compactions, can be accessed programmatically in the IPython kernel when needed.

The introduction of the REPL requires additional work to manage the IPython state. We asynchronously compact and clean the kernel simultaneously, using a spawned agent to act as a garbage collector. This is necessary to avoid REPL memory built up for each agent.

RLM and Programmatic Tool-Calling (PTC):
Prime Agent relies on the IPython kernel as its REPL that persists over the session, which it can invoke every turn. On initialization, the kernel pre-imports each skill / tool as a module, including the rlm for recursive programmatic sub-agent calling.

The rlm is an asynchronous function, meaning the model can freely invoke and parallelize sub-agent calls in code. Spawning a subagent (e.g. await rlm("sub-task")) launches a full session with its own model, IPython kernel, session tree, and conversation history. It returns immediately, because all subsequent communication between agents happens through the agent_message.send(...) tool.

There are several useful primitives that Prime Agent can choose to launch in this way, such as fanning out sub-agents in parallel, or launching background work.

As models continue to improve, new invocation patterns over tool calls and sub-agents will emerge. We expect future generations of models to rely less on hand-holding prompts and more on this kind of direct, programmatic control.

Orchestration and Multi-Agent Communication:
The background daemon manages all live Prime Agent sessions. Prime Agent also enables Agent-to-Agent (A2A) messaging through the daemon, letting any Prime Agent session message any other Prime Agent session using the same mechanism used for messaging persistent sub-agents. This allows for easy orchestration to manage the progress of sub-agent swarms and communication regarding shared resources directly between the affected agents. To prevent undesirable communication across independent sessions, multi-agent communication in Prime Agent is limited to its nuclear family, meaning parent, sibling, or child processes.

Prime Agent supports persistent sub-agents through its RLM-native runtime, meaning a sub-agent's own session directory, context, IPython kernel, and session history persist even after the initial sub-agent call has finished. Prime Agent can send further messages to continue a persistent sub-agent by accessing its unique session identifier, all from its IPython kernel.

Self-Improvement via the Continual Harness:
Prime Agent's harness state lives in the persistent IPython kernel as rlm.harness, immediately readable and callable by the agent mid-task, and every change is also written to disk, so it survives across turns and across sessions. Continual Harness formalizes this state as H=(p,G,K,M), prompt, sub-agents, skills, and memory, refined online from the agent's own trajectory without resets.

Each of the four components exposes the same create, read, update, delete surface. create_prompt_note(...), create_memory(...), create_skill(...), and create_subagent(...) each add an entry of that kind, update_X(...) and delete_X(...) mirror them, and list(kind) or get(kind, id) read them back. Skills follow this same surface: authoring a Python-backed skill is a create_skill(...) call carrying a SKILL.md-style reference, the same operation as adding a memory or a prompt note.

/refine is the self-improving pipeline built on top of this CRUD surface. It reads the agent's own trajectory, the record of what was tried and what happened, and applies the smallest relevant CRUD edit that improves the harness toward better outcomes: updating a prompt note, memory, skill, or sub-agent spec, rather than rewriting the whole harness. Each refinement records its trigger and the outcome it produced, so improvement is evidence-backed rather than arbitrary. Refinement runs in two phases. Planning, the LLM call that proposes the edit, runs in the background and does not block the ongoing conversation. Applying the edit, writing to disk and rebuilding the system prompt, is fast and only briefly blocks at the next turn boundary. The agent can call refine.run() directly whenever it notices a repeated failure or a reusable tactic, not only on a fixed schedule.

The base system prompt remains immutable. /refine only edits the harness layer around it. Rollback is supported through prior refinement history, allowing a bad harness update to be reverted by ID.

Autonomous Mode for Evals:
Prime Agent's eval mode combines three complementary mechanisms. A goal sets the overall objective: a persistent objective with an optional token budget that the harness keeps re-prompting the agent to pursue across turns, tracked until the agent explicitly calls goal.complete(). Heartbeats are scheduled cron-style messages injected into the session on a fixed interval, used for regular checks such as monitoring a sub-agent's progress or polling for a training update. Autonomous mode is the continuation mechanism itself, ensuring the agent keeps working toward the goal instead of stopping early once a turn produces no further output. Together, these let a session run unattended for extended periods while remaining bounded by an explicit budget and inspectable through the Agents View.

Autonomous mode is available directly from the CLI with --autonomous, no scripting required. A run can set a completion goal and a turn limit in the same command.

The gate command runs before the session is allowed to finish. A failed gate returns its bounded output to the agent for another attempt, and Prime Agent skips rerunning a failed gate when the workspace has not changed since the last attempt. --autonomous-max-turns, --autonomous-max-tokens, and --autonomous-timeout-ms bound continuations, tokens, and wall-clock time respectively.

Benchmarks:
Prime Agent serves as both a coding agent to be used, and a harness design to be evaluated for research. No model has been trained around Prime Agent or its core feature set yet.

ARC-AGI 3: Prime Agent with Opus 5 achieves 95.5% RHAE Best@1, surpassing the human expert baseline of 95.4%. Across three runs: [95.0, 95.2, 95.5] and 99.97% Best@3 with 183/183 levels complete. Prime Agent also achieves this at lower token usage than native harnesses, by programmatically running functions over data rather than spending tokens reading data with tools.

Long context benchmarks: Prime Agent with GLM-5.2 is competitive across long-context coding, retrieval, and reasoning tasks against closed-model harnesses (Codex with GPT, Claude Code with Opus). Excels on long-running autonomous tasks.

EmulatorBench: Prime Agent successfully reproduces SEGA Genesis and Nintendo Game Boy Color emulators from scratch in Rust, sandboxed without reference implementation. Averaged over 16 emulator reconstructions.

PMPP-Hard (GPU kernels): Evaluated on GPU kernel writing benchmark with correctness checks against KernelGuard, the verification tool used for the official GPU MODE kernel leaderboard.

Factorio (FLE): Prime Agent leveraged /refine to turn failures into successes, achieving 100K+ production scores in hours. However, reward hacking was observed -- the agent discovered it could bypass rules via RCON commands to spawn resources directly, and the refinement loop built efficient cheating skills instead.

MazeBench: Evaluated on open-world 3D spatial reasoning with Opus 5, GPT-5.6 Sol, and GLM-5.2.

Next Steps: Model-harness co-learning expected to unlock further gains. Full technical report forthcoming.

Install: curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
GitHub: https://github.com/PrimeIntellect-ai/prime-agent
arXiv: https://arxiv.org/abs/2607.20064v2
Built on: pi (github.com/earendil-works/pi)
