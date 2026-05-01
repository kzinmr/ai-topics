---
title: "A non-technical CFO is shipping better code than the agencies he hired"
url: "https://martinalderson.com/posts/non-technical-cfo-shipping-better-code-than-agencies/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-05-01T07:02:07.186772+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# A non-technical CFO is shipping better code than the agencies he hired

Source: https://martinalderson.com/posts/non-technical-cfo-shipping-better-code-than-agencies/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I've been advising non-technical execs at mid-sized companies for a while now. Since the release of Claude Code and other agentic coding tools, I'm starting to see a real shift in what these people can achieve.
I was pretty astonished to see a non-technical friend (CFO) who had managed to use Claude Code to build a pretty impressive internal operations dashboard, tying various systems together. He'd been trying to build this for many years; one of those (many?) projects where it is very useful, but hard to justify the budget/return on investment to hire and manage a full development team.
This project had been tried with various other approaches:
AirTable (fell apart once data reached a certain size, too slow)
Low code tooling (didn't quite work, again, hit scale problems)
A low code agency specialising in retool (many problems from what I can gather transferring business domain knowledge to them)
I told him about Claude Code a month or two ago, and recently caught up with him. To my surprise there was a pretty well thought through application in Next.js which seemed surprisingly bug-free.
If he'd hired a less senior developer with no domain understanding I think getting to the point he got to with Claude Code would have actually been quite challenging.
I think this therefore highlights a significant shift in how software projects are going to be put together. I am not here to suggest that suddenly all developers are going to be replaced - I'll come to some of the areas where they are extremely valuable still - but what is very clear to me is that business people with LLMs
and
all their domain knowledge is an extremely powerful combination for (at least) internal systems.
What I do think is at real risk of automation over the coming years are less senior engineers with limited domain knowledge.
Domain knowledge is what's important in this new era
As someone that has mostly sat at the interface between technical strategy & commercial outcomes for the past decade, I've worked with a lot of great developers who do get the importance of domain knowledge, and others that (usually for corporate culture reasons) get treated as a "JIRA robot", picking up essential random tickets and following them to the letter.
The importance of developers having good domain knowledge and being trusted to experiment within it cannot be underestimated.
It has three main benefits in my view:
It's extremely frustrating for business stakeholders to try to explain intricacies of the problem and the edge cases with someone that doesn't get the business. This causes a major morale drop, and often leads to poor outcomes because stakeholders give up pushing for what they need eventually. Equally it's hard for the developer to get up to speed on years of accumulated organisational knowledge
Perhaps more importantly, it allows developers to have some element of 'predictive software design'. If you know a lot about the industry you are working in, you start being able to predict what parts will need future flexibility and start designing for that even if there isn't a commercial need. You also start to get a feel for what can be 'hardcoded' as it is very unlikely to change.
Finally, and somewhat obviously, it massively improves the cohesion and iteration speed. Product development goes from less of a one way "JIRA factory" to a collaborative option, where developers can offer ideas and suggestions based on the code and the product goals
The issue is if you don't have this culture of shared understanding in your organisation, I think you'll see non technical stakeholders start to build their own products and tools very quickly with these tools.
It completely solves part 1) - they can literally transfer the domain knowledge to the LLM very quickly with a back and forth, and they can work together on 3).
This is going to substantially change the face of the industry. At a minimum we're going to see a lot more fully coded prototypes being handed over to product teams instead of PRDs or sketches of wireframes. I am sure a lot of these tools will also get put into production use - especially at smaller organisations where there isn't a CISO overlooking these kind of deployments.
Where senior developers are still essential
For now I think this is actually all good news for more senior developers, especially with domain knowledge.
While agentic coding tools are improving at a very rapid rate, they don't out of the box tend to setup unprompted:
A proper software development lifecycle
Source control approach and CI/CD
Unit/integration/e2e testing
A well thought out approach to security/access control
Performance/scalability
This tends to be what senior/lead engineers can do in their sleep - take a "MVP" app and make it (more) "production ready" and help on the ongoing scalability of said apps. Ironically, when
prompted correctly
they can do a pretty good job of each of these parts, but it is going to beyond non technical users to understand these concepts to prompt it.
So I can see a world where suddenly organisations have 10-50x the number of internal applications, and senior engineers helping out with taking these MVPs that business stakeholders build and making them production ready.
Jevons Paradox
states that when something gets cheaper, the demand for it often rises far more than the price reduction. We're seeing potentially a 95%+ drop in costs for people to build internal business apps, so we'd expect to see way more of them.
There's always going to be a place for highly knowledgeable, motivated and smart software engineers. But I'm increasingly convinced they are going to see less and less MVPs from start to finish.
How are we going to manage so many new apps?
Where I can see this all going wrong is having so many new apps to manage. We're assuming a lot get transferred to an engineering team to develop further, which I expect will happen to some degree. However, I suspect there is going to be a huge long tail of 'ghost' apps that people build without really thinking too much about the ongoing maintenance.
We're going to need some sort of internal company 'PaaS' to manage them all. This PaaS should handle authentication and data access at a higher level (similar to Cloudflare Zero Trust), but be super simple for people to deploy apps. If we can reduce the attack surface of these apps being hosted on random (personal) Vercel accounts, then that is half the battle.
Ideally this PaaS would automatically manage to a certain degree platform and package updates, automatically deploying security fixes. I think "agentic" DevOps will really help out here - attempting to patch apps, and notifying if the agent fails.
Data exfiltration is a concern but again this PaaS could firewall outbound network (similar to how the Claude analysis tools are hardened to only allow very limited network requests).
However, we must keep in mind that right now this already happens - with a lot of random Excel and Google Sheets running a lot of critical business processes, often being emailed around. So I actually think there is a lot of opportunity to improve security and data access with this new future that's on the way - it's far easier to reason about and secure web applications than Excel files - especially if we could have a centralized, ACL'd SQL database system that isolates everyone's apps correctly, only allowing access to the data they need with the lowest possible permissions.
As such I think it's worth senior technical leadership starting to think of a strategy about this
now
. How would you handle 100x the amount of internal apps, and what processes would you put in place?
When tools like Claude Code get more enterprise support I suspect it's going to be a lot easier to start including an 'organization-level' claude.md file. But let's think this through now and start communicating the plan.
This to me means that developers will move less on line of business apps and more to building the systems, policies and automating the infrastructure, to allow organisations to deliver agentically built business applications at scale.
I'm really excited (and to be honest, slightly scared) about this new future. There are
so many
business challenges that are done in Excel that would unlock so much productivity if they could be built in code.
