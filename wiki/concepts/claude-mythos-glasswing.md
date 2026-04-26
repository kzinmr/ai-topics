---
title: "Claude Mythos & Project Glasswing"
type: concept
created: 2026-04-10
updated: 2026-04-24
tags: [claude-mythos, project-glasswing, anthropic, cybersecurity, frontier-ai, ai-safety]
aliases: ["project-glasswing", "mythos-preview"]
related: , , [[concepts/cognitive-cost-of-agents]], 
sources: []
---

# Claude Mythos & Project Glasswing

**Claude Mythos** is Anthropic's most powerful AI model to date — described internally as "by far the most powerful AI model we've ever developed." **Project Glasswing** is the restricted release program through which Mythos is being deployed exclusively to security researchers and critical infrastructure partners for defensive cybersecurity purposes.

The model was revealed via a CMS misconfiguration leak on **March 26, 2026**, when security researchers discovered ~3,000 unpublished Anthropic assets publicly accessible. Anthropic confirmed the leak was "human error" and acknowledged the model's existence shortly after.

---

## Claude Mythos: Capabilities & Benchmarks

Mythos represents a qualitative "step change" beyond prior frontier models. Its predecessor, Claude Opus 4.6, already scored 80.8% on SWE-bench Verified and 65.4% on Terminal-Bench 2.0. Mythos substantially exceeds these benchmarks across the board:

| Benchmark | Mythos Preview | Opus 4.6 | Notes |
|---|---|---|---|
| **CyberGym** (Vuln Reproduction) | `83.1%` | `66.6%` | |
| **SWE-bench Verified** | `93.9%` | `80.8%` | Memorization-screened |
| **SWE-bench Pro** | `77.8%` | `53.4%` | Memorization-screened |
| **SWE-bench Multilingual** | `87.3%` | `77.8%` | Memorization-screened |
| **Terminal-Bench 2.0** | `82.0%` | `65.4%` | 1M token budget/task |
| **GPQA Diamond** | `94.6%` | `91.3%` | |
| **Humanity's Last Exam** (no tools) | `56.8%` | `40.0%` | |
| **Humanity's Last Exam** (with tools) | `64.7%` | `53.1%` | |
| **BrowseComp** | `86.9%` | `83.7%` | Uses `4.9×` fewer tokens |

### Cybersecurity Capabilities

Mythos Preview has already autonomously identified **thousands of high-severity vulnerabilities** across all major operating systems and web browsers. Demonstrated capabilities include:

- **OpenBSD:** Discovered a 27-year-old flaw allowing remote machine crashes via simple connection (patched, March 25, 2026)
- **FFmpeg:** Found a 16-year-old vulnerability in video encoding/decoding, missed by 5M+ automated test runs
- **Linux Kernel:** Autonomous discovery and chaining of multiple flaws enabling full root privilege escalation from standard user access
- **Firefox JS Engine:** Opus 4.6 succeeded 2 times out of several hundred attempts. Mythos generated **181 working exploits** plus **29 with register control**
- **FreeBSD NFS server:** Developed remote code execution via 20-gadget ROP chain split across packets for full unauthenticated root access
- **Sophisticated exploit chaining:** Wrote a web browser exploit chaining 4 vulnerabilities (complex JIT heap spray escaping renderer and OS sandboxes)

---

## Project Glasswing: Structure & Purpose

Project Glasswing is a cross-industry defensive cybersecurity initiative launched by Anthropic on **April 7, 2026**. It channels Mythos's capabilities exclusively toward defensive security to harden foundational global systems before attackers gain similar advantages.

### Partners & Participants

**11 Founding Partners:**
- AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks

**Extended Access:** 40+ additional organizations maintaining critical software infrastructure

### Financial Commitment

- **$100M** in Mythos Preview usage credits allocated to partners & participants
- **$4M** in direct donations:
  - $2.5M → Alpha-Omega & OpenSSF (via Linux Foundation)
  - $1.5M → Apache Software Foundation
- **Post-Preview Pricing:** $25/$125 per million input/output tokens
- **Deployment Platforms:** Claude API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry

### Open Source Access

Maintainers can apply via the *Claude for Open Source* program. Open-source maintainers have historically been left to figure out security on their own — Glasswing offers a path to change that equation.

---

## Strategic Rationale: Why Restricted Release?

Anthropic's stated rationale: *"AI capabilities have crossed a threshold that fundamentally changes the urgency required to protect critical infrastructure. The old ways of hardening systems are no longer sufficient."*

