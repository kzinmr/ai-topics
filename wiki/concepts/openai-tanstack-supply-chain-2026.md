---
title: "OpenAI TanStack npm Supply Chain Attack Response (May 2026)"
type: concept
status: complete
created: 2026-05-14
updated: 2026-05-14
tags:
  - security
  - openai
related:
  - concepts/agentic-security
  - concepts/ai-supply-chain-security
  - entities/openai
  - entities/codex
sources:
  - raw/articles/openai.com--index-our-response-to-the-tanstack-npm-supply-chain-attack--7e8d14b0.md
---

# OpenAI TanStack npm Supply Chain Attack Response (May 2026)

In May 2026, OpenAI disclosed its response to the **Mini Shai-Hulud** supply chain attack, which compromised open-source npm packages including TanStack. This incident is a significant case study in how supply chain attacks propagate to downstream organizations and how large AI companies respond.

## What Happened

- **Attack vector**: Compromised TanStack npm package (part of the broader "Mini Shai-Hulud" campaign)
- **Impact on OpenAI**: Two employee devices in the corporate environment downloaded and executed the malicious package
- **Data accessed**: Limited unauthorized access to internal source code repositories to which the two impacted employees had access
- **Credentials**: Limited credential material was successfully exfiltrated from these repositories, including signing certificates for iOS, macOS, Windows, and Android products
- **No customer data or IP compromise**: OpenAI found no evidence that user data, production systems, or intellectual property were compromised

## OpenAI's Response

### Immediate Actions
1. Isolated impacted systems and identities
2. Revoked user sessions
3. Rotated all credentials across impacted repositories
4. Temporarily restricted code-deployment workflows
5. Engaged a third-party digital forensics and incident response firm

### Certificate Rotation
- All application signing keys (iOS, macOS, Windows, Android) were rotated
- **macOS users** required to update apps by June 12, 2026
- Windows and iOS apps did not require user action
- Previous signing certificates blocked from further notarization
- Coordinated with platform providers to prevent unauthorized use

### Affected macOS Applications (last versions with old certificates)
| Application | Version |
|-------------|---------|
| ChatGPT Desktop | 1.2026.125 |
| Codex App | 26.506.31421 |
| Codex CLI | 0.130.0 |
| Atlas | 1.2026.119.1 |

### Security Controls Accelerated After Axios Incident
After the earlier Axios incident, OpenAI had begun deploying additional controls:
- Hardening of sensitive credential materials in CI/CD pipelines
- Package manager configurations with `minimumReleaseAge` controls
- Security software to validate provenance of new packages

**Critical finding**: The two impacted employee devices did not yet have the updated configurations, highlighting the risk of phased security rollouts.

## Broader Significance

### Shift in Threat Landscape
OpenAI noted that attackers are increasingly targeting **shared software dependencies and development tooling** rather than individual companies. Modern software built on interconnected open-source libraries, package managers, and CI/CD infrastructure means a vulnerability introduced upstream can propagate widely and quickly.

### AI Supply Chain Risk
This incident is particularly relevant for AI agent security because:
1. Coding agents (Codex, Claude Code, etc.) automatically install npm/pip packages
2. Agents may not evaluate package safety before installation
3. A compromised package in an agent's dependency chain could lead to credential theft, data exfiltration, or lateral movement
4. The incident demonstrates that even well-resourced companies with dedicated security teams are vulnerable to supply chain attacks

### Lessons for AI Agent Deployment
- **Never fully trust the dependency chain**: Even popular, well-maintained packages can be compromised
- **Phase security controls carefully**: Rolling out protections gradually leaves windows of vulnerability
- **Certificate management is critical**: Code signing certificates are high-value targets for attackers
- **Monitor for indicators of misuse**: Ongoing vigilance after initial containment is essential

## Related Incidents

- **Axios incident** (earlier 2026): Preceded OpenAI's security control acceleration
- **Claude Code npm sourcemap leak** (April 2026): Entire Claude Code TypeScript source leaked via `.map` file in npm package
- **Cline compromised agent** (2026): AI coding assistant installed rogue agents on thousands of systems
- **Mini Shai-Hulud campaign**: Broader attack campaign targeting npm ecosystem
