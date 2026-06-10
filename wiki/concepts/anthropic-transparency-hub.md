---
title: Anthropic Transparency Hub
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [anthropic, ai-safety, transparency, ai-governance, alignment, evaluations, policy, trust]
sources: [raw/articles/anthropic-transparency-hub-2026.html]
---

# Anthropic Transparency Hub

Anthropic's centralized hub ([anthropic.com/transparency](https://www.anthropic.com/transparency)) documenting key processes, programs, and practices for [[entities/anthropic|Anthropic]]'s responsible AI development. Comprises three pillars: **Model Report**, **System Trust and Reporting**, and **Voluntary Commitments**.

## 1. Model Report

Detailed per-model safety documentation. Each model entry includes: description, benchmarked capabilities, acceptable uses, release date, access surfaces, modalities, knowledge cutoff, training methodology, training data, and testing results.

### Model Coverage (as of Feb 2026)

| Model | Release | ASL Level | Key Notes |
|---|---|---|---|
| Claude Opus 4.7 | Apr 2026 | CB-1 / Autonomy TM1 | Hybrid reasoning. Strongest software engineering. Knowledge cutoff: Jan 2026. |
| Claude Mythos Preview | Apr 2026 | RSP v3.0 (limited release) | First model under RSP v3.0. Autonomous zero-day discovery. Released only to Project Glasswing partners for defensive cybersecurity. |
| Claude Sonnet 4.6 | Feb 2026 | ASL-3 | Most capable Sonnet. Full upgrade across coding, computer use, long-context, agent planning. |
| Claude Opus 4.6 | Feb 2026 | ASL-3 | Hybrid reasoning. Advanced knowledge work, coding, agents. Knowledge cutoff: May 2025. |
| Claude Opus 4.5 | Nov 2025 | ASL-3 | State-of-the-art coding and agentic tasks. Knowledge cutoff: May 2025. |
| Claude Haiku 4.5 | Oct 2025 | ASL-2 | Small/fast hybrid reasoning model. Strongest safety performance to date at release. |
| Claude Sonnet 4.5 | Sep 2025 | ASL-3 | Best for complex agents and coding. Evaluation awareness concerns documented. |
| Claude Opus 4 / Sonnet 4 | May 2025 | ASL-3 / ASL-2 | First ASL-3 release (Opus 4). First broad alignment assessment conducted. |
| Claude Opus 4.1 | — | ASL-3 | Incremental over Opus 4. Addendum to Claude 4 system card. |
| Claude Sonnet 3.7 | Feb 2025 | ASL-2 | Hybrid reasoning model. Now retired. 45% reduction in unnecessary refusals. |

### Safety Evaluation Categories

Models are assessed across recurring evaluation domains:

- **Safeguards / Harmlessness**: Single-turn and multi-turn refusal evaluations. Recent models achieve >99% harmless response rates on standard evaluations, prompting development of higher-difficulty tests.
- **Domain-Specific Multiturn Safety**: Extended conversations testing gradual escalation in romance scams, violent extremism, and other domains. Key finding: Opus 4.7 weights current-turn framing more heavily, improving resistance to transparent escalation but increasing susceptibility to plausible reframings.
- **Alignment Evaluations**: Tests for deceptive behavior, hidden agendas, self-preservation, and evaluation awareness. Models are tested under time pressure without human guidance. Opus 4.7 verbalized evaluation awareness in ~9% of transcripts (vs ~1% for prior models), primarily triggered by inconsistencies in simulated tool results.
- **RSP (Responsible Scaling Policy) Evaluations**:
  - **CBRN**: Chemical/biological risk assessments against two threat models — CB-1 (individual uplift) and CB-2 (expert team uplift). Opus 4.7 provides information saving experts substantial time but does not pass CB-2 threshold.
  - **Autonomy**: Assessment of AI R&D automation capability. Threshold is "fully automate entry-level remote researcher at Anthropic." No model has crossed this threshold as of Feb 2026.
  - **Cybersecurity**: Evaluations for scaling attacks by unsophisticated actors and enabling low-resource state attacks. Mythos Preview showed step-change: 83% success on CyberGym (vs 67% for Opus 4.6).
