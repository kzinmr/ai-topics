---
title: "Run isolated sandboxes with full lifecycle control: AWS Lambda introduces MicroVMs"
url: "https://aws.amazon.com/jp/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/"
source: aws-blog
published: 2026-06-22
fetched: 2026-06-29
tags: [aws, lambda, microvm, firecracker, sandbox, agent-infrastructure, serverless, isolation, virtualization]
---

# Run isolated sandboxes with full lifecycle control: AWS Lambda introduces MicroVMs

**Source**: [AWS News Blog](https://aws.amazon.com/jp/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/) (2026-06-22)

## Key Announcement

AWS Lambda MicroVMs — a new serverless compute primitive within AWS Lambda for running user/AI-generated code in isolated, stateful execution environments. VM-level isolation, near-instant launch/resume, direct lifecycle/state control, no infrastructure management. Powered by Firecracker (same tech powering 15T+ monthly Lambda invocations).

## Why It Exists

New class of multi-tenant apps need per-user isolated execution environments:
- AI coding assistants
- Interactive code environments
- Data analytics platforms
- Vulnerability scanners
- Game servers running user-supplied scripts

Existing tradeoffs:
- **VMs**: Strong isolation but minutes to start
- **Containers**: Seconds launch but shared-kernel, needs hardening for untrusted code
- **FaaS**: Event-driven request-response, not designed for long-running stateful sessions

## Three Core Capabilities

1. **VM-level isolation** — Firecracker, no shared kernel/resources between users
2. **Rapid launch and resume** — Image-then-launch model: Dockerfile + zip → Firecracker snapshot → near-instant resume from pre-initialized snapshot
3. **Stateful execution** — Retains memory, disk, processes across session; auto-suspend/resume on idle

## Technical Details

- **Image creation**: `create-microvm-image` — supply Dockerfile + code zip → Lambda builds, initializes, takes Firecracker snapshot
- **Launch**: `run-microvm` — pass image ARN + idle policy → dedicated endpoint URL returned
- **Auth**: Short-lived token via CLI, attach to HTTPS request via `X-aws-proxy-auth` header
- **Idle policy**: Configurable `maxIdleDurationSeconds`, `suspendedDurationSeconds`, `autoResumeEnabled`
- **Max runtime**: 8 hours total
- **Specs**: Up to 16 vCPUs, 32 GB memory, 32 GB disk per MicroVM
- **Architecture**: ARM64
- **Regions**: US East (N. Virginia, Ohio), US West (Oregon), Europe (Ireland), Asia Pacific (Tokyo)
- **Base image**: `public.ecr.aws/lambda/microvms:al2023-minimal`

## Key Differentiator from Lambda Functions

Lambda Functions = event-driven request-response
Lambda MicroVMs = multi-tenant isolated environments for untrusted code

Complementary: app uses Lambda Functions for event-driven backbone, calls Lambda MicroVMs for untrusted code execution.

## Pricing

Separate pricing from Lambda Functions — see AWS Lambda pricing page.
