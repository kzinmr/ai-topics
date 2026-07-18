---
title: "VulnHunter: Capital One's Open-Source, Agentic AI Code Security Tool"
url: "https://www.capitalone.com/tech/open-source/announcing-vulnhunter/"
date: "2026-07-17"
source: "Capital One Tech Blog"
author: "Capital One Tech"
tags:
  - agentic-ai
  - code-security
  - vulnerability-scanning
  - open-source
  - claude-code
  - saast
  - falsification-engine
  - capital-one
summary: |
  Capital One open-sourced VulnHunter, an agentic AI security tool that uses Claude Opus 4.8 to perform attacker-perspective code analysis. Unlike traditional SAST scanners, VulnHunter employs a falsification engine to challenge its own findings, forward-attack-path reasoning from entry points, and evidence-backed remediation modeling. The tool was validated across thousands of internal repositories and is released under Apache 2.0 as a set of Claude Code skills (vulnhunt, vulnhunter-fix, vulnhunt-fix-verify) forming a closed-loop hunt→fix→verify pipeline. HN discussion (71 points, 34 comments) noted similar tools from Visa and Cloudflare, skepticism about false sense of security, and the growing trend of agentic security methodologies.
hn_url: "https://news.ycombinator.com/item?id=48946692"
hn_points: 71
hn_comments: 34
github_url: "https://github.com/capitalone/VulnHunter"
license: "Apache 2.0"
---

# VulnHunter: Capital One's Open-Source, Agentic AI Code Security Tool

**Published:** July 17, 2026  
**Source:** Capital One Tech Blog  
**URL:** https://www.capitalone.com/tech/open-source/announcing-vulnhunter/  
**HN Discussion:** https://news.ycombinator.com/item?id=48946692 (71 points, 34 comments)  
**GitHub:** https://github.com/capitalone/VulnHunter  

---

## Capital One Blog Post (Full Article)

### Introduction

The rules of software security are changing faster than most defenders can keep pace.

Advanced AI models have dramatically lowered the barrier for bad actors to discover and exploit vulnerabilities in software. What once required significant skill and time can now be automated, accelerated, and scaled. The world faces an increasingly short window of time before highly sophisticated, next-generation AI attack capabilities become affordable and accessible to virtually every adversary. Across the industry, organizations are racing to prepare for this paradigm shift.

Traditional environmental protections like network segmentation, identity controls, and monitoring remain essential, but are no longer sufficient on their own. The ultimate defense in this new reality requires a shift in approach: organizations need to consider and detect the vulnerabilities in their code and fix them before adversaries can deploy advanced models to discover and exploit them.

At Capital One, we decided that the right response to AI-enabled threats wasn't to wait, but to build cutting-edge AI-driven defenses and put them in the hands of defenders everywhere.

That's why we are announcing today the open-source release of **VulnHunter**, an advanced agentic AI security tool designed to apply proactive, attacker-perspective analysis directly to the source code.

Developed internally at Capital One, VulnHunter is not a traditional, passive vulnerability scanner. It represents a shift in defensive tooling with an agentic reasoning workflow to identify potentially exploitable defects, map prospective attack paths, and propose highly targeted code remediations.

### Built for the Developer Experience

To fully unlock the utility of VulnHunter, we knew ease of use mattered. A persistent challenge with traditional security tools is that they are often built primarily to enforce rigid cybersecurity practices, without much consideration for a developer's actual day-to-day workflow.

We brought a developer-first mindset when building VulnHunter. We knew the only way a security tool can be successful at enterprise scale is if it is something developers actually want to use.

We focused on making the developer experience highly efficient in the moments that matter. By intentionally rounding out and minimizing traditional points of friction throughout the development process, VulnHunter shifts the developer's burden away from triaging false alarms. Instead, the workflow is focused on immediate, evidence-backed code repair.

### Under the Hood: The Unique Capabilities of VulnHunter

VulnHunter introduces several key technical innovations designed to minimize speculative alerts and maximize actionable repair:

1. **Falsification Engine Designed to Challenge Its Own Conclusions:** Our goal is to minimize false positives before they ever reach a developer. After surfacing any finding, VulnHunter runs a structured reasoning workflow specifically designed to disprove its own argument. This falsification engine actively searches for assumptions that don't hold, logical gaps in the exploit path, and conditions that would prevent the attack from succeeding. It is designed to immediately discard findings that rely on unsupported assumptions. The result: what reaches a developer's attention has already survived a rigorous internal challenge. Every flagged vulnerability is one the tool has tried and failed to rule out.

