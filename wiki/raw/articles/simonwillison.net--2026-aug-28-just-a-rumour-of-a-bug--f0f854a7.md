---
title: "Just a rumour of a bug is enough to find a security exploit these days"
url: "https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/"
fetched_at: 2026-08-29T10:01:01.358301+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Just a rumour of a bug is enough to find a security exploit these days

Source: https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/

28th August 2026 - Link Blog
Just a rumour of a bug is enough to find a security exploit these days
(
via
) Anil Madhavapeddy is a professor of computer science at Cambridge and a core maintainer of the OCaml compiler. In this somewhat alarming post he reports that security issues in OCaml projects are seeing evidence of attempted exploits within minutes of patches being shared for discussion:
This normally takes a few days and a release within a week or two is reasonable. Within about ten minutes (!) this website was fielding probes for percent-encoded traversal sequences, indicating that automated watchers are keeping an eye on public repositories.
Modern coding agents have become so effective at finding flaws that the slightest hint at a new bug can be enough information for them to find it, something Anil has been able to demonstrate using his own agents, switching to DeepSeek V4 Pro⁠ when Claude Fable refused the task.
Anil points out that this rate of discovery appears incompatible with existing open source embargo practices for new issues. If an issue can become an exploit this fast, we need to figure out new processes for keeping our communities safe.
rclone maintainer Nick Craig-Wood
confirms in the Hacker News comments
that his project is seeing this problem:
In the first 10 years of the rclone project we received about 20 security disclosures through GitHub. We had to deal with over 40 in the last month! That has taken a huge amount of my time, even using AI tools to triage and come up with fixes for review.
The hit rate for those security disclosures is pretty good - about 75% of them have a nugget of something which needs looking at. [...]
GitHub assigns CVEs for the advisories. Before the AI apocalypse they took 2-3 days for an assignment but now it they are running at 3-4 weeks so I have to send the point releases out with CVE-PENDING in the changelog which isn't ideal.
