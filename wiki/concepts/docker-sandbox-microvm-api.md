---
title: "Docker Sandbox MicroVM API"
created: 2026-04-30
updated: 2026-04-30
tags: [sandbox, docker, microvm, agent-infrastructure, security]
aliases: ["docker-sandbox-microvm", "sandboxd-api", "docker-sandboxes"]
related: [[concepts/agent-sandboxing-patterns]], [[concepts/agent-sandboxing]], [[entities/rivet-dev]]
sources:
  - "https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/"
---

# Docker Sandbox MicroVM API

## Summary

Docker Sandboxes は AI コーディングエージェントを安全に実行するために Docker が提供している仕組み。公式 CLI は Claude、Codex などホワイトリスト化されたエージェントのみに制限されているが、**Rivet** が基盤となる undocumented な MicroVM API (`sandboxd`) をリバースエンジニアリングし、開発者が独自インフラ上で任意のコンテナワークロードをカーネル分離された MicroVM 環境で実行できるようにした。

## Containers vs. MicroVMs

| Feature | Docker Container | Docker Sandbox |
|---------|-----------------|----------------|
| **Security** | Shared kernel (namespaces) | Separate kernel (microVM) |
| **Untrusted code** | Not safe | **Safe** |
| **Network access** | Direct HTTP | Filtering proxy (MITM HTTPS) |
| **Volumes** | Direct mount | Bidirectional file sync |
| **Platform** | Linux, macOS, Windows | macOS, Windows only |

標準コンテナはホストカーネルを共有するため信頼できないコードの実行には適さない。Docker Sandbox は MicroVM により VM ごとに独立したカーネルを提供する。

## The Undocumented `sandboxd` API

`sandboxd` デーモンがローカルの Unix socket でリッスンしている:

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

レスポンスには **per-VM Docker daemon の socketPath** が含まれる。通常の Docker と異なり、各 MicroVM は独立したデーモンを持つ。

## Running Code Inside the MicroVM

1. **Build & Archive:** ホスト上でイメージをビルドし `.tar` として保存
2. **Load:** tarball を MicroVM の socket にロード
3. **Run:** VM 固有のホストパスでコンテナを実行

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

- 外部トラフィックは `host.docker.internal:3128` のフィルタリングプロキシ経由
- HTTPS に対して MITM (Man-in-the-Middle) を行い、ポリシー強制を実施
- ワークスペース同期は絶対パスを使用: `-v "/path/to/project:/path/to/project"`

### Requirements

- **Docker Desktop 4.58+** が必要 (macOS / Windows)
- Apple Virtualization.framework (macOS) または Hyper-V (Windows) を利用
- Linux は現在 **未サポート**

## Sandbox Agent SDK

Rivet がオープンソースで公開している [Sandbox Agent SDK](https://sandboxagent.dev) により、セッションのライフサイクル管理、イメージのロード、VM との通信を自動化できる。

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

- **Untrusted Code Execution:** ユーザー提出スクリプトの安全な実行
- **AI Coding Agents:** LLM が完全権限でファイル修正・コマンド実行
- **Multi-tenant Plugins:** SaaS アプリでの顧客コード分離
- **Secure CI/CD:** ビルドプロセスの VM レベル分離

## Comparison with Other Sandboxing Approaches

| Aspect | Docker Sandbox (MicroVM) | Browser Use (Unikraft) | gVisor | Firecracker |
|--------|-------------------------|----------------------|--------|-------------|
| **Isolation** | MicroVM (separate kernel) | Unikraft micro-VM | User-space kernel | Firecracker microVM |
| **Boot time** | ~seconds | <1s | Instant | <125ms |
| **Platform** | macOS, Windows | Linux (AWS) | Linux | Linux (KVM) |
| **Management** | sandboxd daemon | Unikraft scheduler | Container runtime | Firecracker API |
| **Status** | Undocumented API | Production | Production | Production |

詳細は [[concepts/agent-sandboxing-patterns]] を参照。

## Sources

- [We Reverse-Engineered Docker Sandbox's Undocumented MicroVM API](https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/) — Nathan Flurry (Rivet CTO), 2026-02-04
- [Docker Sandboxes Official Docs](https://docs.docker.com/sandbox/) — Docker
