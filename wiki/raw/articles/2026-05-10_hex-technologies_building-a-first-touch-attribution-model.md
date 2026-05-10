---
title: "Why, when and how to use a first-touch attribution model | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/building-a-first-touch-attribution-model/"
scraped: "2026-05-10T01:29:47.042819+00:00"
lastmod: "2023-07-17"
type: "sitemap"
---

# Why, when and how to use a first-touch attribution model | Hex 

**Source**: [https://hex.tech/blog/building-a-first-touch-attribution-model/](https://hex.tech/blog/building-a-first-touch-attribution-model/)

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
Why, when and how to use a first-touch attribution model
Or: this blog post has made $0
Caleb Bowie
Data
July 17, 2023
Share:
twitter
linkedin
In this article
What even is marketing attribution?
How we landed on first-touch attribution
Okay, let’s build that model!
Now it is time to put your new model to use!
Final thoughts
Get started for free
This blog post has made $0 (as of 7/17/23).
Depending on how long ago it was published, that figure should serve as either commentary on the unpredictable futility of content marketing, or as an incredible proof point of the success of content marketing. Hopefully the latter.
Because this took a long time to write! And even though I
mostly
wrote it because I hope that you will read it, enjoy it, and learn something valuable from it…
I also
sort of
wrote it because I hope that after doing all that, you might try out Hex, and maybe some day even start paying us some money.
But without the ability to calculate exactly how many people paid for Hex as a result of this blog, we cannot answer the two most important questions to ask of any marketing activity: “Was it worth it?” and “What should we do differently next time?”
This blog post details the efficient way we built a first-touch marketing attribution model at Hex, why we decided to do it this way, and how you can build your own.
What even is marketing attribution?
Marketing attribution is the process of assigning credit to the activities that drive a customer to convert. There are lots of tools and services you can purchase to do marketing attribution, but if you want the most control over the solution, developing one on your own with SQL is probably the right approach.
There are many different ways to do marketing attribution, but most of them fall into two different categories; single touch and multi touch attribution. Within those two categories, there are many different ways to actually attribute credit in your model.
Here are a few common ways:
First-touch attribution - 100% of the attribution goes to the first touch
Last-touch attribution - 100% of the attribution goes to the last touch
Linear attribution - The attribution is split evenly between all touches
Weighted multi-touch attribution - The attribution is split between all the touches, but each touch is weighted differently.
And no,
it’s not fake
. Although I suppose we did kind of just make it up.
How we landed on first-touch attribution
Attribution is a highly debated topic, filled with many spicy takes. Often times building an attribution model can turn into a huge time sink, so as an analyst it is very important to prioritize
speed-to-value
with your resources.
If you are building your own attribution model, the method of attribution you choose will be dictated by your current data ecosystem. One of the foundational pieces to most of those attribution models is something called
web sessions
.
Web sessions represent a period in time, that a user interacts with your web site or app.
They are typically defined by a series of page views or other actions.
At Hex, we had not developed a model that turned our web traffic into sessions.
That brought us to an important inflection point in the process. We needed to decide if we were going to shift gears and build a sessions model, or find a way to continue to move quickly to provide value.
So we decided to go with a first-touch model. It aligned with our top-of-funnel focus, and allowed us to quickly provide some value and insight into where our conversions are coming.
Okay, let’s build that model!
1. Categorize traffic into channels
Our site traffic comes from many sources, so it is important to group traffic into categories. This is done by using a combination of referrer information and utm attributes to determine these channels.
This article has a great overview of the different types of channels
https://support.similarweb.com/hc/en-us/articles/360000807449-Marketing-Channels
You will likely end up doing something like this in your ETL process for each of channel:
Copy
when utm_medium in ('social', 'social media')
or (utm_medium is null
and (contains(referrer_host, 't.co')
or contains(referrer_host, 'twitter')
or contains(referrer_host, 'linkedin')
or contains(referrer_host, 'facebook')
)
)
then 'organic social'
2. Match users to their traffic
Once our traffic is categorized into channels, we need to be able to match users to their pre-signup visits. This process is commonly referred to as
user stitching, identity stitching or member resolution.
I will just refer to it as user stitching.
User stitching is the process of enriching your web traffic or user actions with user data once you know the identity of that user.
Most modern companies have a tool they use for event tracking. Those tools typically issue a UUID for each unique visitor. For converted users, we have our own internal UUID as well. Once a conversion event happens, we can map those UUIDs to each other.
We turned this into a model that can be consumed by our web page models, and we can then use this pairing to match a user to their traffic that predates their signups
Copy
select distinct
anonymous_id -- id from your event tracking tool
, hex_user_id
from events
In the SQL that builds our web page models, we can then join in this mapping model to create a new field that we can later use in the attribution model.
, coalesce(user_mapping.hex_user_id, page_view.anonymous_id) as individual_identifier
We have now created this field called
individual_identifier
on all of our page views that will be a users Hex user id if we have matched them with their traffic.
Once you have done this you have laid the ground work for your first-touch attribution, and all that’s left is driving off into the sunset
3. Create the final model
In the Hex product, multiple users can be in the same workspace, but for this use case we want to limit our analysis to just users who created a new workspace. We can do this by getting the first user in each workspace.
Copy
with workspace_creating_user as (
select
user_id
, user_created_at
, workspace_id
from users
qualify row_number() over(partition by workspace_id asc) = 1
)
Then, we can do something very similar to get the first page view for a user,
Copy
first_touch_page_view as (
select
individual_identifier
, page_viewed_at
, cat_channel_group
from page_views
qualify row_number() over(partition by individual_identifier asc) = 1
)
Finally we can join these two together, and that will give us a first-touch attribution model that we can use to quantify the most impactful sources of our customers
Copy
select
user_id
, user_created_at
, workspace_id
, page_viewed_at as first_touch_at
, cat_channel_group as first_touch_channel
from workspace_creating_user
join first_touch_page_view
on workspace_creating_user.user_id
= first_touch_page_view.individual_identifier
Now it is time to put your new model to use!
In our case, we wanted to know which channels most of our signups were coming from, and we also wanted to set up some reporting to monitor that over time. The quickest way to get an idea of this is by doing something like signups over time by first-touch channel.
Attribution— signups chart
Another metric that many people measure is Conversion to Signup by these different channels. If you are sinking money into one channel, but it is not resulting in many conversions, resources may need to be reallocated to target users who typically come in through a different flow
There can be a lot of nuance in conversion rates that people don’t always consider. I could probably write an entire article about that. But for now some things to keep top of mind are the volumes of your denominators and time to conversion.
One simple rate to look at is a forward looking conversion rate. Something like this:
Attribution blog— Conversion rate
When doing forward looking conversions, I like to time bound that story. I do this typically by adding some context like a “Conversion Rate in 30 Days” line. You can still see the all time conversion rate, but conversions that have really long tails are hard to predict and action against. So the 30 day time bound serves as a leading indicator of the trend.
Backwards looking conversion rates are another way to do conversion, but I will save that for another day.
Final thoughts
Building a first-touch attribution model is not something an analyst would likely consider their magnum opus, but it may be what best serves your stakeholders in the interim until you can build a more sophisticated model.
To recap:
If you are asked to build a marketing attribution model, you first have to decide which type of model you can build with the resources you have.
If you do settle on first-touch attribution, remember this is a huge leap from nothing to something very actionable.
Remember; you are the one closest to the data, and it is your responsibility to deliver the best speed-to-value solution you can with the resources you have.
Share:
twitter
linkedin
This is exactly the kind of analysis that's delightful to do in Hex, with our flexible and polyglot environment for working with SQL and Python. So what are you waiting for? Click "Get Started" to try it out (for free!) and maybe... just maybe... help change the subtitle of this post.
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
