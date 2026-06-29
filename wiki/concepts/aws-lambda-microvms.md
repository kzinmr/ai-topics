---
title: "AWS Lambda MicroVMs"
type: concept
created: 2026-06-29
updated: 2026-06-29
tags:
  - aws
  - serverless
  - microvm
  - firecracker
  - sandbox
  - ai-agents
  - infrastructure
  - isolation
  - multi-tenancy
  - virtualization
status: full
aliases: ["lambda-microvms", "aws-lambda-microvms"]
sources:
  - "https://aws.amazon.com/jp/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/"
  - raw/articles/2026-06-22_aws-lambda-microvms-announcement.md
---

# AWS Lambda MicroVMs

AWS Lambda MicroVMs is a new serverless compute primitive within AWS Lambda for running user- or AI-generated code in **isolated, stateful execution environments**. Built on Firecracker, it delivers VM-level isolation, snapshot-based near-instant launch/resume, and up to 8 hours of stateful session runtime — purpose-built for multi-tenant applications that need to safely execute untrusted code.

> **Announced**: 2026-06-22 | **GA Regions**: US East (N. Virginia, Ohio), US West (Oregon), Europe (Ireland), Asia Pacific (Tokyo) | **Architecture**: ARM64

## Why It Exists

Multi-tenant applications (AI coding assistants, interactive code environments, data analytics, vulnerability scanners, game servers) need per-user isolated execution environments. Existing options all carry tradeoffs:

| Approach | Isolation | Startup | Stateful | Long-Running |
|----------|-----------|---------|----------|-------------|
| **Full VM** | Strong | Minutes | Yes | Yes |
| **Containers** | Weak (shared kernel) | Seconds | Partial | Yes |
| **FaaS (Lambda Functions)** | Medium | ~100ms | No | No |
| **Lambda MicroVMs** | **Strong (Firecracker)** | **Snapshot-instant** | **Yes** | **Yes (up to 8hr)** |

## Architecture

### Three Core Capabilities

1. **VM-Level Isolation** — [[concepts/firecracker]] hardware virtualization. Each session runs in its own dedicated MicroVM with no shared kernel or resources between users.
2. **Rapid Launch and Resume** — Image-then-launch model:
   - Upload Dockerfile + code zip to S3
   - `create-microvm-image` builds, initializes, and takes a Firecracker snapshot
   - Subsequent `run-microvm` calls resume from snapshot (no cold boot)
3. **Stateful Execution** — Retains memory, disk, and processes across the session. Auto-suspend on idle, auto-resume on request.

### Resource Specs

| Dimension | Value |
|-----------|-------|
| vCPUs | Up to 16 |
| Memory | Up to 32 GB |
| Disk | Up to 32 GB |
| Max runtime | 8 hours |
| Architecture | ARM64 |
| Base image | `public.ecr.aws/lambda/microvms:al2023-minimal` |

### Workflow

```
[1] create-microvm-image
    Dockerfile + zip → S3 → Lambda builds/initializes → Firecracker snapshot saved
    ↓
[2] run-microvm
    Snapshot resumed → dedicated endpoint URL issued
    ↓
[3] Request traffic
    CLI generates short-lived token → X-aws-proxy-auth header on HTTPS requests
    ↓
[4] Idle policy
    maxIdleDurationSeconds → auto-suspend → next request auto-resumes
```

### Idle Policy Configuration

```json
{
  "maxIdleDurationSeconds": 900,
  "suspendedDurationSeconds": 300,
  "autoResumeEnabled": true
}
```

During suspension, memory and disk state are snapshotted and stored, reducing costs. On resume, application state is fully restored.

## Lambda Functions vs. Lambda MicroVMs

| Dimension | Lambda Functions | Lambda MicroVMs |
|-----------|-----------------|----------------|
| **Design philosophy** | Event-driven request-response | Multi-tenant isolated execution |
| **Workload** | Short, stateless | Long-running, stateful |
| **Target code** | Developer-written | **User-generated / AI-generated (untrusted)** |
| **Isolation** | Lambda execution environment | Firecracker VM isolation |
| **State** | None (cold start each time) | Memory + disk + process state preserved |
| **API surface** | Lambda API | **Lambda MicroVMs API (separate)** |

Complementary: build event-driven backbones with Lambda Functions; call Lambda MicroVMs for steps that require isolated untrusted code execution.

## Position in Agent Sandbox Ecosystem

Lambda MicroVMs represents AWS's entry into the AI agent sandbox market with a low-level, infrastructure-first primitive:

| Provider | Isolation | Startup | Stateful | Max Runtime | Notes |
|----------|-----------|---------|----------|-------------|-------|
| **AWS Lambda MicroVMs** | Firecracker microVM | Snapshot-instant | Yes | 8 hours | AWS-native, snapshot-based |
| **E2B** | Firecracker-based | Seconds | Yes | Hours | Managed API, SDK-centric |
| **Modal** | gVisor/Firecracker | Seconds | Yes | Hours | GPU support, Python SDK |
| **Daytona** | Firecracker | Seconds | Yes | — | OSS, dev-environment focused |
| **Docker Sandbox** | MicroVM (sandboxd) | Seconds | Yes | — | Docker Desktop integrated |
| [[entities/amazon-bedrock-agentcore]] **Code Interpreter** | Managed | Seconds | Partial | 8 hours | AgentCore platform-integrated |

## Relationship to Other AWS Services

- **[[concepts/firecracker]]** — Foundation technology. Powers 15T+ monthly Lambda invocations.
- **[[entities/amazon-bedrock-agentcore]]** — AgentCore is the higher-level platform. Its Code Interpreter provides managed sandboxing, but Lambda MicroVMs is the lower-level, more flexible primitive for custom sandbox implementations.
- **AWS Fargate** — Container-based isolation (same Firecracker technology, different API design).

## Use Cases

- AI coding assistant code execution
- Interactive code/analytics environments
- Vulnerability scanning
- User script execution (game servers, etc.)
- Multi-tenant SaaS customer code isolation

## References

- [Lambda MicroVMs Product Page](https://aws.amazon.com/lambda/lambda-microvms)
- [Lambda MicroVMs Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html)
- [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing)

## Related Pages

- [[concepts/firecracker]] — MicroVM foundation technology
- [[entities/amazon-bedrock-agentcore]] — AWS AgentCore platform
- [[concepts/sandbox]] — Agent Sandboxing overview
- [[concepts/docker-sandbox-microvm-api]] — Docker Sandbox MicroVM API
- [[comparisons/lambda-microvms-vs-agentcore]] — Lambda MicroVMs vs AgentCore — Isolation Primitive vs Managed Platform
- [[comparisons/agent-sandboxing]] — Agent Sandboxing comparison
