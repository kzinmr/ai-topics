---
title: "AI Engineering has a Runtime Problem"
created: 2026-01-15
date_ingested: 2026-05-14
type: x_article
x_article_tweet_id: "2011607262893129943"
x_article_author: "Ashpreet Bedi"
x_article_author_handle: "@ashpreetbedi"
source: "https://x.com/ashpreetbedi/status/2011607262893129943"
tags: [x-article]
---

Claude Code shipped two years after function calling.
Models have outpaced the application layer. We have frameworks to build agents, we have observability to trace them, we have evals to test them. But nothing to run them.
AI engineering has a runtime problem.
The runtime is what turns a python script into a working product. It runs our agents as an API. It manages state across users and sessions, streams responses without breaking, stores memory and context, recovers when things crash, provides request-level isolation. Its the backend for AI.
In web development, this was solved decades ago. In AI engineering, every team builds it from scratch - streaming, state management, recovery, all of it. Most teams spend months on infrastructure before shipping anything.
Every tutorial ends with a notebook. Production is left as an exercise for the reader.
The AI Stack
Here's how I see the AI stack today:
 
Every other layer has tooling. The runtime is the hole every team is missing.
Why Agents Are Different
Traditional web applications follow a simple request-response pattern: request comes in, server processes it, response goes out. Thousands of requests per second, each independent. Scale horizontally by adding servers. This is solved infrastructure.
Agents break this model completely.
An agent isn't a request-response cycle. It's a long-running, stateful process. It receives input. It thinks, calls a tool, waits for the result, reasons, responds. The user sends another message. The agent thinks, now with full context of everything before, reasons, responds.
A single session can span minutes, hours, or days - paused while waiting, resumed on input, cancelled if the user walks away.
Agents are stateful, but scalable infrastructure is stateless by design.
Building stateful applications on stateless infrastructure is one of the hardest problems in distributed systems. Every AI team is solving it from scratch, all while building the actual product.
What the Runtime Actually Does
The runtime handles deployment. You package your agent into a container, deploy it to your cloud, and the runtime handles everything between your code and your users.
Serving: Exposes your agents as an API. HTTP, WebSockets, SSE. Requests route to the right agent with the correct state.
State Management: Sessions persist across containers and survive restarts. State doesn't bleed between users. The agent picks up exactly where it left off, regardless of which container handles the next request.
Streaming: Durable streams that survive network hiccups. Backpressure when the client can't keep up. Graceful resumption after disconnects. Users see tokens flowing, not blank screens.
Storage: Your runtime needs a database - not as an afterthought, but as a core primitive. Sessions, memory, knowledge, traces, conversation history: all stored in your infrastructure, not scattered across third-party services.
Recovery: Container dies mid-reasoning? State is checkpointed. Context preserved. The runtime resumes the conversation. The user doesn't notice.
Scale: 100,000 concurrent users, each with multiple sessions, none interfering with each other. Horizontal scaling that actually works for stateful processes.
Request Isolation: Every request lives in complete isolation. User A's context never touches User B's memory space. Not "probably won't leak". Guaranteed  isolation at the infrastructure level. 
This is hard. Really hard. But it's infrastructure. Solve it once, not for every project.
Why This Hasn't Been Solved
Everyone assumed existing infrastructure would handle it.
Framework companies focused on building agents. Makes sense, that's the AI part. But then they stopped at the notebook. "Here's a notebook demo. Deployment is your problem."
Observability companies focused on watching agents. Tracing, logging, debugging. Valuable, but you can't observe what isn't running.
Eval companies focused on testing agents. Benchmarks, regression suites, quality metrics. Also valuable, but you can't test your way to production.
Everyone pointed at the next layer. Nobody built it.
And so teams reach for what they know: "Just use FastAPI". Then they discover they need to build 50+ endpoints, manage state across containers, handle streaming that doesn't break, recover from mid-conversation failures, scale without state bleeding. They spend 6 months building serving infrastructure instead of product.
This is why most agent projects never reach production. Not because the agents aren't smart enough. Because there's no runtime to run them.
The Runtime is the Foundation
Frameworks, observability, evals. None of it matters if you can't run the thing. Everything except the runtime is a demo.
We've spent the last year building it. More soon.
