---
title: "Using On-Demand GPUs to Build and Deploy ML Models with Hex and Modelbit | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/modelbit-and-hex/"
scraped: "2026-05-10T01:27:13.020364+00:00"
lastmod: "2023-10-31"
type: "sitemap"
---

# Using On-Demand GPUs to Build and Deploy ML Models with Hex and Modelbit | Hex 

**Source**: [https://hex.tech/blog/modelbit-and-hex/](https://hex.tech/blog/modelbit-and-hex/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
Platform
chevron-down
Products
Agentic notebooks
Powerful, deep-dive analysis without the silos
Conversational self-serve
The best BI tool isn't just a BI tool
semantic-models
Context Studio
Build trust in data with semantic models and AI governance
cli
Hex CLI
Control your analytics from the terminal
Capabilities
Exploratory analysis
Go from quick question to deep analysis to data app in one place
Embedded analytics
Ship secure, customer-facing data experiences
app-builder
Data apps
Build and share interactive dashboards and reporting
Integrations
Out-of-the-box connections and flexible APIs
magic
AI & agents
Agentic workflows to empower your entire team
Solutions
chevron-down
lightbulb
Explore all solutions
One connected system - infinite data answers
By team
solutions-data-leader
Data leader
Focus your team and scale answers
solutions-product
Product
Build your product with data, not gut feels
solutions-marketing
Marketing
Turn scattered data into clear growth opportunities
solutions-sales
Sales
Clear pipeline. Confident forecasts
solutions-customer-success
Customer success
Create a complete view of customer health
Enterprise
Resources
chevron-down
Get started
integrations
Switching to Hex
A guide to getting started on agentic analytics
Templates
Jumpstart with pre-built projects
Hex Foundations
Video series
help
Docs
Resources and product guides
Changelog
Product updates
Inspiration
Blog
From data teams to data teams
Guides
Learn how to do more with data, together
Events
Learn and connect with peers
Customer stories
Empowering the best data teams
Partners
Learn more about our partnerships
save
Download
The Data Leader's Guide to AI Analytics
A practical roadmap for understanding and implementing AI to accelerate your data team and enable true self-service.
Pricing
Log In
Get started
Blog
Using On-Demand GPUs to Build and Deploy ML Models with Hex and Modelbit
On-demand GPUs, model training, and deployment.
Michael Butler
Data
October 31, 2023
Share:
twitter
linkedin
In this article
Modern ML On Modern Platforms
Setup
Building The Model
Deploying The Model
Get started for free
Modern ML On Modern Platforms
Hex is often a platform of choice for building ML models. The collaborative nature of the product means that teams can work together on their models. And the visual and exploration-based features of the Python+SQL notebook make it easy to experiment with models and model technologies.
Many modern model technologies require GPUs for training and inference. By using Modelbit alongside Hex, we can leverage Modelbit’s scalable compute with on-demand GPUs to do the model training. We can orchestrate the model training and deployment in our Hex project. And finally, we can deploy the model to a production container behind a REST API using Modelbit.
To illustrate with a simple example, let’s use a Grounding DINO model. Grounding DINO is a new computer vision model from the folks at IDEA Research. It takes an image and a text description of what to look for, and can find every instance of the named object in the image:
Setup
To get started building this model in Hex, we’ll begin by installing and importing Grounding DINO’s Python package:
Here we’ll see some warnings related to the local compute environment. That’s okay! We’re going to farm out the actual compute for building and getting inferences from the model to separate compute resources, while still orchestrating from our Hex project.
Next we’ll want to pull down the GroundingDINO configuration and checkpoint. These will be necessary for building the model itself.
As our last setup step, let’s go ahead and import the methods we’ll be using from GroundingDINO:
As before, we can ignore the GPU-related errors as we won’t be using local compute to build or call this model!
Building The Model
GroundingDINO is pretty simple to get started with! The core line of code here is
Copy
model = load_model('GroundingDINO_SwinT_OGC.py', 'groundingdino_swint_ogc.pth')
But of course, we want to build that model on a machine with a GPU! So what we’ll do is we’ll wrap that line of code in a function. We’ll have that function return the model so that we can use it when the call completes.
Then, to execute it, we’ll call `mb.add_job` from Modelbit. That will ship the function as well as all of its Python and system dependencies to a remote container in Modelbit for execution.
We’ll go ahead and choose `gpu_small` here for a reasonably-sized box with a T4 GPU attached. We can always up the resources if we need to. You can read about Modelbit’s
available box sizes here
.
After we run the cell, we get a button linking us to Modelbit!
When you click the button, you’ll be brought to this view showing your training job in Modelbit.
We can see the job is ready to run! The “Runner size” dropdown lets us change our mind about what resources we’d like to give the job. By clicking “Run Now,” we can go ahead and kick it off.
On this sized box, the model takes about 4 minutes to run! We can see its output here:
Finally, back in our notebook, let’s pull the loaded model back down so we can work with it in code! The Modelbit API call “mb.get_job_output” will do the trick:
Deploying The Model
Finally, we’ll want to deploy the model so we can use it for inference! To do that, let’s write a function that gets an inference:
As before, we’re not going to
call
the function locally, because we want to use on-demand GPU-enabled compute for inference!
To get an inference endpoint, let’s call Modelbit’s deploy() function. We’ll pass in the name of our inference function, and make sure to specify that we want a GPU:
This will give us a REST API to the model, as well as a Snowflake API!
For our purposes, we’ll want to use the REST API. We can integrate this REST API into our product, or anywhere else we might want to get inferences.
For now, let’s go ahead and call that REST API right from our Hex notebook:
As you can see, the image masks containing object identification came right back from the REST API. The object identification happened on Modelbit compute with GPU-enabled inference. The resulting data structure came right back to the Hex project, where we can keep working on it.
To tie it all together, let’s see whether we found those cows. Here’s some quick output via Matplotlib:
Boom! Model built and run remotely using on-demand GPU compute. Cows identified, locally in the Hex project. Let us know all the cool uses you find for on-demand GPU compute within Hex!
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
🔊
🎧
on
🌎
.
Company
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
