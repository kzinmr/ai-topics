---
title: "AI-pilling our company: lessons learned"
url: "https://sierra.ai/blog/ai-pilling-our-company-lessons-learned"
fetched_at: 2026-07-10T07:01:42.336065+00:00
source: "Sierra Blog"
tags: [blog, raw]
---

# AI-pilling our company: lessons learned

Source: https://sierra.ai/blog/ai-pilling-our-company-lessons-learned

In 1968, a
seminal study
found something that would shape Silicon Valley for decades: the best software engineers were dramatically more productive than their peers. Ever since, every technology company has been hunting for those rare individuals capable of generating extraordinary results.
Returning from the holidays in January, AI-pilled by the advances in the frontier models, our engineering team started running agents in parallel with git worktrees, Claude Code, and Codex. On some tasks, they were getting 5X more done.
That raised a bigger question: if agents could make engineers that much more productive in a month, what would it take to get everyone at Sierra there? We set up a six-person AI acceleration team to find out. This blog explains what we’ve built, and what we learned in the process.
1. Agent, singular
We began with a group of role-specific agents: a support agent (PINE), a data analyst (Pinewood), an engineer (Pinecone), and a sales agent (Reggie Jr). An agent per role may seem intuitive, but it failed in practice.
Superficially, the problem was the burden on employees, who had to remember which agent did what. Our love of pine-themed names didn’t help. But the deeper issue was structural — the most important work happens across teams not within them.
At their core, companies are a collection of jobs to be done. Take shipping a product. It involves technical teams as well as sales, marketing, legal, and operations. Departments exist because one team or person cannot do every part of the job. AI changes that, as it can increasingly complete work end-to-end.
So we collapsed all these role-specific agents into Pinecone: a single agent with one Slack handle, one URL, and one unbroken thread from question to finished result. Pinecone figures out which systems to pull from, and what to do with a request, so employees don’t have to. That’s technically hard, but that’s the point of AI: technology absorbs the complexity, not the employee.
It’s a lesson we had already learned with our platform. Agents built on Sierra are full-service: one agent can handle everything from product discovery to account set-up, troubleshooting, billing and more. Not "press one for sales, press two for support" like an old IVR.
Collapsing everything into one agent gets you much closer to where the value in a company lies — the jobs to be done. Every improvement benefits the entire business, so everyone gets better, faster.
2. Proactive, not reactive
Most work isn't completed in a single sitting. It unfolds over days, weeks, or even months as teams learn, priorities shift, and new information emerges. An agent that shows up when prompted and disappears when the session ends is only so useful. Pinecone persists across the whole process — carrying context forward and picking the thread back up, until the job, not just the individual request, is done.
Persistence also makes Pinecone proactive. Instead of waiting to be asked, it can act when the next step is ready — a webhook fires on an artifact, a task lands in Linear, a review comes in. It gathers context and takes a first pass, bringing people in when their judgment is needed. Prep notes are waiting before a meeting. Interview debriefs are drafted before you sit down to add your scores. Reviews arrive with summaries, key risks, and suggested comments. The goal isn't more notifications. It's less work arriving unfinished.
We haven't fully nailed this yet — most sessions still begin with a human prompt — but inverting that relationship, so agents prompt humans when needed, is where persistence is taking us.
3. Business context is the bottleneck, not intelligence
The bottleneck with AI was raw intelligence — whether a model was smart enough. Today, frontier models are capable enough for most business needs. So the bottleneck has moved to context: what's specific to your company, your workflows, your history, the judgment calls that don't show up in any training set.
In January, two people on our team hacked together a data analyst agent using Claude Code and Opus 4.6, connected to our systems through Model Context Protocol (MCP) and command-line tools. Without much additional guidance, it could investigate a customer issue across Slack, GitHub, ClickHouse, Salesforce, and PagerDuty in minutes. Work that once consumed an afternoon became the first step in debugging and incident response.
The same pattern extends well beyond debugging. An agent with complete context can prepare a customer meeting, research an account, review a contract or RFP, trace a product decision, and turn scattered work into a finished artifact. Of course, giving an agent access to all of that context introduces a new problem. An unrestricted agent is a massive security and privacy risk. Our MCP Gateway solves this: Pinecone inherits each employee's access, enforces policy at every tool call, isolates customer data, and leaves an audit trail.
Pinecone is built on Claude Code and Codex. Their frequent improvements are a tailwind, but the state of the art shifts constantly — one model may be best at planning, another at coding, another at prose. Owning the layer above the models lets us route each task to the right model, fail over during downtime, and manage cost, while avoiding being at the mercy of any one player. But the durable advantage isn't owning the underlying model. It's owning the context, workflows, and routing layer that make every model more useful.
We're also experimenting with letting Pinecone dream: reflecting on each day's work and proposing improvements to its own skills. Over time, that's the difference between an agent that just works for Sierra and one that learns from Sierra.
4. The agent is the UI, the system of record the backend
Every piece of work produces something concrete, an artifact. Coding agents found theirs first: the pull request. Every other department has its own equivalent — a customer story, a contract, an RFP questionnaire, a pitch deck, a performance review.
Artifacts are both the input and the output. They give agents the context they need to do the work — and they're where the finished work belongs. Ask Pinecone to tighten a pitch deck, and the deck itself comes back updated, not a chat message telling you what to change.
We've found it's best to work with your systems of record, not replace them. GitHub keeps the PR, Salesforce keeps the account, and Linear keeps the issue — the agent is the layer across them.
Replacing those systems means recreating decades of mature software. Worse, it splits the company in two — people working through the agent and people working directly in the original tools, each with their own version of the truth. Our bet is that these products become more like backends over time, with the agent as the primary interface.
5. Outcomes, not just activity
Since Pinecone's first commit in March, it's run more than 75,000 sessions for 600+ people. Today, 70% of our PRs are opened through it, while hundreds of automations quietly handle work no one explicitly prompted.
Numbers like that are tempting to lead with, and early on they're the right thing to track — they're evidence something is actually being used, not sitting on a roadmap slide gathering dust. But sessions run and tool calls made are activity, not outcome. A team can tokenmaxx its way to an impressive-looking adoption chart without anything downstream actually getting better — the same number of mistakes, the same cycle times, just more AI involved in producing them.
So token usage is a fine place to start. Teams need to form the habit of using the tool before you can measure whether it's working. But it's not where the value is, and we don't want it to be where the story ends. The question we're trying to get better at asking isn't how much an agent did — it's what actually changed because of it: whether a deal closed faster, whether a customer's issue got resolved on the first pass, whether someone got their evening back instead of finishing a review late into the night.
We don't have a good way to measure that yet. Sessions and tool calls are just easier to count. But that gap — between what we can measure today and what we actually care about — is the next thing we're building toward.
That 1968 study found a 10X gap between the best and the rest — and for fifty years, the only answer was to go hunt for those rare people. Now there's a better one: give everyone an agent so they have the advantages of the few. The goal isn't just to get more done. It's to give people more time for the work that only people can do: judgment, taste, creativity, and building relationships.
Up next
We’ll do deeper dives on the systems we’ve built:
Allen Chen
on Pinecone, its many iterations, and the technical architecture behind it
Mihai Parparita
on MCP Gateway and safely gathering complete context
Rohith Ravi
on Agency, the infrastructure underneath it all
