---
title: "Magic, for everyone | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/magic-public-beta/"
scraped: "2026-05-10T01:27:13.816568+00:00"
lastmod: "2023-05-04"
type: "sitemap"
---

# Magic, for everyone | Hex 

**Source**: [https://hex.tech/blog/magic-public-beta/](https://hex.tech/blog/magic-public-beta/)

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
Magic, for everyone
Powerful AI assist for data, now in Public Beta
Bryan Bischof
Data
May 4, 2023
Share:
twitter
linkedin
The Hex team is excited to announce that our
Magic AI-assist tools are now available in Public Beta.
This brings access to tools for generating, editing, debugging, and documenting SQL and Python to thousands of you, right from where you’re already working:
Starting now, anyone on Pro, Teams, or Enterprise plans can turn on Magic by flipping the switch on their settings page. If you’re not using Hex yet, you can start up a trial
here
.
Still a beta!
Before we dive into some more details, a big
thank you
to everyone who participated in our Private Beta these past 10 weeks. Your feedback (and patience!) were essential in getting Magic ready for everyone else.
While we’re excited to expand access,
Magic features should still be treated as beta
. Like any AI system, it isn’t perfect, and will make significant errors. You should plan to carefully review generated code, and
treat Magic as an accelerant – not a replacement – for human judgement.
New features and improvements
Since the launch of our Private Beta in February, our circle of magicians have been hard at work, tackling some major infrastructure improvements and adding new powers.
First, we
upgraded the underlying models and prompt strategies.
Magic now uses GPT-4 for most tasks, which, along with significant updates to our prompting, is creating better completions, with much lower rates of errors or hallucination (again, though: still not perfect!)
Second, Magic can
stream responses
. This is a huge improvement for longer-running completions, allowing you to start code review during generation, and ensure they’re useful responses (and cancel if not).
Third, we added a couple small improvements to continue to make Hex feel more magical.
Magic CTE Explode
takes big nested queries and breaks them up into little, bite-size bits which utilize
Chained SQL cells
.
Magic Cell Title
is fun too.
You can see all of these in action below, or
visit the documentation
for a complete list of tips, tricks, and examples of using Magic:
Magic autogenerating a query with semantic understanding of the data
Magic exploding a CTE query into chained SQL cells
We’re hard at work making more improvements to Magic, focusing on continuing to make code completions more reliable and accurate. We are also practicing some new, powerful spells (including some from the
Restricted Section
) that we can’t wait to show you soon!
Magic is still free to use while in Beta
, so we can maximize access (and have some time to think about how pricing should work). Of course, we’ll be in touch before we make any changes on this front.
Privacy and security are always our top priority
Data security is our top priority, and of course we realize that many people have legitimate concerns about privacy while using AI. A few notes and reminders on that front:
Hex doesn’t – and doesn’t allow any third-party partners – to train models using customer data, reducing risk of IP leakage through passed context. This means a model won’t spit out your code to someone else (or vice-versa).
Hex doesn’t send underlying customer data to the models. This means that values of specific rows of a table aren’t at risk of leakage through Magic.
Hex
does use
schema information and project code as model context. This means that any sensitive information in your table or column names, or in your code, could be passed to a model.
Magic is built on Hex’s existing, secure data platform, and is protected by the same practices and policies, including SOC 2 Type II, bug bounty programs, and principles of least-access.
We’re also going to hold off on rolling this out to EU or HIPAA stacks until we have a chance to work with those customers on some specific considerations.
We’d encourage folks with any questions to check out our documentation on
data privacy
for Magic or
reach out
directly.
We also know some teams might not be there yet in terms of adopting AI for their workflows, so we have added an option for account administrators to opt-out of Magic for members of their organization in the settings page.
Magicians wanted!
We’re growing the Magic team, and are
looking for talented AI engineers
to come build with us.
Candidates should have deep experience in AI, with an interest in how data analytics workflows can be changed for the better. Our team is small, focused, and fast-paced (Magic has been just 2 engineers to-date).
If this sounds like an opportunity for you to do your best work, please
check out the job post and get in touch
.
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
