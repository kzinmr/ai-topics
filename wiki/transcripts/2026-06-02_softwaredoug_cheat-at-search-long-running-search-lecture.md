---
title: "Cheat at Search — Long Running Search Agents (Lecture Transcript)"
author: Doug Turnbull (@softwaredoug)
date: 2026-06-02
date_ingested: 2026-06-02
related_article: articles/2026-06-02_softwaredoug_cheat-at-search-long-running-search
type: transcript
tags:
  - agentic-search
  - long-running-agents
  - context-management
  - memory
  - harness-engineering
  - search
  - ai-agents
  - crawling
  - local-index
  - topic-modeling
---

# Cheat at Search — Long Running Search Agents (Lecture Transcript)

**Author:** Doug Turnbull (SoftwareDoug / softwaredoug.com)
**Date:** June 2, 2026
**Context:** Live lecture for the Cheat at Search Maven course. Part 4 of the series — long-running search agents and context management.
**Companion slides:** [[articles/2026-06-02_softwaredoug_cheat-at-search-long-running-search|Long Running Search Agents — Cheat at Search (Slides)]]
**Companion course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)

---

## 1. Introduction — Long Running Search Agents

So let's talk about this fun test. So we're gonna switch in problems entirely. We're more or less, for at least this week, we're leaving the Wayfarer data set behind. We're actually gonna look at a longer-term, bigger picture process.

Like I said, we're gonna talk about long-running search agents. These are agents that run long periods of time. I'd like to think of them as open claw kinds of things, but honestly, I think being a bit smarter than just the open claw thing. And how we can think about context, or not exhausting context through things like memory, and guiding agents to a next action.

Most of this is based in this Gather Experts notebook. This notebook, this task that I'm gonna set up, is basically — there's not a magic way to search, like, actual people looking for jobs. So what we're doing in these notebooks is using Google's patent search to find experts in given fields, and to simulate this process. In some ways, simulate the idea that a recruiter's job, or something like that. But of course, this doesn't just have to do with that domain, this is just a slightly different domain. There are many times where we might have some long-running monitoring task that an agent is performing for us through search primarily.

---

## 2. Product Rationale

As a recruiter, I want to find Java programming experts who know Spring and Hibernate and want to work remotely. If you think about how job search works, it's this iterative process where people are trying queries, but really, the recruiter has some complete specification — you could write what they wanted in a long prompt.

We're gonna take a long prompt of the kinds of experts we want, and try to systematically go through a corpus like Google Patent Search, and go through them.

From a product point of view, we're moving away from giving a recruiter keyword-based search, and now giving them a bit more of a prompt-based interaction, or a way to specify what they want in natural language — almost like a spec, if you're used to AI coding.

In these situations, a recruiter does individual searches, collates the data themselves, tracks what they're finding on a spreadsheet, and they're sort of iterating through the stuff and doing a lot of data plumbing. We sort of want an agent to do some of this grunt work of searching, maintaining the spreadsheet of who we found, trying not to duplicate work, and trying to always find novel and interesting people.

---

## 3. Search vs. Crawling

Another way to think about this — in a classic search engine context, a lot of times this is more of a crawler than it is a search. We used to have this notion of a web crawler that would go out and find all the things, crawl all people looking for jobs or all job postings, and put them somewhere. And then through search, we would help solve queries.

In some ways, we're using a prompt to make a bespoke index that's focused on a specific problem. Instead of a spreadsheet, we're making a little local index of what we found.

You might think of this as crawling, because crawling is also something that works over months and tries not to repeat visit places unless some time has expired or something like that.

---

## 4. The Patent Search Tool

We're going to find experts on Google Patent Search, in part because there's an API. There is a website called searchapi.io that lets you do search-like Google patents from an API.

The patent search tool is relatively straightforward. It's literally a patent search with keywords. And we pull back the title, the inventors, the assignee, which is usually a company, and other metadata about a patent.

We have a system prompt: "You're finding recruits for our company with more relevant experts. Use the patent search tool to find scientists we should network with. Add them to the expert database. The more new users you add, the better."

