---
title: "Production-Ready Agent Engineering — Lesson 1: Agent Patterns and Principles (Lecture Transcript)"
author: Will Brown
date: 2025-06-17
date_ingested: 2026-06-10
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
type: transcript
tags:
  - ai-agents
  - reinforcement-learning
  - tool-calling
  - context-engineering
  - education
  - transcript
related_article: articles/2025-06-17_willbrown_agents-mcp-rl-lesson1.md
participants:
  - Will Brown (instructor)
  - Raymond Weitekamp (co-host)
---

# Production-Ready Agent Engineering — Lesson 1: Agent Patterns and Principles (Lecture Transcript)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Date:** June 17, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]

---

## Course Introduction

**[00:02:29]** I know people are coming from a lot of different backgrounds as well as kind of like focus areas. And I'm hoping that the whole thing will end up being pretty much like a holistic overview of both the RL stuff and the agent stuff.

**[00:02:45]** One of my perspectives. Part of the background for the course is that there's a lot of things about the 2 topics that in my mind are very similar, but are often treated as very different.

**[00:02:50]** A lot of the people who are researching RL and writing about it are not thinking about the agent element of it.

**[00:03:01]** And then a lot of people who are working on agents are just thinking about the programming with APIs element, and not necessarily about the model capabilities or optimization.

**[00:03:18]** The theme of the course is intended to be this kind of bird's eye, but also getting into the weeds view of what does it really take to make an agent that's good. What are the techniques that work? What are the things that are good patterns and also dangerous patterns? Because there's certain things that I think a lot of people are tempted by that get unwieldy pretty quickly. Then there's also a lot of clever tricks that make things much better. And reinforcement learning is very much a thing that I am very excited about.

### Engagement & Format

**[00:04:12]** Questions in the chat is great. We'll have some helpers who will be looking over the chat and kind of flagging and grouping questions, and then we'll pause every once in a while.

**[00:04:58]** The plan for today is like, I'm probably gonna spend about the 1st hour kind of going through a notebook I prepared and then I want to do some kind of interactive hands on stuff towards the end, where we kind of like pick some versions of the things we talk about and like go a little more in depth, based on people's interests.

### Favorite Agent Benchmarks

**[00:05:44]** Favorite agent benchmark. BFCL v3 multi turn. It's just kind of like a standard multi turn tool calling benchmark.

**[00:05:58]** There aren't enough great ones. A lot of benchmarks are still very much in the single turn world, even ones that feel like they should be agent benchmarks really are not.

**[00:06:09]** Claude's Pokemon, honestly, is a really good one. Whether or not a model can coherently play Pokemon, even in any harness, is a good test.

**[00:06:28]** On compute credits — those will be coming very shortly. Once we freeze the sign up list so we can do everyone at once. Nothing this week should require GPUs. This week will be mostly about stuff that can be done in terms of APIs, as well as evaluations. As we get into next week we'll start doing a little more experimentation with training.

### The Best Eval

**[00:07:10]** You can do a lot of stuff with looking at benchmarks to try to get a feel for which model is good. But they're all really different. They all have different things that they are good at. And the real way to tell if a model is going to be right for your use case is to build a version of your application, your agent, that can be evaluated.

**[00:07:42]** LLMs are very powerful. But they're still machine learning models. And machine learning models are very good at things that are in distribution. People are always hoping that LLMs will just generalize out of distribution — sometimes they do, but it's also harder to find what out-of-distribution generalization really means. And so the most concrete thing is just like, let's measure them in distribution. Let's optimize them in distribution, which means our evals do kind of need to capture the distribution.

**[00:08:34]** For any given application you do kind of want to be thinking, how do I create my benchmark? There's not that many benchmarks, but also making a benchmark is not that hard. And there's a lot of tricks that you can do to quickly make benchmarks. This will be a thing we do quite a bit in the course — make your own benchmark, explore lots of different ways to create questions, spot check both with programmatic methods as well as manual inspection.

---

## Model Ecosystem Overview

**[00:09:36]** Today is going to be like a speed run from basically first principles up to the point where we're actually building things that are using some fancy tools.

### Package Management: UV

**[00:09:47]** I'm going to be using UV as my package manager. I moved to it about a year ago, and it's great. It's essentially just a better pip. It makes installing things like 100 times faster, and it's much better at automatically resolving dependency issues.

**[00:10:19]** The practice that I would encourage you to follow is every project, every code base should have its own virtual environment. UV makes this really easy and really fast.

### Primary Agent Models

**[00:10:41]** Having some sort of OpenAI-compatible API set up — whether or not it's actually OpenAI, or something that just is called OpenAI — is totally fine.

