---
title: "How Snorkel runs realistic agent simulations with Modal"
url: "https://modal.com/blog/how-snorkel-runs-realistic-agent-simulations-with-modal"
fetched_at: 2026-11-07T10:01:30.571796+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# How Snorkel runs realistic agent simulations with Modal

Source: https://modal.com/blog/how-snorkel-runs-realistic-agent-simulations-with-modal

Snorkel
, a frontier AI data lab, develops and validates complex datasets to train and evaluate AI systems. Snorkel’s Agentic Data Platform combines human experts with specialized, continually learning agents to produce higher quality data, faster. Snorkel’s platform underpins systems that process trillions of queries and records across frontier AI labs and top-tier enterprises, supporting data curation, model evaluation, and agent benchmarking.
A central and growing part of Snorkel’s work is evaluation: building rigorous benchmarks and running large-scale simulations to verify model performance gains. Today, Modal powers inference for the open-weight models that Snorkel is evaluating as well as GPU and CPU sandboxes for millions of simulations per month.
Creating realistic environments with GPU and VM Sandboxes
Snorkel needed to model a wide variety of simulations at scale. They evaluate agents across a broad range of tasks: coding (they’re a contributor to Terminal-Bench), infrastructure, ML engineering, and more.
Accurately measuring an agent requires creating a realistic environment for it to work in. Without a realistic environment, it’s hard to know whether an agent failed because it didn’t have the tools it needed or whether it failed because of its capabilities. But what tools an agent needs varies across the benchmarks that Snorkel creates. An ML agent needs access to a GPU to train a model, while an infrastructure agent may want access to a full Linux Kernel.
Snorkel used Modal’s sandboxes to reproduce complex environments, including multi-service systems and GPU-enabled workloads. Comprehensive GPU sandbox support was a requirement for their team, and Modal was the only Sandbox provider able to meet their needs at scale. Having one provider for both GPU and CPU sandboxes also simplified their infrastructure and cost tracking.
“For agent simulations to be meaningful, the environment needs to represent the real world the agent will operate in. Modal’s VM sandboxes let us recreate complex, production-like systems — from multi-container infrastructure workloads to GPU-enabled deep learning environments — across the millions of simulations we run each month.”
Rustem Feyzkhanov
Sr. Manager AI Platform
While Snorkel creates millions of Sandboxes per month, they often peak at tens of thousands of Sandboxes an hour. As new models are released or “old” models are tuned, Snorkel’s team runs them against a mix of public and proprietary benchmarks. These holistic evaluations are time-sensitive because customers typically want to know whether a model may perform well for their use-case within a day, meaning high sandbox concurrency— like what Modal offers— was a requirement.
Decreasing costs by 20% with memory bursting
Previously, the Snorkel team was estimating the CPU and memory needs of their agents when configuring a sandbox. In some cases, the agent would fail because the sandbox didn’t have sufficient resources to complete the task, rendering the result of the run invalid. In other cases, resources were over-provisioned, leading to low spend-efficiency.
Estimating the resource needs of agents is particularly difficult for two reasons: resource usage within a Sandbox is spiky, and workload shapes are not statically known. Within the lifetime of a Sandbox, there are often periods of inactivity— like when waiting for an LLM response— followed by spikes when something like a grep command is running. Because all the code running in a Sandbox is LLM-generated, it’s also difficult to estimate specific resourcing needs. This is especially true for Snorkel because of the large variety of benchmarks they run.
To simplify provisioning, Snorkel began using Modal’s bursting, where individual Sandboxes can elastically expand the memory or CPU resources they need at a given point. Customers are charged for the resources the Sandbox is using at a given time or the resources that were originally requested, whichever is higher. They’re still early in the adoption process, with ~10-15% of Snorkel’s sandboxes using bursting today.
Random sample of 5,000 Snorkel’s Sandboxes plotted by peak CPU and Memory usage as a % of the resource request.
Bursting made it possible to allocate CPU and memory at configuration while retaining flexibility at runtime. For the Snorkel team, this meant the reliability of runs increased as the number of runs failing due to resource limits decreased. Bursting also allowed Snorkel to lower the amount of resources they were requesting for their Sandboxes without compromising reliability— leading to substantial cost savings.
“We need to support tasks from SMEs or agents, without over-provisioning infrastructure. Bursting gives us flexibility at configuration and runtime, avoiding over-provisioning and saving us around 20% on our total Sandbox bill.”
Rustem Feyzkhanov
Sr. Manager AI Platform
Serving open-weight inference
Running simulations requires more than an environment; it requires inference. Snorkel’s team needed to quickly stand up endpoints, run benchmarks, and then stand them down across new and fine-tuned models.
Sometimes, like when performing d0 evaluations of new models, Snorkel can use an off-the-shelf endpoint. Other times, they need to host and serve a custom model that a customer has fine-tuned.
Snorkel uses a mix of Modal’s Shared and Dedicated Endpoints to serve inference, allowing them to quickly stand up models and load custom weights without involving their infrastructure team.
“Modal’s serverless GPUs mean we can bring our own model or use shared inference, use the inference for different benchmarks, all while scaling really fast and reliably.”
Rustem Feyzkhanov
Sr. Manager AI Platform
What’s next
Agents keep creating new infrastructure needs, and Snorkel's benchmarks have to keep up. Over the roughly six months Snorkel has worked with Modal, they've adopted new capabilities as Modal shipped them like VM Sandboxes.
“With agents, infrastructure becomes a very interesting challenge, and the ability to move fast is important. The AI industry is all about moving fast, and Modal moves fast with us.”
Rustem Feyzkhanov
Sr. Manager AI Platform
Today, Snorkel relies on Modal for running inference and Sandboxes to power their simulations. In the future, they plan to evaluate Modal as a training solution, enabling them to use their data for the full loop of model improvement from training through evaluation.
“At the end of the day, improving models requires two things: data and compute. Modal enables us to focus on the data while providing the infrastructure for our compute.”
Rustem Feyzkhanov
Sr. Manager AI Platform
