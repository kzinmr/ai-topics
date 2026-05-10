---
title: "MCPs: What they are and how you can use them with Hex's API | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/mcps-with-hex/"
scraped: "2026-05-10T01:27:10.247372+00:00"
lastmod: "2025-03-20"
type: "sitemap"
---

# MCPs: What they are and how you can use them with Hex's API | Hex 

**Source**: [https://hex.tech/blog/mcps-with-hex/](https://hex.tech/blog/mcps-with-hex/)

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
MCPs: What they are and how you can use them with Hex's API
Rethinking the dev workflow with MCPs
Franccesco Orozco & Olivia Koshy
Data teams
March 20, 2025
Share:
twitter
linkedin
Updated October 29, 2025:
You can now use Hex's official MCP server to get answers to data questions and access Hex content without leaving AI assistants like Claude Desktop, Claude Code, and Cursor.
knowledge
Get started with our
MCP server docs
.
Keep reading if you're interested in using an open-source project to leverage Hex's
public API endpoints
with the MCP standard!
We sat down with
Fran Orozco
, a data leader at BloomGrowth, and learned how he’s taking advantage of MCPs to streamline his data dev process. It was pretty sweet so we asked him if he’d be willing to share — and to our delight, he did!
Using an MCP with Hex. ✨ Learn how to do this below!
Before we jump in…. a quick MCP intro
You've probably seen MCPs
generating
buzz
on
X
. But what are they really? 🤔🤔🤔
Model Context Protocols create a standardized API for AI systems to access context and use tools. MCPs define how:
Tools expose capabilities to AI assistants — and you can define those tools
AI models request actions using those tools — and then can combine multiple tool use
AI models can automatically write code to quickly parse/extract the necessary info returned from the tool calls
It's really easy to plug in APIs that already exist, customize them to your use case, and get started with tools like Cursor or Claude.
So, what does this look like in practice?
That’s where Fran comes in! He’s been experimenting with MCPs and experiencing first-hand how they're saving him time. Let’s turn it over to Fran 🙂...
MCPs: Rethinking the dev experience
👋 Hi — I'm Fran, a data lead at BloomGrowth! We're a team that’s quickly growing, and so is our use of data to ask and answer questions. This means Hex is an integral part of our data stack and is used throughout the business.
While Hex provides an incredible frontend experience for
ad hoc analysis
and interactive reports, a lot of my day-to-day analytics engineering work is done in Cursor. I'm constantly doing data transformation using dbt, building tests, or writing documentation. After this, I need to re-execute my Hex projects to make sure they've run successfully, but I've always wished I could do this from my own development environment without switching tools and contexts.
This workflow is changing dramatically with the introduction of MCPs. By using MCPs in Claude or Cursor, our developers and data engineers are accelerating development times, simplifying onboarding challenges for new engineers, and orchestrating jobs using only natural language.
So how does this actually work day-to-day?
I have a Hex project that pushes data to HubSpot. I run it daily, but when I integrate new data, I want to run the project ahead of the usual schedule. I can ask Cursor to search for it:
It returns the project along with metadata like its schedule. I can ask for it to run it again and give me a run status:
Finally, I can ask if the project has finished running:
This unlocks a new level of interactivity as a data practitioner working on the backend and makes Hex feel integrated
across
the dev data stack
.
This new workflow isn't just about convenience — it's about maintaining deeper focus. My team can iterate faster on changes and observability is a breeze.
Under the hood: How my Hex MCP server works
My open-source
hex-mcp
project bridges Hex's existing
public API endpoints
with the MCP standard.
Today, Hex offers APIs that allow you to:
List and review projects
Trigger project runs
Check run statuses
Cancel ongoing runs
The
hex-mcp
package wraps these capabilities in the MCP format, enabling AI assistants like those in Cursor or Claude to understand and use them. It essentially translates between:
Copy
AI Assistant (using MCP) → hex-mcp server → Hex API → Hex Platform
This translation layer means I can interact with Hex through natural language in my dev environment and the MCP server handles the details of API authentication, making requests, and response parsing.
Set up your own MCP integration: A step-by-step guide
Want to give my MCP package a spin? Follow along below! My MCP server is open-sourced, so also I welcome folks to contribute or fork their own versions specific to their needs 🙂.
1. Install the
hex-mcp
Package
Using
uv
(recommended for a cleaner environment):
Copy
bash
Copy
uv add hex-mcp
Or with traditional pip:
Copy
pip install hex-mcp
Verify the installation:
Copy
hex-mcp --version
# Should show: hex-mcp version 0.1.10 (or newer)
2. Configure your workspace key
Set up your
Hex API key
:
Copy
hex-mcp config --api-key YOUR_HEX_API_KEY
# Configuration saved to ~/.hex-mcp/config.yaml
This saves your API key in your home directory, making it accessible across projects without environment variable hassles.
3. Install MCP in your project
In your project directory, run:
Copy
hex-mcp install
# MCP configuration installed to .cursor/mcp.json
This creates the necessary configuration file that Cursor uses to discover and interact with the MCP server.
4. Start using it in your dev environment
Open your project in Cursor, activate the AI pane, and start asking questions about your Hex projects! Try prompts like:
"Find my HubSpot data integration project."
"Run the weekly sales dashboard project."
"Is my customer churn analysis project done running?"
The future of observability and governance
This integration between Hex and Cursor through MCPs represents just the beginning of a broader shift in how data teams can take advantage of AI. My team no longer has to jump from one context to another — our development workflow is more streamlined and our interaction with Hex as a platform is much more enjoyable.
With expanding product API access (spoiler: Hex is working on this!) — you can imagine observability and governance to be far easier. Imagine a world, where, with just natural language you could:
Handle project lifecycle management at scale — automatically archiving or deleting projects based on specified rules
Do bulk handling of user and group permissions
Create and modify data connections
This list goes on! By using MCPs, now much of the painful and tedious administrative tasks can be handled with a prompt — lowering the barrier to entry and improving Hex usability for everyone on our team.
Want to contribute or explore more? Check out
my GitHub repository
for the Hex MCP implementation or dive into the
Model Context Protocol specification
to learn how you can customize an MCP for your team!
PSA from Olivia: At Hex we're excited to expand our public API coverage — making it easier than ever to manage your Hex instance at scale (and especially with the help of LLMs!). We’re looking for design partners for these changes so if you're interested in providing API feedback for better workspace management please reach out at magic [at] hex.tech.
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
