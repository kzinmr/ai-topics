---
title: "Cheat at Search — Coding Agents & Auto Research (Lecture Transcript)"
author: Doug Turnbull (@softwaredoug)
date: 2026-06-04
date_ingested: 2026-06-04
related_article: articles/2026-06-04_softwaredoug_search-with-agents-lesson6-rlms
type: transcript
tags:
  - agentic-search
  - rlm
  - recursive-language-models
  - auto-research
  - coding-agents
  - overfitting
  - guardrails
  - search-ranking
  - ndcg
  - context-management
  - harness-engineering
  - search
---

# Cheat at Search — Coding Agents & Auto Research (Lecture Transcript)

**Author:** Doug Turnbull (SoftwareDoug / softwaredoug.com)
**Date:** June 4, 2026
**Context:** Live lecture for the Cheat at Search Maven course. Lesson 7 — Recursive Language Models (RLMs) and Auto Research for search ranking.
**Companion slides:** [[articles/2026-06-04_softwaredoug_search-with-agents-lesson6-rlms|Search with Agents Lesson 6: Recursive Language Models]]
**Companion course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)
**Prior lectures:** [[raw/transcripts/2026-06-02_softwaredoug_cheat-at-search-long-running-search-lecture|Lesson 5: Long Running Search Agents]], [[raw/transcripts/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge-lecture|Lesson 4: LLM as Judge]], [[raw/transcripts/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents-lecture|Lesson 3: Steering Lost Agents]], [[raw/transcripts/2026-05-20_softwaredoug_cheat-at-search-llm-query-understanding-lecture|Lesson 2: LLM Query Understanding]]

---

## 1. Introduction — Two Big Topics

**[Doug Turnbull, 00:01:44]** Today's a pretty exciting day, because this is a topic I'm really interested in — auto research. Auto-researching coding agents. I'm actually giving a talk in Berlin on this topic.

**[00:02:18]** We're gonna talk about two big topics today. We're gonna continue the task we had on Monday — using the notion of a long-running agent to solve problems for us, and wake up, and try to search again for whatever we needed to find. And we're also gonna talk about auto research.

---

## 2. Recap — Long-Running Agents and Context Waste

**[00:03:08]** Previously we had this notion of lots of local tool calls that wasted a lot of context, dealing with remembering what past instances of this agent had done. Or we try to express either a task frontier — or you could think of it as delegating a task to an agent — as one way to solve the problem, so we're not consuming so many tokens, just wasting time on trying to find what a new search could be.

**[00:03:49]** If you remember from last time, we were talking specifically about this recruiting analogy — going out to Google Patent Search, trying to find experts on a field, to maybe talk to them.

**[00:04:23]** The other thing we did — we learned it helps to interact with some local storage that's sort of self-organized by the agent. So the agent decides what to index and how to index it, and then the agent can later query. We found that to be a really big time saver — having a local cache was really important. And when I say local here, that was our local Elasticsearch or whatever other search engine we're using.

---

## 3. Recursive Language Models (RLMs) — Context as Python Variable

**[00:05:07]** We can imagine a world where the index is just part of the context. Imagine we didn't have this constraint — we might just have an infinite context window with no context rot whatsoever. That's a glorious future that maybe one day we will have.

**[00:05:32]** But right now, of course, we are constrained with around 1 million token windows. So imagine instead, we had all of the data, all of the experts we had found so far, just part of the context that we were working on. And we had a way for the agent to reflect on its own context and say, "oh, I've already done this or not done this." That's kind of what RLMs purport to do.

### 3.1 The REPL Pattern

**[00:06:12]** RLMs are a way of interacting with a Python REPL. The idea is the context — in this case, all results so far, every tool call out to an external search system — and the list of existing experts just keeps getting appended to a string variable in a Python REPL.

**[00:06:46]** The agent is on the left, and it just has tool calls to this REPL to interact with this large variable that's sitting on it. When I say REPL — that's basically just a running Python process that accepts Python commands, executes them, and returns the response. The Jupyter notebook that we've worked with is a REPL. It just means Read, Evaluate, Print Loop.

**[00:07:36]** This context variable could grow up as long as we have memory on the system. The idea is the Python code emitted could correctly try to find things within that using normal string manipulation commands, regex, that kind of thing, and then look at the output and see if it can understand what the current state of its system is. And use that as a means to avoid duplicating work.

