---
title: "WarpBench "case study page""
source: "Warp Blog"
url: "https://www.warp.dev/blog/warpbench-case-study-reduce-cost-per-pr"
scraped: "2026-10-21T06:01:03.139060+00:00"
lastmod: "2026-10-15T22:33:13.000Z"
type: "sitemap"
---

# WarpBench "case study page"

**Source**: [https://www.warp.dev/blog/warpbench-case-study-reduce-cost-per-pr](https://www.warp.dev/blog/warpbench-case-study-reduce-cost-per-pr)

Engineering
WarpBench: How we reduced our cost-per-PR 75%
Zach Lloyd
|
September 2, 2026
Using Benchmarks, we reduced Warp's internal factory cost per PR from $80 to $30
With Warp Factories Benchmarking it’s now possible to build custom coding agent benchmarks on your team’s real data and workflows with a few clicks.
The advantage of private benchmarking compared to public benchmarks is that the latter are frequently saturated because test data has leaked into model training sets. Also, an internal benchmark is more useful because it shows performance on your actual code, not on some set of random, unrelated tasks. You can use the results to build model routing rules you know work.
<Insert video of me walking through the whole WarpBench process>
The setup
In order to optimize the default implementation model we use in our factory, we created an internal benchmark called WarpBench. To build the task set, we asked our foreman agent to search over our corpus of past agent runs looking for a representative set of XX tasks, at different levels of scope; roughly S, M, L, XL. The tasks span both our server codebase (golang, react) and our client (rust), and represent a range of coding tasks - from UI changes to database updates, server business logic, and systems programming tasks.
Once the task set was curated, we picked a set of models to test, with a mix of lab and open-weight (Opus 5, GPT-5 Sol, Gemini 3.7, and Grok 4.6, GLM 5.3 flash). We used Warp Agent as the harness, although in future iterations we plan on also testing Claude Code and Codex directly, since our infra supports other agents.
<Show model selection>
It took less than 30 minutes of setup work to create the benchmark using the built-in primitives in Warp Factories. The same method works out of the box for any factory on our platform.
The actual benchmarks run by recreating the state of the curated tasks and re-launching them in sandboxes with the original environment. We achieve this by using git to rehydrate not just the original code, but also fix the factory configuration at a point in time. Since our factories are defined as code, this ensures that agent definitions, skills, etc. are all constant across tests. We then use our built-in scorers (LLM-as-a-judge) to score the runs along different dimensions like cost, quality, verbosity and custom dimensions.
Without these primitives it would have taken weeks of engineering work to gather the traces, build the replay and LLM-as-a-judge functionality, build the data analysis, generate the pareto charts, etc. We know from experience testing our harness on public benchmarks like terminal bunch (previously #1) and SWEBench (#3) how much work this is, but also how valuable benchmarking is for improving harness performance.
<Insert video of Ben building a benchmark>
The results
The benchmarks took XX hours to run and cost XX. We don’t recommend running benchmarks often because of the cost, but running them when new models come out or when you make significant changes to other inputs like your code, skills, MCPs, etc. You also can make very targeted benchmark sets for specific types of tasks, which tend to cost less. I’ll cover how we do this in another article.
We’ve iterated on the benchmarks in the last two weeks, and applied them to save a bunch of money so far.
Our first iteration was on a set of targeted simple UI tasks - these showed that grok 4.6 (high) was the best model, so about a week ago we made that the primary implementation agent (note that developers can deviate from this if they want). Prior to Grok 4.6 (high) we were using Warp’s “auto (genius)” routed model, which for complex tasks routes most frequently to Opus 5. The result was a drop from about $80 to $30 per completed PR, with no measured drop in agent quality.
<Insert graph of initial Grok 4.6 (high) results>
As a quality check, we looked not only at merge rate (which stayed constant), but also at our internal scorer agents that rate agent runs using LLM-as-a-judge on quality and correctness, amongst other dimensions. Our task compliance scores actually went up after the change, from 69% to 83%.
We expanded the benchmarks earlier this week, and now believe that GPT 5.6 sol is even better from a cost / quality tradeoff. Here’s the pareto graph from the more full benchmark run:
We just made this the default implementation agent yesterday and are letting the results bake, but we expect about another 25% improvement (there’s some variance here).
Towards more specialized benchmarks
The next steps are actually to try to refine these benchmarks into different task sets that we can effectively model-route on. It’s relatively simple to come up with a good default model by doing a wide benchmark across various tasks (and we might have guessed ahead that Grok 4.6 and Sol would be more cost-effective than Opus 5).
Next though we will try to slice tasks and see if there are model-routing rules that we can confidently deploy to get even more benefit, e.g. slicing by language, or task complexity, or client/server, etc.
The idea is to build up more task sets, measure what model is best, and then use Warp’s custom router feature to route work accordingly.
Future steps
We are exploring a couple of future directions, namely benchmarking across harnesses and A/B testing different configs.
Cross-harness benchmarking (e.g. comparing Warp Agent vs. Claude Code vs. Codex) is particularly interesting and not yet fully supported  in our platform, but coming soon. I’m eager to see how the different harnesses fare on the same tasks.
A second improvement we are exploring is A/B testing. Right now, our benchmarks only support retroactive measurements of quality. When you make changes based on them, you are assuming future tasks are similar to past ones. You can get more confidence by actually A/B testing model routing rules and make sure the benchmarking results hold.
Request access
You can
get early access
to Warp Factories or
book a demo
for a tailored walk-through of the platform.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Oct 15, 2026
|
Engineering
10
min
Tactics for rolling out software factories: human and organizational changes
10
min
Oct 15, 2026
|
Engineering
7
min
The road to self-improving software
7
min
Sep 15, 2026
|
Engineering
12
min
Adopting the software factory model: crawl, walk, run
12
min
Aug 27, 2026
|
Engineering
12
min
Closing the loop with self-improving cloud software factories
12
min
Aug 26, 2026
|
Engineering
8
min
The missing feedback loop for software factories
8
min
View all articles
