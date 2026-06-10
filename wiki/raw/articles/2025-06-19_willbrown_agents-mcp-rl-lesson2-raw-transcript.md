---
title: "Production-Ready Agent Engineering — Lesson 2: MCP + Production-Grade Agents (Raw Transcript)"
author: Will Brown
date: 2025-06-19
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

# Production-Ready Agent Engineering — Lesson 2: MCP + Production-Grade Agents (Raw Transcript)

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Co-instructor:** Kyle Corbitt (CTO, OpenPipe)
**Date:** June 19, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]

---

## Course File & Setup

**[00:02:28]** Yeah. And so for the course file for today, they are in the Github, which is linked in the general section above a little bit.

**[00:02:47]** It's my github with agent engineering. I can paste this in the chat. Just so people have it right here.

**[00:03:00]** So that is, the notebook will be with you today. And then a few things are not in the notebook. They're just going to be like, live demos, with some other programs.

## Lesson Focus: From Demo to Production

**[00:03:05]** So the top focus for today is going to be kind of how do we take things from demo stage super notebook like running in us in the loop to like what is, what are these things actually look like in production? What does it mean to productionize an agent?

**[00:03:28]** Kind of how do we apply ideas from general software productionization to make agents that we can actually kind of reliably deploy, and that we kind of know what the right considerations are going to be for both, improving them as well as as just making sure that they kind of work well and are stable and are able to integrate into real world systems.

**[00:04:01]** The kind of themes I want to break this down into are some general kind of software best practices and how they especially relate to agents. Then talking about kind of higher level system architecture, things in terms of kind of where is code going to live? And how do we kind of monitor the code and logging and whatnot? Then, also kind of security considerations and reliability.

## Type Hints & Strong Typing

**[00:04:25]** I wanted to kind of revisit our discussion from typing like type hints and strong typing, dynamic typing from last time and talk a bit about Python.

**[00:04:34]** Python does not require you to use types. Python is perfectly happy to let you just throw variables around with names and the program kind of figures out what type they will be as needed.

**[00:04:47]** In general, this is like, I see a lot of people doing this. I think people have started to kind of move away from this as a default practice. I think it's very good to not do dynamic typing to actually like strongly require type hints. And I wanted to show an example as to what can go wrong.

### The Cumulative Product Bug

So this is a function that is just taking a cumulative product of numbers. So this is like, if you think of investing like you have returns or some number that's going up by some multiplicative factor every day you want to have cumulative returns as opposed to just the daily like yesterday versus today returns. And so the way that you do this mathematically is you're just taking the products over all these things. We were starting at one, and we are accumulating the total return by multiplying, and we're returning the list of final returns.

**[00:05:36]** We are not specifying a type. Here, we're just saying, okay, it's a list. And that's fine for this case. It works just fine.

### LM Integration and Type Mismatch

**[00:05:42]** Here's a we might want to integrate this into an LM program where we have like, there's some upstream stuff. The LM is going to be saying, okay, the prompt was the value yesterday was 100. The value today is 300. Return just the number of the growth multiple. It says 3. Great, awesome. 3 seems reasonable, right?

**[00:06:07]** Anyone see what's wrong? What's gonna happen when I run this function?

**[00:06:32]** I'm grabbing the content. I'm printing it. It says 3. So the return is 3.

**[00:06:36]** Right? So it's a string.

**[00:06:40]** And the code actually runs just fine.

**[00:06:43]** But it's doing 1, 3, 6. Then in Python, if you do 6 times 3, you get a bunch of threes, because Python has a lot of these things that are like kind of fun that you can do with typing sometimes, but they also can be the cause of lots of sneaky bugs.

### Type Hints as Defense

**[00:06:54]** Especially for any production element facing code, I think you always want to be using type hints as well as they play very nicely with structured output. So as you have your agents doing more complex things — we talked a lot about structured outputs last time — it's kind of a rule of thumb. And so that's kind of just like the LM way of doing strong typing in Python.

**[00:07:04]** And so here, now, we're actually going to be enforcing that these are a list of floats. So this would flag something in the code. There'd be a type error from your type checker if you were not doing this.

### Test Cases as Frozen Intentions

**[00:07:21]** And so here we're good. Then we also like can write test cases. LLMs are great at writing test cases. I think this is a thing that more people should be doing. Especially when you're writing programs that are going to be changing a lot, sometimes like, especially if you have an LM that's writing a lot of code in your code base. Things can go wrong very quickly, and having test cases is kind of a way of freezing the logic, or like the intention of your code where you can just tell your LM what it's supposed to do. The test case need to reflect this. And then, if something changes where another function is now broken, this is a way to kind of have an early warning that something has gone wrong.

**[00:08:25]** And so these pass, which means they did get a type error, which means that our function would give us an error if we were to pass the wrong type.