2. **Attacker-First Forward Analysis:** Conventional tools often leverage "sink-first" analysis, looking at potentially dangerous code patterns in isolation to search backward for a hypothetical attacker. This approach can flood engineering teams with false positives. VulnHunter flips this model to simulate a bad actor's exact journey. It begins at potential attacker-accessible entry points — such as APIs, network messages, or file uploads — and reasons forward through application logic, data transformations, and internal security checkpoints. By modeling how an attacker actually interacts with a system, VulnHunter evaluates whether an attacker can truly break through.

3. **Evidence-Backed Remediation Modeling:** When a defect survives the falsification engine, VulnHunter doesn't just sound the alarm and leave the guesswork to developers. It shifts from finding the problem to working to solve it. VulnHunter gathers supporting evidence across the codebase to map out the entire surviving exploit path. It is designed to provide a clear explanation of the defect, detail the specific capabilities or access an attacker would gain, and generate focused, targeted code changes for engineering review.

### Validation

Before releasing VulnHunter to the community, we ran it on our own code. We were able to identify and remediate vulnerabilities across thousands of repositories, spanning tens of business areas, with speed and efficiency. What took our teams significant time and manual triage before now produces verified, actionable findings quickly and effectively.

### A Commitment to Collective Defense

Modern software supply chains are deeply interconnected. A single vulnerability in a widely-used open-source component can ripple across thousands of enterprises simultaneously. We're open-sourcing VulnHunter because no single organization can solve this challenge alone. The defensive tools to address this reality need to be just as widely distributed, tested, and improved as the codebases they protect.

Building on Capital One's commitment to open collaboration, the release of VulnHunter enables the broader tech and security community to inspect the workflow, challenge its assumptions, and contribute improvements to this new defensive approach.

### Get Started with VulnHunter on GitHub

VulnHunter is available now. To run it, you will need access to Claude Opus 4.8 and access to a working Claude Code environment. The repository includes a Quickstart guide, architecture documentation, and annotated example workflows showing how VulnHunter traces code paths and generates remediations. Known limitations and the active development roadmap are documented in the repository.

If you want to contribute — whether that's reporting a bug, proposing a change to the reasoning workflow, or expanding model support — the CONTRIBUTING.md outlines the process for submitting issues and pull requests.

- **Repository:** github.com/capitalone/vulnhunter
- **License:** Apache License 2.0
- **Model Optimization:** Claude Opus 4.8 model
- **Initial Implementation:** Claude Code skill

While VulnHunter was authored and leveraged with Claude Opus 4.8 and Claude Code in mind, the framework and skills have potential to be leveraged across coding harnesses and foundation models.

The threat landscape isn't waiting. We built VulnHunter to give defenders a more rigorous, evidence-driven way to find and fix vulnerabilities before attackers can reach them. We're releasing it because secure software is a shared foundation that benefits developers, enterprises, and the people who depend on the systems we all build. We look forward to seeing what the community builds with this next.

---

## GitHub README

> Source: https://github.com/capitalone/VulnHunter

**VulnHunter** — From pattern-matching to provability.

VulnHunter is an open-source, **agentic AI security tool** that applies proactive, attacker-first analysis directly to source code.

Unlike traditional, passive SAST scanners that flag suspicious patterns and often cause false positives, VulnHunter reasons like an adversary. It **identifies** which defects are actually exploitable, maps prospective attack paths, and proposes targeted, evidence-backed fixes.

Modern software supply chains are deeply interconnected. A single vulnerability in a widely-used open-source component can ripple across thousands of enterprises simultaneously.

Developed internally at Capital One, VulnHunter is released to the community because no single organization can solve this challenge alone.

> [!WARNING]
> **Cyber-safeguard disclaimer:** VulnHunter performs dual-use cybersecurity work (vulnerability discovery and exploitation). If you run it against an Anthropic account that is **not** enrolled in Anthropic's Cyber Verification Program, real-time cyber safeguards may block requests and your usage may be flagged for cyber abuse.

> [!IMPORTANT]
> **Prerequisites & Model Requirements:** Built and optimized for **Claude Opus** running in **Claude Code**. The framework depends on deep, multi-step reasoning and requires frontier Opus-class models. **You supply your own model access.**

### Why VulnHunter is Different