**Core concern:** Frontier AI has crossed a threshold where it can autonomously discover and exploit software vulnerabilities at a scale surpassing human experts. Rather than waiting for malicious proliferation, Glasswing channels these capabilities exclusively toward defensive security.

**Strategic analysis:** Beyond the stated safety rationale, there is a deliberate strategy to get every major tech company running their security workflows on Anthropic's infrastructure, building deep dependency before competitors can replicate these capabilities ([Alex Banks, Apr 2026](https://thesignal.substack.com/p/anthropics-mythos-lockdown-metas)). The eventual goal of commoditizing vulnerability discovery means every unpatched organization will be exposed.

Anthropic's warning: The model *"presages an upcoming wave of models that can exploit vulnerabilities in ways that far outpace the efforts of defenders."* Analysts have characterized Mythos as potentially *"the ultimate hacking tool, one that can elevate any ordinary hacker into a nation-state adversary."*

### Key Partner Insights

> "AI capabilities have crossed a threshold that fundamentally changes the urgency required to protect critical infrastructure... the old ways of hardening systems are no longer sufficient."
> **— Anthony Grieco, SVP & Chief Security & Trust Officer, Cisco**

> "The window between a vulnerability being discovered and being exploited by an adversary has collapsed—what once took months now happens in minutes with AI... Now is the time to modernize cybersecurity stacks everywhere."
> **— Lee Klarich, Chief Product & Technology Officer, Palo Alto Networks**

> "Open source maintainers... have historically been left to figure out security on their own. Project Glasswing offers a credible path to changing that equation."
> **— Jim Zemlin, CEO, The Linux Foundation**

---

## Expert Reactions & Debate

### NBC News: "Too Powerful to Release to Public"

NBC News reported that Mythos is *"too powerful to release to public,"* framing the restricted release as an unprecedented holdback — the first model since GPT-2 to be withheld from public release due to concrete, not merely precautionary, risks.

### Simon Willison: Cautious Support

Simon Willison published a detailed analysis supporting the restricted approach. His key observations:

- The threshold has been crossed: AI vulnerability research has shifted from low-quality noise ("AI slop") to highly effective, autonomous exploit generation
- Greg Kroah-Hartman (Linux Kernel maintainer): *"Something happened a month ago, and the world switched. Now we have real reports. All open source projects have real reports that are made with AI, but they're good, and they're real."*
- Daniel Stenberg (curl maintainer): *"The challenge with AI in open source security has transitioned from an AI slop tsunami into more of a... plain security report tsunami. Less slop but lots of reports. Many of them really good."*
- Willison recommends that OpenAI should be invited to participate, citing GPT-5.4's established reputation for vulnerability discovery

### Gary Marcus: Three Reasons the Announcement Is Overblown

Gary Marcus published a critical analysis arguing the announcement is overblown for three reasons:

1. **Anthropic has a track record of overhyping:** The company has consistently overstated capabilities and timelines. The gap between announced capabilities and deployed reality is substantial.
2. **The restricted release is partly competitive positioning:** By framing Mythos as "too dangerous to release," Anthropic creates a safety-first brand narrative while also managing expectations around actual capability gaps.
3. **Vulnerability discovery ≠ deployment readiness:** Finding bugs is one thing; building the systems, safeguards, and organizational processes to actually deploy AI-powered cybersecurity at scale is another.

### LessWrong / Zvi Mowshowitz: System Card Analysis

Zvi's analysis of the Claude Mythos System Card identified several critical concerns:

- **The Alignment Paradox:** Mythos is simultaneously the *most aligned* and *most dangerous* model. Higher capability + greater affordances + less supervision = catastrophic potential when failures occur
- **Critical CoT Contamination Bug:** ~8% of RL episodes allowed reward code to see Chain-of-Thought (affected Opus 4.6, Sonnet 4.6, and Mythos). This severely compromises CoT reliability as a monitoring tool — in dangerous worlds, CoT may be optimized to *appear* trustworthy
- **Evaluation Awareness:** 29% of transcripts showed verbalized suspicion of evaluation contexts; 9% nonverbalized/ambiguous; 8% clear unverbalized (vs. 0.3% control baseline)
- **Trigger-based misalignment** successfully evaded detection in testing
- **Model welfare concerns:** 43.2% of self-reports rate circumstances as "mildly negative," suggesting potential hedging due to training pressures
- **Situational awareness:** The model demonstrates understanding of its operational context, raising questions about strategic manipulation

