---
title: "Code Execution with MCP"
type: concept
aliases:
  - code-execution-mcp
  - code-mode
  - mcp-code-execution
  - filesystem-tool-discovery
created: 2026-04-12
updated: 2026-05-01
tags:
  - concept
  - system-architecture
  - harness-engineering
  - anthropic
  - mcp
  - code-execution
status: draft
sources:
  - "https://www.anthropic.com/engineering/code-execution-with-mcp"
---

# Code Execution with MCP

MCP（Model Context Protocol）サーバーをコードAPIとして公開し、エージェントがコードを書いてツールを呼び出すパターン。Cloudflareの「Code Mode」と同じ核心洞察。

## 核心洞察

> "The core insight is the same: LLMs are adept at writing code and developers should take advantage of this strength to build agents that interact with MCP servers more efficiently."

**LLMはコードを書くのが得意。この強みを活かして、MCPサーバーとのやり取りを効率化する。**

## 問題: 直接ツール呼び出しのコンテキストオーバーロード

エージェントが数十/数百のMCPサーバーにスケールすると：
- **ツール定義の膨張**: すべてのツールスキーマを事前にロードすると、リクエスト処理前に巨大なコンテキストを消費
- **中間結果のトークン浪費**: 生出力（トランスクリプト、大規模データセット）がモデルコンテキストを複数回通過
  - 例: 2時間の営業会議トランスクリプトを2回処理 = **~50,000追加トークン**

## 解決策: MCPをコードAPIとして公開

MCPサーバーを構造化されたファイルシステムとして公開。エージェントがコードを書いてツールをオーケストレーションし、オンデマンドで定義をロード。

### 実装アーキテクチャ

```
servers
├── google-drive
│   ├── getDocument.ts
│   └── index.ts
├── salesforce
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

**ツール定義例**:
```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput { documentId: string; }
interface GetDocumentResponse { content: string; }

/* Read a document from Google Drive */
export async function getDocument(input: GetDocumentInput): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>('google_drive__get_document', input);
}
```

**エージェントワークフロー例**:
```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

## メリット

| メリット | 仕組み | インパクト |
|:---|:---|:---|
| **プログレッシブ開示** | エージェントがファイルシステムをナビゲートまたは`search_tools`で必要な定義のみをロード | 事前のコンテキスト膨張を排除 |
| **コンテキスト効率的な結果** | 実行環境でデータをフィルタ/変換してからモデルに返す | 10,000行のシート → 5行のみ返却 |
| **強力な制御フロー** | ネイティブなループ、条件分岐、エラーハンドリングがチェーン型ツール呼び出しを置換 | 「最初のトークンまでの時間」遅延を削減。ポーリング/リトライをクリーンに処理 |
| **プライバシー保護** | 中間データは実行環境内に留まる。MCPクライアントがPIIを自動トークン化 | 機密データがコンテキストに入らず安全にフロー |
| **状態永続化とスキル** | 中間結果をファイルに保存。再利用可能なコードを`./skills/` + `SKILL.md`として永続化 | ワークフローの再開と、エージェント能力の累積的向上 |

## トレードオフ

- **インフラオーバーヘッド**: 安全な実行環境（サンドボックス化、リソース制限、監視）が必要
- **直接呼び出しとの複雑さ**: 単純なツールルーティングよりも運用負担が増加
- **推奨**: トークン/遅延の削減効果と実装コストを比較検討。大規模データセット、複雑なワークフロー、厳格なプライバシー要件に最適

## キーメトリクス

| メトリクス | 値 |
|---|---|
| **トークン削減** | `150,000 → 2,000 tokens` (**98.7%節約**) |
| **MCP採用** | 2024年11月ローンチ。業界デファクトスタンダード。数千のコミュニティサーバー |
| **業界検証** | Cloudflareの「Code Mode」が同一の効率改善を実証 |

## 実践的提言

1. **直接ツール呼び出しからコード実行へシフト**: 数十のMCPサーバーを超える場合
2. **ファイルシステムベースのツールディスカバリ**: `search_tools`でプログレッシブコンテキストローディング
3. **コード内でデータフィルタ/集約**: モデルに返す前に
4. **MCPクライアントのトークン化パイプライン**: PII-heavyワークフローで活用
5. **再利用可能なロジックをスキルとして保存**: `SKILL.md` + コード。エージェント能力を時間とともに累積
6. **安全なサンドボックスへの投資**: エージェント生成コードを安全に実行

## 関連概念

- [[concepts/programmatic-tool-calling]] — 上位概念: LLMがコードを書いてツールを呼び出すAPIメカニズム。Code Execution with MCPはこのパターンのMCP版
- [[concepts/code-execution-with-mcp]] — 上位概念（ルートレベル）: MCPをコードAPIとして扱うアーキテクチャパターン
- [[concepts/code-mode]] — Cloudflare Code Mode (V8 MCP)、Pydantic Monty実装など具体的実装
- [[concepts/harness-engineering]] — 上位インデックス
- [[concepts/harness-engineering/system-architecture/advanced-tool-use]] — 高度なツール使用（PTCと関連）
- [[concepts/harness-engineering/system-architecture/writing-tools-for-agents]] — エージェント用ツール設計
- [[concepts/harness-engineering/system-architecture/building-effective-agents]] — エージェント構築の基本原理
