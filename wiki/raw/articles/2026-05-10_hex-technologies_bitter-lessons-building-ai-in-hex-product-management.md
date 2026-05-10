---
title: "Bitter lessons building AI products | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/bitter-lessons-building-ai-in-hex-product-management/"
scraped: "2026-05-10T01:28:58.457493+00:00"
lastmod: "2025-10-09"
type: "sitemap"
---

# Bitter lessons building AI products | Hex 

**Source**: [https://hex.tech/blog/bitter-lessons-building-ai-in-hex-product-management/](https://hex.tech/blog/bitter-lessons-building-ai-in-hex-product-management/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
Platform
chevron-down
Products
Agentic notebooks
Powerful, deep-dive analysis without the silos
Conversational self-serve
The best BI tool isn't just a BI tool
semantic-models
Context Studio
Build trust in data with semantic models and AI governance
cli
Hex CLI
Control your analytics from the terminal
Capabilities
Exploratory analysis
Go from quick question to deep analysis to data app in one place
Embedded analytics
Ship secure, customer-facing data experiences
app-builder
Data apps
Build and share interactive dashboards and reporting
Integrations
Out-of-the-box connections and flexible APIs
magic
AI & agents
Agentic workflows to empower your entire team
Solutions
chevron-down
lightbulb
Explore all solutions
One connected system - infinite data answers
By team
solutions-data-leader
Data leader
Focus your team and scale answers
solutions-product
Product
Build your product with data, not gut feels
solutions-marketing
Marketing
Turn scattered data into clear growth opportunities
solutions-sales
Sales
Clear pipeline. Confident forecasts
solutions-customer-success
Customer success
Create a complete view of customer health
Enterprise
Resources
chevron-down
Get started
integrations
Switching to Hex
A guide to getting started on agentic analytics
Templates
Jumpstart with pre-built projects
Hex Foundations
Video series
help
Docs
Resources and product guides
Changelog
Product updates
Inspiration
Blog
From data teams to data teams
Guides
Learn how to do more with data, together
Events
Learn and connect with peers
Customer stories
Empowering the best data teams
Partners
Learn more about our partnerships
save
Download
The Data Leader's Guide to AI Analytics
A practical roadmap for understanding and implementing AI to accelerate your data team and enable true self-service.
Pricing
Log In
Get started
Blog
Bitter lessons building AI products
What actually matters when building AI products when the world keeps changing
Olivia Koshy
Product
October 9, 2025
Share:
twitter
linkedin
In this article
The first failed attempt at building the Notebook Agent
Blinded by “pretty good”
What are we doing differently now?
Building during a technology shift
Get started for free
I was catching up with a friend who had also been building AI products for a few years now. We were lamenting (and laughing) on the graveyard of seemingly-failed projects that now have turned into rapid successes. AI features that were multi-quarter grinds a couple years ago can now be shipped in a matter of weeks.
We realized that we had just actually learned "the Bitter Lesson" - building AI products edition.
The Bitter Lesson
- from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin.
The version of this we – and many others – have learned is that
you shouldn't try to make AI work for your existing roadmap with fancy clever engineering
– much of it will be obsolete with the next major model upgrade (trained with more compute and more data). Instead,
you should aim to understand model capabilities and how you can best pivot your roadmap accordingly.
Some questions I now ask:
What unique value are we delivering that others can't easily replicate?
How can we leverage evolving model capabilities to take advantage of that?
Are we building something that can take advantage of better models, or are we building around existing model deficiencies?
2+ years into building AI features, we’ve also changed a few things about
how
we build:
Ditching demos - we have customers use alpha features early to validate if the feature is even viable.
Spot capability shifts - what does a new model release unlock for you and your team?
Kill projects faster - don’t let sunk cost fallacy keep you building if you realize something isn’t working.
But this wasn’t obvious - and we made a lot of mistakes to get here.
The first failed attempt at building the Notebook Agent
The Notebook Agent has been a
huge hit with customers
, but what folks may not realize is that the core idea of what we built was an idea originally from early 2023. Our team was convinced that this was the future - and we were right, just a bit too early.
We spent a year trying to build the
Notebook Agent in 2023
with the simple goal: users could ask a data question, and AI could generate SQL, charts, and Python to help them draft an answer. Models were not quite ready for complex multi-step reasoning. We built many clever hacks and smart workarounds for model deficiencies.
One example? The model would often doom loop and create cells infinitely if we let it pick which cell to create next. We’d have the model first run a step to “pick” a template of cells to create - SQL, SQL + Chart, Python, Python + Chart. From there, we’d 1-shot the code for each cell based on the sequence of the template chosen.
The feature was a sick demo - but fell flat when actually used for anything mildly complex. The "agent" (
now, better known as a workflow
) struggled to figure out the right data, and when it did, there were often too many gotchas, and it wasn't able to recover from failures.
Our first version of the Notebook Agent from 2023.
Sunk-cost fallacy and deep belief in our notebook domain expertise kept us working on it much longer than we should have.
It was difficult to be intellectually honest with ourselves after pouring so much time into the project.
Reflecting back, because the initial version had dragged on so long, we weren’t as bullish to pick the project back up even when there was a clear model capability shift with the release of Sonnet 3.5.
Blinded by “pretty good”
Using AI to create beautiful, interactive visualizations has been a priority for years. Back in October 2024, we released
Explore
— a new way to visualize data that had more capabilities than ever like pivots, totals, charting, and spreadsheet like functionality.
Of course, when releasing this feature, we figured “it should work with our AI too.” It was easy to disregard the complexity - it was just one cell? How hard would it be for an LLM to generate?
Behind the scenes, any visual cell is a pretty complex JSON that resembles vega-spec, with different rules based on the type of visualization you want to create.
We did some pretty clever engineering — a two-step generation process that took advantage of reasoning models like o3 and a very small fine-tuned model for the actual visualization generation. It worked
pretty good,
and that was perhaps the worst part.
Because it worked
pretty good,
we put our blinders up and focused on optimizing our current implementation, rather than paying attention to new model capabilities.
It was easy to miss the shift to tool calling for complex tasks vs our “2-shot” JSON spec generation.
When we did start building an agentic tool framework, the writing was on the wall; a simple tool calling agentic approaches was obviously 10x better.
Since then, we’ve released
Threads
, which allows anyone in an organization to self-serve their data questions with trusted context and is far more capable than anything we previously had. It can create multiple native Explore visualizations, and we outpaced what previously took months of development, in weeks.
Get useful outputs like summaries and viz.
The bitter lesson repeated itself — our clever (and very cool!) engineering optimizations were completely outpaced by just leveraging improved model capabilities.
What are we doing differently now?
There's some changes in the way we now operate as we continue to build AI features, based on what we’ve learned from the past few years:
Ditching demos
A core principle now is "get it to users before it's ready." When we show the feature to early beta customers, it's no longer a "demo" - we just ask customers to use it directly. If the call feels more like a bug bash, we know we haven’t quite yet built something that works. Real product validation happens in messy, complex customer environments. Do they still want to use it, despite all its rough edges? Speaking from personal experience, AI demos
are often vaporware,
and you can too easily delude yourself into thinking you’ve built something that works.
Spot capability shifts
Sonnet 3.5 and 3.7 were major capabilities shifts that our team didn’t pay close enough attention to. We were using the models internally, but didn’t quite realize how to take advantage of them to their fullest extent, and were still stuck in a RAG + “k-shotting” mindset.
Cursor’s Agent Mode and Claude Code in February of 2025 were telling product shifts — agents were real and actually working. The #1 job, for anyone in charge of the roadmap, is not just to validate that the idea is good and your customers want it, but to validate if the models are truly capable to support that feature today. If not, no amount of clever feature engineering will get it there.
Kill projects faster
As soon as you realize the team needs to hack together a solution to make up for intelligence, cut the project. It’s easy to let your team keep iterating on what you’ve been building because of sunk cost fallacy, or because you’ve committed to a marketing release date — and truthfully, f*** the release date.
When this happens, celebrate the failure — as long as your team was able to move quickly and reorient. Being able to say “no, this isn’t working” is often the hardest skill and you’ll need team leads who are confident to make this call amongst high stakeholder pressure and team emotions!
Lastly, retry failed ideas every ~3 months or just when a new model drops. Sometimes you're just a bit too early.
Building during a technology shift
Part of the reason to share our failures is to help celebrate it. It's hard to not let your ego get in the way when you realize you’ve built a few things that haven’t hit the mark. But my advice is to give yourself some grace; we’re all building in a new space where the ground is shifting beneath us every day. It’s challenging, but I think it’s the most exciting time to be building.
PS: if you want to come work on really cool AI product surface area, reach out!
We’re hiring
💜
Share:
twitter
linkedin
Want to try Hex's AI capabilities?
Get started for free
Request a demo
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
🔊
🎧
on
🌎
.
Company
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
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
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