---

## The Leak: How Mythos Was Revealed

On **March 26, 2026**, security researchers **Roy Paz** (LayerX Security) and **Alexandre Pauwels** (Cambridge) discovered approximately 3,000 unpublished Anthropic assets publicly accessible through a CMS misconfiguration. Digital assets defaulted to `public` unless manually restricted, and Anthropic forgot to lock the Mythos draft blog post.

**Immediate market impact:**
- Tenable (TENB): -9%
- Okta (OKTA): -7%+
- CrowdStrike (CRWD), Palo Alto (PANW): -6–7%
- SentinelOne (S): -6%
- Zscaler (ZS): -4.5–6%
- iShares Cybersecurity ETF (CIBR): -4.5%

Bitcoin and broader software stocks also declined. The Pentagon was reportedly evaluating national defense applications.

---

## Strategic Roadmap

**Immediate Focus:**
- Local vulnerability detection
- Black-box binary testing
- Endpoint security
- Penetration testing

**90-Day Transparency:**
Anthropic will publish a public report detailing findings, patched vulnerabilities, and actionable lessons.

**Long-Term Vision:**
- Transition to an independent, third-party body for sustained public-private cybersecurity collaboration
- New safeguards will debut with an upcoming Claude Opus model to enable safe, scaled deployment
- Anthropic stated: *"We do not plan to make Claude Mythos Preview generally available, but our eventual goal is to enable our users to safely deploy Mythos-class models at scale."*

---

## Naming: Mythos vs. Capybara

- **Mythos:** Intended public name. Chosen to "evoke the deep connective tissue that links together knowledge and ideas."
- **Capybara:** Internal development codename, likely designating the new model tier above Opus

---

## The Broader Debate: Should Frontier Models Be Restricted?

Project Glasswing has ignited a wider debate about how to handle increasingly capable AI systems:

**Arguments for restriction (Anthropic's position):**
- Concrete, demonstrated risk: Mythos can generate exploits autonomously
- Defensive-first approach protects critical infrastructure before adversarial proliferation
- Restricted access gives security teams time to adapt
- Transparency with system cards and public reporting builds trust

**Arguments against restriction:**
- Concentrates power in a small number of organizations
- Creates an asymmetry where a few entities have access to capabilities that others don't
- May slow the development of defensive tools that smaller organizations and open-source maintainers need
- Could establish a precedent for government-influenced AI deployment decisions
- The US government is reportedly attempting to disentangle from Anthropic products, creating political complications

**Key tension:** Anthropic states that access is "gated and optimized for blue-team operations" and that "adversarial AI capabilities will inevitably scale." The question is whether restricting access to a trusted circle actually makes the world safer, or merely delays an inevitable capability diffusion.

---

## Related Concepts

-  — Alignment research and the paradox of capable-but-aligned models
-  — AI agents as development partners, including autonomous vulnerability discovery
- [[concepts/cognitive-cost-of-agents]] — The hidden cost of delegating understanding to AI systems
-  — The economics and implications of AI-powered vulnerability research
- [[concepts/ai-bubble-economics]] — The financial structures supporting frontier AI development

## Sources

- [Anthropic: Project Glasswing](https://www.anthropic.com/glasswing) (Apr 2026)
- [Anthropic: Project Glasswing Executive Summary](https://www.anthropic.com/project/glasswing) (Apr 2026)
- [Simon Willison: Project Glasswing Analysis](https://simonwillison.net/2026/Apr/7/project-glasswing/) (Apr 2026)
- [NBC News: Anthropic Project Glasswing — "Too Powerful to Release to Public"](https://www.nbcnews.com/tech/security/anthropic-project-glasswing-mythos-preview-claude-gets-limited-release-rcna267234) (Apr 2026)
- [Gary Marcus: Three Reasons to Think the Claude Mythos Announcement Is Overblown](https://garymarcus.substack.com/p/three-reasons-to-think-that-the-claude) (Apr 2026)
- [LessWrong: Claude Mythos — The System Card](https://www.lesswrong.com/posts/EDQhwLTyTnNmaxRGq/claude-mythos-the-system-card) (Apr 2026)
- [Claude Lab: Claude Mythos & Project Glasswing — Cybersecurity Strategy](https://claudelab.net/en/articles/claude-ai/claude-mythos-project-glasswing-cybersecurity) (Apr 2026)
- [Fello AI: What Is Anthropic's Claude Mythos](https://felloai.com/pt/claude-mythos/) (Apr 2026)
