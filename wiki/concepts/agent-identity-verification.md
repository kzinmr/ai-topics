---
title: "Agent Identity & Verification (A2A Signed Agent Cards)"
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [agent-communication, security, protocol, identity, multi-agent]
sources:
  - raw/articles/crawl-2026-04-27-sigstore-a2a-keyless-signing.md
  - raw/articles/crawl-2026-04-27-agent-identity-verification-a2a-signed-agent-cards.md
---

# Agent Identity & Verification (A2A Signed Agent Cards)

Multi-agent systems spanning organizational boundaries require verifiable agent identity. The A2A (Agent-to-Agent) Protocol v1.0 addresses this with **Signed Agent Cards** — cryptographic identity verification for agent discovery and trust across organizational boundaries.

## Problem Statement

When Agent A discovers Agent B's Agent Card, it has no protocol-level mechanism to verify the card is authentic without Signed Agent Cards. Transport-layer trust (HTTPS, OAuth) covers authorization but not identity verification of the agent itself. This matters in:

- Open agent marketplaces where agents from different organizations interact
- Delegation chains where an agent acts on behalf of another
- Audit and compliance contexts requiring proof of which agent performed an action

## A2A Signed Agent Cards (v1.0)

The A2A Protocol v1.0 (April 2026) introduced **Signed Agent Cards** as a core feature:

- **Cryptographic identity verification**: Agent Cards are signed using Sigstore infrastructure (keyless, OIDC-based)
- **Provenance binding**: Cards link to source repositories and build workflows via SLSA provenance
- **Transparency logging**: Signatures are recorded in Rekor (public transparency log) for auditability
- **Discovery integration**: Signed cards served at well-known endpoints

### Agent Card Verification Material Structure

```json
{
  "agentCard": {
    "protocolVersion": "1.0",
    "name": "Example Agent",
    "description": "An example AI agent",
    "url": "https://example.com/agent",
    "version": "1.0.0",
    "capabilities": { ... },
    "skills": [ ... ]
  },
  "verificationMaterial": {
    "signatureBundle": {
      "signature": "base64-encoded-signature",
      "certificate": "-----BEGIN CERTIFICATE-----...",
      "transparencyLogEntry": { ... },
      "timestamp": "2026-04-27T00:00:00Z"
    },
    "provenanceBundle": {
      "provenance": {
        "subject": [ ... ],
        "runDetails": { ... },
        "buildDefinition": { ... }
      }
    }
  }
}
```

## Sigstore Integration for Agent Cards

The [sigstore/sigstore-a2a](https://github.com/sigstore/sigstore-a2a) library (Apache 2.0, Python) provides:

- **Keyless signing** using Sigstore's Fulcio CA (OIDC-based, no long-lived keys)
- **SLSA provenance** generation linking AgentCards to repos and build workflows
- **Verification** checking both signature validity and identity claims

### Signing Flow (CI/CD)

1. CI/CD environment obtains OIDC token (e.g., GitHub Actions with `id-token: write`)
2. Token authenticated with Sigstore's CA (Fulcio)
3. Short-lived X.509 certificate issued embedding OIDC claims (repo, workflow, commit SHA, actor)
4. AgentCard signed; signature, certificate, transparency log entry (Rekor) bundled together
5. Transparency log provides public auditability and permanent verifiability

## Relationship to Other Security Mechanisms

Unlike transport-layer trust (HTTPS/OAuth), Signed Agent Cards provide **agent-level identity** that persists across delegation chains. This is complementary to:

- **MCP security model** — tool-level authorization within an agent
- **ACP governance** — enterprise auditability and RBAC
- **OAuth 2.0** — user/application authorization, not agent identity

## Current Status (April 2026)

- A2A v1.0 with Signed Agent Cards is stable and production-ready
- sigstore/sigstore-a2a is prototype-stage (not audited)
- Open GitHub issue [#1672](https://github.com/a2aproject/A2A/issues/1672) proposes additional agent identity verification mechanisms beyond the base spec
- Multi-tenancy support allows a single endpoint to securely host many agents with distinct identities

## Related Concepts

- [[concepts/agent-communication-protocols]] — MCP vs A2A vs ACP protocol comparison
- [[concepts/agent-team-swarm/_index]] — Multi-agent coordination patterns requiring identity
- [[concepts/multi-agent-orchestration-patterns]] — How identity enables cross-org orchestration
- [[concepts/agent-swarms]] — Emergent swarm behavior with identity verification
