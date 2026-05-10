---
title: "Introducing Debug Mode: Agents with runtime logs · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/debug-mode"
scraped: "2026-05-10T01:19:44.246131+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Introducing Debug Mode: Agents with runtime logs · Cursor

**Source**: [https://cursor.com/blog/debug-mode](https://cursor.com/blog/debug-mode)

Blog
/
product
Dec 10, 2025
·
product
Introducing Debug Mode: Agents with runtime logs
Alexey Kozy & Albert Slepak
·
6 min read
Table of Contents
↑
Describe the bug
Reproduce the bug
Verify the fix
Coding agents are great at lots of things, but some bugs consistently stump them. That's why we're introducing Debug Mode, an entirely new agent loop built around runtime information and human verification.
To build it, we examined the practices of the best debuggers on our team. We rolled their workflows into an agent mode, equipping it with tools to instrument code with runtime logs, prompts that generate multiple hypotheses about what's going wrong, and the ability to call back to you to reproduce the issue and verify fixes.
The result is an interactive process that reliably fixes bugs that were previously beyond the reach of even the smartest models working alone, or could take significant developer time to address.
#
Describe the bug
To get started, select Debug Mode from the dropdown menu and describe the bug in as much detail as you can.
Instead of immediately trying to generate a fix, the agent reads through your codebase and generates multiple hypotheses about what could be wrong. Some will be ideas you would have thought of on your own, but others will likely be approaches you wouldn't have considered.
The agent then instruments your code with logging statements designed to test these hypotheses. This prepares the agent to receive concrete data about what's actually happening when the bug occurs.
#
Reproduce the bug
Next, go to your application and reproduce the bug while the agent collects the runtime logs.
The agent can see exactly what's happening in your code when the bug occurs: variable states, execution paths, timing information. With this data, it can pinpoint the root cause and generate a targeted fix. Often that's a precise two or three line modification instead of the hundreds of lines of speculative code you'd have received with a standard agent interaction.
#
Verify the fix
At this point, Debug Mode asks you to reproduce the bug one more time with the proposed fix in place. If the bug is gone, you mark it as fixed and the agent removes all the instrumentation, leaving you with a clean, minimal change you can ship.
This human-in-the-loop verification is critical. Sometimes bugs are obvious, but other times they fall into a gray area where the fix might work technically but not feel right. The agent can't make that call on its own. If you don't think the bug is fixed, the agent adds more logging, you reproduce again, and it refines its approach until the problem is actually solved.
This kind of tight back-and-forth is one way we think AI coding works best. The agent handles the tedious work while you make the quick decisions that need human judgment. The result with Debug Mode is that tricky bugs that used to be out of reach are now reliably fixed.
Read the
Debug Mode docs
. Learn about all the new features in
Cursor 2.2
.
Filed under:
product
Author
s
:
Alexey Kozy & Albert Slepak
