---
title: "Cheat at Search — Steering Lost Agents (Lecture Transcript)"
author: Doug Turnbull (@softwaredoug)
date: 2026-05-27
date_ingested: 2026-06-03
related_article: articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents
type: transcript
tags:
  - search
  - harness-engineering
  - search
  - ai-agents
---

# Cheat at Search — Steering Lost Agents (Lecture Transcript)

**Author:** Doug Turnbull (SoftwareDoug / softwaredoug.com)
**Date:** May 27, 2026
**Context:** Live lecture for the Cheat at Search Maven course. Part 3 of the series — harness design patterns for agentic search.
**Companion slides:** [[articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents|Steering Lost Agents — Cheat at Search (Slides)]]
**Companion course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)

---

## 1. Introduction — Harness Design

A lot of these things I'm going to be talking about today, we're going to be really getting into… these words mean so many different things. People talk about harnesses, scaffolds — we're really going to be talking about **harness design**.

The other disclaimer is it's changing all the time. But I'm going to talk about some patterns that teams have come up with that seem pretty effective, and that I've seen come up over and over again.

Really, we're talking about:
- **The knobs we control as humans**
- **What the agents actually control**
- **All of the guardrails** we can apply to the agentic process

---

## 2. The Tool Calling Loop (Recap)

If we remember from last week, we talked about an **agentic tool calling loop**. The agentic tool calling loop is literally just the thing where we tell the agent: here's a set of tools, here's a prompt to solve this problem. We call tools on behalf of the agent, and then we keep iterating until the agent decides it doesn't need to call any more tools, and its final message isn't a set of tools to call — it's an actual piece of output.

In harness design parlance, I say "agentic loops" sometimes, but what I really think of is the **tool calling loop**. In some ways, because these terms are so overloaded, "tool calling loop" is much more precise. There are many loops you put around things in search and agents.

We also can have a **loop around that** — and that's what we're going to be talking about a lot today. The actual thing that harnesses that tool calling loop to do things like:
- Modify the inputs as they come in
- Check the outputs as they come out
- Validate things
- Make sure things are staying in a valid state
- When the LLM is not behaving itself, prompt it to go in the right direction

---

## 3. What We Control

If we walk through this from front to back:

1. **We provide** all of these things to the LLM: system prompt, context so far (full chat turns back and forth, all the tool calls, everything appended over time), and a set of tools it can use and manipulate. We have control of that anytime we call an LLM.

2. **The LLM chooses tools** to call, like search tools. We can push the agent, we can tell it it's said something wrong, but at the end of the day, it's an LLM deciding what tools to call.

3. **We control how tools respond** to a request — because we write the tools, usually. The agent might do something, but we get to decide how we respond to that tool call.

4. That goes back and forth several times — this is the **tool calling loop**.

5. **Finally, the agent decides** what it's gonna output at the very end — a set of search results, chat response, whatever.

6. **We can respond to that** — honestly, by repackaging all of this stuff back up and calling the agent again. We can decide we want to give some feedback to the agent on how we feel about its search results.

This response back can also just be an automated: "hey, I asked you to give me 10 results, you gave me 8, keep trying."

---

## 4. Carrots and Sticks

How I like to think about search with agents: they're starting somewhere with a query. Someone wants to search for "earnings report for company XYZ." We're coming in with a query. The agent sees the results, it can adjust its strategy to hopefully move closer to relevant results.

This iteration of searching, seeing results, reasoning about them, making another query, and iterating — the happy spaces are the relevant results. Our goal is to build structure around a search process so that the agent will be steered towards the relevant results, and wastes less context navigating around this corpus.

**Carrots** are nice, gentle ways of trying to get the agent to do what we want. **Sticks** are literal errors and reprompting and telling the agent it's screwing up.

There are things like user feedback that really — because LLMs want to be so people-pleasing — are in some ways "painful" to an agent to get wrong. It's a bit more of the stick. There are other things that are carrots, like our initial prompts.

We're really nudging, we're manipulating the agentic process through **prompting** and **programmatic guardrails** to make sure that the agent is moving towards relevant results.

---

## 5. Harness Definition

**Q: Are harnesses just about making sure the agent is grounded without hallucinating?**

Harness is many things. In this case, I'm meaning it to mean **the thing that's controlling the tool calling loop** — that's looking at it, that's validating it, that's implementing business logic.

There are two ways that we work with LLMs:
1. **Through prompting** — we've done that forever
2. **Programmatically enforcing things** — whether that's a tool enforcing that how it's being searched is valid, or getting a response back and making sure the agent did what we expected it to, to the extent that we can programmatically check something

It's very similar to coding harnesses and how coding harnesses work.

---

## 6. Auto-Tuning Prompts with DSPY/GEPA

**Q: Is there a way to auto-tune prompts to make sure carrot and stick get closer?**

There are techniques like **DSPY** and **GEPA** (a reinforcement learning prompt engineering technique) that let you manipulate this entire environment to get closer and closer to an ideal outcome.

