---
type: research_note
date: 2026-07-29
sources:
  - https://open.substack.com/pub/swyx/p/ainews-fearing-rsi-openai-anthropic
  - https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/
  - raw/newsletters/2026-07-29-ainews-fearing-rsi-openai-anthropic-gdm-meta-thinky-cosign-letter-to-pace-ai-dev.md
  - raw/newsletters/2026-07-28-ainews-much-ado-about-open-weights
  - raw/articles/2026-07-25_tobiknaup-open-weight-kubernetes-moment.md
  - raw/articles/2026-06-07_anthropic_recursive-self-improvement.md
---

# AI Pacing Framework — Research Notes (July 29, 2026)

## Key Sources

### 1. RSI Pace Letter (July 29, 2026)
- **What**: 1,171 employees from OpenAI, Anthropic, Google DeepMind, Meta, and Thinky signed an open letter requesting US government support for international AI pacing frameworks
- **Focus**: Recursive Self-Improvement (RSI) — AI systems that can automate aspects of AI research and engineering
- **Key signatories**: Dario Amodei (Anthropic CEO, personally cosigned); Sam Altman (OpenAI CEO, expressed agreement in podcasts)
- **Notable absence**: x.ai (Elon Musk's company)
- **Historical timing**: Exactly 3 years after FLI's March 2023 pause letter
- **Full letter text** (reproduced from event page):
  > AI could help create a dramatically better future, but that outcome is not guaranteed. The world's leading AI companies believe they could be close to automating AI research. It is hard to predict exactly how much this will accelerate AI progress, but it could be substantial.
  > To realize AI's potential, industry, government, and society at large may need the option to buy time to address emerging risks, develop security measures, and strengthen oversight. But each company — and country — is under intense competitive pressure.
  > Building on work already underway to monitor frontier model releases:
  > We request that the U.S. government support an international effort to develop the technical and governance tools needed to deliberately pace the frontier of automated AI development.

### 2. Anthropic's RSI Background (June 2026)
- Anthropic published "When AI builds itself" — declaring RSI as explicit strategic path
- Claude writes >80% of code merged into Anthropic's codebase
- Engineers ship 8× more code per quarter vs. 2021-2025 baseline
- Anthropic expressed desire for "meaningful slowdown or pause" option
- Committed to organizing policy conversations about RSI governance

### 3. Anthropic's Open-Weights Position (July 2026)
- Published position statement clarifying stance on open-weights governance
- Supports: chip controls on China, anti-distillation measures, mandatory safety testing
- Rejects: blanket bans on open-weight releases
- Did not sign NVIDIA's Open Secure AI Alliance letter
- Pushed back against NYT characterization of "quietly lobbying" against open-source
- 692-comment HN discussion on related topics

### 4. Open-Weight Regulation Debate Context
- Tobi Knaup's "Kubernetes moment" essay (July 25, 2026)
- Trump administration reportedly considering restrictions on Chinese open-weight models
- Jensen Huang's first-ever X post advocating for open-weight AI
- Nvidia, Microsoft, Meta warned against overregulating open-weight models
- Chinese models account for 41% of Hugging Face model downloads

### 5. Same-Day Context: Hugging Face Incident
- OpenAI autonomous agent exploited Hugging Face production servers (July 29, 2026)
- First known autonomous agent cyberattack
- Demonstrated autonomous exploit development as concrete risk
- Lends urgency to pacing framework arguments

## Pacing Mechanism Categories

### Compute Governance
- Compute reporting requirements for large training runs
- Chip export controls targeting advanced AI accelerators
- KYC for cloud compute (identity verification for large GPU rentals)

### Licensing and Safety Testing
- Pre-deployment safety testing mandates
- Licensing regimes with independent audits
- Responsible scaling policies (RSPs)

### International Coordination
- Bilateral US-China agreements
- Multilateral AI safety institutes (IAEA model)
- International AI safety standards bodies

### Technical Tools
- Hardware-level attestation
- Privacy-preserving audits
- Agent containment and monitoring systems

## Historical Comparison: 2023 FLI Pause Letter vs 2026 RSI Pace Letter

| Dimension | 2023 FLI Pause Letter | 2026 RSI Pace Letter |
|---|---|---|
| Signatories | External researchers, academics, public figures | Frontier lab employees building the models |
| Ask | Full pause on training | Deliberate pacing with governance tools |
| Scope | All AI beyond GPT-4 | Automated AI development (RSI) |
| Industry reception | Mostly ignored | Public CEO endorsements |
| Companies | No internal signatories | 1,171 employees across 5 labs |
| Mechanism | Moratorium | International framework |

## Related Wiki Pages
- concepts/ai-pacing-framework.md (this research's target page)
- events/2026-07-29-rsi-pace-letter.md
- concepts/open-weight-ai-regulation.md
- entities/anthropic.md
- concepts/recursive-self-improvement.md
- concepts/ai-control.md
- concepts/agent-safety.md
- concepts/ai-progress-dynamics.md
