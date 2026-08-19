---
title: "DeepSeek V4 Pro 0813 vs Claude Fable 5 on DeepSWE: Cost, Coding, and Routing"
url: "https://www.together.ai/blog/deepseek-v4-pro-0813-vs-claude-fable-5-on-deepswe-cost-coding-and-routing"
fetched_at: 2026-08-18T10:03:44.547752+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# DeepSeek V4 Pro 0813 vs Claude Fable 5 on DeepSWE: Cost, Coding, and Routing

Source: https://www.together.ai/blog/deepseek-v4-pro-0813-vs-claude-fable-5-on-deepswe-cost-coding-and-routing

‍
In our
DeepSeek V4 Pro 0813
vs Claude Fable 5 comparison on DeepSWE, a benchmark that tests a model's software engineering ability across many task types and programming languages, the two models sit at opposite ends of the price sheet. Claude Fable 5 is the most expensive rollout on the DeepSWE board. DeepSeek V4 Pro 0813 is one of the cheapest. Fable is seven points more accurate on the first try and costs ninety times as much per rollout, so the real question is not which model is better, but what that 90x premium actually buys and when it is worth paying.
DeepSWE · Head to Head
DeepSeek V4 Pro 0813 vs Claude Fable 5 at a glance
Model
Pass@1
Avg cost
Solves / $100
Out tok
Steps
claude-fable-5 [max]
69.7% ± 2.3%
$21.63
3
115k
79
deepseek-v4-pro-0813 [max]
62.8% ± 3.1%
$0.24
260
101k
146
We ran DeepSeek V4 Pro 0813 (max) against Claude Fable 5 (max) on all 113 DeepSWE tasks, four trials each, from the published per-trial records: 904 rollouts in total (452 each). Fable is the expensive craftsman; Pro is the value outlier. The two also disagree more than any other pairing in this set, which turns out to be the most interesting thing about them. Every figure below comes from this run, so it can differ from other public DeepSeek V4 Pro 0813 vs Claude Fable 5 scorecards.
The DeepSWE scoreboard: pass@1 and pass@k
Single shot, Fable leads: 69.7% pass@1 to Pro's 62.8% (official scoring). But the lead is fragile. At two attempts Pro pulls level (78.5 vs 77.1), and at four Pro's 88.5% pass@4 clears Fable's 84.1% by more than four points. For a model that costs ninety times as much, Fable neither owns the ceiling nor holds its first-shot edge under retries. The lower-cost model has both the wider reach and the higher best-of-k.
Cost comparison: DeepSeek V4 Pro 0813 vs Claude Fable 5 pricing
At \$0.24 a rollout, DeepSeek V4 Pro 0813 is 90x cheaper than Fable (\$21.63): 260 solves per \$100 against Fable's 3. This is the widest cost gap of any pairing we have measured, and Fable is the single most expensive config on the board. And unusually, the lower price does not come with the speed penalty you would expect: Fable's median rollout is 31 minutes to Pro's 35, roughly even, because Fable is by far the most verbose model on the board (115k output tokens) even though it takes fewer steps (79 vs 146). Pro takes more steps; Fable writes more per step. Neither model is notably faster.
Failure modes: how each model gets it wrong
Both are disciplined about not breaking things:
DeepSeek V4 Pro 0813 and Fable each regress the existing test suite in only 11% of failures
, well below the GPT-family's 20%. The difference is in the other direction: Fable carries the largest big-miss share here (18% vs Pro's 10%), meaning when Fable is wrong it is more often badly wrong, a solution far off the mark rather than one edge case short. Pro fails closer to correct more often (66% near miss vs Fable's 57%). So both are safe to accept without heavy regression gating, but Fable's misses are the more expensive kind to debug.
Where each wins, by task type
Fable's craftsmanship shows in the reasoning-heavy, exact-contract domains: it wins 6 of 8, led by data modeling and serialization at 88% (24 points over Pro) and language internals (78). But DeepSeek V4 Pro 0813 takes two, and both are significant: stateful reactivity (66 vs 64) and, tellingly, concurrency and durability (58 vs 45): a 13-point edge in exactly Fable's worst domain. Fable's 45% on concurrency is its weakest cell and the one domain where the lower-cost model is simply the better engineer, not just the cheaper one.
DeepSeek V4 Pro 0813 vs Claude Fable 5 by programming language
Fable wins four of five languages, but the number that justifies its price is Rust: 85% to Pro's 65, a 20-point margin and the widest single gap in the matchup. Fable is clearly the serialization and Rust specialist. Elsewhere it is closer than the price implies (Python 70 vs 60, Go 71 vs 67, JavaScript 75 vs 65), and DeepSeek V4 Pro 0813 actually takes TypeScript (61 vs 57). Outside Rust and serialization, the case for paying 90x is hard to make.
How different are DeepSeek V4 Pro 0813 and Claude Fable 5?
Here is the redeeming feature. Per-task correlation is just 0.39, the lowest of any DeepSeek-Pro pairing, so these two genuinely disagree. They both solve 88 tasks; Pro alone gets 12, Fable alone gets 7, and only 6 defeat both. Their union covers 107 of 113 (94.7%), and the disagreements go both ways: DeepSeek V4 Pro 0813 sweeps awilix-async-container-initialization four-for-four while Fable never lands it, and Fable four-for-fours four tasks Pro zeros (including koota-query-predicates and testem-bail-on-test-failure). This is real complementarity, not redundancy.
Routing between them: the portfolio play
That diversity plus the price makes the cascade compelling. Run DeepSeek V4 Pro 0813 first and escalate to Fable only when your test suite rejects the answer: 82.7% solved at \$8.28 per task. That is thirteen points above Fable alone (69.7%) for well under half of Fable's own per-task price (\$21.63). The low-cost first stage clears most of the queue, so Fable's premium price applies only to the hard remainder, and those tasks get a second independent attempt on top. The cascade beats a perfect one-shot oracle router (78.8%) too. The order is not optional: Pro-first costs \$8.28, Fable-first costs \$21.71, for the same accuracy.
What it means
Fable 5 is the hardest single model on this board to justify as a default: the most expensive rollout by far, a first-shot lead that retries erase, and no four-shot ceiling advantage. Buy it for exactly two things, Rust (85%) and serialization-heavy work (88%), where its quality genuinely justifies the price.
DeepSeek V4 Pro 0813 is the opposite profile: near-Fable accuracy on the first try, a higher ceiling, an equal or better failure profile, and 90x cheaper, though it cedes Rust and the exact-contract domains. And because the two are the most diverse pair we have measured, the best use of Fable is not as a default but as a selective escalation behind a low-cost Pro first stage, paid only on the handful of tasks that actually need a Rust or serialization specialist.
Data table: DeepSeek V4 Pro 0813 vs Claude Fable 5, full results
DeepSWE · Full Results
Metric
deepseek-v4-pro-0813 [max]
claude-fable-5 [max]
Pass@1 (official scoring)
62.8%
69.7%
Pass@1 (errors as failures)
62.8%
67.3%
Pass@2 / pass@4
78.5 / 88.5%
77.1 / 84.1%
Coverage / reliability
88.5 / 71.0%
84.1 / 82.0%
Solid (4/4) / walls (0/4)
35 / 13
56 / 18
Cost per rollout / total
$0.24 / $109
$21.63 / $9,346
Solves per $100
261
3
Median minutes / steps
35 / 146
31 / 79
Median peak context / output tokens
232k / 101k
202k / 115k
Failure anatomy (near / big miss / regression)
66% / 10% / 11%
57% / 18% / 11%
Domains won (of 8)
2 (stateful, concurrency)
6
Languages won
1 (TypeScript)
4 (Rust a rout)
Per-task correlation / union
0.39 / 107 of 113 (94.7%)
Cascade Pro → Fable (accuracy / cost)
82.7% / $8.28
(vs Fable alone 69.7% / $21.63)
Oracle 1-shot router
78.8%
Infra errors
0
16
FAQs
Is DeepSeek V4 Pro 0813 better than Claude Fable 5?
It depends on the metric. Claude Fable 5 wins single-attempt quality on DeepSWE (pass@1 69.7% vs 62.8%) and solves more tasks four-for-four (56 vs 35). DeepSeek V4 Pro 0813 pulls level at pass@2 and wins pass@4 (88.5% vs 84.1%) at 90x lower cost per rollout, so it is the stronger value pick for high-volume or retry-tolerant agent work.
How much cheaper is DeepSeek V4 Pro 0813 than Claude Fable 5?
In our run, DeepSeek V4 Pro 0813 cost \$0.24 per rollout versus \$21.63 for Claude Fable 5 at max effort, roughly 90x cheaper. Measured per solved task, Pro returned 260 solves per \$100 against Fable's 3, about 80x the solved work per dollar.
Which is better for coding, DeepSeek V4 Pro 0813 or Claude Fable 5?
For most coding work they are closer than the price implies. Claude Fable 5 leads Rust (85 vs 65), Python, Go, and JavaScript, and wins 6 of 8 task domains, led by data modeling and serialization. DeepSeek V4 Pro 0813 takes TypeScript (61 vs 57), stateful reactivity, and concurrency and durability (58 vs 45), which is Fable's weakest domain.
Should I route between DeepSeek V4 Pro 0813 and Claude Fable 5?
Yes, if you can verify results. The two models have the lowest per-task correlation of any pairing we have measured (0.39) and together cover 107 of 113 tasks. Running DeepSeek V4 Pro 0813 first and escalating to Claude Fable 5 when your test suite rejects the output reaches 82.7% at \$8.28 per task, beating Fable alone and a perfect one-shot oracle router.
What is pass@k on DeepSWE?
pass@k measures whether at least one of k attempts at a task passes the hidden test suite. pass@1 rewards getting it right first try; higher k rewards a model that can eventually reach a solution across several tries. DeepSeek V4 Pro 0813's edge grows as k increases.
‍
