---
title: "Self-Improving Agents, Powered by Your Evals"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/self-improving-agent"
scraped: "2026-05-10T01:27:07.208980+00:00"
lastmod: "2026-01-16T21:10:01.000Z"
type: "sitemap"
---

# Self-Improving Agents, Powered by Your Evals

**Source**: [https://fireworks.ai/blog/self-improving-agent](https://fireworks.ai/blog/self-improving-agent)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Self Improving Agent
Self-Improving Agents, Powered by Your Evals
PUBLISHED
12/17/2025
Table of Contents
What kind of gains are we talking about?
Why care about prompt optimization at all?
What Did GEPA Learn?
System output, before and after
Pushing on Agents Even Further
Table of Contents
Table of Contents
What kind of gains are we talking about?
Why care about prompt optimization at all?
What Did GEPA Learn?
System output, before and after
Pushing on Agents Even Further
Table of Contents
TL;DR:
Eval Protocol is a unified eval interface that powers both prompt optimization and RL on the same evaluation function. Author your evaluator once, and instantly unlock huge gains on open-source models.
Imagine: You’ve built an eval suite that tells you where your agent fails, but it doesn’t tell you how to fix it. So you tweak the prompt—add a few instructions, maybe some examples, re-run the evals, watch the number wobble up or down. After a while, it’s just hours of staring at failure cases and guessing what the next prompt change needs to be.
Eval Protocol is introducing a new integration to help eliminate some of this prompt guesswork:
GEPA
inside EP. GEPA runs on your existing eval setup—datasets, metrics, and task constraints—to convert failure signals into precise, enforceable prompt improvements and deliver automatic, inspectable gains to your agent, without touching weights.
Reflective prompt optimization uses the evaluation framework you already trust, tightening the loop from failure case to shipped improvement. Self-improving prompts are a step towards the broader vision for Eval Protocol: a single eval interface that powers both prompt optimization today and RL on the same evaluation function.
What kind of gains are we talking about?
Eval Protocol is an
open-source evaluation solution
for doing reinforcement learning, across any language, environment, or framework. With our EP + GEPA integration, we tackled a Text2SQL problem by defining the evals and running our agent with GEPA-based prompt optimization on Qwen3-32b.
Without touching the model weights, our team was able to achieve a 10% improvement in test set accuracy and a >5% increase in validation set accuracy, and then further improve model accuracy with RFT on the same eval.
Metric
Before
After GEPA
After GEPA + RFT
Test set accuracy
26.7%
43.3%
51.6%
This was achieved on the same model, across the same tasks and eval definitions. GEPA helped dramatically (and automatically) improve this system prompt with no other extra evaluation setup outside of the existing evaluation suite, in only ~45 minutes of search.
Eval Protocol, now with GEPA-based prompt optimization
Eval Protocol
gives you a clean, structured way to write down your evals: datasets, metrics, scoring logic, and task-specific constraints all live in one place.
On top of that evaluation layer, EP now supports GEPA as a first-class prompt optimizer. Via DSPy, it handles prompt manipulation and candidate evaluation. In your code, you define your eval as usual, then call
GEPA
through our DSPy integration in just a couple of lines. GEPA will:
•
Look at which examples pass/fail
•
Automatically propose structured edits to the prompt
•
Keep whatever reliably moves your metric up
•
Spit out an optimized system prompt you can diff, inspect, and plug back into your agent
In practice, this means you write your evals once with Eval Protocol and watch as those same evals keep paying dividends. Now those evals aren’t just measuring performance, they’re improving it.
Here’s what the interface looks like. Plug in the below to any code with an @evaluation_test defined, and watch as your agent automatically improves.
1
2
3
4
5
6
7
8
9
10
trainer
=
GEPATrainer
(
test_sql_gepa
)
reflection_lm
=
build_reflection_lm
(
"fireworks_ai/accounts/fireworks/models/deepseek-v3p1-terminus"
)
optimized_program
=
trainer
.
train
(
)
evaluation
=
trainer
.
evaluate
(
optimized_program
)
optimized_prompt
=
trainer
.
get_optimized_system_prompt
(
optimized_program
)
Why care about prompt optimization at all?
Prompt optimization is a way to squeeze out better performance from your agent, before moving on to more complicated methods like running reinforcement learning.
If you’re already running evals, you’re probably hitting a familiar wall: you’ve picked a solid model, you’ve got a decent eval suite, and have done a couple of rounds of prompt engineering. And then the curve just… flattens. Getting another 5–10 points of performance usually feels like it requires something heavy-weight: swap to a bigger (and more expensive) frontier model, fine-tune or run RLHF with new data, or accept that this is just how well it does.
Automatic prompt optimization gives you a cheaper, lower-friction option: use the evals you already have to automatically search for better prompts and improve performance, without changing models or running any training.
Real Case Study: Text2SQL Agent
We tried this method on a Text2SQL agent and saw the gains mentioned in model performance (+10% in test set accuracy).
Here was our text-to-SQL benchmark setup:
Set up the database
: a synthetic OpenFlights-style database (airlines, airports, routes)
Create the data
: 243 natural-language questions → SQL queries → ground truth results
Define the evaluation process:
Generate a DuckDB SQL query from the model
Execute both the generated query and the ground truth query
Compare result sets (ignoring ordering, with appropriate tolerances)
Mark as pass/fail based on whether they return the same data
Split the data into:
A validation set used as the optimization playground
A test set held out until the end
After all this, we took DeepSeek V3 and ran GEPA prompt optimization on its system prompt using the evals, which were defined in
Eval Protocol
.
What Did GEPA Learn?
When we ran GEPA against the eval, it found that most failures fell into a few buckets:
•
Inconsistent output naming
– the query was logically right, but column names didn’t match what the eval expected.
•
Incomplete answers
– questions asking for multiple metrics only got a subset in the SELECT.
•
Incorrect relationships
– joins or filters didn’t follow the actual relationships between tables.
The original system prompt basically just told the model, “you are an expert SQL analyst.” But, after multiple iterations with GEPA, we were able to achieve the following final system prompt:
System prompt that GEPA learned
Note: trimmed for brevity. There were 3 more requirements.
The optimized prompt encodes those patterns as concrete rules:
•
A strict contract for how outputs should be named and formatted
•
Reminders to include all requested fields in the result
•
Guidance on using the right keys and conditions when joining and filtering.
In short, GEPA turned recurring eval failures into explicit prompt constraints, giving the same model a much sharper task specification without changing any weights.
System output, before and after
Better prompts resulted in better results for our Text2SQL use case. The unoptimized system prompt produced a correct SQL query 0 times out of 8 tries, one of which is shown as the before image. After using the optimized system prompt, the Text2SQL agent produced a correct SQL query 3 out of 8 tries.
Before
Output SQL, before GEPA optimization
After
Output SQL after prompt optimization
Pushing on Agents Even Further
After pushing on the prompt and optimizing it, we wanted to see how we could push quality even further. The answer was in Fireworks’ RFT product, which helped us test how an RFT training run would go using this optimized system prompt.
We trained the following job using Qwen3-32b, a much smaller model than DeepSeek-V3. Here, we ran the experiment over 4 epochs, seeing absolute score gains of ~20%. We’ve included the code for our experiment and instructions on how to run it in
the same repo
as the rest of our GEPA example.
RL on top of GEPA with additional gains
At a high level, this is the pattern we’re betting on: you define an eval once, and that same evaluator powers everything—prompt search today, RL-style training tomorrow. GEPA inside Eval Protocol is one concrete example of that loop: take the evals you already trust, turn their failures into prompt constraints, and then, when you’ve squeezed out as much as you can from prompting, reuse that same eval as the objective for RFT or RL. No separate reward models, no parallel eval stack to maintain—just one evaluation interface that sits in the middle of agents, prompt optimization, and training. If you already have evals, you’re most of the way there; the rest is wiring in GEPA and (optionally) RFT. You can find the full examples and code paths in the Eval Protocol docs.
See more in our docs here:
eval-protocol
!
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