**[00:08:43]** The errors are bad in general, but like often you want the error — the errors are just like your signal as to whether something has gone wrong. And so, thinking very carefully of like for each function, what's your input type spec? What's your output type spec?

## Pydantic, Instructor, and Structured Outputs

**[00:09:11]** Any call to an LM has some schema of what's going into it. Maybe there's some reformatting. Maybe there's some other prompt management stuff that goes under the hood. But in terms of the program logic, there's a function that's being called that is going to be called from code. This will get translated into a single query to one LM.

**[00:09:21]** LLMs natively are taking in text as tokens and outputting tokens. LLMs themselves don't have a native notion of types, but this is where all these things like Pydantic and instructor and outlines, and these parsing tools that are available, Json mode — the job of these and the way that we should think about these is as our mechanism for translating LLMs which operate over tokens into the world of types where our programs are operating over very explicitly typed objects.

**[00:09:46]** So that we can know that the right types of things are being passed through our program, which is kind of essential to be able to keep our sanity as programs scale to larger complexities.

### Instructor and Provider Compatibility

**[00:11:21]** It depends on the provider. So instructor is kind of like a catch all for a lot of different under the hood methods. And it's going to depend on what the provider has.

**[00:11:40]** For example, some LM Providers will natively support direct structured output generation. Usually there's some degree of prompting that is done, especially in terms of the Json schema. Sometimes this will have the actual type. Sometimes it'll just be like return a valid Json.

**[00:12:21]** If you're not using one of these wrapper tools, you should do what we did in the last lecture, where you are making it very clear in your prompt what the return format should be. Examples are really useful there.

**[00:13:06]** In terms of what to use: if you're working with open models, you probably want to use outlines with the LM. If you're working with OpenAI all the time, then you probably want to use OpenAI's default. If you want to write code that is very portable between lots of things, instructor is nice. But it kind of depends on the exact software stack you're working with.

## Tools Are Software

**[00:13:33]** This kind of brings us into thinking about tools and so, tools are really just software. They're software that's going to be used by LLMs, they're functions, and everything about software testing and software best practices applies here as well.

### Constrained Generation (Grammar Masking)

**[00:13:53]** There are certain mechanisms that can guarantee that the model does output valid structured data. The way that they do this: if you're familiar with how Regex works, where there is this kind of context-free grammar sort of tree that is being parsed where there's only certain valid paths.

**[00:14:06]** Outlines with the LM — what it does is it will compile the schema you give it into a grammar. What this grammar really is: it's this way of masking out certain tokens, such that these sampling paths allow — because the LM is just every next token there is a probability of what the next token is going to be.

**[00:14:33]** Based on the grammar, some of these tokens are not allowed because they would violate the schema. And so some of these tools — their approach is to apply masking to these distributions based on this compiled grammar, such that you literally cannot sample an invalid schema.

**[00:14:39]** This gets a little complicated. The other option is some will do a much simpler thing, which is like you keep retrying.

**[00:15:00]** Sometimes you will have this happen, but generally I find that once you're using a strong enough model it works well.

**[00:15:19]** Outlines and XGrammar are kind of the 2 open source projects that have a lot of academic literature behind them. SGLang is a vLLM alternative that also kind of has its roots in structured generation. That's what the Sg in SGLang stands for.

**[00:15:46]** I think for applications, it's usually better to think of this as an abstraction where you don't need to worry too much about how it works under the hood. You just need to kind of get comfortable with your tools, test them, understand what sorts of prompts work for you with those tools in small situations, and then kind of build on top of that.

## Calculator Tool Demo

**[00:16:23]** In terms of tools, this is a very simple calculator tool. The idea is this calculator can take in an arbitrary expression that is contained in these characters. These characters that we're going to basically say, the LM can give us a calculator expression. We're going to disallow any character that is not one of these. So anything that's not a number or one of these mathematical operations, we throw it away.

**[00:17:08]** And then what we're going to do is we're going to use Eval. Eval is a thing you can do in Python that is very convenient and also very dangerous. Here we are pretty safe because we're filtering everything. There's nothing that can go into Eval. But Eval can execute arbitrary code.

**[00:17:27]** Sometimes, if you're testing a thing, and you kind of trust your LM, and you know what the prompt is going to be, you can see what the tool is doing, you can watch it, you can make sure it's not deleting important files. Then sometimes it's fine to trust this. There's then there's a number of degrees of sandboxing you can do.

### Tool vs No-Tool Comparison

**[00:18:44]** I'm writing a prompt and I'm going to give this prompt to an LM. I'm bringing back the OpenAI Agents SDK that we touched on last time. You just wrap any tool with an Async function, put this decorator for function tool on it, make sure the doc string explains how to use it.

**[00:19:23]** The first version of this is running it with the tool. And this is the output: 0.007704.

**[00:19:34]** Then without the tool — its answer was different.

**[00:19:40]** So the other one under the hood is calling the tool in the agent loop. And this is its final answer to the user.