### 3.2 Direct Corpus Interaction

**[00:09:03]** This is very similar to a lot of stuff we've done in the past — I'm getting this new phrase called "direct corpus interaction." Which is really the same idea we did a couple classes ago — just letting an LLM have access to a Bash process and run whatever bash commands it wants. You can think about a bash terminal and the file system as a kind of REPL. Where all of the information is not necessarily in the agent itself, it's off in the file system.

**[00:09:51]** And we're doing the same thing here with a recursive language model. We're using the variables within Python itself to basically get that kind of similar behavior.

### 3.3 System Prompt Design

**[00:10:12]** We have our system prompt. You have access to a Python REPL, which has on it these variables: `historical_results`, a list of patent search queries and relevant experts. There's a big "append experts here." And then there is the patent search function. We sort of indicate how to call the patent search function.

**[00:10:42]** And we give it a task: "Your job is to pick a query to execute against Google patents that might help find experts. Look over the history, pick a good next query, append to historical results. Iterate, looking for experts, adding to historical results. Return a message saying how many you appended."

**[00:11:18]** A hint is how the historical results string variable will be formatted — first expert description, second expert description, the original Google Patent Search. So we kind of have this infinitely growing log of every task that was ever done by this process.

### 3.4 Observed Agent Behaviors

**[00:20:49]** It's interesting — when you do this, based on the LLM's own memory, I occasionally see situations where the agent just appends relevant inventors it knows about. Just with Python code. These LLMs have trained on the entire universe of human knowledge. So whatever we talk about with electric cars, it's gonna already know prominent inventors. Which might be a problem if it's hallucinating.

**[00:21:48]** Sometimes what you'll see is it will append code to rate results. But what the rating is really doing is some kind of programmatic rule-based rating — like "lithium in the title" or "plating in the title." This might be specifically searching for items about lithium-ion batteries.

### 3.5 The Recursive Part — Sub-Agent via LLM Query

**[00:29:07]** Everything is kind of interesting — it's just an LLM interacting with a REPL. But there's another layer. An RLM has access — gives the REPL access to call an LLM with a prompt, and get a response. So it has access to this patent search function, it also has access to this `llm_query` function. Which just sends a prompt to an LLM and gets a response back.

**[00:29:41]** So that's the recursive part. We have LLMs calling LLMs — we have sub-agents, it's sort of similar to that concept.

**[00:30:06]** We still have a lot of interactions. If we restart the context on the left, we're still gonna have a lot of interactions with the REPL — for example, to figure out the current state of things and try to figure out what should be searched for that we don't already have results for.

### 3.6 Skills and Tool Usage

**[00:32:22]** What I have generally found when working with recursive language models is if you just give a tool like `llm_query`, and you give basically no examples of how to use it, it tends not to be used. If you do something like this, where you actually give examples of how you want it to be used, it will actually be used for those situations.

**[00:32:47]** This is very similar to how agentic skills work. You give something very open-ended, the agent won't necessarily use it. If you give an agent examples and a quote-unquote "skill" of how you can use this to solve a problem, it will actually be used for that.

**[00:33:11]** But the other question is — should we even tell this outer LLM that it has access to a sub-query that it can run arbitrary prompts? Or should we literally just have a function called `judge` and say "evaluate an expert's relevance"?

### 3.7 Is "Recursive" the Right Word?

**[Joel Turner, 00:34:56]** I just want to make sure I'm understanding how you're using the word "recursive" in this context. When I think of a recursive function, I think of a base case, and a function continuously looping until the base case is solved. Is that similar to what you're talking about here?

**[Doug Turnbull, 00:35:32]** It's not classically recursive. It's just maybe a bit of branding. Really, all it is is giving the outer agent an LLM — or putting on the REPL some way of calling an LLM. But it's not recursive — it can't keep recursing, because this LLM in here doesn't have access to the REPL. It's just executing a one-off task to do something.

**[00:36:18]** It's almost more of a sub-agent that does a small task than truly recursive. The big picture: we have an outer agent that is maintaining all its state in a Python Process. And that Python process has some functionality we've given it: a variable of what the historical results have been, a patent search function, and now a new Python function to basically run a sub-agent.

### 3.8 State Enforcement and Validation

