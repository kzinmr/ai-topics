---
title: "What MiniMax M3.1 Flash reveals about choosing and combining models"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/what-minimax-m3-1-flash-reveals-about-choosing-and-combining-models"
scraped: "2026-11-18T06:00:47.203056+00:00"
lastmod: "2026-11-17T19:06:12.000Z"
type: "sitemap"
---

# What MiniMax M3.1 Flash reveals about choosing and combining models

**Source**: [https://fireworks.ai/blog/what-minimax-m3-1-flash-reveals-about-choosing-and-combining-models](https://fireworks.ai/blog/what-minimax-m3-1-flash-reveals-about-choosing-and-combining-models)

Where does
MiniMax M3.1 Flash
deliver useful performance at an acceptable cost and speed? The
Specialized Intelligence Index
(SII) helps teams answer that question through domain-specific benchmarks built by practitioners. We used those evaluations to compare M3.1 Flash with closed models including Claude Sonnet 5.5, GPT-6 Luna and Gemini 3.8 Flash, and explored whether using it alongside another model could improve results.
Coding shows the clearest gains. M3.1 Flash completes more DeepSWE tasks than Gemini at substantially lower model cost; against Luna, the additional completions come at a premium. Web-research results are more mixed: lower costs than Sonnet come with longer waits or lower scores, depending on the evaluation.
The coding findings also extend beyond comparing models individually. In one simulation, starting with M3.1 Flash and sending failed attempts to Claude Opus 5.5 completed more legacy-code tasks at lower model cost than Opus alone. This illustrates why evaluating a model includes considering the role it could play alongside others.
What we evaluated
The study covers software engineering with DeepSWE v1.1 and Factory’s Legacy-Bench, and web research with Nimble’s Web Context, Exa’s ATLAS and Parallel’s Search Capability Leaderboard. Sierra’s τ³-Banking, Doximity’s Bedside Bench and Column Tax’s TaxCalcBench provide comparisons on banking support, clinical questions and tax preparation. We examine quality, model cost and execution time where available, then use individual runs to simulate retries and model combinations. Rogo’s Big Finance Benchmark, which tests financial research, also contributes to the workload-assignment analysis.
Coding: M3.1 Flash completes more tasks than Gemini 3.8 Flash and GPT-6 Luna
DeepSWE v1.1 tests whether an agent can resolve software issues across 113 tasks in 91 repositories. The agent explores the codebase, edits files and submits a patch. Tests withheld from the agent then check whether the patch resolves the issue.
For teams using Gemini 3.8 Flash, M3.1 Flash offers higher completion at about 92% lower model cost in this evaluation. Against GPT-6 Luna, it costs about 84% more, adding roughly eight successful tasks per 113-task run for $18 in additional model spending.
M3.1 Flash averages about 20 minutes per task, broadly similar to Gemini and Luna in this setup. Its advantage here is completion, with the cost benefit depending on which model it replaces.
Retrying M3.1 Flash raises coding coverage from 73% to 90%
Some tasks M3.1 Flash misses on one attempt succeed on another. Across three recorded runs, it solves 102 of the 113 tasks at least once, compared with about 83 per run on average.
We simulated allowing up to three attempts and stopping at the first success. Average model spending rises from about $0.35 to $0.50 per submitted task, or about $0.55 per solved task. Each retry starts fresh, without feedback from the previous failure.
Retrying can help M3.1 Flash solve more coding tasks, provided the application can reliably check whether each patch fixes the issue. The simulation uses hidden benchmark tests to decide when to stop; verification costs and time would also matter in a production workflow.
Web research: savings depend on the quality and speed you need
M3.1 Flash offers different tradeoffs across three web-research evaluations. It scores higher than Claude Sonnet 5.5 on Nimble’s Web Context benchmark at lower model cost, but takes substantially longer. On Exa’s ATLAS and Parallel’s Search Capability Leaderboard, the savings come with lower scores.
Open in lightbox
Higher scores on Web Context come with longer waits
Nimble’s Web Context tests agents on gathering information about companies and creators, finding entities that match specified criteria, and writing research reports. It checks reported facts against source pages and scores both accuracy and completeness.
M3.1 Flash scores 74.7, compared with Claude Sonnet 5.5’s 67.2 and GPT-6 Luna’s 67.9. It also scores higher than both across the benchmark’s three verticals: go-to-market, finance and social media.
On Web Context, M3.1 Flash scores higher than Sonnet at 33% lower model cost, but takes nearly eight times as long. That makes it more plausible for background research than an interaction where someone is waiting. Against Luna, the higher score comes with both higher spending and longer execution.
For teams using more expensive models, M3.1 Flash also merits evaluation: Claude Opus 5.5 scores 71.8 and GPT-6 Astra 72.6, at approximately seven and eighteen times its model cost. Those small score differences do not establish a reliable quality advantage.
Lower search costs can come with lower scores
Exa’s ATLAS tests whether agents can build complete tables of entities matching a request. M3.1 Flash scores 22.0, compared with Claude Sonnet 5.5’s 46.8. Web Context includes entity-finding tasks too, so these aggregate results do not isolate why the models’ relative performance changes.
Parallel’s Search Capability Leaderboard evaluates 300 questions spanning multi-step research, specialist knowledge and business research. Models use search and page-extraction tools to answer them.
M3.1 Flash scores 68.8 against Sonnet’s 74.1, at $0.04 versus $0.80 per question including estimated search fees. That is about 95% lower cost with a 5.3-point lower score. Evaluate M3.1 Flash where lower research costs matter most, checking that it meets your workflow’s requirements for answer quality, completeness and turnaround time.
Banking, clinical and tax evaluations favor the tested alternatives
M3.1 Flash’s coding strengths do not extend to every workload. On Sierra’s τ³-Banking, which tests customer requests handled through bank policies and account-management tools, it resolves 34.0% of attempts, compared with Gemini 3.8 Flash’s 51.4% and GPT-6 Luna’s 37.7%.
We examined 38 conversations that at least three-quarters of the evaluated models could resolve. Across four attempts per conversation, M3.1 Flash failed 57 times. In 23 of those failures, it completed every required step but also made an unrequested account change. In one example, it correctly denied a credit-limit increase, then issued a statement credit to soften the refusal. For account-changing workflows, checking only that the request was fulfilled would miss these additional actions.
Clinical and tax results also favor the tested alternatives. Doximity’s Bedside Bench evaluates answers to physician-written clinical questions. M3.1 Flash scores 75.3, versus Gemini’s 86.5 and Luna’s 87.2. Column Tax’s TaxCalcBench tests preparation of complete federal and state tax returns from taxpayer documents. M3.1 Flash is close to Luna in correctly reporting wages and taxes already withheld, but less accurate on deductions and exemptions that reduce taxable income. Accuracy on those basic figures therefore does not translate into a correct return.
Combining M3.1 Flash with other models can improve the quality-cost tradeoff
Pairing M3.1 Flash with Gemini 3.8 Flash completes more tasks at lower cost
The earlier comparisons show strengths in coding and weaker results in banking support. Could M3.1 Flash’s coding strengths improve overall results while another model handles workloads where that model performs better?
We simulated dividing work between models across four workloads: fixing software issues, maintaining older codebases, handling banking support requests and answering financial-research questions.
For each pairing, we assigned each workload to the model with the higher recorded completion rate, using cost to break ties. Each task was attempted once by one model, with no retry or fallback to the other model.
Paired with Gemini 3.8 Flash, M3.1 Flash handled repository coding and legacy-code maintenance, while Gemini handled banking support. Across these 307 benchmark tasks, the pairing completed an average of 188, compared with 172 for Gemini alone, while reducing model spending from $661 to $108.
Most of that 84% saving came from DeepSWE, where M3.1 Flash cost $0.35 per task versus Gemini’s $4.24. The percentage depends on the workload mix: an application with more banking tasks and fewer coding tasks would see a smaller percentage saving.
Open in lightbox
The other pairings show why the comparison model matters. Adding M3.1 Flash to GPT-6 Luna bought additional completion at higher cost. Pairing it with Claude Opus 5.5 or GPT-6.1 Sol reduced spending but did not consistently complete more tasks than those models alone in the validation checks.
We also checked whether the model choices worked on tasks that were not used to make those choices. Across 500 random splits, we chose a model for each workload using half the tasks and evaluated those choices on the remaining half. The Gemini pairing still achieved higher average completion and lower spending than Gemini alone.
Starting with M3.1 Flash before Opus 5.5 improves completion at lower cost
Assigning models by workload is one option. Another is to let one model attempt a task and send failures to a second model. We tested this approach with M3.1 Flash first and Claude Opus 5.5 handling failed attempts.
On Factory’s Legacy-Bench, which tests maintenance of older codebases, this simulated sequence solves about 71% of the 97 shared tasks, compared with 64% for Opus alone. Average model spending falls from $0.51 to $0.42 per task, about 18% lower, including unsuccessful attempts.
M3.1 Flash solves some tasks Opus misses, while Opus recovers some M3.1 Flash failures. Tasks M3.1 Flash solves also avoid the cost of an Opus attempt. That combination explains how the sequence can improve both completion and spending.
The simulation uses hidden benchmark tests to identify failures. Applying this approach requires reliable checks; the reported costs exclude verification and orchestration, and end-to-end execution time was not measured.
A model can add value without taking over every task
M3.1 Flash’s coding results show how a model can earn a limited role alongside an existing one. That changes the adoption question from whether to replace a model outright to whether assigning it some work, or giving it the first attempt, improves the overall result. The answer depends on the existing model, the workload mix and, for escalation, the ability to identify failures reliably.
Explore the benchmark comparisons in the
Specialized Intelligence Index
, or learn about
Fireworks Nexus
for using an ensemble of open and closed models.
Methodology and limitations
Sources, scoring and costs
Results use the study’s November 7 and November 11, 2026, snapshots. Scores follow each benchmark’s own grading rules. Model costs use recorded usage and evaluation pricing, including Gemini 3.8 Flash’s introductory pricing. Parallel and Exa include search fees; grader costs are excluded. Costs per task include unsuccessful attempts.
DeepSWE and retries
M3.1 Flash completed three runs over 113 tasks across 91 repositories; all 339 attempts are included. The October 29 runs used a dedicated Fireworks deployment, with costs calculated at serverless rates of $0.15 per million uncached-input tokens, $0.015 per million cached-input tokens and $0.60 per million output tokens.
Retry estimates average every possible ordering of the recorded attempts, stopping at the first benchmark-verified success or the attempt limit. Repeated attempts are not assumed independent.
Workload assignment and escalation
Expected completions sum per-task pass rates averaged across recorded attempts. Full-set routing results select and evaluate workload assignments on the same data. A separate check uses 500 splits, selecting assignments on half the tasks and evaluating them on the other half.
Legacy-Bench routing and escalation use the 97 tasks all compared runs could build. Three additional Java 7 tasks available in M3.1 Flash’s later environment are excluded.
Task-level analysis and coverage
The banking subset contains 38 conversations resolved by at least three-quarters of evaluated models, with four M3.1 Flash attempts per conversation. The 23-of-57 finding describes failures within that subset.
The tax comparison uses no-search runs for both models. M3.1 Flash received OCR text extracted from PDFs. Wage/withholding and deduction/exemption categories are analyst-defined groupings of return lines.
Run coverage varies across models. M3.1 Flash has fewer recorded runs on some benchmarks, including Legacy-Bench and Bedside Bench, limiting conclusions from small score differences. Only one benchmark is shared with MiniMax M3, so this study does not establish a general upgrade recommendation.
