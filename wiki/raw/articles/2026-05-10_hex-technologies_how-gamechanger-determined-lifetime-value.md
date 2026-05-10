---
title: "How GameChanger used LTV modeling to predict and prevent churn | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/how-gamechanger-determined-lifetime-value/"
scraped: "2026-05-10T01:29:40.158954+00:00"
lastmod: "2024-09-12"
type: "sitemap"
---

# How GameChanger used LTV modeling to predict and prevent churn | Hex 

**Source**: [https://hex.tech/blog/how-gamechanger-determined-lifetime-value/](https://hex.tech/blog/how-gamechanger-determined-lifetime-value/)

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
How GameChanger used LTV modeling to predict and prevent churn
LTV clarified the "what" and "why" questions about churn
Nick Moore and Jessica Schimm
Data teams
September 12, 2024
Share:
twitter
linkedin
In this article
Redefining lifetime value (LTV)
Getting new LTV metrics ready to share with the company
LTV clarified the "what" and "why" behind churn
How the data team is supporting the company with LTV
Get started for free
You might be familiar with the nation-wide franchise Dick's Sporting Goods, but unless you have kids in youth sports, you might not know about
GameChanger
, its popular and family-loved app.
The app lets families and friends watch their favorite youth team players during live games and gives access to highlights and game archives while also helping coaches keep score and set lineups.
With GameChanger's array of users — paid and free with seasonal gains and drop offs — they needed a clear lifetime value metric at the user level (some companies just do this at the business level).
This would let marketing, finance, and product create more efficient action plans and strategy and also clarify predictions of churn due to seasonal fluctuations. The data team set out to create a clear understanding of the monetary value that users provided for GameChanger and how it would change over time.
knowledge
Watch the full GameChanger story in
our Select Session
.
Redefining lifetime value (LTV)
To do the research to support this work, the data team spun up
a Hex notebook
which gave them a collaborative environment to do all the data preparation and
exploration
. Then it was time to explore
LTV
.
In its simplest form, LTV has two components:
“Lifetime” which measures a subscriber’s time to churn
“Value” which measures a user’s monthly value in dollars (e.g., if a user stays on the app for 10 months, how much money does that translate to?).
LTV is the result of multiplying these two numbers together.
They looked at LTV of paid users first (knowing they could build upon that formula for free users).
To get the “Lifetime” of a paid user, they used survival regression to estimate a subscriber’s time-to-churn.
To get the “Value” of a paid user, they used the metric average revenue per user (ARPU), which changes based on which of the four different subscription plans a user is on.
knowledge
LTV of free and paid users
Since the app has both free and paid user plans, a LTV metric that only focuses on paid users or subscription dollars misses the value that free users provide via advertising dollars. Not only does this leave a gap in understanding the monetary contribution of all users, but it also means their team was unequipped to see when and how free users could convert into paid ones.
In order to build LTV accurately of free users, they modeled not just their advertising potential, but their likelihood of them eventually subscribing. The data team could then use that complete view and then bring it together with paid user LTV to model growth that is based on all users.
Modeling Lifetime and Value in Hex
They pulled data from Snowflake to have two different models run on lifetime and value metrics in Hex, which then dumped the results of those back into Snowflake. Hex’s
multimodal workflow
made it easy to keep the MRR work in SQL, and the Lifetime metric work in Python and SQL, all in the same place.
Hex made it easy to keep the MRR work in SQL, and the Lifetime metric work in Python and SQL.
Getting new LTV metrics ready to share with the company
With the lifetime and value components established, the data team used Hex to port the insights they were producing into Snowflake. Data engineers then took the data from Snowflake, modeled it in dbt, and exposed the data to end-users. They were able to automate much of the work by using Hex’s built-in scheduler to schedule weekly data dumps from Hex Notebooks into to Snowflake.
Before sending out their new metrics, the data team looked at general accuracy metrics to gauge log likelihood and concordance. “Those have to look good to train the model and they did,” Nihal said. For even more confidence, the data ran the workflow weekly for a month and then compared it to actual churn results. “We were happy with the outcome.”
LTV clarified the "what" and "why" behind churn
The insights from Hex were ported into their BI tool, where business teams could answer "the what" questions of churn. They could see trends of LTV across different user segments like and understand the current state: How has churn changed over the last two quarters? What’s the average LTV of a subscriber?
The product, marketing, and finance teams all began using LTV as an essential, instrumental metric for generating better forecasts and strategy.
The product team uses LTV to more deeply understand specific user segments
The marketing team uses LTV to analyze paid media performance by marketing channel
The finance team uses LTV (among other metrics) to improve financial revenue forecasting
In Hex, they were able to dig into the "the why" questions behind churn. It was key for model explainability where the data team could see: What are the most important features within your ML model that are affecting churn? Are there any interactions between various features usage and order of usage that impact churn?
The LTV model could also be used to do revenue forecasting. “All we had to do was bring in a new model to answer our new subscriber growth and forecast questions,” Nihal said.
That model played a key role in validating the opportunity and helped scale the Ads business to over $2M in revenue its first year.
Nihal RP
— Senior ML Engineer, GameChanger
How the data team is supporting the company with LTV
The behavioral dynamics of GameChanger’s users are sometimes hard to parse and predict because the company has free and paid features, numerous subscriber plans, and multiple predictors of when a user might upgrade or churn. But through experimentation, accuracy checking and models that check themselves, GameChanger is able to have a much clearer picture of growth.
Without the results of this work, GameChanger would have been left with a shallow view of its user base. The behavioral dynamics of user types would have been inscrutable at a granular level, and other teams would have struggled to predict churn or improve conversion rates.
Now, GameChanger has a better understanding of LTV and can offer sophisticated prediction models that use LTV to predict churn. From the data team to the finance and marketing teams — the family-loved app is now much better equipped to build and maintain a more reliable, more predictable business.
knowledge
For the full behind-the-scenes workflow,
watch the GameChanger Select Session
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