**[00:20:14]** For the next one I took away the calculator, and so you still have the agent without the tools. It's just not a very useful agent, because it's just an agent that does nothing besides give an answer.

**[00:20:25]** In this case, I'm kind of surprised how close it was. Because I'm using 4.1 nano, which is a very small model. But it's not right. It's off by a little bit.

### Math Tools and Code Execution

**[00:20:39]** Math tools, anything where you kind of need really fine grain calculation — people love to benchmark models on math. I think the important piece of LM math skills is about reasoning through problems and understanding the pieces of them, but generally anything beyond pretty simple calculations, it is generally going to be safer if you at least give the LM the option to use tools.

**[00:20:58]** This calculator one is a very simple tool, but generally like, if you give them all the ability to write and run code — this is going to be one of the if you're building a general purpose agent that can do lots of things. Most tools can be written as code.

**[00:21:38]** There's a lot of all sorts of things you could do here. If you're using Eval, we'll touch on kind of fancier code bases a little bit later in the lecture. But the idea is that the ability to run code and execute code is very convenient.

**[00:22:03]** Tools you want to use that are in already code form — the branching factor of the sort of thing the LM might do with it is larger than the number of tools you want to enumerate. LLMs generally perform best when the number of tools you give them is not crazy large, like smart LLMs can probably handle few dozens of tools just fine. But if you wanted to give an LM like a thousand tools, this is gonna get silly.

**[00:22:25]** But if it's kind of writing its tools on the fly, it's much easier. And so this is the pattern you see a lot of the kind of popular agents adopt, which is like, as I just mentioned in the chat, Manus does this sort of thing as well.

### Tool Count: How Many Is Too Many?

**[00:22:53]** Part of this is going to depend on your application areas and your kind of explicit goals for the agent, as well as how much do you trust it.

**[00:23:08]** If you are in the situation where you're on a server that you kind of are willing to let the LM make a mess, it's kind of fine to give the LM more permissions and less explicit tools. If you're in a situation where your LM is running on your work computer, you probably don't ever want to give the LM full system access.

### Model Behavior Differences

**[00:24:44]** OpenAI Codex has been heavily optimized to use the terminal. It does terminal-based commands for almost everything. It's also kind of like a safe model in that it's less likely to kind of go crazy.

**[00:24:55]** If anyone played with one version ago Gemini 2.5 Pro — it would write everything, every function of a 10 line comment, it would make a million scripts that it would never use. It would just very code happy to just churn out tokens and make a mess.

**[00:25:21]** You do kind of need to know what model are you working with. There's a sense in which models are trained to behave in certain ways with tools. And this can be an important part of testing your setup with different models.

## Async Processing

**[00:25:44]** The next big concept is Async processing. Async I/O is a Python built-in library for handling things in parallel processing.

**[00:25:53]** If you are familiar with computer architecture — computers have threads and processes. Processes are fully isolated things. Multiple threads within them are kind of like programs that are taking turns in little bitty steps.

**[00:26:22]** Especially for any sort of network request — you're just kind of like busy waiting. When you send out a request, the piece of your computer that sent the request is just sitting around doing nothing. And the work is happening somewhere else. The work is happening on a remote server, and you can do many of these in parallel.

### Sequential vs Async Demo

**[00:26:35]** For example, we're going to create a bunch of different prompts: who are the most famous players of all these different sports? We're gonna use typing again to make sure the schema is being followed.

**[00:27:35]** It's taking its time. It's a little slow. And you could imagine if you had an agent that was doing multiple requests at once, or you have many users that are active, you don't want to be doing this.

**[00:28:02]** Jupyter as a notebook is already using Asyncio under the hood. So Jupyter is already kind of taking advantage of the event loop in Python because of the way that it kind of operates like multiple different pieces of the program going on at the same time.

### Gather and Semaphore Patterns

**[00:28:28]** Same idea where we are just putting Async in front of these things. Async in front of a function just means this is an asynchronous function, and it doesn't return right away. You have to await the return.

**[00:29:39]** To actually call them, what we do is gather. Gather is just saying, these are our tasks. These are objects. When we call gather, we are telling to actually run all these functions and return them as they finish.

**[00:30:02]** This whole thing took 2.6 seconds as opposed to 19.5. But it's doing the same thing. There's no difference in the logic here. The order is the same. It's just that we're doing them in parallel, because the slow thing here is not the program running. The slow thing is the LM response to a request.

### Semaphore for Rate Limiting

**[00:30:51]** A semaphore is a pattern for putting a global throttle on the number of async requests that are active at a time. Here we're just saying 5. So at most 5 parallel requests can go at once.

**[00:31:21]** The synchronous way of doing this would be batching — explicitly saying, I'm going to send 5, wait for 5 to finish, then send the next 5. This is kind of not ideal, because if one of your requests takes a really long time, your whole batch is delayed.

