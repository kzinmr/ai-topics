---
title: "How we compare model quality in Cursor · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/cursorbench"
scraped: "2026-05-10T01:19:38.981685+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# How we compare model quality in Cursor · Cursor

**Source**: [https://cursor.com/blog/cursorbench](https://cursor.com/blog/cursorbench)

Blog
/
research
Mar 11, 2026
·
research
How we compare model quality in Cursor
Naman Jain
·
7 min read
Table of Contents
↑
The limitations of public benchmarks
Building CursorBench
CursorBench shows more separation between models
CursorBench scores align with online evals
The next eval suite
Developers are asking coding agents to take on longer, more complex tasks that span multiple files, tools, and steps. As these requests grow in scope, the evals that measure agent performance need to evolve with them.
At Cursor, we use a hybrid online-offline eval process to keep our understanding of model quality aligned with what developers actually do.
The offline part uses CursorBench, our internal eval suite based on real Cursor sessions from our engineering team. Because tasks come from actual Cursor usage rather than public repositories, CursorBench is both better at distinguishing between models and more aligned with real developer outcomes than public benchmarks.
We built CursorBench to measure multiple dimensions of agent performance including solution correctness, code quality, efficiency, and interaction behavior. This blog focuses on solution correctness results, but in practice we evaluate agents across all of these axes.
This chart shows correctness scores on CursorBench plotted against median completion tokens to capture the compute/latency tradeoff that affects usability. The top right corner represents ideal agent quality, with highest performance at the lowest cost.
We supplement CursorBench with controlled analysis on live traffic. These online evals catch regressions that offline suites miss, like where the agent's output looks correct to a grader but feels worse to a developer using the product.
Together, this online-offline loop keeps our notion of model quality grounded in production as workflows change, and lets us craft the best possible agent experience in Cursor.
#
The limitations of public benchmarks
A good benchmark needs to distinguish between models that perform differently in practice, while aligning with how developers actually experience those models. Public offline evals struggle at both.
The first issue is alignment. As developers take on increasingly complex and varied work with agents, static or misaligned benchmarks end up testing the wrong things entirely. Most SWE benchmarks, for example, are still focused on bug-fixing tasks. Similarly, Terminal-Bench emphasizes broad puzzle-style tasks like finding the best chess move from a board position. We find that these are not well aligned with the coding work developers ask agents to do.
The second is grading. Many public benchmark tasks assume a narrow set of correct solutions, but most developer requests are underspecified enough to admit many valid approaches. As a result, benchmarks tend to either penalize alternative correct approaches or append synthetic requirements to remove underspecification. Neither provides an accurate assessment of true performance.
The third is contamination. SWE-bench Verified, Pro, and Multilingual all draw tasks from public repositories that end up in model training data, inflating scores. OpenAI
recently
stopped reporting SWE-bench Verified results entirely after finding that frontier models could reproduce gold patches from memory, and that nearly 60% of unsolved problems had flawed tests.
The result is that at frontier levels, these benchmarks no longer tell apart models that have very different utility for developers.
#
Building CursorBench
We source tasks for CursorBench using
Cursor Blame
, which traces committed code back to the agent request that produced it. This gives us a natural pairing of developer query and ground-truth solution. Many tasks come from our internal codebase and controlled sources, which reduces the risk that models have seen them in training. We refresh the suite every few months to track shifts in how developers use agents.
Problem scope in our correctness evals has roughly doubled from the initial version to the current one, CursorBench-3, in terms of both lines of code and mean number of files. CursorBench-3 tasks involve substantially more lines than those in SWE-bench Verified, Pro, or Multilingual. While lines of code is an imperfect measure of difficulty, growth on that metric reflects the way we've incorporated more challenging tasks into CursorBench, such as handling multi-workspace environments with monorepos, investigating production logs, and performing long-running experiments.
CursorBench tasks also align with the underspecified, often ambiguous way developers talk to agents. Our task descriptions are intentionally short, in contrast with the detailed GitHub issues sourced in public benchmarks, and we use agentic graders to reliably score them.
#
CursorBench shows more separation between models
These differences in task complexity and specification have practical consequences for benchmark utility. CursorBench produces more separation between models at frontier levels, where public benchmarks are increasingly saturated, and in some cases, models like Haiku can match or exceed GPT-5. CursorBench distinguishes reliably between models that developers experience as meaningfully different.
#
CursorBench scores align with online evals
Online evaluation measures whether improvements to our agent actually help developers in practice. We track a set of high-level proxies of agent outcomes, including both interaction and output quality signals, and look for consistent movement across them rather than optimizing for any single metric. Aggregating these allows us to catch regressions where the agent's output scores well under an offline grader, but doesn't actually work well for developers.
We use controlled online experiments to attribute impact. For example, when iterating on
semantic search and retrieval
, we ran an ablation removing the semantic search tool entirely. This let us pinpoint scenarios where semantic search mattered most, such as repository-grounded question-answering on larger codebases.
CursorBench rankings also more closely track how developers experience model quality in Cursor, as measured by our online evaluation metrics.
#
The next eval suite
While CursorBench-3 tasks are longer than tasks on public benchmarks, they still resolve within a single session. We anticipate that over the next year, the vast majority of development work will shift to long-running agents working on their own computers, and we are planning to adapt CursorBench accordingly. Doing so will require finding ways to make grading cheaper, solve reproducibility for tasks that interact with external services, and close the gap between offline assessment and developer experience.
The online-offline loop gives us what we think is the right foundation, and we plan to share more as we build on it.
If you're interested in working on deep technical problems related to the future of coding, reach out at
hiring@cursor.com
.
Filed under:
research
Author
:
Naman Jain
