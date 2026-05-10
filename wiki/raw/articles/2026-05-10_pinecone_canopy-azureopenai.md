---
title: "Azure OpenAI, meet Canopy"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/canopy-azureopenai/"
scraped: "2026-05-10T01:27:19.462099+00:00"
lastmod: "2024-02-15T23:34:00Z"
type: "sitemap"
---

# Azure OpenAI, meet Canopy

**Source**: [https://www.pinecone.io/blog/canopy-azureopenai/](https://www.pinecone.io/blog/canopy-azureopenai/)

←
Blog
Azure OpenAI, meet Canopy
Audrey Sage
Feb 15, 2024
Engineering
Share:
Jump to section:
Canopy
Azure OpenAI
Build with Canopy and Azure OpenAI Studio
The Canopy CLI
Stay in touch
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Canopy
, the
open-source RAG framework
from Pinecone, is now compatible with
Azure OpenAI Studio
.
By integrating with Azure OpenAI Studio, Canopy users are able to
chat with their documents
and
launch RAG applications into production
knowing their models are backed by the
enterprise-ready features
of Microsoft Azure.
Canopy
Canopy is an open-source, production-ready RAG framework that allows you to build and productionize RAG applications easily. Canopy comes with a CLI for rapid iteration of proof-of-concepts and
various options
for launching your final product into production.
By default, Canopy uses OpenAI’s
text-embedding-3-small
as its embedding model and OpenAI’s
gpt-3.5-turbo
as its LLM. However, Canopy is compatible with any publicly available embedding model or LLM from
Anyscale
,
Cohere
,
OpenAI
, and, now,
Azure OpenAI Studio
.
Azure OpenAI
Azure OpenAI Studio is a cloud service that allows you to deploy your own instances of OpenAI’s powerful models through Microsoft Azure. By accessing OpenAI models through Azure, you can host private instances of OpenAI models, easily fine-tune those models, and keep the full lifecycle of your work in a corporate, enterprise-grade platform.
Azure OpenAI vs OpenAI
While using OpenAI models directly is easy and beginner-friendly, OpenAI does not offer the security controls and enterprise-ready features that a service like Azure does. Some of the differences between the two services are outlined below:
Azure OpenAI
OpenAI
Auth
API keys, Azure account, MFA
API keys
Data security
Encrypted
at rest and in transit
Unclear;
personal data is accessible
to an extent
Compliance
HIPAA
,
FedRAMP
,
GDPR
,
ISOs, SOC 1/2/3
,
etc
.
GDPR, SOC 2/3, CCPA
General security
Threat detection, network security
, security audits,
VNETs and private endpoints
,
RBAC
Unclear; see
Privacy Portal
.
Recovery
Infra has built-in
disaster recovery and backups
N/A
SLAs
Azure Cognitive Services SLA
N/A
Fine tuning
Yes
No
Rate limits
Azure OpenAI
rate limits
OpenAI
rate limits
Note: the above table is a cursory summary; do your own research before taking action from this information.
For enterprise users, one of the chief motivations for using Azure OpenAI Studio is that all model calls stay within the user’s Azure ecosystem – this helps maintain privacy, allows for customization, and simplifies security and compliance.
Note: access to Azure OpenAI Studio is limited. You need to
apply
to use the service.
Build with Canopy and Azure OpenAI Studio
The best way to get a feel for how Canopy works with Azure OpenAI Studio is to build with it! Follow along in
this notebook
to see Canopy in action.
The demo notebook linked above takes you through the process of building an end-to-end RAG application with Canopy and Azure OpenAI Studio. You will create a Pinecone account, apply for Azure OpenAI Studio access, deploy Azure models, and build individual Canopy components to complete your RAG application.
Above is a preview of your final product: a RAG application that answers questions based on the context retrieved from your Canopy index.
The Canopy CLI
One of the most exciting things about Canopy is its CLI. Engineers use the CLI during the proof-of-concept phase of the RAG application development lifecycle.
Through the
canopy chat
command, you can chat back and forth with the documents in your Canopy index. The
ChatEngine
’s answers will differ according to the parameters you set in a configuration file.
You can also use the CLI to quickly build a Canopy index (
canopy new
), upsert documents into that Canopy index (
canopy upsert <file path to data file>
), and start up the Canopy server (
canopy start
).
When using the CLI commands with Azure OpenAI Studio, you will need to modify the
appropriate configuration file
(
azure.yaml
in this case).
Config modifications
The first modification you’ll make to the example Azure configuration file is replacing dummy text in the
LLM
section with the name of your Azure-deployed LLM. This will be the LLM’s “deployment name,”
not
the name of the underlying OpenAI model. For instance, I could deploy a model named “canopy-azure-llm” whose underlying LLM is “gpt-35-turbo.” The “deployment name” that I would put in my config file would be “canopy-azure-llm,” not “gpt-35-turbo.”
Preview of Azure OpenAI Studio's deployments page, showing each model's "deployment name."
The next thing you’ll do is replace more dummy text, this time in the
ContextEngine
section, with your Azure-deployed embedding model’s deployment name:
You can continue modifying the example Azure config file to your heart’s content. Replacing the two instances of dummy text outlined above, though, is mandatory to start using the CLI.
You can use these configuration files programmatically in notebooks and scripts, too; see the “Load from config section” in the
demo notebook
.
Canopy Chat
With your Azure configuration file modified and saved, you can spin up the canopy server, pointing it to your Azure config, by executing
canopy start --config=canopy/config/azure.yaml
from within the
src
directory. You’ll see the Uvicorn server start on your local machine.
Note: you’ll need to set
the appropriate environment variables
for this step to work.
To chat with the docs in your Canopy index, open a new terminal window (ensure your environment variables are still set in this window). In this new window, execute
canopy chat --no-rag
. It’s fun to include the
--no-rag
flag when chatting with your documents because it shows you how your LLM’s answer changes with and without the addition of the context fetched from your Canopy index.
Note that in order to showcase the
no-rag
option, you’ll need to set your OpenAI API key environment variable (
OPENAI_API_KEY
).
You can see above that without the context from the documents in your Canopy index, your LLM has no way of knowing which "Aitchison" you are referencing in your question!
Stay in touch
Integrating with enterprise-grade hosting platforms like Azure OpenAI Studio is just the beginning for Canopy.  Check out Canopy's latest official releases (
7
and
8
) and submit
issues and feature requests
on Github.
We
can’t wait
to see what you build.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
