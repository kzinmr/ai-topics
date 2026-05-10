---
title: "Hex for Analytics Engineers: Hex Powered PR Review | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/hex-for-analytics-engineers-hex-pr-review/"
scraped: "2026-05-10T01:29:14.839460+00:00"
lastmod: "2022-06-09"
type: "sitemap"
---

# Hex for Analytics Engineers: Hex Powered PR Review | Hex 

**Source**: [https://hex.tech/blog/hex-for-analytics-engineers-hex-pr-review/](https://hex.tech/blog/hex-for-analytics-engineers-hex-pr-review/)

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
Hex for Analytics Engineers: Hex Powered PR Review
Streamlining analytics engineering workflows with Hex
Erika Pullum
Data
June 9, 2022
Share:
twitter
linkedin
In this article
Hex as an IDE
Validating dbt Changes: Before Hex
Audit Helper’s Hexy Glow Up
Audit Traceability with App Snapshots
High Quality Hex Powered PR Reviews
Get started for free
knowledge
This is part 2 of a series on using Hex for analytics engineering workflows.
Part 1️⃣:
Hex for Data Transformation
Stay tuned for the next posts, and drop a line in
the #tools-hex channel on dbt slack
if there's an analytics engineering concept you're interested in having me cover! If you're not a member yet,
join here
.
Data teams have adopted a whole host of software engineering
best practices
, among them:
Version control and PR review
Modularity
Documentation
Testing
Linting
We’ve come a long way, but reviewing data transformations in PRs still kind of sucks. Consider the simple diff below — should you approve this PR?
🤔🤔🤔
The code doesn’t give you everything you need to understand how the changes affect the warehouse in context. As a reviewer, you have to read the diff with the codebase and the data in mind, asking questions like:
What’s in this table?
How does changing this where condition affect the results?
What are the downstream dependencies of this model?
Will anything break if we merge this PR?
Reviewers have to make a choice between two bad alternatives: rubber stamping PRs, or replicating enough of the work themselves to be confident in what’s going on. At best, you spend a lot of time to get to a good review. At worst, you give a 👍 and LGTM and hope nothing breaks.
Submitters don’t have great developer experience either. It’s a lot of work to get enough context into the pull request to enable your reviewer to understand your work. Before Hex, I often did this as an extra, final step involving writing things up and copying screenshots into a PR.
Here's how we’ve leveraged Hex to enable frictionless high quality reviews, for both submitters and reviewers!
Hex as an IDE
I wrote a
few weeks ago
about how I use Hex to keep myself in flow when developing data transformations.
Typically, I create one Hex app for every PR I make to change our data transformations. I work as messily and non-linearly as I need to get to a happy place with the transformations. When I’m happy, I’ll move the code over to dbt and start getting ready for review.
I clean up and annotate my working app for my reviewer, until it contains a story with:
Markdown explaining the code in the app
Queries and sample data for new models
Annotated investigation of exceptions
For reviewers, the Hex app provides a helpful context. They can skim the logic view to understand what EDA was done, and how. The reviewer can see the queries and the output in context in the Hex app. This means when they’re reviewing the code, they don’t have to imagine the output. They can just go look at it!
To demonstrate this, we’ve cooked up some sample data for a hypothetical Dumpling Shack business and modeled it in dbt.
Here are two example Hex apps for changes to the dbt models:
A change to a definition for what constitutes a customer’s favorite
An refactoring of the dbt models that shouldn’t change any resultant data
Validating dbt Changes: Before Hex
Using Hex to document the development work is a big improvement in review quality and reviewer experience. Reviewers can see how the work was done, but they're not done yet. They still need to know that the changes to the output — the models in the warehouse — are correct.
Before Hex, I used
audit helper
to make PR validation a little less painful. Audit helper prints nifty comparisons between your development and production schemas, like this:
Example audit helper output
If you’re not familiar, check out this vintage Claire Carroll post for an overview of
what audit helper is and how it works
.
Still, the workflow for using audit helper is clunky:
Go to my analysis file
Update it for my relation
Compile it
Copy the query from the compiled file
Run in my IDE
Look at the comparison report
Uncomment the rows that match, comment out the summary
My workflow before
Before Hex, I wrote a
shell function
to automate steps 1-4 above. I still found myself changing the compiled SQL a lot — it’s not perfect for all use cases. For big tables, the query can get expensive and it’s a good idea to add a
where
to sensibly limit your data.
If the new relation has new columns, the query can’t compute the intersect and you have to edit the analysis file or the query to account for that.
Then, once the queries are run, you still need to get the results in to your PR. Run query, copy screenshot, repeat for as many audit queries as you need. If a reviewer has feedback and you make a change, you have to do it all over again.
Audit Helper’s Hexy Glow Up
I hit peak Hex hype the day I realized I could migrate audit helper to Hex for a much better PR submitter validation workflow.
For this post, you’re not stuck with just the Loom — you can check the app itself out in
our gallery
! It uses the two Dumpling Shack examples from above:
A change to the definition for what constitutes a customer’s favorite
An improvement to the dbt models that shouldn’t change any resultant data
Audit Traceability with App Snapshots
I used to do audit at the last minute, as part of PR submission. My Hex app made auditing ✨ so easy and magical ✨ that I now do it whenever I’ve committed a change I think needs auditing.
My new workflow looks like this:
Use Audit Helper to check my changes
Make a snapshot for later
Add snapshot links to my PR when I’m ready to submit
My workflow now
Hex snapshots persist with the app, so I can make a snapshot when I’m in flow and come back to it to snag the link when I’m ready for PR review.
Unlike query code or screenshots pasted into PRs, Hex app snapshots make a persistent record the data team can come back to if problems arise later on.
Integrating audit into my developing flow means I’ve already validated my changes by the time the PR is submitted for review. Auditing is a part of how I work, not a checkbox I have to tick off before I “get” to submit my PR for review. Since the auditing work is integrated, it’s less likely to be skipped or shortchanged.
Snapshots > checkboxes
High Quality Hex Powered PR Reviews
We shouldn’t have to make tradeoffs between effort and quality in review. Hex enables submitters and reviewers to collaborate throughout the development and review process. This enables high quality, low effort reviews for data transformations.
What more do you want to learn about how we’re using Hex at Hex? I’m not done writing about it yet, so come
join the conversation over in dbt slack
and let me know what I should tackle next!
Share:
twitter
linkedin
Want to try out Hex on your own data? Click below to get started for free.
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
