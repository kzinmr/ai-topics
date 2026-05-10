---
title: "FireFunction V1 - Fireworks’ GPT-4-level function calling model - 4x faster than GPT-4 and open weights"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/firefunction-v1-gpt-4-level-function-calling"
scraped: "2026-05-10T01:27:21.754258+00:00"
lastmod: "2026-02-12T18:53:13.000Z"
type: "sitemap"
---

# FireFunction V1 - Fireworks’ GPT-4-level function calling model - 4x faster than GPT-4 and open weights

**Source**: [https://fireworks.ai/blog/firefunction-v1-gpt-4-level-function-calling](https://fireworks.ai/blog/firefunction-v1-gpt-4-level-function-calling)

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
Firefunction V1 Gpt 4 Level Function Calling
FireFunction V1 - Fireworks’ GPT-4-level function calling model - 4x faster than GPT-4 and open weights
PUBLISHED
2/20/2024
Introduction
Last December, Fireworks
launched
the alpha version of our first function calling model to empower developers to incorporate external knowledge in their LLM applications. Since then, the response from the community has been overwhelming, and we've been fueled by the invaluable insights gained from user experiences.
Today, we're thrilled to announce
FireFunction-v1
, our new & improved, open-weights model, based on Mixtral.
Try out the new model
here
!
We have packed in a significant amount of improvements over our last version of the function calling model -
fw-function-call-34b-v0
. Some highlights of the new model include
Highest quality for real-world use cases
- We’ve optimized performance for structured output generation & routing decision-making. Decision-making is made even better through a new option to configure “tool_choice” to
‘any’
to force a function call
.
Improved response accuracy
for multilingual inputs.
Based on one of the highest quality OSS models
- Mixtral 8x7B.
Available open-weights or hosted with blazing-fast speeds
on the Fireworks platform
Compared to GPT4, FireFunction provides similar accuracy on real-world use cases with significantly faster speeds and the flexibility of open-source. Based on internal evaluations, FireFunction achieves significant quality & speed improvements over other OSS-based function calling model providers. See tl;dr chart
FireFunction - v1
GPT-4
Mixtral-Instruct + JSON mode
Accuracy with fewer than 5 functions (Nexus OTX)
87.88%
87.88%
74.24%
Accuracy with >10 functions (Nexus VT)
84.43%
89.16%
75.41%
Guaranteed structure adherence for structured output
✅
✅
✅
Response latency
0.4 - 0.6 s
2.3 - 3.0 s
0.4 - 0.6 s
Forced function call ability (“any” tool_choice value)
✅
❌
❌
Open weights
✅
❌
✅
Price
Free during limited beta
$10/M input tokens$30/M output tokens
$0.4/M input tokens$1.6/1M output tokens
Recap: What is function calling?
Function calling is the ability of a model to output information to call external APIs. LLMs have immense utility on their own but cannot access real-time or internal data. Function calling bridges that gap by letting LLMs format text to call APIs and optionally incorporate the API response. This enables use cases like dynamic agents. For example, you could have a scheduling agent that can check the weather through API and change plans based on the result.
Use Cases
Structured Output
Our previous function calling model faced difficulty dealing with nested function specifications and dealing with complex output data types such as arrays, dictionaries etc. We have enhanced the ability of FireFunction to follow complicated JSON Spec now. The model is aided in this task by our recent launch of general
JSON mode support
. We bring the best of two worlds together (1) Using the function calling model to make the right decisions about data format to choose & what parameter values to populate and (2) Using JSON mode to force the model to always generate the correctly formatted JSON.
All of the improvements greatly improve the accuracy of making correct, well-formatted function calls. For example, let’s say you wanted the model to call a Stripe-like API that always requires the following properties:
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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
{
"name"
:
"createPayment"
,
"description"
:
"Create a new payment request"
,
"parameters"
:
{
"type"
:
"object"
,
"properties"
:
{
"transaction_amount"
:
{
"type"
:
"number"
,
"description"
:
"The amount to be paid"
}
,
"description"
:
{
"type"
:
"string"
,
"description"
:
"A brief description of the payment"
}
,
"payment_method_id"
:
{
"type"
:
"string"
,
"description"
:
"The payment method to be used"
}
,
"payer"
:
{
"type"
:
"object"
,
"description"
:
"Information about the payer, including their name, email, and identification number"
,
"properties"
:
{
"name"
:
{
"type"
:
"string"
,
"description"
:
"The payer's name"
}
,
"email"
:
{
"type"
:
"string"
,
"description"
:
"The payer's email address"
}
,
"identification"
:
{
"type"
:
"object"
,
"description"
:
"The payer's identification number"
,
"properties"
:
{
"type"
:
{
"type"
:
"string"
,
"description"
:
"The type of identification document (e.g. CPF, CNPJ)"
}
,
"number"
:
{
"type"
:
"string"
,
"description"
:
"The identification number"
}
}
,
"required"
:
[
"type"
,
"number"
]
}
}
,
"required"
:
[
"name"
,
"email"
,
"identification"
]
}
}
}
}
You could feed text into the FireFunction model, such as a user conversation, and the model would always adhere to the provided structure so that it’s more likely to make valid API calls.
Another potential use case of the structured response mode is in not calling APIs but in providing structured output. For example, let’s say you wanted to extract structured data from animal articles to easily add to a database. You could specify output for the firefunction model to be attributes from all articles like the “animal weight” and “animal habitat”. Then you can run articles through firefunction and ensure that info is always extracted in the specified format. See examples of both of these use cases in this example
notebook
!
Routing Decision-Making
One of the most important use cases for function that we’ve heard is in decision-making and routing. Inputs to LLMs apps are often dynamic and different inputs could spur different optimal reactions. For example, consider an application for a financial assistant that takes a user command to get more information. Depending on the user command, we may want to call a function to get stock price or a different function to get news. The model must be able to parse user input and choose between these couple functions. __See the model in action choosing between 4 different functions in our UI
demo
(screenshot below).
Our model is designed for exceptional accuracy across many functions. We present the result of our model on 2 benchmarks - evaluating the function calling ability of short context (choose between 5 functions), and long context (choose between 10 functions). For evaluation, we use a dataset released by the Nexus
team
. We’d also like to thank the Nexus team for creating a high-quality dataset!
In the evaluations, we use function calling mode for all the available models, except the prompt-engineered Mixtral Instruct model. For the prompt-engineered Mixtral Instruct model, we use JSON mode to keep the comparison fair. For comparison with GPT-4, we use
gpt-4-0125-preview
. We don’t train on any of the evaluation datasets.
The short-function context accuracy eval was run on Nexus OTX dataset, which contains 5 input functions.
Figure 1: The chart displays the accuracy of firefunction-v1 compared to other models. Higher is better. Going from v0 to v1, we observe around 4% jump in accuracy and on-par accuracy with GPT-4.
For long-function context accuracy, we use the Nexus VT dataset which contains 10 input functions.
Figure 2: The chart displays the accuracy of firefunction-v1 compared to other models. Higher is better. Most notably the firefunction-v1 closes the gap to latest GPT-4 turbo from 14% to under 5%.
“Any” parameter -
In many decision-making use cases, we always want the model to make a function call and may never want the model to respond with just its internal knowledge. For example, if you’re routing between multiple models specialized at different tasks (multilingual input, math, etc), you may use the function-calling model to always send requests to one of the models and never respond independently.
Current function calling models don’t enable users to “force function calls”. For example, OpenAI provides two options for “tool_choice” (1) “Auto” - which risks having the model respond without an API call and (2) “Function_name”- which makes the model always choose the specified function.
Firefunction v1 supports a new parameter value of “any” to always force the model to make a function call. The model can choose between any of the provided functions, but must always call a function.
Blazing fast speed without quality sacrifices
Especially for use cases like decision-making and model routing, we know that speed matters greatly. Users don’t want to wait for output as a model routes queries and calls APIs. Compared to GPT4, our model especially performs well in speed, despite maintaining a comparable quality to GPT-4. Our Mixtral-based model is served at the industry-leading inference speeds as other featured Fireworks models. Users can expect 4X speedups compared to GPT-4 Turbo.
_Figure 3: The chart highlights latency distribution given output token length distribution. We divide responses into 2 categories -
< 50 and > 50. In both scenarios, we observe around 4X faster response times compared to GPT-4._
Using the Function Calling Models
The FireFunction models checkpoints are available on
Hugging Face
. We host FireFunction on Fireworks platform in a speed-optimized setup with OpenAI-compatible API. So you should be able to
easily swap in our model
with a 1-line code change if you were previously using OpenAI. The models are
free to use
while they’re in our limited beta period! Get started with our function calling documentation
here
.
We’d love to hear what you think and what you’re trying to build! We’re actively trying to tailor the next iteration of function calling for developer use cases. Please join the function calling channel on our
Discord
community or sign up with this
form
to be a function calling Feedback partner to directly influence upcoming product development and receive Fireworks credit. We can’t wait to see what you build!
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
