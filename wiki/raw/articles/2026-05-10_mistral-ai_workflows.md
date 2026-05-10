---
title: "Workflows for work that runs the business"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/workflows"
scraped: "2026-05-10T01:19:56.195221+00:00"
lastmod: "2026-04-29T13:49:09.381Z"
type: "sitemap"
---

# Workflows for work that runs the business

**Source**: [https://mistral.ai/news/workflows](https://mistral.ai/news/workflows)

Extract data
Retrieve context
Cross-reference records
Generate report
Execute action
Workflows
for work that runs the business
Workflows is now in public preview.
Today, we're releasing Workflows in public preview. Workflows is the orchestration layer for enterprise AI. It brings the durability, observability, and fault tolerance required to move AI-powered processes from proof of concept to production reliably. Organizations like
ASML, ABANCA, CMA-CGM, France Travail, La Banque Postale, Moeve
, and many more are already running Workflows to automate critical processes.
Enterprise teams today have access to capable models. What they lack is a way to run them reliably in production. We see this across every industry we work with. The failure modes are consistent: pipelines that run in a notebook but fail silently in production with no trace, long-running processes that can't survive a network timeout, multi-step operations that need human approval mid-execution but have no mechanism to pause and resume, and systems that offer no way to verify they're still doing what they're supposed to after deployment.
Building all of the capabilities to address these challenges is months of complex work for enterprises: the orchestration layer has to be stitched together from scratch, and the components it connects, inference, agents, connectors, observability, each come from different tools with their own interfaces and formats.
Workflows is part of Studio, so the orchestration layer and the components it orchestrates are built to work together. Once a business process is identified, developers write the workflow in Python. Every workflow can then be published to Le Chat so anyone in the organisation can trigger it. Every step is tracked and auditable in Studio. By bringing all of this together, Workflows lets your organisation go from identifying a use case to running it in production in days.
Try Workflows
Run workflow
Chat
Run workflow
Workflow graph
Trigger
Extract
Retrieve
Validate
Cross-ref
Approval
Report
Execute
Reject
Archive
Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.
Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.
Execution
0.0
s
2.0
s
4.0
s
6.0
s
8.0
s
10.0
s
1
Trigger workflow
2
Extract data
3
Retrieve context
4
Apply validation rules
5
Cross-reference records
6
Request approval
7
Generate report
8
Execute action
Workflows deployed in the real world
As mentioned, Mistral AI customers are already using Workflows to automate business processes and run them in production. The examples below show how durability, observability, and human-in-the-loop approvals work in practice.
Cargo release automation.
Global shipping runs on paperwork. A single cargo release can involve customs declarations, dangerous goods classifications, safety inspections, and regulatory checks across multiple jurisdictions. A missed step can result in cargo delays at port and potential compliance breaches.
The operational requirements for a use case like this are: the system must survive intermittent timeouts, pause mid-execution for human review, and produce a precise account of where and why when something fails.
Using Workflows, a customer is able to automate this end to end. The workflow validates every incoming shipping document against customs rules, checks for anomalies, flags anything that needs human sign-off, waits for approval, then releases the cargo. With Workflows, the human approval step is a single line of code: wait_for_input(). The workflow pauses, waits for as long as it takes with no compute consumption, notifies the reviewer, and resumes exactly where it left off. Studio records the full execution history.
Document compliance checking.
KYC reviews are manual, repetitive, and time-consuming. A single customer onboarding can require extracting identity documents, verifying them against sanctions lists and PEP databases, cross-referencing regulatory requirements across jurisdictions, and producing a structured risk assessment with supporting evidence. Done manually, this takes hours of analyst time per case.
The operational requirements here are speed and auditability. A system to automate a process like this should be fast and should document the steps and reasoning behind them for meeting regulatory requirements.
With Workflows, the entire review process only takes minutes and Studio surfaces every step as a structured timeline you can drill into at any level of detail, down to specific traces with native support for OpenTelemetry.
Customer support triage.
Support teams deal with volume. Refund requests, technical issues, billing disputes, account escalations. Routing them to the right team quickly and consistently is what determines resolution time.
The operational requirement here is correctability. Automated routing will get things wrong. When it does, the team needs to see why a ticket was routed the way it was, and fix it without retraining the model.
With Workflows, incoming tickets are analysed, categorised by intent and urgency, and routed to the right downstream process automatically. Each routing decision is visible and traceable in Studio. When the categorisation is wrong, the team corrects it at the workflow level.
Why Workflows
Durable execution.
Workflows track state at every step. If a process fails, it resumes where it left off. As a result, developers can focus more on writing business logic instead of recovery logic.
Observability.
Every branch, retry, and state change is recorded in Studio. If a decision needs to be investigated months later, the full timeline is there to show how it was reached.
Human-in-the-loop.
A single line of code pauses a workflow for approval. The reviewer responds from Le Chat, a webhook, or any connected surface, and the workflow picks up where it stopped.
Native to Studio
. Workflows use the same agents and connectors as the rest of Studio. There's no separate integration work to wire them in.
Enterprise readiness.
Workspaces within Studio keep teams and projects separated, and role-based access control (RBAC) makes sure those rules are enforced consistently.
Built for developers and business teams.
Engineers write workflows as code. Business teams run them from Le Chat.
Deployment flexibility.
The control plane runs on Mistral. Workers and data processing run in your environment, right where your critical services are hosted: cloud, on-prem, or hybrid.
Under the hood
Workflows is built on Temporal's durable execution engine, the same infrastructure that powers orchestration at Netflix, Stripe, and Salesforce. We extended it for AI-specific workloads by adding streaming, payload handling, multi-tenancy, and observability that the core engine does not provide out of the box.
The deployment model is split between Mistral and your environment, and separates the control plane from the data plane. Mistral hosts the orchestration infrastructure: Temporal cluster, the Workflows API, and Studio. You deploy workers on your own Kubernetes environment using a separate Helm chart, and they connect back to the central cluster via secure credentials. Your data and business logic stay within your perimeter.
The Mistral SDK handles retry policies, tracing, timeouts, rate limiting, and human-in-the-loop through decorators and single-line configuration, so the only thing you write is the business logic itself.
Get started
The Python SDK is how developers write and run workflows. v3.0 is now publicly available and installable with a single command:
Install Workflows
Try Workflows in Studio
From scratch or using our demo templates.
Read the docs
Build your first Workflow in Studio
Talk to our team
Share this article
More from Mistral AI
News
Models
AI Services
