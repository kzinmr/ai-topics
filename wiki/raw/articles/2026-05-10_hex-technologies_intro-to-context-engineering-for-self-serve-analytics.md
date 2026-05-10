---
title: "How context engineering makes or breaks AI-driven self-service | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/intro-to-context-engineering-for-self-serve-analytics/"
scraped: "2026-05-10T01:29:02.641023+00:00"
lastmod: "2025-11-05"
type: "sitemap"
---

# How context engineering makes or breaks AI-driven self-service | Hex 

**Source**: [https://hex.tech/blog/intro-to-context-engineering-for-self-serve-analytics/](https://hex.tech/blog/intro-to-context-engineering-for-self-serve-analytics/)

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
How context engineering makes or breaks AI-driven self-service
AI agents for analytics only work if they know what they're talking about
Andrew Lee
Data
November 5, 2025
Share:
twitter
linkedin
In this article
What is context?
Why context matters more than the model
The data team’s job is shifting from answering one-off questions to building a context lake
4 Principles for effective context engineering
Four tools to steer your agents
From vicious to virtuous
Choose progress over perfection when it comes to context
Get started for free
Here's the thing about AI in analytics: it's either going to amplify your team's expertise or undermine it. The difference comes down to context.
We've worked with hundreds of data teams at Hex navigating this exact challenge. This guide shares what we've learned about context engineering — teaching AI agents about your business so they actually deliver trustworthy results instead of confident hallucinations.
What is context?
Context is the business knowledge you give AI agents so they understand your specific data environment. It's the difference between an AI that sees "customer_segment" as just a column name and one that knows SMB means companies with fewer than 100 employees at your company.
This includes things like which tables are your source of truth, how you calculate key metrics, your naming conventions, the quirks in your data, and the business rules that govern how everything should be interpreted.
Why context matters more than the model
Context is how you get your stakeholders
useful and relevant metrics
with AI. Better context means more accurate answers. Accurate answers build trust. Trust means people actually use self-serve tools instead of going back to the data team for every question. That's how you scale.
But LLMs don't know anything about your business out of the box. They can't tell the difference between three metrics all called "revenue" but calculated differently depending on the use case.
The question isn't if people will use AI for data — it's whether they'll use AI grounded in your team's knowledge or AI that's guessing based on column names alone.
The data team’s job is shifting from answering one-off questions to building a context lake
Working with hundreds of data teams implementing AI at Hex, I've seen a fundamental shift in how successful teams operate. Instead of being query mechanics answering the same questions over and over, they're becoming context engineers.
The old model was exhausting: business user asks question, data team writes SQL, repeat forever. No learning, no compounding value, just an endless queue.
The new model is different. You're building what I call a "context lake" — a living repository of business knowledge that AI agents can draw from. Every analysis you create, every metric you define, every edge case you document becomes part of this knowledge base.
Here's what changes: you're not trying to anticipate every possible question upfront (that's the old way). You're giving AI the knowledge it needs to navigate safely when someone asks something you didn't anticipate. You're building guardrails, not gates.
This isn't about replacing data teams. It's about scaling your expertise across the organization. When you encode your knowledge into context, you're not just answering today's question — you're teaching the AI how to answer tomorrow's questions correctly.
4 Principles for effective context engineering
Before diving into the specifics, let's establish some core principles that will guide your context engineering efforts. These principles will help you build a framework that makes AI analytics both reliable and scalable for your company.
1. Turn what you've already built into context
Your team has been building queries, notebooks, and logic for years. That work is the raw material for context. Take those components and codify them into something agents can rely on.
2. Curate, don't lock down
Context curation is not semantic modeling. You're not trying to anticipate every possible question and hardcode the answer. You're giving agents the knowledge and guardrails they need to figure it out themselves. It's a fundamentally different approach — and it scales way better.
3. Roll out self-serve when you're ready
Once your context is solid, you can actually trust a conversational interface. Without it, you're just letting ChatGPT hallucinate answers that
sound
right but use the wrong metrics.
4. Use a hybrid architecture
The semantic layer isn't the only path to great context. Some questions need tight governance — your revenue metric should always be calculated the same way. For that, you want something deterministic like a semantic model.
Other questions are exploratory. Someone's poking around, trying to understand a new dataset, asking something you didn't anticipate. For that, you want looser guidance — rules files and metadata that help the agent navigate without locking it into a single path.
The best systems use both. Strict where it matters, flexible where it doesn't.
You don't need to build the whole thing overnight. Some changes take an hour and dramatically improve agent behavior, others are longer-term initiatives that you iterate on over time. Start small, add layers as you go.
Four tools to steer your agents
In Hex, we use four different types of context, and they each play a different role.
Warehouse metadata
This is the baseline and refers to column names, table descriptions, dbt docs — everything that already exists in your warehouse (if you're using dbt Cloud, you can pull this in automatically). It's helpful, but it's not enough on its own. Agents making best guesses based on column names alone will get things wrong.
Endorsements
This Hex specific feature lets you highlight what matters. With
endorsements
, you're telling the agent which tables are the source of truth, which ones to favor, and which ones to ignore. It's a simple way to steer behavior without writing a ton of rules.
Most data teams could sit in a circle, determine a few tables to endorse, add descriptions for those tables, and get it all done in an hour. With just that, agent behavior radically improves.
Rules files
Rules files provide freeform guidance. They are plain text instructions about anything: your coding preferences, how your business is structured, how your warehouse is organized. Using a Medallion architecture? Want the agent to always use the reporting layer for certain queries? Want time series visualized as line charts? Just write it down.
Semantic models
These are the most structured options. YAML definitions of your metrics, dimensions, join logic — all the stuff that needs to be deterministic. When the agent uses a semantic model, it's calling a tool that generates the correct SQL, every time.
Start with your North Star metrics — ARR, customer churn, pipeline velocity. Use Hex's modeling workbench to convert validated SQL into reusable semantic models.
Hex agents consume all of this. You get to control how tightly they stick to the rules depending on the situation. Sometimes you want exploratory queries. Sometimes you need to guarantee consistency. The architecture adapts.
From vicious to virtuous
Most data teams are stuck in a cycle that feels broken. Business users ask questions. Data teams answer them. New questions emerge. Repeat forever.
The problem isn't the cycle itself — it's that every new question starts from scratch. There's no compounding. No learning. Just an endless queue of requests that never seems to get shorter.
When you implement context engineering, the cycle transforms:
The data team curates context as they work.
Every analysis, every metric, every notebook becomes part of a trusted knowledge base. That work doesn't disappear into Slack threads or forgotten dashboards. It compounds.
Business users can self-serve with confidence.
They're not guessing. They're not bothering the data team with questions that have already been answered. They're using the same trusted logic the data team built, through a conversational interface that actually works.
Novel questions surface naturally.
When someone asks something new in Threads, the agent takes a shot at it. The data team reviews the logic, validates it, and decides if it's worth promoting into governed context. If it is, that one-off question becomes reusable for everyone.
The cycle gets faster and smarter.
Context builds over time. Answers get better. The data team spends less time on repetitive requests and more time on the strategic work that actually matters.
This is the virtuous cycle. It's not about eliminating handoffs between data teams and business users — it's about making those handoffs compound in value instead of starting from zero every time.
Choose progress over perfection when it comes to context
Perfect is the enemy of good when it comes to context curation. Your goal isn't comprehensive coverage but progressive improvement.
You can spend the next hour identifying and endorsing your golden tables. Tomorrow, add rich descriptions to their key columns. By the end of the week, draft your first rules file capturing the tribal knowledge your analysts carry.
Each piece of context makes your AI more reliable, your users more confident, and your data team more strategic.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
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