**[00:11:05]** Especially as we get towards the RL section, I am a very big fan of DeepSeek. The newest DeepSeek V3 model — not R1. R1 is good for some things, but for the things that I think will be useful to most people, it's good to have a model that's not just a reasoner model.

**[00:11:25]** DeepSeek V3 is nice because it's super cheap — about the cost between GPT 4.1 Mini and 4.1 Nano. It's a dirt cheap model as far as smart models go. It's also a model that you are very permissively allowed to train on the outputs of. This is a thing that comes up a lot in practice, especially if you're working in enterprise settings where if you want to do fine tuning, you do have to be careful about where you're getting your data from.

**[00:12:15]** GPT 4.1 is probably a very good starting agent model for many people. Chain of thought is really useful as a reasoning pattern. But it's not always the sort of thing where you really want to use a heavy duty reasoner model for everything — because that incurs higher costs as well as latency. As you go up towards scaling many tool calls, sometimes the tools are essentially taking the place of chain of thought where the reasoning chain is not just one long message, but it's lots and lots of small ones.

**[00:13:19]** The other 2 that are kind of very popular in the middle models are Claude Sonnet and Gemini 2.5 Pro. People have very strong preferences about these models. I think you should just pick one that you like that works for you and your budget, but also in terms of which providers you're able to access.

**[00:14:07]** Most of what you care about is having a model that is very good at being an LLM. More so than a model that has all the answers to every question in the universe. Because what we care about is models that are doing work. And a lot of the work people want models to do is not actually that intellectually difficult, but it requires interacting with complex systems. And so the ability to reliably call tools is really important.

**[00:14:45]** The ability for models to maintain coherence over multi turn interactions is very important. This is a pitfall that a lot of open models fall into where they were over-optimized for academic benchmarks because they weren't really going to be sold anyways. And so a lot of them don't function that well as agent models, because a lot of benchmarks are very much single turn question answer.

### Helper Models

**[00:15:08]** It's also good to have a go-to smaller, cheaper helper model — a model where you're less worried about burning through tokens. Less in terms of a primary agent model and more as a model that is going to be useful for looking and finding answers through data. A model that's reliable at answering a question given the context that contains the question is a very useful primitive for building up these things — both for LLM as a judge as well as for synthetic question generation as well as for using models as a component of your pipeline.

**[00:16:20]** It's good to have a model that you go for and reach for which is your helper model. That you can kind of comfortably plug into your pipeline if you want to have things look at lots of docs that are going to be in total a lot of context. And you want to have a model that's going to read 10 websites at a time. It is often best to offload this to a helper model.

**[00:16:54]** GPT 4.1 Mini and Nano are good for this. Gemini 2.5 Flash, Claude 3.5 Haiku. As far as open models go, Mistral Small 3.1 is quite powerful and is very permissively licensed. If you were going to pick only one open model to do everything with and you wanted it to basically just work for everything, that's a pretty good one.

**[00:17:28]** The Qwen models are nice. They're very popular among researchers who are doing fine tuning, partly because they're really good on benchmarks out of the box. Gemma is similar. For doing research experiments, it's nice to have access to a model suite where you can measure how things change as you go up the model suite. This is one big reason why the Qwen models are very popular — they have lots of sizes, from 0.6B up to 200 something.

### Reasoner Models

**[00:19:17]** Models that are good to know about and have their place but don't use all the time are the reasoners. The big Claude Opus.

**[00:19:29]** The reasoner models are really nice as single hard problems, like as a chatbot in an interface where you want to be typing a question and having a model think really hard about the context you give it and give you a really great answer at the end. In the context of an agent pipeline, you want to be very surgical with using them, because they will add a lot of latency. And if you're doing things that involve many tool calls, some of these models are not very good at managing context or not thinking too much.

**[00:20:13]** It's maybe hard to justify for anything that's a consumer facing agent where you were hoping to charge reasonable amounts.

---

## Tool Calling & Structured Outputs

### Chat Completions vs Responses API

**[00:22:13]** OpenAI chat completions — this is what we're going to be using in a lot of the applications for the course, just because it's very standard. Almost every LLM is accessible via chat completions. It's missing some bells and whistles, but it's also a nice clean slate of pieces for building whatever you want on top of it.

> **⚠️ Note (2026-06):** This recommendation reflects the landscape as of June 2025. With GPT-5 and later models, OpenAI has shifted toward the Responses API as the primary interface, and Chat Completions support may be incomplete or deprecated for newer models. The portability argument still holds for non-OpenAI providers, but for OpenAI-native workflows, Responses API is now the expected path.