- **DSPY** is more built for pure classification setups — optimizing the examples given to a prompt to make sure it's not overfitting
- **GEPA** is a more holistic process

But having **solid evals is the most important thing** — that's often a prerequisite for doing lots of cool things.

---

## 7. Model-Specific Behavior

**Q: Do carrots and sticks need to be adjusted per model?**

Yes. For example:
- Claude Opus 4.5 had elevated code generation
- Later versions (4.6, 4.7) became more chatty, less focused, didn't follow instructions as well
- ChatGPT 5.5 was behaving better for some use cases

A lot of what we talk about today — you can't entirely overcome a completely horrible model. But for most models, most of the time, they want to please the user and fix errors. As long as models are acting in good faith and you have good programmatic guardrails, generally that will steer most models in the right direction.

**Convergence as evaluation:** If you give a model the same query multiple times, does it tend to converge on a similar set of behaviors? If it's all over the place, I don't trust it as much. If the harness is giving feedback and it's going consistently in the same direction, that's a well-constrained, reasonably deterministic search process.

---

## 8. File System-Like Tools

We're gonna simulate file system tools. Instead of BM25 and embedding search, we're just gonna have:
- **`ls`** — lists all the things in a folder
- **`cat`** — dumps the contents of a file
- **`grep`** — searches a glob with a regular expression

We're simulating a file system with the Wayfair dataset (~50,000 documents). The dataset has natural organization: category and subcategory as directories. Each product gets a path like `furniture/bedroom_furniture/solid_wood_platform_bed_12345.txt`.

**Key insight:** Someone did a study on using grep and file system tools on complicated, deep research tasks where agents have to do multi-hop reasoning. The stuff broke down after about 100,000 documents. So 50,000 on a relatively well-structured e-commerce dataset seems promising.

**Results:** An agent with file system tools beats BM25 (NDCG ~0.541). On the one hand: "who needs a search engine?" On the other hand: barely beating a super-fast keyword search algorithm. The takeaway: if you already have an agent with file system tools, it's not unreasonable to find what you need by navigating the file system.

This is GPT-5 Mini. With a frontier model (GPT-5.5), performance is probably ~10% higher.

---

## 9. Ralph Loop — Repeating "Try Harder"

You can literally just do a kind of **Ralph loop** where you tell the LLM every time it calls to try harder — try new and different strategies. This is a way of giving more user feedback back to the LLM. Setting a max loop so we don't loop forever. It helps a little bit, but always consider: how much does this cost per query?

---

## 10. Validators and Stoppers

One of the biggest areas of giving agents feedback is **validation** — also called "hooks." Seeing what the agent came back with and pushing back: "that's not right, you need to fix this."

The reason to do this: LLMs are trained to please users. A lot of good harness design is figuring out what LLMs are trained on and trying to stay in those rails.

**File system tools** are an example — LLMs are super optimized for coding tasks and exploring file systems, so we take advantage of that.

**Search to an LLM** is sometimes a means for it to get new information it doesn't already have. A lot of what we're doing is the opposite — using the LLM's encyclopedic knowledge to find things in a corpus.

### Minimum results validator
Count the number of tool calls. If we didn't get at least 10 results, tell the LLM it screwed up and to try again.

### Hallucination validation
Validating that the data you got back wasn't hallucinated — that it's actually real data in the corpus. Is this a real doc ID? Is this actual data from the corpus?

---

## 11. LLM Judge Validation

The big one people think of: having some kind of **judge or evaluation** that sits on top of the agentic stack to push back on the agent.

This is calling another LLM to evaluate the results. For demonstration purposes — I don't expect this to perform better, because the LLM that's the agent itself would already be doing this. But if you had an LLM judge — or honestly, any kind of ranker or classifier that can tell you whether a result is relevant — that could sit here and tell an agent whether results are relevant.

**Important:** Have a max loop so we don't loop forever. If there's something that's supposed to be valid but isn't, the message comes back as a string and we send it back as a user prompt.

**Relevance feedback analogy:** If you know what's relevant, you can do query expansion or find similar things. If we have an LLM judge we trust, we can do that by giving feedback to the agent. The agent reacts similarly to how it would if a human said "I didn't like the search result."

**It doesn't have to be an LLM judge.** It could be a re-ranker, an ML model that classifies relevance. In some ways, it'd be preferable if it wasn't another LLM, just to get more diversity.

---

## 12. Evaluate Tool (In-Loop)

Could we have a tool that takes a query and document, and encourage the LLM to call this evaluate tool while searching? Certainly could do that. One tricky thing: it's difficult to enforce tool calls from an agent — to force it to evaluate every search result. There's no enforcement mechanism in the tool calling loop.

---

## 13. Re-ranker Inside vs. Outside the Search Tool

Should you just have the re-ranker be part of your search tool? Excellent question.

- **Inside the search tool:** It becomes a bit more of a black box
- **Outside the agentic process:** You can help an agent learn to use primitive tools more efficiently, but you'll use more tokens

