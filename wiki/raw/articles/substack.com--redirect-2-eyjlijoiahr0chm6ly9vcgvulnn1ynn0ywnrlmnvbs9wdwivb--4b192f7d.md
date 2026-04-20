---
title: "🎙️ This week on How I AI: How Intercom 2x’d their engineering velocity with Claude Code"
url: "https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvbGVubnkvcC90aGlzLXdlZWstb24taG93LWktYWktaG93LWludGVyY29tP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj0yZmx4NiZ0b2tlbj1leUoxYzJWeVgybGtJam8wTURnM05EZ3lMQ0p3YjNOMFgybGtJam94T1RReU5UTXpPVFlzSW1saGRDSTZNVGMzTmpjd01EQXpOaXdpWlhod0lqb3hOemM1TWpreU1ETTJMQ0pwYzNNaU9pSndkV0l0TVRBNE5EVWlMQ0p6ZFdJaU9pSndiM04wTFhKbFlXTjBhVzl1SW4wLl9rZFlvSXpNdEdSTUFST3k2aHZmSzB6VnVtdjgySHNKTTFKNTViVk81T1UiLCJwIjoxOTQyNTMzOTYsInMiOjEwODQ1LCJmIjp0cnVlLCJ1Ijo0MDg3NDgyLCJpYXQiOjE3NzY3MDAwMzYsImV4cCI6MjA5MjI3NjAzNiwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.ODYg2R5I1FLDnzN036sgczDZmGg27mRZA2D8YcZmNSk?&utm_source=substack&utm_medium=email"
fetched_at: 2026-04-20T15:47:29.719285+00:00
source_date: 2026-04-20
tags: [newsletter, auto-ingested]
---

# 🎙️ This week on How I AI: How Intercom 2x’d their engineering velocity with Claude Code

Source: https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvbGVubnkvcC90aGlzLXdlZWstb24taG93LWktYWktaG93LWludGVyY29tP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj0yZmx4NiZ0b2tlbj1leUoxYzJWeVgybGtJam8wTURnM05EZ3lMQ0p3YjNOMFgybGtJam94T1RReU5UTXpPVFlzSW1saGRDSTZNVGMzTmpjd01EQXpOaXdpWlhod0lqb3hOemM1TWpreU1ETTJMQ0pwYzNNaU9pSndkV0l0TVRBNE5EVWlMQ0p6ZFdJaU9pSndiM04wTFhKbFlXTjBhVzl1SW4wLl9rZFlvSXpNdEdSTUFST3k2aHZmSzB6VnVtdjgySHNKTTFKNTViVk81T1UiLCJwIjoxOTQyNTMzOTYsInMiOjEwODQ1LCJmIjp0cnVlLCJ1Ijo0MDg3NDgyLCJpYXQiOjE3NzY3MDAwMzYsImV4cCI6MjA5MjI3NjAzNiwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.ODYg2R5I1FLDnzN036sgczDZmGg27mRZA2D8YcZmNSk?&utm_source=substack&utm_medium=email

Brought to you by:
Brian Scanlan
, Senior Principal Engineer at Intercom, breaks down how the company doubled engineering throughput in just nine months by going all-in on Claude Code. He shares how custom skills, deep telemetry, and a culture of permission turned AI into a true force multiplier.
Treat your engineering org like a product, and instrument everything.
Intercom tracks skill invocations in Honeycomb, stores anonymized Claude Code sessions in S3, and built custom dashboards that show engineers how they compare to peers. This isn’t surveillance—it’s the same product thinking you’d apply to customer-facing features. You can’t improve what you don’t measure, and you can’t scale AI adoption without visibility into what’s working and what’s breaking.
The 2x velocity gain is real, but only if you prepare your foundation.
Intercom doubled their merged PRs per R&D employee in nine months, but they already had mature CI/CD, comprehensive test coverage, and a high-trust culture. AI magnifies your strengths and weaknesses—if your deployment pipeline is broken or your code review process is manual chaos, AI will just help you ship broken code faster. Fix your fundamentals first, then pour gasoline on the fire.
Custom skills with hooks enforce quality at the point of creation, not after the fact.
Intercom’s “Create PR” skill blocks Claude Code from using the GitHub CLI directly and forces it to write context-rich PR descriptions instead of just regurgitating code. Build guardrails that make the golden path the only path.
Code quality improves when you ship twice as fast because you finally have capacity for tech debt.
Intercom’s partnership with Stanford researchers shows their code quality metrics are going up, not down. When the cost of fixing flaky tests, improving developer experience, and tackling technical debt compresses to near-zero, you can actually do those things instead of just talking about them in retros. The business constraint on internal projects disappears when agents can execute them in hours instead of quarters.
The most important job of technical leadership in the AI era is giving permission and taking accountability.
Brian’s framework is simple: Tell people they can do things, and if anything goes wrong, blame me. Engineers don’t need more tutorials or documentation; they need permission to connect Claude Code to Snowflake, to ship code from their phone on the subway, to build a CLI that bypasses email verification. The activation energy for experimentation is cultural, not technical.
Make your product agent-friendly or watch customers build it themselves.
Brian built an Intercom CLI that can autonomously sign up for Fin, verify email addresses by accessing Gmail, and complete installation without human intervention. If you don’t build this, your customers’ agents will just brute-force your website, burn more tokens, get frustrated, and eventually press escape and build it themselves. The switching cost is literally one keystroke. Your conversion funnel is now invisible, and your drop-off point is “forget it, let’s do this a different way.”
All work will become agent-first, and you should set a deadline for it.
Brian’s vision is that by the end of any given month, the first response to an alarm, a planning meeting, or a customer question should be an agent doing the basic work. This isn’t aspirational—it’s a realistic expectation given the current state of models and harnesses. The bottleneck isn’t the technology; it’s organizational willingness to reimagine workflows from first principles and give people permission to experiment.
If you’re enjoying these episodes, reply and let me know what you’d love to learn more about: AI workflows, hiring, growth, product strategy—anything.
Catch you next week,
Lenny
P.S. Want every new episode delivered the moment it drops? Hit “Follow” on your favorite podcast app.