- **Attacker-First Forward Analysis:** Conventional tools often leverage "sink-first" analysis, looking at potentially dangerous code patterns to search backward for a hypothetical attacker, flooding teams with false positives. VulnHunter flips this model to simulate a bad actor's exact journey. It begins at potential attacker-accessible entry points (APIs, network messages, file uploads) and reasons *forward* to evaluate whether an attacker can truly break through.
- **Falsification Engine:** After finding a potential vulnerability, VulnHunter runs a structured reasoning workflow specifically designed to *disprove* its own argument. It searches for flawed assumptions, logic gaps, or security controls that would block the attack. It is designed to immediately discard findings that rely on unsupported assumptions. What reaches you is a high-priority, actionable defect.
- **Evidence-Backed Remediation:** When a defect survives the falsification engine, VulnHunter maps the exact exploit path, explains the structural flaw, details the specific capabilities or access an attacker would gain, and generates focused, targeted code changes for review.

### The Closed Loop: Hunt → Fix → Verify

VulnHunter ships as three composable Claude Code skills that form a complete, automated remediation loop:

| Skill | Phase | Core Responsibility |
| :--- | :--- | :--- |
| **`/vulnhunt`** | **Hunt** | Maps entry points to dangerous sinks. Filters findings through a multi-stage falsification pipeline (Recon → Parallel Hunt → Adversarial Disprove → Capability Filter). Emits only verified issues with an executable exploit and a proposed fix. |
| **`/vulnhunter-fix`** | **Fix** | Developer-led, test-driven remediation. It writes an exploit demo, creates a failing security test (**RED**), implements the code fix (**GREEN**), verifies the exploit is blocked without regressions, and cuts a reviewable PR. |
| **`/vulnhunt-fix-verify`** | **Verify** | A completely separate, read-only agent that independently validates whether a finding was successfully remediated. It emits a per-finding verdict so fixes are proven, not taken on faith. |

> **Note:** For running this loop unattended at scale, `vulnhunter-agent/` wraps the scanner in a headless runtime, while `harness/` drives it across multiple repositories in batch.

### Repository Layout

| Path | Description |
| :--- | :--- |
| `vulnhunt/` | The core `/vulnhunt` scanner skill (Prompt-only: `SKILL.md` + phases) |
| `vulnhunter-fix/` | The `/vulnhunter-fix` skill, its companion Python helper package, and tests |
| `vulnhunt-fix-verify/` | The `/vulnhunt-fix-verify` standalone verification skill (Prompt-only) |
| `vulnhunter-agent/` | Config-driven headless runtime wrapper that runs scans and files GitHub issues |
| `harness/` | Developer tooling for running large batch-scans and benchmarking detection accuracy |

### Requirements & Setup

**Prerequisites:**
- Claude Code CLI, authenticated with access to **Claude Opus**
- Python 3.12+ (Required only for the runtime agent and the benchmarking harness)
- Responsibility Check: Ensure you are only scanning code bases you are explicitly authorized to analyze

**Installation:**
```bash
git clone https://github.com/capitalone/vulnhunter.git
cd vulnhunter
./install.sh      # Copy skills into ~/.claude/skills/
```

### Usage

```bash
# 1. Run the Scanner
claude --model opus --add-dir ~/.claude/skills/vulnhunt --add-dir ~/.claude/skills/vulnhunt/phases
# Inside the Claude Code session, invoke: /vulnhunt

# 2. Run the Fixer (requires git, gh CLI, Python helpers)
claude --model opus --add-dir ~/.claude/skills/vulnhunter-fix
# Inside the Claude Code session, invoke: /vulnhunter-fix

# 3. Run the Fix Verifier (read-only, no Bash execution, no network access)
claude --model opus --add-dir ~/.claude/skills/vulnhunt-fix-verify \
       --add-dir ~/.claude/skills/vulnhunt-fix-verify/phases
# Inside the Claude Code session, invoke: /vulnhunt-fix-verify repo=<abs_path> report=<abs_path> fixed=VULN-001,... out=<abs_path>
```

### Automation & Scale

- **Headless Runtime Agent (`vulnhunter-agent/`):** For non-interactive or CI/CD pipelines. Wraps the scanner into a headless workflow. Clones targets, executes `/vulnhunt`, publishes results, and opens GitHub issues for confirmed bugs. Connects via the direct Anthropic API.
- **Local Harness (`harness/`):** Workstation-scale developer tooling for batch scanning and benchmarking. Manage target lists in `REPO_LIST.txt`, run scans across repos, and benchmark against known-vulnerable corpora.

