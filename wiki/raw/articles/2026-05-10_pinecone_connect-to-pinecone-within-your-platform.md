---
title: "Connect to Pinecone within your platform to enable a seamless AI development experience"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/connect-to-pinecone-within-your-platform/"
scraped: "2026-05-10T01:27:20.418377+00:00"
lastmod: "2024-07-24T13:30:05Z"
type: "sitemap"
---

# Connect to Pinecone within your platform to enable a seamless AI development experience

**Source**: [https://www.pinecone.io/blog/connect-to-pinecone-within-your-platform/](https://www.pinecone.io/blog/connect-to-pinecone-within-your-platform/)

←
Blog
Connect to Pinecone within your platform to enable a seamless AI development experience
Xian Huang
,
Adam Heerwagen
Jul 24, 2024
Product
Share:
Jump to section:
Simplify AI workflows with a frictionless experience
Industry leaders use Pinecone Connect to help users ship more accurate AI applications faster
Hassle-free integration with Pinecone
Get started now
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Today, we’re announcing the general availability of
Pinecone Connect
. Pinecone Connect is an integration that allows developers to manage Pinecone resources directly from another platform via a simple authentication flow.
Pinecone partners including Twilio and Matillion are already using Pinecone Connect to streamline AI workflows for their users. If you also want to enable a better AI workflow for developers using your platform, you can easily set up the integration to our industry-leading vector database and start offering developers a frictionless experience building knowledgeable AI applications.
Connect your users to Pinecone
Try it now
Simplify AI workflows with a frictionless experience
To build great AI applications, developers need to navigate the AI stack and utilize various tools, including data sources, model providers, and more. Without direct integrations for these tools, developers are forced to switch between multiple platforms. Leaving your workflow/UI for tasks in other environments wastes developers’ time.
Pinecone Connect offers a widget within your platform for developers to sign up or log in, choose or create an organization and project in Pinecone, and generate an API key instantly.
Developers can build with higher velocity utilizing our
industry-leading vector database
to ship more accurate and secure AI applications, in a unified experience directly from your platform. Those who are new to
vector databases
can easily import their data into Pinecone and begin their GenAI journey
for free
.
With the plug-and-play Pinecone Connect integration, you can enjoy direct access to Pinecone without worrying about managing any pass-through operational burdens. Developers own their accounts, we manage the infrastructure, and all you need to do as the platform provider is to
set up the integration
.
Connect to Pinecone
Industry leaders use Pinecone Connect to help users ship more accurate AI applications faster
Industry-leading companies are already leveraging Pinecone Connect to help users build remarkable AI applications and ship faster.
Twilio
's Emerging Technology and Innovation Team uses Pinecone Connect for
AI Assistants
, their project to enable developers to build customer-aware autonomous agents. “Pinecone is the first stop for many developers as they explore the power of vector databases and RAG,” said
Braden Becker, Head of Emerging Technology & Innovation at Twilio
, “We are excited to partner with Pinecone so that developers can bring the data they've already collected to
Twilio AI Assistants
within seconds!”
Twilio AI Assistants + Pinecone Connect
Data productivity cloud
Matillion
uses Pinecone Connect for developers to execute
vector upsert
and
query
in Pinecone directly from their platform. “With Pinecone Connect, Matillion brings unparalleled simplicity to RAG with our no-code Pinecone integration and dropdown activation,” said
Ed Thompson, CTO at Matillion
, “Our users now get instant access to Pinecone on top of our 100+ business and database connectors and data transformation capabilities that ensure data is optimized for RAG, directly on our platform. Together, we create enterprise-grade AI pipelines for any GenAI use cases.”
Hassle-free integration with Pinecone
To enable Pinecone Connect, create a
custom object
or embed our
pre-built widget
, which provides the same functionality but with the ease of a drop-in component.
To start, create an
integration ID
for your app. If you’d like to build a custom object, the ConnectPopup function can be called with either the JavaScript library or script.
If you want to embed our pre-built widget, you can use:
JavaScript
library
(@pinecone-database/connect) or script: Renders the widget in apps and websites.
Colab
(pinecone-notebooks): Renders the widget in Colab notebooks using Python.
JavaScript Example
import {connectToPinecone} from '@pinecone-database/connect'

const setupPinecone = (apiKey) => { /* Set up a Pinecone client using the API key */ }

connectToPinecone(
  setupPinecone,
  {
    integrationId: 'myApp',
    container: document.getElementById('connect-widget')
  }
)
Get started now
First, build your
Pinecone Connect integration
today to improve the developer experience and help your users more easily build knowledgeable AI applications.
Second,
add attribution
to monitor adoption and qualify for go-to-market partnership support.
If you’re interested in deeper collaboration with Pinecone to accelerate your go-to-market of AI solutions,
become our partner
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
