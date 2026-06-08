---
title: Agent Hosting on AWS
created: 2026-05-29
updated: 2026-05-29
type: concept
tags:
  - aws
  - infrastructure
  - ai-agents
  - sandbox
  - isolation
  - architecture
  - security
  - agent-safety
  - comparison
aliases: [hermes-agent-aws-deployment, agent-hosting-architecture]
related: [concepts/agent-sandboxing, concepts/programmatic-tool-calling, entities/hermes-agent]
sources: [raw/articles/2026-05-26_matt-palmer_hermes-agent-deployment-fly-modal.md, raw/articles/2026-05-19_aws_ptc-bedrock-agentcore.md]
---

# Agent Hosting on AWS

How to map Matt Palmer's Fly.io + Modal + Cloudflare [[entities/hermes-agent]] deployment architecture to AWS infrastructure, as of May 2026.

## Architecture Mapping

| Matt Palmer Component | AWS Tier 1 (EC2) | AWS Tier 2 (ECS Fargate) | AWS Tier 3 (AgentCore) |
|---|---|---|---|
| **Hermes Gateway** | EC2 (t3.medium) | ECS Fargate (private subnet) | Bedrock AgentCore Runtime |
| **Chat UI** | Same EC2 + Docker | ECS Fargate / Express Mode | AgentCore Gateway + any UI |
| **Sandboxed Execution** | AWS Lambda | ECS Fargate Ephemeral Tasks | AgentCore Sessions (Firecracker microVM) |
| **Auth Gateway** | CloudFront + Lambda@Edge | Cognito + ALB Auth | Cognito / AWS Verified Access |
| **LLM Provider** | OpenRouter | Amazon Bedrock (IAM/SigV4) | Bedrock (native integration) |
| **Persistent Storage** | EBS | EFS | S3 + AgentCore Memory |

## Tier Comparison

### Tier 1: Simple EC2 (VPS-equivalent)

Single EC2 instance running Hermes Agent + Open WebUI via Docker. Closest to the "VPS approach" Matt explicitly rejected, but simplest to set up.

**Pros**: Familiar, one machine, existing OSS deployment tools available
**Cons**: Self-managed security, OS patching, no isolation between agent and terminal, Lambda limited to 15 minutes

