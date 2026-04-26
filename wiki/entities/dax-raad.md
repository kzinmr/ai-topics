---
title: Dax Raad
type: entity
handle: "@thdxr"
created: 2026-04-13
updated: 2026-04-13
sources: [https://grokipedia.com/page/Dax_Raad]
tags: [person, open-source, ai-coding-agent, serverless]
---


# Dax Raad (@thdxr)

| | |
|---|---|
| **X** | [@thdxr](https://x.com/thdxr) |
| **Blog** | [thdxr.com](https://thdxr.com/) |
| **GitHub** | [thdxr](https://github.com/thdxr) |
| **Role** | Co-founder of Anomaly (SST, OpenCode), Creator of Bumi & OpenAuth |
| **Known for** | OpenCode (80k+ GitHub stars), SST (Serverless Stack), candid takes on AI productivity |
| **Bio** | Self-taught developer and open-source maintainer based in NYC. Creator of OpenCode, a terminal-based AI coding agent, and co-creator of SST. Known for blunt, realistic critiques of AI hype in software engineering. |

## Background

### Early Career and Ironbay

Before his work on serverless and AI developer tools, Raad founded **Ironbay** as a software engineering venture dedicated to helping young companies build lasting technology (via Grokipedia). Ironbay operated as a group of engineers offering services to achieve technology goals for startups (via Grokipedia). Under Ironbay, he maintained an open-source presence on GitHub with repositories focused on Elixir tools (via Grokipedia):

- **Riptide** — a framework for realtime applications
- **Harpoon** — an HTTP client framework emphasizing pluggable and mockable clients
- **Brine** — a configuration loader for Elixir projects

These tools aimed to streamline backend development tasks like real-time functionality, API interactions, and project setup (via Grokipedia).

### Bumi

In 2021, Raad founded **Bumi**, a startup developed in collaboration with his wife that initially created a productivity tool for the healthcare sector (via Grokipedia). Bumi sought to empower healthcare teams to build and scale patient-focused systems by overcoming constraints in legacy electronic medical record (EMR) systems, including challenges with data volume, scalability, and efficient syncing (via Grokipedia). The tool incorporated local-first techniques to deliver high performance for use cases like searching patient data and partial syncing to manage large datasets (via Grokipedia). Ultimately, the project pivoted away from its original direction due to the market's limited size, though it retained some customers (via Grokipedia).

### Early Serverless Contributions

Raad began contributing to the serverless community through technical explorations and writings focused on making AWS serverless development more approachable for developers, particularly in small teams and startups without dedicated DevOps resources (via Grokipedia). In October 2021, he published detailed analyses on his blog addressing common challenges in serverless architectures, such as integrating relational databases with AWS Lambda's ephemeral nature (via Grokipedia). In one notable post, Raad benchmarked performance of three approaches to using relational databases serverlessly: Amazon Aurora Serverless (both standard and with Data API) and PlanetScale (via Grokipedia). He also shared insights into AWS Lambda's internals, breaking down the Runtime API and its execution model to help developers better understand and optimize function execution (via Grokipedia).

These early entrepreneurial efforts reflected Raad's focus on addressing technical friction for teams building applications, through general software assistance for startups via Ironbay and domain-specific system-building via Bumi (via Grokipedia). This groundwork preceded his transition to full-time work on serverless developer tools (via Grokipedia).

## Overview

Dax Raad is a prominent figure in the open-source and serverless communities, best known as the co-creator of **SST (Serverless Stack)** and **OpenCode**. Starting his career with a focus on simplifying AWS deployments through SST, Raad pivoted to AI developer tools in 2025, launching OpenCode which rapidly grew to over 80,000 GitHub stars and 1.5 million monthly active users by early 2026.

Unlike many AI tool founders who focus purely on capabilities, Raad has gained significant attention for his **skeptical and pragmatic views on AI productivity**. His viral tweet in February 2026 ("Dax Raad just dropped the most honest take on AI productivity") argued that while AI removes coding bottlenecks, it exposes deeper organizational issues like lack of good ideas, bureaucracy, and unmotivated workforces.

Raad represents the "builder-first" philosophy: creating tools that he and his team use daily, prioritizing developer experience (DX) and privacy (local-first, bring-your-own-key models) over venture-scale growth metrics.

## Core Ideas

### AI Productivity: The "Honest Take"
Raad challenges the narrative that AI automatically leads to 10x productivity. He argues that **coding was never the real bottleneck**; the constraints were often beneficial because they filtered out bad ideas.
> "Your org rarely has good ideas. Ideas being expensive to implement was actually helping."
> "Even when you produce work faster you're still bottlenecked by bureaucracy and the dozen other realities of shipping something real."

He warns of a "slop" crisis where high-performers are overwhelmed by AI-generated low-quality code, leading to burnout and attrition.

### Open Source as a Necessity, Not Just Ethics
Raad believes open source is essential for rapid iteration and community feedback in the AI era.
> "Just because something's open source doesn't mean it's going to be any better than the closed source equivalent... We need help improving how it all works."
He positions OpenCode as the open-source alternative to proprietary tools like Cursor or GitHub Copilot, emphasizing model freedom (bring your own API keys) and privacy.

### Developer Experience (DX) over Benchmarks
Raad dismisses the "benchmark wars" among AI models.
> "You start to think if I do better on these benchmarks, you'll get more users. But people can't tell. They literally cannot tell."
He focuses on the **experience** of using the tool — native terminal UIs, fast feedback loops, and seamless integration with existing workflows — rather than raw model scores.

### Local-First and Serverless
Before AI, Raad was a strong advocate for local-first SaaS and serverless architectures. His work on **Bumi** and **SST** reflects a desire to give developers control over their infrastructure without the complexity of managing servers. He has a deep appreciation for the actor model (Erlang/Elixir) and functional approaches to distributed systems.

## Key Work

### OpenCode
- **Description**: An open-source, terminal-native AI coding agent (MIT License).
- **Impact**: 135k+ GitHub stars, 1.5M+ MAUs (as of early 2026).
- **Key Features**: Multi-agent support, native TUI (rewritten in Zig + SolidJS for v1.0), model agnostic (works with any provider via Zen or local models), and privacy-focused.
- **Role**: Co-founder alongside Jay V, Frank Wang, and Adam Elmore. Raad is the public face and primary technical voice.
- **Launch Details**: OpenCode was launched on June 19, 2025, by Jay V, Frank Wang, Dax Raad, and Adam Elmore (via Grokipedia). The project emerged as an open-source alternative to proprietary AI coding assistants such as Anthropic's Claude Code, motivated by a recognition that the proliferation of AI coding models would create demand for a flexible, provider-agnostic tool (via Grokipedia).
- **Architecture**: OpenCode employs an agent-based architecture centered around a client-server model, where the backend handles LLM interactions, tool execution, session management, and orchestration, while the frontend delivers a terminal user interface (TUI) (via Grokipedia). Primary agents include Build (full tool access) and Plan (read-only analysis requiring user confirmation), with subagents for specialized roles like General (multi-step tasks) and Explore (read-only codebase navigation) (via Grokipedia).
- **Community Response**: When Anthropic attempted to block third-party tools like OpenCode from accessing certain Claude API endpoints, developers quickly devised and shared workarounds within 15–20 minutes (via Grokipedia). In January 2026, OpenCode announced a formal partnership with GitHub enabling full support for authentication using existing GitHub Copilot subscriptions (via Grokipedia).

### SST (Serverless Stack)

- **Description**: A TypeScript framework for building serverless applications on AWS.
- **Impact**: 25k+ GitHub stars, profitable by 2025.
- **Philosophy**: "SST allows developers to define infrastructure as code... enabling deployment to personal AWS accounts." It simplifies the hundreds of AWS services into a manageable developer experience.
- **Key Technical Features**: SST provides higher-level components that simplify common workflows, such as `sst.aws.Function` for defining functions, `sst.aws.Bucket` for storage, and `sst.aws.Service` for containerized or API services with linking to other resources for automatic access and configuration (via Grokipedia). A signature capability is **Live** (previously known as Live Lambda Development), which enables local editing, debugging, and testing of functions while they remain invoked remotely by deployed resources. Changes are automatically detected and reloaded in under 10 milliseconds (via Grokipedia). Deployment is managed through the SST CLI, with `sst dev` launching the local development environment and `sst deploy` provisioning to named stages and regions for isolated environments (via Grokipedia).
- **Evolution**: The framework evolved to SST v3 (released August 20, 2024), which replaced CDK and CloudFormation with Pulumi (using Terraform providers) to address earlier limitations and further simplify deployments across a broader ecosystem (via Grokipedia).
- **Role**: Core Maintainer and Co-founder.
- **Industry Impact**: SST has played a significant role in popularizing serverless architectures for developers and teams without extensive DevOps expertise. Its newsletter reaches over 90,000 subscribers and its guide serves as a widely read resource for serverless development on AWS (via Grokipedia). The SST user base influenced broader AWS ecosystem developments, including the creation of OpenNext — motivated by requests from SST users seeking better Next.js deployments on AWS Lambda (via Grokipedia).

### Bumi
- **Description**: A healthcare sector productivity tool founded in 2021 in collaboration with Raad's wife (via Grokipedia).
- **Purpose**: Empowered healthcare teams to build and scale patient-focused systems by overcoming constraints in legacy EMR systems, including challenges with data volume, scalability, and efficient syncing (via Grokipedia).
- **Technical Approach**: Incorporated local-first techniques to deliver high performance for use cases like searching patient data and partial syncing to manage large datasets (via Grokipedia).
- **Outcome**: The project pivoted away from its original direction due to the market's limited size, though it retained some customers (via Grokipedia).

### OpenAuth
- **Description**: An open-source, self-hosted authentication provider that implements a standards-compliant OAuth 2.0 solution, designed to simplify authentication for web, mobile, single-page, API, and third-party clients (via Grokipedia).
- **Purpose**: Provides developers with an alternative to proprietary services like AWS Cognito, Auth0, or Clerk by enabling full ownership of authentication infrastructure (via Grokipedia).
- **Features**: Supports standard OAuth 2.0 flows (authorization code flow for server-side apps, token flow with PKCE for client-side/mobile), multiple identity providers (Google, GitHub, email/password, PIN codes), themeable prebuilt UI components, and a minimal storage model using simple key-value stores (via Grokipedia).
- **Deployment**: Can be deployed as a standalone service or embedded directly within an application. Built for modern runtimes including Node.js, Bun, AWS Lambda, and Cloudflare Workers (via Grokipedia).
- **Status**: In beta (via Grokipedia).

### OpenTUI
- **Description**: A custom terminal user interface (TUI) framework developed to power the OpenCode terminal client (via Grokipedia).
- **Technology**: Combines Zig for performance-critical native rendering with SolidJS for reactive UI construction (via Grokipedia). Zig was selected to enable low-overhead, native rendering during intensive tasks (via Grokipedia).
- **Architecture**: Structured as a monorepo with `@opentui/core` providing an imperative API, primitives, and hierarchical renderables supporting positioning, nesting, styling, and terminal output. Includes Tree-Sitter integration for syntax highlighting. The `@opentui/solid` package supplies a SolidJS reconciler for reactive component-based UI within the terminal (via Grokipedia).
- **Origin**: Created as part of OpenCode's 1.0 release, replacing the prior Go + Bubble Tea TUI implementation to address performance and capability limitations (via Grokipedia).

## Notable Quotes

> "The 2 people on your team that actually tried are now flattened by the slop code everyone is producing, they will quit soon."

> "They're not using AI to be 10x more effective they're using it to churn out their tasks with less energy spend."

> "I'm tired of people feeling like suddenly the tables are going to turn and things are going to be easier. They're not easier. My life is just as hard as it's ever been." (On AI in engineering)

> "Just because something's open source doesn't mean it's going to be any better than the closed source equivalent."

## Recent Themes (2025–2026)

- **The "Slop" Crisis**: Critiquing the degradation of code quality due to unchecked AI generation.
- **Model Agnosticism**: Advocating for tools that don't lock users into a single LLM provider.
- **Terminal Renaissance**: Pushing for better terminal-based tools (OpenCode TUI) as a superior environment for focused coding.
- **Open Source Sustainability**: Exploring business models (like Zen) that support open source without compromising user freedom.

### Monetization: The "Double Miracle" Approach

Raad has articulated a monetization model for open-source projects he terms the **"double miracle"** approach (via Grokipedia). This framework addresses the perennial challenge of sustaining open-source development financially while preserving community ownership and freedom (via Grokipedia). The "double miracle" refers to the rare alignment of two outcomes: (1) the organic explosion of community contributions, adoption, and collaborative improvement that propels a project forward without central control; and (2) the emergence of viable, non-restrictive revenue streams that enable maintainers to dedicate time and resources to continued innovation (via Grokipedia).

In applying this model to OpenCode during its rapid growth phase, Raad focused on leveraging widespread community traction to attract strategic partnerships with major platforms and providers. This enabled funding through enterprise-oriented support and integrations without compromising the project's open-source license or accessibility for individual users (via Grokipedia).

### Emphasis on Execution and Power Users

Raad consistently emphasizes rigorous execution and a primary focus on serving power users as foundational to creating enduring software products and tools (via Grokipedia). He argues that exceptional execution — particularly in eliminating small but cumulative frictions such as slow interactions, spinners, or delays — dramatically improves daily user experience, even if users rarely articulate these issues explicitly (via Grokipedia). For applications used intensively throughout the workday, optimizing for sustained speed after initial load outweighs prioritizing fast first impressions (via Grokipedia).

Central to his approach is the conviction that retention depends primarily on satisfying power users through deep, capable foundations. He advocates building advanced primitives first, then assembling them into streamlined experiences that the majority of users encounter. This strategy balances simplicity for new users with the power required by advanced users (via Grokipedia).

## Public Engagements

### Conference Talks

- **"The Hidden Infrastructure Powering Our Frontends"** — React Miami 2023 (JSWORLD Conference): Examined the complex cloud architectures enabling high-performance deployments of modern frontend frameworks like Next.js on platforms such as Vercel, Netlify, and AWS Amplify. Broke down AWS S3, CloudFront, Lambda, Lambda@Edge, and Incremental Static Regeneration techniques. Highlighted SST as a framework for replicating these capabilities directly on AWS with reduced complexity and no vendor lock-in (via Grokipedia).
- **"The GraphQL Stack"** — SST 1.0 Conf: Centered on assembling optimal GraphQL tools for a fully typesafe development experience spanning infrastructure, backend services, and frontend integration (via Grokipedia).
- **"AI Changes Nothing"** — Late 2025 AI Conference: Argued that AI does not fundamentally alter the essential elements of building successful products — marketing, user onboarding, and long-term retention continue to demand human creativity, taste, and rigorous execution (via Grokipedia).

### Podcasts and Interviews

- **Ready, Set, Cloud!** (June 2023): Explored building serverless applications effectively, highlighting domain-driven design and proper data boundaries in project structure (via Grokipedia).
- **devtools.fm** (October 2023): Detailed SST as a TypeScript framework built on AWS CDK, covering its primitives, local development model, and critiques of proprietary platforms that monetize developer knowledge (via Grokipedia).
- **localfirst.fm** (May 2024): Discussed local-first SaaS approaches as applied to projects including SST (via Grokipedia).
- **Kent C. Dodds' platform**: Spoke about authentication challenges and OpenAuth as a self-owned, spec-compliant solution addressing issues with services like AWS Cognito (via Grokipedia).
- **Baseten** (October 2025): Discussed creating OpenCode as an open-source alternative to proprietary terminal-based tools, emphasizing model flexibility, community contributions, terminal workflows, and preference for real-world user experience over benchmarks (via Grokipedia).
- **AI Giants** (December 2025): Argued that AI changes nothing fundamental to building winning products despite widespread claims otherwise (via Grokipedia).
- **Live interview with Nuno Maduro** (January 2026): Discussed OpenCode's development and philosophy (via Grokipedia).

## Related People

- [[jay-v]]: Co-founder of Anomaly (SST/OpenCode).
- : Co-founder/CTO of Anomaly.
- : Co-founder of Anomaly, AWS Hero.
- : Co-founder of Supabase; marveled at OpenCode's growth compared to Supabase.

## X Activity Themes

- **AI Coding Tools**: Daily usage, feature announcements, and critiques of competitors.
- **Software Engineering Realities**: Rants about bureaucracy, hiring, and the "myth" of productivity gains.
- **Open Source Philosophy**: Defending MIT licenses, community contributions, and transparency.
- **Terminal/CLI Culture**: Sharing tips on Neovim, shell workflows, and local-first tools.