---

## 5. The Harness

The harness here is just driving — underneath is that OpenAI agent we have worked with. Just passing the tools and things that we're going to use. It has a convenience method for listing some functions to tell it when to stop. In this case, it's gonna call the OpenAI agent to execute once and stop after exactly one call.

But everything else is exactly the same stuff we've seen so far. Your inputs, your context that will be built up, the tools, agent state — which is just some global information for this that's instantiated for this call.

We do this, and we get back a prompt with Top Kitty litter experts. And you can see the patents that this person has worked on in the kitty litter domain. It works as we'd expect.

---

## 6. The Challenge: Avoiding Repeated Searches

The challenge for these long-running search tasks is: how do we get the agent to avoid repeating searches per task? Specifically, how do we increase the gain relative to the tool calls?

Tool calls are a great proxy for output tokens, too, because when they sense requests to be called, that's output tokens being emitted. So it's a good proxy for overall cost.

We want to minimize duplicates, minimize Google patent search tool calls, and maximize the experts we find over time.

We're not going to dig into relevance analysis right now. We could wire a judge up to give feedback back to the agent, but for now, just for simplicity, we're going to assume the agent is giving us relevant people. But of course, in real life, we might want to have more judgment or guidance to the agentic process.

---

## 7. Approach 1: Single Large Context

The very first thing we would probably do is just have a single context. We're sort of simulating the agent waking up and repeating the same call. You can imagine we put the inputs somewhere off into a database, or append them to a file. And the agent wakes up, slurps up its past context, and then does another call to the agent. Appends that context. Saves that off to a file or a database. To wake up again in an hour, or a day, or whatever.

The context continually grows. In this case, we let it run for 5 times.

We can have a check in the tool — we can return an error if we actually have seen a duplicate. This agent state is kind of global state to this whole harness. For this one search, we can see if we've duplicated a search. So if patent search is called twice with kitty litter expert, it will fail. That also encourages it to try to more exhaustively search everything.

**Result:** 35 experts for 44 patent search calls. Per-call yield: 35 / 44 = 0.795. No dupes because we prevent them.

The other motivation: we're spending money on tool calls, we're spending money on tokens, but we're also spending money to call these APIs. In Hev's example, calling out to Reddit's APIs are expensive. In this case, we're calling Google Patent API through searchapi.io. So that's the other reason to minimize it.

---

## 8. Discussion: Goal Mode and Alternative Approaches

**Hev:** What I used this morning is I used goal mode, and I said I want 50 data scientists that are working on ecology. You have access to the LinkedIn and the GitHub API. From what I understand, the goal mode actually hands off from one model to another model, so it's kind of got a judge built in, basically.

**Doug:** I should see how it works. I haven't dug into how it works. I presume it's starting with fresh context periodically?

**Hev:** I believe that there's two agents, and one checks the work to see if you hit the goal, and one is doing work. And so you get that extra check on a pretty fresh context window. And I do see compaction happen. It does seem to have pretty good performance compared to just trying to accomplish a plan.md file. One of the few features that went from Codex to Claude, interestingly.

**Hev:** Also, a really good free API for searches is the GitHub API. It's free. A lot of people put their email in there. That is how recruiters are finding you. You can often find, like, who's a top committer of something — you want to find your Java Spring developers? GitHub if you want.

---

## 9. Approach 2: Cron Job with Persistent Memory

Another version is the cron job. We start with fresh context. For really long-running stuff that's over days and weeks and months. We start with fresh context, we gather hopefully new experts each run, and use memory's guardrail to avoid duplicate work somehow.

The trick is: how do we do this to avoid, to improve gain per LLM call?

In this case, we're not resetting the agent state every time we loop. We're actually maintaining it. So we have a kind of memory that tools can see to see, hey, at any time in the past that I've been running this process — independent of the context being reset — did I try this query already?

So it's like a duplicate check that lasts for each of these cron jobs. The only difference here is I'm not infinitely appending to context, I'm restarting the context every time. But I'm not resetting the memory of what I searched in the past.

