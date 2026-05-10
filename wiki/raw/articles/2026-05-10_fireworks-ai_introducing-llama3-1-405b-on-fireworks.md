---
title: "Introducing Llama 3.1 inference endpoints in partnership with Meta"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/introducing-llama3-1-405b-on-fireworks"
scraped: "2026-05-10T01:27:36.780880+00:00"
lastmod: "2026-02-12T18:52:54.000Z"
type: "sitemap"
---

# Introducing Llama 3.1 inference endpoints in partnership with Meta

**Source**: [https://fireworks.ai/blog/introducing-llama3-1-405b-on-fireworks](https://fireworks.ai/blog/introducing-llama3-1-405b-on-fireworks)

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
Introducing Llama3 1 405b On Fireworks
Introducing Llama 3.1 inference endpoints in partnership with Meta
PUBLISHED
7/23/2024
Table of Contents
Key Highlights about Llama 3.1
Getting Started with Llama 3.1 405B
Install the Fireworks AI Python package
Accessing Llama 3.1 on Serverless Inference API
Commitment to Open and Responsible AI Development
Building Compound AI Systems with Llama 3.1
Table of Contents
Table of Contents
Key Highlights about Llama 3.1
Getting Started with Llama 3.1 405B
Install the Fireworks AI Python package
Accessing Llama 3.1 on Serverless Inference API
Commitment to Open and Responsible AI Development
Building Compound AI Systems with Llama 3.1
Table of Contents
We’re thrilled to introduce Llama 3.1 inference endpoints in partnership with Meta. With expanded context length, multilingual support, tool calling, and the inclusion of Llama 3.1 405B, Llama 3.1 represents a significant leap forward in AI capabilities. Fireworks is proud to be a launch partner, offering AI developers immediate access to Llama 3.1 for production use from day one. Llama 3.1 is available on Fireworks AI inference engine and optimized for performance, which means you benefit from the lowest latency and most-efficient deployment.
List of Llama 3.1 models available on Fireworks
•
Llama 3.1 8B Instruct
•
Llama 3.1 70B Instruct
•
Llama 3.1 405B Instruct
Our mission is to provide the fastest and most efficient inference platform and tools for building compound AI systems, equipping developers with the essential building blocks to create custom, production-ready AI applications. Fireworks is at the forefront of the rapid shift towards compound AI systems, which integrate multiple models and tools to enhance performance, reliability, and control. With the addition of Llama 3.1 to our portfolio of over 100 state-of-the-art models, and its new tool-calling capabilities, we are advancing this mission even further.
This week, we are also introducing
AMD Instinct MI300 accelerators
alongside
NVIDIA H100
to power serverless inference for Llama 3.1 405B Instruct.
Key Highlights about Llama 3.1
•
Unmatched Flexibility and Control
: Llama 3.1 405B is the largest openly available foundation model, offering state-of-the-art capabilities that rival the best closed-source models.
•
Expanded Context and Multilingual Support
: The new models support context lengths up to 128K and span 8 languages, enabling richer and more nuanced interactions.
•
Enabling New Capabilities
: With Llama 3.1, the community can unlock new possibilities in synthetic data generation and model distillation.
•
Commitment to Open AI
: Fireworks AI continues to champion openness in AI, fostering innovation and safety in the ecosystem.
•
Tools for Developers
: Llama 3.1 provides robust tools for creating custom agents and new agentic behaviors, bolstered by new security and safety measures.
Getting Started with Llama 3.1 405B
To quickly get up and running using Llama 3.1 on the Fireworks AI visit
fireworks.ai
to sign up for an account. Pickup the API Key from Profile on top right -> API Keys.
Install the Fireworks AI Python package
pip install *--*upgrade fireworks-ai
Accessing Llama 3.1 on Serverless Inference API
Below code snippet instantiates
Fireworks
client and uses chat completions API to call the Llama 3.1 listed at -
accounts/fireworks/models/llama-v3p1-405b-instruct
.
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
from
fireworks
.
client
import
Fireworks
#replace the FIREWORKS_API_KEY with the key copied in the above step.
client
=
Fireworks
(
api_key
=
"<FIREWORKS_API_KEY>"
)
response
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
"accounts/fireworks/models/llama-v3p1-405b-instruct"
,
messages
=
[
{
"role"
:
"user"
,
"content"
:
"what is open-source?"
,
}
]
,
)
print
(
response
.
choices
[
0
]
.
message
.
content
)
The above API request results in the below response.
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
Open
-
source refers to a software
,
hardware
,
or
other product that
is
released under a license that allows users to freely use
,
modify
,
and
distribute the source code
,
design
,
or
other components
.
The term
"open-source"
was first coined
in
1998
by Bruce Perens
and
Eric S
.
Raymond to describe software that
is
released under these principles
.
The main characteristics of
open
-
source products are
:
1.
**
Free to use
**
:
Open
-
source products are free to use
,
modify
,
and
distribute
.
2.
**
Source code available
**
:
The source code
,
design
,
or
other components are made available to the public
,
allowing anyone to view
,
modify
,
and
distribute them
.
3.
**
Modifiable
**
:
Users have the freedom to modify the product to suit their needs
.
4.
**
Redistributable
**
:
Users are allowed to redistribute the product
,
either
as
-
is
or
with
modifications
.
5.
**
Community
-
driven
**
:
Open
-
source products are often developed
and
maintained by a community of volunteers
and
contributors
.
Commitment to Open and Responsible AI Development
At Fireworks AI, we believe that openness leads to better, safer products, faster innovation, and a healthier market. We are dedicated to the responsible release of models with our partners and continuously work with them on developing tools to ensure safety and security in AI applications.
Building Compound AI Systems with Llama 3.1
We’re excited to see how the community leverages Fireworks to create groundbreaking applications with Llama 3.1. For inference pricing and deployment options, visit
fireworks.ai/pricing
.
For more information and to get started with Llama 3.1, visit
fireworks.ai
.
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
