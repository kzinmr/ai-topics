# Secure, Scalable Agent Sandbox Infrastructure
**Source:** Browser Use | **Author:** Larsen Cundric | **Date:** 2026-02-25

---

## 🎯 Core Problem & Architectural Shift
- **Initial Setup:** Ran millions of web agents on AWS Lambda (isolated, instant scaling). Added code execution (Python, shell, files) via an isolated sandbox tool.
- **Bottleneck:** Agent loop & REST API shared the same backend process. 
  - `Redeploy?` → All running agents die.
  - `Memory-hungry agent?` → API slows down.
  - **Result:** Two fundamentally different workloads sharing one process.
- **Security Challenge:** Agents running arbitrary code can access environment variables, API keys, database credentials, and internal services. Must be isolated from infrastructure and secrets.

---

## 🔍 The Two Sandboxing Patterns
| Pattern | Architecture | Pros/Cons |
|:---|:---|:---|
| **1. Isolate the tool** | Agent runs on backend infrastructure. Dangerous ops (code exec, terminal) run in a separate sandbox via HTTP. | Code runs somewhere with nothing to leak. Agent remains tied to backend lifecycle. |
| **2. Isolate the agent** | Entire agent runs in a sandbox with **zero secrets**. Talks to the outside world through a control plane holding all credentials. | Agent becomes disposable. No secrets to steal, no state to preserve. Can kill/restart/scale independently. |

> **Decision:** Started with Pattern 1, migrated to **Pattern 2**.

---

## 🛡️ Sandbox Implementation & Hardening
- **Unified Image:** Single container image runs everywhere. 
  - Production: [Unikraft](https://unikraft.cloud/) micro-VM (boots in <1s, provisioned via REST API on dedicated bare metal in AWS).
  - Dev/Evals: [Docker](https://www.docker.com) container.
  - Config switch: `sandbox_mode: 'docker' | 'ukc'`
- **Minimal Env Vars:** Only `SESSION_TOKEN`, `CONTROL_PLANE_URL`, and `SESSION_ID` are passed. No AWS keys, DB credentials, or API tokens.
- **Unikraft Features:** Scale-to-zero out of the box (suspend when idle, resume instantly). Distributed across multiple AWS metros to prevent bottlenecks.

### 🔒 Hardening Steps
1. **Bytecode-only execution:** Compile all Python source to `.pyc` during build, delete every `.py` file. Framework loads into memory as root; source is gone afterward.
2. **Privilege drop:** Entrypoint starts as root (to read root-owned bytecode), then immediately drops to a `sandbox` user via `setuid`/`setgid`.
3. **Environment stripping:** Read the 3 env vars into Python variables, then delete them from `os.environ`. Token is useless outside the sandbox's network. VM sits in a private VPC with permissions limited to talking to the control plane.

---

## 🌐 Control Plane Architecture
Acts as a **stateless proxy service**. Sandbox has no direct external access; all requests hop through the control plane.

- **Authentication:** Every request carries `Bearer: {session_token}` header. Control plane validates session & executes with real credentials.
- **LLM Proxying:** 
  - Sandbox sends only new messages.
  - Control plane owns full conversation history in DB, reconstructs context, and forwards to provider.
  - Keeps sandbox stateless (kill & restart without losing context).
  - Enforces cost caps & handles billing.
- **File Sync via Presigned URLs:**
  1. Sandbox detects changed files in `/workspace`
  2. Calls `POST /presigned-urls` with file paths
  3. Control plane generates scoped presigned S3 upload URLs
  4. Sandbox uploads directly to S3 without holding AWS credentials
  - Downloads work in reverse.
- **Gateway Protocol:**
  ```python
  class AgentGateway(Protocol):
      async def invoke_llm(self, new_messages, tools, tool_choice) -> LLMResponse: ...
      async def persist_messages(self, messages) -> None: ...
  ```
  - **Production:** `ControlPlaneGateway` (HTTP requests to control plane)
  - **Dev/Evals:** `DirectGateway` (direct LLM calls, in-memory history)
  - *Same interface, same behavior, different backend.*

---

## 📈 Scaling Strategy
- **Control Plane:** Stateless FastAPI service on ECS Fargate behind an ALB. Auto-scales based on CPU utilization.
- **Sandboxes:** Scale independently via Unikraft. Each session gets its own VM; Unikraft handles scheduling across metros.
- **Result:** Each layer scales based on its own bottleneck. Independent scaling prevents resource contention.

---

## ⚖️ Tradeoffs & Key Takeaway
- **Tradeoff:** Extra network hop on every operation + deploying 3 services instead of 1.
- **Impact:** Latency is negligible compared to LLM response times. Operational complexity is standard for ops teams.
- **Key Takeaway:** 
> *"your agent should have nothing worth stealing and nothing worth preserving."*
