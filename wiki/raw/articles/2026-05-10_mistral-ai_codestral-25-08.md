---
title: "Announcing Codestral 25.08 and the Complete Mistral Coding Stack for Enterprise"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/codestral-25-08"
scraped: "2026-05-10T01:20:52.096632+00:00"
lastmod: "2025-07-30T17:00:40.972Z"
type: "sitemap"
---

# Announcing Codestral 25.08 and the Complete Mistral Coding Stack for Enterprise

**Source**: [https://mistral.ai/news/codestral-25-08](https://mistral.ai/news/codestral-25-08)

Announcing Codestral 25.08 and the Complete Mistral Coding Stack for Enterprise
Research
Jul 30, 2025
Mistral AI
How the world’s leading enterprises are using integrated coding solutions from Mistral AI to cut development, review, and testing time by 50%—and why the playbook now fits every company that wants AI-native software development.
AI-powered coding is taking off, but enterprise adoption still lags due to critical limitations
Over the past year, AI coding assistants have introduced powerful capabilities, such as multi-file reasoning, contextual suggestions, and natural-language agents, all directly within the IDE. Despite these improvements, however, adoption inside enterprise environments has been slow. The reasons have less to do with model performance or the interface, and more with how these tools are built, deployed, and governed.
Key limitations holding back enterprise teams include:
Deployment constraints: Most AI coding tools are SaaS-only, with no options for VPC, on-prem, or air-gapped environments. This is a hard blocker for organizations in finance, defense, healthcare, and other regulated industries.
Limited customization: Enterprises often need to adapt models to their own codebases and development conventions. Without access to model weights, pos-training workflows, or extensibility, teams are locked out of leveraging the best of their codebases.
Fragmented architecture: Agents, embeddings, completions, and plugins are frequently decoupled across vendors—leading to integration drift, inconsistent context handling, and operational overhead. Moreover, coding copilots are not well-integrated into full enterprise platforms, such as product development tools, CRMs, and customer issue trackers.
No unified observability or control: Teams lack visibility into how AI is being used across the development lifecycle. Without telemetry, audit trails, and centralized controls, it’s difficult to scale AI usage responsibly or measure real ROI.
Incompatibility with internal toolchains: Many assistants operate in closed environments, making it hard to connect with internal CI/CD pipelines, knowledge bases, or static analysis frameworks.
For enterprises, these limitations aren’t edge cases—they’re baseline requirements. Solving them is what separates a good developer tool from an AI-native software development platform.
A Full-Stack Approach Built for AI-Native Software Development
Our approach to enterprise coding isn’t a bundle of isolated tools. It’s an integrated system designed to support enterprise-grade software development across every stage—from code suggestion to autonomous pull requests.
It starts with fast, reliable completion—and scales up to full codebase understanding and multi-file automation.
1. Fast, High-Fidelity Code Completion
At the foundation of the stack is Codestral, Mistral’s family of code generation models built specifically for high-precision fill-in-the-middle (FIM) completion. These models are optimized for production engineering environments: latency-sensitive, context-aware, and self-deployable.
Today, we announce its latest update. Codestral 25.08 delivers measurable upgrades over prior versions:
+30% increase in accepted completions
+10% more retained code after suggestion
50% fewer runaway generations, improving confidence in longer edits
Improved performance on academic benchmarks for short and long-context FIM completion
These improvements were validated in live IDE usage across production codebases. The model supports a wide range of languages and tasks, and is deployable across cloud, VPC, or on-prem environments—with no architectural changes required.
Codestral-2508 also brings improvements to chat mode:
Instruction following: +5% on IF eval v8
Code abilities: +5% in average MultiplE
2. Codebase-Scale Search and Semantic Retrieval
Autocomplete accelerates, but only if the model understands your codebase.
Codestral Embed
sets a new standard in this domain. Designed specifically for code rather than general text, it outperforms leading embedding models from OpenAI and Cohere in real-world code retrieval benchmarks.
Key advantages include:
High-recall, low-latency search across massive monorepos and poly-repos. Developers can find internal logic, validation routines, or domain-specific utilities using natural language.
Flexible embedding outputs, with configurable dimensions (e.g., 256-dim, INT8) that balance retrieval quality with storage efficiency—while outperforming alternatives even at lower dimensionality
Private deployment for maximum control, ensuring no data leakage via third-party APIs. All embedding inference and index storage can run within enterprise infrastructure
This embedding layer serves as both the context foundation for agentic workflows and the retrieval engine powering in‑IDE code search features—without sacrificing privacy, performance, or precision.
3. Autonomous Multi-Step Development with Agentic Workflows
With relevant context surfaced, AI can take meaningful action.
Devstral
, powered by the
OpenHands
agent scaffold, enables enterprise-ready agentic coding workflows. It’s built specifically for engineering tasks—cross-file refactors, test generation, and PR authoring—using structured, context-rich reasoning.
Standout capabilities include:
Top open‑model performance on SWE‑Bench Verified: Devstral Small 1.1 scores 53.6%, and Devstral Medium reaches 61.6%, outperforming Claude 3.5, GPT‑4.1‑mini, and other open models by wide margins
Flexible architecture for any environment: Devstral is available in multiple sizes. The open-weight Devstral Small (24B, Apache-2.0) runs efficiently on a single Nvidia RTX 4090 or Mac with 32 GB RAM—ideal for self-hosted, air-gapped, or experimental workflows. The larger Devstral Medium is available through enterprise partnerships and our API for more advanced code understanding and planning capabilities.
Open model for extensibility: Teams can fine-tune Devstral Small on proprietary code, build custom agents, or embed it directly into CI/CD workflows—without licensing lock-in. For production environments requiring higher model performance, Devstral Medium is available with enterprise-grade support, including the ability for companies to post-train and fine-tune.
Delivering agentic automation within private infrastructure lets engineering organizations reduce friction, ensure compliance, and speed up delivery with repeatable, auditable AI workflows.
4. IDE Integration and Operational Control
All capabilities in the Mistral stack—completion, semantic search, and agentic workflows—are surfaced through Mistral Code, a native plugin for JetBrains and VS Code.
It provides:
Inline completions using Codestral 25.08, optimized for FIM and multi-line editing
One-click task automations like “Write commit message”, “Fix function”, or “Add docstring”, powered by Devstral
Context awareness from Git diffs, terminal history, and static analysis tools
Integrated semantic search, backed by Codestral Embed
Mistral Code is built to support enterprise deployment requirements:
Deploy in any environment: cloud, self-managed VPC, or fully on-prem (GA in Q3)
No mandatory telemetry, and no external API calls for inference or search
SSO, audit logging, and usage controls for secure, policy-compliant adoption
Usage observability via the Mistral Console, including metrics on AI-generated code, suggestion acceptance, and agent usage
These features give engineering, platform, and security teams the ability to roll out AI tooling safely, incrementally, and with full visibility.
How It All Fits Together: From Developer Actions to Organizational Impact
The Mistral coding stack integrates autocomplete, semantic retrieval, and agentic workflows directly into the IDE—while giving platform teams control over deployment, observability, and security. In a typical development task:
Say a developer is working on a payments service written in Python. A recent update to a third-party billing API means they need to update the integration logic and add proper error handling.
They start by navigating to the billing handler. As they modify the function signature, Codestral fills in the expected parameters and suggests a first-pass implementation, reducing the need to copy patterns from other services.
Before changing the retry logic, they need to understand how similar failures are handled elsewhere. Instead of switching to Slack or searching GitHub manually, they enter a query directly in the IDE: “How do we handle Stripe timeouts in the checkout flow?” The embedding index, running locally, returns a helper module from another service that wraps retry logic with exponential backoff.
They copy the pattern into their own handler—but realize three other services are using outdated retry code. They invoke a Devstral-powered agent from within the IDE: “Replace all uses of retry_with_sleep in the billing and checkout services with the new retry_exponential helper, and update the docs.” Devstral scans the codebase using the same embeddings, makes the required edits across files, and generates a draft PR. The agent also writes a changelog and updates the README section on error handling.
The developer reviews the PR, confirms the logic, and merges it. A cross-service update that previously would have required search, coordination, and hand-written boilerplate now completes in one editing session—with traceable, reviewable output.
At the organization level, this same workflow unlocks broader advantages:
Every component in the stack can be self-hosted or run on-prem, giving teams control over data, latency, and deployment architecture.
Observability is built in. The Mistral Console tracks usage patterns, model acceptance rates, and agent adoption, providing the data needed to tune rollout and measure ROI.
Security and compliance controls—including SSO, audit logging, and telemetry configuration—make it easy to integrate with internal policies and infrastructure.
No stitching required. Because completion, search, and agents share architecture, context handling, and support boundaries, teams avoid the drift, overhead, and security gaps of piecing together third-party tools.
The result is a development workflow that’s both faster and easier to govern—designed for individual productivity and organizational scale.
Adopted by Leading Enterprises Across Diverse Environments
The Mistral coding stack is already being used in production by organizations across consulting, finance, transportation, and industry—each with different requirements, but shared constraints around data control, deployment flexibility, and internal code complexity.
Capgemini has rolled out the stack across global delivery teams to accelerate development while maintaining code ownership and compliance across clients in defense, telecom, and energy.
Abanca, a leading bank in Spain operating under European banking regulations, uses Mistral’s models in a fully self-hosted deployment to meet data residency and network isolation requirements—without sacrificing usability.
SNCF, the French national railway company, uses agentic workflows to modernize legacy Java systems safely and incrementally, with human oversight built into the loop.
“Leveraging Mistral’s Codestral has been a game changer in the adoption of private coding assistant for our client projects in regulated industries. We have evolved from basic support for some development activities to systematic value for our development teams“.
Alban Alev, VP head of Solutioning at Capgemini France.
In addition, several tier-1 global banks and industrial manufacturers are actively piloting or scaling adoption across their engineering teams—driven by requirements that hosted copilots and fragmented tooling can’t support.
These use cases reflect a growing shift: organizations are no longer looking for isolated assistants—they’re adopting integrated AI systems that match the complexity, security posture, and velocity of modern enterprise software development.
Get Started
The full Mistral coding stack—Codestral 25.08, Devstral, Codestral Embed, and the Mistral Code IDE extension—is available today for enterprise deployment.
Teams can start with autocomplete and semantic search, then expand to agentic workflows and private deployments at their own pace.
To begin:
Install Mistral Code from the
JetBrains
or
VS Code
marketplace
Connect to your preferred deployment modality (cloud, VPC, or on-prem)
If you would like to use the models for your own copilot, get your keys at
console.mistral.ai
. For more information on Mistral’s coding solutions, please visit our
website
and
documentation
.
To evaluate on-prem options, enterprise-scale deployments, or schedule a hands-on pilot, fill out the demand form on this page. A member of the Mistral team will follow up to help tailor the rollout to your environment.
Get in touch.
Explore Codestral and Mistral Code.
0
/
500
By submitting this form, you agree with our
Terms of Service
. We process your data to respond to your contact request in accordance with our
Privacy Policy.
Submit
