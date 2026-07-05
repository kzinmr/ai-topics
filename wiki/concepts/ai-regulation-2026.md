---
title: "AI Regulation (2026)"
type: concept
created: 2026-04-30
updated: 2026-06-15
tags:
  - concept
  - regulation
  - safety
  - security
  - policy
  - governance
status: complete
sources:
  - url: "https://www.wsgr.com/en/insights/2026-year-in-preview-ai-regulatory-developments-for-companies-to-watch-out-for.html"
    title: "2026 Year in Preview: AI Regulatory Developments (Wilson Sonsini)"
  - url: "https://www.multistate.ai/artificial-intelligence-ai-legislation"
    title: "State AI Legislation Tracker 2026: All 50 States"
  - url: "https://www.osborneclarke.com/insights/regulatory-outlook-january-2026-artificial-intelligence"
    title: "UK Regulatory Outlook January 2026 - AI"
  - url: "https://www.blockchain-council.org/news/ai-regulation-2026-us-federal-preempt-california"
    title: "AI Regulation 2026: US Federal vs California"
  - url: "https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/"
    title: "California SB 53: Frontier AI Safety Legislation"
  - url: "https://www.lexology.com/library/detail.aspx?g=a917b0b5-6d38-4aab-aee2-ee7f584f36c8"
    title: "New York RAISE Act Gets a California Makeover"
  - url: "https://www.ncsl.org/financial-services/artificial-intelligence-legislation-database"
    title: "NCSL AI Legislation Database"
  - raw/articles/2026-06-10_dario-amodei_policy-on-the-ai-exponential.md
  - raw/articles/apple.com--newsroom-2026-06-due-to-dma-siri-ai-delayed-in-eu-for-ios-27--dec9fef2.md
  - raw/newsletters/2026-06-14-welcome-to-the-agi-era-of-ai-governance.md
---

# AI Regulation (2026)

> 2026 is a watershed year for AI regulation. Over 1,500 state bills introduced across the US, California's landmark frontier AI safety law in effect, the EU AI Act nearing implementation, and a new federal administration reshaping the national approach. The regulatory patchwork is both the biggest risk factor and most significant compliance challenge for AI companies.

## United States: State-Level Surge

### Scale
- **2026 (so far):** 1,561 AI-related bills introduced across 45 states (as of March 2026)
- **2025:** ~1,200 bills introduced, ~100 enacted
- **2024:** 635 bills introduced, 99 enacted
- **2023:** <200 bills introduced

The pace is accelerating dramatically. The most active areas: generative AI regulation, algorithmic accountability, AI in hiring/employment, and expanded protections against nonconsensual explicit deepfakes.

### California: The Leader

#### SB 53 — Transparency in Frontier Artificial Intelligence Act (TFAIA)
- **Status:** Signed September 2025, effective January 1, 2026
- **Scope:** Large frontier AI developers
- **Key requirements:**
  - Publish a "frontier AI framework" describing how safety standards are incorporated
  - Report catastrophic safety incidents to the Office of Emergency Services
  - Disclosure of risk assessments and third-party evaluator involvement
  - System card / model card publication for new or substantially modified models
- **Additional provisions:**
  - CalCompute consortium: public computing cluster for safe, ethical AI research
  - Whistleblower protections for AI safety researchers
- **Framework:** "Trust but verify" — companies self-certify frameworks, subject to incident reporting requirements

#### California AI Transparency Act (AB 1064)
- Requires generative AI systems with >1M monthly users to provide free detection tools
- Labeling and watermarking requirements for AI-generated content

### New York: RAISE Act
- **Status:** Signed December 2025, amended early 2026
- **Key features:**
  - "Frontier AI framework" requirement (aligned with CA TFAIA terminology)
  - Quarterly catastrophic risk assessment submissions to regulator
  - Model card / transparency reports for new deployments
  - Ownership disclosure requirements
  - Incident response obligations
- **Key difference from CA:** Added incident response, ownership disclosures, and penalty structures not present in TFAIA

### Other Notable State Activity
- **Colorado:** First state AI law (SB 24-205) — AI in high-risk decision-making
- **Texas, Illinois, Minnesota:** Active AI bills in 2025–2026 sessions
- **22 states:** Enacted nonconsensual explicit deepfake laws

