# Cisco DefenseClaw: Open-Source Security for the Agentic Workforce

**Source:** [Cisco Blogs](https://blogs.cisco.com/ai/cisco-announces-defenseclaw)
**Date:** March 23, 2026 (RSAC 2026)
**Author:** DJ Sampath (SVP/GM, AI Software and Platform, Cisco)
**Repository:** [github.com/cisco-ai-defense/defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)

## Context: The OpenClaw Security Crisis
OpenClaw has become the "operating system for personal AI" but created significant vulnerabilities:
- **CVE-2026-25253:** Critical RCE vulnerability — malicious webpage could hijack an agent
- **135,000+ instances** exposed on the public internet
- **ClawHavoc:** ~800 malicious skills (20% of ClawHub registry) planted for information theft
- **Prompt Injection:** Data exfiltration via third-party skills

## DefenseClaw Overview
An open-source agentic governance layer built by Cisco. Sits on top of **NVIDIA OpenShell** (kernel isolation/sandboxing) to provide operational security.

> "OpenShell gives you the sandbox. Cisco gives you the scanners. But who manages the block lists? Who sees the alerts when something goes wrong at 2 AM? That's DefenseClaw."

## Three Pillars

### A. Pre-run Scanning (Admission Gate)
Five integrated scanners before any skill/tool installation:
1. **skill-scanner:** Vets community-contributed skills
2. **mcp-scanner:** Secures MCP supply chain
3. **a2a-scanner:** Secures Agent-to-Agent communications
4. **CodeGuard:** Static analysis on AI-generated code
5. **AI Bill-of-Materials (BOM):** Generates manifest of the AI stack

### B. Runtime Threat Detection
Content scanner inspects every message in the execution loop for data exfiltration or emergent malicious behavior.

### C. Non-Advisory Enforcement
Immediate and structural (not suggestive):
- **Skill Blocking:** Revokes sandbox permissions, quarantines files
- **MCP Server Blocking:** Removes endpoints from sandbox network allow-list
- **Speed:** Under 2 seconds, no restart required

## Observability
Native **Splunk integration** — streams scan findings, block/allow decisions, prompt-response pairs, and tool calls as structured events.

## Availability
- **Release:** March 27, 2026 on GitHub
- **Related:** Cisco Skill Scanner, NVIDIA OpenShell integration
