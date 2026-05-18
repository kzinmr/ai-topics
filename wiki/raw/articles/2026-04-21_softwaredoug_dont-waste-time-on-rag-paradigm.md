---
title: "Don't waste too much time on the original RAG paradigm"
author: Doug Turnbull (@softwaredoug)
date: 2026-04-21
source: linkedin
url: https://www.linkedin.com/posts/softwaredoug_dont-waste-too-much-time-on-the-original-share-7452177290798686208-HRC-
platform: LinkedIn
type: social-media-post
---

# Don't waste too much time on the original RAG paradigm. AI has moved on

Originally in RAG, complexity lived in retrieval. With agentic search, it's accruing in the agent+harness leaving us to wonder if we even need complex retrievers?

Problem after problem, RAG began to resemble exactly what we've built for decades. Query understanding / routing on ingress, use of different retrieval strategies to find candidates (i.e., lexical, embedding, etc.). Then combine+rerank results. Aggregate some statistics. Append results to the LLM's context.

A big "thicc daddy" search system. Like what we've always built. We're unwinding that now to let an agent search using the parts.

It began with the structured attributes. With those we could perform query understanding through the LLM reliably. LLMs could speak in schema.

Then agents added tool calling — the agent could know it was searching, not just force-fed context relevant to the prompt. With a structured schema agents could filter to vocabulary + language familiar to our users.

Then agents could reason. The agent could reflect on search results, realize they're irrelevant, analyze patterns, and search again. Exhaustively iterating until better results were found. With this, agents get by with dumb retrievers. People legitimately wonder if we need that complexity. Do we literally just let an LLM drive a BM25 retriever? Or grep? Why chunk and embed when an LLM knows all about the "semantics" of your query?

Increasingly today it's about the scaffold+tools that push agents closer to what's relevant. Agentic skills to help an agent plan how to use simple search tools to find what's relevant. We're getting models like SID-1 that speed up the search reasoning loop. And tools like semantic grep to make the "simple retriever" waste fewer tokens.

I wouldn't start RAG today assuming you need the classic RAG embedding+chunking paradigm. I'd focus on tools that deliver needed context. The dumbest thing that can work, with simplest possible data system. Start simple and improve when tools can't deliver context. But absolutely do not overbuild until you have data that points where an agent cannot cope.

---

## Notable Comments

**Emaline Gayhart**: Wouldn't giving agents "dumb retrievers" be inefficient and result in them needing to do more tool calls anyways? BM25 is built in with ES (assuming you're using ES), what does it hurt to utilize it, or hybrid search, and give the agent more relevant results to reason with?

**Leo (Leonid) Boytsov**: There's evidence that the value of core retrieval is still high. [Link to X post](https://x.com/i/status/2042365770672345145)

**Jeremy Pickens**: But of what use is agentic search if users won't enter queries longer than 2.3 keywords with which to seed the agent or otherwise describe their information need? The web giants have told us for twenty years that users not wanting to enter long queries is not a function of a poor search system not supporting those queries. It's a function of human nature. Of the users themselves. If that is changing, if users are willing to explicitly enter more information given the right system, then maybe they're also willing to do other kinds of activities, such as evaluation of and giving feedback on results, so as to steer the search system. And the more they do that, the more they themselves become... agents. Like, human agents. Is the future of agentic search... human agency?

**Doug Turnbull** (reply to Emaline): I'd say this. If you wanted to try agentic search in an existing app, what's the fastest path to value? Start with a simple tool connecting to your ES. Get the agent+harness to identify and provide context from different backends. Once you see "here the agent can't do X" you at least have a user-driven roadmap for what you need to evolve. It moves you from where you're overbuilding to solve a problem you don't have, to building what you know users actually need.
