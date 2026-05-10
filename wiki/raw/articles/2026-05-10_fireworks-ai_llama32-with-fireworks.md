---
title: "Partnering with Meta: Bringing Llama 3.2 to Fireworks for Fine-Tuning and Inference"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/llama32-with-fireworks"
scraped: "2026-05-10T01:27:11.191497+00:00"
lastmod: "2026-02-12T18:52:45.000Z"
type: "sitemap"
---

# Partnering with Meta: Bringing Llama 3.2 to Fireworks for Fine-Tuning and Inference

**Source**: [https://fireworks.ai/blog/llama32-with-fireworks](https://fireworks.ai/blog/llama32-with-fireworks)

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
Llama32 With Fireworks
Partnering with Meta: Bringing Llama 3.2 to Fireworks for Fine-Tuning and Inference
PUBLISHED
9/25/2024
Table of Contents
Key Highlights
Llama 3.2 Adds New Multimodal Capabilities, Expanding Use Cases For Developers
Pricing and Deployment Options: The Great News
Serverless
On-Demand
Enterprise Reserved
Customize Llama 3.2 With Fine-Tuning
Try the models out directly in our playground
Next, try using the models with our inference APIs
Install the Fireworks AI Python package
Accessing Llama 3.2 on Serverless Inference API
Table of Contents
Table of Contents
Key Highlights
Llama 3.2 Adds New Multimodal Capabilities, Expanding Use Cases For Developers
Pricing and Deployment Options: The Great News
Serverless
On-Demand
Enterprise Reserved
Customize Llama 3.2 With Fine-Tuning
Try the models out directly in our playground
Next, try using the models with our inference APIs
Install the Fireworks AI Python package
Accessing Llama 3.2 on Serverless Inference API
Table of Contents
We are excited to announce support for the newest additions to the
Llama collection
from Meta. With the addition of
Llama 3.2
, developers gain access to new tools that enable the creation of sophisticated multi-component AI systems that combine models, modalities, and external tools to deliver advanced real-world AI solutions.
Llama 3.2: Seeing The World More Clearly (And Quickly)
The release of
Llama 3.2 1B
,
Llama 3.2 3B
,
Llama 3.2 11B Vision
, and
Llama 3.2 90B Vision
models brings a range of text-only and multimodal models designed to enhance modular AI workflows. These models provide deep customization, allowing developers to tailor solutions and accelerate specific tasks in compound AI systems.
Get started today on Fireworks:
•
Llama 3.2 1B (text-only)
: Ideal for
retrieval and summarization
tasks such as
personal information management
,
multilingual knowledge retrieval
, and
rewriting tasks
.
•
Llama 3.2 3B (text-only)
: Optimized for
query and prompt rewriting
, it supports applications like
mobile AI-powered writing assistants
and
customer service tools
running on
edge devices
.
•
Llama 3.2 11B Vision
and
Llama 3.2 90B Vision
: These models extend capabilities with
image understanding
and
visual reasoning
for tasks such as
image captioning
,
visual question answering
, and
document visual analysis
.
The instruct variants of these models are available serverless (pay-per-token for models on Fireworks-configured GPUs). Both the instruct and non-instruct variants of these models are available
on-demand
(private GPU instances billed per GPU second). Meta’s Llama Guard 3 models for detecting violating content are also available on-demand.
Key Highlights
Text
Multimodal
Recommendation
Use Case
Llama 3.2 1B
✅
Ideal for retrieval and summarization tasks.
This model can be effectively deployed for personal information management, multilingual knowledge retrieval, and rewriting tasks running locally on edge devices, offering efficiency in handling data close to the user.
Llama 3.2 3B
✅
Recommended for query and prompt rewriting and optimized for mobile AI-powered writing assistants and edge devices.
This model is perfect for customer service applications and mobile AI-powered writing assistants, allowing businesses to deploy high-performance models that deliver real-time AI solutions at scale.
Llama 3.2 11B Vision
✅
✅
Optimized for image understanding and visual reasoning, it excels in image captioning, image-text retrieval, visual grounding, and document visual question answering.
This model is critical for any application needing advanced visual and text-based comprehension, such as enterprise search and expert copilots in areas like coding, math, and medicine.
Llama 3.2 90B Vision
✅
✅
Similar to the 11B model, this larger model offers exceptional performance in visual question answering, visual reasoning, and other complex multimodal tasks.
Its ability to handle both image and text inputs allows for a range of applications, from image captioning to document analysis, making it ideal for industries like healthcare, legal, and finance.
Llama 3.2 Adds New Multimodal Capabilities, Expanding Use Cases For Developers
The release of multimodal models unlocks exciting new production use cases for developers, from enterprise to everyday applications.
Examples of use cases for Llama 3 models on Fireworks includes:
•
Visual Question Answering and Reasoning
: In healthcare, clinicians can use multimodal systems to ask questions about medical images, like "Is there a fracture in this X-ray?" The system analyzes the image, provides a precise answer, and highlights key areas, enabling faster, more accurate diagnoses and reducing human error in time-sensitive situations.
•
Document Visual Question Answering
: For document-heavy fields like legal and finance, visual-language models can extract specific information from PDFs or charts, such as "What is the total amount due?" This reduces manual effort, speeds up analysis, and boosts accuracy in reviewing complex documents.
•
Image Captioning
: In retail, compound-AI systems can automatically generate product descriptions from images, such as "A sleek black leather handbag with gold hardware." The system analyzes the product image and creates a detailed, engaging caption that enhances customer experience and boosts metrics like conversion rates. By eliminating the need for manual captioning, this approach enables businesses to quickly scale as their product catalogs grow, while maintaining consistency and accuracy.
See how customers like AlliumAI are supporting multimodal models in production with Fireworks in this
blog post
.
Start Small Then Scale Quickly and Efficiently with Llama 3.2 Models on Fireworks
Llama models
, fine-tuned and deployed through Fireworks, offer developers the flexibility to build personalized AI systems tailored to specific needs.
With Fireworks handling the
fine-tuning and inference
, developers can leverage these powerful tools to accelerate innovation and bring their AI solutions to market faster. For example,
Fireworks
can serve
Llama 3.2 1B
in approximately
500 tokens/second
and
Llama 3.2 3B in 270 tokens/second.
Pricing and Deployment Options: The Great News
There’s no one-size-fits-all approach to developing compound AI systems, which is why Fireworks offers a number of different options for using and deploying models like
Llama-3.2
for production AI (including
serverless, on-demand, and enterprise reserved
).
We’re also happy to announce
new, competitive pricing
for text and multimodal models, especially for the Llama 3.2 - 11B and Llama 3.2 - 90B multimodal models which will be the
same price as the text-only models
. Images will be charged as text tokens. The exact number of tokens depends on image resolution and model. Images for the Llama 3.2 vision models are typically counted as 6400 text tokens.
Serverless
Fireworks serverless is the easiest way to get started. Serverless offers the new Llama models on pre-configured GPUs, no set-up required.
Base Model Parameter Bucket
Specific Model
$/1M tokens
0B - 4B
Llama 3.2 1B Instruct
$0.1
0B - 4B
Llama 3.2 3B Instruct
$0.1
4B - 18B
Llama 3.2 11B Vision Instruct
$0.2
16B+
Llama 3.2 90B Vision Instruct
$0.9
On-Demand
For heavier volume and fully configurable latency and reliability, Fireworks on-demand provides private GPUs to host Llama 3.2. Developers pay per second for on-demand with no commitments. The efficiency of Fireworks’ software stack enables significant price, throughput and latency improvements compared to running vLLM on private GPUs (see
pricing
and performance
tests
).
Enterprise Reserved
For high-volume applications, Fireworks offers private, enterprise GPU deployments options that are fully personalized and backed by SLAs and performance guarantees.
Contact us
for additional information.
Customize Llama 3.2 With Fine-Tuning
Meta is releasing the Llama 3.2 models under very open and permissive licensing that makes them ideal for fine-tuning and additional model customization.
Today you can fine-tune the
Llama 3.2 1B (text-only)
and
Llama 3.2 3B (text-only)
models on Fireworks, with fine-tuning for multimodal models like Llama 3.2 11B Vision and Llama 3.2 90B Vision coming soon.
For more information about fine-tuning, read our documentation
here
.
Getting Started with Llama 3.2
Try the models out directly in our playground
With our model playground, you can focus on developing a feel for a model’s behavior, adjusting prompt and parameter values, and then grabbing the code to test our inference APIs.
For example, how would you describe making pancakes from scratch to someone that’s learning to make breakfast for themselves, the very first time?
Is date night coming up and you need some ideas on the fly? Try out the Llama 3.2 3B chat API.
Writing a paper for an art history class about comedic paraodies of famous artworks but need help getting started?
**Llama 3.2 90B Vision
can help out.**
Next, try using the models with our inference APIs
To quickly get up and running using Llama 3.2 on the Fireworks AI visit
fireworks.ai
to sign up for an account. Pickup the API Key from Profile on top right -> API Keys.
Install the Fireworks AI Python package
pip install --upgrade fireworks-ai
Accessing Llama 3.2 on Serverless Inference API
Below code snippet instantiates Fireworks client and uses chat completions API to call the Llama 3.2 listed at -
accounts/fireworks/models/llama-v3p2-3b-instruct
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
14
from
fireworks
.
client
import
Fireworks
#replace the
FIREWORKS_API_KEY
with
the key copied
in
the above step
.
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
"accounts/fireworks/models/llama-v3p2-3b-instruct"
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
or other product that is released under a license that allows users to freely use
,
modify
,
and distribute the source code
,
design
,
or other components
.
The
term
"open-source"
was first coined
in
1998
by
Bruce
Perens
and
Eric
S
.
Raymond
to describe software that is released under these principles
.
The
main characteristics
of
open
-
source products are
:
1.
**
Free
to use
**
:
Open
-
source products are free to use
,
modify
,
and distribute
.
2.
**
Source
code available
**
:
The
source code
,
design
,
or other components are made available to the
public
,
allowing anyone to view
,
modify
,
and distribute them
.
3.
**
Modifiable
**
:
Users
have the freedom to modify the product to suit their needs
.
4.
**
Redistributable
**
:
Users
are allowed to redistribute the product
,
either
as
-
is or
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
source products are often developed and maintained by a community
of
volunteers and contributors
.
Get Started Today
Ready to start building with Llama 3.2? Here’s how to get started:
•
Run
inference:
Run the models with blazing fast speeds
serverless
or on-demand
•
Fine Tune Llama 3.2
: Follow our
step-by-step guide
on fine-tuning models.
•
Deploy Your Model
: Follow our
deployment guide
to quickly deploy your fine-tuned model.
•
Join Our Community
: Join our
Discord channel
to connect with other developers and the Fireworks team
Contact us
:
Reach out
to discuss how we can help you leverage Llama 3.2 and the Fireworks inference engine for your specific use case.
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
