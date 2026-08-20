---
title: "Decagon"
type: entity
created: 2026-05-08
updated: 2026-08-19
tags:
  - company
  - ai-agents
  - speech
aliases: ["Decagon AI"]
sources:
  - https://decagon.ai/
  - https://decagon.ai/about
  - raw/articles/2026-08-13_decagon_browser-actions.md
  - raw/articles/2026-08-19_decagon_teaching-flow-matching-tts-with-rl.md
---

# Decagon

Decagon is an AI-powered customer support platform that builds, optimizes, and scales AI agents for enterprises. Its generative AI agents handle complex inquiries end-to-end — answering questions, processing refunds, canceling subscriptions, and more — across chat, email, and voice channels.

| | |
|---|---|
| **Type** | AI Platform / Enterprise SaaS |
| **Founded** | 2023 (San Francisco, CA) |
| **Leadership** | [[entities/jesse-zhang]] (Co-founder & CEO), Ashwin Sreenivas (Co-founder & President) |
| **Key Products** | Decagon AI Agents (voice, chat, email), Decagon Duet, Agent Workbench, Watchtower (QA), Proactive Agents |
| **Website** | [decagon.ai](https://decagon.ai) |
| **Tech Blog** | [decagon.ai/blog](https://decagon.ai/blog) |

## Key Facts

- Founded in August 2023 by Jesse Zhang (ex-Google, Citadel, Harvard CS) and Ashwin Sreenivas (ex-Palantir, Stanford)
- Valued at $4.5 billion as of 2026; raised $481M+ total including $250M commitment
- Serves over 10 million customers with 80% deflection rate and 93% quality score
- Named a leader in conversational AI support across retail, travel, fintech, health, and telecom

## Products & Technology

Decagon's platform includes AI agents defined in natural language via Agent Operating Procedures (AOPs), Agent Workbench for debugging, Watchtower for QA monitoring, Proactive Agents for outbound engagement, and Duet for assisted agent building. Supports voice 2.0 with real-time streaming, simulations for testing, and full auditability.



### Agent Engineering at Decagon

Decagon employs Applied Software Engineers (ASWEs) focused on agent engineering — building at the frontier of AI agent capabilities:

- **Technical scope**: Prompt-to-agents wiring, knowledge bases, tools, multi-channel communication, latency optimization (time-to-first-token benchmarking), reliability infrastructure (retries, failover, monitoring)
- **Product impact**: Treats customer bespoke requirements as platform improvements (e.g., Block/Square/Cash App voice interaction improvements shipped as product features for all customers)
- **Customer outcomes**: ASWEs directly influence deals, revenue, and product direction
- **Cross-functional**: Works with orchestration, research, infrastructure, product, and APM teams

Authored by Kathryn Zhou (May 11, 2026).


## Duet Autopilot — Redefining Forward Deployment (June 2026)

Decagon launched **Duet Autopilot**, a paradigm shift in how AI customer support agents are deployed and improved. Rather than the traditional "forward deployment" model (consultants on-site configuring agents), Duet Autopilot automates the full deployment lifecycle.

**Key components:**
- **A/B Testing**: Automated experimentation — run multiple agent configurations simultaneously, measure performance, and auto-select winners
- **Simulation**: Test agents against synthetic customer scenarios before going live, reducing deployment risk
- **Watchtower QA**: Continuous quality monitoring post-deployment, with automatic detection of regression and drift
- **Agent Development Kit**: Tools for engineering teams to build, test, and iterate on agent behavior programmatically

**Significance**: Decagon's approach challenges the consulting-heavy enterprise AI deployment model. By automating deployment and improvement, they aim to make AI customer support self-service rather than professional-services-dependent.

Source: [How Decagon is redefining forward deployment — Decagon Blog](https://decagon.ai/blog/how-decagon-is-redefining-forward-deployment)

## Anti-FDE Philosophy: Product-Driven Deployment (Aug 2026)

Jesse Zhang's "To FDE, or not to FDE?" (2026-08-11, 1104 bookmarks) articulates Decagon's explicit rejection of the FDE-heavy model that Palantir pioneered and Anthropic/OpenAI are now adopting:

- **Two-thirds of deployment work now autonomous through Duet** — configuration, iteration, and tuning that used to require a human in the loop
- **Days to launch first AOP** — even for big banks, airlines, telcos
- **Product-driven bet**: Customer service is high-volume, repeatable, decomposable — the FDE model's bespoke approach is structurally mismatched
- **Key tradeoff**: Refused to hack solutions in the field when faster; turned escalations into requirements instead of patches
- **Core insight**: FDEs should be a discovery tool that feeds product, not a permanent business model. "FDEs eat pain and excrete product. If yours are eating pain and excreting more pain, you don't have an FDE team. You have a services business."

Source: [To FDE, or not to FDE? — @thejessezhang](https://x.com/thejessezhang/status/2087198484093149421)

## Browser Actions — Computer Use for CX Agents (August 2026)

Decagon launched **Browser Actions**, a computer-use capability that lets AI agents log into, navigate, and complete tasks inside web-based systems that lack traditional API integrations — internal claims systems, partner portals, vendor dashboards, and legacy on-prem tools.

**Key capabilities:**
- **Direct page interaction**: Reads on-screen content, clicks elements, fills fields, waits for page loads — operates the same UI a human would use
- **No integration build required**: Uses the existing website/application login, not a backend API connection
- **Security**: Runs inside SOC-2/GDPR/HIPAA/CCPA-compliant sandboxed containers with full audit logging of every click, field entry, and page transition
- **Failure handling**: If an expected field is missing or a screen fails to load, the agent stops and escalates at the exact failure step

**Use case example**: A banking customer reporting a lost/stolen account — the agent navigates the multi-step help center flow (routing depends on customer answers), fills forms, submits the report end-to-end without the customer leaving the chat.

**Significance**: Browser Actions extends Decagon's agent capabilities beyond API-connected systems into the long tail of enterprise software that only exposes a web UI — addressing the "last mile" of enterprise automation where legacy systems have no API.

Source: [Introducing Browser Actions — Decagon Blog](https://decagon.ai/blog/browser-actions) (Bihan Jiang, Director of Product, Aug 5, 2026)

## Flow-DPO / Flow-GRPO — Post-Training Flow-Matching TTS with RL (Aug 2026)

Decagon published the internals of its work on **post-training modern flow-matching text-to-speech (TTS) models with preference- and group-based reinforcement learning**, introducing two methods it calls **Flow-DPO** and **Flow-GRPO**. The motivating problem: modern TTS sounds natural on average, but "average quality hides the failures that matter most" — a rushed sentence, misplaced pause, or flattened intonation dominates the impression of an otherwise convincing interaction. The post-training goal is not a better mean sample but a **tighter distribution**: fewer tail failures, no leakage onto ordinary prompts, and no loss of intelligibility, speaker identity, or naturalness.

**The core mismatch:** [[entities/vibevoice|flow-matching]] models generate speech by learning how to continuously transform noise into audio — after the initial noise is chosen, generation follows a *deterministic* trajectory (a learned velocity field), not a sequence of distribution-sampled actions with explicit log-probabilities. An autoregressive backbone conditions a flow head that emits the next latent audio patch as a deterministic update. That breaks the machinery standard preference/RL methods assume:
- **DPO** needs a policy-vs-reference log-probability gain — a flow model exposes no exact waveform likelihood.
- **GRPO** needs old and current action log-probabilities — a deterministic trajectory provides none.

**Flow-DPO (preference learning without exact likelihoods):** a flow model can't produce exact waveform likelihoods, but it *can* measure how well its velocity field fits a supplied audio trajectory. Decagon replaces the unavailable policy-vs-reference log-probability gain with a **negative relative flow loss** (built from the standard flow-matching loss, sampled flow times, and a strength coefficient), reusing the same flow times and noise for policy and reference to reduce variance. Winner-side flow and stop-head anchors preserve reconstruction and termination. The flow loss is *not* an exact likelihood — it only provides the relative signal DPO needs to separate preferred from rejected trajectories. Dataset quality is decisive: an early Flow-DPO run for a `[cough]` control tag failed because many "rejected" samples still contained real coughs, so the preference signal came from voice/intelligibility rather than the event; rebuilding around **same-prompt contrasts that isolate the target event** and filtering preferred samples for intelligibility/speaker consistency/artifacts fixed it.

**Flow-GRPO:** applies group-relative policy optimization to the flow model by substituting the missing action log-probabilities with the flow-fit / relative-loss surrogate, keeping the group structure for variance reduction.

**Significance:** This is one of the first concrete recipes for bringing DPO/GRPO-style preference and group RL to *flow*-based (diffusion-like) generative models where the likelihood is not directly available — a relevant technique for any voice/[[entities/vibevoice|TTS]] stack built on flow matching rather than autoregressive token sampling. It also echoes Decagon's broader post-training focus on cutting tail failures in production voice rather than chasing average-case quality.

Source: [Teaching flow-matching text-to-speech models with RL — Decagon Blog](https://decagon.ai/blog/teaching-flow-matching-tts-with-rl) (Aug 2026)

## Related

- [[entities/jesse-zhang]] — Co-founder & CEO
- [[entities/palantir]] — Origin of the FDE model; co-founder Ashwin Sreenivas is ex-Palantir
- [[concepts/forward-deployed-engineering]] — The FDE paradigm Decagon explicitly challenges
- [[entities/modal-labs]] — infrastructure partner for real-time voice AI deployment
- [[entities/openai]] — uses GPT-family models alongside proprietary fine-tuned models
- [[entities/glean]] — fellow enterprise AI platform, focused on search vs. customer support