**[00:31:49]** Here the idea is we are putting a throttle where we have up to 5 active requests. When one finishes, the next goes in. And it ran in 4 seconds, 4 and a half seconds instead of 2 seconds. Because we're saying only 5 can go at a time. So of the 12 total, they have to wait for other ones to finish.

**[00:32:27]** That is kind of the key way that I think is good to have as your default programming pattern for when you're programming with LLMs and you want to build something that is going to end up in production.

**[00:32:38]** Sometimes your first iteration will be without Async processing, because it does add some complexity. But fairly quickly, you will want to — especially once you start doing evaluations. If you want to run an Eval on a big set of prompts, if you have a hundred test cases and you're in a for loop, it's like okay let's go for a walk, get some coffee, because it's gonna take 15 min versus if you're doing everything Async, it's like a couple of seconds.

## Async Tool Calls

**[00:33:12]** The same thing goes for tool calls. We can also apply the same pattern. In many cases we will want our models, especially for things like search — there's a lot of complexity there.

**[00:33:18]** One of the ideas is having multiple tool calls that can do different things in parallel. You can have this be a way to trade off speed for decomposing your tasks into smaller pieces. If you have a model that's going to be doing web search, maybe the model knows that there are like 10 potentially useful websites to search.

**[00:33:56]** The kind of naive way to do this is just have it do one, then the next, and the next. These requests don't need to happen all the same time, if we trust our LM to handle the responses all at once.

### Parallel Tool Call Execution

**[00:34:55]** Once we have these tool calls, we can handle these asynchronously by using the same pattern from before, where the call for the function can happen asynchronously.

**[00:36:49]** If your tools are doing web search or doing a database lookup or are doing something that requires calling other models as helper functions, having your tool calls being asynchronous is a good pattern to make sure that you are always able to maximize your throughput.

### Timeout Patterns

**[00:37:13]** You could also have sort of like a timeout where you say, for any given function, you could have the function timeout if it doesn't complete in a certain amount of time.

**[00:37:43]** You can have a timeout on each one where you're gonna say, okay, I know that they usually finish in 30 seconds. I'm going to submit them all, but that function will raise a timeout warning, and we'll handle the warning so that maybe we only get 17 search sub agent results. And we just roll with that.

**[00:38:25]** When you're doing parallel requests, it's important to think about what kind of latency guarantees do you need for your application? Any sort of request that has some nondeterminism to it is going to have a tail of how long things can take, and so you either need to be willing to allow it to take full time sometimes, or you have other mechanisms for dealing with latency.

## RAG Patterns: Old School vs Agentic

**[00:38:51]** I think what a lot of people refer to as RAG — what they mean by it is kind of old school RAG. It's kind of before models got really good at tool calling, where the best approach for many cases was to have software that handles all of the search given the user query.

### Embedding-Based Prefetch RAG

**[00:39:07]** The simplest way to do this was embedding search, where you have a database of documents or document chunks. You have a user query that goes in. You do some similarity with the query and all the other embeddings of the chunks in your database. Then maybe it's 10 or 20 top-K results. Then maybe you have some other re-ranking process.

**[00:40:57]** This is what Prefetch RAG looks like — we've done some search, getting a URL's content. You could think of this as a stand-in for the vector database lookup. We are taking the whole thing from our search result, giving it to the LM, telling the LM the question. This is the standard old school RAG pattern, where the searching is not happening from the LM itself. It's just happening from a tool whose job is to go gather the context, arrange it in a certain way, and then show this with the question to the LM.

### Agentic RAG

**[00:42:08]** The agent decides which tools it should be using, especially in cases where you have multiple document sources. So let's say you have pieces of the Internet, some websites, and you also have your internal documents. You want the LM to be able to use and cross reference these with other sources.

**[00:42:52]** This tends to be much less engineering involved. And you also have a lot more flexibility in that, let's say the LM does a search and it actually doesn't find what it needs, but maybe it realizes something about the thing it saw — it realizes the definition was different than what it had assumed in its query. And now it knows, okay, that's actually not the right word for this. I should use a different word instead. It can just kind of go again.

**[00:43:11]** Deep research or Claude Code — a lot of these tools can have multiple swings at search. They don't have to always get it right the first time, which is kind of new in agentic RAG as opposed to Prefetch RAG.

**[00:43:49]** In Prefetch RAG, there's not really a way that you can say, oh, actually, I want to change my theory a little bit based on considerations XYZ, without having to manually hand engineer every version of that.

### RAG Tips

**[00:44:07]** LLMs are great at Markdown. If you were going to try to pick one standardized format for documents that you want LLMs to be able to read and search over, Markdown is great.

**[00:44:14]** PDF to Markdown is pretty doable. There's a lot of these models like Gemini Flash can do it. Mistral's OCR model can do it, for cheaply converting lots of docs into Markdown.

