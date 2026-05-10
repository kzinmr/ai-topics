---
title: "Recap: San Francisco Public Data Hackathon | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/sf-public-data-hackathon/"
scraped: "2026-05-10T01:29:29.754392+00:00"
lastmod: "2024-02-21"
type: "sitemap"
---

# Recap: San Francisco Public Data Hackathon | Hex 

**Source**: [https://hex.tech/blog/sf-public-data-hackathon/](https://hex.tech/blog/sf-public-data-hackathon/)

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
Recap: San Francisco Public Data Hackathon
We brought the city's cleverest data people together to explore public municipal datasets
Izzy Miller
Friends of data
February 21, 2024
Share:
twitter
linkedin
In this article
Intro
Winning project: Road Risk Radar
Runner-up project: SF Data-Land
See you next time?
Get started for free
Join our next Hackathon and live events by checking out
our events page
.
Intro
Last weekend, Hex and
Modelbit
hosted a
San Francisco public data hackathon
at our office downtown. What the heck is a “public data hackathon”? Here’s our magical recipe:
Pull down a few hundred million rows of data from the
San Francisco Open Data
portal.
Clean (not
too
much) and load the data into a publicly accessible Snowflake warehouse.
Order a ton of pizza from
Pie Punks
.
Give free Hex and Modelbit accounts to a hundred curious data people, and set them loose.
We wanted people to discover new insights about the city they live and work in, understand their daily backdrop in a different way, and build data experiences that inspire everyone to make this beautiful city even better (I put an official moratorium on 💩 maps). At the end of the day, twenty teams submitted finished projects that ranged from Vision Pro data apps to careful analysis of sidewalk width variance.
In this blog, I’ll highlight the two winning projects.
Winning project: Road Risk Radar
Anup Mantri, Vinit Agrawal, Lourdes Lopez, Joshua Sorkin, Shayan Guha.
The winning team looked at data on traffic accidents in the city over the last 18 years, and built a model that analyzes a route through the city to provide an aggregated risk level for every intersection that route crosses.
Their project has two components: A data visualization tool and the actual model.
Before diving into model training, the team built a data app in Hex to visualize the traffic injury data. Running directly off the public datasets in Snowflake, it lets you drill in by street and vehicle type, and scrub through time to see specific trends.
Road Risk Radar 1
After exploring the city and validating some initial assumptions, they built a machine learning model to predict accident risk anywhere in the city. Their model (trained and deployed on Modelbit, using Hex’s Modelbit integration) takes in multiple features: [Day of week, Month, Time, Weather, and lat/lon] and outputs a “risk level”, computed from a predicted incident ratio and overall injury / death forecast. There’s some neat innards to this model, like a clever block-level lat/lon binning to make it more performant, and the inclusion of weather conditions.
roadriskradar #2
Taking it one step further, they deployed this model using Modelbit and built a quick app that lets users make informed decisions about their routes through the city.
Their completed app:
Takes a Start and a Destination location.
Computes a Google Maps route between them.
Returns an overall and intersection-level risk score for the entire route.
This is a really impressive project, completed in just a couple of hours using brand new tools— very impressive and complete work.
Runner-up project: SF Data-Land
Jess Cherny, Mattie Blue
Our runner-up project combined two distinct sources of data: Movie film locations and SF Muni bus routes. They built an app that helps you:
Locate which famous film locations were filmed on your bus route of choice.
Locate all the bus routes that take you to the locations from your movie of choice.
Find transit directions from Hex's office to your SF film location of choice.
sf land
My childhood bus route (38 —> 43) is loaded with Hollywood points of interest! But I promise that’s not why this team won the second place prize— behind the scenes of these beautiful maps, there’s actually a lot going on: requests to the Google Maps API, clever joining of data from a few different sources, and some quick geospatial distance calculations that are performant enough for the Hex app to feel smooth and interactive.
This is a great use of Hex, and a nice clean interface to some surprisingly complex data manipulation. And a lovely story to boot.
See you next time?
This is just our first event. If that magical blueprint (remember: millions of rows of public data, unreasonable amounts of pizza, and cool data tools) sounds enticing to you, we’d love to see you next time.
Join our slack community
and we'll keep you posted on events to come!
And if you want to get a jump on things... you can pop into Hex and explore against our
DEMO_DATA.SF_PUBLIC_DATA
schema right now. Here’s a project you can fork that shows some recent lobbyist activities:
clone
See you soon 🖖.
Share:
twitter
linkedin
Want to give Hex a spin? Click below to create a free forever Hex account. Or, check out our open roles, and come join us building the future of data.
✨ Get started for free
👩‍💻 Open roles
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
