# Cloud Infrastructure Mapping Research Pattern

When the user asks to map a deployment architecture (e.g., Fly.io + Modal + Cloudflare) to a specific cloud provider (e.g., AWS), use this multi-source research pattern.

## Step 1: Find existing implementations

Search GitHub for prior art before designing from scratch:
```
web_search: "{technology} {cloud-provider} deployment github template"
web_search: "{technology} {cloud-provider} architecture"
```

Examples from Hermes → AWS:
- `JiaDe-Wu/sample-host-hermesagent-on-amazon-bedrock-agentcore` — AgentCore + Firecracker
- `JiaDe-Wu/sample-hermes-agent-on-aws-with-bedrock` — ECS + Bedrock
- `PaulCailly/hermes-deploy` — NixOS on EC2
- `unrealandychan/Hermes-Agent-Cloud` — Terraform multi-cloud

## Step 2: Identify the hardest component to map

In this case, Modal sandboxed execution was the hardest AWS equivalent. Target the most specialized component first:
```
web_search: "{cloud-provider} sandboxed code execution isolated container agent"
web_search: "{cloud-provider} {specialized-service} agent hosting 2026"
```

This surfaced:
- AWS Nitro Enclaves (hardware isolation, but EC2-only)
- Amazon Bedrock AgentCore (Firecracker microVMs, 125ms boot, per-session isolation)
- ECS Fargate Ephemeral Tasks (30-45s cold start, task-level isolation)
- AWS blog: "Secure Agent Sandboxes for Programmatic Tool Calling" (EKS Fargate/gVisor/Kata)

## Step 3: Extract service documentation

For each candidate service, extract the official docs:
```
web_extract: "https://docs.aws.amazon.com/{service}/latest/devguide/how-it-works.html"
web_extract: "https://aws.amazon.com/{service}/"
```

Key details to extract: isolation mechanism, cold start time, session lifetime, pricing model, integration points.

## Step 4: Structure as tiered comparison

Present the mapping as ascending tiers (simple → sophisticated) rather than a single "best" option:

| Tier | Philosophy | Services Used | Monthly Cost |
|---|---|---|---|
| 1 | VPS-equivalent | EC2 | $50-70 |
| 2 | Managed containers | ECS Fargate + Bedrock | $70-100 |
| 3 | Fully managed agent platform | AgentCore | $40-60 |

Include: architecture diagram (ASCII), component-by-component mapping table, cost comparison, design principle alignment table.

## Step 5: Cross-reference with the original architecture

Always map back to the original design principles from the source architecture. For Matt Palmer's approach the principles were:
- Agent not internet-accessible → private subnet / AgentCore
- Least-privilege secret injection → IAM boundaries
- Defense in depth → WAF + Cognito + ALB
- Complete code execution isolation → Firecracker / Nitro
- Persistent state → EFS / S3 / Memory

## Step 6: Follow-on discovery — subsidiary concept pages

Cloud infrastructure research often surfaces a related technical article that warrants its own concept page. When this happens:
1. **Save the discovered article as a raw article** (use the article's actual publication date, found via JSON-LD or meta tags)
2. **Create a subsidiary concept page** that goes deep on the specific technology (e.g., `concepts/programmatic-tool-calling.md` surfaced from sandbox research)
3. **Cross-link bidirectionally**: add wikilinks from the infrastructure concept page to the new concept page, and update the infrastructure page's `sources:` frontmatter
4. **Enrich the infrastructure page** with a dedicated subsection summarizing what the subsidiary concept adds to the architecture

Example: Researching AWS sandbox options → found AWS blog on Programmatic Tool Calling → created `concepts/programmatic-tool-calling.md` → added "Programmatic Tool Calling (PTC) Integration" section to `concepts/agent-hosting-aws.md`.

## Pitfall: Cost surprises

NAT Gateway is a hidden cost driver in private-subnet architectures (~$35/mo). AgentCore eliminates this. Always include network costs in comparisons.

## Pitfall: Tag taxonomy for new cloud products

When adding cloud-provider-specific product tags (e.g., `bedrock`, `fly-io`) to concept pages, check `wiki/SCHEMA.md` first — even tags that seem obvious may not be in the taxonomy yet. Product names go under the **Products** category. Add them to SCHEMA.md before the commit to avoid the round-trip.