**Result:** 56 experts for 77 calls. It does seem to gain a lot each round, about 56 experts for 77 calls.

---

## 10. Discussion: Context vs. Memory

**Prasad:** Rather than restarting the task regularly, is there a way to do compaction, sort of building on the existing knowledge that has gathered?

**Doug:** You're thinking along the right path. That is the crux of designing these things.

**Asim:** If you start a fresh new context, fresh new agent, then you would need some reference to previous tool calls, or the history, right? There has to be some persistence layer that we need to use.

**Doug:** That's what we have, except now, the only persistence layer itself still requires context to use and process over. So exploring that persistence layer is itself — the more the longer the task runs, the more work is done by the agent to basically figure out that persistence layer of what it's allowed to do.

**Doug:** Yeah, so we know that we can't have an infinitely growing context. So we need to have — if we want this to run months into the future doing this task, we know it's going to need to reset its context. And how do we do that in a way that ensures that we still have this statefulness that doesn't start to hit lots of repeated work?

**Asim:** I just have a quick question — when we're running an agent session, are these memory and context local to our session, or is it on the hosted runtime?

**Doug:** It's all in your local runtime. In this case, this state, this memory — there are many agent frameworks. In this case, literally, your context is a set of things that you've sent or received back from the LLM, and then this state is just working memory that you have off to the side. The LLM doesn't see it. It's something that you might have in a database, honestly.

**Asim:** Why does it release context and not memory? Shouldn't compaction handle both?

**Doug:** The reason we're not resetting memory every time is because the goal of this task is to find more experts. We're reawakening the same agent. We don't want it to try yesterday's queries. We want to start with fresh context for useful reasons of not wanting to have context rot, run out of context. But we also want to compact to give hints about the state of the memory, so that we don't go down wrong paths.

---

## 11. Approach 3: Compaction (Search History Summary)

We could have a compact search history of previous runs. Literally a little search summary with basically all the queries we've tried in the past. Maybe a set of queries and a bunch of information.

At least we're only eating — this isn't trying a lot of tool calls, which eats up output tokens and calls our expensive APIs. If we could somehow summarize the things that have been searched in the past, we could at least give some encouragement for more novel exploration.

What's tricky is — there are classic compaction techniques we could use, but we can't necessarily enumerate every possible query that has been explored. In this case, we're just listing queries and the kinds of things that we found to help the next agent continue on.

This saves us time, saves us tool costs, but it's not necessarily as good as long context. We're getting back to the performance of a single long context, but as a cron job.

**Result:** 31 / 42 = 0.738 yield. Not as good as lengthy context (expected).

But we've just made this bubble that grows in proportion to the number of historical queries a little bit smaller, but it's still gonna grow proportional to N. So these kinds of things will work for a good number of runs for the same task, but they're not gonna work indefinitely.

No matter what, we need O(n), and there's not some magic compaction scenario that will easily cover everything perfectly. We can't just list every query. If we have thousands of queries that we've done in the past, that's obviously gonna eat up a lot of context.

---

## 12. Approach 4: Local Index (Expert Database)

What happens if we have a local index? We call out to Google patents, or LinkedIn, or whatever, to pull in new people. And we also index to a local index, and we use tool calls there.

This is a little bit of splitting the baby, because it's not saving us necessarily on output tokens, but it is saving us on calling external APIs. With a local index, if we think the call out here is expensive, at least the agent can do some strategizing about, like, oh, I found this expert by using this search term, how should I try to explore new and different areas that I don't have in my local index?

This is more of an agentic crawler — truly, because we are pulling something from an external system, but also maintaining a local system. At least we're not wasting on external APIs, we're now only wasting on internal APIs.

We have an external database that's a Pandas data frame with useful hints. The NAICS here is just a classification of expertise — a U.S. code system, like a taxonomy. The "user search found with" is the keywords that the agent used to search with. That's what we don't want to duplicate.