### Federal Landscape
- **119th Congress:** ~150+ AI bills introduced, none passed in 118th Congress
- **Trump Administration:** New AI Executive Order in 2025, shifting federal approach toward deregulation
- **Federal preemption debate:** Ongoing tension between states and federal government — will federal law override California and New York's frameworks?
- **No comprehensive federal AI legislation** passed as of April 2026

## European Union

### EU AI Act
- **Status:** Adopted 2024, phased implementation through 2027
- **Key milestones:**
  - August 2026: High-risk AI system rules originally planned for applicability
  - November 2025: EC proposed "Digital Omnibus" amendments extending HRAI applicability to December 2027
  - 2026: Guidance development on high-risk AI, research exemptions, and interplay with GDPR
- **Scope:** Risk-based framework (unacceptable, high, limited, minimal risk categories)
- **Enforcement:** EU AI Office, national competent authorities, fines up to 7% of global annual turnover

### Digital Omnibus Simplification
- November 2025 EC proposal: targeted changes to EU AI Act
- Delayed high-risk AI rules applicability
- New guidance on research exemptions (Articles 2(6) and 2(8))
- Joint guidance with EDPB on AI + data protection interplay

### DMA × AI Assistants: Apple Siri AI Case Study (June 2026)

Apple's June 11, 2026 announcement that Siri AI would be delayed for iOS 27/iPadOS 27 in the EU represents the first major test of how the EU Digital Markets Act (DMA) interacts with AI platform capabilities. Unlike the EU AI Act (which governs high-risk AI systems directly), the DMA's provisions on gatekeeper platform obligations are being interpreted by the European Commission to require AI systems to have unrestricted device access and third-party app control rights as a competition remedy.

**Key facts**:
- Apple proposed a **Trusted System Agent** intermediary solution; the European Commission rejected it
- EU regulators demand that any AI system on Apple devices have "nearly unlimited access" to user data and the ability to "act autonomously without ongoing user visibility"
- Apple cites security research showing AI systems can be hijacked to steal sensitive data
- The dispute only affects iOS/iPadOS/watchOS; macOS and visionOS Siri AI will be available in the EU
- No resolution timeline exists

**Regulatory implications**: This case highlights a gap in current regulatory frameworks: the EU AI Act governs AI safety directly, but the DMA's platform competition provisions create conflicting requirements with AI security/privacy. The outcome will set precedent for how competition regulation and AI safety regulation interact in the EU.

Source: [[raw/articles/apple.com--newsroom-2026-06-due-to-dma-siri-ai-delayed-in-eu-for-ios-27--dec9fef2.md]]

## United Kingdom

- **No dedicated AI bill** expected in 2026
- Government focusing on "AI Growth Zones" and "AI Growth Labs" (regulatory sandboxes)
- AI Minister Kanishka Narayan: existing laws (data protection, competition, equality, online safety) already apply
- Copyright and AI: ongoing debate on training data licensing

### Anthropic / Amodei's Proposed Framework (June 2026)

In "Policy on the AI Exponential" (June 10, 2026), Dario Amodei articulated Anthropic's most detailed regulatory proposal to date. The essay marks a definitive shift from the **transparency era** (2023–2025, where Anthropic supported SB 53, RAISE Act, and SB 315 disclosure requirements) to advocating **binding regulation** — modeled on the Federal Aviation Administration (FAA) for frontier AI. Anthropic released a **legislative proposal on frontier model testing** and a **policy framework for job displacement** alongside the essay, with substantial financial backing pledged.

**Key elements of the proposed framework:**

- **Shift from transparency to binding regulation** — FAA-model for frontier AI: mandatory technical testing and auditing before deployment, with government power to block or reverse unsafe model releases
- **Mandatory third-party testing** for models above a compute threshold in four specific risk areas: cybersecurity, biological weapons, loss of control, and automated R&D (which could accelerate the other three risks)
- **Government power to block/deter unsafe model deployment** — scoped to the four specific risk domains, with anti-arbitrariness protections against political favoritism or capricious decisions
- **Private authorized evaluators or government agency** — a "regulatory markets" approach: evaluation by either a government agency (FAA model) or private organizations authorized and inspected by the government to evaluate models against defined standards
- **Strong security standards** for model weights, regular red teaming and penetration testing, collaboration with government to defend against major threat actors
- **Safety incident reporting** — prompt mandatory reporting of safety incidents in the four critical areas

