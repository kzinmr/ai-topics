---
title: "The State of Agent Wikis"
type: x_article
source: https://x.com/mem0ai/status/2079585032587694582
author: mem0
date_published: 2026-07-21
date_ingested: 2026-07-22
tags:
  - agent-wiki
  - llm-wiki
  - memory-systems
  - knowledge-management
  - survey
metrics:
  likes: 493
  retweets: 48
  bookmarks: 996
  impressions: 42195
---

# The State of Agent Wikis

In April 2026, Andrej Karpathy published a GitHub Gist describing a pattern he called the LLM Wiki.
In the months since, four different teams have shipped the same idea without coordinating: @cognition built DeepWiki, @FactoryAI built AutoWiki, @Langchain open-sourced OpenWiki, and Garry Tan open-sourced GBrain. Different companies, different users, one architecture.

An LLM reads a body of sources, compiles them into a maintained set of markdown pages, and keeps those pages current as the sources change. Agents then read the pages instead of re-deriving everything from raw material on every question.

The pattern has become a category, and the systems built on it are increasingly just called agent wikis.

## The idea: compile at ingest, not at query

Start with the problem, because the pattern is a direct answer to it.

The default way to give a model a body of knowledge is retrieval. You upload documents, chunk and embed them, and at query time you fetch the relevant chunks and answer. It works, and it has a structural flaw: nothing accumulates. Every question starts from raw chunks, so the model re-derives the same understanding again and again, and the tenth question about a codebase is no cheaper or better informed than the first.

The LLM Wiki inverts when the synthesis happens. Instead of assembling knowledge at query time from raw pieces, an LLM assembles it once at ingest time into durable pages, then maintains them. When a new source arrives, the model reads it, updates the entity pages it touches, revises summaries, and flags contradictions with what was already written.

RAG re-derives knowledge on every question. A wiki derives it once and then keeps it current. Both are legitimate; they differ in when you pay the synthesis cost and whether the result survives.

The architecture is consistently three layers. Raw sources are immutable: articles, papers, repositories, data. The model reads them and never edits them. The wiki is LLM-generated markdown the model owns entirely: summaries, entity pages, concept pages, cross-references. The schema is a configuration file (CLAUDE.md, AGENTS.md, or similar) that tells the model how the wiki is organized and what workflows to run, which is what makes it a disciplined maintainer rather than a chatbot with file access.

Three operations run on top: ingest a source and file it across the pages it affects, query the wiki (and optionally file good answers back as new pages, so exploration compounds too), and lint, a periodic pass hunting contradictions, stale claims, and orphaned pages.

## Why it works: the bottleneck was never the writing

Human wikis rot, and the reason is specific. The hard part was never reading the sources or having the insight. It was the bookkeeping: updating cross-references, keeping summaries current, reconciling a new document against forty existing pages. That work is unbounded, unglamorous, and the first thing a busy team drops. So the wiki decays, people stop trusting it, and it dies.

That is precisely the work a language model does not mind. It does not get bored, it does not forget to update a cross-reference, and it can touch fifteen files in one pass. The LLM Wiki works because it removes the maintenance cost that killed every wiki before it.

The idea is older than the tooling. Vannevar Bush described the Memex in 1945: a curated personal store of documents with associative trails between them. Bush's unsolved problem was who maintains the trails. The answer, eighty years later, is the model.

## Where the pattern got its name

Karpathy's gist is worth reading directly. His complaint about ordinary document workflows: "the LLM is rediscovering knowledge from scratch on every question. There's no accumulation." His alternative was to compile instead of retrieve, so that "the knowledge is compiled once and then kept current, not re-derived on every query," producing what he called "a persistent, compounding artifact."

Crucially, you do not write it. "You never (or rarely) write the wiki yourself, the LLM writes and maintains all of it." His own setup was the agent on one side and Obsidian on the other: "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

Scale specificity: "works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure." Past that, it recommends adding search, specifically qmd, described as "a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking."

## What the labs actually built

### Cognition: DeepWiki — the wiki as a public utility

Cognition pointed the pattern at every public repository on GitHub. Swap github.com for deepwiki.com in any public repo URL and you get a generated, navigable wiki of that codebase: architecture overview, file index, dependency graph, and search, with links back to source.