**Existing OSS tools**: [PaulCailly/hermes-deploy](https://github.com/PaulCailly/hermes-deploy) (NixOS + sops), [unrealandychan/Hermes-Agent-Cloud](https://github.com/unrealandychan/Hermes-Agent-Cloud) (Terraform, AWS/Azure/GCP)

**Monthly cost**: ~$30-50 (EC2 t3.medium reserved + Lambda pay-per-use)

### Tier 2: ECS Fargate + Bedrock (closest to Matt's architecture)

Paradigm-aligned with Matt's managed-stack philosophy. Each component maps to an AWS managed service:

```
                    Internet → ALB (Public)
                                   │
                    ┌──────────────┼──────────────┐
                    │ Cognito      │               │
                    │ (OIDC Auth)  │               │
                    └──────────────┘               │
                                                   │
        ┌──────────────────────┐    ┌──────────────────────┐
        │ Open WebUI           │    │ Hermes Agent Gateway │
        │ ECS Fargate (Public) │───▶│ ECS Fargate (Private)│
        └──────────────────────┘    └──────────┬───────────┘
                                                │
                                    ┌───────────▼───────────┐
                                    │ Sandbox Executor      │
                                    │ ECS Ephemeral Tasks   │
                                    │ or Lambda             │
                                    └───────────┬───────────┘
                                                │
                                    ┌───────────▼───────────┐
                                    │ Amazon Bedrock        │
                                    │ (IAM auth, no API key)│
                                    └───────────────────────┘
```

**Key advantage over Matt's setup**: Amazon Bedrock eliminates API key management — IAM roles provide SigV4 authentication, every API call is audited via CloudTrail. [JiaDe-Wu/sample-hermes-agent-on-aws-with-bedrock](https://github.com/JiaDe-Wu/sample-hermes-agent-on-aws-with-bedrock) provides a CloudFormation template with Bedrock provider integration already built.

**Monthly cost**: ~$70-100 (Fargate × 2 + EFS + NAT Gateway is the main cost driver)

### Tier 3: Bedrock AgentCore (AWS-native peak)

The most sophisticated option. AgentCore Runtime hosts Hermes Agent directly on Firecracker microVMs — the same technology that powers AWS Lambda:

```
Telegram / Slack / Discord / Web
         │
    API Gateway / ALB
         │
    ┌─────▼──────────────────────┐
    │  Amazon Bedrock AgentCore  │
    │                             │
    │  AgentCore Runtime          │
    │  ┌─────┐ ┌─────┐ ┌───┐    │
    │  │VM 1 │ │VM 2 │ │VM3│    │  ← Firecracker microVM
    │  │UserA│ │UserB│ │Usr│    │    1 session = 1 VM
    │  └─────┘ └─────┘ └───┘    │    125ms boot time
    │                             │    Hardware-level isolation
    │  AgentCore Memory           │  ← Persistent (S3-backed)
    │  AgentCore Identity         │  ← Inbound/Outbound Auth
    │  AgentCore Gateway          │  ← MCP/A2A protocol support
    └─────────────────────────────┘
         │
    Amazon Bedrock (Claude)
```

**Why AgentCore replaces Modal entirely**:
- Firecracker microVM provides **hardware-level isolation** (KVM-based), same class as Modal
- 125ms cold start (Modal-equivalent)
- 8-hour session lifetime (vs Modal's similar limits)
- Memory hotplugging — scales within a session without restart
- Session termination = complete memory sanitization (no cross-session data leak)
- CPU billing only during active processing — I/O wait periods (waiting for LLM) are free

**Implementation exists**: [JiaDe-Wu/sample-host-hermesagent-on-amazon-bedrock-agentcore](https://github.com/JiaDe-Wu/sample-host-hermesagent-on-amazon-bedrock-agentcore) — Hermes + AgentCore integration with Firecracker microVMs, Bedrock Claude via SigV4 auth, CDK-based deployment (8 stacks).

**Monthly cost**: ~$40-60 (consumption-based, no NAT Gateway needed, no idle resource billing)

## Sandbox Execution Options (Modal Replacement)

This is the most critical design decision. AWS offers four tiers of code execution isolation:

| | Lambda | ECS Fargate Ephemeral | AgentCore Firecracker | Nitro Enclaves |
|---|---|---|---|---|
| **Cold start** | ~100ms | 30-60s | ~125ms | Seconds |
| **Max runtime** | 15 min | Unlimited | 8 hours | Unlimited |
| **Isolation level** | Container (gVisor) | Task-level | **Hardware (microVM)** | **Hardware (dedicated CPU+mem)** |
| **Network isolation** | VPC | VPC + SG | **Fully air-gapped** | **No external networking** |
| **Ephemeral storage** | /tmp (10GB) | 20GB | Session storage | None |
| **Operational burden** | Lowest | Medium | **Zero (managed)** | High (EC2 required) |
| **Best for** | Simple, short scripts | Long-running, package-heavy | **Interactive agent sessions (Modal equivalent)** | Maximum-security workloads |

### AgentCore Firecracker — Recommended

The closest AWS equivalent to Modal. Each user session gets its own Firecracker microVM with:
- Own Linux kernel (hardware-level isolation via KVM)
- 125ms boot time, ~5MB memory overhead
- 5 new microVMs per CPU core per second (36-core server = 180/sec)
- Auto-scaling: horizontal only (new VMs, not bigger VMs)

### AWS Official Sandbox Guidance

AWS published "[Secure Agent Sandboxes for Programmatic Tool Calling on AWS](https://aws.amazon.com/blogs/containers/)" detailing three EKS-based approaches:
- **EKS Fargate**: Each pod gets dedicated kernel, serverless, 30-45s cold start
- **gVisor**: User-space kernel, sub-5s startup, NetworkPolicy enforcement
- **Kata Containers + Cloud Hypervisor**: microVM per pod, hardware-enforced isolation, full syscall compatibility

The reference implementation uses an NDJSON protocol over TCP between an orchestrator and sandbox pod, with the sandbox in a private subnet with no internet gateway, communicating only via VPC endpoints.

## Auth Layer Options

| Cloudflare Access Feature | AWS Equivalent |
|---|---|
| GitHub OAuth login | Cognito User Pools + GitHub IdP |
| ALB-level auth enforcement | ALB listener rule `authenticate-oidc` |
| Rate limiting | AWS WAF (attached to ALB) |
| Bot/DDoS protection | AWS Shield + WAF |
| Custom domain | CloudFront + ACM certificate |

**Note**: CloudFront + WAF in front of ALB provides edge-level protection equivalent to Cloudflare. Alternatively, keep Cloudflare Access and point the CNAME to the AWS ALB — Cloudflare is cloud-agnostic.

## Cost Comparison (Monthly Estimate)

| Resource | Tier 1 (EC2) | Tier 2 (ECS) | Tier 3 (AgentCore) |
|---|---|---|---|
| Compute | EC2 t3.medium: ~$30 | Fargate 0.5vCPU/1GB × 2: ~$35 | AgentCore consumption: ~$20-40 |
| Sandbox | Lambda: ~$5 | Fargate Tasks: ~$10 | Included |
| Auth | Cognito: free tier | Cognito: free tier | AgentCore Identity: included |
| LLM | OpenRouter: ~$20 | Bedrock: ~$20 | Bedrock: ~$20 |
| Network | NAT Gateway: ~$35 | NAT Gateway: ~$35 | Not needed |
| **Total** | **~$50-70** | **~$70-100** | **~$40-60** |

NAT Gateway is a surprising cost driver in private-subnet architectures. AgentCore eliminates this entirely by managing network paths internally.

## Matt's Design Principles on AWS

| Principle | Matt's Implementation | AWS Equivalent |
|---|---|---|
| **Agent not internet-accessible** | Fly internal network | Private subnet + SG / AgentCore automatic |
| **Least-privilege secret injection** | Modal per-command secret pass-through | IAM role boundaries + Lambda/ECS task-level secrets |
| **Defense in depth** | Fly → Cloudflare → OIDC | Private subnet → ALB+Cognito → WAF+Shield |
| **Complete code execution isolation** | Modal Sandboxes | AgentCore Firecracker (HW isolation) or ECS Ephemeral Tasks |
| **Persistent state** | Fly persistent volume | EFS / S3 / AgentCore Memory |

## Recommendation

- **Quick start / evaluation**: Tier 2 ECS Fargate + Bedrock — closest paradigm match to Matt's approach, existing CloudFormation templates available
- **Production / long-term**: Tier 3 Bedrock AgentCore — purpose-built for this use case, zero server management, Firecracker isolation, cost-optimized billing
- **Avoid Tier 1 EC2** unless you have specific compliance requirements for self-managed infrastructure — it reintroduces the security surface area Matt deliberately avoided

## Programmatic Tool Calling (PTC) Integration

AWS published [[concepts/programmatic-tool-calling|Programmatic Tool Calling]] (May 2026) as the recommended approach for agent tool execution on Bedrock. PTC replaces sequential tool calling with code-orchestrated execution in sandboxes — directly relevant to the sandboxing layer in this architecture:

- **87-92% token reduction** vs traditional tool calling (across 8 Bedrock models)
- **3 implementation paths** map to our tiers:
  - Self-hosted ECS + Docker sandbox → Tier 2
  - AgentCore Code Interpreter (managed) → Tier 3
  - Anthropic SDK compatible proxy → Tier 2/3 hybrid
- **All 8 models produced correct results** in PTC mode; only Claude models were accurate in sequential mode
- **~90% monthly cost savings** ($15,600 → $1,560 at 1,000 executions/day)

See [[concepts/programmatic-tool-calling]] for the full paradigm, benchmarks, and implementation details.