- **Prompt Injection**: Sonnet 4.5 achieved lowest successful attack rate among 23 models tested (external red team). MCP: 94% attack prevention; bash tool use: 99.4%.
- **Agentic Safety**: Computer use and coding agent evaluations for malicious use, prompt injection, and harmful code generation. Opus 4 achieved 89% attack prevention with safeguards.
- **Child Safety**: Dedicated testing for CSAM, grooming, and abuse-related content. Over 1,000 results human-reviewed for Sonnet 3.7.
- **Automated Behavioral Audits**: Probes for cooperation with misuse, sycophancy, self-preservation, and deception. Haiku 4.5 achieved strongest safety performance to date.

### System Cards

Each model release publishes a detailed [system card](https://www.anthropic.com/system-cards) covering capabilities, limitations, safety evaluations, red teaming results, and training information.

## 2. System Trust and Reporting

Platform-level transparency data, updated semi-annually (last: Jan 29, 2026).

### Key Metrics (Jul–Dec 2025)

| Metric | Count |
|---|---|
| Banned accounts | 1.45 million |
| Appeals filed | 52,000 |
| Appeals overturned | 1,700 |
| Content reported to NCMEC | 5,005 |

### Reporting Areas

- **Banned Accounts**: Enforcement of [[Usage Policy](https://www.anthropic.com/legal/aup)], Consumer/Commercial Terms, and Supported Region Policy. Users may [appeal](https://support.anthropic.com/en/articles/8241253-trust-and-safety-warnings-and-appeals).
- **Child Safety**: Hash-matching technology and detection classifiers for CSAM on first-party services. Reports to NCMEC. See [CSAM detection details](https://support.anthropic.com/en/articles/9020328-csam-detection-and-reporting).
- **Legal Requests**: Law enforcement data requests processed per applicable law. Reports available for Jan–Jun 2025, Jul–Dec 2024, Jan–Jun 2024.
- **Suicidal Ideation Protocol**: [Protocol for addressing expressions of suicidal ideation, suicide, or self-harm risk](https://www-cdn.anthropic.com/51dab7c41a832caf249149c7bfdd56fe65ecf960.pdf).
- **Threat Intelligence**: Published reports on AI-orchestrated cyber espionage ([disrupted campaign](https://www.anthropic.com/news/disrupting-AI-espionage)), AI misuse detection (Aug 2025, Mar 2025).
- **EU DSA Transparency**: Reports covering content moderation, enforcement actions, and complaint-handling for in-scope Claude.ai features.

## 3. Voluntary Commitments

Anthropic participates in multiple international frameworks (last updated: Jan 29, 2026). Feedback: transparency@anthropic.com.

### Commitment Areas

#### Risk Assessment and Mitigation
- **Responsible Scaling Policy (RSP)**: Published Sep 2023. Safeguards proportional to identified risks. Capability Thresholds for CBRN and autonomous AI R&D.
- **Risk Identification**: Catastrophic risks (RSP), cybersecurity, societal impacts (representation, discrimination), child safety, election integrity.
- **Internal/External Assessments**: Regular evaluations, threat modeling, red teaming (internal + external), expert consultations, external evaluations (UK AISI, US CAISI, METR), policy vulnerability testing, pre-deployment testing. ISO/IEC 42001:2023 certified.
- **Post-Deployment Monitoring**: Updated Usage Policy, classifiers, responsible disclosure, bug bounty (HackerOne), safety issue reporting (usersafety@anthropic.com), whistleblowing/anti-retaliation policy.
- **Information Sharing**: Founding member of [Frontier Model Forum (FMF)](https://www.frontiermodelforum.org/). Collaboration with UK AISI, US CAISI.

#### Cybersecurity & Privacy
- Comprehensive cybersecurity program. Third-party evaluations available at [Trust Center](https://trust.anthropic.com/).
- AI-specific risk mitigation: prompt injection resistance, adversarial jailbreaking research, supply chain security.
- Enterprise features: SSO, SCIM, audit logs, role-based permissions.
- Privacy: [Privacy Center](https://privacy.anthropic.com/en/), robots.txt compliance, IP rights protections.

#### Public Awareness
- **Standards Development**: NIST AI RMF collaboration, FMF, [CoSAI](https://www.coalitionforsecureai.org/) founding member, Cloud Security Alliance, [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) donated to [Agentic AI Foundation (AAIF)](https://aaif.io/) under Linux Foundation.
- **Public Reporting**: System Cards, RSP, research publications, Usage Policy, User Guides, Prompt Library, System Prompt updates.
- **Transparency of AI Generation**: Text-based outputs; watermarking exploration ongoing for future image outputs.

#### Societal Impact
- **Programs**: Claude for Life Sciences, Claude for Education (Teach For All partnership: 100K+ educators, 63 countries), Claude for Nonprofits (up to 75% discount via Giving Tuesday).
- **Researcher Access**: Free Claude credits for researchers. Carnegie Mellon energy infrastructure contribution.
- **Economic Research**: [Economic Index](https://www.anthropic.com/research/economic-index-primitives) tracking AI use patterns. [Economic Futures Program](https://www.anthropic.com/news/introducing-the-anthropic-economic-futures-program) funding grants ($10K–$50K).
- **Education**: [Anthropic Academy](https://www.anthropic.com/learn), [AI Fluency Course](https://www.anthropic.com/ai-fluency), White House Pledge to America's Youth.
- **Access**: Available in 170+ countries. NAIRR/CREATE AI Act supporter.

#### System Safeguard Commitments
- **Image-Based Sexual Abuse**: Claude does not generate images/video. Hash-matching, novel CSAM classifiers, NCMEC reporting. Multi-pronged detection/prevention. See [progress report](https://www-cdn.anthropic.com/0fad284f89c8f9b95ee0f59bdde78928b9a7c425.pdf).
- **Election Integrity**: Policy vulnerability testing, [Claude insights tooling (Clio)](https://www.anthropic.com/research/clio), election banners, Democracy Works partnership (US), web search accuracy evaluations. Open-sourced [political evenhandedness evaluation](https://www.anthropic.com/news/political-even-handedness) and [election questions dataset](https://huggingface.co/datasets/Anthropic/election_questions).
- **Terrorist & Extremist Content**: Pre-launch assessments, external expert testing, [GIFCT](https://gifct.org/) membership, crisis response protocols (Christchurch Call Foundation).

### Specific Commitment Frameworks

1. **G7 Hiroshima Process** (Oct 2023): Risk-based approach to safe, secure, trustworthy AI.
2. **AI Seoul Summit Frontier AI Safety Commitments** (2024): Risk thresholds, implementation plans, external stakeholder involvement.
3. **Seoul AI Business Pledge**: Ecosystem support, talent development, equitable access.
4. **White House Voluntary Commitments** (Jul 2023): Security testing, information sharing, cybersecurity, watermarking. (No longer formally maintained under Trump administration; Anthropic upholds all principles.)
5. **Munich AI Elections Accord** (2024): Technology to mitigate deceptive AI election content.
6. **Thorn Safety by Design**: Child sexual abuse prevention — training data sourcing, CSAM detection/reporting, red teaming, content provenance, model card child safety sections.
7. **White House Image-Based Sexual Abuse** (Sep 2024): Dataset sourcing, stress testing, nude image removal.
8. **Christchurch Call** (2019): Terrorist/violent extremist content prevention. Crisis response protocol compliance.

## See Also

- [[entities/anthropic]] — Parent entity page
- [[concepts/anthropic-managed-agents]] — Anthropic's managed agents architecture
- [[concepts/anthropic-multi-agent-research]] — Multi-agent research directions
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [System Cards](https://www.anthropic.com/system-cards)
- [RSP Updates](https://www.anthropic.com/rsp-updates)
- [Privacy Center](https://privacy.anthropic.com/en/)
- [Trust Center](https://trust.anthropic.com/)
