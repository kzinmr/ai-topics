---
title: "OpenAI"
type: entity
created: 2026-04-16
updated: 2026-06-06
tags:
  - company
  - model
  - ai-agents
  - product
  - openai
aliases: ["OpenAI Inc."]
sources:
  - raw/newsletters/2026-05-17-anthropic-pulls-away-openai-strikes-back-and-google-s-gemini-rising.md
  - raw/newsletters/2026-04-24-chatgpt-images-2-0-is-genuinely-fantastic.md
  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
  - raw/newsletters/2026-04-28-openai-breaks-free-from-microsoft.md
  - raw/articles/simonwillison.net--2026-apr-25-romain-huet--fea00393.md
  - raw/articles/2026-04-28-openai-aws-bedrock-partnership.md
  - raw/newsletters/2026-05-03-gemini-gets-to-work-claude-s-big-pull-and-openai-unchained.md
  - raw/articles/2026-05-04_techcrunch-anthropic-openai-jv.md
  - raw/articles/2026-05-05_reuters-openai-anthropic-jv-acquisitions.md
  - raw/articles/openai.com--signals-research-2026q1-update--45f994a1.md
  - raw/newsletters/2026-05-15-codex-goes-everywhere.md
  - raw/newsletters/2026-05-22-ainews-openai-gpt-next-disproves.md
  - raw/articles/2026-06-04_openai_chatgpt-memory-dreaming.md
  - raw/articles/2026-06-04_openai_openai-biodefense-intelligence-age.md
  - raw/articles/simonwillison.net--2026-jun-5-openai-help-lockdown-mode--2ec234f9.md
---

# OpenAI

