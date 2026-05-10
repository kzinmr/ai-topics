---
title: "Simplifying Code Infilling with Code Llama and Fireworks.ai"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/simplifying-code-infilling-with-code-llama-and-fireworks-ai"
scraped: "2026-05-10T01:20:40.362568+00:00"
lastmod: "2026-02-12T18:53:28.000Z"
type: "sitemap"
---

# Simplifying Code Infilling with Code Llama and Fireworks.ai

**Source**: [https://fireworks.ai/blog/simplifying-code-infilling-with-code-llama-and-fireworks-ai](https://fireworks.ai/blog/simplifying-code-infilling-with-code-llama-and-fireworks-ai)

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
Simplifying Code Infilling With Code Llama And Fireworks Ai
Simplifying Code Infilling with Code Llama and Fireworks.ai
PUBLISHED
9/12/2023
Llama 2 and Code Llama
Llama 2
is one of the latest open-source foundation large language models (LLMs) from Meta AI.
Code Llama
is a new family of code LLMs based on Llama 2 and specifically trained for code generation tasks. Code Llama achieves state-of-the-art performance on several code benchmarks when compared to other open models.
These code models support large input context, infilling capabilities, and instruction following for several programming tasks.
Code Llama Infilling
Code infilling is the task of predicting missing code that is consistent with the preceding and subsequent code blocks.
The 7B and 13B variants of Code Llama and Code Llama Instruction support infilling, which is important for practitioners as it enables the use of LLMs for features such as type inferencing or docstring generation.
But Code Llama infilling is tricky to use out of the box.
First, you must format your prompt properly and use proper whitespacing, especially for whitespace-meaningful languages such as Python. For instance, the model expects this format:
<PRE> {pre} <SUF>{suf} <MID>
. But you won't get infilling if the last space isn't added such as in
<PRE> {pre} <SUF>{suf}<MID>
. This user experience can be improved by having a standard interface that prevents these issues.
Second, we've noticed Code Llama base models are better than instruction models for the infilling task. Although instruction models are capable of infilling, it's hard to have precise control over it.
Infilling with the Fireworks API
To improve the experience and make it easier to use code infilling, we now support Code Llama infilling with the
Fireworks API
!
For Code LLama base models (currently
llama-v2-7b-code
and
llama-v2-13b-code
on Fireworks AI Platform), we've set up a default chat completion template capable of infilling.
We have simplified how to easily use Code Llama infilling with a convenient and familiar API. You simply pass a prefix and suffix, which represents the surrounding context, and ask the API to return the missing parts. It's that simple!
In the example below we are prompting the model to generate the remaining code between the given comment (prefix) and the returned value (suffix):
The code returned by the model properly completes the function to add two numbers:
Here is another more advanced example:
The actual code returned by the model is as follows:
Check out our API to start using Code Llama infilling and other models like Llama 2 to build your products:
http://fireworks.ai/api
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
