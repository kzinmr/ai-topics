---
title: "PlanetScale protects production reliability with Bugbot · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/planetscale"
scraped: "2026-05-10T01:19:39.502647+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# PlanetScale protects production reliability with Bugbot · Cursor

**Source**: [https://cursor.com/blog/planetscale](https://cursor.com/blog/planetscale)

Blog
/
customers
Mar 2, 2026
·
customers
PlanetScale protects production reliability with Bugbot
Bugbot saves PlanetScale the equivalent of two full-time engineers worth of review effort.
3 min read
Contact sales
Table of Contents
↑
Agents shift bottlenecks in the SDLC downstream
Eliminating production downtime with Bugbot
Measuring the quality of Bugbot reviews
PlanetScale is a Cloud Infrastructure company in North America.
80%
Bugbot resolution rate
2K+
PRs reviewed monthly
2 FTEs
Dev time saved
PlanetScale is a Cloud Infrastructure company in North America.
80%
Bugbot resolution rate
2K+
PRs reviewed monthly
2 FTEs
Dev time saved
PlanetScale manages cloud database workloads for its customers' most sensitive data. Reliability is the product and every code change pushed to production must be flawless. As agents made code generation cheap and fast, code review became the new bottleneck in the software development lifecycle.
To ensure correctness and ship code to production with confidence, PlanetScale adopted
Bugbot
as a dedicated agentic review layer. Today, roughly 80% of Bugbot comments are addressed before merge time, preventing issues from reaching production and saving PlanetScale the equivalent of two full-time engineers worth of review effort.
#
Agents shift bottlenecks in the SDLC downstream
To maintain product reliability, the PlanetScale engineering team sets an uncompromising bar for code review. "Reliability is at the core of our product. Every change pushed to production must be flawless," said Fatih Arslan, a software engineer at PlanetScale.
As coding agents became central to development workflows, bottlenecks shifted downstream, from code generation to code review. "Code has become cheap. The bottleneck is now whether your code is correct and whether you understand what it does," explained Arslan.
Code output increased rapidly while human review capacity remained fixed. This imbalance created pressure on product quality. To keep pace, PlanetScale estimated it would need to dedicate two engineers exclusively to code review. That tradeoff would reduce engineering bandwidth for product development without solving the long-term reliability challenge as agent adoption continued to scale.
We realized we need Bugbot's agentic review to complement our existing process. It would otherwise be very difficult to push code to production with confidence in quality and correctness.
Fatih Arslan
Software engineer, PlanetScale
#
Eliminating production downtime with Bugbot
Bugbot stood out from other agent review tools in detecting issues that human reviewers were missing because of the complexity of PlanetScale's codebase and volume of agent-generated code.
With Bugbot, engineers began catching and resolving bugs that could cause production downtime earlier in development.
Bugbot is different from other tools. It detects issues that as a human reviewer I would never imagine to look at. I was blown away.
Fatih Arslan
Software engineer, PlanetScale
Unlike static analyzers and linters that focus on mechanical correctness, Bugbot surfaces deeper semantic and logical issues like:
State synchronization gaps
where systems are marked complete prematurely
Logical flow changes
that prevent critical code paths from executing
Asynchronous controller interactions
that fail to converge properly
Edge cases
that could trigger restarts across production databases
Bugbot consistently finds bugs that can cause meaningful downtime in production, but are very hard for humans to catch.
Fatih Arslan
Software engineer, PlanetScale
PlanetScale also found that simply prompting a frontier model to review code would not consistently surface the most critical issues Bugbot identifies. "When I use a reasoning model and ask it to review the branch, it doesn't find these issues. It's the specialized harness and the way Bugbot is built that makes all the difference," said Arslan.
#
Measuring the quality of Bugbot reviews
PlanetScale evaluates Bugbot using a simple metric: resolution rate, which measures the proportion of Bugbot-identified issues that are addressed at merge time.
Roughly 80% of Bugbot comments are now addressed by engineers across more than 2,000 PRs reviewed each month. "Bugbot's comments are top notch and keep improving over time as Bugbot gets more context," said Arslan.
The signal-to-noise ratio for Bugbot is very high. When Bugbot comments on a PR, we know it is highlighting an issue we have to fix.
Fatih Arslan
Software engineer, PlanetScale
Bugbot is now deeply embedded in PlanetScale's workflow and gives engineers the confidence that both human-written and agent-generated code can be shipped safely to production. "I love Bugbot. That's my motto," says Arslan.
PlanetScale can now ship software more quickly without sacrificing quality, while engineers can focus on solving complex infrastructure problems rather than manually reviewing every line produced by agents.
If I took Bugbot away from our engineering team, there would be a mutiny.
Sam Lambert
CEO, PlanetScale
If you're excited about streamlining code review and enhancing product reliability with agents, please
reach out to our team
to get started with a Cursor trial.
Filed under:
customers
Author
:
Cursor Team
PlanetScale is a Cloud Infrastructure company in North America.
80%
Bugbot resolution rate
2K+
PRs reviewed monthly
2 FTEs
Dev time saved
PlanetScale is a Cloud Infrastructure company in North America.
80%
Bugbot resolution rate
2K+
PRs reviewed monthly
2 FTEs
Dev time saved
