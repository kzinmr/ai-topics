---
title: "Docker Sandbox MicroVM API"
created: 2026-04-30
updated: 2026-05-26
tags:
  - sandbox
  - developer-tooling
  - ai-agents
  - security
aliases: ["docker-sandbox-microvm", "sandboxd-api", "docker-sandboxes"]
sources:
  - "https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/"
---


# Docker Sandbox MicroVM API

## Summary

Docker Sandboxes are Docker's mechanism for safely running AI coding agents. The official CLI is restricted to whitelisted agents (Claude, Codex, etc.), but **Rivet** reverse-engineered the underlying undocumented MicroVM API (`sandboxd`), enabling developers to run arbitrary container workloads in kernel-isolated MicroVM environments on their own infrastructure.

## Containers vs. MicroVMs

| Feature | Docker Container | Docker Sandbox |
|---------|-----------------|----------------|
| **Security** | Shared kernel (namespaces) | Separate kernel (microVM) |
| **Untrusted code** | Not safe | **Safe** |
| **Network access** | Direct HTTP | Filtering proxy (MITM HTTPS) |
| **Volumes** | Direct mount | Bidirectional file sync |
| **Platform** | Linux, macOS, Windows | macOS, Windows only |

Standard containers share the host kernel and are unsuitable for running untrusted code. Docker Sandbox provides an independent kernel per VM via microVMs.

## The Undocumented `sandboxd` API

The `sandboxd` daemon listens on a local Unix socket:

- **Socket path:** `~/.docker/sandboxes/sandboxd.sock`

### Key Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/vm` | List all VMs |
| `POST` | `/vm` | Create a new MicroVM |
| `DELETE` | `/vm/{vm_name}` | Destroy a VM |

### VM Creation

```bash
curl -X POST --unix-socket ~/.docker/sandboxes/sandboxd.sock \
  http://localhost/vm \
  -H "Content-Type: application/json" \
  -d '{"agent_name": "my-sandbox", "workspace_dir": "/path/to/project"}'
```

The response includes the **per-VM Docker daemon socketPath**. Unlike standard Docker, each MicroVM has its own independent daemon.

## Running Code Inside the MicroVM

1. **Build & Archive:** Build the image on the host and save it as `.tar`
2. **Load:** Load the tarball into the MicroVM socket
3. **Run:** Run the container using the VM-specific host path

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

### Networking Details

- External traffic goes through a filtering proxy at `host.docker.internal:3128`
- Performs MITM (Man-in-the-Middle) on HTTPS for policy enforcement
- Workspace sync uses absolute paths: `-v "/path/to/project:/path/to/project"`

### Requirements

- **Docker Desktop 4.58+** required (macOS / Windows)
- Uses Apple Virtualization.framework (macOS) or Hyper-V (Windows)
- Linux is currently **not supported**

## Sandbox Agent SDK

Rivet's open-source [Sandbox Agent SDK](https://sandboxagent.dev) automates session lifecycle management, image loading, and VM communication.

### TypeScript Example

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

- **Untrusted Code Execution:** Safe execution of user-submitted scripts
- **AI Coding Agents:** LLMs modify files and run commands with full permissions
- **Multi-tenant Plugins:** Customer code isolation in SaaS applications
- **Secure CI/CD:** VM-level isolation for build processes

## Comparison with Other Sandboxing Approaches

| Aspect | Docker Sandbox (MicroVM) | Browser Use (Unikraft) | gVisor | Firecracker |
|--------|-------------------------|----------------------|--------|-------------|
| **Isolation** | MicroVM (separate kernel) | Unikraft micro-VM | User-space kernel | Firecracker microVM |
| **Boot time** | ~seconds | <1s | Instant | <125ms |
| **Platform** | macOS, Windows | Linux (AWS) | Linux | Linux (KVM) |
| **Management** | sandboxd daemon | Unikraft scheduler | Container runtime | Firecracker API |
| **Status** | Undocumented API | Production | Production | Production |

Details in [[concepts/security-and-governance/agent-sandboxing-patterns]].

## Sources

- [We Reverse-Engineered Docker Sandbox's Undocumented MicroVM API](https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/) — Nathan Flurry (Rivet CTO), 2026-02-04
- [Docker Sandboxes Official Docs](https://docs.docker.com/sandbox/) — Docker
