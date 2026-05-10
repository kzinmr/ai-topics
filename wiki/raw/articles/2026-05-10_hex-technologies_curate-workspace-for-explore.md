---
title: "How to curate your Hex Workspace so business partners can answer their questions | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/curate-workspace-for-explore/"
scraped: "2026-05-10T01:29:59.848765+00:00"
lastmod: "2024-11-21"
type: "sitemap"
---

# How to curate your Hex Workspace so business partners can answer their questions | Hex 

**Source**: [https://hex.tech/blog/curate-workspace-for-explore/](https://hex.tech/blog/curate-workspace-for-explore/)

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
Curate your Hex Workspace for a better Explore experience
Curating your data for Explore makes everyone more productive
Olivia Koshy
Product
November 21, 2024
Share:
twitter
linkedin
In this article
Curation at the warehouse level for better Explore experiences
Taking time to create a great Explore experience makes everyone more productive
Get started for free
Last updated: March 5, 2025
More and more people outside of the data team — from product, finance, ops, and marketing — are relying on Hex to get clearer and more specific answers on what’s happening in their world. This is exciting! It means data teams are producing powerful work in Hex that business partners want to dive into further.
We wanted these business partners (and data team members, too!) to have a first-class experience working with data in a way that didn’t require code. So we built a new no-code experience, called
Explore
. It lets business partners get their hands on warehouse data and semantic models directly using visual data exploration to answer their follow-up questions in Hex. No waiting on the data team or learning code.
If your business users are already using Hex or you have a hunch they’ll start to soon, we recommend doing a bit of curation at the data warehouse level, as well as creating semantic models via
Semantic Model Sync
. This will ensure that the data they explore and summon with
Magic
can be trusted and is relevant to them.
Curation at the warehouse level for better Explore experiences
To start this process, head over to the
Data browser
and complete the following steps.
1. Create a data connection that’s dedicated to non-data team users
Chances are your business users don't need to wade through every nook and cranny of your data warehouse (cough, cough, looking at you… dev_user_42_test_table 👀). To give them access to the data only they need, set up
a new data connection
to house just the right databases, schemas, and tables that are relevant to them. Not only will your stakeholders feel right at home, but Magic will also serve up data insights tailored just for them. From there you can curate relevant data.
knowledge
Data connection tips:
Use a clear, consistent, and descriptive name for your connection to make it easily identifiable to team members
Clearly document the purpose of this data connection, its internal owner, and notes about special configurations or limitations.
2. Within that connection, identify the tables and semantic datasets that business partners can trust
Business users want data that can give them trustworthy information, so it’s best to prune anything that could be inaccurate, not up-to-date, sensitive or just too raw. Think of this connection as the “Gold layer” from
Databricks’ medallion architecture concept
— ”organized in consumption-ready, project-specific databases.”
To create a smooth Explore experience, there are three ways to curate what data is surfaced in your data connection.
Schema filtering (in the Data browser)
Using the
Data browser
, admins can
easily use
schema filtering
to include or exclude specific databases, schemas, or tables from your data connection. On the refresh, only your selected assets will be synced. We recommend filtering out STAGING/DEV/RAW schemas to start. Any excluded objects can still be queried, they just won’t appear in the data browser, autocomplete, or Magic AI responses. To fully remove access to certain objects, you’ll want to set up role permissions in the actual warehouse.
Magic - Include/Exclude toggles and Endorsements (in the Data browser)
Think of Magic AI like a data exploration sidekick — ready to assist any Explore users who might not speak fluent SQL or Python. Adding an
endorsed status
to databases, schemas or tables is the easiest way to quickly tell Magic (and your eager end users) which data is "Approved" or "Trusted" by the data team. And now you can get endorsement suggestions from Magic itself…
*NEW: Magic Curation Suggestions
🪄 Magic will now suggest tables to endorse to Admins! In the Data browser, Magic will automatically surface popular tables and datasets to endorse and you can accept or dismiss suggestions. Magic will then prioritize any endorsed tables when answering questions and generating suggested prompts in Ask Magic. This helps your non-data team users ask the right questions and explore the right data.
If you want to maintain access in the Data browser to certain databases/tables/schemas but never want Magic to use these tables, you can toggle them via “Include/Exclude for Magic” setting.
Warehouse permissioning - (in your data warehouse, not in Hex)
If you don’t want folks in your workspace to be able to access specific tables at all — like ultra sensitive data or raw warehouse data — configure user permissions in your warehouse and your data connection to prevent business partners from querying or viewing the data.
3. Add descriptions to the remaining tables in the connection
Descriptions provide relevant context to both users exploring data and Magic. When anyone asks Magic a question, it first uses the metadata from the Data browser to perform a semantic similarity search for tables and columns that might answer that question. You can add descriptions to any database, schema, or table. The more information you add to the Data browser, the more likely that Magic will be match the right tables and columns.
What should you include in metadata? It’s best to include information about what can be calculated from a table and what it should be used for. If there is company jargon or synonyms, explain what they mean or referring to. Dig into more
metadata tips that are useful for Magic
.
For Magic, here are some tips to reduce any potential string hallucinations:
Add enumerations - For low cardinality string columns that are often filtered on or used in case statements,
try explicitly enumerating or describing options for these fields in the Data Browser (this can reduce hallucination rates down to near 0). This could be useful for a question like: “How many orders have shipped but not yet been delivered?”
Try explaining the pattern in natural language - For high cardinality string columns that have too many options to list but follow a consistent pattern
(like a City / State combo), call out the pattern in natural language like “City State pairs, like 'Memphis TN.’” This can help Magic better understand.
Add custom metadata - Try using natural language to tell Magic when a table should and shouldn’t be referenced.
For example, you could write: “only use this table if the prompt explicitly requires raw stripe data, otherwise use
fct_orders
.”
knowledge
Pro tip:
If you want to prototype descriptions and see how Magic does with them, feel free to directly edit/update them in Hex in our
Data browser UI
! You can then ask Magic your question and see how it does.
4. Hook up your data connection with our dbt integration
If you use dbt Cloud, you can use metadata from your dbt project to enrich the Data browser, making the Explore experience with Magic even more useful. When you use our
dbt integration
with your data connection, Hex will grab metadata, like: model, source, and column descriptions and tests; when the model was last updated; source freshness tests, and more for Magic to reference. Explore users will also be able to see these descriptions in Hex.
5. Add a semantic model
Hex supports importing semantic models from
dbt MetricFlow
,
Snowflake Semantic Views
, and
Cube
to abstract away complexity with predefined metrics. Surfacing these models within the data browser makes self-serve analytics even easier for your business stakeholders. Check out our
docs
and
tutorial video
to get your models imported into Hex.
If you haven't set up a semantic model yet, both dbt MetricFlow and Cube offer free open-source products to author semantic specs—making it easy to get started.
If you're starting from scratch, it's best to start with one use case to help one group of users start answering questions on their own without data team intervention. We recommend taking the following steps:
Choose one team or subset of users as the consumer. For this example, we're using our entire sales team.
Identify the most important questions being asked where self-service could be valuable. For example, sales reps may be regularly inquiring about their pipeline.
Identify a core set of metrics that are required to answer the users' common questions. In this example, this could include open and closed opportunities, stage of opportunity, and expected ARR.
Model these metrics in dbt MetricFlow or Cube. Make sure everything in the model has a description to help users understand what they're working with. (Coming soon, Magic will also leverage these descriptions.)
Once these are modeled, follow the
steps in our docs
to import these models into Hex.
Lastly, add
endorsements
to the most important datasets you've modeled.
To make the most of your semantic models, try building an app using only
Explore cells
in the notebook and your freshly modeled measures, dimensions, and joins. This makes it easier for stakeholders interacting with your data app to answer follow-up questions with new explorations.
Taking time to create a great Explore experience makes everyone more productive
Congrats on making it through our data curation crash course! By carving out just a bit of time to spruce up your Hex workspace, you're giving your stakeholders a reliable and relevant data exploration experience to drive even more value from your data.
Have more questions? Watch our
Magic AI live event
! We’ll go more in-depth on how Explore works with Magic AI and how to set up business users for success!
Share:
twitter
linkedin
Have more questions? Ask our team directly during our Magic AI live event! We’ll go more in-depth on how Explore works with Magic AI and how to set up business users for success!
Sign up
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