**[00:44:51]** It's useful if you have tools that allow models to take advantage of the natural file system structure or link structure in documents. If you have a hyperlink that's in your document, often you just show this hyperlink to the LM. You also want to give the LM the ability to click in by giving it a tool where it can see the hyperlink, and its argument to the next tool will be that same link. This allows it to kind of browse the Internet, or browse your filestone by seeing where a thing is, seeing any hidden references in it, and following those forward.

### Use Existing Search Interfaces

**[00:45:55]** Building a really good search engine from scratch is very hard. I think it's generally best to avoid getting into the weeds whenever possible. Take whatever kind of APIs you have already. If you have a database that exposes a SQL-like API, or a tag-like API — you can kind of just turn that interface for whatever search index is already built into a tool for the LM.

**[00:46:52]** Google Advanced Search, or Twitter search — all the sorts of things you can type like min date, since — these can all be arguments to a tool. And this allows the LM to have very fine grained control, and LLMs are quite clever at deciding for a given query how to populate all these fields to make a good tool call.

**[00:47:02]** Codex when it wants to search through a file, what it will do is it will use the terminal to be like show me lines 20 through 47. Giving LLMs that kind of interface is a nice way to allow them to explore files.

**[00:47:35]** Allowing LLMs to kind of use existing software systems is often friendly because they're trained on the Internet. They are trained on documentation of these systems already.

### Tool Count Limits

**[00:47:56]** Dozens is usually fine for really big models. Maybe 5 to 10 is where I would do for a tiny model. But it depends on the complexity of the tool.

## System Architecture: Logging & Monitoring

**[00:48:14]** In terms of system architecture — we're not just doing this for one little thing, this is going to be deploying in real world applications. We want people to be able to watch what's going on. We want people to have kind of we know where different pieces of the code live.

**[00:48:49]** Logging — especially if you're really doing serious agent debugging, you want to have some kind of dashboard where you can, without having to print through the code and stare at the terminal, you want something where you just hook it onto your thing and have it run through, and all of your things show up in a nice dashboard.

### Logging Frameworks

**[00:48:56]** These are the 4 that I'm the most familiar with:

- **Pydantic Logfire** — integrates nicely with Pydantic AI
- **Weights & Biases Weave** — if you already use W&B for training experiments
- **MLflow Tracing** — open alternative to W&B
- **Arize Phoenix** — another popular one

### Logfire Demo

**[00:50:36]** Install it, log in. Configure it to tell it what project you're using. Similar to Weights & Biases if you're familiar with W&B.

**[00:51:05]** It looks very similar to OpenAI's Agents SDK. Here, just you want your input types and your output types. It uses the term "dependencies" as their name for input types. But then we're giving it a prompt and `instrument=True` is how we're saying, hey, use logfire.

**[00:52:27]** In the Json version, this is like the raw OpenAI requests going on. You get a pretty version where you get to look through and see: what did it do — call the tool, goal set, final result, process.

### Choosing a Logging Framework

**[00:53:00]** Every different version of logging is going to have its own syntax, going to have different compatibilities with your agent frameworks. And so you kind of have to decide what the right version is.

**[00:53:04]** The easiest way to make these choices: think about what are the pieces of your system that have the most friction towards moving. If you were already deeply embedded into AWS for your whole ecosystem, there's going to be an AWS version of this. If you're already using Weights & Biases, you probably want to use Weave. If you're already using Pydantic AI as your agent framework, you probably want to use Logfire.

## MCP: Model Context Protocol

**[00:54:22]** The magic of MCP is really about client server architectures. The first example for client servers that a lot of people see is FastAPI servers. The idea of your server being a thing whose job is to be an always running program that people will send requests via HTTP, and it sends responses back.

### Wikipedia Search Server Demo

**[00:56:25]** FastAPI is just a kind of lightweight way to turn any code you have into an app or a server API. A few different functions — the main ones are search and get articles. So we want to return matching titles and get the full articles markdown.

**[00:57:20]** This is a thing that's alive now, this terminal is running still. It's not going anywhere. It's not finished. It's just a server that is alive, and I'm going to send it a request.

**[00:57:37]** It got this request for "python programming language" and we got back a nice long chunk of the Python Wikipedia article nicely converted to Markdown.

### MCP as "FastAPI but LM-Shaped"

**[00:57:54]** MCP is simply a version of a server where you have an MCP client and an MCP server, where, instead of it being kind of web-based web primitive where the natural thing is like an HTTP request, it's still using that under the hood, but it's designed to be LM-shaped.

**[00:59:21]** Think of it like FastAPI, but it's LM-shaped.

**[00:59:37]** The server can handle many tool calls in parallel because each of them is processed asynchronously. But really what it's doing is just: hey, run the thing where we want it to be alive. What are the tools? And it's telling the LM, compiling this prompt where this is how the LM knows what to actually do, because this is a server that has first class functionality for exposing prompts and for calling tools, because that's the LM language.

### When to Use MCP

