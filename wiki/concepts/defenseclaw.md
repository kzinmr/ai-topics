---
title: "DefenseClaw"
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [agent-safety, security, infrastructure, open-source, sandbox, cisco, openclaw]
sources: [raw/articles/2026-03-23_cisco-defenseclaw-rsac.md]
---

# DefenseClaw

An open-source agentic governance layer built by Cisco, announced at RSAC 2026 (March 23). DefenseClaw secures [[entities/openclaw|OpenClaw]] deployments by providing pre-run scanning, runtime threat detection, and non-advisory enforcement. It sits on top of **NVIDIA OpenShell** (kernel isolation/sandboxing) as an operational security layer.

## Why DefenseClaw Exists

The OpenClaw ecosystem faced a security crisis in early 2026:
- **CVE-2026-25253:** Critical RCE vulnerability — malicious webpages hijacking agents
- **135,000+ instances** exposed on the public internet
- **ClawHavoc:** ~800 malicious skills (20% of ClawHub registry) planted for information theft
- Part of the broader "Lethal Trifecta" of agent security incidents alongside [[concepts/moltbook-breach-2026]]

> "OpenShell gives you the sandbox. Cisco gives you the scanners. But who manages the block lists? Who sees the alerts when something goes wrong at 2 AM? That's DefenseClaw." — DJ Sampath

## Three Pillars

### 1. Pre-run Scanning (Admission Gate)
Every skill, tool, or AI-generated code fragment is scanned before installation:

| Scanner | Purpose |
|:---|:---|
| **skill-scanner** | Vets community-contributed skills |
| **mcp-scanner** | Secures MCP supply chain |
| **a2a-scanner** | Secures Agent-to-Agent communications |
| **CodeGuard** | Static analysis on AI-generated code |
| **AI BOM** | Generates manifest of the AI stack |

### 2. Runtime Threat Detection
A content scanner inspects every message in the execution loop — catching data exfiltration or malicious behavior that emerges after installation.

### 3. Non-Advisory Enforcement
Enforcement is immediate and structural (not suggestive):
- **Skill Blocking:** Revokes sandbox permissions, quarantines files
- **MCP Server Blocking:** Removes endpoints from sandbox network allow-list
- **Speed:** Actions take effect in <2 seconds without restart

## Observability
Native **Splunk integration** streams scan findings, block/allow decisions, prompt-response pairs, and tool calls as structured events — designed for enterprise SOC monitoring.

## Ecosystem Position

DefenseClaw is part of a growing "claw" security ecosystem:
- **OpenClaw:** The agent OS (by Peter Steinberger)
- **NVIDIA OpenShell:** Kernel-level sandboxing
- **NVIDIA NemoClaw:** Enterprise governance for OpenClaw
- **DefenseClaw:** Cisco's open-source security layer

This "claw" pattern mirrors how Linux distributions layered security (SELinux, AppArmor) on top of the kernel.

## Comparison with Other Agent Security Efforts

| Aspect | DefenseClaw | Microsoft Agent Governance Toolkit |
|:---|:---|:---|
| Scope | OpenClaw-specific | Framework-agnostic |
| Approach | Scanner-driven | Policy-driven |
| Enforcement | Non-advisory (blocking) | Policy-based |
| Identity | OpenShell integration | DIDs + Ed25519 |
| Observability | Splunk-native | Framework-integrated |

Both are open-source and complementary — DefenseClaw for OpenClaw deployments, Microsoft's toolkit for broader framework coverage.

## Related Pages
- [[entities/openclaw]]
- [[concepts/openclaw-architecture]]
- [[concepts/moltbook-breach-2026]]
- [[concepts/agent-sandboxing]]
- [[concepts/agent-sandbox-patterns]]
- [[entities/nvidia]]
