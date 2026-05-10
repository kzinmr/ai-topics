---
title: "The productivity impact of coding agents · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/productivity"
scraped: "2026-05-10T01:19:44.554380+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# The productivity impact of coding agents · Cursor

**Source**: [https://cursor.com/blog/productivity](https://cursor.com/blog/productivity)

Blog
/
research
Nov 11, 2025
·
research
The productivity impact of coding agents
Oskar Schulz
·
4 min read
Table of Contents
↑
Accepting agent-written code
Impact on productivity
User behavior and applications
Conclusion
We’re interested in the open questions around how developers use Cursor’s agent in their work and the productivity impacts of Cursor in organizations.
Suproteem Sarkar, an assistant professor of finance and applied AI at the University of Chicago,
recently conducted a study
analyzing agents' early effects across tens of thousands of Cursor users.
The study found that companies merge 39% more PRs after Cursor's agent became the default. It also found that experienced developers write more plans before coding and appear more proficient with agents.
#
Accepting agent-written code
The study looked at two signals: how frequently users send requests to the agent and how often they accept its code edits. Whether a user accepts the agent's edits depends on how well the output aligns with their intent and their threshold for applying generated code.
Junior developers are more likely to accept code from Tab, while senior developers are more likely to accept code from agents. For every standard deviation increase in years of experience, we see a corresponding ~6% increase in the rate of agent acceptances relative to the mean.
We would have expected that less experienced developers tend to use and accept agent at higher rates: it seems like the opposite is true!
A few theories:
Experienced developers may be more skilled at using agents by using custom rules or managing context more effectively.
They are more confident in their ability to evaluate agent-written code changes, which increases their willingness to accept.
They are working on more well-scoped tasks which can be easier for agents to complete in fewer iterations.
#
Impact on productivity
The study measured how proxies for throughput and quality changed after Agent became the default mode on Cursor. It compared these measures between an "eligible" group of organizations that were already using Cursor before the agent was released and a "baseline" group of organizations that weren't using Cursor during the analysis period. It found that the rate of merged PRs increased by 39% relative to time trends in the baseline group.
Across other metrics, the study found that the PR revert rate did not significantly change and the bugfix rate slightly decreased. It also found that the average lines edited and average files touched per merged PR did not change significantly.
#
User behavior and applications
The contents of requests indicate how developers are using agents and the actions they intend to perform. In a sample of 1,000 users, there were three broad categories of conversation-starting requests: implementing code, explaining code and errors, and planning an action. The majority of conversation-starting requests (~61%) were for implementation, where the agent is instructed to generate code.
The study found that more experienced developers are more likely to plan an action before generating code.
#
Conclusion
There isn’t yet a single definitive metric for measuring the economic impact of AI on software engineering. Like with any new technology, realizing AI’s full value will take time.
We’re encouraged by these early findings, and we’d like to continue studying Cursor’s effects on productivity.
To read the full study, you can access it
here
.
Filed under:
research
Author
:
Oskar Schulz
