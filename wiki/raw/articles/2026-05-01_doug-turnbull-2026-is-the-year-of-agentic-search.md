---
title: "Why 2026 is The Year of Agentic Search — Doug Turnbull & Jo Kristian Bergum"
created: 2026-05-01
author: Doug Turnbull (@softwaredoug)
co-host: Jo Kristian Bergum (@jobergum, Vespa.ai)
source: YouTube
url: https://www.youtube.com/watch?v=h370222tnAQ
type: talk
duration: 65:52
tags: [agentic-search, llm-query-understanding, autoresearch, search-harnesses, llm-as-judge, search-engineering, softwaredoug, vespa]
---

# Talk Overview

A 65-minute fireside chat between **Doug Turnbull** (search relevance expert, author of *AI-Powered Search* and *Relevant Search*) and **Jo Kristian Bergum** (Vespa.ai) arguing that the search problems of 2026 are fundamentally **agentic search problems**. The conversation covers four pillars of modern search engineering: LLM-driven query understanding at scale, autoresearch (agents that write their own ranking code), agentic search harnesses (the feedback loops that make dumb retrievers smart), and LLM-as-a-Judge for principled evaluation.

Doug's course "Cheat at Search with Agents" (Maven) starting May 18, 2026 is referenced throughout.

## Core Thesis

> "The search problems of 2026 are agentic search problems."

Classical search architecture — query understanding pipeline → retrieval → reranking — is being unwound and replaced by agent-driven loops. The complexity shifts from the search stack itself to the agent harness and the feedback loops that guide agent behavior.

## Four Pillars

### 1. LLM Query Understanding at Scale

How to classify search queries with LLMs — even into thousands of fine-grained labels — without burning excessive token budgets. Doug's approach uses LLMs to hallucinate plausible labels from the schema, then map the query onto the existing classification taxonomy efficiently.

This extends Doug's earlier work: [[raw/articles/2025-04-08_softwaredoug-llm-query-understand]] and his "semantic search without embeddings" framework ([[raw/articles/2026-01-08_softwaredoug-semantic-search-without-embeddings]]).

**Key insight:** LLMs don't need full content understanding at query time. They need to understand *intent* — color, material, category, price range — as structured attributes, not semantic vectors.

### 2. Autoresearch — Agents That Write Ranking Code

Agents can craft optimized ranking code that's specific to a query or domain. Rather than hand-tuning BM25 parameters or building complex Learning-to-Rank pipelines, an agent can:

- Inspect the retrieval results
- Write a Python/ranking function optimized for NDCG
- Test it against judgment lists
- Iterate

**Key challenge:** Avoiding overfitting to a handful of training queries. The LLM may write ranking code that scores perfectly on the eval set but generalizes poorly. The solution is diversity constraints and careful evaluation design.

This topic connects to Doug's experiment described in [[raw/articles/2026-04-28_softwaredoug-can-agents-replace-search-stack]] on the Amazon ESCI benchmark.

### 3. Agentic Search Harnesses

Agents can turn simple retrieval tools (BM25, grep, even `find` + `grep` on the filesystem) into compelling search experiences — **but only if the harness provides the right feedback loops**.

The harness layer is critical:
- Agents need visibility into *why* results matched
- Simple tools (BM25, grep) give clear cause-and-effect — the agent can reason about why a keyword matched or didn't
- Thick APIs (vector search, complex reranking) obscure this reasoning, making agents trust results blindly
- The harness must enforce exploration: minimum tool calls, diversity constraints, similarity thresholds to avoid query stagnation

This directly echoes the "dumb retrievers" argument from Doug's earlier talk [[raw/articles/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how]] and the [[concepts/agent-harness]] framework.

### 4. LLM as a Judge

A principled approach to getting highly accurate search quality evaluation using LLMs — moving beyond gut-check evaluations to systematic, reproducible quality measurement.

Doug's experience at Daydream (hybrid search with CLIP models) and work on evaluations at Shopify informs a pragmatic take:
- LLM-as-a-Judge is not a shortcut — it requires careful rubric design
- Best used for "grug-brained evals": simple thumbs-up/thumbs-down labels from coworkers rather than ML-powered perfection
- Combined with engagement-based ground truths (click-through, purchase data) for production validation

## Connection to Wiki Concepts

### [[concepts/agentic-search]]
This talk directly illustrates all three levels of the agentic search framework:
- **Level 1 (IR)**: LLM Query Understanding replaces traditional query parsing — agents classify intent, not just expand terms
- **Level 2 (Harness)**: The entire conversation about agentic search harnesses maps to skill/tool discovery + feedback loops
- **Level 3 (Externalized Processing)**: Autoresearch agents that write their own ranking code are a canonical example of externalized processing

### [[entities/doug-turnbull-core-ideas]]
- "Agents need simple search" — demonstrated with the harness feedback loop argument
- "Search relevance as engineering" — LLM-as-a-Judge as a systematic evaluation practice
- "Query understanding > ranking" — LLMs classify intent, agents do the rest

### [[concepts/agent-harness]]
The critique of thick APIs vs. thin search tools is a direct argument about harness design: agents reason better with transparent, cause-effect tools.

### Vespa.ai
Jo Kristian Bergum represents the Vespa.ai perspective — an open-source big data serving engine that handles both vector and lexical search at production scale. Vespa is frequently used as the retrieval backend in agentic search architectures.

## Related

