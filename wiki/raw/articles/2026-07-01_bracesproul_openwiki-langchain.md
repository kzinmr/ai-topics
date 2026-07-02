---
title: "Introducing OpenWiki, an open source agent for repo documentation"
author: Brace Sproul (@BraceSproul)
source: https://x.com/bracesproul/status/2072375136368660515
type: x-article
created: 2026-07-01
fetched: 2026-07-02
---

# Introducing OpenWiki, an open source agent for repo documentation

**Author**: Brace Sproul — Head of Applied AI at LangChain
**Published**: 2026-07-01
**Engagement**: 394 bookmarks, 69.5K impressions, 165 likes, 22 reposts

---

Today we're releasing OpenWiki, an open source agent and CLI for generating and maintaining documentation for codebases.

Agents write better code when they understand the repo they're working in. They need to know where key logic lives, how files connect, and which patterns the codebase expects. Good documentation gives agents that context, which leads to more informed code changes and fewer avoidable mistakes.

The problem is that documentation is hard to keep current. Writing the initial docs takes time, and updating them every time the code changes is even harder. In large repos with frequent PRs, docs can fall out of date quickly.

OpenWiki handles that work automatically. It creates a wiki for your repo, connects that wiki to your coding agent, and keeps it updated as your code changes.

## Why wikis for agents

We were inspired by existing work around codebase wikis, including DeepWiki, AutoWiki, and Karpathy's LLM Wiki concept. The shared idea is simple. A wiki gives humans and agents a structured way to understand a codebase without forcing all context into one giant file.

That matters because most coding agents already read files like `AGENTS.md` or `CLAUDE.md` for instructions. Those files are useful, but they're not the right place to store hundreds of pages of repo documentation. They should point the agent toward the right context, then let the agent retrieve what it needs.

OpenWiki follows that model. It generates a repo wiki, then updates your agent instruction files with a reference to that wiki. From there, your coding agent can discover and use the docs automatically.

## Getting started

OpenWiki is designed to be easy to run from the command line.

Install it with NPM:

```bash
npm install -g openwiki
```

then run:

```bash
openwiki --init
```

The init command asks for a model provider and API key, then generates documentation for your repo.

OpenWiki supports both open and closed model providers, including OpenRouter, Fireworks, Baseten, OpenAI, and Anthropic. By default, it uses OpenRouter with an open model, but you can configure the provider that works best for your setup.

Because OpenWiki is built on top of DeepAgents, it also supports tracing to LangSmith. If you provide a LangSmith API key, OpenWiki will trace runs to a LangSmith project so you can inspect exactly what the agent did while generating or updating your docs.

## How OpenWiki connects to your coding agent

After generating the wiki, OpenWiki updates your repo's agent instruction files. If your repo uses `AGENTS.md`, `CLAUDE.md`, or both, OpenWiki adds a reference to the generated wiki and explains when the agent should use it.

We chose this approach because putting the entire wiki inside an instruction file would add too much context. In a large repo, the wiki can span hundreds of files. Loading all of that into every agent run would be wasteful and hard to maintain.

A short reference works better. Your coding agent already reads the instruction file. Once OpenWiki adds the reference, the agent can find the wiki when it needs repo context, without requiring you to change your workflow.

## Keeping the wiki up to date

Generating docs once is useful. Keeping them current is where OpenWiki becomes more valuable.

OpenWiki includes a GitHub Action that can run on a schedule, for example once a day. The action runs OpenWiki with the update flag. OpenWiki checks which commits landed since the last run, uses git diffs to understand what changed, then updates the wiki with the relevant context.

That means the workflow can run in the background. As your codebase changes, OpenWiki updates the documentation. Your coding agent keeps picking up the latest wiki through the existing instruction file reference.

## Built for codebases first

This first release focuses on wikis for codebases. The goal is to make it easier for agents to understand the repos they work in, without asking developers to manually write and maintain detailed docs.

Over time, we think the OpenWiki concept can apply more broadly. Agents need durable context for many kinds of work, not just coding. Codebase documentation is the first use case, but the same pattern can help agents maintain useful context across other workflows too.

## Try it

OpenWiki is open source and available now.

You can install it, run `openwiki --init`, and generate a wiki for your repo in a few minutes.

- **GitHub**: https://github.com/langchain-ai/openwiki
- **Walkthrough video**: https://youtu.be/nIVu3zfYprI
- **DeepAgents docs**: https://docs.langchain.com/oss/python/deepagents/overview
- **LangSmith**: https://langsmith.com/
- **Factory wiki docs**: https://docs.factory.ai/cli/features/wiki/overview
