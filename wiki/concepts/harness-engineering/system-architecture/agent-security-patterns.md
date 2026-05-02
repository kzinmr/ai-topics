---
title: "Agent Security Patterns"
type: concept
aliases:
  - agent-security
  - container-security
  - egress-proxy
  - secret-injection
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - architecture
  - harness-engineering
  - security
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
---

# Agent Security Patterns

エージェントが外部システムと安全に相互作用するための**セキュリティ制御パターン**。OpenAI Responses APIのコンテナ環境で実装されている。

## 3層のセキュリティ

### 1. サイドカーエグレスプロキシ

```
┌─────────────────────────────────────────────┐
│  Agent Container                            │
│  ┌─────────────┐    ┌──────────────────┐    │
│  │   モデル/    │ →  │  Sidecar Egress  │ →  外部API/インターネット
│  │  シェルコマンド│    │     Proxy        │    │
│  └─────────────┘    └──────────────────┘    │
│                          │                   │
│                    ポリシー適用               │
│                    - ドメイン許可リスト        │
│                    - アクセス制御             │
│                    - トラフィック観測         │
└─────────────────────────────────────────────┘
```

- **すべての**アウトバウンドリクエストが centralized policy layer を通過
- ドメインベースの許可リストでアクセス制御
- トラフィックの完全な観測性

### 2. ドメインスコープシークレットインジェクション

| 場所 | 見えるもの |
|------|-----------|
| **モデル/コンテナ** | プレースホルダー（例: `{{API_KEY}}`） |
| **エグレスプロキシ** | 実際のシークレット値（許可ドメインにのみ適用） |

```python
# モデルが使用するプロンプト内
prompt = "Call the API at https://api.example.com with key: {{API_KEY}}"

# エグレスプロキシが実行時に置換
actual_request = "Authorization: Bearer sk-actual-secret-value"
```

**利点**:
- シークレットがモデルコンテキストに露出しない
- 意図しないデータ流出を防止
- 許可された宛先にのみ適用

### 3. ネットワークポリシー

- **許可リストベース**: 明示的に許可されたドメインのみアクセス可能
- **最小権限の原則**: 必要な外部アクセスのみを許可
- **観測可能性**: すべてのトラフィックを監視・記録

## セキュリティリスクと対策

| リスク | 対策 |
|--------|------|
| シークレット漏洩 | ドメインスコープインジェクション |
| 意図しない外部アクセス | エグレスプロキシ + 許可リスト |
| データ流出 | トラフィック観測 + ポリシー適用 |
| 内部システムへのアクセス | ネットワーク分離 |

## 設計哲学

> "At the same time, giving containers unrestricted internet access can be risky: it can expose information to external websites, unintentionally touch sensitive internal or third-party systems, or make credential leaks and data exfiltration harder to guard against."

OpenAIは「制限されたネットワークアクセス」をデフォルトとし、必要な外部アクセスのみを明示的に許可するアプローチを採用。

## ベストプラクティス

1. **最小権限**: 必要なドメインのみ許可リストに追加
2. **シークレット分離**: プレースホルダー使用、直接埋め込み禁止
3. **監視**: すべてのエグレストラフィックを記録
4. **段階的公開**: 開発→テスト→本番でポリシーを厳格化

## 関連概念

- [[concepts/harness-engineering/system-architecture/container-context]] — セキュリティ制御が適用される実行環境
- [[concepts/harness-engineering/system-architecture/agent-loop-orchestration]] — セキュアなコマンド実行
-  — セキュリティ機能を提供する基盤API
## 参照

- [OpenAI: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- [[openai]] — OpenAI
