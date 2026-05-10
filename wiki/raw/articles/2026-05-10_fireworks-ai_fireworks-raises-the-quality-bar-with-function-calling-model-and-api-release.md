---
title: "Fireworks Raises the Quality Bar with Function Calling Model and API Release"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/fireworks-raises-the-quality-bar-with-function-calling-model-and-api-release"
scraped: "2026-05-10T01:27:07.536495+00:00"
lastmod: "2026-02-12T18:53:19.000Z"
type: "sitemap"
---

# Fireworks Raises the Quality Bar with Function Calling Model and API Release

**Source**: [https://fireworks.ai/blog/fireworks-raises-the-quality-bar-with-function-calling-model-and-api-release](https://fireworks.ai/blog/fireworks-raises-the-quality-bar-with-function-calling-model-and-api-release)

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
Fireworks Raises The Quality Bar With Function Calling Model And Api Release
Fireworks Raises the Quality Bar with Function Calling Model and API Release
PUBLISHED
12/20/2023
Table of Contents
Function calling through a fine-tuned model vs prompt engineering
Using the API
Future Work
Conclusion
Table of Contents
Table of Contents
Function calling through a fine-tuned model vs prompt engineering
Using the API
Future Work
Conclusion
Table of Contents
Since rolling out the Fireworks AI platform earlier, we've been delighted to be part of the development journey of thousands of developers. At Fireworks, our vision has been to provide developers with a fast AI platform with the highest-quality models. We've heard a common user request for function calling, so we're thrilled to announce the Alpha launch of the Fireworks function calling model and API, reaching GPT-4 quality.
What is function calling and why is it important?
Function calling is the ability for a model to call external APIs. While LLMs are very useful on their own, they struggle in situations such as:
Access to real-time data:
LLMs sometimes hallucinate and cannot answer questions that require real-time information. For example, it's difficult for LLMs to answer questions like “What's the current temperature in New York?”.
Dynamic Agents:
Many of our users create LLM-based agents to take action. These agents sometimes require external information to adapt and decide. For example, a scheduling agent may need to know whether it's raining to cancel an appointment.
Function calling enables LLMs to incorporate knowledge from these API calls to address these issues. For example, an LLM with function calling capabilities could call upon a weather information API to get real-time information or provide an agent with the information to act.
Function calling challenges
While calling a single weather API could be straightforward for an LLM, the function calling problem space quickly becomes multi-faceted with more complex queries. For example, let's take the example of creating an agent to help with web shopping.
•
Agent description:
Conversational agent that a business deploys to help users make purchases
•
Functions to use:
Entire Stripe SDK
•
Example queries:
(1) Fetching the price of a product (2) Buying a product based on customer intent .
The agent will have to grapple with issues, such as:
Intent detection
— Does the model know when it's necessary to call an API vs relying on its own knowledge?
Function quantity —
How does the model perform when many functions are provided? In this example, the agent is provided with the Stripe SDK, which has numerous functions. The agent will need to know when and how to call each individual function.
Value Formatting
— Can the model correctly structure information, especially for complex data types? In this example, many potential queries utilize more nested structures like the
recurring field
in the create_price stripe API. This field has a dictionary type where child fields can take on only specific enum values.
Contextual Information —
Can the model utilize conversational context and knowledge, especially in multi-turn or chat contexts? For example, if a user asks: “What's the stock price of the shirt?” and follows up with a question like “How does that compare to the jacket?”, can the model use contextual info to format corresponding API calls?
Our API is based on a fine-tuned CodeLlama-34B model that we've trained specifically to call functions and converse reliably. This means that our function calling model should have capabilities like a typical CodeLlama-34B-Instruct model (able to remember context) but it can also call functions to access external knowledge and chat with users.
Function calling through a fine-tuned model vs prompt engineering
We've fine-tuned a model for function calling, but a popular alternative approach is to engineer a function-calling prompt for a non-specialized model. We predominantly validated that this technique lacks in the following ways:
Accuracy
— Given aforementioned complexities, it can be difficult for non-fine-tuned LLMs to reliably parse context to understand intent and structure function call arguments.
Generalization Ability
— To be used in production, a function calling LLM must be able to generate calls for APIs that were not seen during training is crucial to its usefulness in production. Fine-tuning allows us to teach the model to generalize over a wide variety of arguments and functions. The resulting model does well on complex APIs such as Google Place APIs, to Stripe APIs or Plaid APIs even though such APIs don't appear in fine-tuning training data.
Tool Chaining
— Some use cases for function calling require the model to gather context from both conversation & previous function call outputs to perform function calls. This interaction can become fairly complex as the length of the conversation increases. Dealing with various ways function calling intent & normal conversation can intertwine with each other is a challenging ask for prompt engineered models.
Intent Detection
— It's crucial to find a balance between a trigger-happy agent & reluctant agent. Both ends of the spectrum result in a bad user experience. It's tricky to construct a prompt to convey a balanced message to the agent about function calling.
Quality Evaluation
To assess these claims and test the accuracy and generalizability of function-calling models, we designed two evaluation datasets. Neither of these datasets was included in model training.
Single Turn Dataset
— This dataset focuses on single-turn requests, where the LLM response is supposed to be a function call. We assess for accuracy of the function call — right function selection, right argument population & correct output structure. Additionally, the number of functions available is > 10. This dataset is derived from
VirusTotalBenchmark
.
Multi Turn Dataset
— This dataset tests scenarios where context for function call is spread across multiple turns — for example a conversation with multiple user statements. Our evaluation is judged on accuracy of the final function call, using the same criterion as described above. This dataset is derived from
Glaive2
.
We compare our model against some strong baselines. As GPT-3.5 is not strong in function calling generation, we compare with GPT-4. The instruct models, which don't have native tools support, are given a one-shot prompt like
this
to help with output formatting & function calling intent detection.
It's clear that our model comes very close to GPT-4's performance when it comes to function-calling
.
Table 1: Table with accuracy breakdown across 2 datasets. For the Single Turn dataset, the number of functions available is higher > 10. Whereas for multi turn the number of functions available is lower > 5.
In particular, our model performs notably better for multi-turn use cases where the context is spread across multiple turns. Another interesting aspect we see is that when the number of available functions is higher (as in the single-turn dataset), models don't do as well when they have a narrower function corpus available. One interesting thing to note here is that doing better on the function calling dataset has no bearing on general conversational ability of the model. We expect GPT-4 to be far superior in that area as compared to fine tuned CodeLlama.
If we break down mismatches (see Figure 1), we can see that prompt-engineered models frequently fail to make a function call entirely. This suggests that non-fine-tuned models find it difficult to stick to the function call format/intent detection when the conversation takes multiple turns.
Figure 1: Mismatch breakdown for the competitor models on the multi turn dataset.
A similar story emerges when we look at the mismatch breakdown on the single-turn dataset (Figure 2). The prompt-engineered models often “miss function arguments” and cannot use the prescribed function call format.
Figure 2: Mismatch breakdown for the competitor models on the single turn dataset.
Intent Evaluation
Evaluating function calling performance is more nuanced than just assessing whether a function call was made vs not. Another dimension where we evaluated performance was intent classification. To illustrate this, let's consider the following scenario
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
{
"FUNCTIONS"
:
[
{
"name"
:
"get_movie_details"
,
"description"
:
"Get details of a movie"
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
"movie_title"
:
{
"type"
:
"string"
,
"description"
:
"The title of the movie"
}
,
"year"
:
{
"type"
:
"integer"
,
"description"
:
"The release year of the movie"
}
}
,
"required"
:
[
"movie_title"
]
}
}
]
}
USER: "Can you please book a ticket for me for the movie 'Inception'?"
Here are two valid agent responses:
AGENT_2 is simply AGENT_1 with an extra function call appended. In this scenario, technically, both AGENT_1 & AGENT_2 are correct. Preference between the two responses depends subjectively on how trigger-happy you'd like to be.
We, therefore, evaluated responses for intent detection as a preference question using the following
prompt
. This validation framework allows us to deal with the inherent subjectiveness in the decision. We evaluated our model against GPT-4 while also using GPT-4 as a preference model. In this validation framework, the preference model rated responses from two competitors from 0–10 and indicated a preference (see table below). We discard ties for calculating win rate.
Table 2: Mean score records an average of preference score granted by GPT-4 on a scale of 0–10. In order to increase the veracity of the scores, we ask GPT-4 also to produce reasoning for giving the score. Along with the mean score, we present the winning % to highlight the distribution of cases of how each model wins.
Based on the evaluation, our model is doing a better job at intent detection. When taking a deeper look at the cases where the fireworks model is doing better — we see a pattern of GPT-4 being more trigger-happy with issuing a function call, whereas the Fireworks model tends to rely more on asking users for clarification where the intent is unclear.
Evaluation Data
For transparency we are open sourcing the datasets used for evaluation. We are always looking for ways to improve our evaluation methodologies, so please provide input on ways we can improve our evaluation dataset, metrics, etc.
Quality Evaluation Dataset —
https://huggingface.co/datasets/fireworks-ai/function-calling-eval-dataset-v0
Intent Evaluation Dataset —
https://huggingface.co/datasets/fireworks-ai/function-calling-intent-eval-v1
Using the API
Developers can easily integrate the
function calling API
into their applications to unlock new capabilities,
Get started for free
. Our function calling functionality is OpenAI API compatible. You can switch out base_url & api_key values to plug & play. Here is an example usage of a function calling API to help users fetch the price of a given item on an e-commerce website.
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
53
import
openai
client
=
openai
.
OpenAI
(
base_url
=
"https://api.fireworks.ai/inference/v1"
,
api_key
=
"<YOUR_SECRET_KEY>"
)
messages
=
[
{
"role"
:
"system"
,
"content"
:
"You are a helpful assistant with access to functions. Use them if required."
}
,
{
"role"
:
"user"
,
"content"
:
"Can you fetch me the price of Nike Air Jordan from 2012?"
}
]
tools
=
[
{
"type"
:
"function"
,
"function"
:
{
"name"
:
"get_object_price"
,
"description"
:
"Get the price of a given item."
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
"item_description"
:
{
"type"
:
"string"
,
"description"
:
"Description of item for which we want to fetch the price"
,
}
,
"model_year"
:
{
"type"
:
"integer"
,
"description"
:
"A specific year of the construction of item."
}
,
}
,
"required"
:
[
"item_description"
]
,
}
,
}
,
}
]
chat_completion
=
client
.
chat
.
completions
.
create
(
model
=
"accounts/fireworks/models/fw-function-call-34b-v0"
,
messages
=
messages
,
tools
=
tools
,
tool_choice
=
"auto"
,
temperature
=
0.1
)
print
(
repr
(
chat_completion
.
choices
[
0
]
.
message
.
model_dump
(
)
)
)
>
{
'content'
:
''
,
'role'
:
'assistant'
,
'function_call'
:
None
,
'tool_calls'
:
[
{
'id'
:
'call_....'
,
'function'
:
{
'arguments'
:
'{"item_description": "Nike Air Jordan", "model_year": 2012}'
,
'name'
:
'get_object_price'
}
,
'type'
:
'function'
,
'index'
:
0
}
]
}
Future Work
We are constantly working on improving the function calling API. The release of new and powerful OSS models like
Yi
,
Mixtral 8x7B
etc. offers exciting opportunities for improving function calling ability. We are working on upgrading the base model from the current CodeLlama-34B to another top performing OSS model, and improving performance with many available functions and longer conversation context. We would love to see community contributions to our evaluation data and hear your feedback about what is and isn't working well. We hope to release these improvements to the general public in the new year.
Conclusion
We're excited to empower developers to build more grounded and powerful applications through function calling. Get started today with our
Function Calling Guide
. Your feedback is invaluable to us — we'd love to hear what you think! Please join our Function Calling
Discord
community or apply (< 2 min
form
) to be part of our feedback partners program. Feedback partners will receive free Fireworks credit in exchange for helping to provide feedback and ideas about our API.
Thanks for your continued support, and we can't wait to see what you build!
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
