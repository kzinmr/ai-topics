---
title: "Extend Cursor with plugins · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/marketplace"
scraped: "2026-05-10T01:19:40.422185+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Extend Cursor with plugins · Cursor

**Source**: [https://cursor.com/blog/marketplace](https://cursor.com/blog/marketplace)

Blog
/
product
Feb 17, 2026
·
product
Extend Cursor with plugins
6 min read
Table of Contents
↑
Plugins for the full development lifecycle
Build and share your own plugins
Coming soon
Cursor now supports plugins, allowing agents to connect to external tools and learn new knowledge. Plugins bundle capabilities like MCP servers, skills, subagents, rules, and hooks that extend agents with custom functionality.
We’re starting with a highly curated set from partners such as Amplitude, AWS, Figma, Linear, and Stripe. These plugins span the product development lifecycle, allowing Cursor to deploy services, implement payments, run advanced testing, and more.
You can discover and install prebuilt plugins on the
Cursor Marketplace
or create your own and
share them
with the community.
#
Plugins for the full development lifecycle
Plugins allow Cursor to more effectively use the tools your team already relies on. This lets you orchestrate the entire product development lifecycle in the same place you generate code.
#
Plan and design
Access issues, projects, and documents with the
Linear plugin
.
Translate designs into code with the
Figma plugin
.
#
Subscriptions and payments
Build payment integrations with the
Stripe plugin
.
The Stripe plugin lets Cursor understand how Stripe integrations should be built. It created the products, prices, and payment link using Stripe's APIs, then shipped a working app almost immediately. It's a much faster way to build and test Stripe integrations.
Gus Nguyen
Senior Software Engineer
,
Stripe
#
Services and infrastructure
Deploy and manage infrastructure in Cursor with the
AWS
,
Cloudflare
, and
Vercel
plugins.
Cursor now knows our React best practices and can deploy to preview or production directly from the editor.
Elliot Dauber
Software Engineer
,
Vercel
#
Data and analytics
Query production data and surface insights with the
Databricks
,
Snowflake
,
Amplitude
, and
Hex
plugins.
With the Amplitude plugin, Cursor can pull in rich behavioral context, analyze growth dashboards, synthesize customer feedback, and turn those insights into concrete recommendations. I can even have Cursor draft a PR immediately.
Frank Lee
Principal Product Manager
,
Amplitude
#
Build and share your own plugins
You can also build your own plugins and share them on the Cursor Marketplace. A plugin combines one or more primitives that agents use to execute tasks:
Skills
: domain-specific prompts and code that agents can discover and run
Subagents
: specialized agents that allow Cursor to complete tasks in parallel
MCP servers
: services that connect Cursor to external tools or data sources
Hooks
: custom scripts that let you observe and control agent behavior
Rules
: system-level instructions to uphold coding standards and preferences
We’re accepting
plugin submissions
and look forward to seeing what the community builds. We’ve also published some Cursor-built plugins. Check out the
Cursor Team Kit
to install our favorite internal workflows for CI, code review, and testing.
#
Coming soon
We're working on private team marketplaces so organizations can share plugins internally with central governance and security controls.
Learn more about plugins in our
docs
.
Filed under:
product
Author
:
Cursor Team
