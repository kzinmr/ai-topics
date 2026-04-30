---
title: "Has the cost of building software just dropped 90%?"
url: "https://martinalderson.com/posts/has-the-cost-of-software-just-dropped-90-percent/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-30T07:01:57.406629+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Has the cost of building software just dropped 90%?

Source: https://martinalderson.com/posts/has-the-cost-of-software-just-dropped-90-percent/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I've been building software professionally for nearly 20 years. I've been through a lot of changes - the 'birth' of SaaS, the mass shift towards mobile apps, the outrageous hype around blockchain, and the perennial promise that low-code would make developers obsolete.
The economics have changed
dramatically
now with agentic coding, and it is going to totally transform the software development industry (and the wider economy). 2026 is going to catch a lot of people off guard.
In my previous post I delved into why I think
evals are missing
some of the big leaps, but thinking this over since then (and recent experience) has made me confident we're in the early stages of a once-in-a-generation shift.
The cost of shipping
I started developing just around the time open source started to really explode - but it was clear this was one of the first big shifts in cost of building custom software. I can remember eye watering costs for SQL Server or Oracle - and as such started out really with MySQL, which did allow you to build custom networked applications without incurring five or six figures of annual database licensing costs.
Since then we've had cloud (which I would debate is a cost saving at all, but let's be generous and assume it has some initial capex savings) and lately what I feel has been the era of complexity. Software engineering has got - in my opinion, often needlessly - complicated, with people rushing to very labour intensive patterns such as TDD, microservices, super complex React frontends and Kubernetes. I definitely don't think we've seen much of a cost decrease in the past few years.
AI Agents however in my mind
massively
reduce the labour cost of developing software.
So where do the 90% savings actually come from?
At the start of 2025 I was incredibly sceptical of a lot of the AI coding tools - and a lot of them I still am. Many of the platforms felt like glorified low code tooling (Loveable, Bolt, etc), or VS Code forks with some semi-useful (but often annoying) autocomplete improvements.
Take an average project for an internal tool in a company. Let's assume the data modelling is already done to some degree, and you need to implement a web app to manage widgets.
Previously, you'd have a small team of people working on setting up CI/CD, building out data access patterns and building out the core services. Then usually a whole load of CRUD-style pages and maybe some dashboards and graphs for the user to make. Finally you'd (hopefully) add some automated unit/integration/e2e tests to make sure it was fairly solid and ship it, maybe a month later.
And that's just the direct labour. Every person on the project adds coordination overhead. Standups, ticket management, code reviews, handoffs between frontend and backend, waiting for someone to unblock you. The actual coding is often a fraction of where the time goes.
Nearly all of this
can be done in a few hours with an agentic coding CLI. I've had Claude Code write an entire unit/integration test suite in a few hours (300+ tests) for a fairly complex internal tool. This would take me, or many developers I know and respect, days to write by hand.
The agentic coding tools have got
extremely
good at converting business logic specifications into pretty well written APIs and services.
A project that would have taken a month now takes a week. The thinking time is roughly the same  - the implementation time collapsed. And with smaller teams, you get the inverse of Brooks's Law: instead of communication overhead scaling with headcount, it disappears. A handful of people can suddenly achieve an order of magnitude more.
Latent demand
On the face of it, this seems like incredibly bad news for the software development industry - but economics tells us otherwise.
Jevons Paradox
says that when something becomes cheaper to produce, we don't just do the same amount for less money. Take electric lighting for example; while sales of candles and gas lamps fell, overall
far
more artificial light was generated.
If we apply this to software engineering, think of supply and demand. There is
so much
latent demand for software. I'm sure every organisation has hundreds if not thousands of Excel sheets tracking important business processes that would be far better off as a SaaS app. Let's say they get a quote from an agency to build one into an app for $50k - only essential ones meet the grade. At $5k (for a decent developer + AI tooling) - suddenly there is far more demand.
Domain knowledge is the only moat
So where does that leave us? Right now there is still enormous value in having a human 'babysit' the agent - checking its work, suggesting the approach and shortcutting bad approaches. Pure YOLO vibe coding ends up in a total mess very quickly, but with a human in the loop I think you can build incredibly good quality software,
very
quickly.
This then allows developers who really master this technology to be hugely effective at solving business problems. Their domain and industry knowledge becomes a huge lever - knowing the best architectural decisions for a project, knowing which framework to use and which libraries work best.
Layer on understanding of the business domain and it does genuinely feel like the mythical 10x engineer is here. Equally, the pairing of a business domain expert with a motivated developer and these tools becomes an incredibly powerful combination, and something I think we'll see becoming quite common - instead of a 'squad' of a business specialist and a set of developers, we'll see a far tighter pairing of a couple of people.
This combination allows you to iterate incredibly quickly, and software becomes almost disposable - if the direction is bad, then throw it away and start again, using those learnings. This takes a fairly large mindset shift, but the hard work is the
conceptual thinking
, not the typing.
Don't get caught off guard
The agents and models are still improving rapidly, which I don't think is really being captured in the benchmarks. Opus 4.5 seems to be able to follow long 10-20 minute sessions without going completely off piste. We're just starting to see the results of the hundreds of billions of dollars of capex that has gone into GB200 GPUs now, and I'm sure newer models will quickly make these look completely obsolete.
However, I've spoken to so many software engineers that are really fighting this change. I've heard the same objections too many times - LLMs make too many mistakes, it can't understand
[framework]
, or it doesn't really save any time.
These assertions are rapidly becoming completely false, and remind me a lot of the desktop engineers who dismissed the iPhone in 2007. I think we all know how that turned out - networking got better, the phones got way faster and the mobile operating systems became very capable.
Engineers need to really lean in to the change in my opinion. This won't change overnight - large corporates are still very much behind the curve in general, lost in a web of bureaucracy of vendor approvals and management structures that leave them incredibly vulnerable to smaller competitors.
But if you're working for a smaller company or team and have the power to use these tools, you should. Your job is going to change - but software has always changed. Just perhaps this time it's going to change faster than anyone anticipates. 2026 is coming.
One objection I hear a lot is that LLMs are only good at greenfield projects. I'd push back hard on this. I've spent plenty of time trying to understand 3-year-old+ codebases where everyone who wrote it has left. Agents make this dramatically easier - explaining what the code does, finding the bug(s), suggesting the fix. I'd rather inherit a repo written with an agent and a good engineer in the loop than one written by a questionable quality contractor who left three years ago, with no tests, and a spaghetti mess of classes and methods.