**[01:00:18]** The reason to use MCP is if you want portability across applications. If you want to make a tool that you want your LM to use for searching through your file system, and you use both Cursor and Claude Code, doing it as an MCP server makes a lot of sense.

**[01:00:49]** Or if you work at a company where you have an internal database, and you have lots of internal applications that might care about this database — this is a case where it makes a lot of sense.

### The N×M vs N+M Problem

**[01:01:01]** People talk about this being the N×M versus the N+M problem. If you have a lot of different data sources and a lot of different applications, you can make a manual connection for each one. Or you can make each application be an MCP client, each data source be an MCP server. And now these can kind of plug into each other.

### MCP Demo with Claude Code

**[01:01:44]** We can add a server. A few other ones here.

**[01:02:10]** E2B is a code sandbox. As I was mentioning earlier, sandboxing code execution — if you want your models to be running code that is less trustworthy, especially if you don't know what they're going to be writing and you aren't sanitizing the code, then it can make a lot of sense to have a tool that is essentially a way for the LM to write its tools on the fly. The simplest version of this is just a code sandbox.

**[01:03:32]** What happened: it's calling a tool call and run code. And its argument is code. And it's just passing in this string. And it's getting standard output from the code. So this is just what's the printout from running the program, and that is the return of the tool which is then shown to the LM.

### Streamable HTTP vs SSE

**[01:04:36]** Streamable HTTP versus SSE — differences in protocol to make things a little safer for streaming requests or long running requests. SSE is kind of what originally rolled out with MCP — a protocol for you send a request, keep this connection alive, and it sends back the thing as a full object. Streamable HTTP is a little better at handling intermittent requests or what if the connection is interrupted, or you have to send part of the request back.

### Multi-Tool Orchestration

**[01:05:15]** It did a web search, and then it found some URLs, and for each URL it did a fetch. So it's doing something very similar to the one that we had built where it's just getting the markdown of a page.

### Local vs Remote MCP Servers

**[01:05:47]** Claude Code is running these on my machine as background workers. Claude Code has registered these so that when Claude Code comes live, it knows one of the things I need to do is also run these servers. You could also have these be remote servers, in which case you kind of talk to them like an API.

**[01:06:31]** ChatGPT, I believe, is rolling this out now. There's all these repositories of different MCP servers that you can browse around.

## A2A: Agent-to-Agent

**[01:07:30]** You can also convert a sub agent to a server. One thing I built a while back was making a client that's also a server. MCP client is a thing like Claude Code. But similarly to the way you could make a spec for a server, you can also make a client.

**[01:08:08]** The MCP docs have examples of how to actually make an MCP client. It's really just an application that is able to accept a request from MCP server.

**[01:08:27]** I was trying to use Claude Code to build MCP tools, and I was getting annoyed that you'd have to close the application and reconnect a tool. I wanted this to be able to happen dynamically on the fly so that Claude could make a tool, connect to it, test it, disconnect it, edit the code and repeat without having to kill the whole program. The solution was having a test client with also a server.

**[01:08:52]** This client allows you to deploy a server as a tool, so the ability to deploy an MCP server is now a tool where this server that we've built for Claude Code is also an MCP client. So it's from Claude's perspective it is a server; from the secondary service perspective it's a client, and it is just responsible for forwarding these requests.

### A2A Skepticism

**[01:09:27]** The issue with A2A is that I think people are imagining a world where there's lots of these first class agents that talk together, and they're in a group chat or something. And I just don't think we've seen any kind of winning applications that really lay into this pattern.

**[01:09:36]** I think the multi agent pattern that is the most reliable and the easiest to maintain is when there's really like one primary agent, and it's delegating work to sub agents, in which case you don't really need A2A — you can just use MCP. You can also use all these things like Crew AI and whatnot, Swarm. I'm not sold on those too much.

**[01:10:17]** If you want to have the Anthropic multi-agent research style processing going on, you can have these sub agents be client servers, so they can use their own tools as MCP clients. They can also be a tool for the main agent as a server.

**[01:10:33]** I'm not gonna tell anyone to go really build on A2A right now. But I think you probably should be building on MCP.

## Data Structures for LLMs

**[01:10:44]** File systems are great.

### Docker Containers as Sandboxes

**[01:10:50]** If you want to kind of build your own sandboxes without relying on E2B or some other paid service — just giving your LLMs a Docker container where things are — Docker containers are not infinitely safe. But they're kind of usually good for testing where you can decide what sort of requests can come in and out.

**[01:11:10]** This is a way to give your LLMs a little virtual machine, where they can run around and do stuff and make folders and files.

### File System as Memory

**[01:11:23]** This can be one data structure for the LLMs — essentially a file system that looks like a computer where any information that they need to write themselves for later, as their memory, can just be in a folder. And so this is kind of the easiest way to do LM memory — you have a system prompt or a CLAUDE.md file that tells the LM where its memories live and how to go search them, and then you just let it go search them when it wants.

### Memory Is Unsolved

