---
title: "hex cortex overview, all your questions answered | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/hex-cortex-recap/"
scraped: "2026-05-10T01:28:50.928795+00:00"
lastmod: "2025-01-30"
type: "sitemap"
---

# hex cortex overview, all your questions answered | Hex 

**Source**: [https://hex.tech/blog/hex-cortex-recap/](https://hex.tech/blog/hex-cortex-recap/)

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
How to Hex: Snowflake Cortex Recap
Highlighted questions and answers from the How to Hex session on Snowflake Cortex
Armin Efendic
Product
January 30, 2025
Share:
twitter
linkedin
We recently hosted a How to Hex session focused on Snowflake
Cortex, offering a high-level overview of its powerful features—with a special deep dive into Cortex LLM Functions.
In this session, we explored a project that used Cortex in SQL and Python to extract meaningful insights, such as classifying product recalls and determining the total number of units impacted. You can also browse the
complete Hex project
.
Below, you’ll find answers to all the questions we received—and there were some great ones!
Q: What are the advantages of using Snowpark and Cortex on Hex as opposed to just using Snowflake SQL, Python, and Cortex?
Answer: Hex offers a
Snowpark “Easy Button”
that instantly creates a Snowpark session using your existing Snowflake connection—no need to expose credentials, manage keys, or use hidden files. It’s a secure, shareable setup.
Snowpark dataframes also work seamlessly in Hex’s native SQL cells, with syntax highlighting and auto-formatting. Plus, Hex visualizations are Snowpark-aware, generating efficient queries under the hood that bring only the necessary data to Hex for visualization. The aggregation are handled by the Snowflake warehouse—perfect for working with billions of rows.
Need a boost? Hex Magic can help debug or write Snowpark code, making it easy to get started or level up your workflow!
Q: Can we swap this to OpenAI with an api key [when using Cortex complete()]?
Answer: No. Cortex LLM Functions are managed functions provided by Snowflake. The models that are available can be found
here
. Snowflake is constantly working on providing more and more models. Check out
Sridhar Ramaswamy (Snowflake CEO) talking about DeepSeek
.
Q: Any steps to evaluate which model suits the most?
Answer: Yes! Start with the largest model for prototyping and use it as your benchmark. For example, if extracting numbers from text, measure how often a number is extracted and how accurately it does so. Use a diverse random sample to assess accuracy.
Q: What are the main considerations when using these Cortex functions?
Answer:
Check Model availability
Enable cross-region inference as needed
Cost - see the
Pricing → Consumption Table
For productionalized pipelines, consider fine-tuning a smaller model for cost savings without sacrificing performance.
Context window
The amount of tokens you send per request could limit some models from your selection
Q: Can we fine-tune a Cortex model and save/deploy it using Snowflake Registry?
Answer: No. The model registry
accepts machine learning models
. You would not run a
.predict()
on the fine-tuned model. Rather, you would utilize the
complete()
function and pass it your fine-tuned model.
Q: How was the count of companies extracted since there were millions of rows that needed to be evaluated?
Answer: Hex can leverage “pushdown” compute. Meaning, we can utilize the warehouse to process large amounts of data and only bring in a preview or the required data into Hex memory. This can be handled automatically or controlled by the user depending on the use case.
Q: Is an alternative [to Cortex] making API calls out to something like OpenAI?
Answer: Yes, you can call the OpenAI endpoint from Hex using your private key for authentication.
However, there’s no built-in function that integrates directly with SQL or Python. Instead, you’ll need to use Python to loop through each row of data when sending requests to OpenAI. Additionally, since the model isn’t hosted in Snowflake, be sure to consider your organization’s security requirements.
Q: Using containerization in Snowflake & open source models, can you leverage the LLM in these Cortex functions in SQL?
Answer: Yes and No.
Yes, you can run open source models in a Snowpark Container Service. Check out
Running DeepSeek-R1 in Snowpark Container Services: A Complete Guide
for more information.
No, you can not call this model use the
complete()
function in SQL or Python. You call the model with an endpoint. In the example above, OpenAI’s completions endpoint is used with
localhost
pointing to the DeepSeek model.
If you have any questions about Hex or Snowflake Cortex, feel free to connect with me on LinkedIn -
Armin Efendic
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
More on Product
BLOG
Announcing: Magic support for Claude on Snowflake Cortex
Barry McCardel
·
November 20, 2024
Announcing: Magic support for Claude on Snowflake Cortex
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
