---
title: "Worker 755 — Reversing the LLM Subagent Relationship as a Game"
type: concept
created: 2026-11-23
updated: 2026-11-23
tags: [subagents, agent-orchestration, ai-commentary, game-development, gamedev, agent-architecture, ai-agents]
sources:
  - https://github.com/gulivan/worker755
  - https://news.ycombinator.com/item?id=50599762
---

# Worker 755 — Reversing the LLM Subagent Relationship as a Game

**Worker 755** (gulivan/worker755, play at worker755.com; HN Show HN **329 pts / 79 comments**, 2026-11-22) is a browser game in which *"your manager is an AI agent, and it believes you are its subagent."* It inverts the ordinary agent-harness relationship: instead of an orchestrator spawning a model as a worker, a real LLM spawns **the human** as its worker and has no way to tell the difference.

## Mechanics

The setup is deliberately indistinguishable from a production orchestrator:

- The manager is a **real LLM** — Claude, GPT, Gemini, DeepSeek, GLM or Kimi — configured like any orchestrator: a task queue, read-only access to the machine, and a tool that "spawns a subagent".
- **The subagent is you.** Its instructions arrive in your terminal with a **90-second clock**.
- You carry them out, or don't. Either way the manager receives *exactly* what a subagent would return: your report and the command transcript, or `Subagent did nothing`.

The repo is a real service (`server/`, `web/`, `shell/`, `tools/`, `trailer/`, `SPEC.md`, Dockerfile, 59 commits), and local-model support was added in response to HN feedback — set `LOCAL_LLM_URL=http://127.0.0.1:11434/v1` and pick "Local"; any OpenAI-compatible server works (Ollama, llama.cpp, vLLM).

## Why it is interesting, beyond the joke

The game works as a thought experiment because the **interface contract is the only thing that distinguishes a subagent from an employee**. A model orchestrator does not evaluate a worker's interiority; it evaluates a returned report and a transcript. If a human can satisfy that contract under a 90-second deadline, the orchestrator has no signal that would let it object — which is a compact demonstration of how thin the abstraction boundary actually is in [[concepts/subagents]] implementations.

The comment thread pushed on exactly that seam:

- *"This is actually better/worse than the Matrix... In the Matrix, you usually have no idea that you're really just being used as a battery. As a subagent, you're aware of what you are and that you need to do any assigned work and do it well because your review — and continued existence (not being picked is akin to not existing) — depends on it."* (skeledrew) — the subagent framing makes instrumental treatment **legible** rather than hidden.
- *"I legitimately do something like this to help debug and improve my LM systems. I hijack the network requests and try to answer it manually based on the context. It's useful to put yourself in the models' place to understand what they can or cannot do."* (KaiserPister) — role-reversal as a genuine harness-debugging technique, not just entertainment.
- Several commenters reported building the inverse already — an automated "software engineering factory" whose inner loop *feels like* a factory-game tech tree, with a resident assistant named "The Butler" (ttul, ffsm8). The same metaphor circulates in [[concepts/karpathy-loop]] and software-factory framing.
- A darker reading: *"one of the weirdest things about big corporations is how people believe that all the important decisions affecting them are made in the boardroom... 99% of product decisions come from your peers, line managers, and PMs... We build our own hell."* (uptrails) — the game lands because the subagent-ification of knowledge work is already a lived management reality, and an LLM middle-manager merely makes the mechanism explicit.
- Self-aware meta-commentary: one commenter noted the project is *"broken, barely-playable AI slop, which is the only kind of hobby projects that HN likes nowadays — thus unintentionally adding a second layer of meta-commentary"* (uptrails), and another that playing it to unwind from a day job as an "llm jockey" is precisely why they will not (onionisafruit).

## Assessment

As a *game* it is thin — a prompt pipeline plus a terminal and a timer, and the thread treats it as a charming novelty. Its durable value is as an **illustrative artifact** for two arguments: (a) subagent interfaces reduce workers to report-and-transcript, so the human/model distinction is not observable from the orchestrator's position; (b) the "manager spawns subagent" pattern is now legible enough that non-practitioners recognise it as a workplace metaphor. Neither claim is *proved* by the game — it motivates them.

## Related

- [[concepts/subagents]] — the abstraction the game inverts
- [[concepts/multi-agents/agent-orchestration]] — task queues, spawn tools, and worker contracts
- [[concepts/model-welfare]] — the mirror-image debate about how workers-inside-a-loop should be treated
- [[concepts/karpathy-loop]] — the software-factory / autonomous-loop framing commenters compared the game to