**Regulatory trajectory**: Amodei acknowledged that if risks escalate to nuclear-weapon level, more aggressive measures would be necessary — but cautioned against getting ahead of the curve, arguing policy should match today's emerging risks while laying foundations for faster escalation later. The essay frames this as the transition from transparency-era (2023–2025) to binding regulation era (2026+).

**Bipartisan framing**: Amodei positions these proposals as having "common-sense appeal across the political spectrum," rejecting the framing that AI's problem is "better marketing."

**Legislative action**: Alongside the essay, Anthropic released a concrete legislative proposal on frontier model testing and a job displacement policy framework, signaling intent to move beyond thought leadership into active policy advocacy with financial backing.

### Nathan Lambert: The "AGI Governance Era" Framework (June 2026)

In "Welcome to the AGI Era of AI Governance" (June 14, 2026), Nathan Lambert advanced a distinct framing of the June 12 Fable 5 export control event — not as a discrete policy incident, but as the **transition trigger from the "ChatGPT governance era" (2023–2026) to the "AGI governance era" (2026+)**. This analysis complements Amodei's transparency-to-binding-regulation narrative with a more geopolitically grounded perspective.

**Core argument**: Lambert argues the Friday night call from the government to Anthropic (instructing them to block model access for foreign nationals and overseas users) represents a qualitative shift in how governments perceive AI. The government has **internalized that it is already in the AGI era** and has moved beyond the ChatGPT-era governance model. Lambert warns this is not an isolated incident but the "starting gun" for AGI-era regulation.

**Key claims**:
- **Export bans have permanent consequences**: Model weight export prohibitions are not reversible policy tools; they create persistent geopolitical divisions and supply chain fragmentation
- **Anthropic's fear campaign accelerated regulation**: Lambert argues that Anthropic's consistent use of nuclear-weapon metaphors and catastrophic-risk framing created the political conditions for aggressive government action — the regulation Anthropic helped shape through its own narratives is now governing Anthropic itself
- **Open-source advocates should be alarmed**: The export control precedent can easily be extended to open-weight model distribution, which Lambert characterizes as a structural threat to open-source AI
- **This is just the beginning**: The Friday night call represents the first instance of governments treating frontier AI as an AGI-level concern, setting precedent for more aggressive interventions across jurisdictions

**Contrast with Amodei's framework**: Where Amodei frames the transition as voluntary transparency → mandatory testing (a regulatory locus shift), Lambert frames it as ChatGPT governance → AGI governance (an epochal shift in government perception). Both agree on the directionality but Lambert emphasizes the **geopolitical trigger** (export controls) over the **institutional mechanism** (FAA-style testing agency). Lambert's framing also highlights the **unintended consequences** of Anthropic's own advocacy — a dimension absent from Amodei's self-narrative.

Source: [[raw/newsletters/2026-06-14-welcome-to-the-agi-era-of-ai-governance]]

## Implications for Developers and Enterprises

### Operational Requirements
1. **Frontier AI frameworks** — model governance documentation, risk assessments, red-teaming records
2. **Transparency-by-design** — labeling, watermarking, detection tooling
3. **Incident reporting** — critical safety incident protocols
4. **Model cards** — standard publication for new and substantially modified models
5. **Cross-state compliance** — programs must map requirements by jurisdiction

### Key Risk Areas
- **Content labeling:** Deepfake and AI detection tools mandatory in CA for large platforms
- **Employment AI:** Hiring algorithm audits required in multiple states
- **Healthcare AI:** Growing state-level regulation of AI in clinical settings
- **Child safety:** AI companion safeguards, self-harm detection requirements
- **Copyright:** Training data provenance and licensing uncertainty

### Open Questions
- Will federal legislation preempt state laws, or will the patchwork persist?
- How will enforcement capacity scale with the rapid pace of legislation?
- Will alignment between CA TFAIA and NY RAISE Act templates create de facto national standards?
- How will AI regulation interact with emerging agentic AI capabilities (autonomous agents making decisions)?

## Related Pages
- [[concepts/security-and-governance/agent-governance]] — Enterprise AI agent governance frameworks
- [[concepts/ai-agent-traps]] — Safety and failure modes for AI agents
- [[concepts/ai-autonomy-debate]] — Debate around AI autonomy levels
- [[concepts/security-and-governance/ai-safety]] — AI safety and alignment
- [[entities/_index]]