- [[concepts/agentic-search]] — Central concept page
- [[entities/doug-turnbull]] — Main entity page
- [[entities/doug-turnbull-speaking]] — Other conference talks
- [[concepts/agent-harness]] — Agent harness architecture
- [[raw/articles/2026-04-28_softwaredoug-can-agents-replace-search-stack]] — Directly related benchmark article
- [[raw/articles/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how]] — Previous Doug Turnbull talk

---

## Transcript (auto-generated)

<details>
<summary>Click to expand transcript (65:52, ~31K words)</summary>

00:00 So, this is what you're here for. 2026
00:03 will be the year of the of Agentic
00:05 Search. That's what Joe and I are going
00:06 to talk about.
00:09 And Joe, of course, I'll let you
00:10 introduce yourself in a minute, but
00:12 yeah, many people may know him as uh he
00:14 was a long time at Vespa.
00:17 I think really came into his own. Really
00:19 started to hear a lot from him in the
00:22 years around when RAG was really coming
00:24 out, speaking the truth of how Perch is
00:27 actually built to the RAG folks.
00:30 Um, and now he's CEO of Hornet, which is
00:32 trying to build a gentic an agentic
00:34 search engine uh, search for agents, not
00:37 just for people. Of course, I'm Doug for
00:39 those who don't know me. I have done
00:42 search in some form since about 2013.
00:45 Done all kinds of consulting and I do a
00:47 lot of training these days.
00:50 I do these events frequently, roughly
00:52 once a week.
00:54 Um,
00:56 in a couple weeks I'm going to host as
00:58 another event Hugo uh Bound Anderson who
01:02 is a great person to just learn about
01:03 build learn from about building agents.
01:06 He's going to give a great talk on uh
01:09 sort of his experience building agents
01:12 and not stressing out about all of the
01:16 it's very easy to get FOMO if you watch
01:18 social media for this stuff and that if
01:21 you're solving a problem you're probably
01:23 need like 10% of that right and it's
01:25 picking the right 10%. So he's going to
01:26 give a talk on that.
01:29 Uh, next week is Haystack. So, I'll be
01:32 there. That's why Renee is here. It may
01:36 be a quick turnaround if you're not
01:38 already in the east coast of the US to
01:41 come out, but uh, definitely come out.
01:43 It's a conference dedicated to search
01:46 relevance, search retrieval.
01:48 Happens once a year in the US on the
01:50 East Coast and once a year in Europe.
01:52 So, if you miss this one, there'll be
01:53 one hopefully in the fall.
01:57 Uh finally or not finally but uh last
02:01 and ultimately I'll be teaching my
02:04 search 101 class at search essentials.
02:08 This is a great chance if you just have
02:10 no idea about search concepts. It's a
02:14 free course I teach. It's just threehour
02:17 sessions with notebooks and things that
02:19 I've in my back pocket to learn things
02:22 like what is BM25 or what is an
02:25 embedding?
02:27 What do we even think about evaluating
02:28 search results? So really like core
02:30 concepts of search
02:32 and yeah check that out. You can always
02:35 find it software.com/sarch101.
02:38 And finally for if you want to support
02:41 all the tokens I spend writing blog
02:43 articles. I appreciate anyone who wants
02:47 to come to my class cheat with agents.
02:51 and I we talk about things from building
02:54 good harnesses to what retrieval looks
02:57 like for search and what uh doing things
03:00 like auto research with agents with the
03:02 search space. All of these things that
03:04 seem to come up a lot with the search
03:06 teams I'm talking to in my consulting
03:08 practice.
03:10 So yeah, that's it for events coming up.
03:15 I think Joe, do you want to introduce
03:17 yourself really quickly? just uh
03:20 anything I didn't cover?
03:23 &gt;&gt; No, I think you did a great job. Um
03:26 &gt;&gt; Okay.
03:27 &gt;&gt; I I can add a few words maybe. Um yeah.
03:31 So, hi everyone. I'm Joe. I been working
03:35 in search for quite some time. Um I
03:39 started actually on web search engine
03:42 that was built here in Tronim called the
03:44 webb.com.
03:46 And this was back in 2001. So I've been
03:49 in the search space for my entire
03:52 professional career and now we are
03:56 building a company and a new type of
03:59 retrieval engine that is built for
04:01 agents. It's new type of
04:04 new type of user of of search
04:06 infrastructure. So I'm quite excited
04:09 about joining you tonight and uh talking
04:12 about agentic search and agentic
04:14 retrieval. What's changing? What's not
04:16 changing? Um, I think it's very
04:18 interesting period we are in. So excited
04:21 to be here, Doug.
04:23 &gt;&gt; Yeah, for sure.
04:25 &gt;&gt; Yeah. Um, and maybe just to kick things
04:27 off, I'm I'm
04:29 like one thing I've noticed and I'm
04:31 curious to get your take on this is, um,
04:34 noticed there's Well, first of all, when
04:37 people say agentic search, they probably
04:38 mean like four or five different things.
04:40 &gt;&gt; Yeah,
04:41 &gt;&gt; that's one thing I've noticed. Um
04:44 I'm I'm curious to get your take on
04:47 this. Like one delineation I see for
04:49 agentic search is you have people who
04:53 build on one side you have people who
04:55 build really rich and robust harnesses
04:58 to uh try to make sure that they're
05:01 gathering the relevant information from
05:04 whatever search tools they're using. And
05:06 a lot of their effort is spent in part
05:09 because we're all learning how to build
05:10 harnesses right now. a lot of their
05:12 effort is spent like on the harness side
05:14 of things
05:16 and then on the other side what when
05:17 people talk sometimes when people talk
05:18 about agentic search they're talking
05:21 about topics which I think are
05:25 are I'm only like recently realizing are
05:28 fairly different which is um
05:32 the case I just earlier described like
05:34 assumes you're using the agent's
05:35 knowledge but what about cases where
05:38 you're the agent needs knowledge and
05:40 that feels more like well that's what I
05:42 see with like people using
05:44 multi vector search or like more um what
05:49 I think of more as like now deep
05:51 research
05:52 &gt;&gt; and I'm curious to get your take on that
05:54 or any other areas where definitions or
05:57 categories of agentic search you see in
05:59 the marketplace.
06:01 Yeah, I think uh this is an interesting
06:03 topic because
06:06 uh I think it was Boris, the guy from
06:08 Entropic that uh invented clo code. He
06:12 went on
06:13 &gt;&gt; he went on the latent space podcast and
06:16 talked about how claw code was not using
06:20 rag and was instead using aentic search.
06:24 And that was kind of a fun moment
06:27 because then everyone said essentially
06:30 that oh rag is dead and agentic search
06:33 is the new thing. And the definition
06:35 then of agentic search was that you have
06:38 a agent and a harness that is
06:41 essentially performing GP uh over your
06:44 codebase to uh get context to the to the
06:48 model. And this kind of created this rag
06:51 is dead. um team I would say uh and I
06:56 think that's because people associate
06:59 rag with the full kind of vector
07:02 database uh embed everything uh do a
07:06 similarity search and for a lot of
07:09 people new in the space rag meant
07:12 exactly that right so then suddenly
07:15 agentic search was a new thing because
07:18 uh and that was associate using gp I
07:20 personally my Definition of agentic
07:23 search is essentially that you have
07:25 search infrastructure or a search tool.
07:27 Uh you can call it harness maybe it's a
07:30 stretch but the key point is that it's
07:34 the agent that decides the query
07:36 formulation. Uh for me that is so it's
07:39 not me typing the query it's the agent
07:42 that is typing the query into the search
07:43 box. So that's my kind of broad
07:46 definition of of agentic search that the
07:48 agent is the new user. uh it's for the
07:51 the queries. Yeah.
07:53 &gt;&gt; Yeah. And how I'm curious how agents
07:56 uh how agents search differently than
07:58 people
07:59 &gt;&gt; if you have thoughts on that. Yeah.
08:01 &gt;&gt; Oh yeah. I have I have so many thoughts
08:03 on this. I think the most interesting
08:07 &gt;&gt; you know I'm I'm I'm a benchmark guy. I
08:09 love looking at benchmarks and one of
08:11 the most interesting benchmarks out
08:13 there when it comes to deep uh research
08:16 and aentic search is browser comp plus.
08:20 is about 830 very difficult questions
08:24 that are more like a pub quiz type of
08:26 question. Uh really long question uh
08:29 with a lots of hints and years and
08:31 whatnot and you have a relatively short
08:34 answer. So it's quite easy to judge the
08:38 overall response of the model and you
08:42 have a fixed corpus of about 105,000
08:45 uh web pages. Mhm.
08:47 &gt;&gt; And this is this is like a really gold
08:50 mine uh of a data set. So I recommend
08:54 everyone to check it out.
08:56 &gt;&gt; And if you look at the trajectories, so
09:00 essentially the harness is very simple.
09:02 It's a simple prompt, just a few
09:05 paragraphs like you're a search
09:07 assistant blah blah blah. You have a
09:08 question and here's a search tool. And
09:11 the search tool is simply search and it
09:15 takes a string. And that tool in the
09:18 official benchmark protocol returns five
09:21 hits uh truncated by the 512 first
09:26 tokens.
09:27 &gt;&gt; Mhm.
09:28 &gt;&gt; And then you can look at the
09:29 trajectories. So on average you have
09:32 about 25 search calls that the agent is
09:36 like deciding to search and reason and
09:39 search and search and reason.
09:40 &gt;&gt; Interesting. Yeah.
09:42 &gt;&gt; And I spent a lot of time gpping and
09:45 analyzing this data and one of the
09:49 surprising findings is that one the
09:52 queries are really long.
09:54 &gt;&gt; So there's about 23 query terms, right?
09:57 So this is definitely not like AOL
09:59 search log from uh back in the day,
10:02 right? Where you had about two terms on
10:05 average.
10:06 &gt;&gt; That's one big change. But the most
10:08 surprising thing is there's a lot of
10:10 phrase queries. A lot of phrase queries.
10:12 And even if you haven't told the agent
10:15 like
10:15 &gt;&gt; what is the query syntax that the engine
10:18 supports is doing phrases, it's doing
10:21 site, it's doing all kinds of things. Uh
10:24 so I find that interesting. Um yeah.
10:28 &gt;&gt; Yeah, that's really interesting. And um
10:31 agents can really drive a lot of these
10:35 like syntaxes that you give it. Uh so
10:38 yeah, I find that really interesting. Um
10:41 is anyone I I want to make sure it's
10:43 open. So if anyone else has any thoughts
10:45 or comments or questions, feel free to
10:46 raise your hand or or jump in with
10:48 anything.
10:51 Yeah, I've I've uh Tito says a agents
10:54 doing phrase search more than humans is
10:56 fascinating, surprising. You know, one
10:58 thing about an agent that's interesting
11:00 in that regard is they also have a great
11:03 deal more patience than humans. So if
11:08 you gave agents
11:10 some way of um searching like I think
11:15 you said it might issue go through like
11:18 15 or 20 different search goals or
11:20 something like this. Agents will sort of
11:23 exhaustively go through and
11:26 spend the time to go through things in a
11:28 way that and and analyze them and reason
11:30 about them and also reason about cause
11:33 and effect. So if I if I stimulate the
11:36 search this way, this comes back.
11:38 &gt&gt; Yeah.
11:38 &gt>&gt; Um in a way that is somewhat reminiscent
11:42 of a human researcher using an advanced
11:44 search tool. Uh but I don't think we
11:47 have the patience.
11:49 &gt;&gt; Maybe we maybe some people have the
11:50 patience, but I don't have the patience
11:52 for that anymore.
11:54 So, another thing that I think is
11:55 interesting is just
11:57 sometimes when you see these um
12:00 sometimes it's I don't I'd be curious to
12:02 get your take because one take I have
12:04 and feel free to disagree with this is
12:06 agents sometimes do better with
12:08 predictable search tools than they do
12:10 with search tools where it's not easy to
12:13 reason about the cause and effect why
12:15 results came back the way they did
12:18 &gt;&gt; which which yeah
12:20 &gt;&gt; yeah I think this is obviously in
12:23 browser comp plus the harness the prompt
12:26 is really simple.
12:29 So the trajectories you get the the
12:33 queries that the agent is executing
12:37 are really in a way just showing us the
12:40 pure way how the GPT5 model was trained
12:45 uh within learning
12:48 &gt;&gt; and whatever data went into that mix.
12:51 It's certainly web search oriented with
12:55 using the the query syntax that is
12:58 supported by Bing and Google and others.
13:00 &gt;&gt; Yeah. Mhm.
13:01 &gt;&gt; I think there are like 5% of the 20,000
13:05 qu queries that were executed that were
13:07 actually including the site operator. So
13:09 if you've been around for some time,
13:11 Google if you type site colon like
13:14 restricted to a certain domain
13:16 &gt;&gt; that's in there. uh year, ranges, things
13:20 of that nature. Um,
13:23 &gt;&gt; and I see Tito here wondering if Oh,
13:26 sorry. Stro says presumably they agent
13:28 have access to the full programmatic
13:30 search syntax. Yes, they could have if
13:32 if the prompt included it, but in the
13:35 browser comp plus harness and the
13:37 setting and the protocol, it's pure the
13:40 search tool is just a string, right?
13:42 Yeah.
13:44 &gt;&gt; So,
13:44 &gt;&gt; yeah, it's interesting. Obviously if you
13:47 prompt it differently if you say here's
13:50 the syntax that is supported then
13:52 obviously it can uh use that information
13:55 while searching through right but in
13:58 that they don't have that. Yeah.
14:01 &gt;&gt; Yeah. There's a when you design agents,
14:03 there's an interesting thing where
14:06 &gt;&gt; if you stay roughly aligned to their
14:08 training data,
14:11 &gt;&gt; you where agents tend to LLMs tend to
14:14 want to veer back towards the tool usage
14:16 it knows from the training data.
14:18 &gt;&gt; Exactly. The one one reason that people
14:20 can get some reasonably good results out
14:22 of GP over a file system of a knowledge
14:25 base even an extensive knowledge base is
14:28 in part because the frontier labs have
14:30 spent so much time training that
14:34 specific thing
14:36 and same with web search. Yeah,
14:39 &gt;&gt; I think that's a very important
14:40 observation is whatever you're doing uh
14:45 relating to harness or whatnot, right?
14:48 You should look at what the frontier
14:50 model companies are optimizing for.
14:54 &gt;&gt; What is the training mix? And currently
14:56 the training mix is heavily biased
14:58 towards coding and using the computer
15:02 through GP etc. Right? And if you use a
15:06 coding agent, you will see that they are
15:08 very effective at using GP, right?
15:11 Multiple trade formulations going into
15:13 the same GP. Um, and you can exploit
15:17 that. Uh, you know, you can expose
15:21 search infrastructure that supports GP,
15:24 right? If you somehow have something
15:26 that is indexed, you can essentially
15:28 say, \"Oh, you can GP.\" and then you
15:30 intercept that GP call and you can
15:32 translate that into uh actual search
15:35 request to the to the engine. So I think
15:38 that's a lot of the current harness
15:40 engineering is about optimizing for
15:42 whatever the model companies are doing.
15:45 &gt;&gt; And when you're doing that, you're
15:47 essentially putting yourself on the
15:49 trajectory of the models getting better
15:52 and your harness and performance will
15:54 automatically get better, right? H
15:57 &gt;&gt; so
15:57 &gt;&gt; yeah I think it's interesting because I
15:59 think in um well to get to maybe answer
16:01 Tito's question really quick or discuss
16:03 that is one he's wondering if agents
16:05 have a search query formulation feedback
16:07 loop based on the results.
16:10 &gt;&gt; And I I definitely see that and you can
16:11 see that in the p in the if you read any
16:13 of the
16:16 &gt;&gt; like a lot of to the original tool usage
16:18 papers actually search is a very front
16:20 and center tool. It's probably the early
16:22 on at least it's the number one tool
16:23 probably talked about
16:26 &gt;&gt; and you see that you see like oh I
16:28 issued this search for some Apple remote
16:30 but I messed up oh it didn't seem like
16:33 the results were right let me try new
16:35 query so you definitely see stuff like
16:37 that
16:38 &gt;&gt; yeah no it definitely you can you you
16:41 find so many if you look at the
16:43 trajectories from browser chrome plus uh
16:45 you can download them from hugging face
16:48 hugging
16:49 And it's almost entertaining to see how
16:53 the model is trying first broadly and
16:56 then uh going down into a certain
16:59 direction and then coming back doing
17:01 something else and then finally figuring
17:03 out right so they're definitely
17:07 they're definitely learning from what
17:10 they're observing and what they're
17:12 seeing. And this also is a very
17:14 interesting aspect from for for me has
17:16 been in the search industry for a so
17:18 long time
17:20 &gt;&gt; and that is that we usually kind of
17:22 built the systems around doing a single
17:25 query right you had query
17:27 &gt;&gt; 100%
17:28 &gt;&gt; like query when I was at Yahoo there was
17:31 like a team probably like 40 50 people
17:34 just working on query understanding um
17:37 right across the entire Yahoo surface
17:41 Mhm.
17:42 &gt;&gt; And then you would forward that query
17:43 into a specific vertical and that
17:46 vertical will do some similar query
17:47 understanding. For example, if it was
17:49 forwarded to local search, you would
17:50 like try to figure out if this is
17:53 looking for a business or a particular
17:55 business or a category.
17:58 And I feel all of that now except from
18:00 latency and complexity and all of that
18:02 if we put that aside is like essentially
18:06 almost like a solve problem. Um, and if
18:09 you in in certain domains where you
18:12 &gt;&gt; you're not constrained by having to have
18:15 submillisecond latency or things like
18:17 that, right? Let
18:18 &gt;&gt; Yeah. Yeah.
18:19 &gt;&gt; Let the agent rip through the data and
18:21 you get a much better response, right?
18:24 &gt;&gt; So, I'm I'm like and I I I'm been
18:28 working on so many big systems and large
18:30 QPS, hundred thousands of QPS, billions
18:32 of documents and whatnot. And it kind of
18:35 have influenced my thinking around
18:37 things being like oh you can only do one
18:39 query you have to care about latency
18:41 performance and cost but there are so
18:43 many domains that you don't have the
18:45 scale you don't have the problems with
18:47 it it doesn't matter if 5 seconds right
18:50 because if the response is great so I
18:52 think like the whole search industry and
18:55 all of us veterans we're like so biased
18:57 about oh we have to make it super fast
18:59 we can only do single query but there's
19:01 so many use cases where you you know
19:03 you're not operating in the scale, you
19:05 can just let the agent rip through. So,
19:08 &gt;&gt; absolutely. Yeah. Um, and you can
19:10 premputee a lot of stuff too. So, you
19:12 can
19:12 &gt;&gt; you can uh a lot of what I do in my
19:15 courses, we just talk about like of
19:16 course everyone asks, \"Isn't this going
19:18 to be slow if we have an LM helping us
19:20 do query understanding,
19:21 &gt;&gt; but even in regular search and I see
19:23 people doing this now, it's just people
19:26 people default to, well, let me just
19:28 have a nightly job. Maybe I'll self-host
19:30 a model. It doesn't have to be big to
19:32 like and it's funny because I'm in the
19:35 same camp like people would spend very
19:38 highly educated people would spend a lot
19:40 of time spell like how do I spellch
19:42 checkck this type of query
19:45 &gt;&gt; and that would be a multi-month project
19:47 and now it's just like the LLM just does
19:49 it.
19:50 &gt;&gt; Yeah. or the I will say like for like
19:54 the 80% use case
19:57 where it gets interesting is probably
20:00 the last 20% where you are really trying
20:04 to squeeze out all the hundo performance
20:06 and you're trying to do new and novel
20:09 things and you're trying to do super
20:11 domain specific things. That's where
20:13 things get really interesting. But 80%
20:16 of what people are doing with search
20:18 relevance today could almost be done
20:20 automatically.
20:22 &gt;&gt; Yeah. I think one thing that's
20:24 interesting about the the 20% is that
20:26 we are sort of handed that with RAG, but
20:29 RAG gives you the ability to not care
20:32 about the 80% or the 80% was the things
20:34 that old school search was all about.
20:36 And RAG sort of did away with that in a
20:37 good way. But then the 20% becomes a
20:41 harder problem.
20:43 &gt;&gt; So hard. So I had started earlier saying
20:46 that we've been solving these single
20:49 query problems for so long with a set of
20:52 50 or 60 people and you have the big
20:55 advantage that you can precompute a lot
20:56 of things to make the single query
20:59 work, right? the n-gram, the whatever.
21:01 And now you're moving to a world where
21:04 you can't precompute everything because
21:06 you don't know what questions the agent
21:08 is going to ask you, right? So in a way
21:12 you're going back to not doing query
21:14 understanding, right? You're letting the
21:16 agent do the query understanding. So
21:19 that's also a new challenge for
21:21 search practitioners.
21:23 &gt;&gt; They have to think about what are the
21:25 primitives that are going to satisfy
21:27 this.
21:29 &gt;&gt; And one of the things we also discovered
21:31 in BrowserComp+ analysis is that you can
21:35 just look at the queries that are being
21:37 generated and one of the big issues is
21:40 that they're really long. about 23 terms.
21:43 &gt; &gt; So you need a retrieval engine that
21:46 can handle long queries, right? If you
21:48 have a retrieval engine that has a limit
21:50 that truncates the query after you know
21:52 10 terms, you're probably in trouble.
21:55 Because you can see in the trajectories
21:58 the query length is about 23 terms.
22:02 &gt;&gt; That's really interesting.
22:04 &gt;&gt; And also you have to think about how
22:07 many queries per second you are doing
22:10 because the agent in one conversation is
22:14 doing 25 queries. So the average search
22:18 session for a human might be you know an
22:20 average of 1.5 to 2.5 queries. So you
22:25 get an order of magnitude more queries
22:28 per session. So your system needs to be
22:31 able to support that without suffering
22:34 from the query per second load.
22:37 &gt;&gt; And you also need good relevance for
22:39 that long tail.
22:40 &gt;&gt; Yeah. Yeah. And also you need to
22:44 handle queries that have phrase syntax
22:48 and you need to handle the path
22:51 navigational queries.
22:53 &gt;&gt; So there's a lot of interesting
22:55 dimensions there.
22:57 &gt;&gt; There is. And so I think one of the
22:59 interesting things about agentic search
23:00 is there's a lot of you that you can
23:03 build your own tool that's just specific
23:05 to what you're doing. Um and I see kind
23:08 of two really interesting things that
23:10 are going on. One is you can give agents
23:15 really low level searching capabilities
23:18 like just GP. It's very familiar to the
23:21 agent. They know what it is. They can
23:24 reason about cause and effect
23:27 and you'll get reasonably good results
23:29 out of that but you'll have really poor
23:31 token efficiency because GP is just
23:33 going to dump a lot of stuff into the
23:35 context window that isn't useful.
23:38 Then on the other extreme you can give
23:41 them a very high level search ability
23:43 which is a dense retriever which returns
23:46 you five things and the agent can't
23:49 reason about why those five things came
23:51 back. And you kind of need to choose a
23:54 middle path and when I teach my
23:57 class we talk about like creating a
23:59 harness around the search to give people
24:01 the feedback they need to get the good
24:03 results but also not overly pollute the
24:05 context with all the stuff that GP is
24:07 going to dump into it.
24:10 &gt;&gt; I think we seeing a lot of really cool
24:13 products and ventures along this
24:16 dimension. You have clouds on one end
24:19 and you have hornet on the other end.
24:22 &gt;&gt; which one is which?
24:25 &gt;&gt; This is a gentle plug. I'm just getting
24:29 started.
24:29 &gt;&gt; There's gonna be a lot of companies that
24:31 sit along that that spectr. And I think
24:33 the choice of where you fall depends on
24:35 what problem you're trying to solve. But
24:38 I think we're seeing a lot of innovation
24:40 along that spectrum.
24:43 &gt;&gt; Absolutely. And I think the the plug is
24:45 fine. Joe, maybe you want to say a
24:47 little bit more about what Hornet is
24:49 doing?
24:50 &gt;&gt; Yeah, so Hornet is building a retrieval
24:53 engine designed specifically for agents
24:56 and you you we heard about some of the
24:58 requirements agent like has such as long
25:00 queries ah phrase queries all of that.
25:03 And we also need the retrieval engine to
25:06 be reactive. So when the agent is
25:09 searching for something and you update a
25:11 document the next query should see that
25:13 doc. You also need it to be low latency.
25:16 But the most important thing is it needs
25:19 to have controllable relevancy. So the
25:22 agent needs to be able to through the
25:24 query formulation influence the ranking
25:27 and we spend a lot of time on building
25:31 relevance models that you can steer and
25:33 adjust at query time through the query
25:36 extension and controls. Um, so that's
25:38 Hornet in a nutshell.
25:40 &gt;&gt; Are you already doing that? Is is that
25:41 active?
25:43 &gt;&gt; Yes. We are active. We've been working
25:46 quite some time on it and we are ramping
25:48 up more design partners and opening up
25:51 more of our capabilities. So if anyone
25:54 is interested, you can reach out to me.
25:57 More to come.
25:58 &gt;&gt; Nice.
26:00 &gt;&gt; And we've worked with design partners
26:03 um related to to browsing, to tool
26:06 usage, many things. So I think the
26:09 challenge right now is that agents think
26:13 differently and they also type in the
26:16 query search box in a different manner
26:18 than users. And we need to be reactive
26:23 to that.
26:24 &gt;&gt; And it's also more than just the query.
26:25 It's understanding the intent that's
26:27 behind the query, right?
26:30 &gt;&gt; So we need a lot more signals than just
26:32 the query to be able to understand the
26:34 intent. But I think the current direction
26:37 is that you can get a lot done by just
26:39 looking at the query.
26:41 So yeah, very interesting times.
26:43 &gt;&gt; Yeah. And sometimes I think also in
26:44 terms of evaluating a gentic search, I
26:47 think we're having to reevaluate how we
26:49 think about search in general. So one of
26:51 the analogies I use is imagine you're
26:53 going to a library and you ask the
26:55 librarian a question and the librarian
26:58 goes and searches in different shelves.
26:59 It's sort of like that. And we have to
27:02 think about not just the final result
27:04 but how we got there.
27:08 &gt;&gt; Yeah and there was a paper on that. And
27:10 a similar analogous statement was
27:12 searching in a library and it's someone
27:14 who knows the domain and can navigate
27:16 the library versus someone who just
27:18 goes to the card catalog.
27:21 &gt;&gt; Right. Exactly. So I think evaluation is
27:24 also an area where we have to look at
27:26 the journey and not just the result.
27:30 &gt;&gt; Well, and also within the journey, what
27:32 is the interaction between the agent and
27:34 the search engine? So in the Browser
27:36 Comp+ dataset, you see trajectories. And
27:39 if you look at the wrong search results,
27:42 you can see how that influences the
27:44 agent's reasoning. If the search engine
27:47 returns a wrong result, the agent might
27:49 go down a path that doesn't lead to the
27:51 answer. So the impact of a bad search
27:55 result is really amplified in agentic
27:58 search because it can lead the agent
27:59 down the wrong path.
28:02 &gt;&gt; And that's what we call the "cascade
28:05 effect" in search. One bad result can
28:08 cascade into a whole series of bad
28:10 results.
28:12 &gt;&gt; Absolutely. And also the positive side
28:14 is that the agent can recover from bad
28:16 results if it has good reasoning. So the
28:19 agent can say, "Well, that didn't work.
28:21 Let me try a different approach." And
28:23 that's something that humans do but
28:25 automated systems don't.
28:28 &gt;&gt; So the agent has this self-correction
28:30 capability that is really powerful.
28:33 Absolutely. And there is a point to make
28:36 about the search engine needing to be
28:38 designed with the agent in mind. The
28:40 query processing, the ranking, the
28:42 relevance models all need to be
28:44 optimized for agent queries which are
28:46 different from human queries.
28:48 &gt;&gt; And I think that's the key insight. The
28:50 search engines that are designed for
28:52 agents will outperform those that are
28:54 designed for humans when the user is an
28:56 agent.
28:57 &gt;&gt; 100%. I think the paradigm shift is that
29:00 the agent is the new user. The search
29:03 engine needs to understand that the
29:05 agent has different needs, different
29:07 query patterns, and different
29:09 expectations.
29:11 &gt;&gt; And this will reshape the search
29:13 industry.
29:15 &gt;&gt; It will.
29:17 So
29:18 &gt;&gt; let's open it up for questions.
29:20 &gt;&gt; Great. Anyone have questions?
29:22 &gt;&gt; I have a question. How do you think
29:25 about the balance between giving the
29:27 agent too many tools versus too few?
29:31 &gt;&gt; That's an excellent question. I think
29:33 the trend is towards giving agents fewer
29:35 but more powerful tools. Give them a
29:38 search tool, a code execution tool, maybe
29:40 a file system tool. Let the agent figure
29:43 out how to combine them.
29:45 &gt;&gt; I agree. The MCP approach where you
29:48 have 50 different tools is not going to
29:50 work well because the agent's context
29:52 window fills up with tool descriptions
29:54 and not actual data.
29:56 &gt;&gt; Exactly. That's the problem with the
29:58 current approach. You end up with more
30:00 context about tools than about the
30:02 problem you're trying to solve.
30:04 &gt;&gt; So I think we'll see a consolidation
30:06 towards a few key tools that are highly
30:08 optimized for agent usage.
30:10 &gt;&gt; And I think that's where the innovation
30:12 is happening. Companies like Cloudflare
30:14 with their two-tool approach (search and
30:16 execute) or what Hornet is doing with
30:18 agent-specific retrieval engines.
30:20 &gt;&gt; So the future is not more tools, it's
30:22 better tools.
30:24 &gt;&gt; Exactly.
30:26 &gt;&gt; Another question.
30:27 &gt;&gt; Yes, I have a question about evaluation.
30:30 How do you evaluate an agentic search
30:32 system? Because it's not just about the
30:34 relevance of the results, it's about the
30:36 whole trajectory.
30:38 &gt;&gt; That's a great question. I think we need
30:40 to move beyond NDCG and MAP for agentic
30:43 search. We need to evaluate the entire
30:45 search trajectory. Did the agent find
30:47 the right answer? How many queries did
30:49 it take? Did it get stuck in loops?
30:52 &gt;&gt; And also, did the search engine help or
30:54 hinder the agent's reasoning? We need
30:56 metrics that capture the interaction
30:58 between the agent and the search engine.
31:01 &gt;&gt; So it's a whole new evaluation paradigm.
31:04 &gt;&gt; It is. And that's why I'm excited about
31:06 the work being done on process-based
31:08 evaluation rather than just outcome-based.
31:11 &gt;&gt; Yes, exactly. Looking at the reasoning
31:13 trace, the query trajectories, and how
31:15 the agent responds to search results.
31:18 &gt;&gt; That's the frontier.
31:20 &gt;&gt; So let's check the chat for more
31:22 questions.
31:24 &gt;&gt; I see a question from Tito about
31:26 personal agents and the inverted SEO
31:28 concept.
31:30 &gt;&gt; That's a fascinating topic. Tito, do you
31:32 want to ask?
31:34 &gt;&gt; Sure. When I think about agents, I think
31:36 that ultimately their goal is to complete
31:38 tasks or achieve some goals and they
31:40 don't necessarily have foresight into
31:42 what are the best sources to search
31:44 against to accomplish that.
31:46 &gt;&gt; Right. With an enterprise agent that's
31:48 been tuned for a specific task, you can
31:50 optimize the model to know which sources
31:52 are good. But I'm thinking about personal
31:54 agents where a human has an agent
31:56 accomplishing a task across dozens or
31:58 hundreds of potential sources.
32:00 &gt;&gt; We may be moving towards a world of
32:02 competitiveness in terms of search
32:04 providers that are optimized for
32:06 receiving and interpreting agent
32:08 searches. The ones that do the best at
32:10 that will be the ones where agents come
32:12 back. The ones that are more brittle will
32:14 lose traffic. This is almost like an
32:16 inverted SEO.
32:18 &gt;&gt; That's a really good point. I think
32:20 personalization in search is easier than
32:22 ever because of in-context learning.
32:24 &gt;&gt; API-first will be a thing. Search
32:26 providers will be forced to expose APIs
32:28 for agents. There will be a whole new
32:30 economy around giving API access to
32:32 agents.
32:34 &gt;&gt; But the pricing model is still up in
32:36 the air. How do you pay for agent
32:38 traffic? It's a huge debate that still
32:40 needs to be solved.
32:42 &gt;&gt; Absolutely. And also, the search
32:44 providers that are set up to be
32:46 agent-friendly will be the winners in
32:48 the future.
32:50 &gt;&gt; I think that's right. And we're already
32:52 seeing companies build agent-specific
32:54 APIs.
32:56 &gt;&gt; Let's take another question.
32:58 &gt;&gt; Hi, this is Jen. I'm from Waldo. Thanks
33:00 for the discussion. I had a question
33:02 about the file system approach. With
33:04 your idea of running grep with code on
33:06 the file system, are we moving away from
33:08 indexing? And do we need to keep our
33:10 system of record in the file system?
33:12 &gt;&gt; Great question. First, grep relates to
33:14 scanning versus indexing. Indexing is
33:16 about optimizing data structures because
33:18 you're going to search a lot or you have
33:20 large scale.
33:22 &gt;&gt; You can do BM25 without building an
33:24 index. You can scan through data and
33:26 calculate statistics.
33:28 &gt;&gt; The second answer is that you don't
33:30 necessarily need to scan. You just need
33:32 to make sure that you look like grep.
33:34 Support some of the syntax of grep, but
33:36 the implementation could be powered by
33:38 something else.
33:40 &gt;&gt; Same thing applies to a file system. You
33:42 can build a virtual file system on top
33:44 of a database or retrieval engine. You
33:46 don't have to dump your database into a
33:48 real file system.
33:50 &gt;&gt; It's just creating abstractions and APIs
33:52 that look like the tasks that current
33:54 models are great at.
33:56 &gt;&gt; That's very insightful. Thank you.
33:58 &gt;&gt; And the interesting thing is that if you
34:00 go to a medium-sized or large e-commerce
34:02 site, a lot of how people think about
34:04 search is in a much more metadata
34:06 oriented way.
34:08 &gt;&gt; What's interesting about the virtual
34:10 file system is it's like different
34:12 perspectives on the data organized by
34:14 different ways of organizing metadata.
34:16 &gt;&gt; When you've organized the data that way,
34:18 that is solving a major part of the
34:20 search problem.
34:22 &gt;&gt; But you really miss the scoring
34:24 sometimes. Grep can scan and fill up the
34:26 context, whereas scoring is valuable to
34:28 manage context - to know the top 10.
34:30 &gt;&gt; But if you look at how agents do grep,
34:32 sometimes it includes a regular
34:34 expression, other times it uses the pipe
34:36 character to mean "try any of these."
34:38 You can intercept that and use a real
34:40 relevancy-capable retrieval engine to
34:42 search your data in a meaningful way.
34:44 &gt;&gt; We have been working on search for a
34:46 long time. We know about precision and
34:48 recall. Recall is about finding all the
34:50 relevant information. Precision is about
34:52 finding nothing but the relevant
34:54 information.
34:56 &gt;&gt; That's essentially what context
34:58 engineering is about. You want all the
35:00 relevant information to get the task
35:02 done. You could just stuff everything
35:04 into the context window, but that
35:06 doesn't work well. You need the
35:08 precision component.
35:10 &gt;&gt; A lot of what we've been working on for
35:12 20-25 years on relevance, precision, and
35:14 recall is now even more relevant because
35:16 you can apply those principles to
35:18 context engineering.
35:20 &gt;&gt; Absolutely. And I probably need to close.
35:22 This has been a fantastic conversation.
35:24 I shared Joe's Hornet. You can find Joe
35:26 everywhere on X and LinkedIn.
35:28 &gt;&gt; If we haven't convinced you hopefully
35:30 we've convinced you that agentic search
35:32 is really the thing coming. And we
35:34 haven't even touched on context
35:36 engineering.
35:38 &gt;&gt; There are many, many little search
35:40 problems - retrieving skills, agentic
35:42 memory. Every other day I'm opening
35:44 social media and I have to go learn
35:46 about something new.
35:48 &gt;&gt; Please stay in touch, check me out
35:50 everywhere. Hope to see you in a future
35:52 class or lightning lesson.
35:54 &gt;&gt; Thank you so much, Joe, and thanks
35:56 everyone for coming.
35:58 &gt;&gt; Thank you so much. This has been great.
36:00 I could talk about search and agentic
36:02 search as you can tell.
36:04 &gt;&gt; Take care. Thank you everyone. Bye-bye.

</details>

