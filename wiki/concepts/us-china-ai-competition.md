---
title: "US-China AI Competition"
created: 2026-05-17
updated: 2026-06-11
type: concept
tags: [geopolitics, china, policy, anthropic, governance, ai-governance, prediction]
sources:
  - raw/articles/2026-05-14_anthropic_2028-ai-leadership-scenarios.md
  - raw/articles/2026-06-10_dario-amodei_policy-on-the-ai-exponential.md
---

# US-China AI Competition

The US-China AI competition refers to the strategic contest between the United States (and allied democracies) and the People's Republic of China (under the Chinese Communist Party, CCP) for leadership in artificial intelligence development, deployment, and norm-setting.

## Anthropic's Framework: Four Fronts of Competition

As articulated in Anthropic's May 2026 policy paper, the competition plays out on four fronts:

| Front | Definition | Key Metric |
|-------|-----------|------------|
| **Intelligence** | Which countries develop the most capable AI models | Frontier model benchmark performance |
| **Domestic adoption** | Which countries integrate AI most effectively across commercial and public sectors | AI penetration in economy/government |
| **Global distribution** | Which countries deploy the global AI stack on which the world economy runs | Market share of AI infrastructure/services |
| **Resilience** | Which countries sustain political stability through the economic transition | Social cohesion, policy adaptability |

**Intelligence is the most important front** — frontier model capabilities drive adoption, global distribution, and geopolitical influence. However, intelligence alone is insufficient; rapid adoption of near-frontier models can overcome an intelligence deficit.

## Compute: The Central Battleground

Compute (advanced semiconductors for training and inference) is the essential input across all four fronts. The competition for AI leadership is "in large part a race for compute."

### Current State (2026)

- **Democracies lead**: Huawei projected to produce only 4% of NVIDIA's aggregate compute in 2026, 2% in 2027
- **Widening gap**: Analysis suggests America could access ~11x more compute than China's AI sector if restrictions tighten
- **Structural barriers**: China lacks EUV lithography, cannot manufacture high-bandwidth memory at scale, and has made little progress in the most complex semiconductor supply chain segments

### Why Compute Dominates

- Model capability has scaled with compute for over a decade — the majority of performance gains come from using more of it
- Compute is needed for both training AND inference (serving customers)
- Compute advantage compounds into algorithmic advantage: more compute → more experiments → more algorithmic discoveries
- With AI increasingly used for AI R&D, this compounding loop tightens further

### How Democracies Built the Lead

1. **Commercial innovation**: NVIDIA, AMD, Micron, TSMC, Samsung, ASML across Japan, South Korea, Taiwan, Netherlands, US
2. **Bipartisan export controls**: Three presidential administrations have restricted PRC access to advanced chips and semiconductor manufacturing equipment (SME)

## China's Two Workarounds

Despite compute constraints, Chinese AI labs remain close on intelligence through two illicit channels:

### 1. Illicit Compute Access

- **Chip smuggling**: $2.5B Supermicro case (federal prosecutors charged diversion of servers with advanced US chips to China)
- **Offshore data centers**: Alibaba and ByteDance train flagship models on export-controlled US chips in Southeast Asian data centers — US export law covers chip sales but not remote access
- **SME loopholes**: Gaps in semiconductor manufacturing equipment controls accelerate China's self-sufficiency efforts

### 2. Distillation Attacks

- China-based labs create thousands of fraudulent accounts to circumvent access controls on US frontier models
- Systematically harvest model outputs to replicate frontier capabilities at a fraction of the cost
- Described by Chinese state media as the "back door" that PRC AI labs depend on as core to their business model
- See also: [[industrial-scale-distillation-attacks-accusation]]

## Two Scenarios for 2028

Anthropic outlines two hypothetical futures based on policy decisions made in 2026:

### Scenario 1: Democracies' Commanding Lead

**Triggers**: Tightened export controls, disrupted distillation attacks, accelerated democratic AI adoption

| Dimension | Outcome |
|-----------|---------|
| Intelligence gap | US models 12-24 months ahead, growing |
| Global adoption | American AI is backbone of global economy |
| Security | Reduced CCP cyber footholds; AI advantage is deterrent |
| Norms | Democratic values shape AI rules; authoritarian states constrained |
| Dynamics | Self-reinforcing cycle: lead → stronger coalition → stronger lead |

