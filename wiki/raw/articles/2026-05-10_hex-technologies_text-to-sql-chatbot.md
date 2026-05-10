---
title: "Building a Text-to-SQL Chatbot | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/text-to-sql-chatbot/"
scraped: "2026-05-10T01:29:54.324385+00:00"
lastmod: "2023-09-20"
type: "sitemap"
---

# Building a Text-to-SQL Chatbot | Hex 

**Source**: [https://hex.tech/blog/text-to-sql-chatbot/](https://hex.tech/blog/text-to-sql-chatbot/)

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
Building a Text-to-SQL Chatbot
How to use Hex, LangChain, and OpenAI to use natural language to query your database
Jordan East
Data
September 20, 2023
Share:
twitter
linkedin
In this article
Embarking on an AI Journey
Using LangChain with OpenAI
Seamless Integration with Hex
Looking Forward: Expanding Functionality
Get started for free
This is a summary of a Select session that was presented live on September 19, 2023.
Have you wondered how the latest AI technologies could improve your data team’s productivity? Can large language models (
LLMs
) improve the efficiency of your data-driven projects?  Is it possible for natural language processing to bridge the accessibility gap, allowing colleagues throughout your organization to effortlessly engage with your data efforts?
These are some of the questions I set out to understand while experimenting with new AI tools and tech.
Embarking on an AI Journey
As I haven't spent a ton of time using python to build front end applications (mostly just data analysis work using pandas) I set out to use
ChatGPT
as a coding assistant to help build a text to SQL chatbot application. While ChatGPT was helpful, the 2021 knowledge cutoff proved a blocker as it wasn't aware of many of the new AI frameworks available to build these types of applications (like
LangChain
). So I began building a very simplistic bot, and I found that I needed to hardcode repeatedly to get the desired results. As I ran into new issues I continued to create more and more functions to deal with these scenarios and soon my code was bloated and slow. But it worked!
While I know we don't have this limitation anymore, at the time I was limited to 25 messages per 3 hours to ChatGPT. So on one forced break, I decided to spend the timeout reading some documentation of a new framework I kept hearing about called LangChain. I figured there had to be a way to approach this project in a cleaner way, and maybe leverage some libraries or frameworks instead of trying to handle every part with custom functions.
Using LangChain with OpenAI
Within 10 minutes of reading
LangChain documentation
I had enough to get started. I threw together parts of what I had already built, including connecting to and defining the database/schema/ tables I wanted to work with into some LangChain code. To my very pleasant surprise, with just 20 lines of code I had a much better, faster, and accurate text to SQL chatbot working.
This V2 chatbot built with LangChain demonstrated a strong ability to process user queries. It also did well understanding which tables it needed to join to answer certain questions. While it wasn't perfect, it provided me with a much more advanced starting point for this project and guided the way I approached building apps with LLMs.
Seamless Integration with Hex
Since I was already familiar with Hex and its user facing applications capabilities, I decided to build the front end of the app using a mix of Hex features.
Start with the template here:
Text to SQL Chatbot Template
I leveraged input parameters, parameterized SQL queries and SQL table display cells. This allowed the end user to navigate directly to the data they wanted to ask questions against, and explore and see samples of that data to better inform the questions they wanted to ask of it. I used variables from the user dropdown selections to send context to the LangChain and OpenAI functions about what database and schema the user was asking against.
Looking Forward: Expanding Functionality
This initial POC was just the beginning. We’ve built on this foundation in a number of ways, including materially enhancing bot accuracy by:
Providing even more context in the prompt, and using more variables that are derived by user selections.
Allowing a user to select a single table or an entire schema to ask questions against.
Sending column names, column descriptions, column data types, and table descriptions as part of an initial custom prompt.
All of this is dynamic based on user selections, drastically improving the accuracy of the bot.  With increased accuracy comes more potential use cases.  We’ve started using
LangSmith
, another LangChain product, to trace the prompts and calls that are sent to
OpenAI
and adjust, tweak and quickly understand the impact of the changes we made to our prompt. Looking forward, we want to incorporate memory and chat-like features, but are aware of rate limit issues (OpenAI tokens) with our ever growing prompt.
Overall this has been a great learning experience into Hex, OpenAI, and LangChain.  We continue to build upon and experiment with these technologies in relation to adding business value here at
Workrise
.
Ready to start building your own chatbot?  Start a
free 14-day Hex trial
today.
Share:
twitter
linkedin
Here at Hex, we're creating a a collaborative notebook that makes it easy to build and share beautiful interactive data visualizations.
✨ Get started for free
🕵️ Learn more
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