**[00:37:33]** Things can still happen — Joel, you mentioned this — that you still get hallucinations. What if we pass information in to do a repeated call, and somehow it deletes the old information? All kinds of crazy things can happen, so we do need to have some checks as we pull out of this to make sure things are in a sane state.

**[00:38:12]** Another way to do that would be — instead of a variable, if this was just access to an index, like a search index, we could do things like not allowing deletes or modifies, that only adding new data is allowed.

**[00:39:26]** There's not necessarily — if you remember last Monday, we talked about tools being able to return errors when they got into a weird state. In this case, maintaining this state is all within a separate Python process entirely, so it may be harder for us to strictly maintain that global state that's outside the process and inside this tool.

### 3.9 RLM Takeaways

**[00:41:07]** I really just want to — my goal in this is not necessarily to say this is what you should go rush to do in production. But the takeaway is to think about how you build search differently than maybe you might classically think about it.

**[00:42:04]** Imagine a situation where this Python REPL wasn't just getting Python code, but was actually getting Elasticsearch query syntax through the Python REPL. That could really change how we approach search — instead of rigorously tuning one search tool, we're more or less giving something open-ended.

**[00:42:50]** And then, everyone's talking about doing this with grep now. When RLMs came out, it was all about Python, and now it's like, should we just be using Bash and grep? That's sort of maybe supplanting that in the conversation.

---

## 4. Auto Research — Agent-Coded Search Ranking

**[00:43:30]** We're gonna talk about auto research. The idea here is we have some Python code, and we want to use coding tools to improve or modify it. We also want to use eval tools to evaluate specific queries.

### 4.1 The Reranker Setup

**[00:43:55]** We might have this `start` function — `rerank_wands`. It takes as an input this primitive `search_wands`. Which it can do kind of a fielded search with — the keywords. We also take the query. This code here searches the product name, uses an AND operator, and gets 10 top results, and then just returns the doc IDs of those doc results.

**[00:44:34]** We're hitting the reset button — we're moving on to a completely different topic. We're just gonna talk about using agents to optimize ranking code. Not necessarily agents themselves.

**[00:44:51]** Can we let an agent modify this code so that this piece of code will produce more relevant results according to the ground truth that we have of what's relevant and what's not?

**[00:45:07]** We've talked a lot about having agents in the loop. Well, what happens when we ask the agent to generate — based on all its knowledge about how to search this dataset — we just ask an agent: "generate code that will rank search results optimally." And then we take this code, some version of this that's been modified, and deploy that to production. The nice thing is we don't have an agent in the loop. We just have a set of code that an agent helped us produce.

### 4.2 Dependency Injection Pattern

**[00:46:58]** I like to think in terms of dependency injection. This `search_wands` is the primitive that is doing the underlying retrieval work. What we're kind of doing — why I call it re-rank — is this `search_wands` here is basically standing in for calling out to your Elasticsearch or something.

**[00:48:18]** The agent is not modifying this code, it's just using this code. That's the big takeaway.

### 4.3 The Eval Loop

**[00:48:56]** In this WANDS — Wayfair dataset — it's our furniture search e-commerce dataset. The agent can run an eval tool that takes this code and plays back all 480 or whatever queries, and tries to evaluate how good this code is at ranking this dataset.

**[00:49:28]** It then can propose a patch to modify this code. Which then gives us some new code, and we can evaluate it further, and just repeat, hopefully finding better and better code.

**[00:49:55]** If you recall, we were messing with NDCG and gotten anywhere from .54 for BM25 up to .61 — when we really cranked up the LLM as a judge. But all of those involved an agent in the loop. Here, we're just having an agent generate code, so we might not expect it to be as high.

### 4.4 Code Editing Mechanism

**[00:50:15]** Code editing is actually pretty straightforward. We have a tool that accepts this as an argument. The main thing that it's doing is "anchor and block until" — that's search for anchor. And then after that, search for block until. These are just strings to search for in the code that it's modifying. Take some action — replace is pretty common. And replace it, put in this text.

**[00:51:05]** Takes an edit. Open code, apply edits, ensure the new code runs, save code. We have a little bit of protection — there'll be errors if it doesn't actually run.

### 4.5 The Overfitting Problem

**[00:54:14]** Seems like an improvement. Seems like it just works. But — this is often what happens if you naively use Claude or Codex for this kind of work. You get a lot of this stuff.

