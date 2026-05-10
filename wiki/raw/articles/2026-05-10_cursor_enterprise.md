---
title: "Introducing Cursor for Enterprise · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/enterprise"
scraped: "2026-05-10T01:19:45.195081+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Introducing Cursor for Enterprise · Cursor

**Source**: [https://cursor.com/blog/enterprise](https://cursor.com/blog/enterprise)

Blog
/
product
Oct 31, 2025
·
product
Introducing Cursor for Enterprise
5 min read
Table of Contents
↑
Hooks
Team Rules
Upgraded Analytics
Audit Log
Sandbox Mode
Working with our team
Cursor is used by tens of thousands of enterprises, including Salesforce, NVIDIA, and PwC, to accelerate product velocity and build durable software.
To further support enterprise teams, we’re launching new features that make Cursor’s coding agents more capable, transparent, and secure.
#
Hooks
Hooks
allow you observe, control, and extend the agent loop using custom scripts.
{
"version"
:
1
,
"hooks"
: {
"beforeSubmitPrompt"
: [
{
"command"
:
"./audit.sh"
}
],
"beforeShellCommand"
: [
{
"command"
:
"./audit.sh"
},
{
"command"
:
"./allowlist.sh"
}
]
}
}
Integrating Cursor Hooks with our engineering intelligence platform gives us a better sense of how AI is affecting developer productivity throughout the software development lifecycle, and gives engineering leaders the insights they need to make smarter decisions.
Rebecca Fitzhugh
Lead Principal Engineer
,
Atlassian
Hooks can:
Add observability:
Log agent actions, tool calls, prompts, and completions for future analysis.
Control the full agent loop:
Enforce compliance policies, block unapproved commands, and scrub secrets or proprietary code in real time.
Extend Cursor with code:
Connect external systems, inject context, or trigger automations.
Hooks can be distributed through MDM or with
Cursor’s cloud option
.
#
Team Rules
Team Rules
bring shared context and best practices to every developer in your organization.
Team Rules make it easy for our agents to stay aligned with how we build at Duolingo. They guide developers toward the right patterns automatically, so we spend less time fixing and more time shipping.
Sarah Deitke
Software Engineer
,
Duolingo
Rules can standardize API schemas, enforce conventions, or teach common workflows. Admins can choose to recommend or require rules from the
cloud dashboard
.
#
Upgraded Analytics
We’ve
rebuilt our analytics
to give leaders data about how their teams use AI:
See daily activity and top users at a glance
Data on CLI, Background Agent, and Bugbot adoption
View percentage of AI lines of code on the commit level
Filter data by Active Directory group
Exportable replication data per visualization (via API or CSV)
Data updates every two minutes instead of every 24 hours
The new usage leaderboard has already helped us surface power users and learn how they work. The cleaner dashboard makes the data easier to trust and act on.
Nicolas Arkhipenko
Senior Director of AI Platforms & Developer Productivity
,
Salesforce
The upgraded dashboard is generally available today, with data from August 27th for all clients 1.7 and later.
#
Audit Log
Audit Log
gives administrators full visibility into every key event on the platform from security changes to rule updates.
It currently tracks 19 event types covering access, asset edits, and configuration updates.
Audit Log data is available in the web dashboard and can be exported as a CSV.
#
Sandbox Mode
Sandbox Mode
executes agent terminal commands in a restricted environment to enable faster and safer iteration.
By default, the sandbox blocks network access, limiting file access to the workspace and
/tmp/
.
If a command fails due to restrictions, the user can skip it or choose to re-run outside the sandbox.
Enterprise Admins have
control
over sandbox availability and team-wide git and network access.
#
Working with our team
We want to make Cursor the best place for teams building with AI. Many of these features were inspired by the work we're already doing with many of the most innovative companies in the world, and we’d like to
build with yours
.
Filed under:
product
Author
:
Cursor Team
