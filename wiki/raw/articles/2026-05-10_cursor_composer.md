---
title: "Composer: Building a fast frontier model with RL · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/composer"
scraped: "2026-05-10T01:19:45.542263+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Composer: Building a fast frontier model with RL · Cursor

**Source**: [https://cursor.com/blog/composer](https://cursor.com/blog/composer)

Blog
/
research
Oct 29, 2025
·
research
Composer: Building a fast frontier model with RL
5 min read
Composer is our new agent model designed for software engineering intelligence and speed. On our benchmarks, the model achieves frontier coding results with generation speed four times faster than similar models.
We achieve these results by training the model to complete real-world software engineering challenges in large codebases. During training, Composer is given access to a set of production search and editing tools and tasked with efficiently solving a diverse range of difficult problems. The final result is a large-scale model optimized for high-speed use as an agent in Cursor.
Our motivation comes from our experience developing Cursor Tab, our custom completion model. We found that often developers want the smartest model that can support interactive use, keeping them in the flow of coding. In our development process, we experimented with a prototype agent model, codenamed Cheetah, to better understand the impact of faster agent models. Composer is a smarter version of this model that keeps coding delightful by being fast enough for an interactive experience.
Composer is a mixture-of-experts (MoE) language model supporting long-context generation and understanding. It is specialized for software engineering through reinforcement learning (RL) in a diverse range of development environments. At each iteration of training, the model is given a problem description and instructed to produce the best response, be it a code edit, a plan, or an informative answer. The model has access to simple tools, like reading and editing files, and also more powerful ones like terminal commands and codebase-wide semantic search.
To measure progress, we constructed an evaluation that measures a model's usefulness to a software developer as faithfully as possible. Our benchmark, Cursor Bench, consists of real agent requests from engineers and researchers at Cursor, along with hand-curated optimal solutions to these requests. The resulting evaluation measures not just the agent’s correctness, but also its adherence to a codebase's existing abstractions and software engineering practices.
Reinforcement learning allows us to actively specialize the model for effective software engineering. Since response speed is a critical component for interactive development, we incentivize the model to make efficient choices in tool use and to maximize parallelism whenever possible. In addition, we train the model to be a helpful assistant by minimizing unnecessary responses and claims made without evidence. We also find that during RL, the model learns useful behaviors on its own like performing complex searches, fixing linter errors, and writing and executing unit tests.
Efficient training of large MoE models requires significant investment into building infrastructure and systems research. We built custom training infrastructure leveraging PyTorch and Ray to power asynchronous reinforcement learning at scale. We natively train our models at low precision by combining our
MXFP8 MoE kernels
with expert parallelism and hybrid sharded data parallelism, allowing us to scale training to thousands of NVIDIA GPUs with minimal communication cost. Additionally, training with MXFP8 allows us to deliver faster inference speeds without requiring post-training quantization.
During RL, we want our model to be able to call any tool in the Cursor Agent harness. These tools allow editing code, using semantic search, grepping strings, and running terminal commands. At our scale, teaching the model to effectively call these tools requires running hundreds of thousands of concurrent sandboxed coding environments in the cloud. To support this workload, we adapted existing infrastructure we built for Background Agents, rewriting our virtual machine scheduler to support the bursty nature and scale of training runs. This enabled seamless unification of RL environments with production environments.
Cursor builds tools for software engineering, and we make heavy use of the tools we develop. A motivation of Composer development has been developing an agent we would reach for in our own work. In recent weeks, we have found that many of our colleagues were using Composer for their day-to-day software development. With this release, we hope that you also find it to be a valuable tool.
—
¹ Benchmarked on an internal benchmark in the Cursor tool harness. We group models into classes based on score and report the best model in each class. "Fast Frontier" includes models designed for efficient inference such as Haiku 4.5 and Gemini Flash 2.5. "Best Open" includes recent open weight model releases such as Qwen Coder and GLM 4.6. "Frontier 7/2025" is the best model available in July of this year.  "Best Frontier" includes GPT-5 and Sonnet 4.5, which both outperform Composer. For the Tokens per Second calculation, tokens are standardized across models to the latest Anthropic tokenizer.
Filed under:
research
Author
:
Cursor Team
