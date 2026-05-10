---
title: "Version Control for Notebooks: Sync Hex With GitHub | Hex | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/github-sync/"
scraped: "2026-05-10T01:28:58.671200+00:00"
lastmod: "2022-05-05"
type: "sitemap"
---

# Version Control for Notebooks: Sync Hex With GitHub | Hex | Hex 

**Source**: [https://hex.tech/blog/github-sync/](https://hex.tech/blog/github-sync/)

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
versioning_v3_final: Version Control for Hex Notebooks
Introducing an all-new way to version work in Hex
Claire Carroll
Product
May 5, 2022
Share:
twitter
linkedin
In this article
Should we even be versioning analytics work?
A human-friendly, reviewable file format
GitHub sync and pull requests
Logic diff view
See it in action
Get started for free
Today, we’re introducing a whole new suite of versioning workflows in Hex, including a
human-friendly file format
,
GitHub sync
, and a
rich in-app diff view
.
Together, these incorporate the best of software engineering best practices, while embracing the highly visual and UI-driven process of exploratory analysis and app building. Let’s dig in.
Should we even be versioning analytics work?
Over the last few years, software engineering best practices have changed how data teams transform data, configure infrastructure, and deploy pipelines. These things are now managed as code, and versioned through Git, making it easy to review work, revert changes, and collaborate without getting in each others’ way.
Teams using these workflows build trust in the assets they produce — code that is version controlled and reviewed is less error-prone than a script running on someone’s laptop. Code reviews raise the quality bar, by giving people feedback on making code more efficient and readable. It feels like how it always should have been done!
The data science and analytics layer, however, is still a mess.
Notebook .ipynb files are dense JSON that
include serialized outputs,
and are hard for team members to read or diff, let alone review. Analysts bookmark their queries in SQL runners, without any way for their peers to check their work. One-off dashboards float around, with no sense of governance or context.
Sometimes these things are checked into Git, without any way to understand what that code does, the artifacts that they produce, or what a stakeholder is actually consuming. And let’s be honest: a lot of data work still happens in spreadsheets, which are basically impossible to version control.
At times, this approach is ok, good even — when you’re pulling together a quick prototype, or spelunking for an insight, the ability to move quickly is a strength. But what happens when it moves past the exploratory phase? When your stakeholders are using your work to make business-critical decisions? Well, bad things can happen: bad analysis can cause bad decisions, eventually eroding trust in the work of a data team.
We believe analytical work deserves the same benefits of versioning workflows that other parts of our data stack have received.
And today we’re releasing a number of features to get us there.
A human-friendly, reviewable file format
If you’ve ever opened a notebook file (those ones with the
.ipnyb
extension) in a standard code editor, you would have been faced with a large blob of JSON. Notably, this JSON:
Represents both the logic in a cell, and a serialized version of the result, including potentially sensitive information in those results.
Is extremely hard to diff between versions — JSON just doesn’t really lend itself well to diffing.
Is inflexible, and doesn’t support many of the things we have built into Hex like SQL cells, input parameters, or app layouts.
What a .ipynb diff looks like even if only 1 cell was changed
Hex has always supported importing and exporting .ipynbs as Hex Projects. But with a caveat: exporting to an .ipynb meant you lost many of the things that make Hex special, like SQL cells, input parameters, and app layouts.
We needed a file format that preserved all aspects of a Hex project, was easier for members of a data team to review, and that didn’t contain those potentially-sensitive outputs. So, we adopted a file format based on YAML.
You can now export (or... hexport) your Hex projects as YAML files
— the YAML file contains all the code we need to to be able to reconstruct your project from scratch.
The same commit as above, in our purpose built YAML format
And, you can import these files back into Hex as well: either as new projects, or new versions of your existing project.
GitHub sync and pull requests
Ok, we have a file format - where are we putting it? Well, you can now sync your Hex projects to GitHub.
Every version of a project that you save will be represented as a commit on a branch, while the published version (i.e., what app users see) will reflect what’s on your main branch. You can either let Hex keep your GitHub branches up to date for you, or, if you’re a team that uses pull requests, you can require that team members get their work reviewed before publishing a Hex app.
Whether you choose to use pull requests or not, GitHub sync also unlocks a few other benefits:
You own your code.
We aren’t here to lock you in! You should keep using Hex because you love the product, not because you can’t get your code out of it.
You can search your code.
Deprecating a table in your data warehouse and need to know where it’s referenced? That can be much easier to do in a code repo.
You can make bulk changes to your code more easily.
Need to actually
replace
that table name? You can update the code in your repository, and import the changed code as a new version of your project back into Hex.
But reviewing code can be challenging when you can’t see the context of those changes — sure that SQL looks fine, but does it run? What kind of results does it return? Did that refactor change the output of my chart (I didn’t want it to!), or was that bug I was trying to fix actually fixed? Well, once again, we can help you out with that too.
Logic diff view
Our publish workflow contains a new tab:
Logic diff.
This view does exactly what the name implies: it shows you the differences between the logic of the version that’s currently published, and the version you’re about to publish. New cells, updated outputs, markdown grammar fixes, and tweaked SQL queries are all visible and easily auditable before publishing.
Exploring a version's changes in Logic diff
This view also:
Lets you run the old version of your app, aligning the outputs of each cell side-by-side, making it possible to visually inspect the impact of those changes on your app
Includes a file format representation of each cell, which includes any changed configurations, so you can review more than just the code
This is a powerful interface that brings together the changes to your code, and the impact of those changes. Whether you’re refactoring code and want to check that your final app
hasn’t
actually changed, adding new functionality to an existing project, or just can't quite remember what exactly you did change, you can review your changes to your project directly in Hex.
You can use this as a standalone feature, or in conjunction with GitHub sync to help pull request reviewers gain an understanding of the changes you want to merge.
See it in action
If you’re a current Hex user on the Teams plan, this is all live in production now!
If you’re not on Hex yet, you can get started with a free trial below.
We can’t wait to hear what you think of it.
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