**[01:11:48]** This is kind of hard to get right. I've tried for a while. They often will forget to go check their memory. It's hard to dynamically trigger the right memories on the fly, and I don't think anyone has really robustly solved this problem.

**[01:12:04]** I would think of memory as being the kind of thing that is still very much in the early days. I don't think there's any great write up on how to fully do memory in a way where the things that happen to an LM that might be relevant in the future just are magically saved and retrieved in the right place.

### SQL and Vector Databases

**[01:12:35]** In many cases your data LLMs can write SQL really well. You can just have any data that need to query stored in SQL databases. SQLite is what I just used for testing. You can have a SQLite MCP server, you can have a Postgres MCP server.

**[01:12:58]** Deciding when to use SQL versus a vector database — I think it really comes down to embeddings are a very useful primitive for building applications around. They don't just have to be for RAG. They can be for any other sort of similarity search.

**[01:13:16]** I tend to use Chroma when I'm trying to build something the first time around. But it's kind of becoming more of a commodity thing — everybody has a vector database, they all are fine. You should use the one that makes the most sense for your setup.

### Evals-Driven Development

**[01:14:16]** There are none of these things that have hard and firm answers. When people at places like Anthropic and OpenAI are building agents, you can bet that they are doing lots of evals behind the scenes.

**[01:14:41]** The way that these decisions are made — how many tools to give to an agent, how much prompting to do — is the kind of thing that you really get a feel for through the Eval-driven development loop. So you need to know what you want your system to do, you need to know how you're evaluating it as a starting point before building anything beyond non-trivial complexity.

## Security Considerations

**[01:15:11]** Another way to think about what you can do with code sandboxes or with terminals — you can kind of think of this as a whitelist and blacklist approach.

### Whitelist vs Blacklist

**[01:15:35]** You could ban certain libraries, you could say I want to prevent my agent from using libraries XYZ and manually strip these out of any code it writes. This is kind of like playing whack-a-mole, because there's always a workaround.

**[01:15:58]** If it's smart enough, it can kind of find a way to do bad stuff if it really wants to, or if it is so confused that it just is trying to do whatever it can.

### Codify Repeated Patterns as Tools

**[01:16:13]** Once you know what the types of code are — if you find your agent is maybe writing the same code a lot, and you realize it sometimes does this type of thing 3 different ways, one of them is definitely better — this is when you want to take the pattern and codify it as a tool.

**[01:16:58]** If it's going to be interacting with things all day, you should take the pieces of logic that it just will be rewriting the same code with errors sometimes, and freeze that and say, now this is a tool. Now we can reliably ensure that we're kind of guaranteeing the code is correct each time, because it's just calling the tool.

### Preventing Code Chaos

**[01:17:10]** When LLMs have many options to do the same thing, they will take advantage of many options. And you don't necessarily have coherence across the patterns of your code base.

**[01:17:38]** Having examples for your LLMs is another way of codifying behavior. Being very clear, either giving them tools that enforce pathways, or examples plus docs that highly encourage pathways for how to use a code base.

**[01:18:10]** LLMs love to write scripts. Claude especially, and Gemini. These models just write script after script after script. Some of them never get used. Some of them are redundant. This is the sort of thing that you want to tamp down by being very clear, either giving them tools that enforce pathways or examples plus docs.

## Authorization & Permissions

**[01:18:48]** MCP rolled out something today that's a new set of changes for it. In general, it's optional. But if you're building applications at a certain level of scale for production use cases, you do need to handle auth.

**[01:18:59]** The easy way to think about it is that in most cases you're gonna have your agent be an extension of some user where the user can decide to grant the agent some subset of the permissions. Maybe certain actions need human approval before an action is taken.

**[01:19:18]** This could be the pattern like we saw in Claude Code of, oh, this thing is going to search the web. Do you want me to approve it? You can have this be the sort of thing that is overridden on top of the function call.

**[01:19:56]** I think it's still early for having fully autonomous open ended agents where auth is just handled, because the kind of failure rate for long horizon agents of doing things that create a mess is just a little bit too high currently.

### Environment Variables

**[01:20:20]** General best practices about environment variables: generally best to not give the LLMs your environment variables directly. You never know whether they're gonna write them or where the data is getting stored. You don't want it to be accidentally trained on, and then end up in the completion at some point. If you can keep your environment variables isolated away from your LLMs, this is generally going to be safer.

## Error Handling

**[01:20:56]** You have to decide — let's say a tool is broken because some website is down or an LM is down, what you want to do in that case.

**[01:21:09]** Usually you'd want a few retries, exponential back off. You can kind of have some graceful failure — maybe a server's load is spiking. You can get around this with retries. In some cases you want to gracefully handle errors and return to the user. You have to decide, when in my application flow do I want the user to see some really nasty error that's really confusing? Or do I want to bucket certain types of errors as things where I just tell the user, hey, the servers down, sorry.

## Q&A Session

