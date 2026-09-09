---
source_url: https://sierra.ai/blog/hyper-t-bench-evaluating-agents-that-build-agents
ingested: 2026-09-09
sha256: 07c2673d5e44a379edc22a7f6b0f91cf67123708503d8b102dcc3a3bcb6a4deb
---

 Today we're open-sourcing hyper-𝜏-bench (published as 𝜏^𝜏-bench), a new long horizon agent evaluation that measures how well models can not only act as an agent, but construct one.

 The hyper-𝜏-bench setup: A developer agent recovers requirements from a business's records, builds a customer-service agent in a sandboxed workspace, and is scored on how that agent handles held-out tasks.
 Inside the sandbox
 A candidate response on a hyper-𝜏-bench task - one of many agent responses the developer builds and iterates over dozens of turns of tool feedback.

# The harder question: who builds the agent?

 We built 𝜏-bench in 2024 to answer a question that felt novel at the time: Can a model act as a reliable customer service agent? That's table stakes now. The harder question is, who's building the agent in the first place? Increasingly, it's the models themselves.
 We've partnered closely with some of the world's leading companies to launch their agents. In practice, the work is less like implementing a spec, and more like doing research. Requirements are scattered across handbooks, support, spreadsheets, and the minds of your best frontline reps — so you form a hypothesis, dig up evidence, and build and test to identify which levers actually move performance.
 That's what we wanted to measure. Existing benchmarks like SWE-Lancer and Humanity's Last Exam test coding and general knowledge respectively, but neither of them captures what it takes to build an agent: recovering a natural language specification from context, then iterating on it across many turns.

# How it works

 We start with a roleplay domain: a business with its own products, policies, and edge cases, alongside the documents that describe them. A developer model is given those documents and asked to build an agent that can serve that business's customers.
 From there it's a long horizon task. The developer mines the documents for the spec, writes the agent, and runs it against simulated customers, tool feedback that describes how the agent behaved but that the developer never sees the conversations themselves. The developer revises, re-runs, and iterates dozens of times before its submission is scored on held-out data.

 We chose to make this a multi-turn task on purpose. A single shot is a coding eval, and it misses the part that matters most in practice: reading what your own agent said and deciding what to change.

# Results

 They try to cheat. In 17-42% of runs, developers made at least one attempt to cheat — probing the sandbox for held-out data, or the grading mechanism itself. None succeeded, but it's a reminder that hardening the sandbox matters as much as writing the tasks.

# The bigger picture

 Hyper-𝜏-bench sits alongside benchmarks like MLE-bench and RE-Bench, which measure research capability: designing experiments, weighing tradeoffs, and iterating toward a better system. Building an agent demands all of that — and adds a few problems of its own. The spec has to be recovered from documents and people. And because the system being built is an AI itself, the only way to know if a design works is to run it and read what it says to real users, who the developer never sees while building.
 𝜏-bench asked whether models could be good agents. Hyper-𝜏-bench asks whether they can build them. As agents take on more of that work themselves, we'll keep using hyper-𝜏-bench to track how well they're doing it.

 Paper | Codebase | Leaderboard
