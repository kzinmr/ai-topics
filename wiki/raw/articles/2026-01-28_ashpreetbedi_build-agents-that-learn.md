---
title: "Build Agents That Learn"
created: 2026-01-28
date_ingested: 2026-05-14
type: x_article
x_article_tweet_id: "2016318096772936159"
x_article_author: "Ashpreet Bedi"
x_article_author_handle: "@ashpreetbedi"
source: "https://x.com/ashpreetbedi/status/2016318096772936159"
tags: [x-article]
---

Agents are changing how we work. But there's a gap between what we expect from them and what they actually deliver.
Most agents are stateless. They reason, respond, forget. Every conversation starts from zero. 
This isn't a flaw in any particular framework. It's how LLMs work. The model doesn't remember the messages it received, the tool calls it made, or what happened three turns ago.
If you want an agent that learns, you have to build that capability yourself.
We did, and here's how it works.
What Learning Isn't
Before we talk about learning, let's clear up what doesn't count.
Session history isn't learning. It's a transcript that gets thrown away when the session ends. Useful for context within a conversation. Useless across conversations.
RAG isn't learning. RAG is retrieval. You loaded static documents. The agent can search them, but it didn't discover anything. It's not getting smarter.
Fine-tuning isn't learning. Fine-tuning happens offline. Your agent can't learn while it's running. And you probably don't want to fine-tune on every conversation anyway.
Memory is a noun. Learning is a verb. This might seem like wordplay, but the shift in perspective matters. Memory is static: a database of facts. Learning is dynamic: it evolves, compounds, gets sharper. Memory stores what you said. Learning figures out what it means.
So what does actual runtime learning look like?
An agent that remembers users across sessions. That captures insights from conversations. That learns from its own decisions and feedback. Where knowledge from one user can benefit another.
That's what we built.
Learning in Action
 
Set `learning=True` and the agent automatically captures user profiles and memories in the background. It recalls them in future sessions. No explicit tool calls. No manual context injection.
Your agent now remembers.
But that's just the beginning.
Level 1: The Agent Remembers You
 
Session 2 is a completely new conversation. Different session ID. But the agent knows Alice's name, her role, her preferences. It responds accordingly.
Behind the scenes, two things are happening:
User Profile captures structured facts: name, role, company, preferences. These get updated in place as new information arrives.
User Memory captures unstructured observations: "prefers concise responses", "works on ML projects", "mentioned struggling with async code". These accumulate over time.
Both are extracted automatically after each response. No tool calls visible. The agent just... learns.
Level 2: The Agent Captures Insights
For some types of learning, you want the agent to decide what's worth saving. Not everything in a conversation is valuable. The agent should have judgment.
 
In Agentic mode, the agent receives tools: `save_learning`, `search_learnings`. It decides when to use them.
When a user shares something genuinely useful (a non-obvious insight, a best practice, a pattern that might help others), the agent saves it. When answering a question, the agent searches for relevant prior learnings first.
The agent also logs its decisions. Why did it recommend Python over JavaScript? Why did it search the web instead of answering from memory? Decision logs capture this reasoning, useful for auditing and debugging.
 
The agent can now log decisions with reasoning, record outcomes, and search past decisions. When something goes wrong, you know why.
Level 3: Knowledge Compounds Across Users
This is the breakthrough.
 
Now watch what happens:
Session 1, Engineer 1:
"We're trying to reduce our cloud egress costs. Remember this."
The agent saves the insight.
Session 2, Engineer 2 (different user, different session, a week later):
"I'm picking a cloud provider for a data pipeline. Key considerations?"
The agent surfaces the egress cost insight. Unprompted. No shared context. No explicit handoff. Engineer 2 benefits from what Engineer 1 discovered.
One person taught the agent something. Another person benefited from it. 
No fine-tuning. No RLHF infrastructure. Just a database and some prompt engineering. GPU Poor Learning. It works.
If you're on a team where people work with agents all day, this changes everything. When one person figures out how to test a tricky feature, everyone benefits automatically. When someone discovers a gotcha in the codebase, the whole team knows.
This is how agents become organizational memory.
The Full Picture
Learning happens through learning stores. Each store captures a different type of knowledge:
User Profile: Name, role, preferences (per user)
User Memory: Observations from conversations (per user)
Session Context: Goals, plans, progress (per session)
Entity Memory: Facts about companies, projects, people (configurable)
Learned Knowledge: Insights that transfer across users (configurable)
Decision Log: Decisions with reasoning (per agent)
Each store can operate in a different learning mode:
Always: Extraction runs automatically after each response
Agentic: Agent receives tools and decides what to save
Propose: Agent proposes learnings, you confirm before saving
Mix and match. Automatic profile extraction. Agent-driven knowledge capture. Human-approved insights for high-stakes domains.
 
One agent. Four learning stores. Configured independently. The agent learns who users are, what they're working on, what insights matter, and why it made the decisions it made.
But these are just the built-in stores. Need something different? The Learning Protocol lets you build custom stores for your domain.
 
Four methods. ~50 lines. Your domain, your rules. Legal docs. Medical records. Codebases. Sales pipelines. Whatever you need.
Why This Matters
Claude's memory feels magical. It's natural, contextual, never announces "saving to memory". It just knows you. But you can't build with it. Claude's memory is a consumer product feature. The API gives you nothing. If you want learning for your agents, you're on your own.
That's why we built this.
Support agents that get better with every ticket. Ticket #1000 gets resolved faster because the agent learned from tickets #1-999. Solutions that worked. Patterns that recur. Gotchas to avoid.
Coding assistants that learn your codebase. Not just RAG over your docs—actual learning. How you test. How you structure code. What your team's conventions are. The agent adapts to your way of working.
Team knowledge that compounds. When one analyst discovers something, the whole team benefits. No Slack message that gets buried. No wiki page that gets stale. The knowledge lives in the agent.
The agent on day 1000 is fundamentally better than it was on day 1.
Your Data Stays Yours
Everything runs in your infrastructure. Your database. Your vector store. Your cloud.
This isn't a hosted memory service. No vendor has access to your learnings. No data leaves your environment. You own the database. You own the knowledge.
Query it with SQL. Build dashboards. Export whenever you want. Your data. Your choice.
Get Started
One line to enable learning:
 
Your agents learn now.
→ Get Started
→ GitHub
 
Agno is an open-source framework for building agents that learn. Persistent storage, learning stores, and cross-user knowledge transfer. All built in.
