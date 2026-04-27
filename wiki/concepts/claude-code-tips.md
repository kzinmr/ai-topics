---
title: "Claude Code Tips — Running Inside Docker with VSCode Dev Containers"
type: concept
created: 2026-04-27
updated: 2026-04-27
tags: [concept, claude-code, docker, dev-containers, security, agent-sandboxing]
aliases: [claude-in-docker, claude-code-docker-setup]
sources:
  - "https://timsh.org/claude-inside-docker/"
  - "https://github.com/tim-sha256/claude-in-docker"
related:
  - concepts/claude-code-leak
  - concepts/agent-sandboxing
  - concepts/container-context
  - entities/claude-code
---

# Claude Code Tips — Running Inside Docker with VSCode Dev Containers

Running **Claude Code** inside a **Docker container** via VSCode's **Dev Containers** feature provides a practical balance between the power of Anthropic's CLI agent and security isolation. This approach gives Claude Code access to your project files while preventing it from accessing your broader filesystem, local secrets, or SSH keys.

## Why Run Claude Code in Docker?

### Security Isolation

Giving an AI agent terminal and filesystem access is inherently risky. Running Claude Code inside a container constrains what it can do:

- **Filesystem sandboxing** — Claude can only access files inside the container or mounted volumes. It cannot read your home directory, SSH keys, or system configuration.
- **No local credential exposure** — The container has no access to your local SSH keys, GPG keys, or credential stores. A separate GitHub fine-grained access token is used for git operations.
- **Contained blast radius** — The worst case is the container breaks or stops. Your host system remains unaffected.
- **Network access control** — External integrations (APIs, MCP servers, databases) require explicit setup inside the container rather than automatic access to the host's network.

### Performance and Cost

- **Claude Code's $20 Pro subscription** replaces more expensive setups (e.g., Cursor Pro at $40 total) while providing reasonable rate limits and clear token spending visibility.
- **No queue delays** — Unlike Cursor's post-update rate limits (2-5 minute waits for standard prompts), Claude Code provides fast response times.

### Practical Benefits

- **Works with any Claude subscription plan** — Pro or Max, the container setup is identical.
- **Quick setup** — 5 minutes if Docker and VSCode are already installed.
- **Familiar IDE experience** — VSCode with Dev Containers provides the same editor experience as working locally.

## Setup Guide

### Prerequisites

1. **Docker** installed and running
2. **VSCode** with the **Dev Containers** extension
3. **Claude subscription** (any paid plan)
4. **GitHub account** (for repository operations)

### Step 1: Create the Dev Container

Create a project folder with a `.devcontainer/devcontainer.json` file. You can either:

- **Clone the [reference repo](https://github.com/tim-sha256/claude-in-docker):**
  ```bash
  git clone https://github.com/tim-sha256/claude-in-docker.git
  ```

- **Create it manually** by placing a `devcontainer.json` inside a `.devcontainer/` folder. The reference implementation includes:
  - Node.js runtime (required by Claude Code CLI)
  - Git for version control
  - Claude Code CLI pre-installed
  - Any project-specific dependencies

### Step 2: Open in VSCode

Open the root folder in VSCode. A modal will appear: **"Reopen in Container"** — click it. VSCode builds the container image and opens the project inside the isolated environment. This takes a minute on first run.

### Step 3: Verify Claude Code

In the VSCode terminal inside the container, run:
```bash
claude
```

Claude Code starts in the container, with access only to the project files inside it.

### Step 4: Configure Git Access (Fine-Grained Token)

Inside the container, there are no SSH keys. Use a **GitHub fine-grained personal access token** instead:

1. Go to [GitHub Settings > Personal Access Tokens > Fine-grained tokens](https://github.com/settings/personal-access-tokens/new)
2. Select the repositories Claude Code needs access to
3. Under **Repository permissions**, set **Contents** to **Read and write**
4. This single permission is sufficient for basic git operations (clone, pull, push)

Use the token in git operations:
```bash
git clone https://<USERNAME>:<TOKEN>@github.com/<USERNAME>/<REPO>.git
cd <REPO>
git remote set-url origin https://<USERNAME>:<TOKEN>@github.com/<USERNAME>/<REPO>.git
```

This token approach is preferred over generating an SSH key inside the container, because:
- SSH keys can't be scoped to specific permissions — adding one for the container gives Claude unintended access to your account settings
- Fine-grained tokens can be limited to `Contents: Read and write` — the bare minimum for code operations

## Security Considerations

| Concern | Mitigation |
|---------|-----------|
| File system access | Container isolation — Claude can't access host files outside mounted volumes |
| SSH keys | Not present in container; fine-grained token replaces them |
| Secrets exposure | External integrations require explicit setup inside container |
| Malicious code execution | Container is disposable; rebuild to reset |
| GitHub account access | Token scoped to specific repos with read/write contents only |

## Comparison with Alternatives

| Approach | Security | Setup Complexity | Cost |
|----------|----------|-----------------|------|
| **Docker + Dev Container** (this guide) | High — container isolation | 5 minutes | $20/mo (Claude Pro) |
| **Claude Code locally** | Low — full filesystem access | 2 minutes | $20/mo (Claude Pro) |
| **Cursor Pro** | Medium — some built-in guards | 1 minute | $40/mo |
| **OpenAI Codex** | Low — runs locally | 2 minutes | $20/mo (ChatGPT Plus) |

## References

- [GitHub: claude-in-docker](https://github.com/tim-sha256/claude-in-docker) — Reference implementation
- [Original article: timsh.org](https://timsh.org/claude-inside-docker/) — "Switching to Claude Code + VSCode inside Docker"
- [[concepts/agent-sandboxing]] — Broader discussion of agent isolation techniques
- [[concepts/container-context]] — Container-based execution environments for agents
- [[entities/claude-code]] — Claude Code entity page
