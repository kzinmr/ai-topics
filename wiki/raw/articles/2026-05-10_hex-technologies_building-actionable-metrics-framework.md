---
title: "Building Metrics Stakeholders Need: An Analyst's Guide | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/building-actionable-metrics-framework/"
scraped: "2026-05-10T01:29:48.134837+00:00"
lastmod: "2025-09-18"
type: "sitemap"
---

# Building Metrics Stakeholders Need: An Analyst's Guide | Hex 

**Source**: [https://hex.tech/blog/building-actionable-metrics-framework/](https://hex.tech/blog/building-actionable-metrics-framework/)

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
Building metrics stakeholders need, not what they want
Sometimes the best thing you can build is something you don’t have to
Caleb Bowie
Data teams
September 18, 2025
Share:
twitter
linkedin
In this article
Why it's important to stop and understand the "why"
3 Tactics to truly get 'under the hood' of a metric
Get started for free
Recently, our Head of Customer came to me with what seemed like a gift: a detailed request for a new metric called 'workspace freshness'. This metric was going to be one of the components of our customer health framework. They had done their homework, knew exactly what they wanted and even had a timeline. It felt like starting on second base.
But here is what I have learned as an analyst: even when things seem really cut and dry, it's important to stop and understand the "why?" Let's dive in.
Why it's important to stop and understand the "why"
Saying yes without understanding the underlying need is how we end up building metrics that don't actually drive decisions. When we build metrics that miss the mark, we're not just wasting time, we're potentially misleading decisions and eroding trust in our data.
Building exactly what your stakeholders want may seem like the right thing to do, but it's important to remember that we have guardrails to consider that come from sitting on the other side of the table. As analysts, we need to recognize that in our world, every "yes" is a "no" to something else. Before jumping into any project, we need to consider: Do we have the bandwidth? How much time do we have to execute? What other projects are we saying "no" to?
New metrics often mean a bigger time investment than stakeholders realize. We might need to capture new data, validate that data's accuracy, and spend significant time on change management and socializing new definitions. For this customer health score project specifically, all of these factors were in play.  And to add more urgency to this particular situation, our existing customer health score was being calculated by a tool we were moving away from at the end of the month.
This is why the most valuable thing we can do as analysts isn't just building what stakeholders ask for, it's translating what they need into data that actually solves their problems. So how do we actually do this translation work in practice?
3 Tactics to truly get 'under the hood' of a metric
Here are three approaches that helped me navigate from the initial request to an actionable metric.
1. Ask exploratory questions to understand the shape of the metric
Digging past the metric name and testing your understanding by reading back to the stakeholder is essential. As I have mentioned many times by now, it's important to understand "why" — to not just accept the metric name at face value as your explanation of what the metric is trying to solve for.
You need to dig into the intended behavior of the metric, understand how it will be used by stakeholders, and understand what a "bad" version of this metric might look like.
For example, I asked the questions:
"What makes a workspace fresh?"
"What makes a workspace stale?"
"If you had to describe workspace freshness in natural language, what would you say?"
I pushed on these questions, spending time trying to ensure I understood the spirit of each of these questions. I then read back my understanding to the stakeholder:
"A customer with a fresh workspace is a customer whose users are continuing to make new content in our product?"
That became our thesis for the metric. This step is critical because it's where you find out if your translation actually captured their intent. Don't skip the confirmation — stakeholders will tell you if you got it wrong.
2. Gathering real-life examples
Asking stakeholders to share examples that capture the spirit of your metrics can be a huge advantage. I like to lean on stakeholders and SMEs to help gather these examples.
For this project, I worked with our customer engineers to find good examples of customers in their book of business that represent different ends of the freshness spectrum. They work really closely with our customers, so they helped me identify customers who they know have a strong core of users making projects in their workspace, and a few customers who they may be concerned about their level of adoption.
This helps the process in multiple ways:
provides real-life examples for you to use during validation
helps ensure what you build captures the spirit of your stakeholders' goals
gets the consumers of the data in on the building process and helps build buy-in
3. Look for existing solutions that may solve your problem
Now that I have a deeper understanding of what the stakeholder is trying to achieve, I look for existing solutions to similar problems. Because of the factors I mentioned earlier — resource constraints and a tight timeline — it's important to explore what already exists.
In our case, I discovered that our product team was already tracking engagement metrics that captured similar behaviors to what our stakeholders were trying to measure. Our product team had already done the heavy lifting. They’d mapped event tracking into
workflows
— groups of customer activities tied to specific use cases.
Two of these workflows,
Project Creation
and
Curation
, lined up almost perfectly with what the customer team was hoping to measure with “workspace freshness.” In other words, we already had a way to see when users were continuing to make new content in the product.
Instead of inventing a brand-new metric, we built on those existing engagement thresholds. That gave us a clear benchmark for what “good” adoption looked like, saved development time, and kept our metrics aligned with how the product team was already thinking about user behavior. It also meant that we had another resource in the organization that already understands the data and can aid in any questions the customer team may have.
Investigating to solve more
By taking time to translate "workspace freshness" into clear behavioral definitions, we didn't just build a new metric — we created a customer health framework that actually changed how our team prioritizes accounts. The metrics that we ultimately built sounded nothing like the original request, but they solved the underlying business problem.
This isn't just about metrics. It's about our role as analysts. We're not just data builders; we're translators between business intuition and measurable reality. When stakeholders come to us with solutions, our job is to help them discover the problems they're really trying to solve.
The next time someone hands you the "perfect" metric request, resist the urge to start building immediately. Instead, start translating. Ask why. Gather examples. Look for existing solutions. After all, our job isn't to be order-takers for analytics requests — it's to be translators helping organizations understand themselves through data. And that translation work? That's where the real value lives.
Share:
twitter
linkedin
New to Hex and want to try agentic analytics?
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
