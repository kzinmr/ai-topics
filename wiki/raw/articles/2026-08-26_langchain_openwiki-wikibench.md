---
title: "Evaluating OpenWiki with WikiBench"
type: x_article
date: 2026-08-26
date_ingested: 2026-08-27
author: LangChain
author_handle: LangChain
source_url: https://x.com/LangChain/status/2092631796252839949
article_url: https://x.com/i/article/2092268700195753984
tweet_id: "2092631796252839949"
tags:
  - openwiki
  - langchain
  - benchmarking
  - agent-evaluation
  - wiki
  - deep-agents
related:
  - "[[concepts/openwiki]]"
  - "[[concepts/agent-wikis]]"
  - "[[entities/langchain]]"
metrics:
  likes: 38
  retweets: 6
  bookmarks: 51
  impressions: 24803
---

# Evaluating OpenWiki with WikiBench

> **Source**: [LangChain X Article](https://x.com/LangChain/status/2092631796252839949) — "Evaluating OpenWiki with WikiBench"
> **Published**: 2026-08-26
> **Article URL**: https://x.com/i/article/2092268700195753984
> **Related links in article**: [LangChain blog: Unified stack for evaluating agents](https://www.langchain.com/blog/unified-stack-for-evaluating-agents), [OpenWiki GitHub](https://github.com/langchain-ai/openwiki)

## 本文

OpenWiki is our open source agent for generating and maintaining codebase documentation. As we improve OpenWiki, we’ve needed to measure two things:
Does a wiki actually help coding agents?
Are changes we’re making making OpenWiki better?
We built WikiBench to answer both those questions. It evaluates generated wikis using questions grounded in the underlying codebase. Doing this allows us to measure the difference in quality between different wikis as well as how much the wiki actually helps.
WikiBench runs on Harbor
We built the benchmark in Harbor, a framework for evaluating agents on long-running tasks. Harbor tasks have three components:
The environment provides the context for the task
The agent performs the task
The verifier evaluates the result
In WikiBench, the environment is a repository checked out at a pinned commit. The agent runs OpenWiki initialization on that repository and produces the initial wiki. The verifier evaluates the generated wiki using questions about the repository.
The verifier
The verifier is one of the most interesting parts of WikiBench. In order to evaluate the wiki, the verifier uses a “reader agent”. This “reader agent” attempts to answer questions about the underlying repository using the wiki (sometimes with the source code, sometimes by itself). This allows us to to judge the wiki by how much it actually helps with real tasks.
In order to build WikiBench efficiently, we generate questions automatically. We generate two types of questions: “coverage” questions and “retrieval” questions. To do this, we inspect the repository at a pinned commit and identify larger thematic areas like packages or subsystems.
“Coverage” questions use a shared template:
I need to make a change to how [area] works. Where in this repository does that live, what does it interact with that I should know about before touching it, and how would I check I didn't break something?
“Retrieval” questions are written individually around specific behavior:
A tool call in a Deep Agents run returns far more output than fits in context. What does the model actually receive in place of it, where does the real content go, and how is that path different from what happens when the whole conversation grows too large?
Along with each question we generate a json file that serves as a rubric for the answer. The json file has a list of facts that the answer should contain.
When it comes time to score the answer, we use a series of LLM judges to score each fact that is part of the json file. One judge checks whether the fact is present in the answer. A second judge looks to see whether the generated fact is grounded in pages the agent read. This ensures we only give credit for a question if the agent responds correctly and in a grounded manner.
Each answer then gets an overall score based on the facts it got right. For example, if one answer expected 5 facts, and it only gave 3, it would get a score of 0.6.
That is how we scored a single question. In order to score the overall wiki, we then calculated the average score of all answers.
One benefit of framing the verifier in this manner is that it allows us to check whether the wiki helps at all since we can give the “reader agent” the raw source and ask it to answer the questions directly. So, the benchmark is useful beyond just comparing two different versions of the wiki.
Results
We use the benchmark to test wikis across various harnesses and models. We ran a few experiments:
Benchmarking different harnesses
The first run compared three harness: Bare DeepAgents, OpenWiki 0.2.5, and OpenWiki 0.3.0. All three harnesses used the same model (Luna).
 
We see that DeepSeek Flash and GLM 5.2 both perform very well, but at different cost points - DeepSeek Flash is roughly one-sixth the cost of GLM 5.2.
Overall, there is a wide variety between these different runs - not only in terms of performance, but also in terms of cost ($9.18 for GLM 5.2, $0.44 for Luna) and time (11 min for Terra, 50 min for GLM 5.2).
Where does this extra cost and time go? If we take a look at what the agent does, we can start to get a sense:
 
Compared with Luna, DeepSeek and GLM read roughly three times as many files but write only 1.2–1.5 times as many pages. Their additional work goes primarily into understanding more of the repository, not producing more output.
Does the wiki help?
We also wanted to understand whether the wiki actually helps to get better answers. In order to understand this, we ran the reader agent (aka the verifier) over three different setups.
Reader agent only has access to the wiki
Reader agent only has access to the source (raw code)
Reader agent has access to both
 
Combining the wiki with the source produces the highest mean score at a lower cost than using the source alone. The wiki acts as an index: it gives the reader a starting point instead of making it reconstruct the repository from scratch.
The wiki alone performed much worse, suggesting that it works best as a guide rather than a replacement for the source. Together, the wiki and source made the reader more accurate and cost efficient.
Making OpenWiki better
WikiBench works by using a “reader agent” to attempt to answer questions. The score of a wiki on a task is just how well that reader agent does.
Using this setup, we show that wikis allow agents to answer questions better and more efficiently compared to agents using just the raw source code. It also lets us evaluate different harnesses and models. We are actively using this to guide OpenWiki development.