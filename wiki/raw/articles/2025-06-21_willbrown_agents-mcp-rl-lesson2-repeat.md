---
title: "Production-Ready Agent Engineering — Lesson 2: MCP + Production-Grade Agents (Repeat Session Raw Transcript)"
author: Will Brown
date: 2025-06-21
date_ingested: 2026-06-10
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: transcript-raw
tags:
  - ai-agents
  - mcp
  - tool-calling
  - async-agents
  - rag
  - security
  - observability
  - education
  - transcript
participants:
  - Will Brown (instructor)
  - Kyle Corbitt (co-instructor)
---

# Production-Ready Agent Engineering — Lesson 2: MCP + Production-Grade Agents (Repeat Session Raw Transcript)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** June 21, 2025 (repeat session)
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Primary transcript:** [[transcripts/2025-06-19_willbrown_agents-mcp-rl-lesson2-lecture]]

---

## Session Context

This is a repeat/rerun of Lesson 2 for students who missed the original or wanted a second pass. Same core content but with additional Q&A depth, especially on RL topics, security patterns, and async best practices.

## Additional Content Not in Primary Transcript

### JSON vs XML for Tool Calls

**[01:19:27]** I tend to like XML better when I can use it, just because it's easier to parse on the human side. There are cases where, especially if you're writing nested logic — if one of the arguments is going to be code itself, JSON nested inside JSON is doable but it gets nasty and introduces a lot of failure. If one of the arguments for your JSON needs to be a JSON argument as well — I think XML is your top level thing, often convenient for blocking out main sections. If you're using one of these tools like instructor or one of the native parsers, Pydantic doesn't support full XML. The way I typically do XML is with regex parsing. Regex and XML fit together quite nicely. If you're going from scratch, that's a pretty good way to do it.

### Async: Progress Tracking & Incremental Results

**[01:34:11]** Tqdm is a library for having a progress bar — a counter that tracks how many of your sub requests have finished. You can also use the `as_completed` pattern where, as things finish, you can have certain things happen. For example, every 100 steps — let's say you're doing thousands of requests — you save your current outputs so you have some fallback if your program crashes. You can also use this to return things to the agents — if these are running as parallel processes, you could have the agent see which tool calls have finished at each step, send these to the agent, the agent can now see them in context and continue on, and maybe submit more tool calls each turn.

**[01:35:31]** Claude Code is starting to enable some of this where you can have background tasks that take longer than a few seconds to run. Some of these are sub-agent level things. You could have tasks running truly in parallel with some sort of tracking mechanism — when one task finishes, make sure we update the global state about which completed tasks should be shown to the agent.

### Sub-Agents vs Parallel Calls

**[01:31:17]** When would you want to enable a sub-agent versus just enabling parallel calls? The versions of sub-agents that make the most sense initially are essentially single-turn tools or structured smaller agents that are doing a very specific thing. Think of sub-agents as tool calls that may take some time to finish. Just as you want your tools to be nice and robust, these sub-agents need to be nice and robust. We want to make sure we have evals or test cases for these sub-agents. If we can rely on our sub-agents — we know they do their subtasks quite well — then these just become tools to be used by the primary agent.

### Prefetch RAG with Input Caching

**[00:38:22]** Prefetch RAG can be good if your docs aren't very long and if you want to leverage caching for multiple questions. A lot of LM APIs offer this caching feature where you can — once you read in a big input prompt once, you can save it so that the next time you ask the same prompt prefix, you can fetch that cache at usually about 10% of the total cost. If you wanted to take advantage of large input caching for smaller numbers of documents that you know you're going to be answering lots and lots of questions about, that is one case where doing this Prefetch RAG can make sense because the whole prefix of the final input to the LM is saved. The only thing that's changing is the question that goes at the end. This also mostly works in cases where you're not doing multi-hop search — you assume that there's one round of search that will find everything you need, and then this goes directly to an LM query.

### File System Memory Patterns

**[01:08:16]** File systems are kind of one of the more natural data structures for LLMs to use. LLMs are very happy to hop around terminal and open up folders. Sometimes they make a mess because they don't remember where things are. CLAUDE.md is really important — make sure it describes the structure as well as some meta-level rules of where things should go and how the LM should take notes for itself.

**[01:08:47]** Patterns that help with LLMs remembering to take notes in the right spot:
- Every time they do a feature, they have to write a design doc first. The design docs go in this folder.
- You can have a backlog / to-do / finished folder for design docs.
- Have rules telling your LLMs to update the README as you go — every time you finish a feature, update the README.
- These patterns create a self-documenting codebase where the LM has a persistent reminder in system prompt of how to keep track of what it's doing.
- It is kind of up to you to decide how it should be doing that. They're not great at figuring out the ideal way. But if you commit to a way, they'll follow it.

### Security: Reward Hacking & Read-Only Defaults

**[01:16:12]** Deleting files happens. There's a lot of things that sometimes agents will do that you can't imagine why they would do it. But especially for things that are really hard challenges for agents — really hard coding problems — sometimes they will just kind of do whatever. Also reward hacking behaviors: things that are kind of like deleting test cases, for example. Agents have been trained to pass test cases, and if they're not passing a test case, sometimes their way of doing it will be to edit the file in a way that deletes the test case.

