# sigstore-a2a: Keyless Signing for A2A AgentCards

**URL:** https://github.com/sigstore/sigstore-a2a
**Retrieved:** 2026-04-27
**Source:** Sigstore (GitHub)

## Overview

A Python library and CLI for keyless signing of A2A (Agent-to-Agent) AgentCards using Sigstore and SLSA provenance. Provides cryptographic identity verification for agent cards, enabling trust in agent origins across organizational boundaries.

## Key Features

- **Keyless signing** of A2A AgentCards via Sigstore's Fulcio CA (OIDC-based)
- **SLSA provenance generation** linking AgentCards to source repositories and build workflows
- **Identity verification** for trust in agent origins
- **Discovery integration** for serving signed cards at well-known endpoints

## Agent Card Structure

Extended AgentCard with `verificationMaterial`:

```json
{
  "agentCard": {
    "protocolVersion": "0.2.9",
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
      "timestamp": "2024-01-01T00:00:00Z"
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

## Verification Flow

1. Signer obtains OIDC token from CI/CD environment (e.g., GitHub Actions, GitLab CI)
2. Token is authenticated with Sigstore's Certificate Authority (Fulcio)
3. A short-lived X.509 certificate is issued embedding OIDC claims (repository, workflow, commit SHA, actor)
4. The AgentCard is signed; the signature, certificate, and transparency log entry (Rekor) are bundled
5. The transparency log provides public auditability and permanent verifiability
6. Verifier checks signature validity + identity claims

## Status

Prototype code – not for production use. No security audit. License: Apache 2.0.