We don't need a separate query tracking system. We could just move our query tracking into the expert database, basically our index, by seeing when we get a query, when that tool gets a query, it can actually look up in the local index whether or not we retrieved that query yet.

The NAICS numbers and NAICS names become things generated by the agent and the LLM when it's doing insertion. So the agent is aware, for example, GPT-5 is aware of this classification scheme, and it will just generate NAICS names and NAICS numbers. When we search, we could add this to our local tool to say, also you can do a search and specify a NAICS name. We will try to find experts that sort of match that as much as possible.

This makes the data self-organizing!

**Result:** 51 experts for 19 patent search calls. Yield: 51 / 19 = 2.68. Notice we have local search calls of 17.

**Joey:** That database, that index, if you were to categorize it, would you say that's just working memory right now that gets iterated upon in part of these long-running loops, or where exactly does that sit?

**Doug:** It's structured in a way to be memory, because it is also looking — it's both indexed and looked up by the agent itself. So the agent is organizing it. The agent is assigning the classifications, the agent is writing a description of the expert. And then the agent is also querying based on that information. So I tend to define memory as a thing, a substrate, where the agent organizes it in a way that makes it easy for the agent to find later. I would probably call that memory. But it's also just classically a search index that happens to be self-labeled by the agent.

**Joey:** On the long-term horizon, that's something that constantly gets maintained, so when the agent de-persists, it's always important to include that as part of its particular task when it's contextualized by its long horizon goal.

**Doug:** Yeah, that's a great way to think about it.

---

## 13. Approach 5: Frontier Exploration (Topic Clustering)

The real problem when you're doing this work is — even with the local index, we still are wasting time on a lot of tool calls, even if they're not external. This orange blob, the summation of these, will still grow in proportion to the number of past queries.

What's really the trick to all this? Is there a way to sort of express the frontier of what's been searched so far, without giving every detail? And how do we encourage creative searches in new and interesting directions?

In the past, we did some compaction, and that was still proportional to the number of queries to try to express this frontier in prompt form. But can we do that in a way that is somehow not proportional to the number of queries? Maybe constant, or at least log N?

**Two approaches:**
1. Give a new direction — have an outer agent that says, hey, search for this part of the problem
2. Have a representation of topics that have already been searched thoroughly

I used a clustering technique — **LDA (Latent Dirichlet Allocation)**, a classic machine learning clustering technique. It takes a set of queries and gives a label, a name, to some cluster of those queries.

Then I asked an LLM to take the cluster — a summary of what has been searched in the past — and generate a new subtopic to search for. "You'll be given a topic clustering some queries that have been searched. Return a topic that is a subtopic, but useful to explore."

**Example:** The user hopes to find kitty litter. Here's what you should do to find more of those experts, because you've already searched the obvious places. Recommendation: end-of-life, compostability of cat litter. Rationale: Several topics touch on biodegradable/compostable litter, but there's less focus on what happens after use. Keywords to search: "OK compost" "home" vs "industrial", "EN 13432".

There is some duplication, but there's also some interesting creativity.

**Result:** 55 experts for 33 calls. Yield: 55 / 33 = 1.667. Fewer local calls, a tad more experts.

I might trust this to run longer without massively exploding context. It doesn't begin to work until we've exhausted the easy cases.

---

## 14. Discussion: Frontier and Taxonomy

**Asim:** When you mentioned frontier abstraction, it sounds like it's going to be like a taxonomy. When you go through open coding and axial coding, when you're doing evals, and then you use LLMs to create a taxonomy of what you really need to inject into your harness — the learnings, lessons. Would it not be similar to a taxonomy here?

**Doug:** Absolutely. I was using just general clustering, and then labeling those clusters, but you could also — if you could classify these things into some kind of taxonomy, that also would be really powerful.

**Asim:** I have seen some development — the idea of constant evolution is that you come up with very fine-tuned taxonomies that would literally increase the quality of your harness, or the operation of your system.

---

## 15. Discussion: Access Control for Long-Running Agents