**Key insight:** If you have a labeler/judge sitting on top of the agentic process, and the agent is exploring the space and pulling back lots of different search results and labeling them as relevant or not — that builds a **really good training set for a re-ranker** that might live in a search tool.

Getting hard negatives (things that look relevant but aren't) is really difficult in search. Letting the agent navigate and label as it goes produces excellent training data.

> This agentic process might not necessarily be on behalf of users — we might be using it to build labeled training sets for production rankers.

---

## 14. Few-Shot Examples

Giving examples of relevant and irrelevant results in the system prompt helps agents not waste time earlier in the process. Random query-document pairs with relevance labels seem to help — maybe it's chain of thought, maybe it's seeing patterns of what's relevant.

**Results:** BM25 baseline → agent with file system tools (slightly better) → agent + few-shot examples (further improvement).

If you got really tailored with query-specific plans for how to search specific types of queries, you could go really far.

---

## 15. Query Expansion and Skills

**Query expansion:** Before searching, have an LLM call expand the query. For "red shoes," expand to "I am looking for red-colored footwear, sneakers, size X." Connecting to information in the language of your corpus is powerful.

**Skills / Query plans:** Map between a query and a strategy for how to search. Very similar to coding agent skills — detailed documentation on how to do a specific task. Could be:
- A vector database lookup
- Simple rules (e.g., if "couch" mentioned → filter furniture)
- Skills.md files

**Semantic caching parallel:** Look up a similar query and return a rule or expanded prompt for how to process that kind of query.

---

## 16. Tool Guards (ToolState as a Stick)

A very common pattern: tell agents when they call a tool that they've already searched for something similar. If the next query overlaps entirely with something searched before, return an error.

Tools can maintain **global state** of the agentic process to prevent the system from doing stupid things:
- Disallow repeated queries
- Force different categories
- Encourage exhaustive search
- Enforce a kind of state machine on the process

**Results (Amazon ESCI dataset):** Forcing the LLM to not repeat queries (at least 4 calls, none repeating) gives a meaningful NDCG bump on top of the BM25 baseline.

---

## 17. Sub-Agents

Another way to not have agents waste time: **delegating parts of the problem to sub-agents**.

If one agent has a massive problem and is trying to do it all in its own context, it has to navigate every permutation. If it can delegate bits of work to sub-agents with specific tasks, that's more efficient context management — at the cost of the sub-agent losing context on the full problem set.

**Sub-agents as a tool:** The main agent says "delegate task: find things that look like maroon sneakers." The sub-agent does its own agentic tool calling loop over the tools and returns results.

**Results:** Adding delegation on top of everything else gets maybe a tiny bump — probably not statistically significant. Given simple file system tools, explicit query plans are probably more useful than arbitrary delegation. But for complex tools, delegation helps sub-agents use context more efficiently.

**Diverse candidates:** Sub-agents help give explicit tasks to find diverse sets of candidates, so the top-level LLM can produce a final ranking given all options.

---

## 18. BEAM Search — Exhaustive Exploration

So far we've been randomly starting somewhere in the corpus and gradually moving towards relevant results. But could we do a more **exhaustive search**?

In regular search, we try to get the top 10 results. One thing agents really bring to the table: the ability to **consciously try to leave no stone unturned**.

**BEAM search:** Tracking if you've visited every place — like a door-to-door salesperson canvassing a neighborhood. "Have I been to this address before?" It's a queue-based graph navigation algorithm.

File system search enables this: if I search for a couch, have I checked all the places a couch could possibly be? There's untapped potential in agentic search for enforcing exhaustive search — did you visit all locations? Did you leave no stone unturned?

> This is a seed for future discussion: not just gently nudging towards relevant results, but encouraging or even requiring exhaustive exploration.

---

## Q&A Highlights

- **Harnesses vs. grounding:** Harnesses are the thing controlling the tool calling loop — validating, implementing business logic, enforcing things programmatically
- **Auto-tuning:** DSPY and GEPA can optimize prompts, but solid evals are the prerequisite
- **Model drift:** New model versions can surprise you — prompts that worked may stop working
- **Convergence as signal:** Consistent behavior across repeated queries indicates a well-constrained process
- **Token costs:** Output tokens are expensive; tool calls are proportional to output tokens; always consider cost per query
- **NDCG ground truth:** Varies by dataset — clickstream data for user-facing, hand-labeled for academic datasets
- **Progressive disclosure:** Agents aren't yet leveraging data organization well — opportunity for better harness design

---

## Companion Resources

- **Slides:** [[articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents|Steering Lost Agents — Cheat at Search (Slides)]]
- **Course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)
- **Author:** [softwaredoug.com](http://softwaredoug.com)
- **Related transcripts:**
  - [[transcripts/2026-05-20_softwaredoug_cheat-at-search-llm-query-understanding-lecture|Part 2: LLM Query Understanding]]
  - [[transcripts/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge-lecture|Part 4: LLM as a Judge]]
