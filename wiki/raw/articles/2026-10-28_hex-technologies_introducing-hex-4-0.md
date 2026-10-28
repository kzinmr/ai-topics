---
title: "Introducing Hex 4.0"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/introducing-hex-4-0/"
scraped: "2026-10-28T06:00:35.361045+00:00"
lastmod: "2026-10-27"
type: "sitemap"
---

# Introducing Hex 4.0

**Source**: [https://hex.tech/blog/introducing-hex-4-0/](https://hex.tech/blog/introducing-hex-4-0/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
Introducing Hex 4.0
A reimagined platform for humans and agents to collaborate with data
Olivia Koshy
Product
October 27, 2026
Share:
twitter
linkedin
In this article
Introducing Hex 4.0: a truly agent-native platform for analytics
Build from anywhere, with context and controls
A new, intuitive Hex UI, built for reviewing and understanding
An all-new, ridiculously faster execution engine
What’s next & getting started with 4.0
Get started for free
Suddenly, data teams have had a lot of things dropped on their plate: Their organizations are working
around
legacy BI, pulling in scattered context, burning tokens, and passing around “vibe-coded” HTML files – a massive sprawl of AI data stuff that nobody can govern or observe.
On one hand, this is great news: finally, people are able to use data in their day to day! Self-serve is here?
On the other,
it’s a nightmare
: they’re stuck managing code they didn’t write, answers they didn’t review, and apps they didn’t even know existed.
Introducing Hex 4.0: a
truly
agent-native platform for analytics
Today, we’re introducing Hex 4.0 to solve exactly this. It’s the next major version of our platform, built to embrace AI agents and code, with the context and controls necessary to make it
actually
work for your company at scale.
With 4.0:
It’s easier than ever to ask questions from Hex’s UI, or external agents like Claude, Codex, or Cursor, and then publish and share them securely
It’s
finally
possible for data teams to have a first class tool for reviewing agent-generated analytics code to know how something was built and if anyone should trust it
Apps in Hex run way faster due to our all-new execution engine
Perhaps most importantly, 4.0 sets the foundation for a huge number of
new
workflows for Hex that previously wouldn’t have been possible.
Build from anywhere, with context and controls
If you run a data platform right now, it can feel like you’re stuck. Leadership wants every team using AI for data, and they’re already doing it with whatever they’ve cobbled together. Meanwhile, the official BI platforms your team has been maintaining are tied to clunky AI harnesses attempting to adapt legacy systems for new technology.
You can try to shut down ad hoc data exploration, especially once the sprawl starts spawning arguments over whose secret dashboard has the right numbers. But then you’re the bottleneck, and the best answer you can give is some version of “no, not like that!”
Hex 4.0 is built to break this tradeoff by embracing
the full flexibility of code
. Now every project’s core logic and visualizations are fully backed by code files (rather than a YAML spec)
,
but rooted in governed context, with consistent logic, visual standards, and logical organization. This means it’s easy for agents to work with, and humans get the benefit of full flexibility in what they can build.
4.0 enables the creation of fully interactive and deeply creative apps, all backed by your company's trusted data.
We’ve also expanded external agent capabilities so you and your team can leverage the Hex platform wherever and however you work.
For example you can start with an artifact in Claude, then easily push it to Hex and rebuild it as an app. Or, you can take a link to one of your existing Hex 4.0 projects, and edit it wherever you are.
With Hex 4.0 and our MCP server, you can create powerful data apps anywhere!
Data teams are also looking for a platform that supports all of thier agents, like StubHub, which has been one of our alpha testers on 4.0.
“The new Hex platform is exactly what we have been looking for: agent-native and code-first, with a super approachable UI that actually makes inspecting agent-written logic easy. We're especially excited about the flexibility this provides for our data workflows with external agents.” — Nova Wang, Sr. Director of Data Engineering & Analytics Engineering @ StubHub
Published apps compound into knowledge you and your team can leverage. Once something is shared in Hex, it’s available to you and the rest of your team (and their agents!). That makes it easy to ask follow-up questions, grab the latest numbers, or pull it into other workflows.
A new, intuitive Hex UI, built for reviewing and understanding
Everyone is focused on giving teams the tools to build with data. We think the next shift is a platform build for understanding what gets built. With 4.0, any number in an app is inspectable, so you can see exactly where it came from. There’s a summary to help you get oriented and you can see the full logic plus quickly see the data sources used.
Click the inspect button on any element, and see the full lineage of your data.
Behind the scenes, this is what our new code framework enables. The agent isn’t just writing arbitrary code files, it specifies every dependency, the full DAG, so you can trace the entire lineage of anything on the page.
We also built this UI so non-technical users can easily gauge numbers for themselves, even if they'll never touch a notebook. They can see if a KPI in their dashboard is backed by a trusted semantic model, or if it's a tangle of complex logic that needs additional eyes from the data team. This has been an early boon to Ro, another one of our alpha testers.
"At Ro, our data team's north star is to help our patients achieve their health goals by allowing everyone at the company to make better, faster decisions. Hex 4.0 enables anyone at Ro ask data questions from wherever they're already working, while giving our data team the tools we need to make sure those answers are reliable and accurate.” — Nick Hardy, VP of Data @ Ro
As part of this evolution of Hex's platform, we’ve also reimagined the Notebook as a collaboration surface between humans and agents. You can still write and tweak code by hand, but a huge part of the job is navigating what an agent has written.
An all-new, ridiculously faster execution engine
We’ve rebuilt our execution engine from scratch, so apps run way faster, especially large, interactive ones.
Rebuilding our compute architecture allowed us to make major improvements:
Parallel logic execution:
if two queries don’t depend on each other, they run at the same time instead of waiting in line. Apps with several warehouse queries feel this most.
Results stream in as they’re ready.
Each chart, table, or KPI shows up the moment its step finishes. You don’t wait on cells in a tab you haven’t even opened.
A changed input only reruns what it affects.
Change a filter and Hex reruns that step and whatever depends on it. Everything else stays cached.
Here’s a side by side example from an internal app:
Hex 3.0 (left) vs. Hex 4.0 (right)
For major critical apps internally, we saw a huge improvement in full app run time.
Beyond just running faster, this unlocks a kind of app you probably wouldn’t have built in Hex before, now that highly interactive filters, drill-downs, and “what if” controls can run instantaneously without triggering a re-run of the entire project. Here’s an example app an engineer on our team built last week tracking Hex 4.0 UI usage (yes, of course we use Hex to build Hex):
This Hex 4.0 project changes filter states live on hover and click, something that would have taken minutes with our 3.0 architecture.
What’s next & getting started with 4.0
Perhaps most importantly, 4.0 sets up the Hex platform to be far more flexible and enables us to build a whole suite of features that previously wouldn’t have been possible. We’re excited to share more on this soon.
Hex 4.0 is in private beta today, with broader availability rolling out over the coming weeks. During this period, we’re
very
excited to keep building in collaboration with customers. Existing Hex projects will continue to work, but we’ll soon have a first class migration workflow to make upgrading to 4.0 a breeze.
To learn more - you can check out our
full docs here
, and we’ll be sharing more during our afternoon keynote session at Prompt later today.
We can’t wait to hear your feedback, and see what you build!
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
✨
🔊
🎧
🌊
🍀
🤠
🎷
on
🌎
.
Platform
AI and agents
Agentic notebooks
Conversational analytics
Context Studio
Data apps
Hex CLI
Business intelligence
Exploratory analysis
Embedded analytics
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
Company
About
Careers
Customers
Solutions
Media kit
Newsroom
Connect
Request a demo
Technical support
Contact us
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
You have opted out of data tracking
