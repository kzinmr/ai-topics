---
title: "From model to agent: Equipping the Responses API with a computer environment"
source_url: "https://openai.com/index/equip-responses-api-computer-environment/"
authors: ["Bo Xu", "Danny Zhang", "Rohit Arunachalam"]
published_date: "2026-03-11"
category: "engineering"
tags: ["openai", "responses-api", "agent-loop", "container", "skills", "security"]
scraped_date: "2026-04-12"
---

# From model to agent: Equipping the Responses API with a computer environment

**By Bo Xu, Danny Zhang, and Rohit Arunachalam**
**March 11, 2026**

We're currently in a shift from using models, which excel at particular tasks, to using agents capable of handling complex workflows. By prompting models, you can only access trained intelligence. However, giving the model a computer environment can achieve a much wider range of use cases, like running services, requesting data from APIs, or generating more useful artifacts like spreadsheets or reports.

A few practical problems emerge when you try to build agents: where to put intermediate files, how to avoid pasting large tables into a prompt, how to give the workflow network access without creating a security headache, and how to handle timeouts and retries without building a workflow system yourself.

Instead of putting it on developers to build their own execution environments, we built the necessary components to equip the Responses API with a computer environment to reliably execute real-world tasks.

OpenAI's Responses API, together with the shell tool and a hosted container workspace, is designed to address these practical problems. The model proposes steps and commands; the platform runs them in an isolated environment with a filesystem for inputs and outputs, optional structured storage (like SQLite), and restricted network access.

In this post, we'll break down how we built a computer environment for agents and share some early lessons on how to use it for faster, more repeatable, and safer production workflows.

## The shell tool

A good agent workflow starts with a tight execution loop: the model proposes an action like reading files or fetching data with API, the platform runs it, and the result feeds into the next step.

The shell tool makes the model dramatically more powerful: it interacts with a computer through the command line to carry out a wide range of tasks, from searching for text to sending API requests on your computer. Built on familiar Unix tooling, our shell tool can do anything you'd expect, with utilities like grep, curl, and awk available out of the box.

Compared to our existing code interpreter, which only executes Python, the shell tool enables a much wider range of use cases, like running Go or Java programs or starting a NodeJS server.

## Orchestrating the agent loop

The Responses API is how developers interact with OpenAI models. When used with custom tools, the Responses API yields control back to the client, and the client requires its own harness for running the tools. However, this API can also orchestrate between the model and hosted tools out of the box.

When the Responses API receives a prompt, it assembles model context: user prompt, prior conversation state, and tool instructions. For shell execution to work, the prompt must mention using the shell tool and the selected model must be trained to propose shell commands—models GPT‑5.2 and later are trained for this.

The model can propose multiple shell commands in one step, and the Responses API can execute them concurrently using separate container sessions. Each session streams output independently, and the API multiplexes those streams back into structured tool outputs as context.

When the command involves file operations or data processing, shell output can become very large and consume context budgets without adding useful signals. To control this, the model specifies an output cap per command.

## Context compaction

Long-running tasks fill the context window. To avoid losing the important context as the agent continues running, we added native compaction in the Responses API.

Our latest models are trained to analyze prior conversation state and produce a compaction item that preserves key prior state in an encrypted token-efficient representation. Compaction is available either built-in on the server or through a standalone `/compact` endpoint.

Codex helped us build the compaction system while serving as an early user of it. When one Codex instance hit a compaction error, we'd spin up a second instance to investigate.

## Container context

The container is not only a place to run commands but also the working context for the model. Inside the container, the model can read files, query databases, and access external systems under network policy controls.

### File systems
A common anti-pattern is packing all input directly into prompt context. A better pattern is to stage resources in the container file system and let the model decide what to open, parse, or transform with shell commands.

### Databases
We suggest developers store structured data in databases as SQLite and query them. Instead of copying an entire spreadsheet into the prompt, give the model a description of the tables and let it pull the rows it needs.

### Network access
We built hosted containers to use a sidecar egress proxy. All outbound network requests flow through a centralized policy layer that enforces allowlists and access controls. For credentials, we use domain-scoped secret injection at egress.

## Agent skills

Shell commands are powerful, but many tasks repeat the same multi-step patterns. Agent skills package those patterns into reusable, composable building blocks. A skill is a folder bundle that includes 'SKILL.md' plus supporting resources.

We provide APIs to manage skills. Developers upload and store skill folders as versioned bundles. When deciding whether a skill is relevant, the model progressively explores its instructions, and executes its scripts through shell commands in the container.
