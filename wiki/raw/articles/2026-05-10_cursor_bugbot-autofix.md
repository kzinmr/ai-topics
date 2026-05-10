---
title: "Closing the code review loop with Bugbot Autofix · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/bugbot-autofix"
scraped: "2026-05-10T01:19:39.740379+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Closing the code review loop with Bugbot Autofix · Cursor

**Source**: [https://cursor.com/blog/bugbot-autofix](https://cursor.com/blog/bugbot-autofix)

Blog
/
product
Feb 26, 2026
·
product
Closing the code review loop with Bugbot Autofix
Jon Kaplan
·
3 min read
Agents are now tackling more ambitious tasks, generating thousands of lines of code, and
controlling their own computers
to demo their work. Today, we're extending these capabilities to Bugbot, our code review agent.
Bugbot can now find and automatically fix issues in PRs. Bugbot Autofix spawns cloud agents that work independently in their own virtual machines to test your software. Over 35% of Bugbot Autofix changes are merged into the base PR.
Autofix is now out of beta and available to all Bugbot users. Once enabled, the PRs Bugbot reviews will include proposed fixes to give you a jumpstart on code review.
#
Resolving more bugs per PR
We’ve
continued to
invest
in Bugbot’s effectiveness at identifying issues while optimizing for bugs that get fixed.
The average number of issues identified per run has nearly doubled in the last six months, while the resolution rate (i.e., percentage of bugs resolved by users before the PR is merged) has increased from 52% to 76%. This means Bugbot is catching more bugs and flagging fewer false positives.
#
What's next
Bugbot Autofix is an early example of agents running automatically based on an event like PR creation. Next, we are working on giving teams the ability to configure custom automations for workflows beyond code review.
We’re also focused on enabling Bugbot to verify its own findings, conduct deep research on complex issues, and continuously scan your codebase to catch and resolve bugs.
Get started by enabling Bugbot Autofix in your
Bugbot dashboard
. Or learn more in our
docs
.
Filed under:
product
Author
:
Jon Kaplan