**[00:22:55]** Multi-turn interaction with the system is kind of what makes something an agent as opposed to just a question answer or single turn chatbot. And so state is something that we'll need to be very careful about. If you don't manage your state, and you try to treat something like a chatbot without giving it the information it needs to know where it is, it's just a language model that has been given some context in a vacuum.

**[00:24:07]** OpenAI Responses API — it has some pros and cons. There are some very nice convenient features for abstracting away some of the state management, especially for things like tool calls and for models that have thinking summaries.

**[00:24:37]** If you don't know that you only want to use OpenAI, I would encourage you to build things with chat completions. They are generally more like — most libraries out there build around them in terms of agent frameworks as well as most inference providers support them for any model. So you can talk to Gemini or Claude via OpenAI chat completions. This is not true for responses.

**[00:26:18]** Deep Infra is one kind of open or general purpose provider of open models. They serve a lot of models for pretty cheap. Chat completions works great, but responses — everything breaks because it does not implement the Responses API. Because it's not actually OpenAI.

### Structured Tool Calls

**[00:27:00]** Tool calling and structured outputs — this is going to be very important for anything agents.

**[00:27:13]** Our setup is we're gonna pretend we have a weather tool. We tell the model in the prompt: you have access to the tool, here are the arguments. If you just ask it without kind of telling it to actually tool call, it's just a language model doing things in tokens, and so its natural response is, can you clarify?

**[00:28:33]** We can be a little more explicit with how we prompt it — just return the JSON. And here it doesn't think, it doesn't say any words. It just returns the JSON. So it's not doing chain of thought. It's not doing any sort of planning. Its first token that it outputs will be the start of the tool call. And this is how a lot of function calling APIs are implemented.

**[00:30:07]** Especially for cases where there's lots of tools, or the tools require some planning to use, you don't necessarily want to have just the function output.

**[00:30:34]** Here I'm telling the model to always think step by step before calling a tool. This is kind of the pattern that we want — we want models to be thinking and then acting and then thinking and then acting and iterating on this.

**[00:31:35]** The old school OpenAI way is to use this whole complex schema of the tool where we just say, okay, this is what we mean by the tool. This is the instructions for filling out the function call.

**[00:32:05]** People have been asking about how do you ensure these structured outputs. OpenAI will essentially do this behind the scenes if you pass things in in a particular way. There's also a number of backends for structured parsing called Outlines and XGrammar — the 2 most popular ones. That essentially are applying a Regex mask to the token. It's kind of like a little beam search thing where it's looking at different valid token paths, and it's only sampling ones that are valid amongst the schema. This is a way to get kind of like 100% guarantees.

### Pydantic for Structured Outputs

**[00:33:45]** Another way to do tool calls that is, regardless of which back end you use, I think a good way to specify structured outputs is with Pydantic. So Pydantic is just like a fancy typing library for Python, where you can create very easily these complex nested structures of what you want your thing to be.

**[00:34:04]** One thing that's important here is ordering matters. For chain of thought, you do kind of need your thinking to be first. The model will not benefit from thinking if it's doing it after. The thinking needs to happen before the tool call happens in order to affect the tool output. And so specifying it like this in your schema ensures that the model is writing the thinking first.

**[00:34:55]** Transformers are kind of only moving linearly, adding new tokens. And so you want anything that's planning or thinking to be something that happens before the specified action.

**[00:35:19]** We are parsing it using OpenAI's built in Pydantic parser. They have in their Beta version of chat completions — you can do parse directly. And so the thing you get out is a Pydantic object where you could dig into these things.

**[00:36:11]** `Literal` is a very useful primitive to be using in your agent applications. Anything that's like determining what fields you care about in a very typed way is really useful for making these applications robust, because you can get a guarantee this way that the output of one thing will flow nicely into the next thing.

---

## Key Takeaways

1. **RL and agents are two sides of the same coin** — the course bridges the gap between RL researchers who ignore agents and agent builders who ignore model optimization
2. **Build your own evals** — benchmarks are useful but insufficient; in-distribution evaluation is the most concrete approach
3. **Start with non-reasoner models** — GPT 4.1, DeepSeek V3, Claude Sonnet for primary agents; use reasoners surgically for hard problems
4. **Have a go-to helper model** — GPT 4.1 Mini/Nano, Gemini Flash, Haiku, Mistral Small 3.1 for cheap bulk processing
5. **Use chat completions over Responses API** — more portable across providers and frameworks
6. **Pydantic + thinking-first schema** — structured outputs with chain of thought requires thinking fields before action fields in the schema
7. **Tool calling is the core agent primitive** — reliable tool use matters more than raw intelligence for most agent workloads
