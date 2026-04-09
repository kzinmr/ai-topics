---
title: "Anthropic built a model too risky to release"
url: "https://substack.com/app-link/post?publication_id=4379299&post_id=193659390&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTM2NTkzOTAsImlhdCI6MTc3NTc0MDI0NywiZXhwIjoxNzc4MzMyMjQ3LCJpc3MiOiJwdWItNDM3OTI5OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.qRpzESzm3_5YDUyryXJiJ6iQVtfa4mflr9LOzy2kLBE"
fetched_at: 2026-04-09T14:50:55.793604+00:00
source_date: 2026-04-09
tags: [newsletter, auto-ingested]
---

# Anthropic built a model too risky to release

Source: https://substack.com/app-link/post?publication_id=4379299&post_id=193659390&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTM2NTkzOTAsImlhdCI6MTc3NTc0MDI0NywiZXhwIjoxNzc4MzMyMjQ3LCJpc3MiOiJwdWItNDM3OTI5OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.qRpzESzm3_5YDUyryXJiJ6iQVtfa4mflr9LOzy2kLBE

Hey folks, Keshav here. Ben is at AI Engineer this week, so I’m covering the intro.
A mis-timed blog last week leaked Anthropic’s next model - Claude Mythos. Well, it is real and has massive improvements on benchmarks over Opus 4.6:
but we are not getting access to it anytime soon. Why? because it is really good at finding and exploiting software vulnerabilities. On Firefox exploit generation, Opus managed 2 working exploits out of hundreds of attempts. Mythos hit 181.
It found many-decades-old bugs in critical software projects like OpenBSD (27-year-old bug), FFmpeg (16-year-old bug) and more.
Instead of releasing it publicly, Anthropic is giving 12 companies access to a preview version of Mythos under “
Project Glasswing
” to find vulnerabilities in critical software. Anthropic is committing $100M in model usage credits and $4M in donations to open-source security orgs under this project.
Theo made a
video
on this, and I like his point:
“Mythos is to Opus what Opus is to Sonnet.”
I tweeted a
list of companies that Meta has acquired
in the past year without anything to show for it, and soon after, Meta released details about their latest model -
Muse Spark
. At a glance, it sits somewhere between Sonnet 4.6 and Opus 4.6. Not usable yet: API access is coming, and there are promises about open-source too (rip llama).
Many people are dunking on Meta for its not-so-frontier model release after spending billions and a year of silence, but I think it’s a good step ahead. Plus, have you used Instagram search over the past couple of months? It’s gotten really good courtesy of AI.
As always, good recap from Ethan Mollick on the
state of frontier models
: Google, OpenAI and Anthropic lead, Meta joins the pack for now while xAI has fallen off, and the best Chinese models are still 7-9 months behind.
ps:
Factory’s desktop app
is now out of beta. It comes with a cloud computer, the ability to use other apps on your device, and, of course, the ability to run and manage multiple Droid sessions easily.
Ben’s Bites is brought to you by
Attio
, the AI CRM
Honestly, no one gets excited about a CRM. But then they try
Attio
. It connects to Claude Code and n8n through its MCP server, completely bridging the gap between my customer data and apps. Wait, there's more, like flagging churn risk and turning customer feedback into Linear projects.
Try it now
.
Chronicle
:
Cursor for slides
. Never build a deck from scratch again. Turn ideas into stunning presentations in minutes.*
OpenRouter Spawn
- Deploy OpenClaw and other agents to the cloud of your choice. Works with all models on OpenRouter.
Zapier’s SDK is now open to everyone
. Programmatic access to all of Zapier’s capabilities. Free to use in beta. (
docs
)
Kiro.dev
(spec-driven IDE from Amazon) is bringing its
startup credits program
back for startups with up to 30 people.
Cogito
- Markdown editor for Mac. I’ve been using Clearly (
recently updated
) for the last few weeks to simply view and edit md files.
Graphify
- Turn any codebase or folder into a queryable knowledge graph.
Pi and Mario
(the maker of Pi) are joining Earendil, the company by the creator of Flask. The core harness stays open-source. New features will be a mix of enterprise & fair source (proprietary now, open-source later).
Impeccable
- Free design skills for coding agents with 21 commands to audit and fix common mistakes.
Superset
and
Builder 2.0
- two new UIs for running parallel agents. Superset is more like Codex (terminal-first, worktrees), Builder is more kanban-style with Slack/Jira integration.
CSS Studio
by Motion - Make design changes by hand on your website in the browser, then pass them over to your agent for implementation.
S3 Files from AWS
allows storing data as a file system, making it easier for agents to use.
Every is running two parallel org charts
- one for humans and another for each employee’s openclaw agents.
Today we're announcing the Billion Dollar Build.

An 8-week competition where teams will use Perplexity Computer to build a company with a path to $1B.

Finalists have the opportunity to secure up to $1M in investment from the Perplexity Fund and up to $1M in Computer credits.
5:20 PM · Apr 8, 2026
·
1.35M Views
225 Replies
·
446 Reposts
·
3.73K Likes
Quick  demo — generating multiple design ideas to choose from, no matter what tech stack you use:
8:34 PM · Apr 8, 2026
·
160K Views
139 Replies
·
112 Reposts
·
2.17K Likes
Introducing Expect

Test your agent code in a real browser

Works with your agent. Fully open source
4:00 PM · Apr 8, 2026
·
52.6K Views
27 Replies
·
30 Reposts
·
688 Likes
New Skill: Email Emulation

Test magic links, verification codes w/o sending real emails

→ Send via the Resend SDK
→ Retrieve emails from a local inbox
→ Extract codes to complete auth flows
→ One env var to reroute traffic

npx skills add vercel-labs/emulate --skill resend
11:07 PM · Apr 7, 2026
·
78.4K Views
26 Replies
·
48 Reposts
·
1.07K Likes
Share Ben's Bites
* sponsors who make this newsletter possible :)
Wanna partner with us for the next quarter?
