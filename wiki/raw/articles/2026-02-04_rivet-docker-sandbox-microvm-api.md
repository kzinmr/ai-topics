---
title: "We Reverse-Engineered Docker Sandbox's Undocumented MicroVM API"
source: "https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/"
author: "Nathan Flurry"
date: "2026-02-04"
scraped: "2026-04-30"
tags: [docker, sandbox, microvm, agent-infrastructure, rivet, security]
related_wiki:
  - concepts/docker-sandbox-microvm-api
  - entities/rivet-dev
  - entities/nathan-flurry
  - concepts/agent-sandboxing-patterns
---

# We Reverse-Engineered Docker Sandbox's Undocumented MicroVM API

**Author:** Nathan Flurry (CTO, Rivet)
**Date:** February 4, 2026
**URL:** https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/

---

## Executive Summary
Docker recently launched **Docker Sandboxes** to run AI coding agents safely. While the official CLI is restricted to whitelisted agents (Claude, Codex, etc.), Rivet has reverse-engineered the underlying **undocumented MicroVM API**. This allows developers to orchestrate any containerized workload within a secure, kernel-isolated MicroVM environment on their own infrastructure.

---

## 1. Containers vs. MicroVMs
Standard containers share the host's kernel, making them unsuitable for untrusted code execution. Docker Sandboxes utilize MicroVMs to provide a separate kernel for every instance.

| Feature | Docker Container | Docker Sandbox |
| :--- | :--- | :--- |
| **Security** | Shared kernel (namespaces) | Separate kernel (microVM) |
| **Untrusted code** | Not safe | **Safe** |
| **Network access** | Direct HTTP | Via filtering proxy |
| **Volumes** | Direct mount | Bidirectional file sync |
| **Platform** | Linux, macOS, Windows | **macOS, Windows only** |

---

## 2. The Undocumented `/vm` API
Docker's `sandboxd` daemon manages these VMs and listens on a local Unix socket: `~/.docker/sandboxes/sandboxd.sock`.

### Key Endpoints
* `GET /vm`: List all VMs
* `POST /vm`: Create a VM
* `DELETE /vm/{vm_name}`: Destroy a VM

### Creating a VM
To create a VM, send a POST request to the socket:
```bash
curl -X POST --unix-socket ~/.docker/sandboxes/sandboxd.sock \
  http://localhost/vm \
  -H "Content-Type: application/json" \
  -d '{"agent_name": "my-sandbox", "workspace_dir": "/path/to/project"}'
```

**The Response:**
The API returns a `socketPath`. This is a **per-VM Docker daemon**. Unlike standard Docker where all containers share one socket, each MicroVM has its own isolated daemon.

---

## 3. Running Code Inside the MicroVM
Because the MicroVM is completely isolated, you must manually load images into the VM's specific daemon before running them.

### Step-by-Step Workflow
1.  **Build & Archive:** Build the image on the host and save it as a `.tar`.
2.  **Load:** Load the tarball into the MicroVM's socket.
3.  **Run:** Execute the container using the VM-specific host path.

```bash
# Load into microVM
docker --host "unix://$VM_SOCK" load < /tmp/image.tar

# Run container with Proxy settings
docker --host "unix://$VM_SOCK" run -d --name my-container \
  -e HTTP_PROXY=http://host.docker.internal:3128 \
  -e HTTPS_PROXY=http://host.docker.internal:3128 \
  -e NODE_TLS_REJECT_UNAUTHORIZED=0 \
  my-image:latest
```

### Important Technical Details
*   **Networking:** Outbound traffic is routed through a filtering proxy at `host.docker.internal:3128`. It performs Man-in-the-Middle (MITM) on HTTPS for policy enforcement.
*   **Volumes:** Workspace syncing uses absolute paths; `-v "/path/to/project:/path/to/project"` works as expected.
*   **Requirements:** Requires **Docker Desktop 4.58+** on macOS or Windows (uses Apple Virtualization.framework or Hyper-V). Linux is currently unsupported.

---

## 4. Sandbox Agent SDK
To simplify this process, Rivet released the open-source [Sandbox Agent SDK](https://sandboxagent.dev). It automates the session lifecycle, image loading, and communication.

**Example Usage (TypeScript):**
```typescript
import { SandboxAgent } from "sandbox-agent";

const client = await SandboxAgent.connect({ baseUrl: "http://127.0.0.1:2468" });
await client.createSession("my-session", { agent: "claude" });
await client.postMessage("my-session", { message: "Fix the tests" });

for await (const event of client.streamEvents("my-session")) {
  console.log(event.type, event.data);
}
```

## Use Cases
*   **Untrusted Code Execution:** Running user-submitted scripts safely.
*   **AI Coding Agents:** Allowing LLMs to modify files and run commands with full permissions.
*   **Multi-tenant Plugins:** Isolating customer code in SaaS applications.
*   **Secure CI/CD:** VM-level isolation for build processes.
