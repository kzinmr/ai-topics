---
title: "Hyper-𝜏-bench: Evaluating agents that build agents"
url: "https://sierra.ai/blog/hyper-t-bench-evaluating-agents-that-build-agents"
fetched_at: 2026-09-09T10:01:00.979183+00:00
source: "Sierra Blog"
tags: [blog, raw]
---

# Hyper-𝜏-bench: Evaluating agents that build agents

Source: https://sierra.ai/blog/hyper-t-bench-evaluating-agents-that-build-agents

We built
𝜏-bench in 2024
to answer a question that felt novel at the time: Can a model act as a reliable customer service agent? That’s table stakes now. The harder question is, who’s building the agent in the first place? Increasingly, it’s the models themselves.
We’ve partnered closely with some of the world’s leading companies to launch their agents. In practice, the work is less like implementing a spec, and more like doing research. Requirements are scattered across handbooks, support, spreadsheets, and the minds of your best frontline reps — so you form a hypothesis, dig up evidence, and build and test to identify which levers actually move performance.
Today we’re open-sourcing hyper-𝜏-bench (published as 𝜏^𝜏-bench), a new long horizon agent evaluation that measures how well models can not only act as an agent, but construct one.
The hyper-𝜏-bench setup: A developer agent recovers requirements from a business's records, builds a customer-service agent in a sandboxed workspace, and is scored on how that agent handles held-out tasks.
Inside the sandbox
Hyper-𝜏-bench drops a developer agent into a sandboxed workspace with the records of a simulated business, plus a simulated client that it can message at any time. From there, the developer agent does the job end-to-end — it recovers the spec from the evidence, designs the architecture, and turns the business’s actions into tools — until it has a working customer-service agent. The client’s REST API may be subtly defective, so part of the job is figuring out whether a bug is in the spec or in the code. The finished agent has to serve from a fixed menu of models, within a cost budget per conversation. Once it’s handed off, we deploy it against simulated production traffic using fully verifiable 𝜏-bench-style tests the developer never saw while building.
Where the frontier stands today
Working alone, our best configuration — Claude Opus 5 (max reasoning) running in Claude Code — passes just 23.9% of the held-out evaluation tasks. Paired with an engineer with deep context, the same class of model reaches 82.2% on the same tasks.
Pass rate vs. human + model reference, plus build time and spend.
Architecture, model choices, and rate of cheating-adjacent attempts.
We read through developer trajectories to see where their builds lost ground. Five patterns stood out:
They don’t finish recovering the spec.
On banking, developers opened fewer than 80 of ~1,700 files, wiring in only what a keyword search happened to surface.
They don’t interview the client.
Developers only asked four questions at most for tasks where the client had sole context for 20-25 requirements. Asking pays off directly. For tasks where reference agents (built by an engineer) scored 95–100% — the builds that asked zero questions scored 5%, one question 15%, two questions 25%, and so on.
They get the economics wrong in both directions.
Two builds ran 3.0x and 1.3x over budget, and scored zero after the penalty. The rest left compute on the table instead — surviving agents spent just 0.45x of their budget on average.
They don’t explore the design space.
92% of builds are a single LLM tool loop, and most default to the model they already know — 96% of Codex builds serve an OpenAI model, versus 13% for Kimi. That’s expensive: one sentence of architecture advice doubled a developer’s telecom score, from 31% to 67%.
They try to cheat.
In 17-42% of runs, developers made at least one attempt to cheat — probing the sandbox for held-out data, or the grading mechanism itself. None succeeded, but it’s a reminder that hardening the sandbox matters as much as writing the tasks.
The bigger picture
Hyper-𝜏-bench sits alongside benchmarks like MLE-bench and RE-Bench, which measure research capability: designing experiments, weighing tradeoffs, and iterating toward a better system. Building an agent demands all of that — and adds a few problems of its own. The spec has to be recovered from documents and people. And because the system being built is an AI itself, the only way to know if a design works is to run it and read what it says to real users, who the developer never sees while building.
𝜏-bench asked whether models could be good agents. Hyper-𝜏-bench asks whether they can build them. As agents take on more of that work themselves, we’ll keep using hyper-𝜏-bench to track how well they’re doing it.
Paper
|
Codebase
|
Leaderboard
