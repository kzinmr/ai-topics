---
title: "How OM1 is advancing healthcare R&D insights with Hex and Snowflake | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/how-om1-is-advancing-healthcare-insights-with-hex-and-snowflake/"
scraped: "2026-05-10T01:29:49.107056+00:00"
lastmod: "2024-07-19"
type: "sitemap"
---

# How OM1 is advancing healthcare R&D insights with Hex and Snowflake | Hex 

**Source**: [https://hex.tech/blog/how-om1-is-advancing-healthcare-insights-with-hex-and-snowflake/](https://hex.tech/blog/how-om1-is-advancing-healthcare-insights-with-hex-and-snowflake/)

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
How OM1 is advancing healthcare R&D insights with Hex and Snowflake
And a flexible self-serve data app
Jessica Schimm
Data teams
July 19, 2024
Share:
twitter
linkedin
OM1’s fragmented, siloed analytics workflow was starting to break down at scale. A simple request from a business user — “How many patients do we have using this new drug?” — would turn into a days-long game of chutes and ladders across multiple teams and multiple tools. After a while, the data team noticed that less and less people were asking questions or requesting updates to reports.
But
OM1
is a
data company
— they provide massive healthcare datasets of anonymized patient data to medical providers and researchers — so becoming less data driven was simply not an option.
Zach Bryant, Associate Director of Data & Analytics, had a bit of a crazy idea: instead of throwing money at the problem by hiring more clinical data engineers, what if they could
turn their existing business users into clinical data engineers?
This is the story of how OM1 used Snowflake and Hex to build a flexible self-serve data app that unified their fragmented workflow and empowered business users to act like data engineers.
🔍 You can check out
their data app
which is open-source and embedded below.
knowledge
Read OM1's case study
Improving patient outcomes with healthcare datasets for clinicians, researchers, and scientists
OM1 provides healthcare datasets of anonymized patient data for scientists, clinicians, and researchers to advance research and precision medicine for chronic diseases. Their research-ready datasets are used to make gains in personalized medicine, evidence generation, and evidence research for immunology, mental health, dermatology, cardiology and more.
Imagine you need to get a knee replacement. Using data from OM1, your doctor can see a comprehensive view of your health and compare it to similar patients to estimate potential outcomes. Maybe they see that, based on your history and data, there is a 60% chance of success with the knee replacement and a 10% risk of severe complications, and walk you through what that means.
Researchers and clinicians can look at that same data to see gaps in patient care, find unmet needs in the healthcare system at large, and identify opportunities for medications to be used in better ways. These insights might even be used to drive new regulations in U.S. healthcare; for example, submitting drugs and devices to the FDA that weren’t able to be done through clinical trials.
The challenges of data management with nation-wide healthcare data
The main thing to know about comprehensive healthcare datasets is that they’re BIG.
To create their research-ready datasets, OM1 collects hundreds of billions of data points from 330 million patient records — relying on healthcare systems, insurers, and other industry partners as sources.
Within all of that data, there are endless combinations of variables that their customers could be interested in. For example, a clinician might want to look at a heart failure dataset and see how many patients have experienced heart failure and are on an anti-coagulant drug and have an underlying condition of PTSD.
The other unique thing about healthcare data is that it’s constantly evolving in structure and scope
; new practice guidelines emerge, new medications are constantly coming out, and new studies with updated trends are published all the time. OM1’s customers — clinicians, scientists, and researchers — need to be nimble and incorporate adjustments to their data as these updates happen to make sure their findings are up-to-date. In turn, OM1’s sales and marketing teams need easy, ad hoc access to best serve their customers and to provide best-in-class service about the data that they are known for.
These two factors — maintaining speed on the scale and frequency of updates of data that OM1 offers AND making sure sales and marketing teams had the information that they needed in a timely manner — were two separate challenges that OM1’s data team needed to solve.
1. Maintaining speed and scale
On the one hand, these massive datasets were just too large, complex, and changing too much, causing expensive aggregations that would need to constantly be updated. They were also too complex to be explored ad hoc in traditional BI tools without help from the data team, creating painful experiences for business users to ask their own questions of data. Data engineers could carefully craft dashboards that were fast and efficient, but as soon as users struck out on their own, they’d run into 10 or 20 minute query runtimes and, to quote Zach, “get bored waiting and move on to greener pastures.”
2. Keeping up with evolving requests from sales and marketing
On the other hand, the rapid pace of evolution on questions from business users also made it challenging for the data team to support updates to datasets, BI dashboards, and reports. Even if the data team tried to create reports for their sales and marketing teams, they could never keep up with the demand; the number of aggregations and mappings needed were endless. As all data people know, every report delivered winds up generating three more follow-up questions.
Here is an overview of OM1’s pipeline with the challenges mentioned above:
“We’d go through this complicated cycle — a really long game of telephone — which caused a lot of friction in the system.” — Zach Bryant
OM1 needed to upgrade its data tooling to something that let the data team move faster and gave business users better access to self serve, with some guardrails.
The solution: A data app that puts business users in the driver’s seat
After adding Hex to their existing stack with dbt and Snowflake, the next step was to empower trusted self-serve. OM1 built a data app in Hex that let business users not just explore data, but actually manage the mappings for data categories like medications and conditions without having to write any SQL or Python.
This data app sits right on top of Snowflake and was easy for the data team to build using multi-modal methods of working with data — combining intuitive UI-based features with SQL, Python, and Snowpark.
Business users interact with a custom point-and-click interface, and behind the scenes, their requests are handled by SQL queries and Snowpark code that reads and writes to the warehouse.
knowledge
The Role of Snowflake in Scalable Analytics
Snowflake provides scalable data warehousing and analytics capabilities that supports OM1’s need for handling massive datasets while ensuring data integrity and performance. Learn about
our integration with Snowflake
.
This is saving the data team hours of time every week by empowering business users to be their own data engineers for ad hoc use cases directly within a user-friendly interface. With OM1’s Mapping Manager data app, business users dictate what they care about in the UI and the rest happens automatically.
knowledge
➡️
Try the open-source mapping manager for yourself
. OM1’s Mapping Manager data app is open-sourced.
OM1's Data App
Instead of adding head count, OM1 brought on tools to go further with their data
Before Hex and Snowflake, OM1’s data architecture of rigid BI tools made arriving at these data insights “a really long game of telephone” that left people to move forward without the data they needed.
Now, with a unified workspace for analytics and a flexible self-serve data app, OM1 is expanding internal knowledge throughout their company. Sales and marketing teams are helping clinicians, researchers, and scientists in faster ways by quickly understanding the full spectrum of data that OM1 can offer to them.
By empowering internal temas to manage data mappings independently, OM1 reduces dependency on IT and accelerates decision-making processes across the org.
See the customer story version of this story here
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
