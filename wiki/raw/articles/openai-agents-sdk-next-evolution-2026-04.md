---
title: "OpenAI Agents SDK Next Evolution (Sandbox GA)"
source: https://openai.com/index/the-next-evolution-of-the-agents-sdk/
published: 2026-04-15
scraped: 2026-04-16
tags: [article, openai, agents-sdk, sandbox, GA, harness, compute]
---

# The Next Evolution of the Agents SDK

**Source:** OpenAI Blog | **Date:** April 15, 2026 | **Package:** `openai-agents>=0.14.0`

## Overview
OpenAI released a major update to the **Agents SDK**, providing standardized, model-native infrastructure for building production-ready agents. The update enables agents to safely inspect files, run commands, edit code, and execute long-horizon tasks within controlled sandbox environments.

## Core Capabilities

### Enhanced Agent Harness
- **Model-Native Alignment:** Execution patterns optimized for frontier models, improving reliability on complex, multi-step workflows.
- **Configurable Architecture:** Supports custom memory, sandbox-aware orchestration, and Codex-like filesystem tools.
- **Standardized Integrations:**
  - Tool use via [MCP](https://modelcontextprotocol.io/)
  - Progressive disclosure via [Skills](https://agentskills.io/)
  - Custom instructions via [AGENTS.md](https://agents.md/)
  - Code execution via [Shell](https://developers.openai.com/api/docs/guides/tools-shell)
  - File edits via [Apply Patch](https://developers.openai.com/api/docs/guides/tools-apply-patch)
- **Design Philosophy:** Turnkey out-of-the-box, yet highly adaptable to custom tech stacks.

### Native Sandbox Execution
- **Out-of-the-Box Workspaces:** Agents can safely read/write files, install dependencies, and run tools in isolated environments.
- **Supported Providers:** Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel (Bring-Your-Own-Sandbox also supported).
- **Manifest Abstraction:** Ensures environment portability across providers. Enables:
  - Mounting local files & defining output directories
  - Direct integration with cloud storage: AWS S3, Google Cloud Storage, Azure Blob Storage, Cloudflare R2
- **Predictable Workspace Structure:** Standardizes input/output locations from local prototype to production deployment.

### Security, Durability & Scalability
- **Security:** Separates harness from compute to mitigate prompt-injection/exfiltration risks and isolate credentials from model-generated code.
- **Durability:** Externalized agent state enables **snapshotting & rehydration**. Failed/expired containers restore from checkpoints without losing run progress.
- **Scalability:** Supports dynamic sandbox provisioning, subagent routing to isolated environments, and parallelized execution across containers.

## Key Code Excerpt
*Demonstrates `SandboxAgent` setup, `Manifest` configuration, and secure execution via `Runner.run`.*

```python
# pip install "openai-agents>=0.14.0"
import asyncio
import tempfile
from pathlib import Path

from agents import Runner
from agents.run import RunConfig
from agents.sandbox import Manifest, SandboxAgent, SandboxRunConfig
from agents.sandbox.entries import LocalDir
from agents.sandbox.sandboxes import UnixLocalSandboxClient

async def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        dataroom = Path(tmp) / "dataroom"
        dataroom.mkdir()
        (dataroom / "metrics.md").write_text(
            """# Annual metrics
| Year | Revenue | Operating income | Operating cash flow |
| --- | ---: | ---: | ---: |
| FY2025 | $124.3M | $18.6M | $24.1M |
| FY2024 | $98.7M | $12.4M | $17.9M |
""",
            encoding="utf-8",
        )

        agent = SandboxAgent(
            name="Dataroom Analyst",
            model="gpt-5.4",
            instructions="Answer using only files in data/. Cite source filenames.",
            default_manifest=Manifest(entries={"data": LocalDir(src=dataroom)}),
        )

        result = await Runner.run(
            agent,
            "Compare FY2025 revenue, operating income, and operating cash flow with FY2024.",
            run_config=RunConfig(
                sandbox=SandboxRunConfig(client=UnixLocalSandboxClient()),
            ),
        )
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

## Customer Validation
> "The updated Agents SDK made it production-viable for us to automate a critical clinical records workflow that previous approaches couldn't handle reliably enough. For us, the difference was not just extracting the right metadata, but correctly understanding the boundaries of each encounter in long, complex records. As a result, we can more quickly understand what's happening for each patient in a given visit, helping members with their care needs and improving their experience with us."
> — **Rachael Burns**, Staff Engineer & AI Tech Lead, Oscar Health

## Pricing & Availability
- **Status:** Generally Available (GA)
- **Access:** OpenAI API
- **Pricing Model:** Standard API pricing (billed on tokens + tool use)

## Roadmap & Next Steps
- **Language Support:** Python (current) → TypeScript (planned)
- **Upcoming Features:** Code mode & subagents (rolling out to both Python & TS)
- **Ecosystem Expansion:** Additional sandbox providers, deeper third-party integrations

## Key Takeaways
- The Agents SDK now provides **model-native** infrastructure for production agents.
- **Sandbox execution** is a core feature, not an afterthought.
- The **Harness/Compute split** is a fundamental architectural principle.
- **Manifests** provide environment portability across providers.
- **Security** is built-in via isolation and credential separation.
- **Durability** via snapshotting and rehydration enables long-horizon tasks.
- **Scalability** via dynamic provisioning and subagent routing.
