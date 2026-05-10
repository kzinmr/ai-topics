---
title: "Automating Reporting at Algolia | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/automating-reporting-at-algolia/"
scraped: "2026-05-10T01:28:51.036519+00:00"
lastmod: "2023-09-01"
type: "sitemap"
---

# Automating Reporting at Algolia | Hex 

**Source**: [https://hex.tech/blog/automating-reporting-at-algolia/](https://hex.tech/blog/automating-reporting-at-algolia/)

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
Automating Reporting at Algolia
How one data team transformed tedious, manual reporting tasks into seamless, automated workflows
Matthew David
Data teams
September 1, 2023
Share:
twitter
linkedin
In this article
From Manual to Magical: Previous vs. Current State
Accelerating Insights
Get started for free
This is a summary of a
Select session that was presented live on August 10, 2023
.
Algolia, like at many other companies, holds quarterly reviews which have many charts and graphs representing what's been going on in the business. Each quarter they would spend a couple weeks regenerating and updating each one of these visualizations. This was time intensive and often stakeholders wanted the data refreshed before and after the meeting leading to more rounds of updating by the data team.
They needed a process to transform tedious manual tasks into a seamless, automated workflow. Here’s how they automated quarterly reviews at Algolia.
From Manual to Magical: Previous vs. Current State
In the past, the quarterly review process was a manual ordeal.  The data team downloaded CSV files from Salesforce, uploaded them to Google Sheets, modeled the data, created visualizations and painstakingly copied charts to Google Slides.  It was time consuming and prone to errors.
They decided to automate pulling data from Salesforce into Redshift using Fivetran. Once the data was in the warehouse they could use dbt to automate the transformations necessary to prepare the data for analysis. This ensured that their data was both accurate and reliable as a single source of truth. They focused on data quality, business logic and thorough documentation.  All together, this created a solid foundation for automated reporting.
Then the Algolia data team used Hex to automatically query the data from the warehouse and push specific data sets into Google sheets using APIs. Check out this
Hex template to push data into Google sheets
.
With the data in Google Sheets, they could pivot and visualize the data into charts that were copied and pasted into Google Slides. These charts are linked so that if the data changes in Google Sheets you can click
update all
in Google Slides to refresh all the charts in your deck, with the push of just one button.
Algolia diagram - quarterly report automation
When this initiative began, Algolia had two goals: to use curated data and to drive data automation across the organization. The breakthrough came when they introduced Hex and dbt into the mix. They started automating data retrieval, transformation, and visualization. They were able to establish an automated connection between data sources and Google Sheets which eliminated the need for manual intervention. Charts in the quarterly review deck could now be updated with a click, saving valuable time while also reducing errors.
Accelerating Insights
The introduction of automation was game-changing. What used to take two weeks to complete is now finished in just 5-10 minutes. Executives now have access to trusted, automated data that they can rely on for accurate insights, anytime. This newfound reliability has prompted the Algolia team to extend automation to other teams with routine reporting needs. And now they re-allocate the time spent on administrative tasks, like copying and pasting data, to more strategic projects.
Algolia relies on data to make smart decisions about the business, so automation is key.  The journey to automating quarterly reviews transformed their process from manual drudgery to efficient, data-driven insights. By automating, they saved time, improved the accuracy of their work and empowered the team to focus on more strategic tasks. With Hex, dbt, Redshift and Google Slides, they created a seamless and efficient reporting process that brings new levels of efficiency to the team.
Are you interested in automating your reporting process?
Watch the original recording
that this post is based upon or
ask Hex to show you
a demo.
Share:
twitter
linkedin
Want to see this project in action? Check out this sample project in the use case gallery. Copy it to your workspace to try it yourself.
✨ Get started for free
📊 Copy the free template
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