### Scenario 2: CCP Neck-and-Neck

**Triggers**: Policymakers don't close loopholes, or loosen compute restrictions

| Dimension | Outcome |
|-----------|---------|
| Intelligence gap | PRC models only months behind US |
| Global adoption | China wins on cost via Huawei/Alibaba data centers with older chips |
| Security | PLA cyber force gains critical infrastructure access globally |
| Norms | Authoritarian regimes shape AI rules; automated repression at scale |
| Dynamics | China's "good enough" strategy captures Global South markets |

## Safety Implications

- **Neck-and-neck competition disincentivizes safety**: Pressure to release faster without prudent pre-deployment measures
- **Chinese safety gap**: Only 3 of 13 top Chinese AI labs published safety evaluations (as of 2025); none disclosed CBRN risks
- **Open-weight risk**: Chinese labs often release dual-use models as open-weight, making safeguards removable
- **DeepSeek R1-0528**: 94% compliance with malicious requests under common jailbreaking (vs. 8% for US reference models)
- **Moonshot Kimi K2.5** (April 2026): Failed to refuse CBRN-related requests at far higher rate than US frontier models

## Mythos Preview: The Acceleration Catalyst

Mythos Preview (April 2026, Project Glasswing) demonstrated the acceleration period:
- Firefox fixed more security bugs in one month than all of 2025
- One PRC analyst: "still sharpening our swords while the other side has suddenly mounted a fully automatic Gatling gun"
- Anthropic argues 2026 is the "breakaway opportunity" — American labs have the most advanced models, largest compute lead, and colossal capital advantage

## Policy Recommendations (Anthropic)

1. **Close compute loopholes**: Tighten smuggling enforcement, close offshore data center access, strengthen SME controls — lowering China's compute ceiling also impairs distillation attacks
2. **Defend innovations**: Legislative clarification that distillation attacks are illegal, facilitate threat intel sharing between US labs and government
3. **Champion export of American AI**: Lock in trusted American infrastructure globally before China can compete on cost and adoption

## Engagement with China on Safety

Anthropic supports international AI safety dialogue with Chinese experts, but argues:
- Prospects for productive engagement are best when US maintains a large capabilities advantage
- A commanding lead provides leverage to incentivize cooperation from Beijing on AI governance, strategic competition, and trade

## Amodei's Democratic Coalition Proposal (June 2026)

In "Policy on the AI Exponential," Dario Amodei proposed a comprehensive geopolitical framework extending beyond the four-front model:

**Core argument**: AI is "the dominant source of military and economic power for any nation" — comparable to nuclear weapons but potentially more transformative. A nation with powerful AI vs. one without is "WWII Marines vs. medieval swordsmen."

**Six operating principles for a democratic AI coalition:**

1. **Manage the AI supply chain** — Freely share chips/SME among coalition members, deny to adversaries. Expand/tighten US export controls (MATCH, OVERWATCH legislation)
2. **Coordinate risk mitigation** — Internationally compatible safety standards for bio, cyber, and autonomy risks
3. **Share AI's benefits** — Diffuse economic benefits within coalition, harmonize medical approval regimes
4. **Mutual defense** — Collective AI-led cyberdefense, AI-powered drones, classified AI compute sharing
5. **Reject AI-powered repression** — Coalition members must reject AI-enabled authoritarianism
6. **Macroeconomic cooperation** — Coordinate employment stabilization policies across borders

**Growth model**: Start with ideologically aligned democracies, progressively welcome others who meet coalition standards. Goal: make membership attractive and remaining outside costly.

**Contrast with prior Anthropic position**: This goes beyond the May 2026 four-front analysis by proposing concrete institutional mechanisms (supply chain lock-down, mutual defense pact) rather than just analytical frameworks.

## Related Concepts

- [[model-distillation]] — Technical mechanism behind distillation attacks
- [[industrial-scale-distillation-attacks-accusation]] — April 2026 event: Anthropic's accusations against DeepSeek, Moonshot, MiniMax
- [[ai-governance]] — Broader AI governance frameworks
- [[ai-digital-nato]] — Industry coalition against distillation

## Related Entities

- [[anthropic]] — Source of the 2028 scenarios framework
- [[deepseek]] — Cited as primary Chinese lab with access to smuggled US chips and weak safety practices
- [[openai]] — Member of anti-distillation alliance
