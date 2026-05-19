---
title: "Your code knows things your warehouse doesn't"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/repos-as-agent-context/"
scraped: "2026-05-16T06:00:23.017103+00:00"
lastmod: "2026-05-15"
type: "sitemap"
---

# Your code knows things your warehouse doesn't

**Source**: [https://hex.tech/blog/repos-as-agent-context/](https://hex.tech/blog/repos-as-agent-context/)

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
Your code knows things your warehouse doesn't
Expand the agent's context with your repos and unlock answers only engineers had before
Andrew Lee
Data teams
Product
May 15, 2026
Share:
twitter
linkedin
In this article
Use case: dbt repos
Use Case: application repos
Context that compounds
Get started for free
tl;dr:
Connect your Git repos to Hex and the agent will use them to understand the logic behind your data — not just what's in it.
Data teams spend a lot of their time making data easy to understand, easy to query, and ergonomic. A good data mart is a high-leverage tool — blessed, safe to use, hard to get wrong with good abstractions, good names, helpful documentation.
Until someone asks a question that requires understanding
how
the data was built, not just what it contains.
What values are getting filtered out here?
What does this column actually mean?
How was this feature implemented?
These questions are impossible to answer without knowing how the data came to be. The answers live in your dbt models, your app code, your transformation logic — scattered across repos that, until now, had no connection to where your data work actually happened.
Today, that changes. You can now attach one or many repos to your Hex workspace, and the Hex Agent will analyze, parse, and synthesize them. Now anyone can understand not just what the data says, but how it got there.
Use case: dbt repos
Even with a great data mart and extensive documentation for each column and table, there is inherently a lot of valuable nuance in the upstream logic that traditionally only the data team could figure out and answer.
Simply connect your dbt repo to Hex, and even with your self-service users still querying high level tables, the agent will be able to better construct queries and understand limitations of the mart tables by crawling up and inspecting upstream logic.
What values are getting filtered out
Are there blanket cases we exclude
what values are getting collapsed and simplified in which
Where are these categories coming from?
Self-service users keep querying the high-level tables they already know. The agent handles the rest.
The Hex agent has significantly increased my ability to tackle 'nebulous' queries — those complex requests where documentation is sparse and the correct approach feels ambiguous. By explicitly leveraging our repository and workspace guides as context, we can now navigate this ambiguous data with much more confidence.
Camden Willeford
— Engineering Manager, Underdog
Use Case: application repos
Many self-service data workflows begin with a dbt repo — but they struggle when a question requires combining data context with an understanding of how the product actually works.
How did we implement tracking?
What
isn’t
being tracked?
What set of events should be analyzed together and how do they relate in a feature?
Connect your application repo and the agent can reason its way through your codebase to answer those questions directly. Combined with your data transformation repo, this gives the Hex Agent an incredible depth of context on how to analyze your company's data.
Our product managers actually ask a shocking number of questions about data lineage that, before, only the data team could answer. After connecting our repos to Hex, these users can self-serve answer these questions.
Alan Peters
— Analytics Engineer, Stubhub
Context that compounds
A large part of how your business views the world is already explicitly written as code. And that logic is constantly evolving, just like the data it produces.
You need an agent that can bring together context from multiple sources — repos, existing projects, warehouse metadata, guides, semantic models — synthesize it, and intelligently draw from the right sources to answer the right question. In Hex, simply connecting your repos gives you exactly that.
Your business, your code, and your data are constantly changing.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
More on Data teams
BLOG
Context Exhaust
Barry McCardel
·
April 28, 2026
The best AI context isn't typed into a doc — it's the exhaust from how you already work. Here's how that exhaust compounds into a smarter system.
BLOG
Introducing Context Suggestions
Andrew Lee
·
April 23, 2026
Hex's new Context Suggestions automatically learn from every Thread, turning user conversations and agent analyses into smarter, compounding data context.
BLOG
Introducing Context Studio
Andrew Lee
·
January 28, 2026
Context Studio gives data teams the tools to observe, test, and deploy AI analytics agents — ensuring users get trustworthy answers they can rely on
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
