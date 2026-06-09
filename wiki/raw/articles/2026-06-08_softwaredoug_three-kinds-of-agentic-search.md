---
title: "Three kinds of agentic search"
author: Doug Turnbull
date: 2026-06-08
source_url: https://softwaredoug.com/blog/2026/06/08/three-kinds-of-agentic-search
domain: softwaredoug.com
type: article
tags:
  - search
  - ai-agents
  - agentic-search
  - methodology
---

# Three kinds of agentic search

I've been thinking a lot about how agents will change search. Not just LLMs summarizing results, but genuinely autonomous systems that search, reason, and act. There are three distinct paradigms emerging, and understanding the differences matters for anyone building search systems.

## 1. Agent-Assisted Search

This is the most familiar pattern. A user types a query, and an agent helps refine, expand, or disambiguate it before passing it to a traditional search engine. Think of it as search with a really smart autocomplete.

The agent might:
- Ask clarifying questions ("Do you mean Python the language or the snake?")
- Decompose a complex query into multiple sub-queries
- Add context from the conversation history
- Reformulate natural language into structured queries

The search engine itself doesn't change. The index, ranking algorithm, and retrieval pipeline stay the same. The agent is a wrapper that improves the *query* side of the equation.

This is where most "AI search" products are today. It's valuable but incremental. You're still fundamentally doing keyword/BM25/vector retrieval and showing ten blue links (or their modern equivalent).

## 2. Agent-Driven Search

Here things get more interesting. The agent doesn't just reformulate queries—it decides *what* to search, *when* to search, and *how* to search. It might:
- Search multiple sources in sequence, using results from one to inform the next
- Decide that a search isn't needed at all and reason from existing context
- Mix search with computation, code execution, or API calls
- Maintain a working memory and iteratively refine its search strategy

The key difference: the agent has *agency* over the search process. It's not a linear "query → results → answer" pipeline. It's a loop: "think → decide whether to search → search → observe → think again."

This is what systems like Perplexity's research mode and Google's AI Overviews are moving toward. The agent orchestrates multiple retrieval steps to build a comprehensive answer.

The challenge here is **search quality becomes agent quality**. A bad agent with a great search engine will produce worse results than a great agent with a mediocre search engine. The reasoning loop matters more than the retrieval precision.

## 3. Agent-Native Search

This is the paradigm shift. In agent-native search, the search infrastructure is *designed from the ground up* for agent consumption, not human consumption.

What does this mean in practice?
- **Structured, machine-readable results** instead of HTML pages designed for human eyes
- **APIs over scraping**—sources expose their data in formats optimized for programmatic access
- **Semantic indexing** where the unit of retrieval is a fact or claim, not a document
- **Provenance tracking** so agents can evaluate source reliability and cite precisely
- **Composable search primitives**—agents can mix vector search, graph traversal, SQL queries, and web search in a single workflow

In this world, "search results" aren't ten blue links. They're structured knowledge packets with confidence scores, source metadata, and semantic relationships.

We're barely at the beginning of this. Most of the web is still optimized for human eyeballs. But the economics are shifting. If 30% of your traffic comes from agents (and it will), you'll start optimizing for agents the way you optimized for Google's crawler.

## Why the distinction matters

If you're building search systems, your architecture choices depend heavily on which paradigm you're targeting:
- **Agent-assisted**: Invest in query understanding. Your retrieval pipeline is fine.
- **Agent-driven**: Invest in orchestration. You need fast, composable retrieval primitives and good monitoring of multi-step retrieval chains.
- **Agent-native**: Invest in your data layer. Structure your content for machines. Build APIs. Track provenance.

The dirty secret is that most organizations will need all three simultaneously. Your search system will serve humans directly (traditional search), humans through agents (agent-assisted), agents on behalf of humans (agent-driven), and autonomous agents making decisions (agent-native).

The companies that win will be the ones that recognize these aren't just "search with AI sprinkled on top." They're fundamentally different interaction patterns that require different infrastructure, different quality metrics, and different product thinking.

Start with agent-assisted. It's the easiest win. But start *planning* for agent-native now, because the web of 2028 will look very different from the web of 2024.
