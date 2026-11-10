---
title: "Crashing the cost of data intelligence"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/crashing-the-cost-of-data-intelligence/"
scraped: "2026-11-10T06:00:25.734371+00:00"
lastmod: "2026-11-09"
type: "sitemap"
---

# Crashing the cost of data intelligence

**Source**: [https://hex.tech/blog/crashing-the-cost-of-data-intelligence/](https://hex.tech/blog/crashing-the-cost-of-data-intelligence/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
Crashing the cost of data intelligence
Reducing the cost per conversation with the Hex agent by 75%.
Caitlin Colgrove
Engineering
November 9, 2026
Share:
twitter
linkedin
Last October, we introduced the world’s first fully featured
analytics agent
. In the year since, token consumption has grown nearly 100x and keeps climbing.
We’re thrilled with the value customers are getting. But tokens cost money, and a lot of tokens can cost a
lot
of money. For some customers, that was getting in the way.
So we ruthlessly optimized, cutting cost per thread (a multi-message conversation with the Hex agent) nearly 75%: from a high of $6.44 in January to $1.64 today.
Better models helped us bring down the cost of tokens, while improvements to our harness made the agent more efficient at using them. Here's how we did it—and what's next.
Incentives matter
At Hex, we want to build our business by maximizing customers’ intelligence per dollar.
We make neutral or negative margins on AI consumption. Unlike consumption-only models that reward more token spend or promote model lock-in, ours gives us every reason to help customers spend less. We think that’s right for customers, and for us.
Making it work means making intelligence cheap. For the past six months, we’ve focused on two levers: helping customers take advantage of newer models across vendors to balance cost and intelligence, and reducing the tokens our agent needs to answer questions.
Cheaper models, but which ones?
We built our original agent on Opus 4, and for over a year no other model family came close. That changed over the summer with strong releases from OpenAI and competitive open-weight models. But how do you know which models
actually
work well for different analytical tasks?
That’s why we built
DataBench
, a benchmark that tests whether AI agents can think like analysts, not just write correct code. Can they navigate messy data, question suspicious results, and draw conclusions the data actually supports?
Early DataBench results showed Kimi 2.7
performed well on typical tasks
at less than half the cost of Opus, though below frontier performance. We’ve since made the benchmark harder to better measure the frontier.
The real breakout has been OpenAI’s Luna. It trails Opus on DataBench, but at just 5–10% of the cost, it’s often the right tool for the task. A rigorous benchmark lets us recommend it confidently—and our customers are seeing cost-effective results.
Special snowflakes
No benchmark perfectly reflects how a model will perform on your company's data. That’s why
Context Studio
lets customers build eval suites and run model sweeps to find their own cost–intelligence sweet spot. Clean, well-modeled environments may run Luna most of the time; more complex ones may still need Opus.
Admins can then monitor conversations with the Hex agent, including those
automatically flagged
for potential issues. If switching to a cheaper default model doesn't lead to an increase in flagged issues, that’s a good signal you’re saving money without sacrificing quality.
Harness hill-climbing with Hero
We’ve also worked hard to squash token bloat in our harness. There’s no silver bullet, and gains in cost can come at the expense of latency. But we keep finding improvements:
Improving our
long tail of cache misses
(hit rate was 94% but misses were expensive)
Progressive disclosure of tools and moving expensive tools to a subagent
Reducing doom spirals caused by tool errors
Careful analysis of common app building patterns and distilling into a small set of skills
To move faster, we built
Hero
: a background agent that analyzes real user interactions, clusters failure modes, and turns them into actionable harness improvements.
Breaking through with Hex 4.0
By June 2026, costs were coming down, but harness complexity had
exploded.
We had dozens of tools, each with their own complex set of arguments. We’d managed their token footprint, but it was still too much for the model to wield effectively, and worse, a lot of tools were clearly out of distribution for models that had been trained to write code. Further gains needed a different approach.
Enter Hex 4.0
. Our code-first rewrite cut the tool set to around 40, making it simpler for the agent to work efficiently.
The result: an expected 20–40% off thread costs, depending on the task—even before more extensive tuning like we had done on the 3.0 harness.
The path ahead
AI costs deserve scrutiny. As more people chat with data and vibe code dashboards, inefficient agents and overreliance on expensive models can quickly blow a hole in any budget.
Fortunately, the gains aren’t slowing down. We get a front-row seat to how people use AI for analytics, and are constantly searching for new ways to make it cheaper. In the coming months, we're taking this a step further by carrying the knowledge from one analysis forward to the next. The Hex agent can then spend less time and fewer tokens rediscovering what it's already figured out.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
More on Engineering
BLOG
Introducing DataBench
Izzy Miller
·
August 13, 2026
A frontier benchmark for complex data work and analytical reasoning
BLOG
Caching is all you need
Zach Kirby & Olivia Koshy
·
July 29, 2026
Our prompt cache hit rate looked great. Our cost data disagreed. Here's what we found when we stopped trusting the average
BLOG
The AI data sprawl
Barry McCardel
·
September 9, 2026
Nobody can trace it. The data team still owns the mess.
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
✨
🔊
🎧
🌊
🍀
🤠
🎷
on
🌎
.
Platform
AI and agents
Agentic notebooks
Conversational analytics
Context Studio
Data apps
Hex CLI
Business intelligence
Exploratory analysis
Embedded analytics
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Company
About
Careers
Customers
Solutions
Media kit
Newsroom
Connect
Request a demo
Technical support
Contact us
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
You have opted out of data tracking
