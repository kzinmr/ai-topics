---
title: "Building a better Bugbot · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/building-bugbot"
scraped: "2026-05-10T01:19:43.157841+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Building a better Bugbot · Cursor

**Source**: [https://cursor.com/blog/building-bugbot](https://cursor.com/blog/building-bugbot)

Blog
/
research
Jan 15, 2026
·
research
Building a better Bugbot
Jon Kaplan
·
7 min read
Table of Contents
↑
Humble beginnings
From prototype to production
Measuring what matters
Hill-climbing
Agentic architecture
What's next
As coding agents became more capable, we found ourselves spending more time on review. To solve this, we built
Bugbot
, a code review agent that analyzes pull requests for logic bugs, performance issues, and security vulnerabilities before they reach production. By last summer, it was working so well that we decided to
release
it to users.
The process of building Bugbot began with qualitative assessments and gradually evolved into a more systematic approach, using a custom AI-driven metric to hill-climb on quality.
Since launch, we have run 40 major experiments that have increased Bugbot's resolution rate from 52% to over 70%, while lifting the average number of bugs flagged per run from 0.4 to 0.7. This means that the number of resolved bugs per PR has more than doubled, from roughly 0.2 to about 0.5.
We released Version 1 in July 2025 and Version 11 in January 2026. Newer versions caught more bugs without a comparable rise in false positives.
#
Humble beginnings
When we first tried to build a code review agent, the models weren't capable enough for the reviews to be helpful. But as the baseline models improved, we realized we had a number of ways to increase the quality of bug reporting.
We experimented with different configurations of models, pipelines, filters, and clever context management strategies, polling engineers internally along the way. If it seemed one configuration had fewer false positives, we adopted it.
One of the most effective quality improvements we found early on was running multiple bug-finding passes in parallel and combining their results with majority voting. Each pass received a different ordering of the diff, which nudged the model toward different lines of reasoning. When several passes independently flagged the same issue, we treated it as a stronger signal that the bug was real.
After weeks of internal qualitative iterations, we landed on a version of Bugbot that outperformed other code review tools on the market and gave us confidence to launch. It used this flow:
Run eight parallel passes with randomized diff order
Combine similar bugs into one bucket
Majority voting to filter out bugs found during only one pass
Merge each bucket into a single clear description
Filter out unwanted categories (like compiler warnings or documentation errors)
Run results through a validator model to catch false positives
Dedupe against bugs posted from previous runs
#
From prototype to production
To make Bugbot usable in practice, we had to invest in a set of foundational systems alongside the core review logic. That included making repository access fast and reliable by rebuilding our Git integration in Rust and minimizing how much data we fetched, as well as adding rate-limit monitoring, request batching, and proxy-based infrastructure to operate within GitHub's constraints.
As adoption grew, teams also needed a way to encode codebase-specific invariants like unsafe migrations or incorrect use of internal APIs. In response, we added
Bugbot rules
to support those checks without hardcoding them into the system.
Together, these pieces made Bugbot practical to run and adaptable to real codebases. But they didn't tell us whether quality was actually improving. Without a metric to measure progress, we couldn't quantitatively assess Bugbot's performance in the wild, and that put a ceiling on how far we could push it.
#
Measuring what matters
To solve this problem, we devised a metric called the resolution rate. It uses AI to determine, at PR merge time, which bugs were actually resolved by the author in the final code. When developing this metric, we spot-checked every example internally with the PR author and we found that the LLM correctly classified nearly all of them as resolved or not.
Teams often ask us how to assess the impact Bugbot is having for them, so we surface this metric prominently in the
dashboard
. For teams evaluating effectiveness, it's a much clearer signal than anecdotal feedback or reactions on comments. Resolution rate directly answers whether Bugbot is finding real issues that engineers fix.
The Bugbot dashboard showing a team's resolution rate over time and other key metrics.
#
Hill-climbing
Defining resolution rate changed how we built Bugbot. For the first time, we could hill-climb on the basis of real signal, rather than just feel. We began evaluating changes online using actual resolution rates and offline using BugBench, a curated benchmark of real code diffs with human annotated bugs.
We ran dozens of experiments across models, prompts, iteration counts, validators, context management, category filtering, and agentic designs. Many changes, surprisingly, regressed our metrics. It turned out that a lot of our initial judgments from the early qualitative analyses were correct.
#
Agentic architecture
We saw the largest gains when, this fall, we switched Bugbot to a fully agentic design. The agent could reason over the diff, call tools, and decide where to dig deeper instead of following a fixed sequence of passes.
The agentic loop forced us to rethink prompting. With earlier versions of Bugbot we needed to restrain the models to minimize false positives. But with the agentic approach we encountered the opposite problem: it was too cautious. We shifted to aggressive prompts that encouraged the agent to investigate every suspicious pattern and err on the side of flagging potential issues.
In addition, the agentic architecture opened up a richer surface for experimentation. We were able to shift more information out of static context and into
dynamic context
, varying how much upfront context the model received and observing how it adapted. The model consistently pulled in the additional context it needed at runtime, without requiring everything to be provided ahead of time.
The same setup lets us iterate directly on the toolset itself. Because the model's behavior is shaped by the tools it can call, even small changes in tool design or availability had an outsized impact on outcomes. Through multiple rounds of iteration, we adjusted and refined that interface until the model's behavior consistently aligned with our expectations.
#
What's next
Today, Bugbot reviews more than two million PRs per month for customers like Rippling, Discord, Samsara, Airtable, and Sierra AI. We also run Bugbot on all internal code at Cursor.
Looking forward, we expect new models to arrive on a regular basis with different strengths and weaknesses, both from other providers and from our own training efforts. Continued progress requires finding the right combination of models, harness design, and review structure. Bugbot today is multiples better than Bugbot at launch. In a few months we expect it will be significantly better again.
We're already building toward that future. We just launched
Bugbot Autofix
in Beta, which automatically spawns a
Cloud Agent
to fix bugs found during PR reviews. The next major capabilities include letting Bugbot run code to verify its own bug reports and enabling deep research when it encounters complex issues. We're also experimenting with an always-on version that continuously scans your codebase rather than waiting for pull requests.
We've made great strides so far that would not be possible without the contributions of some key teammates including Lee Danilek, Vincent Marti, Rohan Varma, Yuri Volkov, Jack Pertschuk, Michiel De Jong, Federico Cassano, Ravi Rahman, and Josh Ma. Together, our goal continues to be to help your teams maintain code quality as your AI development workflows scale.
Read the docs
or
try Bugbot today
.
Filed under:
research
Author
:
Jon Kaplan