Two things stand out. The scale is real: over 50,000 of the top public repositories are already indexed, from MCP to LangChain. And the wiki is not the product's endpoint, it is retrieval infrastructure for the agent. Devin uses the wiki to locate relevant context in a codebase, so DeepWiki is the compiled layer that makes Devin's code search better grounded.

### Factory: AutoWiki — documentation as a build artifact

Factory framed the same pattern in CI terms: documentation should be a build artifact, not a side project. It is built from source, organized around how the codebase actually works, and refreshed when the repo changes.

The generation method is the most explicitly engineered of the four. AutoWiki runs a two-pass analysis: a structural scan of README, package manifests, CI config, and entry points, then a deeper semantic scan of routes, API endpoints, service classes, database schemas, and feature flags. The work is split across specialized agents, each scoped to one facet of the repository.

Currency is handled as infrastructure rather than discipline: /wiki regenerates on demand, and /install-wiki writes a CI workflow that refreshes the wiki on every push to the default branch. For GitHub repos it syncs into the repository's own wiki tab.

### LangChain: OpenWiki — and the leap from code to everything

LangChain open-sourced OpenWiki as a CLI that writes and maintains agent documentation for a codebase, then expanded it into OpenWiki Brains with two modes: Code Brain (original repository use case) and Personal Brain (builds a wiki from your own connected sources: Gmail, Notion, git repositories, X, Hacker News, and web search).

The category jumped from "document my repo" to "compile my working life."

One design detail deserves attention because every team converged on it: the output is not prose for humans. It is structured markdown optimized for LLM context, with headings, cross-references, and summaries designed so an agent can find relevant context fast. The wiki is written for the reader that will actually read it, and that reader is a model.

### GBrain: the personal-scale open-source version

Garry Tan's GBrain applies the same shape to a personal knowledge base rather than a codebase: markdown in a git repository, a schema file, and an automatically maintained graph of entity cross-links. It is the clearest demonstration that the pattern is substrate-simple. No vector database, no service, just files a model maintains and a human can read.

### Technique Matrix

| Dimension | DeepWiki | AutoWiki | OpenWiki | GBrain |
|-----------|----------|----------|----------|--------|
| Scope | Public GitHub repos | Codebases (CI-integrated) | Code + Personal sources | Personal KB |
| Substrate | deepwiki.com | GitHub Wiki tab | Filesystem / git | git repo |
| Freshness | On demand | CI (push-triggered) | On demand | On demand |
| Output target | Devin agent | Coding agents | Coding agents | Any agent |
| Source material | GitHub repos | Code repositories | Code, email, Notion, X, HN, web | Documents |

Four teams, four corpora, one architecture: markdown in git, a schema file the model obeys, synthesis at ingest, refresh on change, and pages written for an agent to read.

## Where it stops

- **Scale.** Index-first with no embeddings is a moderate-scale technique (~100 sources). Past a few hundred pages you need hybrid BM25 and vector search.
- **Fidelity.** Compiling at ingest means an early summary can quietly lose a detail, and every later answer inherits that loss. Retrieval against raw chunks does not have this failure mode.
- **Staleness.** A compiled page is only as true as the last refresh. Factory's CI framing matters: a stale wiki is worse than no wiki.
- **Compile cost.** You pay real tokens up front to build pages you may never query.

## A wiki is not memory

One crucial distinction: these systems are increasingly described as memory. But there are two axes under one term:

1. **Corpus knowledge** — what a wiki does: compile what a set of documents or a repository says. Answers "what does this body of material contain."
2. **User and experience memory** — what a specific person prefers, what they decided last week, which approach their team already rejected. Scoped to identity, accumulates from interaction, handles contradiction and deletion per user.

A wiki is excellent at the first and does not attempt the second. That second axis is what a dedicated memory layer like Mem0 is for: memory tagged to a user_id so it follows a person across sessions, apps, and agents.

## References

- Andrej Karpathy, LLM Wiki (GitHub Gist, April 2026)
- qmd: local hybrid BM25/vector search for markdown
- Cognition, DeepWiki: AI docs for any repo
- Devin Docs, DeepWiki
- Factory, Introducing AutoWiki
- Factory Documentation, AutoWiki overview
- langchain-ai/openwiki (GitHub)
- LangChain, Wiki Memory
- garrytan/gbrain (GitHub)
- Vannevar Bush, As We May Think (The Atlantic, 1945)
