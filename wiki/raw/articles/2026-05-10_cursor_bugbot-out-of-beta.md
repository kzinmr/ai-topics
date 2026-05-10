---
title: "Bugbot is out of beta · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/bugbot-out-of-beta"
scraped: "2026-05-10T01:19:48.958007+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Bugbot is out of beta · Cursor

**Source**: [https://cursor.com/blog/bugbot-out-of-beta](https://cursor.com/blog/bugbot-out-of-beta)

Blog
/
product
Jul 24, 2025
·
product
Bugbot is out of beta
Jon Kaplan, Lee Danilek & Rohan Varma
·
3 min read
We're excited to release Bugbot, our code review agent that automatically analyzes your changes to find logic bugs, edge cases, and security issues before they make it into production.
We built Bugbot for ourselves to help us review our PRs and it has since become a core tool as we continue to build Cursor.
To get started, go to
the Bugbot tab in your Cursor dashboard
.
Issues detected by Bugbot are commented in the PR, right where they're found
#
How Bugbot works
Bugbot runs automatically on your PRs and gathers context from your changes to truly understand the intent of the code. We use the best available models along with our own techniques to find meaningful bugs while keeping the false positive rate low.
With
Bugbot rules
(
BUGBOT.md
), you can also guide reviews using custom knowledge about your codebase. When Bugbot flags an issue, you can send it to Cursor or launch a background agent on the web with one click.
#
Results during beta
During Bugbot's short beta, it has already reviewed over 1 million PRs and found over 1.5 million issues. Perhaps most importantly, over 50% of identified bugs are resolved by the time the PR is merged.
Bugbot beta results showing over 1 million PRs reviewed
We've worked closely with several companies that have deployed Bugbot across their teams. Here's what engineering leaders have to say:
Bugbot helps give back 40% of time spent on code reviews. It's helping our top engineers hold the line on quality while keeping up with shipping pace.
Ankur Bhatt
Head of AI Engineering
,
Rippling
The hit rate from Bugbot is insane. Catching bugs early saves huge downstream cost. Bugbot slotted perfectly into our flow.
David Cramer
Co-Founder & CPO
,
Sentry
Bugbot blew us away with the nuance of bugs it was catching. It's incredibly strong at reviewing AI-generated code and gives us confidence in quality.
Vijay Iyengar
AI Engineering Leader
,
Sierra
Our resolution rate with Bugbot is over 50%. Bugbot finds real bugs after human approval. Avoiding one sev pays for itself.
Kodie Goodwin
AI Engineering Leader
,
Discord
See an overview of your PRs and Bugbot statistics in the Cursor dashboard.
We've come to rely on Bugbot for our own code reviews, and we're excited to see what it does for your teams.
Filed under:
product
Author
s
:
Jon Kaplan, Lee Danilek & Rohan Varma