**[00:54:31]** When you just run this on all the evals and tell it to optimize NDCG, it will happily do that. But no ranker that has all of these very query-specific rules — that's probably not that useful. There's hundreds of lines of stuff that actually gets generated into the rerank function.

**[00:55:00]** It's almost as if the code that's generated is: "if it's this query, return these exact results ranked by the correct ranking." If you took this and tried it on some query that wasn't part of that 480 eval set, it would probably fail miserably.

**[00:55:29]** And if you keep repeating this on a holdout, it just kind of wanders around. It's not actually improving. It may be getting better on the training data, but on holdout data — we're not making any progress, we're just overfitting to whatever queries the agent has to work with.

**[00:56:21]** Coding agents scour for information to achieve their goal. It's pretty frequent that someone goes and tries to optimize search with Claude Code or something, and you'll see stuff like this happen all the time.

---

## 5. Guardrails Against Overfitting

### 5.1 LLM-Based Overfit Detection

**[00:06:06]** What I've done — persisting in my stubbornness of having my own coding agent — is I have taken this Apply Patch tool, and I've basically added some guardrails to reject changes that I consider unreasonable or overfit.

**[00:06:58]** The first thing I do is just ask an LLM: "hey, does this code look overfit?" I often say you can use stop words and things, but does it look like it's doing a lot of query-specific work?

**[00:07:21]** I have a check — looping through here. There's a guardrail list of functions. One of the functions is call an LLM to see if it's overfit. And if the LLM thinks it's overfit, then we just say, okay, we reject it. This tool, apply patch, will return an error back to the agent saying it's overfit, or too specific.

### 5.2 Patch Size Limits

**[00:07:55]** The other thing I've found useful is to limit the patch size that an agent can apply. Another guardrail is a length validator — I don't let it apply patches longer than 10 lines and more than 120 characters in width.

**[00:08:16]** I do this in part to help the agent reason more carefully about the relationship between the changes it's making and the outcomes it's seeing. Think about this from a human perspective: if we wrote a thousand lines of ranking code and then went to look at what queries changed, it would be really hard to figure out the cause and effect. If we made a tactical couple of lines changed and saw which queries improved or got worse, it's easier to reason about why that might have happened.

### 5.3 Training vs. Validation Split

**[00:08:55]** Probably the main and most important thing — the training set I talked about, those are queries the agent itself can access. Can see the individual — how the NDCGs change at the query level.

**[00:09:11]** I also maintain a validation set that makes sure that the change does not go — the change has to improve the NDCG of this validation set by some eval margin.

**[00:09:29]** The difference here is the validation set — the agent doesn't know about the individual queries. The agent only sees the overall change up or down.

**[00:09:41]** In some ways, it's kind of progressive disclosure, but it's honestly kind of regressive disclosure, because we start with the most detailed information, the training queries, and then once the agent feels like it has a change that improves those training queries, it tries to apply them.

**[00:09:59]** This apply patch is almost more like a commit function. And these checks here are almost like pre-commit checks, if you're familiar with that verbiage in coding. And it will fail these checks, and then throw back to the agent and say, "no, you're overfit, your validation actually went down. You need to try again."

### 5.4 AI Coding IS Machine Learning

**[00:10:57]** When we're doing this AI coding, the way to think about it is this AI auto-research really is machine learning. We still need to take our eval data, have good splits, and control the visibility of that data to the model.

**[00:11:20]** Even if you go watch my haystack talk on auto research, there are even cases where validation data — you can overfit the validation data, because even if the agent can't see those specific queries, it will still keep brute forcing until it makes an improvement.

### 5.5 Results with Guardrails

**[00:12:08]** Once we put this in, you can start to see the validation checks rejecting things. I actually have a margin — it has to increase like .003 or something. So it's not making very tiny, incremental waste-of-time improvements.

**[00:12:37]** If we let it incrementally improve, it starts to generate code that looks more like this. You can see things like: we're searching with an OR query, we're getting two sets — title and description.

**[00:13:01]** The other funny thing is when I restrict the code length, agents love to cheat — so it's trying to compact as much as possible into that tiny change. It's no longer giving good descriptive code. It's trying to squeeze in to that 10 rows and 120 columns.

**[00:13:24]** We're getting title and document matches, and we're doing some interesting stuff. It's like — extra boost for this actually being in the title, 0.3 if it's in the description. It's getting these extra constant boosts. And then we sort by this new score.