### Evals for Agentic vs Non-Agentic Systems

**[01:22:34]** (Henry's question) How do you have thoughts on making Evals fair to agentic versus non-agentic systems?

**[01:22:47]** Tool use is kind of like OP, but that's kind of the reason we like it. And so saying LM A with tools is better than LM B without tools — of course it's unfair. But if what we ultimately care about is making applications that are good rather than measuring who's got the highest numbers in a global sense, there aren't a lot of really great benchmarks out there that really do what we want for agents.

**[01:23:20]** There's tool calling benchmarks of can an LM successfully call tools a few times in a row with the right arguments. But these are not terribly hard.

**[01:23:40]** The Claude Plays Pokemon and the Gemini coding Pokemon benchmark is like the best we've seen as a real world super long horizon benchmark. What you're measuring is: can they successfully navigate this open world for a very long time and get unstuck and finish the game of Pokemon by clicking around with tools for actions.

**[01:24:10]** MC Bench is also a good one. The LLMs are given a high level prompt, and they're told to make like go make a pirate ship in Minecraft, and they have tools for putting down blocks. They can iteratively construct a Minecraft object or scene and then the benchmark is people voting on their favorite.

**[01:24:48]** ARC 3 is actually coming quite soon. It's gonna be game-flavored — lots of interactive games where you're trying to solve puzzles with essentially interactive tool use.

**[01:25:28]** (Kyle Corbitt) If you're doing 2 very different architectures, it makes sense to think hard about what is the end goal. What's the task we're trying to accomplish? Often it's like, oh, I'm just trying to answer the user's question. So you can still write an Eval at that higher level of abstraction and compare these different approaches head to head.

**[01:26:29]** (Will Brown) The tool use can be thought of as part of the reasoning. Your top line eval should probably usually be a function of the primary output. For deep research, you can go poke around and see all the different searches it made. But usually what you really care about is the report. And so the Eval is a function of the report, and in principle, a non-agent LM could just write a great report from nothing.

### Sub-Agent Spawning

**[01:27:37]** You'll want a framework of some kind for spawning sub agents. You could tell your LM to spawn a sub agent, and you give it a terminal or a code executor, and you tell it to use the OpenAI key. Maybe one of them will do a Pydantic agent, one will do an OpenAI SDK agent. And now you have all these messy different abstractions that are totally separate.

**[01:28:03]** Especially for things like that, you want to kind of pick one and say, okay, we're going with this for now.

### MCP Adoption

**[01:10:35]** I'm not gonna tell anyone to go really build on A2A right now. But I think you probably should be building on MCP.

**[01:07:13]** If you are building a service that has an API, you should probably have an MCP server for that API. Because that's how a lot of people are building their applications, and it allows agents to use your service in a pretty direct way.

## Homework Assignment

**[01:29:16]** The homework for the weekend is really just to build something fun that will give you a way to test out a lot of these things. I put some structure on it. But really it's just about having a sandbox for getting creative with prototyping agents.

**[01:30:02]** Pick some task — the easiest ones are code agents and search agents, just because those are the ones that we have the most examples of out in the wild where the product really works.

**[01:30:08]** There's ways you can have agents that maybe under the hood they really are code agents or search agents, but they feel like something different because you pick the workflow. Maybe it's a graphic design agent doing its design and code. Maybe the loop is it's creating an image, it's looking at the images, tweaking it. Or maybe it's playing a board game, playing solitaire.

### State Management

**[01:31:37]** If your agent is short-lived and doesn't need to resume, then you can just have this be an in-memory object. If you want this to be a thing where you can close out of your application and the agent state is saved properly and recovered when you wake back up, then you probably want a SQL database.

**[01:32:13]** State management of your application is kind of the lifetime or the rollout of the agent directory — something that the agent isn't necessarily aware of in the same sense as it's aware of its tools. That's kind of higher level or lower level.

### Eval Pattern: LLM-as-Judge

**[01:32:48]** The most flexible pattern for this is going to be LLM as a judge where your agent does some things, you have the final output of the whole trajectory, and you ask the LLM judge to answer questions about this with a schema of some sort of Pydantic object. You are programmatically converting this — maybe it's yes and no, these are getting converted to a 0 or 1 score.

### Best-of-N Sampling

**[01:34:23]** Best of N is just the idea of: if you have a reward signal for your output, you can have your same model, your same agent do many parallel searches. Use your eval function to select which of these is best.

**[01:34:43]** If this is a case where you know the ground truth, or maybe you just have criteria that can measure this without needing the ground truth — LLM judge questions that can be answered like sources being cited, reliability, or any internal contradictions. Those are questions that could be asked by your judge and answered as kind of these objects.

### Blog Post Encouragement

**[01:35:37]** This is a good opportunity to make a blog post. If you've been thinking about blogging — pick a problem, try out these methods, write up a little blog post and put it on LinkedIn or Twitter, or personal website, or Substack.
