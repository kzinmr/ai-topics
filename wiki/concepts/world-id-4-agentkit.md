---
title: "World ID 4.0 and AgentKit"
type: concept
created: 2026-04-27
updated: 2026-04-27
tags: [product, protocol, identity, security, cryptography, ai-agents, verification]
aliases: ["World ID 4.0", "AgentKit", "Proof of Human", "Worldcoin"]
sources:
  - raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md
---

# World ID 4.0 and AgentKit

## Overview

**World ID 4.0** is Sam Altman's "full-stack proof of human" identity infrastructure, unveiled in April 2026. It uses iris scanning (the **Orb**) to verify human identity cryptographically. **AgentKit** extends this infrastructure to AI agents, enabling them to carry cryptographic proof that they act on behalf of a verified human.

## World ID 4.0

### Core Technology
- **Iris scanning (Orb)** — physical device that scans iris patterns to generate a unique cryptographic identifier
- **"Full-stack proof of human"** — verifies identity from biometric capture through to application integration
- **18 million people** across **160 countries** have already scanned their irises at an Orb

### Enterprise Integrations

| Integration | Use Case |
|-------------|----------|
| **Tinder** | Verified-human badges for US users |
| **Zoom** | "Deep Face" cross-checks iris-scanned image, live selfie, and video frame |
| **DocuSign** | Attaching cryptographic proof-of-human to signatures |
| **Shopify** | Building on World ID infrastructure |
| **Okta** | Identity verification integration |
| **AWS** | Cloud identity layer |
| **Vercel** | Deploying on World ID |
| **Visa** | Payment verification |

## AgentKit

**AgentKit** enables AI agents to carry cryptographic proof that they act for a verified human principal. This solves the critical trust problem of "who (or what) is on the other end of an API call."

### Key Integrations
- **Vercel** — "human in the loop" verification live for agent deployments
- **Okta** — planning "Human Principal" for API authorization policies

### Significance
AgentKit represents the first practical infrastructure for **agentic identity** — the concept that AI agents need cryptographically verifiable credentials proving their authorization to act on behalf of a specific human or organization.

## Controversy

There is a notable tension at the core of World ID: Sam Altman sells humanity's verification layer while his company OpenAI has done more than perhaps any other organization to contaminate the internet with synthetic/AI-generated content, creating the very problem that World ID claims to solve.

## Related Pages

- [[entities/openai]] — Sam Altman is CEO of OpenAI; World ID is an Tools for Humanity project
- [[concepts/agent-sandboxing]] — Agent identity is a security prerequisite
- [[concepts/zero-trust-agentic-ai]] — Zero trust for agents requires identity verification
