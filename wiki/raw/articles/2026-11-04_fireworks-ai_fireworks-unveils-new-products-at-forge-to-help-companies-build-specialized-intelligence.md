---
title: "Fireworks unveils new products at Forge"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/fireworks-unveils-new-products-at-forge-to-help-companies-build-specialized-intelligence"
scraped: "2026-11-04T06:00:12.300551+00:00"
lastmod: "2026-11-03T22:14:50.000Z"
type: "sitemap"
---

# Fireworks unveils new products at Forge

**Source**: [https://fireworks.ai/blog/fireworks-unveils-new-products-at-forge-to-help-companies-build-specialized-intelligence](https://fireworks.ai/blog/fireworks-unveils-new-products-at-forge-to-help-companies-build-specialized-intelligence)

There are two visions of the future: A world where all the intelligence is owned by a few closed frontier labs. Or, a world where every company owns the intelligence that makes their organization unique.
Fireworks Forge
is for people building that second future. Our first annual conference opens today, bringing together leaders from AI-native startups, global enterprises, open-weight model labs, and more.
Advances in open-weight models, including models from NVIDIA, Meta, and Reflection AI, available on Fireworks, are giving companies more choice in how they build AI. At the conference, we unveiled new products to help companies turn advances in open models into intelligence built around their own expertise, data, and tasks.
The launches address the practical barriers teams face as they move AI into everyday work: agents that take too long to respond, models that need to perform better on company-specific tasks, and infrastructure that must meet enterprise requirements for cost, control, and security.
Faster agents, with costs that fit the workload
AI agents often make multiple model calls to complete a single task. Each call adds to the time a customer or employee waits for a result, while running more agents simultaneously increases capacity pressure and cost. Teams need speed for time-sensitive work and more economical options for tasks that can wait.
Fireworks
Ultra-fast
, powered by NVIDIA Blackwell GPUs, accelerates those time-sensitive workloads. It is now available in public preview, delivering speeds up to 1,500 tokens per second as demonstrated on
DeepSeek V4.1 Flash
. That speed is especially valuable when delays accumulate across multiple steps: in a benchmarked 30-turn agent task, completion time fell from 1 minute to 8 seconds at ultra-fast.
For workloads where cost matters more than immediate completion,
Background Mode
gives teams a lower-cost runtime option at half price. This mode lowers cost per task for eligible work that can wait, such as data generation for evaluations and overnight research.
Multi-day Prompt Caching lowers costs for repeated context, while higher rate limits
support more concurrent agents.
Figure 1: Persistent agents pay for reprocessing context every time they resume after a pause, and background agents pay peak prices for work that could wait. Multi-day prompt caching and Background Mode reduce each of those costs.
Specialized models can also improve inference economics.
Ember-1
, a Fireworks model available on serverless and dedicated deployments, used about 40% fewer tokens while maintaining comparable quality to Kimi K3 in our evaluations.
Figure 2: Ember-1 sits on the quality-cost frontier across five industry benchmarks, scoring within about a point of Claude Opus 5 at roughly a fifth of the cost per task. Source: Introducing Ember-1 blog
Together, these capabilities help teams match inference performance and spending to the demands of each workload.
Fireworks Nexus: More model choice in the tools employees already use
Employees increasingly rely on AI for coding and everyday work, but switching models can mean leaving a familiar tool or adding another subscription to manage. Companies need to give people more model choice while maintaining visibility into spending.
Fireworks Nexus
brings open models into the AI coding and coworking tools people already use, alongside their existing AI subscriptions. It combines open and closed models with personalized model selection and cache awareness, helping people use models suited to their work while giving organizations centralized spending visibility and controls.
Figure 3: Fireworks Nexus tracks spend by model for every day of the month and compares it with an estimated all-Opus 5.5 baseline, so finance can see where each dollar went and what routing saved.
Today we launched
Nexus Desktop
, joining the Nexus CLI. Nexus now runs in the Codex app, Claude Desktop, and OpenCode, extending personalized model selection beyond coding to everyday knowledge work. New Pro plans start at $8 per month, and Teams plans start at $10 per seat per month. Enterprise plans add SSO, governance, shared budgets, and access controls.
Figure 4: Nexus Desktop connects the tools you use every day to Nexus with one switch per tool, so teams get model routing without touching a terminal.
As workloads grow,
higher serverless rate limits
, now generally available, let teams run more work concurrently without reserving dedicated capacity.
Elastic Burst
, also generally available, allows customers to exceed their normal usage ceiling when spare capacity is available, with no code or pricing changes.
Training: Turn your expertise into better models
Choosing the right model can improve results and reduce costs. Training goes further, teaching a model what good looks like for your particular task. That can mean exceeding the quality of an existing model or getting the performance you need from a smaller, faster one. Often it’s both. At Forge, we made it easier to deliver those gains and bring them into production.
That starts with knowing what to improve.
No Eval, now in private preview, helps turn production traces and product signals into task-specific evaluations, so teams can identify where models fall short and measure whether training closes the gap. This addresses one of the biggest barriers to training your own model because writing your own evals could take weeks of data labeling and then grading.
Figure 5: Turn production feedback into your training loop.
Specialized Model Inference
,
now in public preview, extends a serverless approach to serving LoRA adapters, starting with GLM 5.3 Flash. Teams can evaluate a trained model and serve it through the Fireworks Serverless API with per-token pricing, no dedicated deployment to size, and no serving charge while it sits idle. They can keep a model in use while experimenting with the next version.
Teams can get started with
free training on Muse Glimmer 30B
through November 30, including supervised fine-tuning, direct preference optimization, and reinforcement learning.
Enterprise control, wherever models need to run
As AI moves into critical business workflows, enterprises need to govern model use, control spending, and maintain activity records. Some also need greater control over where their AI infrastructure runs and how their data is protected.
Fireworks now offers generally available model governance, spending controls, and exportable audit logs. Previews of centralized account management, regional data controls, and customer-managed encryption extend those capabilities for organizations with more demanding operational requirements.
For enterprises that want to leverage their own infrastructure,
Fireworks Sovereign
, now in private preview, brings the company’s inference engine to customers’ cloud, neocloud, or data centers. It combines technology that can double the tokens per GPU dollar, or more, with expert management that lowers total cost of ownership, helping customers run open models within their chosen infrastructure.
Inference and training run inside the customer’s environment, under the security and change-control policies it already enforces. Regulated enterprises can meet data residency and model access requirements on infrastructure they govern, and AI capacity stays in the jurisdictions they choose. Because customers own the infrastructure and pick the models, a provider’s price change or model retirement can’t set their roadmap. Fireworks already manages over 25,000 GPUs in customer environments.
Figure 6: Fireworks Sovereign runs inference on your GPUs and inside your perimeter, managed through the same control plane as Serverless and Hyperscaler Marketplace deployments.
Make your own frontier
Together, the Forge launches make specialized intelligence more practical to build, improve, and deploy. Faster inference supports responsive agents; Nexus brings model choice into employees’ daily work; training capabilities help companies improve performance on their own tasks; and enterprise controls support deployment at scale.
To join Fireworks Forge virtually,
register for the livestream
.
Announcement
Inference
Training
Routing
