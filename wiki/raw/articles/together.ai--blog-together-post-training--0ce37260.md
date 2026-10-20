---
title: "Together Post-Training: frontier-grade model shaping, the way that fits you"
url: "https://www.together.ai/blog/together-post-training"
fetched_at: 2026-10-20T10:01:31.048424+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Together Post-Training: frontier-grade model shaping, the way that fits you

Source: https://www.together.ai/blog/together-post-training

We are introducing Together Post-Training, a new service for building custom models on our platform — both from environment rewards via RL and supervision data via SFT. This service is designed to give you flexible and efficient model shaping without the heavy infra burden.
Together Post-Training makes it easy to define the training loop, while we co-optimize the systems and infrastructure underneath for model quality and training speed. Nothing now stands between you and the best model that is
uniquely yours
.
The value of custom models
In 2026, training custom models for your AI workloads is no longer a niche topic. Companies are actively exploring it to reduce costs and improve task-specific performance. Instead of fixing model behaviors and improving their efficiency via context or harness engineering, many AI-native and AI-forward organizations are training specialist agents, matching the quality of frontier models at a fraction of the cost and runtime. On top of that, training the model yourself yields greater ownership and flexibility: the resulting checkpoint can be deployed in any location, further refined, or even used locally.
At Together, we want to empower every AI developer with the ability to get the best model for their task, as conveniently as possible. Post-training a great model requires many iterations on data curation, training algorithms, and evaluation protocols. On top of that, infrastructure for RL is getting ever more complex, with a fine line between “an efficiency optimization” and “a silent bug that holds back your runs”. Doing so for large models reliably and at scale presents its own set of challenges.
Frontier labs have entire teams solving each of the above problems. Since tackling all challenges at once is a big investment, many companies that could benefit from post-training never start it, or start and stall. Together Post-Training handles all optimizations and infrastructure without getting in the way, and our forward-deployed team partners with our customers to help with the end-to-end workflow. This lets every researcher or domain expert focus on what they do best while we take care of the rest.
Together Post-Training at a glance
As the complexity of post-training continues to evolve, so should the tooling around it. Together Post-Training provides a set of common abstractions familiar to ML developers, as well as control over the resources used by each experiment, while making sure that all computations under the hood are fast, cost-efficient, and, most importantly, correct.
We built our service to offer the highest degree of flexibility for your experiments. You can run LoRA training, including multiple LoRA adapters sharing the same GPU capacity, as well as full-weight experiments for select models. In contrast to our
fine-tuning service
, the entire training loop of Together Post-Training is yours to define. You can use any data, environments, or agentic harnesses that suit your setup best, and add any steps you need (such as logging or external benchmarking) throughout the training process. The entire workflow is as follows:
A high-level summary of using Together Post-Training. Left: commands executed on the user side, right: service components running on Together’s side.
All experiments run on Model Resources — GPU allocations that are fully yours, not competing with others’ requests for priority. Each Model Resource can hold one or several Training Sessions, where each one corresponds to a single experiment using the same base model (for example, one set of LoRA adapters). This means you get the best rollout and training performance, as you never have to compete with other users’ requests executing on the same hardware. At the same time, dedicated GPU allocations mean you can run full-weight finetuning, going beyond LoRA when adapting to large knowledge-intensive tasks.
Once you allocate the model resource and start the session, you can execute each step of the training loop. Each session contains a Trainer instance responsible for running forward/backward steps and updating the weights, as well as Generator instances for executing rollouts from the policy. For every model, we heavily optimize training and rollout performance, making sure all operations are fast and numerically aligned across stacks. In the case of SFT, you can start a model resource with 0 generators to save costs. You decide the point at which the trainer parameters are sent to the generator; we also support asynchronous RL for high GPU utilization of both components at all times, especially with long agentic rollouts.
While we support a number of standard losses (from cross-entropy and GRPO to CISPO and DPPO), we also allow computing a custom training objective locally and sending its gradients to the Trainer for computing the updates.
Example of training with a custom loss from
Together Post-Training docs
Together Post-Training launches with a range of leading open-weight models, including Muse Spark Open, GLM 5.3, Kimi K3, and Qwen 3.8-27B. We will expand the selection in the coming weeks, making sure you can use both the highest-capability frontier LLMs and efficient smaller models.
Quality, performance, and efficiency
Delegating the internals of post-training infrastructure can be a daunting decision. Our team has first-hand experience catching silent bugs in complex machine learning systems, from pushing the frontier of RL research to training LLMs that have served millions of users. We understand that
the best training stack is the one that gets you the best model
, and building such infrastructure demands careful implementation and co-design across all components.
For these reasons, we prioritized quality of output models as our north star in the development of the service. One notorious example of issues affecting RL results is the alignment between training and inference engines: if the same model weights produce slightly different outputs due to mismatching numerics, the whole run might underperform or even collapse. We eliminate numerous sources of policy drift across training and inference, using both standard techniques like
Rollout Routing Replay
and advanced optimizations driven by our research in training stability.
Beyond model quality, we also work to make each run as fast and as efficient as possible, because post-training requires multiple iterations: the sooner a run finishes and the less it costs, the more ideas you get to test. Most of the time in RL is spent on generating rollouts, which allows us to capitalize on years of research and engineering behind Together’s inference products. Our rollout engines draw on the same optimizations as our serving stack. For multi-turn agents, intelligent caching and routing minimize redundant computations while keeping memory costs bounded. On the training side, optimized parallelism and sequence packing speed up both SFT and RL steps.
With Together Post-Training, you size each experiment to what it needs and do not pay more. If your experiment is bottlenecked by rollout concurrency, you can request the exact number of sampler replicas. Several LoRA experiments can share one model resource, so running a sweep doesn’t mean reserving more GPUs for every setup. We bill every model resource per GPU-minute, yet thanks to many optimizations of our dedicated and multi-LoRA serving stacks, the overall costs of training drop below token-based pricing as soon as you scale up the experiments.
Optimized deployment after training
When the post-training experiments are finished, it might be important to run each resulting model side by side to compare their outputs. We now support
multi-LoRA adapter serving
in Dedicated Model Inference: instead of starting a separate production deployment for each run, you can swap the adapters at your convenience in a single GPU deployment, helping you lower the serving costs.
Lastly, converting the model to run at the highest throughput in production means it potentially executes in lower precision, in a different hardware configuration, and with different kernels compared to rollout generation. Through a combination of algorithmic and systems improvements, we ensure that each training checkpoint retains the quality in serving, even after switching from multi-LoRA sampling to a fully performant
merged inference in FP4 precision
.
Getting started
To begin your first post-training experiments, install the latest
Together SDK
and
read the docs
. We also provide a selection of cookbooks that can help you get started with Together Post-Training, which are available at
github.com/togethercomputer/post-training-cookbook
. These cookbooks provide examples of training with GRPO on a standard GSM8K benchmark, implementing DPO as a custom loss, or training multiple LoRA adapters within the same model resource. If you already have a setup that uses post-training services such as Tinker API, we also offer a simple way to migrate from them. You can replace one line in your scripts, and everything else can stay the same:
-import tinker
+import together.post_training.tinker as tinker
Read our
Tinker migration guide
to learn more.
How AI-native companies are using Together Post-Training today
Before this launch, we worked with a select group of organizations pushing the frontier of custom models. We granted them early access to our service over the past few months; the feedback we received was invaluable in developing the product which now everyone can use. Hear from the teams themselves:
“We had a great experience with the Together Post-Training platform from day one. The high degree of control and flexibility let us start running real RL experiments within a couple of hours. The service is efficient, allowing us to run up to five concurrent RL experiments on the same GPU capacity. The Together Research team was an exceptional collaborator throughout the training process, giving us feedback on model selection, training techniques, reward functions, and training efficiency.”
– Anthony Li, Associate Director of Data Science,
Deel
“At Jack & Jill, we build two AI agents: Jack for professionals, and Jill for companies, who recruit from Jack’s network of professionals who’ve opted in to being introduced. We used Together Post-Training to post-train a model that predicts which candidates a hiring manager will want to meet, a core step in Jill’s search. Onboarding was easy, their team helped design our experiments, and their forward-deployed engineers wrote the scripts that got us to first results. We matched a closed-source model’s quality in offline evaluations, using an open-source model that’s significantly cheaper to serve.”
– Oliver Normand, Founding Engineer,
Jack & Jill
“We’ve been collaborating with the Together team since the launch of its Post-Training beta in April. With the latest iteration, seamless self-onboarding made it easy to quickly launch full-scale agentic RL runs. The Post-Training service has proven to be exceptionally intuitive, flexible, and powerful for scaling sophisticated agentic workloads.”
– Adit Jain, Researcher,
Collinear AI
Build with Together Post-Training
With the launch of Together Post-Training, we’re turning frontier-grade model customization into a reliable, flexible and efficient service. The next step is for you to make the most of it. For the first eight weeks, we are offering Together Post-Training at a reduced price of $9 per GPU-hour of B200 usage. Learn how to
get started
today — we’re excited to see what you will build.
But you don’t have to do this alone. For companies that want a partner, our forward-deployed engineers work alongside your team across the full post-training lifecycle. They’ll start with helping select the right open model and agent harness for your use case, work with you on your data and training environments, and then help with evaluations and shipping your own optimized endpoint.
If you would like to collaborate with Together on training models for your organization, feel free to
reach out to us
.
