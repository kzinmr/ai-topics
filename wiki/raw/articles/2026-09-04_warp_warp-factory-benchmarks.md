---
title: "Launch Factory Benchmarks"
source: "Warp Blog"
url: "https://www.warp.dev/blog/warp-factory-benchmarks"
scraped: "2026-09-04T06:00:46.605566+00:00"
lastmod: "2026-09-03T18:08:42.000Z"
type: "sitemap"
---

# Launch Factory Benchmarks

**Source**: [https://www.warp.dev/blog/warp-factory-benchmarks](https://www.warp.dev/blog/warp-factory-benchmarks)

Product
Introducing Factory Benchmarks
Zach Lloyd
|
September 3, 2026
Today we are launching Benchmarks in Warp Factories early access: the first model bench generated from your own coding tasks. Rather than guessing at what model and skill configurations are best, you can now easily test, measure, and put your findings into practice.
The idea is similar to public benchmarks like SWEBench and Terminal Bench, but
on your own actual coding tasks, with your own context
. It’s built directly into the Warp Factories infrastructure and works across frontier and open-weight models, and (soon) across different harnesses like Warp, Claude Code and Codex. Using Benchmarks, we have already adjusted our internal factory configuration to reduce costs by 63% on certain types of tasks without impacting quality.
Explore the actual benchmark result that drove the 63% cost reduction
Benchmarks overview
Benchmarks are comprised of:
A set of agent tasks, either curated from your team’s prior runs or built from scratch
A set of factory configurations
to test by varying model or harness
A set of scorers
to evaluate performance for each configuration along different dimensions like cost, quality, and correctness
Once a benchmark configuration is defined, Warp Factories runs it and compiles the results, showing how each model configuration performs on each scorer dimension.
Here’s an actual run where we can see that GPT 5.6 Sol (high) is the winning model on WarpBench, our internal general purpose benchmark
. We’ve used WarpBench to lower internal cost per PR by about 63% over the past couple weeks.
Our WarpBench results
Under the hood
Warp Factories supports a few primitives that make it easy to build benchmarks on your own data.
First, we
define your factory in code
as a factory.yaml + supporting agent definitions. This records the complete state of the factory at any given time and allows A/B testing different factory configurations.
factory.yaml
Second, our infrastructure automatically stores all agent traces and their metadata across all runs (note that for enterprises, you can store these within your own security boundary). This means our factory infra has visibility of the prompt, the full conversation, the git state pre- and post-run, the PR, and any other generated artifacts. It also gives us the ability to replay a run from its initial state with any factory configuration.
Third, we have Scorers built into the infrastructure. A Scorer is an LLM-as-a-judge evaluation loop that takes an agent run and assigns a grade based on a rubric the user defines. For example, we have scorers for correctness, efficiency, verbosity, cost, and so on. We also use Scorers for our
self-improvement loops
, another technique for improving factory performance.
Scorers across different dimensions like verbosity and efficiency
When you run the benchmark it executes a matrix of [tasks X configurations] runs, each producing an output that gets scored along every dimension. Within our factory infrastructure we show visualizations of the performance with pareto graphs. You can see tradeoffs along each scored dimension (e.g. which configuration is best for cost, for quality, and overall), and which configuration performed best overall.
A comparison of cost across five model families for the task set - GPT 5.6 sol (high) wins
To make this concrete, let’s imagine I wanted to see which model configuration is best in our factory for simple UI tasks in our server codebase, and use that configuration by default for tasks going forward.
You can make the benchmarks manually, but since they are defined in code, it’s easier to just ask our factory foreman to make them.
The foreman
can scan prior runs to find good test tasks to replay (e.g. “find me 5 tasks with 50 LOC or fewer UI changes and build a task set from them”).
Asking the foreman in Slack to generate a benchmark config
Benchmark definition .yaml file
You can also add any prior run to a benchmark through the UI:
Adding previous run as benchmark task
The benchmark definition in code
Once the benchmark is defined, you pick the launch configuration by varying the model, harness and scorers, as well as how many repetitions you want per task (more repetitions add cost but reduce variance).
Here I’ll do a bake off of Grok 4.6 (med), GLM 5.3 flash and Claude Opus 5 (med) in Warp’s harness on simple frontend changes. Note that in Warp Factories, you can vary the harness as well to test Claude Code vs. Codex for example.
Once launched, the agents run in the background, loading the prior tasks, setting them up in their original state and launching with the branched factory config that varies the model. Note that these benchmarks are not cheap to run – so this isn’t something you’ll want to do automatically. We recommend running them when new models come out, or when you are considering changes in your agent prompts, skills, or other agent context.
The result of the benchmark includes not just the overall recommendation, but detailed reports on how each model fared on each input task on each dimension:
Warpbench results
Now, you can use the results to improve your factory’s performance. In Warp Factories, we support this with custom model routers. These are classifier-driven routing rules that dynamically pick the best model configuration based on a classification prompt. In this case, I made a model router that classifies simple frontend tasks in our server codebase to use Grok 4.6 (med), which was top on our internal benchmark for these tasks. Like everything else in Warp Factories, custom model routers are defined in code and the agent can create and tweak them.
A custom routing rule for Grok 4.6 for simple server UI changes
Try Benchmarks today
We believe Benchmarks, combined with
self-improvement
, form two foundational capabilities for moving from the realm of operating coding agent systems on vibes to engineering systems that optimize cost and productivity.
Our mission  is to provide the world’s best engineering teams with the tools to build, measure and optimize their own workflows using any underlying model and harness on open infrastructure. These capabilities will help teams ship better software more quickly and efficiently.
Apply for Warp Factories early access
today. We are offering $10k in factory usage for qualified teams.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Aug 18, 2026
|
Product
14
min
Introducing Warp Factories - open, flexible infrastructure for building your software factory
14
min
Aug 4, 2026
|
Product
6
min
Introducing the Warp Agent CLI: a CLI coding agent that does what others can't
6
min
Aug 3, 2026
|
Product
7
min
How to build a cloud software factory - computer use verification
7
min
Jul 18, 2026
|
Product
4
min
Get agents off your machine
4
min
May 20, 2026
|
Product
6
min
Bring your own inference to Warp
6
min
View all articles
