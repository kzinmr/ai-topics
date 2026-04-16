---
title: "Jason Liu on Sandboxes in the Agents SDK"
source: https://x.com/jxnlco/status/2044469127696556153
published: 2026-04
scraped: 2026-04-16
tags: [article, x-thread, jason-liu, openai, agents-sdk, sandbox, harness, compute]
---

# Jason Liu: Sandboxes Are Coming to the Agents SDK

## "In Distribution" — What It Means

Jason Liu argues that OpenAI's Agents SDK additions (sandbox, shell, compaction, memory) are significant because they put capabilities **"in distribution"** for the model.

### Structured Outputs Analogy

- Before function calling, developers had to "beg for JSON" using prompt tricks (`<json>` tags, XML, examples).
- Function calling gave models a native interface for structured data — no more tricks.
- Similarly, built-in tools (shell, compaction, memory) are now **in distribution** — the model already understands their shape from training.

### Shell Tool Naming Matters

- Naming a tool `bash` vs `shell` vs `run_command` actually affects model performance.
- OpenAI's built-in `shell` capability leverages the model's pre-existing understanding of shell interfaces.
- The point is not just convenience — the model already knows how to use shell tools effectively.

### Compaction and Prompt Caching

- Compaction is not a prompt trick — it's a real path in the harness, reinforced into the model's training distribution.
- Long-running agents need to carry state forward without replaying the whole conversation.
- Prompt caching improves price/performance for long tasks — it's not just about fitting more into context, it's about making work cheaper, faster, and less brittle.

> "By using an in-distribution harness, you can see where the puck is going with us, rather than having to chase it from behind."

## "Everything is Computer" — But Not Every Task Needs One

### Why Separate Orchestration from Compute

- Some tasks are lightweight (thinking, planning) — no sandbox needed.
- Some tasks need files, processes, browsers, credentials, or persistent state — sandbox required.
- Separating orchestration (harness/brain) from compute (sandbox/hands) lets you provision the right amount of resources for each task.
- Security: model-generated code runs in a separate sandbox, reducing risk of credential leakage on the orchestration machine.

> "We effectively separate the brain and the hands. You can think without turning the laptop on every time."

### Isolation and Security

- Agent code execution is not theoretical anymore — agents can read files, run commands, install packages, open browsers.
- The execution boundary becomes part of the product.
- You don't want that boundary to be an accident of whatever machine happened to run the agent loop.
- Some tasks need no sandbox. Some need one small workspace. Some need many isolated workspaces.
- The harness decides what needs compute; the sandbox defines what that compute is allowed to touch.

## Applications of Sandboxes

### 1. Code Generation for Pull Requests, Migrations, Vibe Coding

- Agent works inside the repo instead of describing changes from outside.
- Real checkout, shell/filesystem tools, validation commands, resumable workspace.
- Sample prompt: *"Read AGENTS.md, make the smallest safe change, run tests, and prepare a PR summary."*

### 2. Data Room Extraction

- Mount PDFs, spreadsheets, contracts, filings → turn into memos, evidence tables, workbooks, risk registers.
- Workspace can mount S3, GCS, Azure Blob Storage, or Cloudflare R2.
- Sample prompt: *"Read everything in data-room/. Create output/customers.xlsx with two tabs: Contracts and Risks."*

### 3. Creating Artifacts (PDFs, Spreadsheets, Decks)

- Agent output can be spreadsheets, PDFs, datasets, charts, reports, PowerPoints.
- Skills make these outputs more reliable.
- Sample prompt: *"Use the Slidev skill to turn brief.md and figures/ into a short investor update deck."*

### 4. Computer Use and Browser Use for Debugging

- Sandbox exposes ports → agent can build apps, serve them, open in browser, click around, take screenshots, fix issues.
- Sample prompt: *"Fill out the form, upload files from attachments/, stop if anything ambiguous, then call mark_task_done."*

### 5. Autonomous Research (Including GPUs)

- Sandbox holds data, scripts, logs, evaluation outputs, durable run ledgers.
- Compaction, memory, resumability keep work alive across fan-out, pause, continue cycles.
- Sample prompt: *"Run a parameter-golf search over experiments/. Fan out GPU-backed candidates, write every attempt to runs/ledger.csv."*

## Key Takeaway

> "Use the Agents SDK because it helps you build toward where agents are going, not where they are today. Build something that might not 100% work today and in five or six months, not only might that agent work, it might work well, because the capabilities underneath it keep getting better."

The benefits come from:
1. **Separating harness from execution** — clean architectural boundary
2. **Investing in sandbox infrastructure** — durable, resumable workspaces
3. **Using a harness that is in distribution to the models** — leveraging what models are trained on

> "That's why I keep coming back to the work you want to deliver, not just how the work gets done. If you build ambitiously, we will do our best to meet you where you are and help take you to where we all need to be."
