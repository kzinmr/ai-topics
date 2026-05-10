---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/viberl"
scraped: "2026-05-10T01:27:02.557767+00:00"
lastmod: "2026-02-12T18:51:49.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/viberl](https://fireworks.ai/blog/viberl)

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
Viberl
VibeRL: When AI Trains AI
PUBLISHED
7/22/2025
Table of Contents
TL;DR
How RL Got Us Here
Enter VibeRL: Simplifying Fine-Tuning
What We've Learned So Far
Case Study 1: Solving Grade School Math (GSM8K)
Case Study 2: Coding Challenges (LeetCode)
Case Study 3: Real-World Function Calling
Where We're Headed
Table of Contents
Table of Contents
TL;DR
How RL Got Us Here
Enter VibeRL: Simplifying Fine-Tuning
What We've Learned So Far
Case Study 1: Solving Grade School Math (GSM8K)
Case Study 2: Coding Challenges (LeetCode)
Case Study 3: Real-World Function Calling
Where We're Headed
Table of Contents
TL;DR
•
We introduce the concept of VibeRL, an AI agent that automates complex Reinforcement Learning (RL) fine-tuning. Instead of wrestling with intricate setups, you simply provide a dataset and a prompt, and the agent handles the rest.
•
Preliminary validation on diverse tasks like math and coding shows VibeRL automatically selects optimal strategies and delivers significant results.
How RL Got Us Here
Reinforcement Learning (RL) isn't new. Think about it like training a pet - you give a command, your pet performs an action, and if it's correct, it gets a treat. Over time, your pet learns exactly what you want.
The same idea has been quietly revolutionizing AI. Techniques like Proximal Policy Optimization (PPO) played a huge role in early successes such as ChatGPT. But honestly, these early methods weren’t easy. You had to juggle multiple models, tweak countless hyperparameters, and sometimes even then, things would just break.
Things got simpler with methods like Group Relative Policy Optimization (GRPO), which reduced some complexity. But even then, RL remained tricky - designing reward functions and fine-tuning was more art than science. (We previously discussed how models can judge each other in our post,
"Model as a Judge"
).
Enter VibeRL: Simplifying Fine-Tuning
Recently, "Vibe Coding" - AI translating simple human instructions into working code - has changed the game for software developers. It made coding easier, faster, and more accessible.
We thought: why not bring this vibe to RL?
RL’s complexity actually makes it ideal for automation. So we built VibeRL - an AI agent designed to handle all the difficult parts of RL for you. Here’s how easy it is:
•
Give VibeRL your dataset.
•
Write a simple prompt describing your goal.
That’s it. From there, VibeRL analyzes your task, picks the best strategy, and runs the entire fine-tuning process on its own. We're still actively developing it, but early results have been pretty exciting.
What We've Learned So Far
We tested VibeRL with a variety of problems to see how it stacked up against traditional methods.
Case Study 1: Solving Grade School Math (GSM8K)
•
Base Model:
Qwen2.5-3B
•
Task:
Improve math reasoning with GSM8K data.
•
User prompt:
You are given a datase GSM8k about grade school math problem solving in
{dataset_path}
. You are tasked to improve the math problem solving ability of the base model on this dataset by performing funetuning on it. The final solution of the finetuned model should be concise, mathematically correct, and closely follow the desired format.
•
Result:
In just 40 epochs, accuracy jumped from 52% to 85%.
Case Study 2: Coding Challenges (LeetCode)
•
Base Model:
Qwen2.5-7B
•
Task:
Solve LeetCode programming problems without direct answers—just a pass/fail test environment.
•
User prompt:
You are given a datase consist of leetcode coding problems in
{dataset_path}
. You are tasked to improve the coding problem solving ability of the base model on this dataset by performing funetuning on it. The final solution of the finetuned model should be able to give the correct answer to the leetcode coding problems, which passes all of the test cases. The solution should also be concise and easy to understand
•
Result:
Accuracy improved from 34% to 63%. Interestingly, we noticed performance fluctuating slightly near the end, giving us insight into future improvements.
Case Study 3: Real-World Function Calling
We tackled a real client problem, improving the model’s ability to correctly call functions based on user inputs.
•
Base Model:
Qwen3-32B
•
Task:
Function calling accuracy from client dataset.
•
Result:
Using a two-step approach (SFT followed by RFT), accuracy rose dramatically from 50% to 87.3%.
•
Prompt:
<hidden to avoid revealing customer-specific details>
Baseline
SFT
RFT
Function calling accuracy
50.0%
85.8%
87.3%
Where We're Headed
These early tests confirm that AI agents like VibeRL can genuinely simplify RL workflows, making powerful model customization accessible even without deep expertise.
Next up, we’re turning VibeRL into a product. We're also exploring ways to make it smarter, like automatically choosing base models, tuning hyperparameters on-the-fly, and even drafting reward functions with minimal human effort.
Ultimately, we want everyone to easily harness their data and build models - less engineering, more intuition.
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