**Pardeep:** One of the topics is access control for these long-running agents. One of the problems that is coming up is what access should they have? There are multiple types of access — file system access, but also contextual access. If you are working on one customer's behalf, then even though you have access to other customers' database, within that context, you should not be allowed to access it.

**Doug:** My gut reaction says don't trust the agent to decide its access. If there's clearly a customer associated with something, as much as possible, make that part of the harness, and make that part of the structure and program around the agent and the scaffolding. Don't try to have an agent decide, like, oh, I have access to this customer, but not this customer.

**Asim:** There are solutions coming where agents will have their own IDs. You use OIDC type of authentication to authenticate each agent through a JWT token, so there's a time-to-live token given to agent ID, and then you can control what type of roles you want to give it.

**Pardeep:** The problem is a three-phase problem: (1) agent identity, (2) agent access control, (3) contextual agent access — even though the agent has access to all the customer data, in real time, you don't actually want it to access everything. It's similar to personalization — Google Gemini figures out personalized context and applies it to the next queries.

---

## 16. Non-Agentic Query Prediction

A completely different approach — do we even need an agent?

Instead of an agent, use a **next-query model**: given the history of queries and their results, predict the next best query. Reward with how many new experts found.

**Could this be a supervised task?** State: queries by gensim topics, NAICS counts, run history. Label: new experts found. Decompose into features.

**Perhaps a hybrid system:** A query scorer given state, where LLM generates candidate queries and the scorer ranks them.

**Query prediction pros:** Possibly a simpler prediction, can formulate a traditional ML task, if it works could keep going a long time at low cost.
**Query prediction cons:** Lose agentic reasoning to explore results, modeling more difficult than prompt/state.

**Long running w/ frontier prompt pros:** Pretty easy to setup, agentic reasoning to troubleshoot/reflect.
**Long running w/ frontier prompt cons:** Hoping the agent can make a principled decision, prompt magic.

---

## 17. Final Thoughts — Monitoring

Make sure we track when we hit diminishing returns. We can troubleshoot, save state, etc. Don't hesitate to get human in the loop. New request for same run.

What if agents could query their old search?

```python
tools=[patent_search, my_old_context_search]
```

What if agents could generate their own code to query it? Let agent generate python code to explore its past state / the corpus.

---

## 18. Access Control Discussion (continued)

**Doug:** I would want the agent to be — one thing that my gut reaction says, don't trust the agent to decide its access. If there's clearly a customer associated with something, as much as possible, make that part of the harness, and make that part of the structure and program around the agent and the scaffolding.

**Asim:** There are solutions that are coming where agents will have their own IDs, basically, so they will be having their own IDs, and you use OIDC type of authentication to authenticate each agent for their JWT through a JWT token, so there's only a time-to-live token given to agent ID, and then you can control what type of roles do you want to give it to them.

**Pardeep:** I think it's a three-phase problem. One is an agent identity as a problem. The second problem is access and control. The third problem is the very contextual agent access. Even though the agent has access to all the customer data, because we have given them permissions to their entity, but in real time, you don't actually want to. It's a similar problem of personalization as well.

---

## 19. Community and Next Steps

**Asim:** Do we continue after this class ends to collaborate as a community?

**Doug:** Absolutely. Everyone's in Slack indefinitely. Feel free to use it — that community has been around since 2017.

**Next session (Wednesday):** What if agents could maintain their context not as quote-unquote context, but as information outside of the actual context that goes to the agent? Can we give agents infinite context through searchable external storage?

---

## Companion Resources

- **Slides:** [[articles/2026-06-02_softwaredoug_cheat-at-search-long-running-search|Long Running Search Agents — Cheat at Search (Slides)]]
- **Course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)
- **Author:** [softwaredoug.com](http://softwaredoug.com)
- **Related transcripts:**
  - [[transcripts/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents-lecture|Part 3: Steering Lost Agents]]
  - [[transcripts/2026-06-03_softwaredoug_cheat-at-search-llm-as-judge-lecture|Part 5: LLM as a Judge]]
