---
title: "Cloudflare"
type: entity
entity_type: organization
created: 2026-05-19
updated: 2026-05-19
tags:
  - security
  - infrastructure
aliases: ["Cloudflare, Inc."]
sources:
  - raw/articles/blog.cloudflare.com--2026-05-18_cyber-frontier-models--9cce0b5a.md
---

# Cloudflare

**Cloudflare, Inc.** is a global cloud services provider offering content delivery network (CDN), DDoS mitigation, Internet security, and distributed domain name server services. Headquartered in San Francisco, Cloudflare sits in front of millions of Internet applications, acting as a reverse proxy between visitors and customer infrastructure.

## AI Security Research

Cloudflare has been an active participant in [[concepts/claude-mythos-glasswing|Project Glasswing]], Anthropic's restricted-release program for the [[entities/claude-mythos|Claude Mythos Preview]] cyber frontier model. Cloudflare pointed Mythos Preview at over fifty of their own repositories — spanning runtime, edge data path, protocol stack, control plane, and open-source dependencies — to evaluate its vulnerability discovery capabilities.

### Key Contributions (May 2026)

- Published a detailed firsthand account of testing Mythos Preview at scale: *"Project Glasswing: what Mythos showed us"* (Grant Bourzikas, May 18, 2026)
- Developed a multi-stage **vulnerability discovery harness** with Recon → Hunt → Validate → Gapfill → Dedupe → Trace → Feedback → Report stages
- Identified critical lessons: narrow scope produces better findings, adversarial review reduces noise, splitting the chain across agents improves reasoning
- Documented the **signal-to-noise problem** with AI vulnerability scanners and how to address it
- Demonstrated that generic coding agents are the wrong tool for high-coverage vulnerability research

## Harness Architecture (Cloudflare's Design)

Cloudflare's vulnerability discovery harness operates as an orchestration layer around the LLM, not a chat interface:

| Stage | Function |
|-------|----------|
| **Recon** | Agent reads repo top-down, fans out to subagents, produces architecture doc with trust boundaries and attack surface |
| **Hunt** | ~50 concurrent hunter agents, each with one attack class + scope hint, with PoC compilation/execution tools |
| **Validate** | Independent agent with different prompt/model tries to disprove findings — adversarial review |
| **Gapfill** | Uncovered areas re-queued for another pass |
| **Dedupe** | Same root cause findings collapsed into single record |
| **Trace** | Tracer agent fans out per consumer repo, uses cross-repo symbol index for reachability analysis |
| **Feedback** | Reachable traces become new hunt tasks; pipeline improves as it runs |
| **Report** | Structured report against predefined schema, submitted to ingest API |

## Architecture Principles for AI-Era Security

Cloudflare advocates that "patching faster" is not enough. The harder question is the architecture around the vulnerability:

1. **Defenses in front of the application** that block bugs from being reached
2. **Application design** where a flaw in one part cannot give access to other parts
3. **Simultaneous rollout** of fixes to every deployment point, not per-team staggered releases

## Related

- [[concepts/claude-mythos-glasswing]] — Project Glasswing, which Cloudflare participated in
- [[entities/claude-mythos]] — The Mythos Preview model tested
- [[concepts/ai-vulnerability-detection-at-scale]] — Broader concept of AI-powered vulnerability discovery
- [[entities/anthropic]] — Model provider and Glasswing organizer
- [[entities/mozilla]] — Another Glasswing participant with Firefox hardening results
- [[concepts/cyber-frontier-models]] — The class of security-focused frontier models