| | |
|---|---|
| **Type** | AI Research & Product Company |
| **Founded** | 2015 |
| **Leadership** | Sam Altman (CEO), Greg Brockman (Products), Thibault Sottiaux (Core Product), Ilya Sutskever (Chief Scientist, former) |
| **Key Products** | GPT-4/5 series, ChatGPT, Codex, DALL-E, Whisper, o-series, Agents SDK, Symphony |
| **Website** | [openai.com](https://openai.com) |
| **API** | [platform.openai.com](https://platform.openai.com) |

## Overview

OpenAI is a leading AI research and product company known for developing the GPT series of large language models, ChatGPT, and a growing ecosystem of AI developer tools. The company has been at the forefront of the AI agent revolution, releasing the **Agents SDK** (v0.14.0, April 2026) which provides standardized infrastructure for building production-ready agents with sandbox execution capabilities.

### Key Products & Technologies

#### Language Models
- **GPT-4/5 series** — Frontier LLMs powering ChatGPT and API integrations
- **GPT-5.5** (Apr 2026) — First fully retrained base model since GPT-4.5. Designed for multi-step work (planning, tool use, self-checking). Scored 82.7% on Terminal-Bench 2.0. Key unlock for production agent deployment.
  - **Key change:** Since GPT-5.4, OpenAI unified Codex and the main model into a single system. There is no separate coding line anymore. GPT-5.5 extends this further with strong gains in agentic coding, computer use, and any task on a computer (per Romain Huet).
  - **Prompting guidance:** OpenAI recommends treating GPT-5.5 as a **new model family to tune for**, not a drop-in replacement for GPT-5.2 or GPT-5.4. Start with the smallest prompt that preserves the product contract, then tune reasoning effort, verbosity, tool descriptions, and output format ([Simon Willison, Apr 2026](https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/)).
  - **Codex migration:** OpenAI recommends running `$openai-docs migrate this project to gpt-5.5` to follow the embedded upgrade guide in their openai-docs skill.
- **GPT-5.5 Instant** (May 2026) — Now the **default model** for both ChatGPT and API (`gpt-5.5-chat-latest`). Improvements include: factuality, baseline intelligence, image understanding, and conversational tone. Key new capability: access to saved memories, past chats, uploaded files, and connected Gmail for personalized responses.
- **o-series** — Reasoning-focused models with extended thinking
- **GPT-4o / GPT-4o-mini** — Multimodal models with vision and audio capabilities

### Developer Tools
- **Workspace Agents** (Apr 2026) — Codex-powered shared agents for Business/Enterprise plans. Integrates Slack, Salesforce, Notion, Google Drive with persistent memory and role-based governance. Designed for organizational workflows, not individual use.
- **Agents SDK** (v0.14.0, April 2026) — Python SDK for building agents with:
  - **TypeScript support** (May 2026) — Agents SDK now supports TypeScript, including sandbox agents and open-source harness. Major platform expansion.
  - **Auto Review** (May 2026) — New feature for lower-friction approvals in automated agent workflows.
  - Native sandbox execution (isolated workspaces)
  - Harness/Compute architectural separation
  - Manifest-based workspace portability
  - Standardized integrations: MCP, Skills, AGENTS.md, Shell, Apply Patch
  - Provider ecosystem: Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel
  - Security: Default-deny, relative paths only, `..` traversal blocked
  - Durability: Snapshotting & rehydration for long-horizon tasks
- **Symphony** — Agent orchestration framework (see [[concepts/harness-engineering]])
- **Codex** — AI coding agent. Since GPT-5.4, Codex has been unified into the main model — there is no separate coding model line. No GPT-5.5-Codex will be released ([Romain Huet, Apr 2026](https://simonwillison.net/2026/Apr/25/romain-huet/)).
  - **Codex Push (May 2026):**

- **ChatGPT for PowerPoint (May 2026 Beta)**: Create slides, update existing decks, turn source material into presentations. Available for ChatGPT Business, Enterprise, Edu, Free, Go, Pro, Plus users. Users must review formatting, claims, and numbers before sharing.
 OpenAI aggressively targeting non-technical users. Migration tools to import from Claude Cowork. Workplace features (slides, sheets). iMessage handoff skill. `/pet` fun feature. See [[concepts/vibe-physics]] for scientific Codex applications.

### Other Products
- **ChatGPT** — Conversational AI interface
- **GPT Image 2 (ChatGPT Images 2.0)** — Second-generation image generation integrated into ChatGPT. Includes **Thinking mode** with web search mid-generation. 2K resolution with legible non-Latin scripts. Hit #1 on all Image Arena leaderboards; beat Google's Nano Banana models by +242 points (largest gap ever) in Text-to-Image. See [[concepts/chatgpt-images-2.0]] for full details.
- **ChatGPT for Clinicians** (Apr 2026) — Free tool for verified US physicians, NPs, PAs, pharmacists. Includes cited medical sources and HIPAA-compliant options.
- **DALL-E** — Text-to-image generation
- **Whisper** — Speech recognition
- **Sora** — Video generation

### Strategic Initiatives (OpenAI Ecosystem)
- **"The Deployment Company" JV (May 2026)** — OpenAI raised ~$4B at $10B pre-money valuation for a dedicated deployment company. Backed by 19 investors (TPG, Bain Capital, SoftBank, etc.). COO Brad Lightcap is shifting to lead "special projects" and this JV. Represents the shift from model API sales to enterprise service delivery. See [[concepts/ai-services-joint-ventures]].
- **World ID 4.0 / AgentKit** — Sam Altman's Worldcoin project reached 18M verified users across 160 countries. AgentKit enables AI agents to carry cryptographic proof they act for verified humans. Vercel has "human in the loop" authentication live; Okta planning "Human Principal" for API policies. New integrations include Tinder (verified-human badges), Zoom ("Deep Face" iris+live selfie cross-checks), and DocuSign (proof-of-human signatures).
- **SpaceX-Cursor Deal** — SpaceX has right to acquire Cursor for $60B or pay $10B for collaborative compute credits (likely Colossus H100 equivalents). Signals industry trend: top coding labs need to own both model and product.
- **Microsoft Partnership Renegotiation (Apr 2026)** — OpenAI ended exclusive distribution agreement with Microsoft, allowing multi-cloud deployment on AWS, Google Cloud, and Oracle. Microsoft retains nonexclusive IP license through 2032 with capped 20% revenue share through 2030. AGI escape clause replaced with fixed timelines. See [[entities/microsoft]] for Microsoft perspective.

### AWS Bedrock Integration (Apr 2026)

In a landmark multi-cloud expansion, OpenAI launched three offerings on **Amazon Bedrock** (all limited preview, April 28, 2026):

| Offering | Description |
|----------|-------------|
| **OpenAI Models on Bedrock** | Frontier models including GPT-5.5 available through Bedrock APIs with IAM, PrivateLink, guardrails, encryption, CloudTrail |
| **Codex on Bedrock** | Coding agent via Bedrock API; Codex CLI, desktop app, VS Code extension; usage applies to AWS cloud commitments |
| **Bedrock Managed Agents (powered by OpenAI)** | Production-ready agents with persistent context, tool use, multi-step workflows; OpenAI harness + AWS infrastructure |

- **Significance**: Direct consequence of the Microsoft partnership renegotiation — OpenAI now free to sell across any cloud
- Bedrock Managed Agents handles infrastructure, orchestration, and governance, letting teams focus on agent utility
- Each agent has its own identity, logs every action, and runs in the customer's AWS environment

### Economics & IPO Outlook (May 2026)

OpenAI's financial position compared to Anthropic:

| Metric | OpenAI | Anthropic |
|--------|--------|-----------|
| **Annual Revenue** | $25B ARR | $30B ARR |
| **Training Costs** | Forecast to exceed revenue 2026–2028 | Cleaner unit economics (enterprise focus) |
| **IPO Target** | Likely 2027 (delayed due to internal controls) | October 2026 ($400–500B valuation) |
| **Compute Strategy** | "Buy everything" / Consumer scale | Targeted enterprise / Coding focus |

- CFO Sarah Friar reportedly walked back compute commitments from $1.4T to $600B through 2030
- Concern over meeting contract payments if growth doesn't accelerate
- OpenAI's consumer-heavy strategy contrasts with Anthropic's enterprise-first approach


### Privacy & Model Training (May 2026)

OpenAI published guidance on how ChatGPT handles user data in model training:

- **OpenAI Privacy Filter**: Internal tool that identifies and masks personal information in text. Used at multiple stages in the training process, including on public datasets and user conversations with "Improve the model for everyone" enabled. Reported as more effective at removing personal information than any other tool of its kind.
- **Temporary Chat**: Conversations don't appear in history, don't create memories, and aren't used to train models. Retained for 30 days for safety purposes, then deleted.
- **Memory controls**: Users can review, edit, or delete saved memories, or turn memory off entirely. When off, ChatGPT won't save or reference memory from past chats.
- **Data controls**: Users can export their ChatGPT data, delete their account, manage data controls from settings, and submit privacy requests through the privacy request portal.
- **Training data sources**: Mix of publicly available information (freely and openly accessible content), information accessed through partnerships, and information provided/generated by users, contractors, and researchers.
- **Canadian compliance**: Bilingual (English/French) privacy guide published to meet Canadian regulatory requirements for clear language model training documentation.

This reflects OpenAI's shift toward transparency as models become more capable and handle increasingly personal tasks.

### ChatGPT Adoption Metrics (Q1 2026)

In May 2026, OpenAI published consumer ChatGPT usage data for Q1 2026 via OpenAI Signals:

| Metric | Finding |
|--------|---------|
| **Gender parity** | Users with typically feminine names now account for over 50% of usage (among gender-inferred users). Approximate parity was reached in 2025. |
| **Age diversification** | Users 35+ gained share in Q1, though under-35 users still account for the largest share of total messages. |
| **Geographic spread** | Fastest-rising countries by messages-per-capita: Latin America & Caribbean, Asia-Pacific, and Africa. Adoption expanding beyond established markets. |
| **Workplace tasks** | Content creation, health-related documentation, and information retrieval were the fastest-growing use cases. More specialized tasks gaining share over general writing. |
| **Scope note** | Consumer plans only (Free, Go, Plus, Pro). **Excludes Codex** and enterprise/education — understates total workplace and educational usage. |

Source: [How ChatGPT adoption broadened in early 2026](https://openai.com/signals/research/2026q1-update) (OpenAI Signals). See also [[raw/articles/openai.com--signals-research-2026q1-update--45f994a1.md]].



### OpenAI Reorganization — Unifying ChatGPT and Codex (May 2026)

OpenAI announced a major organizational restructuring on May 19, 2026:

| Change | Detail |
|--------|--------|
| **Greg Brockman** | Takes over all products — unifying ChatGPT consumer and Codex developer products under single leadership |
| **Thibault Sottiaux** | Ex-Head of Codex, now leads core product development |
| **Fidji Simo** | On medical leave |
| **Goal** | Structural alignment of consumer (ChatGPT) and developer (Codex) products |

This restructuring signals a strategic shift: **ChatGPT and Codex are no longer separate product lines**. The unification means code generation, chat, and agentic features will be developed as a single platform experience, with shared infrastructure and go-to-market.

### Codex Phone Connection (May 2026)

Codex now supports starting tasks from a **mobile device**, with execution happening on desktop/devbox:

| Feature | Description |
|---------|-------------|
| **Start on phone** | Initiate code generation/agent tasks from mobile |
| **Work on Mac/devbox** | Heavy computation runs on preferred machine |
| **Approve from phone** | Approve commands, answer questions, review diffs |
| **Use case** | Brainstorming and task initiation on-the-go |

Also introduces **Hooks** to Codex — event-driven triggers for automated workflows.

### ChatGPT App Directory & Apps SDK (May 2026)

OpenAI launched an **App Directory** and **Apps SDK** for ChatGPT:

| Feature | Description |
|---------|-------------|
| **App Directory** | Discoverable apps running inside ChatGPT chat UI |
| **Apps SDK** | Build interactive experiences that run in-chat |
| **Renamed** | "Connectors" rebranded to "Apps" |
| **Launch partners** | Spotify, Zillow, Apple Music, DoorDash |
| **Monetization** | Future monetization hinted but not specified |

This represents ChatGPT's evolution from a chat tool to a platform — developers can build interactive experiences that run directly inside the conversational interface.

## May 2026 Product Launches

### GPT-Realtime-2

Next-generation voice AI model. Key features:

- **Speech Reasoning**: Ability to understand and reason with spoken language
- **70+ Language Translation**: Real-time multilingual translation
- **Streaming Transcription**: Real-time text conversion of speech
- Positioned as a new foundation model for voice interaction


### Dreaming V3 — Memory Synthesis (June 2026)

On June 4, 2026, OpenAI launched **Dreaming V3**, a significantly improved memory system that graduates from a supplemental system to a standalone memory architecture for ChatGPT:

- **Evolution**: Saved memories (Apr 2024) → Dreaming V0 + saved memories (Apr 2025) → Dreaming V3 standalone (Jun 2026)
- **Architecture**: Background process that automatically curates and synthesizes memory state from chat history, without requiring explicit "remember" instructions
- **Evaluation**: Three objectives — carry forward useful context, follow preferences/constraints, stay current over time
- **Scale**: Compute-efficient design for hundreds of millions of users and multi-year time horizons
- **Reviewability**: Users can review memory summaries, add/update information, and instruct ChatGPT on what topics to surface
- **Rollout**: Plus and Pro users (US), expanding to additional countries and Free/Go users

See [[concepts/chatgpt-dreaming]] for full details.

### Daybreak — Cybersecurity Initiative (May 2026)

OpenAI launched **Daybreak**, a cybersecurity initiative combining frontier models with Codex as an agentic harness:

- **GPT-5.5-Cyber**: Specialized model with permissive behavior for authorized defensive workflows, paired with stronger verification and account-level controls
- **Trusted Access for Cyber**: Mid-tier access with precise safeguards for verified defensive work (secure code review, vulnerability triage, malware analysis, detection engineering, patch validation)
- **Ecosystem partners**: Cloudflare, CrowdStrike, Palo Alto Networks, and 8 major security vendors
- **Philosophy**: "Safer software, resilient by design" — AI should find and patch vulnerabilities, and software should be resilient to them from the start
- **Positioning**: Direct competitor to Anthropic's Claude Security / Project Glasswing
- **Codex Security**: Agentic harness for security workflows — secure code review, threat modeling, patch validation, dependency risk analysis

### Codex Mobile & ChatGPT Personal Finance (May 2026)

- **Codex in ChatGPT mobile app**: Codex now runs on mobile with a Dispatch-like flow — start on phone, approve on laptop. Enables coding from anywhere.
- **ChatGPT Pro + Plaid integration**: Personal finance features via Plaid connection to 12,000+ financial institutions. Positioned as AI-powered financial management.


### Codex Browser Plugin

OpenAI's coding agent **Codex** released a plugin that runs directly in the browser:

- **Chrome** extension
- **macOS / Windows** desktop integration
- Enables Codex's code generation and editing capabilities from any browser-based development environment

### Multipath Reliable Connection (MRC) — Open Sourced via OCP

OpenAI open-sourced the **MRC (Multipath Reliable Connection)** network protocol through the **Open Compute Project (OCP)**:

- **Co-development partners**: NVIDIA, AMD, Broadcom, Intel, Microsoft
- Distributes GPU traffic across **hundreds of paths**, re-routing in **microseconds** during failures — maintaining lockstep synchronization across thousands of GPUs to prevent training stalls
- **Strategic significance**: Ensures portability across hardware vendors, aiming to weaken NVIDIA's dominance in the networking layer. NVIDIA still wins on hardware, but OpenAI prevents frontier training dependencies from resting on a single supplier
- An industry-wide standardization effort. Related: [[concepts/multipath-reliable-connection]]

### Apple Partnership Dispute (May 2026)

OpenAI is preparing **legal action against Apple** over the ChatGPT-Siri integration deal from 2024 (iOS 18). OpenAI lawyers are working with an outside firm on breach-of-contract claims.

Key developments:
- OpenAI expected the in-Settings ChatGPT subscription signup (Apple taking a cut) "could generate billions of dollars per year" — actual subscriptions "haven't come close"
- An unnamed OpenAI executive: *"We have done everything from a product perspective. They have not, and worse, they haven't even made an honest effort."*
- Apple withheld product details during deal negotiations: *"They basically said, 'OpenAI needs to take a leap of faith and trust us'"*
- No money changed hands — Apple doesn't pay OpenAI, only takes a cut of subscriptions
- Apple now opening Siri to **Google Gemini** (WWDC 2026) and iOS 27 will allow **Anthropic Claude** and other AI models to integrate
- OpenAI was not interested in working with Apple on the new models because "it felt burned by the initial relationship"

> Sources: [9to5Mac](https://9to5mac.com/2026/05/14/openai-preparing-legal-action-against-apple/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-14/openai-apple-partnership-frays-setting-up-possible-legal-fight) (May 14, 2026)



### Erdős Problem — Math Breakthrough (May 2026)

OpenAI's GPT-5.5+ (estimated GPT-5.6) solved the 1946 Erdős plane unit distance problem:

- **Cost**: Under $1,000 / 32 hours of compute
- **Output**: 125-page solution
- **Timothy Gowers** (Fields Medalist): 'First really clear example of AI solving a well-known open math problem'
|- **Implication**: Paradigm shift for test-time reasoning scaling

### Biodefense Action Plan (June 2026)

OpenAI launched a comprehensive biodefense action plan on June 4, 2026, aimed at building AI-powered biological resilience. The plan centers on two key initiatives:

- **GPT-Rosalind** (Apr 2026) — Frontier reasoning model purpose-built for biology, drug discovery, and translational medicine research. See [[concepts/gpt-rosalind]] for full details.
- **Rosalind Biodefense** (May 2026) — Trusted developer program providing advanced AI capabilities for biodefense and pandemic preparedness. See [[concepts/trusted-access-biodefense]] for program details.

**Core thesis**: The same AI capabilities advancing biological science also have implications for biological security. OpenAI's approach is to equip responsible defenders with advanced capabilities while developing safeguards, evidence, and governance for safe deployment.

**Strategic goals**: Enable societies to detect biological threats sooner, develop countermeasures more rapidly, and respond to crises with greater confidence and coordination.

Source: [raw/articles/2026-06-04_openai_openai-biodefense-intelligence-age.md](https://openai.com/index/biodefense-in-the-intelligence-age/)

### ChatGPT Lockdown Mode (June 2026)

OpenAI rolled out **ChatGPT Lockdown Mode** in June 2026, a deterministic security feature designed to prevent the final stage of prompt injection attacks — **data exfiltration** — by limiting outbound network requests that a model can make.

- **Scope**: Rolling out to Free, Go, Plus, Pro, and self-serve ChatGPT Business accounts
- **What it does**: Blocks outbound network requests (e.g., fetching attacker-controlled URLs with stolen data embedded in query parameters), preventing exfiltration of private data accessed during a session
- **What it does NOT do**: Does not prevent prompt injections from appearing in content — injected instructions can still be present in documents, web pages, and other untrusted inputs. Lockdown Mode only blocks the exfiltration vector
- **Simon Willison's analysis**: Directly attacks the "Lethal Trifecta" — the three conditions required for a prompt injection exploit to succeed: (1) access to private data, (2) exposure to untrusted content, and (3) an exfiltration vector. Lockdown Mode cuts off the easiest leg of this triangle
- **Key implication**: Default ChatGPT settings do **not** provide robust protection against data exfiltration. Users must actively enable Lockdown Mode
- **Mechanism**: Uses deterministic mechanisms (network-level restrictions), not AI-evaluated rules, making it a hard security boundary rather than a probabilistic one

Source: [raw/articles/simonwillison.net--2026-jun-5-openai-help-lockdown-mode--2ec234f9.md](https://simonwillison.net/2026/Jun/5/chatgpt-lockdown-mode/)

## Security Architecture

OpenAI's Agents SDK introduces a clear **Harness/Compute separation**:
- **Harness (Control Plane):** Agent loop, model calls, tool routing, handoffs, approvals, tracing, recovery, auth, billing
- **Compute (Execution Plane):** File I/O, commands, dependency installs, port exposure, provider-specific state

This separation mitigates prompt-injection/exfiltration risks and isolates credentials from model-generated code.

## Customer Validation

> *"The updated Agents SDK made it production-viable for us to automate a critical clinical records workflow that previous approaches couldn't handle reliably enough. For us, the difference was not just extracting the right metadata, but correctly understanding the boundaries of each encounter in long, complex records."*
> — **Rachael Burns**, Staff Engineer & AI Tech Lead, Oscar Health

## Related Concepts
- [[concepts/openai-agents-sdk]] — OpenAI's agent development framework
- [[concepts/openai-workspace-agents]] — Codex-powered enterprise shared agents
- [[concepts/gpt-5.5]] — First fully retrained base model since GPT-4.5
- [[concepts/harness-engineering]] — Ryan Lopopolo / Symphony orchestration philosophy
- [[concepts/sandbox]] — AI agent sandbox isolation technologies
- [[concepts/chatgpt-images-2.0]] — GPT Image 2 image generation
- [[concepts/nano-banana-2]] — Google's NB2 image generation competitor

### OpenAI-related articles
- [2026-04-06-openai-anthropic-google-distillation-alliance](2026-04-06-openai-anthropic-google-distillation-alliance.md)
- [2026-04-11-geohot-openai-nothing-without-people](2026-04-11-geohot-openai-nothing-without-people.md)
- [feed.tedium.co--link-15204-17327554-openai-anthropic-ai-tools-expensive-alte--a5938895](feed.tedium.co--link-15204-17327554-openai-anthropic-ai-tools-expensive-alte--a5938895.md)
- [garymarcus.substack.com--p-three-thoughts-on-the-musk-openai--867f8dfb](garymarcus.substack.com--p-three-thoughts-on-the-musk-openai--867f8dfb.md)
- [martinalderson.com--posts-are-openai-and-anthropic-really-losing-money-on-infere--beeb95b5](martinalderson.com--posts-are-openai-and-anthropic-really-losing-money-on-infere--beeb95b5.md)
- [open.substack.com--pub-swyx-p-ainews-openai-launches-gpt-image--6e7fb087](open.substack.com--pub-swyx-p-ainews-openai-launches-gpt-image--6e7fb087.md)
- [openai-agents-sdk-next-evolution-2026-04](openai-agents-sdk-next-evolution-2026-04.md)
- [openai-codex-orchestration-symphony](openai-codex-orchestration-symphony.md)
- [openai-equip-responses-api-computer-environment-2026-03-11](openai-equip-responses-api-computer-environment-2026-03-11.md)
- [openai-harness-engineering-lopopolo](openai-harness-engineering-lopopolo.md)
- [openai-sandbox-agents-api-guide-2026-04](openai-sandbox-agents-api-guide-2026-04.md)
- [openai-unlocking-codex-harness](openai-unlocking-codex-harness.md)
- [openai-unrolling-codex-agent-loop](openai-unrolling-codex-agent-loop.md)
- [simonwillison.net--2026-apr-28-openai-codex--558b4b74](simonwillison.net--2026-apr-28-openai-codex--558b4b74.md)
- [theatlantic.com--technology-2026-04-openai-trial-elon-musk-sam-altman-686984--5e03c7a7](theatlantic.com--technology-2026-04-openai-trial-elon-musk-sam-altman-686984--5e03c7a7.md)
- [thesignal.substack.com--openai-is-cooking-anthropic-sweep-2026-04-26](thesignal.substack.com--openai-is-cooking-anthropic-sweep-2026-04-26.md)
- [trendingtopics.eu--is-this-gpt-6-openai-bets-everything-on-new-model-spud--f17ba49f](trendingtopics.eu--is-this-gpt-6-openai-bets-everything-on-new-model-spud--f17ba49f.md)
- [wheresyoured.at--hatersguide-openai--1e5ccc17](wheresyoured.at--hatersguide-openai--1e5ccc17.md)
- [wheresyoured.at--how-openai-kills-oracle--55ef849c](wheresyoured.at--how-openai-kills-oracle--55ef849c.md)
- [wheresyoured.at--openai-cfo-news--6d149a3a](wheresyoured.at--openai-cfo-news--6d149a3a.md)
- [wheresyoured.at--openai-projects-chatgpt-plus-subscriptions-to-drop-by-80-fro--4a94de93](wheresyoured.at--openai-projects-chatgpt-plus-subscriptions-to-drop-by-80-fro--4a94de93.md)

### TanStack npm Supply Chain Attack — Mini Shai-Hulud (May 2026)

OpenAI disclosed its response to the **Mini Shai-Hulud** supply chain attack targeting the npm ecosystem (May 2026). Hackers published **84 malicious versions** of TanStack packages during a **six-minute window**; a researcher detected the attack within 20 minutes. The malware was designed to steal credentials from infected computers and **self-propagate** to other systems. Two employee corporate devices downloaded a malicious TanStack npm package, resulting in unauthorized access to internal source code repositories and exfiltration of limited credential material including code-signing certificates for iOS, macOS, Windows, and Android products. No customer data or production systems were compromised. All certificates were rotated; macOS users must update apps by June 12, 2026. See [[concepts/openai-tanstack-supply-chain-2026]] for full details.

## Sources
- **OpenAI Agents SDK Blog (2026-04-15)** — [openai.com](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- **OpenAI API Sandbox Docs** — [developers.openai.com](https://developers.openai.com/api/docs/guides/agents/sandboxes)
- **Simon Willison: GPT-5.5 prompting guide (2026-04-25)** — [simonwillison.net](https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/)
- **Alex Banks, The Signal: "OpenAI Is Cooking, The Anthropic Sweep, and SpaceX Courts Cursor" (2026-04-26)** — [substack.com](https://open.substack.com/pub/thesignal/p/openai-is-cooking-the-anthropic-sweep)

## References

- openai-symphony-codex-orchestration
- sign-of-the-future-gpt-55
