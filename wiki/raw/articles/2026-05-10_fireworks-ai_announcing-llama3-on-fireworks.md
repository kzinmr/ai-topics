---
title: "Partnering with Meta to bring Llama 3 to Firework’s inference and fine-tuning"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/announcing-llama3-on-fireworks"
scraped: "2026-05-10T01:27:20.141403+00:00"
lastmod: "2026-02-12T18:53:06.000Z"
type: "sitemap"
---

# Partnering with Meta to bring Llama 3 to Firework’s inference and fine-tuning

**Source**: [https://fireworks.ai/blog/announcing-llama3-on-fireworks](https://fireworks.ai/blog/announcing-llama3-on-fireworks)

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
Announcing Llama3 On Fireworks
Partnering with Meta to bring Llama 3 to Firework’s inference and fine-tuning
PUBLISHED
4/18/2024
Table of Contents
Key takeaways from the Llama 3 Model announcement:
Bringing the best of Open-source AI to Enterprises
Build with Llama 3 on Fireworks AI
Install the Fireworks AI Python package
Accessing Llama 3 on Serverless Inference API
Table of Contents
Table of Contents
Key takeaways from the Llama 3 Model announcement:
Bringing the best of Open-source AI to Enterprises
Build with Llama 3 on Fireworks AI
Install the Fireworks AI Python package
Accessing Llama 3 on Serverless Inference API
Table of Contents
We are pleased to announce the availability of the open-source Llama 3 8B and 70B models with 8k context, served from our blazing fast inference stack. Llama 3 is pretrained on over 15 trillion tokens and with a vocabulary of 128K tokens that encodes language much more efficiently.
List of Llama 3 Series of Models:
•
Llama 3 8B Instruct
•
Llama 3 70B Instruct
•
Llama Guard 2 8B
•
Llama 3 8B
•
Llama 3 70B
Apart from adding the base models, over the next few days, we will be adding support for fine-tuning Llama 3 models, serving of LoRA adapters and increasing inference speeds further. Our serveless inference stack allows to serve 100s of LoRA adapters with NO additional cost.
Key takeaways from the Llama 3 Model announcement:
State-of-the-art performance
: The new 8B and 70B parameter Llama 3 models establish a new state-of-the-art for open-source language model benchmarks. Improvements in pretraining, instruction fine-tuning, and architecture have led to superior performance on industry benchmarks and real-world use cases compared to competing models.
Open and responsible development
: Meta is taking an open approach by releasing Llama 3 models early to enable community innovation. This is combined with a strong focus on responsible development and deployment, providing new safety tools, an updated
Responsible Use Guide
, and a system-level approach to mitigating potential harms.
Extensible platform with more to come: The 8B and 70B models are just the beginning. In the coming months, Meta plans to release larger models with up to 400B parameters with new capabilities like multimodality, multilingual conversation, and longer context.
Bringing the best of Open-source AI to Enterprises
Our goal at Fireworks is to make Open-source AI accessible to developers and businesses by providing the best language and image models at lightning-fast speeds with the utmost reliability.
Our industry-leading inference speed and quality for image and text generation are utilized by companies like Quora, Sourcegraph, Upstage, Tome, and Anysphere for their production use cases.
Build with Llama 3 on Fireworks AI
To quickly get up and running using Llama 3 on the Fireworks AI visit
fireworks.ai
to sign up for an account. Pickup the API Key from Profile on top right -> API Keys.
Install the Fireworks AI Python package
1
2
pip install
-
-
upgrade fireworks
-
ai
Accessing Llama 3 on Serverless Inference API
Below code snippet instantiates
Fireworks
client and uses chat completions API to call the Llama 3 listed at -
accounts/fireworks/models/llama-v3-70b-instruct
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
"accounts/fireworks/models/llama-v3-70b-instruct"
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
Open-source refers to a software
,
hardware
,
or other product that is released under a license that allows users to freely use
,
modify
,
and distribute the source code
,
design
,
or other components. The term
"open-source"
was first coined in
1998
by Bruce Perens and Eric S. Raymond to describe software that is released under these principles.
The main characteristics of open-source products are
:
1
. **Free to use**
:
Open-source products are free to use
,
modify
,
and distribute.
2
. **Source code available**
:
The source code
,
design
,
or other components are made available to the public
,
allowing anyone to view
,
modify
,
and distribute them.
3
. **Modifiable**
:
Users have the freedom to modify the product to suit their needs.
4
. **Redistributable**
:
Users are allowed to redistribute the product
,
either as-is or with modifications.
5
. **Community-driven**
:
Open-source products are often developed and maintained by a community of volunteers and contributors.
For enterprises who need even faster speeds or throughput, you can serve Llama 3 on your own
dedicated GPU infrastructure
or personalized enterprise configurations. If you have any questions or would like to learn more, please don't hesitate to
contact us
.
Happy building!
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
