---
title: "Introducing Mistral Code"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/mistral-code"
scraped: "2026-05-10T01:20:40.138282+00:00"
lastmod: "2025-06-04T21:24:32.957Z"
type: "sitemap"
---

# Introducing Mistral Code

**Source**: [https://mistral.ai/news/mistral-code](https://mistral.ai/news/mistral-code)

Introducing Mistral Code
Product
Jun 4, 2025
Mistral AI
Software engineering teams in enterprises can finally bring frontier-grade AI coding into their workflow in a secure, compliant manner. Mistral Code is an AI-powered coding assistant that bundles powerful models, an in-IDE assistant, local deployment options, and enterprise tooling into one fully supported package, so developers can 10X their productivity with the full backing of their IT and security teams.
Mistral Code builds on the proven open-source project
Continue
, reinforced with the controls and observability that large enterprises require. Private beta is open today for
JetBrains IDEs
and
VSCode
, with general availability planned soon. Mistral Code is a continuation of our efforts to make developers successful with Al, following last month’s releases of
Devstral
and
Codestral Embed
.
Why we built Mistral Code
Our goal with Mistral Code is simple: deliver best-in-class coding models to enterprise developers, enabling everything from instant completions to multi-step refactoring—through an integrated platform deployable in the cloud, on reserved capacity, or air-gapped on-prem GPUs.
Unlike typical SaaS copilots, all parts of the stack—from models to code—are delivered by one provider subject to a single set of SLAs, and every line of code resides inside the customer’s enterprise boundary.
When we spoke with VPs of engineering, platform leads, and CISOs, they surfaced four recurring blockers that stop mainstream copilots at the proof-of-concept stage:
Limited connectivity to proprietary repos and internal services.
Minimal customisation of the underlying models or prompts.
Shallow task coverage that ends at “autocomplete” instead of finishing multi-step work.
Fragmented SLAs spread across one vendor for the plug-in, another for the model, and a third for infra.
Mistral Code addresses those pain points with a single, vertically-integrated offering: models, plugin, admin controls, and 24X7 support—so platform teams retain visibility and can tie AI-powered productivity back to ROI.
Code with intelligence, control with confidence
At its core, Mistral Code is powered by four models that are state of the art in coding:
Codestral
for fill-in-the-middle / code autocomplete
Codestral Embed
for code search and retrieval
Devstral
for agentic coding
And
Mistral Medium
for chat assistance
Critically, customers can fine-tune or post-train the underlying models on private repositories or distill lightweight variants—capabilities that simply don’t exist in closed copilots tied to proprietary APIs.
Mistral Code is proficient in 80+ programming languages and can reason over files, Git diffs, terminal output, and issues. We’re currently testing the product in helping engineers move beyond coding assistance and suggestions to complete fully scoped tickets: opening files, writing new modules, updating tests, and even executing shell commands—all under configurable approval workflows so senior engineers stay in control.
For IT managers, a rich admin console exposes granular platform controls, deep observability, seat management, and usage analytics.
Adopted by global enterprises
Our customers validate the approach:
Abanca
, a leading bank in Spain and Portugal, has deployed Mistral Code at scale for development teams in a hybrid configuration so they can prototype in the cloud while core banking code stays on-prem.
SNCF
, France's national railway company, is empowering its 4000 developers with AI through Mistral Code Serverless, and
Capgemini
, our first global systems-integrator partner, is to deploy Mistral Code on-premises for 1500+ developers in the service of client projects in regulated industries.
We owe a debt of gratitude to the Continue community for pioneering the original developer experience; our fork preserves their extensibility but layers on significant improvements to multi-line editing, chat, and enterprise-grade extras such as fine-grained RBAC, audit logging, issue resolution / suggestion acceptance metrics, and so on. While our initial release is a private beta to collect customer feedback, we are excited to announce general availability soon, and aim to start making contributions to the upstream repo in forthcoming releases.
Getting started
Request access
from your Mistral account team to spin up a pilot. You can choose serverless, cloud, or self-hosted deployment—and get coding with frontier intelligence in minutes.
Share this article
More from Mistral AI
News
Models
AI Services
