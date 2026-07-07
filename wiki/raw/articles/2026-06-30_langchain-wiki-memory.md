---
title: "Wiki Memory"
author: Harrison Chase (@hwchase17)
date: 2026-06-30
type: x-article
url: https://x.com/hwchase17/status/2071963622298050997
source_url: https://x.com/i/article/2071963272727928833
bookmark_count: 1114
---

# Wiki Memory

*By Harrison Chase (@hwchase17), 2026-06-30*

Memory for agents is still early, with little to no standards. "Memory" means something different to everyone. But one common pattern is emerging: wiki memory.

The idea is simple: use an agent to turn raw source data into a compact, persistent, agent-readable knowledge layer.

## Why wikis?

Raw data contains a lot of knowledge, but it is often inefficient to expose directly to an agent. Logs, notes, code, docs, experiments, Slack threads, and transcripts are too noisy and too large. So instead, we run a process over that data and transform it into a denser representation.

This is different from basic RAG. RAG usually retrieves raw chunks at query time. A wiki precomputes and maintains a higher-level synthesis, so the agent does not have to rediscover the structure every time.

This desire exists almost everywhere. When speaking to a friend at a research company, he talked about all the knowledge in their researchers' heads. He wanted to "clone their brain" so that if they left, the knowledge still remained with the company. His hope was that by looking at the experiments they ran, the notes they wrote, and the actions they took, they could approximate this "brain clone."

A wiki is one practical way to do that: not by storing everything, but by compressing what matters into a reusable knowledge base.

## What is a "wiki"?

A wiki is an agent-maintained data structure that represents source knowledge in an agent-friendly way.

In practice, this often means running an agent over some source material and asking it to create a set of files that future agents can use to understand the domain faster.

The important bit is not that it literally looks like Wikipedia. The important bit is that it is persistent, structured, inspectable, and updated over time.

## Examples of wikis

**DeepWiki by Cognition** is probably the first example of this I remember seeing. DeepWiki creates AI-generated documentation for GitHub repositories. It is intended to give humans and coding agents a higher-level mental map of a codebase, making it easier to understand and navigate.

**Karpathy** recently wrote about what he called an "LLM Wiki" or "LLM knowledge base." This is a more general form of the same pattern: instead of only working over code, it can work over arbitrary source files. His framing is that the LLM incrementally builds and maintains a persistent markdown wiki that sits between the user and the raw sources.

**Factory** launched AutoWiki as a similar offering to DeepWiki. AutoWiki analyzes a codebase and generates structured, browsable documentation that stays current as the repo changes.

This pattern also sits adjacent to memory systems like **LangMem**, **Letta**, **Mem0**, and **Zep**. Those systems attack the broader agent-memory problem, while wiki memory is notable because it often uses the simplest possible substrate: files.

## A wiki for every domain

I would argue that for every domain there exists a knowledge base you would be well served to create. This knowledge base is not just the raw data. It is an intelligently compressed version of the raw data.

There are a bunch of open questions here:

- What is the raw data?
- What is the best format for the compressed data?
- How should that data be compressed?
- How should the compressed representation stay up to date?

We are starting to see some common answers emerge:

- **What is the raw data?** → anything an agent can read or access
- **What is the best format for the compressed data?** → files
- **How do you compress that data?** → an agent
- **How do you maintain it?** → an agent

Files are attractive because they are inspectable, editable, versionable, and easy for agents to read and write.

Wikis are not all of memory. They are best for durable domain knowledge, not necessarily short-term conversation state, user preferences, or high-frequency event logs. But for many domains, wiki memory may be the simplest useful long-term memory pattern we have.

---

## Referenced URLs

- https://www.letta.com/blog/agent-memory
- https://arxiv.org/html/2504.19413v1
- https://www.getzep.com/
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- https://cognition.ai/blog/deepwiki
- https://factory.ai/news/wiki
- https://docs.langchain.com/oss/python/concepts/memory
