---
title: "Tristan Handy: dbt's Evolution | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/friends-of-data-tristan-handy-dbt/"
scraped: "2026-05-10T01:28:58.251341+00:00"
lastmod: "2024-10-17"
type: "sitemap"
---

# Tristan Handy: dbt's Evolution | Hex 

**Source**: [https://hex.tech/blog/friends-of-data-tristan-handy-dbt/](https://hex.tech/blog/friends-of-data-tristan-handy-dbt/)

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
October 17, 2024
Tristan Handy: dbt's Evolution
dbt
Share:
twitter
linkedin
Tristan Handy, CEO and co-founder of dbt, just wrapped up his fifth
Coalesce
conference. This year marked the largest turnout yet, with an equally robust product lineup — dbt unveiled
more product announcements
than at any previous Coalesce.
On the event's final day, Tristan sat down with Barry for a
special
live
edition of Friends of Data
. During their "medium-spicy" 🌶️ fireside chat, he shared takes on industry shifts, how dbt thinks about its OSS vs. commercial offerings, Iceberg's impact on data, value capture within the modern data stack, and data team ROI.
Barry: This is the biggest Coalesce ever. How's that feel as CEO?
Tristan: That is a very big question. In a lot of ways it feels great.
It turns out that software amortizes well, and the more people use it, the more cool stuff you can build. And I think that the flywheel of this community continues to get bigger and that allows not just us, but other people in the ecosystem to be able to build cooler, bigger things.
There is also a dynamic that maybe other people are feeling in the room tonight that I think it's important to acknowledge. There was a period of time when if you went to Coalesce, you were a part of a cool kids club — you had to work to get here.
That's a little bit less true than it once was. The relationships that formed in that version of the community are still here, but now the community is bigger and has more diverse groups of people who also have important needs and problems that I think we should care about solving collectively.
The big announcement in 2021 was dbt open-source core 1.0. Today, you guys released a lot of product on cloud. How has your thinking evolved from making open-source ubiquitous to now a broader product surface area?
dbt is now eight and a half years old, but even so, we are still newer relative to some of the commercial successes in open-source and have had the benefit of learning from the bruises that Kafka or Spark had along the way.
I am honestly very proud that we have never had to do a big license change. In the 2017 time period, we saw a lot of relicenses happen and didn't want to experience that. So it was really this “statefulness divide” that we used as our mechanism to say what goes in open-source and what goes in commercial.
dbt core is a locally installed application. It reads and writes files on disk and connects to a data warehouse and has no other source of state. And that choice was made from learning from those companies — we decided that state is a good thing to commercialize.
So, is "statefulness" a good heuristic for distinguishing between what to expect from Core versus your commercial offerings?
Yes, that's a pretty reasonable facsimile.
The way we tend to talk about it in a broader context is: that open-source is generally not enterprise-ready. So, if you need to scale out to a large install, the features that we put in cloud are for you.
But open-source is and always will be a great way to get started.
To some, the Iceberg support might seem like a technical detail, but I think there’s something more there. Can you talk about how you’re looking at Iceberg and how it's going to affect the stacks and technologies we use?
You can imagine a world where Iceberg and
Materialize
actually start to move us back to ETL instead of ELT; because if you get data in a stream, why would you not apply the transformations before they land in the warehouse, if you can do it all in SQL and can go through CI/CD, etc?
I don't know that that’s gonna happen, but it’s an interesting concept. We've been on the ELT bandwagon for eight years. But this is the type of thing that Iceberg is throwing up into the air: how do we construct our systems now that the walls between our compute platforms have gone down?
It turns out that it was not just a better idea to do ELT because of the cloud, it was a better idea because it was just so much easier to throw your data all in one place and then operate in there. You could do anything as long as it was in a batch-based world view.
This is not even getting into the battles between the vendors, and I'm sure there's inside baseball that you and I think a lot about too. Who makes the money?
I’m curious about what percent of the GDP of any of our products are captured by our products vs. the actual platforms underneath.
For instance, what percentage of data warehouse revenue is driven by dbt and how does it compare to dbt’s revenue?
So roughly, as a rule of thumb, about 10% of all dbt users pay us any money at all — which is high, relative to other open-source companies, and obviously that's order of magnitude difference. And my rough belief, and this is very back-of-the-envelope, is that a dbt customer pays us about 10% of the compute that dbt is then driving on the downstream platform.
Wow, that compounds. You guys might be capturing 1% of the GPD then.
That's kind of my rough estimate.
That's really interesting. How does it make you feel?
[
Laughs
]. It certainly makes my day-to-day life challenging, but, honestly, I think you know me well enough to know that based on the metrics that I got into this for in the first place — the idea that we are generating a lot more value than we are capturing is totally consistent with what I would want.
There's this interesting relationship up and down the data stack where the partner-competitor distinctions blur. How do you think about relationships with others as dbt's ambitions broaden?
This is a thing that plays out in so many different ecosystems at so many different scales. Everybody is always trying to become a platform: Snowflake is trying to become a platform in its own unique way, so is Databricks — so we're not unique in having this thought process.
My read of what’s happening in the space is that everybody has identified their unique persona, their unique value proposition — what it is that they do better than everybody else. And the thing about dbt Explorer and our platform play, more broadly, is that we're not actually trying to be a
better
catalog than anybody else. The thing about Explorer is that it is the most uniquely tailored to the dbt workflow. It's not another vendor contract and it is not an incremental cost. It’s a thing that you get if you are a part of the cloud ecosystem.
And that's the platform play — you add more capabilities and make it more and more compelling to join that party.
I don't think that we should be spending all of our time thinking about how do we glue systems together. But I do think that the integration between all these different things needs to happen and the incremental features are less important than: does it all work together?
You said that we are all co-conspirators in increasing ROI from data. What’s your point of view on data ROI? Is it measurable?
When it comes to ROI — obviously if people are paying us to do this stuff, somebody believes that there's a reason to employ us. I don't think it's all a big hoax. I don't think we are all faking our way into jobs and technology budgets.
So then the question is: what percentage of our activities can you directly translate into: “I did the research, I made a decision, and there's a direct result of that decision”? And I think that certainly exists, actually very frequently in the marketing domain.
And then sometimes, you don't really know. How much does it matter that you have a dashboard of the core metrics of your business? Sometimes you check it and it says that everything is the same. Is that good or bad?
You can't
not
have it, though. You also can't not have accountants or lawyers. And no one asks the ROI on lawyers.
There's this qualitative metric of: would you give up headcount to get another data person? I think that's actually the mission.
Over the last 10 or 15 years we've had data teams that didn't used to be a team. Data used to be everyone's responsibility and much of it happened on your local machine on Excel.
There wasn’t a data team employee. There was a job that was attached to a business leader who had an ROI target and needed a business analyst. That was a much more clear conversation.
Then all of the business analysts got crammed together into a central team, and then we all started asking this existential question: are we valuable?
We knew how to measure the value when we were all a part of the business, so a big part of what we're trying to do is actually reduce the centralization. I believe that we should push more of the data function back out to the lines of business.
I don't know if that's spicy, but I really believe that.
Share:
twitter
linkedin
If you found this interesting or meaningful, sign up to find out about the next Friends of Data event.
Sign up here
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