**[00:14:22]** If we run this, you can see it does start to actually climb the validation set. This is actually a dataset that's held out from training entirely. And after 10 iterations, you get an even more sophisticated ranker.

**[00:15:01]** What's really useful when these things get complicated — I paste them into ChatGPT and have it explained to me.

---

## 6. Challenges and Limitations

### 6.1 Path Dependency

**[00:20:31]** One thing with auto research — it's gonna be very heavily influenced by the first edits that it chooses. If it chooses some early edits that seem to work well in that one situation, it may be harder to get back over to a different branch. Every time everything you've done in the past might influence the things that are coming in the future.

### 6.2 Limited by Primitives

**[00:21:24]** We're limited by the primitives. It's not gonna get any better than the BM25 or the embedding model under the hood. There's no magic thing that's gonna happen. If you have some kind of query understanding under the hood, it's really just assembling LEGO pieces really well.

**[Prasad Seemakurthi, 00:21:57]** When you say it's not necessarily creating additional features, but it's going to find out the best local maxima or minima that's possible for the given set of features. Is that the right understanding?

**[Doug Turnbull, 00:24:12]** Yeah, exactly. It's very similar to learning to rank in that way.

### 6.3 LLMs Default to Known Patterns

**[00:24:17]** It's always using a language model to learn how to generate search code. It tends to want to use existing, well-known knowledge — it's not gonna do anything too innovative.

**[00:24:36]** If I give this an embedding to generate code using this embedding backend and this BM25 backend, it almost always tries to do some reciprocal rank fusion, which is kind of the standard way of doing this. That makes sense, because the coding agent has all of the knowledge of how everyone has built search forever in its brain. And that's what it's gonna draw on.

### 6.4 Escaping Local Optima

**[Mario, 00:25:36]** The coding agent proves NDCG in the beginning, but then it quickly reaches a plateau. It seems the agent can get stuck in a local maximum.

**[Doug Turnbull, 00:25:53]** One thing that I've found helps is resetting. There is also changing the system prompts — every round here, the input to this round is the output from this round, and each round here is a fresh agent and fresh context.

**[00:26:26]** You can guide the agent to try specific things — you can participate in this. When people talk about auto research, a lot of times it's as much about humans guiding things in subtle ways.

**[00:26:41]** The other thing that I think is underexplored is how do you get one branch running and another branch running, and have them interact in some way? Do some kind of genetic algorithm thing — taking the outcome of one branch and the outcome of another branch. Like in genetic algorithms, you would breed them somehow and come out with a new ranking function.

**[00:27:33]** The final thing I've messed with — once you get to a plateau, instead, you can recurse this. The code that you generated can then be the primitive for another level of auto-research. And that might be — we created a new `rerank_wands` function that took this as an input. Or maybe we lie — and this is actually from a past round, hidden from it. We're composing it, not necessarily starting and continuing with that. That's another thing I've seen actually work pretty well, because it will start to innovate on top of it, and the past decisions are hidden from it.

---

## 7. Q&A: Claude Code vs. Custom Agent

**[Zenit, 00:28:56]** What's the main difference between just taking Claude Code over your own code and telling it, "here's our goal, change my code, run searches until it gets there, and here's your guardrails as well"?

**[Doug Turnbull, 00:30:13]** Functionally, there's not really a difference, and there's probably advantages to using Claude Code or Codex with goal to do this. I think the mistake most people make is they don't think enough about their setup.

**[00:30:30]** Even with guardrails, you have to be really careful not to have information leak into Claude. Some ways I've seen people do that — there's actually plugins and things out there people use, but they'll have ways of submitting runs to a server or something, or another process entirely, that then gives feedback on validation.

**[00:31:08]** On doing the entire system — there's absolutely no reason you couldn't also do the entire system. That's probably one advantage of using something like Claude Code or Codex, as opposed to doing something like this, which is fairly isolated to just ranking. You could actually set up the entire indexing pipeline and everything.

**[00:31:33]** The main downside is the trials are gonna take longer — re-indexing some data, searching it, re-indexing, searching it, versus just searching it. It's a trade-off: do you want a complete picture of the entire search process that will be slower to run, or do you want to isolate pieces of the search process?

---

## 8. Closing

**[00:32:37]** Well, really appreciate everyone coming. We're gonna have our final office hours tomorrow. Cogitate on this stuff.
