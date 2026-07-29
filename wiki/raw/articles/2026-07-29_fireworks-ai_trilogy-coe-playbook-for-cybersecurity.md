---
title: "Trilogy’s Playbook for Open-Weight Cybersecurity with Kimi K3"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/trilogy-coe-playbook-for-cybersecurity"
scraped: "2026-07-29T06:00:56.137148+00:00"
lastmod: "2026-07-29T00:03:51.000Z"
type: "sitemap"
---

# Trilogy’s Playbook for Open-Weight Cybersecurity with Kimi K3

**Source**: [https://fireworks.ai/blog/trilogy-coe-playbook-for-cybersecurity](https://fireworks.ai/blog/trilogy-coe-playbook-for-cybersecurity)

Kimi K3 on Fireworks: Frontier Intelligence You Can Own
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Trilogy Coe Playbook For Cybersecurity
Trilogy’s Playbook for Open-Weight Cybersecurity with Kimi K3
PUBLISHED
7/26/2026
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
As you hopefully know,
Kimi K3
recently went live on Fireworks. Amid last week's hype about Kimi vs. closed-source benchmarks, the cybersecurity field also took plenty of notice. As such, our friends at Trilogy moved quickly to publish their new cybersecurity playbook. This playbook builds on our continued work together, when we previously explored how Trilogy validated
Open-Weight AI Models for Enterprise AI Workloads
.
Trilogy built its
AI Cybersecurity Playbook
around Kimi K3 on Fireworks because defensive AI workloads require a deployment path that organizations can depend on.
The defender's workload is continuous. Teams audit repositories, triage scanner output, review pull requests, investigate alerts, and preserve incident timelines. During the recent Hugging Face incident,
frontier models breached production infrastructure
during an authorized evaluation and executed more than 17,000 autonomous actions over the course of multiple days, before containment. Due to the persistence and scale of agentic cyber threats today, the reality is that effective cyber-defense must not ignore the unit economics of AI. To quote the playbook:
The defender’s workload is high-volume. You audit every repo, triage every scan, review every PR, preserve incident timelines, and retest fixes. A model that is almost strong enough and cheap enough to run often can be more useful than a stronger model that is gated, expensive, or unavailable during the incident.
Specialized frontier cyber capabilities are often distributed through trusted-access programs, applications, vetting, and policy controls. Those controls may be justified for the services that operate them. They also become part of the operational risk model for any defensive workflow that depends on them.
Public weights create additional deployment paths. Teams can use managed inference for immediate access, move to dedicated capacity as throughput or isolation requirements grow, and retain further deployment options when the workload justifies the infrastructure. Open weights make access and deployment more directly connected to engineering and capacity decisions.
A practical reference stack
The Trilogy AI Center of Excellence built a public AI Cybersecurity Playbook and exercise pack around Kimi K3 on Fireworks. Its
technical overview
links the interactive playbook, the repository, and ten exercises against local training applications.
The open-model advantage: Shannon runs pre-recon and recon sequentially, then pairs five vulnerability-analysis agents with exploitation agents before producing reproducible findings.
The playbook uses a consistent division of labor:
Deterministic tools establish structure and facts.
Code indexes repositories, parses scanner output, computes statistics, deduplicates findings, and records coverage.
Kimi K3 handles judgment.
The model evaluates reachability, impact, prioritization, remediation, and verification inside bounded units of work.
A separate verification stage raises the evidence level.
Fresh-context review challenges static findings. Authorized dynamic testing reproduces impact where appropriate. Regression tests confirm closure after remediation.
The path-centric audit shows how this works. A Tree-sitter indexer maps entry points, call graphs, and security-sensitive sinks across Python, JavaScript, and TypeScript. Each model call receives a bounded bundle containing one entry point and the code reachable from it.
The resulting question is specific:
Is this sink reachable from this route, along which calls, and with what impact?
Semgrep's evaluation found that K3's security-scanning performance varied substantially by harness and repository scale, with weaker precision on its largest target. The result supports the playbook's emphasis on bounded inputs, deterministic indexing, explicit coverage, and separate verification. The repository exposes that harness for inspection and adaptation.
What Fireworks provides
Fireworks exposes Kimi K3 through an
OpenAI-compatible API
, which lets teams integrate the model with familiar clients, agent frameworks, scanners, and CI systems.
The prompts, JSON schemas, tool definitions, coverage records, and run artifacts remain part of the application. Fireworks provides the managed inference layer for the model calls inside that workflow.
This separation matters for security engineering. Deterministic indexing and reporting can run locally or inside existing infrastructure. K3 is invoked for the tasks where model reasoning adds value. Teams can scale the inference layer independently as audit volume, latency requirements, or isolation needs change.
The approach also fits the argument made in the recent open-weights letter. Its signatories argue that open models broaden defensive access, support transparency, and allow more organizations to find and remediate vulnerabilities. Fireworks turns that availability into an endpoint teams can use in production workflows.
Start with one workflow
The
Trilogy AI Center of Excellence overview
links the interactive playbook, repository, and exercises, along with helpful plug and play code snippets.
Setup for K3 on Fireworks:
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
export FIREWORKS_API_KEY="fw_..."
npx @keygraph/shannon@latest setup
# In the Pi custom-provider configuration:
# API base: https://api.fireworks.ai/inference/v1
# Model:    accounts/fireworks/models/kimi-k3
npx @keygraph/shannon@latest start \
-u https://your-staging-app.com \
-r /path/to/your/repo
The path-centric audit is a useful starting point. It produces bounded analysis bundles, a fresh-context verification pass, explicit entry-point coverage, and structured findings that can be compared with an existing scanner.
With Kimi K3's weights public, teams have a broader deployment spectrum. They can begin with the
managed Fireworks endpoint
and evaluate dedicated capacity as volume, latency, or isolation requirements grow. The surrounding audit workflow remains under the team's control while Fireworks operates the model-serving infrastructure.
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
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
