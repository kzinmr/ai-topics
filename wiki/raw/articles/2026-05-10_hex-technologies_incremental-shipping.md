---
title: "On Software, Ships, and Shipping Incrementally | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/incremental-shipping/"
scraped: "2026-05-10T01:28:54.123544+00:00"
lastmod: "2020-09-16"
type: "sitemap"
---

# On Software, Ships, and Shipping Incrementally | Hex 

**Source**: [https://hex.tech/blog/incremental-shipping/](https://hex.tech/blog/incremental-shipping/)

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
On Software, Ships, and Shipping Incrementally
The only path around the 2.0 tar pit is incrementalism - replacing a legacy platform through small, deliberate steps.
Barry McCardel
Engineering
September 16, 2020
Share:
twitter
linkedin
Photo courtesy of NASA Archives
This is the U.S. Navy’s
MQ-8C Fire Scout
. It’s an unmanned drone, intended to provide recon and offense for ships at sea.
There are two weird things about it:
It doesn't look like a “drone”; it's like a normal helicopter with the windows painted over.
It didn't go way over schedule or budget, like so many modern military projects.
These things are related!
The MQ-8C airframe is sourced from the
Bell 407
, a best-selling manned helicopter design since 1996, which itself is based on the
Bell 206
, which in turn was based on the
YOH-4
, which
first flew in 1962
. This basic design has a rich heritage, with thousands of copies and millions of flight-hours behind it.
Similarly, they sourced the robotic UAV system from another existing design - the
MQ-8B
Fire Scout, which has been in production for 20 years.
The Navy - uncharacteristically - took an
incremental
approach to the MQ-8C. They relied on proven technology, made some modest changes, and within a few short years had a new system deployed in the field.
Compare this to the money pits of recent Navy infamy: the
Zumwalt Destroyer
, the
F-35 fighter jet
, the
Gerald Ford-class Carrier
, or the
Littoral Combat Ship
. Combined, these have run billions of dollars and decades over plan, in large part because they tried to make “great leaps”, advancing many parts of their stack all at once. It wasn’t enough to introduce 1 or 2 new technologies into a new version - the whole platform was to be built anew, from the windows to the walls.
In the tar pits
The incentives to approach development as a "big bang" are strong. Planners only work on so many projects in their careers, they have all these cool ideas, and it's someone else's money... why not try and push it all at once?
While appealing, this approach is doomed to fail. Each upgraded sub-system has some natural risk of delay, and the more one crams into a new platform, the higher the likelihood that the whole thing gets bogged down by the "long pole in the tent". And so we wind up with a
brand-new destroyer getting towed through the Panama Canal.
There are clear analogs in the software world, which is also marred by delayed projects and vaporware,
especially
for re-writes. In
The Mythical Man-Month
,
Fred Brooks coined the term
"Second System Effect"
to describe the tendency to over-scope successor projects, leading to their (often indefinite) delays.
Despite the book's presence on the shelves of generations of product and engineering managers, this trap - the figurative
tar pit
from the cover - is still easy to fall into. Some of us at
Hex
have been snared in the past. It's exactly what happened to me with a failed re-write a few years ago.
We hated our legacy backend, had big ideas for a new one, and were excited for everything we could build on top of it. Our team had a
vision
, and dove straight into the new thing, guns blazing. Anything less would have felt like a compromise.
In our minds, we were making lots of progress: the new system performed great in isolation, and we were already developing new frontend features to take advantage of it.
In reality, we were speeding toward a brick wall. Our plan required a big bang cut-over between the old and new backends, but for weeks we kept finding gaps that we needed to fill to make the transition 100%. We were
so close
, but after months of grinding we had to pull the plug because it just wasn't going to work.
Through this, I learned (the hard way) that
the only path around the 2.0 tar pit is incrementalism
: replacing the previous platform through small, deliberate steps, versus one fell swoop.
Incrementalism in Action
How does this work? Let's explore a few examples:
This excellent article on rearchitecting
explores incrementalism in depth, framing Rebecca Parsons's concept of "evolutionary architecture" as "one that supports incremental, guided change across multiple dimensions." It also references
Martin Fowler's classic analogy of a strangler fig
: "gradually create a new system around the edges of the old, letting it grow slowly over several years until the old system is strangled." While a bit macabre, it resonates deeply.
The
WAFL (Well-Architected, Functionally Limited) approach from CircleCI
could also be a helpful framework, especially for frontend redesigns where an in situ, piece-by-piece system replacement might not be feasible.
Shopify's post
on their big storefront re-write serves as an excellent example of incrementalism:
After our success with the password page, we tackled the most frequently accessed storefront pages on the platform (product pages, collection pages, etc).
Diff by diff, endpoint by endpoint, we slowly increased the parity rate between the legacy and new implementations.
By placing a new system alongside their legacy system and slowly cutting cutting traffic over, they built confidence and avoided a risky big-bang transition. Incrementalism FTW!
Slow is Fast
More than any specific approach, the first step to avoiding "second system" failures is internalizing that
incremental approaches don't mean lack of ambition
. It's okay to take things step by step. Focusing on small, shippable chunks can demonstrate progress to yourselves, and others. It may not be as sexy, but will feel better for everyone involved, especially compared to holding breath for a singular drop that may never come.
And now, back to the Navy: I'm not a weapons system designer
1
, but I wonder how the F-35 would have turned out if they pursued an incremental path, like the MQ-8C: take all the advanced avionics, get them working in an
F-18
(or vice versa: put an F-18’s older systems in a new, stealthy airframe), and then iterate from there. While the first version wouldn't be as capable on paper, I bet it could have been deployed years earlier and
still
reach the ultimate destination faster – without lighting billions of extra dollars on fire.
While software is cheaper to develop than a warship
2
, the U.S. military's mistakes are close kin to those committed by many development teams. And, like good product managers, perhaps our nation's Admiralty need to internalize that the fastest way to get to the ultimate destination is through small steps, not giant leaps.
↩
I would love to hear from you if you are
↩
usually, at least,
despite the military's best efforts
Share:
twitter
linkedin
At Hex, we're taking an incremental approach to building software, and making mostly new mistakes along the way.
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