### Contributing, Security & License

- **A Note on Models:** VulnHunter was precision-tuned for **Claude Opus** and **Claude Code**. Its low false-positive discipline relies heavily on frontier-class reasoning, though the underlying orchestration patterns can be adapted to other advanced foundation models.
- **License:** Apache License, Version 2.0

---

## Hacker News Discussion Highlights

**Thread:** https://news.ycombinator.com/item?id=48946692  
**Posted:** July 17, 2026 | **Points:** 71 | **Comments:** 34

### Notable Comments

1. **@ph3t:** "All these security/vulnerability scanning harnesses look more or less the same. Not sure what's the point of bragging or publishing about them anymore, there's no moat."
   - **@skybrian:** "I imagine they built it mostly for themselves, but open sourcing it is a nice gesture."

2. **@_joel:** "Why does this feel like an exec trying to justify token spend?"
   - **@bobthebob:** "They don't need to justify it. Sorry to say, tokens aren't going anywhere... this whole paradigm shift of how people are changing how they work - is a full blown reality."
   - **@cute_boi:** "Don't underestimate how banks operate. Things move very slowly in banking, so they absolutely need to justify it."
   - **@deaton:** "Why does this feel like an exec trying to justify token spend?"

3. **@_pdp_:** "IMHO these type of projects are not tools per-se but methodologies. I think this is a better framing since that's exactly what they are - a bunch of markdown files that describe in general terms how to perform an assessment aligned to some principles. Btw, these type of methodologies are used all the time. Practically every security consultancy has them so adding them to an LLM makes a lot of sense."

4. **@lfx:** Pointed out similar tools: Visa's [vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) and Cloudflare's [security-audit-skill](https://github.com/cloudflare/security-audit-skill). "I'm on the fence here, for one as from recent Linux mailing discussions those tools can really find good bugs (51% of them?), but on other side - I'm afraid of false sense of security."

5. **@spikk:** "I think it's actually interesting how you can use the same model to both find and falsify the findings."
   - **@snorbleck:** "you can, but it's better to use a different model or higher effort level at the very least to do the verifying part... passing the finding(s) to a model that hasn't seen it before and it will judge it with an unbiased perspective."

6. **@bpmct:** "Curious if the team at CapitalOne can share in more detail how this tool is being used internally, including how it's helped their security practices and culture."

7. **@xur17:** "If you intend to use VulnHunter on Anthropic's first-party platforms (Claude API / Claude Code), we strongly recommend enrolling first via the verification portal. Has anyone actually had success with this? I applied for my company several weeks ago, and never heard back."

8. **@mkagenius:** Shared [instavm/security-skills](https://github.com/instavm/security-skills) — security skills distilled from 4000 HackerOne disclosures, designed for mitmproxy-based real-time API traffic pentesting.

9. **@throw567643u8:** "Repo will be inactive and obsolete within 12 months."

10. **@liampulles:** "Wasn't Capital One founded on the premise of massive-scale market and product experimentation? Makes sense that they would design tools that match that approach."

### Key Themes from Discussion

- **Skepticism about novelty:** Many commenters noted similar tools from Visa, Cloudflare, and others.
- **Methodology vs. Tool debate:** Several argued these are better framed as LLM-guided methodologies rather than standalone tools.
- **False sense of security concerns:** While acknowledging LLMs can find real bugs, there's worry about over-reliance.
- **Falsification approach praised:** The self-challenge mechanism was seen as an interesting innovation.
- **Banking context:** Discussion of how slowly banks adopt technology, making this release noteworthy for the financial sector.
- **Anthropic Cyber Verification Program friction:** Users reported difficulty enrolling in the required verification program.

---

## Key Links

- **Capital One Blog Post:** https://www.capitalone.com/tech/open-source/announcing-vulnhunter/
- **GitHub Repository:** https://github.com/capitalone/VulnHunter
- **HN Discussion:** https://news.ycombinator.com/item?id=48946692
- **Related: Visa Vulnerability Agentic Harness:** https://github.com/visa/visa-vulnerability-agentic-harness
- **Related: Cloudflare Security Audit Skill:** https://github.com/cloudflare/security-audit-skill
- **Related: instavm/security-skills:** https://github.com/instavm/security-skills
