---
title: "How Harvey is Building a Frontier Marketing Org"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/how-harvey-is-building-a-frontier-marketing-org"
scraped: "2026-10-22T06:00:15.931452+00:00"
lastmod: "2026-10-21T17:00:00.000Z"
type: "sitemap"
---

# How Harvey is Building a Frontier Marketing Org

**Source**: [https://www.harvey.ai/blog/how-harvey-is-building-a-frontier-marketing-org](https://www.harvey.ai/blog/how-harvey-is-building-a-frontier-marketing-org)

We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
Company
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Agents
→
Purpose built agents execute complex legal work end to end.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Spaces
→
Work with legal teams across organizations in secure, shared spaces.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
Horizon Scanning
→
Track, assess, and take action on regulatory changes.
Intake
New
→
Capture, route, and resolve legal Intake from across the business.
Connector Library
New
→
Bring your team’s tools into Harvey with security-reviewed connectors or custom MCP.
Legal Work Orchestration
New
→
Assign, execute, and review legal work with agents and your team.
Overview
For In-House
→
For Law Firm
→
For Mid-size Firm
→
Industries
Healthcare & Life Sciences
→
Energy & Utilities
→
Technology
→
Media, Entertainment & Telecom
→
Practice Area & Teams
Litigation
→
Transactional
→
Innovation
→
A New Era of Collaboration for Legal and Professional Services
→
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Blog
→
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
→
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
→
Resources for maintaining a uniform and professional presentation of the Harvey brand.
Research
→
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
→
Who we are and what we're building.
Careers
→
Join our team and help Harvey shape the future of professional services.
Newsroom
→
Press releases and partnership announcements.
2025 Year in Review
→
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Login
Request a Demo
Platform
Overview
A unified view of how Harvey's products work together to support your entire practice.
Agents
Purpose built agents execute complex legal work end to end.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Spaces
Work with legal teams across organizations in secure, shared spaces.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
Horizon Scanning
Track, assess, and take action on regulatory changes.
Intake
New
Capture, route, and resolve legal Intake from across the business.
Connector Library
New
Bring your team’s tools into Harvey with security-reviewed connectors or custom MCP.
Legal Work Orchestration
New
Assign, execute, and review legal work with agents and your team.
Solutions
Overview
For In-House
For Law Firm
For Mid-size Firm
Industries
Healthcare & Life Sciences
Energy & Utilities
Technology
Media, Entertainment & Telecom
Practice Area & Teams
Litigation
Transactional
Innovation
A New Era of Collaboration for Legal and Professional Services
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Customers
Security
Resources
Blog
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
Resources for maintaining a uniform and professional presentation of the Harvey brand.
Research
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
About
Who we are and what we're building.
Careers
Join our team and help Harvey shape the future of professional services.
Newsroom
Press releases and partnership announcements.
2025 Year in Review
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Request a Demo
Login
US
EU
AU
Technical
How Harvey is Building a Frontier Marketing Org
Harvey’s marketing team built an agent-powered creative system combining brand guidelines, reusable Figma libraries, and parallel workflows to turn ambitious ideas into repeatable work at scale.
by
Shawn Farsai
and
Gabe Pereyra
•
Oct 21, 2026
Recently, Figma asked us what Harvey was building with its MCP server. This is the long answer.
Between the MCP and better frontier models, agents now run whole design projects end to end across our brand, product marketing, and design work. Here’s what that looks like, and the systems underneath it.
Building a Launch Film With Agents
Watch Video
We made this launch film for Harvey Artifacts entirely with agents, inside of Figma. The agent built every scene as a Figma Motion frame, keyed every camera move, UI state, and line of type on its timeline, and exported the cuts straight from the file.
It all started with a storyboard, which is to a film what a PRD is to code: it sits between the creative brief and production, so every shot, line, and transition is decided up front. That forces the model, and us, to be deliberate about every choice.
We review on the canvas, sometimes 50 comments at a time. The agent reworks the board after each pass and asks which notes should become rules. For music, we marked where the beat should drop and it retimed every scene to the track. When the ending fell flat, it cut and EQ’d the track, added sound design, and laid out four or five ways the outro could land.
Figure 1. The Artifacts storyboard in Figma. Each version is a full board of labeled scenes, with side studies for the ending and the “Share the Work” beat.
Tailoring a Demo for Every Account
Anyone can get one flashy demo out of an agent. The hard part is scale, so we picked a sales problem: a tailored product film for each of the hundreds of accounts we want to win. Our first prompts came back half decent, and 15 to 20 minutes of back-and-forth got each one into shape. But that wouldn’t scale.
So we set out to build a strong foundation in Figma, in two parts. Agents crawled the whole app, clicked every button, and rebuilt all key screens as components, which became Product Map. Then, in Figma Motion, they worked out the grammar of a product film, from camera pushes to screen handoffs to a steady click rhythm, which became Motion Primitives. Both are covered below.
With both in place, we worked with the agent to build a menu of 44 company-agnostic demo flows, each built around one moment buyers ask to see, like a playbook redline in Word. For each account, agents use Enterpret's MCP to pull together Gong calls, Salesforce win-loss reports, and Slack. An agent then writes the script, with a fictional company on screen, and voices it as Ashleigh Whittaker, our narrator, whose voice we built in ElevenLabs from ten minutes of her footage.
Figure 2. The demo menu in Figma: 44 flows in 13 categories, from Contract Work and Litigation to Memory and Word and Outlook, with one of the sticky notes Shawn and Claude used to work through changes.
Making Hundreds Overnight
An engine of about 750 lines of JavaScript turns each script into a film inside Figma. Each film is a short list of beats, and the engine handles the camera, transitions, captions, the pointer’s click rhythm, and the end card. Then it lays out contact sheets of the finished film and flags clipped text, small type, and stray pointers, so the obvious mistakes are caught before anyone watches.
Lots of small things pop up at scale. Like only one agent can work in a file at a time, so agents queuing in one shared file pushed calls to two minutes and timed out. We built a bus to run them in parallel: three lane files, each with its own builder agent, plus a coordinator for export, mixing, and delivery. One batch of 36 films took 69 minutes, and when we hit our daily Figma call cap, overnight agents scripted and voiced the next 97.
Hundreds of films also mean a lot of people to coordinate. So everything runs through one tracker, a Claude artifact that every agent and person reads and writes. Each film has a row with its account, story, status, and links, and agents update their own rows as they build, export, and deliver.
Figure 3. The tracker, a Claude artifact, on its QA Batch tab: the 20-film sample for legal engineering, chosen to cover every common flow. Accounts and names are fictional stand-ins.
Agentic Brand Guidelines
We think about our Figma the way engineers think about a codebase. Our Agentic Brand Guidelines are the top-level AGENTS.md, and everything above runs on them. Each project is a folder with its own AGENTS.md page that adds only what it needs, and Agentic Brand Guidelines tell agents how to set one up with its own context and changelog. It’s progressive disclosure for creative work: an agent reads the brand, then the project, then only what its task needs.
We started with markdown files, and for design tokens they work fine. Everyone has their colors and type in a file somewhere. Markdown breaks one step up, when you try to explain how to make a chart for a blog post or structure a long-form PDF guide. A picture really is worth a thousand words: most of a design lives in the relationships between elements, and words describe those badly. So our Agentic Brand Guidelines became a Figma library, from foundations up to templates with worked examples, where agents see those relationships instead of reading about them.
Figure 4. Color primitives with their rules beside them: mostly Ink and Ivory, secondaries as accents, data colors only for charts, no gradients. The type scale, with every Harvey Serif and Harvey Sans style as a Figma text style.
Layout is where Figma beat HTML canvases for us. Designers work with grids the web was never built for: modular, baseline, compound, and hierarchical grids. We tried to get agents there in HTML, even building a layout engine on top of
Pretext
, but browsers set type in line boxes padded by the font’s ascent and descent, so a headline’s cap height never sits exactly on a grid line. Figma trims text to cap height and baseline, hangs punctuation, and holds each grid as a layout agents apply.
Product Map and Motion Primitives
Our product is designed in a lot of places now. Product designers are more productive than ever, but some work is vibe coded and some lives in Figma, spread across many files. We needed one source of truth an agent could reference and maintain.
Product Map
is that source, published to our Figma org as a library, so any video that needs the product pulls it from there instead of redrawing it.
Figure 5. Product Map: every key Harvey screen rebuilt in Figma and grouped by area, from Home and Agents to Drafting and Review Tables.
Motion was the other gap. Films kept animating the same pieces from scratch, and with little differences. So we built
Motion Primitives
, a library of animated parts that’s also published to our Figma org, down to product moves like redlines arriving in a document. We made sure the product pieces are exactly right, and a fix to one component reaches every film that uses it.
Figure 6. Motion Primitives in Figma: title cards, lower thirds, text animators and product moves, each built once and reused in every film.
ElevenLabs
Every line of voiceover in our films comes from ElevenLabs. Agents call it through its MCP, and our voice library already holds clones of our narrator and of teammates from their interviews, each built from a short clip of footage. We’re excited to try more of what ElevenLabs offers to make our content even better.
Figure 7. Our ElevenLabs voice library, with clones of our narrator and teammates at the top.
Figma Weave
Figma Weave does for images and video what ElevenLabs does for voice. It’s a canvas for chaining image and video models into workflows, and it’s now part of Figma, so our agents reach it through the same MCP they design with. When a frame calls for a photo, a texture, or a shot, the agent runs a model or one of our saved Weave workflows and places the result straight in the Figma file. Our Agentic Brand Guidelines spell out the art direction, so that the agent can easily pick whichever model and workflow in Weave gets the best result.
Figure 8. A grid of Weave generations
Multiplayer Creative Work With Spectre
Spectre is our internal agent platform. Engineers use it to run coding agents and our sales team uses it as a data agent. Shawn and Joey from our dev tools team pointed it at the brand repo and Figma files, and it became a creative agent that works in a Slack channel. Someone tags it on a request, and it does the work in Figma, then replies with what it made, what it changed, and which decisions to check.
We think this is what multiplayer design looks like now. It used to mean several designers in one file. Now the people who own the work in product, legal, sales, and marketing give direction in the Slack thread where they already work, while an agent makes the changes in Figma and everyone watches the work move.
Figure 9. A thread in Spectre’s Slack channel: a request to put blog graphics on brand, feedback from the team, and Spectre queuing each change.
Telling Harvey’s Story at Scale
So that’s the long answer to Figma’s question. In the last 14 days alone, Shawn has used 15.6B tokens across Figma, ElevenLabs, and Weave. All signs point to this only growing. Designers are starting to scale their token use the way engineers have over the last four years, and MCP is what makes that possible.
That’s letting us be far more ambitious with our marketing, from a launch film made entirely in Figma to a tailored product video for every account we want to win. As the models get better, so does what a team our size can make.
Next Up
Building Harvey’s MCP Policy Engine
How We Built Harvey’s Connector Library to Work Across External Tools
How We Rebuilt Playbook Review as a Multi-Agent System
Unlock Professional Class AI for Your Organization
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Overview
→
Agents
→
Vault
→
Knowledge
→
Spaces
→
Command Center
→
Contract Intelligence
→
Horizon Scanning
→
Ecosystem
→
Intake
→
Partnerships
→
Solutions
Innovation
→
Transactional
→
Litigation
→
In-House
→
Law Firms
→
Mid-Sized Firms
→
Healthcare & Life Sciences
→
Energy & Utilities
→
Technology
→
Media, Entertainment & Telecom
→
Company
Customers
→
Security
→
About
→
Careers
→
Newsroom
→
Law Schools
→
Resources
Blog
→
Resources Hub
→
Harvey Academy
→
Help Center
→
Legal
→
Privacy Policy
→
Press Kit
→
Your Privacy Choices
→
Follow
X
→
LinkedIn
→
YouTube
→
Instagram
→
Copyright © 2026 Harvey AI Corporation. All rights reserved.
