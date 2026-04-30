---
title: "Karpathy Second Brain Mercury"
source: "https://x.com/i/article/2049082538686382397"
date: 2026-04-30
type: x_article
tweet_id: "2049082538686382397"
---

A technical look at why the LLM Wiki pattern resonated, where it starts to fail at machine scale, and what serious agent memory likely looks like next.
 
When Andrej Karpathy shared his LLM Wiki workflow, it spread quickly for a reason.
The idea was clean, practical, and immediately useful:
Put raw source material into a folder.
Let an LLM turn it into an evolving Markdown wiki.
Browse it in Obsidian.
Keep improving the knowledge base over time.
No complex stack.
No heavy infrastructure.
Just local files, plain text, and a model that compounds knowledge instead of repeatedly forgetting it.
That mattered.
Because most AI systems still do the same wasteful loop:
Retrieve.
Answer.
Forget.
Repeat.
Karpathy’s model breaks that cycle.
Instead of rediscovering the same information every session, the system builds a persistent artifact that improves with use.
For researchers, writers, analysts, and developers learning a domain, that is a genuine step forward.
But the viral discussion skipped the harder question:
What happens when the user is no longer a human, but an autonomous agent running all day?
That is where the architecture changes.
 
Human Memory and Agent Memory Are Different Problems
A human second brain optimizes for:
Readability.
Browsing.
Reflection.
Learning.
Manual correction.
An agent memory system optimizes for:
Fast retrieval.
Persistent state.
Low token cost.
Conflict resolution.
Repeated automated use.
Reliable updates.
Those are not the same workload.
What feels elegant for a person can become expensive for software.
 
Why the Wiki Pattern Works So Well
Markdown has real strengths:
Portable.
Inspectable.
Versionable.
Local-first.
Easy to own long term.
Obsidian adds navigation, graph views, backlinks, and search.
That combination is excellent for human knowledge work.
It gives people leverage without lock-in.
 
Where It Starts to Break for Agents
The issue is not Markdown.
The issue is using human note architecture as the operational memory layer for autonomous systems.
1. Agents Often Need Facts, Not Pages
A human may want to read a page.
An agent often needs one answer:
Preferred deployment target.
Current budget limit.
Unresolved task.
Latest user preference.
If the system must load a document to extract one sentence, memory becomes inefficient.
Across thousands of calls, that becomes structural waste.
2. Tokens Become a Real Budget
Every irrelevant token loaded into context increases:
Cost.
Latency.
Distraction risk.
Long-running agents need selective retrieval, not memory dumps.
They need the right memory, not the most memory.
3. Memory Drift Is Real
Preferences change.
Projects evolve.
Decisions get reversed.
Old assumptions expire.
If outdated notes continue to rank equally with fresh information, the agent starts reasoning on stale state.
That is not clutter.
It is a reliability problem.
4. Ranking Matters More Than Storage
As memory grows, the real challenge becomes:
What is newest.
What is strongest.
What is relevant now.
What should be ignored.
Storage is easy.
Prioritization is hard.
5. Continuous Writes Change Everything
Humans update notes occasionally.
Agents may update memory after tasks, conversations, tool calls, and decisions.
That favors systems built for structured writes, deterministic updates, and queryable state.
At that point, memory is no longer a notebook.
It is infrastructure.
 
This Is Not a Criticism of Karpathy
Karpathy’s pattern is strong for what it was built for.
It moves people beyond stateless chat.
It makes knowledge compound.
It keeps ownership local.
It turns AI into a collaborator instead of a one-shot assistant.
That is meaningful progress.
But human-facing knowledge systems and machine-facing memory systems are different categories.
What works beautifully for humans is not automatically what machines need.
 
What Serious Agent Memory Requires
The strongest memory systems are converging on a few principles.
Selective Injection
Only relevant memory enters context.
Everything else stays in storage.
Structured Retrieval
Agents should be able to query:
Latest valid preference.
Task state.
Related decisions.
Relevant prior context.
Not just read notes and infer.
Scoring
Memories need metadata such as:
Confidence.
Freshness.
Importance.
Reinforcement.
Without scoring, everything competes equally.
Conflict Resolution
When two facts disagree, the system needs rules.
Newer wins.
Higher-confidence wins.
Or ask the user.
Silent contradiction is failure.
Decay
Some memory should weaken, expire, or be archived.
An agent that remembers everything equally eventually remembers poorly.
 
The Best Architecture Is Hybrid
This is not Markdown vs database.
It is usually both.
Markdown for Humans
Use it for:
Notes.
Reports.
Summaries.
Journals.
Identity files.
Structured Memory for Agents
Use it for:
Facts.
Entities.
Relationships.
Preferences.
Task state.
Indexes.
Timestamps.
Scoring.
That gives humans readability and agents efficiency.
Markdown as interface. Structured memory as substrate.
That is the practical direction.
Where Mercury Fits
Mercury was built around this distinction.
Identity should be human-owned.
Memory should be machine-efficient.
That means editable soul and persona files for users, paired with operational memory optimized for retrieval, persistence, and token-aware context injection.
The goal is not to remember more.
The goal is to remember correctly, cheaply, and when useful.
Why This Matters
The industry is racing toward:
More tools.
Bigger context windows.
Faster models.
More integrations.
Useful, yes.
But substrate matters more.
If memory is weak, agents become powerful but unstable.
They can act.
They cannot compound context reliably.
The Real Shift
The first generation of AI helped us generate answers.
The next generation must sustain context.
We are moving from AI you open occasionally to software that runs continuously, knows your workflows, and acts on your behalf.
That requires memory designed for machines:
Structured.
Selective.
Scored.
Inspectable.
Token-aware.
Built to improve without drifting.
Karpathy helped start that conversation.
The next phase is engineering it properly.
And that is where Mercury is building.
Mercury Agent
Open source. MIT licensed. 

mercury.cosmicstack.org
