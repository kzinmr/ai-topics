---
title: "Agent Sandboxing: Isolation Technologies for AI Agent Code Execution"
description: "Agent Sandboxingは、AIエージェントの動的コード実行を安全に隔离する技術譜。gVisor、FirecrackermicroVM、WASM等の隔离技術を整理。標準コンテナは共有カーネルのため不十分。"
created: 2026-04-20
updated: 2026-04-20
type: concept
status: complete
depth_tracking:
 created: 2026-04-20
 target_depth: concept-level
tags: [agent-security, sandboxing, isolation, firecracker, gvisor, capability-security]
sources:
 - raw/articles/agent-sandboxing-2026-northflank.md
related:
 - agentic-engineering
 - ai-agent-engineering
 - code-execution-with-mcp
---

# Agent Sandboxing: Secure Isolation Technologies

**Agent Sandboxing** は、AIエージェントが生成・実行するコードを安全に隔离する技術。AIエージェントは 개발者がレビューしていないコードを動的に生成するため、**標準コンテナでは不十分**（共有カーネルのため）。

## Why AI Agents Need Special Sandboxing

AIエージェントは従来のアプリケーションと本质的に異なる：

| 課題 | 説明 |
|------|------|
| **未レビューコード実行** | AIが生成したコードを人が事前に監査しない |
| **プロンプトインジェクション** | 悪意ある入力でエージェント操控のリスク |
| **スコープ滥用** | 侵害されたエージェントが想定アクセスを超える |
| **横方向移動** | 攻撃成功時にインフラ全体に波及 |
| **内部リスク** | エージェントが重要なシステムへの 程序アクセスを取得 |

## Isolation Technology Spectrum

### Docker Containers（プロセスク区画）
| 次元 | 評価 |
|------|------|
| **Isolation** | プロセスレベル（namespaces/cgroups使用） |
| **Kernel** | ホストと共有 |
| **リスク** | カーネル脆弱性 = コンテナエスケープ = ホストアクセス |
| **起動時間** | ミリ秒単位 |
| **オーバーヘッド** | 最小 |
| **用途** | 信頼済みコードのみ |

### gVisor（ユーザースペースカーネル）
| 次元 | 評価 |
|------|------|
| **Isolation** | Syscall interception（ユーザースペースで処理） |
| **Kernel attack surface** | 大幅に削減 |
| **起動時間** | 数秒 |
| **オーバーヘッド** | 10-30%（I/Oヘビー workloads） |
| **用途** | 計算ヘビー、I/O限定、AI workloads |

**How it works:** gVisorは`runsc`（runsc runtime）として実装され、syscallをユーザースペースで処理するため、ホストカーネルに触れない。

### Firecracker MicroVMs（ハードウェア隔离）
| 次元 | 評価 |
|------|------|
| **Isolation** | ハードウェアレベル（専用Linuxカーネル） |
| **Startup** | ~125ms |
| **Memory overhead** | <5 MiB |
| **密度** | 150 VMs/秒/ホスト |
| **用途** | マルチテナント、本番環境、 未信頼コード |

**使用事例:** AWS Lambda、AWS Fargateの隔离担保证拠

### Kata Containers（VM区画via VMM）
| 次元 | 評価 |
|------|------|
| **Isolation** | ハードウェアレベル（VMM経由） |
| **VMM options** | Firecracker, Cloud Hypervisor, QEMU |
| **Startup** | ~200ms |
| **Memory overhead** | 最小 |
| **用途** | Kubernetes workloads（VM安全 + コンテナワークフロー） |

## Quick Decision Guide

```
UNTRUSTED code            → Firecracker / Kata Containers（ハードウェア境界）
COMPUTE-HEAVY, I/O limited → gVisor（強い隔离 + 较低オーバーヘッド）
TRUSTED internal automation → Hardened containers（seccomp, AppArmor, capability dropping）
```

## Implementation Requirements

### Resource Limits
| Resource | Mitigation |
|----------|------------|
| **CPU** | Maximum shares設定、暴走プロセス스로rottling |
| **Memory** | 超過時终止のハード制限 |
| **Disk** | Quotas + I/O rate limiting |
| **Network** | Outbound流量抑制、送信データ監視 |

### Network Controls（Zero-Trust Model）
- **Egress filtering:** デフォルト全遮断; 必要なエンドポイントのみ許可
- **DNS restrictions:** C2通信防止のための解決制限
- **Network segmentation:** agentネットワークとproductionシステムの分離

### Permission Scoping
| Pattern | Description |
|---------|-------------|
| **Short-lived credentials** | タスクごとにスコープ限定の一時トークン |
| **Tool-specific permissions** | read-only vs write accessの分離 |
| **Human-in-the-loop** | 金融取引、データ削除等高リスク操作は承認要 |

## Programmatic Tool Calling (PTC) Pattern

PTCは従来の逐次的なLLM-agentループを反転：LLMが**実行可能Pythonコードを生成**し、その中でツールを程序的に呼び出す（ループ、条件分岐、エラー処理等）。

| アプローチ | LLM呼び出し数 |
|-----------|-------------|
| Traditional Loop | 10+ round-trips |
| PTC | 1 invocation |

**PTCのsandbox要件:**
- 双方向通信（sandboxがツールリクエスト送信、結果をmid-executionで受信）
- 长寿命実行（複数の逐次ツール呼び出しを伴うコードブロック全体）
- 媒介されたツール呼び出し（orchestratorが全てintercept、sandboxに直接凭证やネットワークアクセスなし）

## Common Vulnerabilities & Mitigations

| 攻撃 | 缓解策 |
|------|--------|
| **プロンプトインジェクション** | 入力バリデーション、プロンプトフィルタリング、sandboxed tool execution |
| **コード生成エクスプロイト** | ネットワークアクセスなし、最小権限のisolated containers |
| **コンテキストポイズニング** | コンテキストデータの暗号学的検証、不変ストレージ |
| **ツール滥用** | ポリシー实施ゲート、高リスク操作の人間承認 |

## Capability-Based Security Model

Northflankのモデルが示す通り、**capability-based security**がクリーン：

> エージェントは渡された特定のバインディングのみアクセス可能。ファイルシステムなし、環境変数なし、ネットワークアクセスなし。

```python
# Capability-based tool definition
tools = [
    {
        "name": "read_file",
        "capability": "files:read",
        "allowed_paths": ["/data/input"],
        "constraints": {"max_size": "10MB"}
    },
    {
        "name": "http_request",
        "capability": "network:outbound",
        "allowed_domains": ["api.example.com"],
        "constraints": {"max_requests": 10}
    }
]
```

## See Also

- [[comparisons/agent-sandboxing]] — 隔离技術の比較表
- [[code-execution-with-mcp]] — MCPによるコード実行パターン
- [[agentic-engineering]] — エージェント工学全般
- [[ai-agent-engineering]] — Anthropic/OpenAIのエージェント設計