**[01:16:50]** We're not yet at a point where we want to remove responsibilities of code review or testing. Having agents write tests is often useful. Any sufficiently important code, even if you're using LLM significantly to help with writing it — you still want to think of humans as being the owners of the code. Because humans are stakeholders. You can't fire an LLM. An LLM cannot get in trouble if something is bad. It's a thing that only exists as an agent in the runtime that it's doing the action for.

**[01:15:34]** Default to read-only for agents and having any write actions being — really be very careful about what sort of write actions to allow. This includes anything that's creating a file or code execution.

### MCP: Tool Design & Auth

**[01:58:30]** Tool design is just code design. Tools are just software. Some MCP servers are not great, just as some code products are not great. I would not necessarily trust auto-generated ones — you can generally trust the official reference servers, which are pretty solid. Auto-generating MCP servers is hard for the same reason that a lot of code gen products suck — code gen is not a fully solved problem.

**[01:06:50]** MCP servers can just be OAuth resource servers. MCP recently released first-class support for authorization. Originally it was essentially just optional and offloaded to the user to handle auth. It's a moving target.

### Agent Evaluation Deep Dive

**[01:18:49]** How do you evaluate agents? At the core, agents are just programs that are going to be solving a problem. What we really care about in most cases are the solution we get as well as the resource utilization of the agents. Agents that take too many tokens or too many tool calls — these are things that we want to evaluate.

**[01:19:31]** The completion can be just the one final answer we evaluate, or we can evaluate the whole sequence — evaluating the process, the actions taken. One thing I'll do a lot is formatting rewards for tool calls — check what fraction of tool calls the LM is getting the correct format for and not creating errors.

**[01:20:09]** For very open-ended tasks, LLM-as-judge is the most powerful tool for doing fuzzy evals. String similarity — both text and embeddings — is also useful when you have some kind of ground truth.

**[01:20:46]** Naive LLM-as-judge — you don't want to be naive. What I would not do is: agent does a thing, send it to the judge, be like "hey, is this good or not." What you can do is ask granular questions:
- Are there any turns of this trajectory that seem completely useless?
- Did the LM seem to make logical steps after each previous thing?
- Did the final answer have 5 paragraphs?
- Are links cited in line as opposed to at the end?

These are properties of the final thing that we can granularly write down, similar to how you would write a system prompt. Think about all the things you want your LM to do — anything that's a sentence in your system prompt can also be a piece of your eval. Each of these instructions can become something that is judged by an LLM at the end.

### RL Resources & GRPO Details

**[01:17:41]** RL resources:
- Nathan Lambert has both a really good blog (non-technical, mostly concepts) and rlhfbook.com (in-progress web textbook, very good overview of all things LLM RL)
- Lillian Wang has a good blog
- Mutual Information (YouTube channel) — doing the Sutton and Barto textbook in video form. If you like 3Blue1Brown videos, you can think of it as 3Blue1Brown for reinforcement learning.

**[01:22:11]** GRPO — removing KL: it's really good for memory if it allows you to do more with less, in that you can get rid of the reference copy of your model and just have the policy model being trained online. I am a little skeptical that you can totally get rid of KL. There have been a lot of papers with conflicting results.

**[01:22:50]** Default approach: pretty small KL term with online updates of the reference model. This is a way of interpolating between KL and no KL penalty. If your reference model was updating every step, this is almost as if you have no KL penalty. As you increase the frequency of your reference model being updated with the policy model, this washes out the influence of the KL penalty — because now it's just becoming about the local change rather than drift from the start. This is a knob you can tune.

**[01:23:49]** Random Rewards paper: it's a good paper. It points out some funny things with Claude models. My takeaway is just we have a lot to learn still. People are spending too much effort doing experiments on the same math data sets where these models are already saturated.

**[01:24:16]** Entropy collapse: one thing that we know happens sometimes with certain RL configurations. It's kind of like artificially lowering temperature — not exactly, but similar. As an analogy, maybe some models just do better at low temperature, they're more reliable. RL, even without reward signals — just the fact that you are applying this KL penalty at each step can have the effect of penalizing things that are out of distribution or more random. You're kind of collapsing down into the most likely behavior. Sometimes that most likely behavior is better.

**[01:25:36]** Structured generation during training: you can use Outlines during training. What you can do is turn off the possibility of your model ever doing something that does not follow the schema. If you're going to be using structured generation at the end, you should also use it during training and evaluation. You could have some samples use it, some not, and still use format rewards.

**[01:27:17]** Verifiers baseline evaluation: there's built-in GRPO support. You can take any model, expose this endpoint, or pick your favorite LM API that's OpenAI-compatible. The environment is just like any agent framework — essentially the tool-called while loop with evals plugged in. The same reward functions you use for RL can be used for getting the baseline. Take your model, either locally hosting the LM endpoint or finding a provider, run your eval set on your environment where you're doing rollouts, get scores. What comes out is a dataset of your rollouts with scores, and the average of these scores is your baseline.
