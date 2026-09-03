---
title: "How Botika runs full-stack generative AI on Modal"
url: "https://modal.com/blog/botika-case-study"
fetched_at: 2026-09-03T10:00:50.564825+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# How Botika runs full-stack generative AI on Modal

Source: https://modal.com/blog/botika-case-study

Botika builds agentic e-commerce teams that automate visual production for global fashion brands. Powered by custom models researched and trained in-house, Botika handles the entire pipeline - from 4K image generation to real-time personalization at scale.
Behind that product is a full-stack AI operation: proprietary foundation models with tens of billions of parameters, a data pipeline processing a 100-terabyte image dataset, and roughly 15 models serving production inference. All of it runs on Modal.
“
"I don't think Botika would have existed in its current form without Modal," says Eran Dagan, Botika's co-founder and CEO. "We would have needed probably twice as many people."
”
— Eran Dagan,
Co-founder & CEO
In search of a cloud built for AI workloads
Dagan and his co-founder started building in generative AI in 2018, years before the tooling existed to support it. So they built the tooling themselves: node autoscaling, cold start mitigation, Docker image optimization, GPU fleet management.
“
It might be easy to get started with one VM running CUDA, but it's very hard once you want to really scale. I remember our Kubernetes fleet, and just the amount of work chasing down why a certain node was unhealthy, you can often waste weeks just hunting down random driver bugs.
”
— Eran Dagan,
Co-founder & CEO
In 2023, Dagan went looking for something better. He evaluated the major GPU cloud options and found them either too rigid or too custom. Then he spotted Modal on an AI infrastructure landscape chart, the one name he didn't recognize, and asked for beta access.
“
I remember the moment I typed modal run and it just worked. I was like, OK, this just saved me a week of work right here and now.
”
— Eran Dagan,
Co-founder & CEO
Now, Botika runs an end-to-end operation on Modal, from their data pipeline to production inference.
A 100-terabyte data pipeline with no orchestrator
Botika's data pipeline turns raw fashion imagery into training data: generating features, filtering, tagging, clustering, and aggregating across dozens of steps. It runs about a dozen different AI models, from open-source VLMs doing zero-shot tagging to classifiers Botika researched and built in-house, each in its own specialized environment on its own GPU type.
The pipeline originally ran on GCP Batch, and before Modal, moving data end to end took weeks of launching VMs, running scripts, and tweaking scaling parameters by hand. The alternatives were no better: adopt a full orchestrator like Airflow and take on the DevOps burden, or keep compromising on velocity.
"By the time a job boots on GCP Batch, you could have launched a thousand jobs on Modal," Dagan says. "The simple logic of 'once this job is done, run this one' is so easy to express on Modal, and so difficult without a full-blown orchestrator anywhere else."
With Modal, just the application code files allow the team to process a 100-terabyte dataset with less than a 1% error rate, across thousands of concurrent containers, using nearly every GPU type Modal offers.
Enabling rapid cutting edge research
Training their own foundation models means Botika researchers run thousands of experimental training runs to push their models forward. Modal has played a crucial part in allowing the team to iterate at the pace they want.
Before Modal, each researcher could launch maybe one or two experiments a day. Now a single researcher runs 50: plug Claude into Modal, launch 50 short experiments, pick the ones that work, and scale the winners up. Researchers spin up their own workstations on Modal for rapid iteration, then send jobs to run in the background while an agent works on something else, an experiment throughput closer to a frontier lab than a startup research team.
"You give a smart person, and an AI agent that translates that person's thoughts, access to very fast and very responsive compute, and you just get a ton more work done," Dagan says. "As a founder, I see how fast every department is moving. Without Modal, the research team would be six months in the past."
Botika trains its own foundation models for 4K image generation, jobs that run for weeks across many GPUs. Few teams of Botika's size train at this scale at all; fewer do it on infrastructure they didn't have to assemble. The team was one of the first to adopt Modal's multi-node training, back when it was still behind an experimental flag, and had cross-GPU communication and RDMA networking running from day one.
Most recently, the team stood up its own reinforcement learning infrastructure in less than a day, using nothing but Modal primitives. Reward servers run as spawned Modal functions. Training jobs spawn additional jobs mid-run for iterative reward modeling. Rollouts were easy to wire up.
Because everything lives in one place, the reward servers the research team built for RL training get reused directly in the production inference stack. "With SageMaker or Vertex, that scenario just wouldn't work," Dagan says. "I have a server, and I want to access it during training, during inference, and during my data pipeline. On Modal there's no jumping between tools. It saves us a lot of time and complexity."
Inference that scales with demand
Botika serves about 15 models in production at any given moment, spanning L4s, L40S, A100s, and H100s. Modal handles queuing, autoscaling, and cold starts, so there's no Redis queue bolted in front of every service.
AI traffic breaks the traditional scaling model, so here, it’s Modal’s ability to elastically scale at a moment’s notice that Botika’s team values the most.
“
We can double or 3x traffic in seconds and nobody knows about it. Nobody at the company cares from a technical standpoint, we know Modal will just work.
”
— Eran Dagan,
Co-founder & CEO
The cloud that gets out of the way
“
We don't really need to work with traditional clouds anymore. Everything that is compute, and for us that's 99% of the business, runs on Modal.
”
— Eran Dagan,
Co-founder & CEO
For a team like Botika, it’s crucial that they have infrastructure that enables them to do the work they need to, without forcing them to conform to a certain way of building. On Modal, Botika runs its application in ways that aren't Modal-specific, runs open-source and custom frameworks without modification, and never touches a proprietary black box. "It's such an integral part of our workflow now. Somebody needs to run something, you write a function, modal run, and it just works."
Every engineer Dagan has onboarded reaches the same conclusion: there's no going back to the Kubernetes way.
