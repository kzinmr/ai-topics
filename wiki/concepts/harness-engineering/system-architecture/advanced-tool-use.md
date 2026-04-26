---
title: "Advanced Tool Use"
type: concept
aliases:
  - advanced-tool-use
  - tool-search-tool
  - programmatic-tool-calling
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-architecture
  - harness-engineering
  - anthropic
  - mcp
status: draft
sources:
  - "https://www.anthropic.com/engineering/advanced-tool-use/"
---

# Advanced Tool Use

AnthropicがClaude Developer Platformでリリースした、大規模ツール使用を可能にする3つの新機能。

## 問題意識

> "The future of AI agents is one where models work seamlessly across hundreds or thousands of tools."

従来のツール呼び出しはスケールすると以下の問題に直面：
- **コンテキスト飢餓**: すべてのMCP定義を事前にロードすると、最初のリクエスト前に50K〜134K+トークンを消費
- **推論オーバーヘッド**: 各ツール呼び出しにフルモデルパスが必要。中間結果がコンテキストを汚染
- **スキーマの限界**: JSONは構造を定義するが、使用規約やパラメータの相関、フォーマット期待値は定義できない

## 3つの新機能

### 1. Tool Search Tool

**解決する問題**: 大規模ライブラリにおけるコンテキスト膨張と誤ったツール選択

**仕組み**:
- `"defer_loading": true` でツールを初期コンテキストから除外
- Claudeが検索ツール（regex、BM25、カスタム埋め込み）を使用してオンデマンドで関連ツールを発見
- マッチしたツールのみがコンテキストに展開。プロンプトキャッシュは維持される

**実装例**:
```json
{
  "tools": [
    {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
    {
      "name": "github.createPullRequest",
      "description": "Create a pull request",
      "input_schema": {...},
      "defer_loading": true
    }
  ]
}
```

**MCPサーバー設定**:
```json
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-drive",
  "default_config": {"defer_loading": true},
  "configs": {
    "search_files": {"defer_loading": false}
  }
}
```

**効果**:
- コンテキスト消費を85%削減（191,300トークン vs 122,800トークンの従来アプローチ）
- 大規模ツールライブラリでのMCP評価で精度が大幅に向上（Opus 4で顕著）

**いつ使うべきか**:
| ✅ 最適 | ❌ 不要 |
|---|---|
| 10Kトークン以上のツール定義 | 10未満のツールまたはコンパクトな定義 |
| 類似ツール名での精度問題 | すべてのツールが毎セッション使用される |
| マルチサーバーMCPアーキテクチャ | |

### 2. Programmatic Tool Calling (PTC)

**解決する問題**: 中間結果によるコンテキスト汚染と推論遅延

**仕組み**:
- ClaudeがPythonオーケストレーションコードを記述し、シーケンシャルAPI呼び出しの代わりに実行
- コードはサンドボックス化された`code_execution`環境で実行
- ツール結果はプログラム的に処理され、**最終出力のみ**がClaudeのコンテキストに入る

**オーケストレーション例**:
```python
team = await get_team_members("engineering")
levels = list(set(m["level"] for m in team))
budget_results = await asyncio.gather(*[
    get_budget_by_level(level) for level in levels
])
budgets = {level: budget for level, budget in zip(levels, budget_results)}
expenses = await asyncio.gather(*[
    get_expenses(m["id"], "Q3") for m in team
])
exceeded = []
for member, exp in zip(team, expenses):
    budget = budgets[member["level"]]
    total = sum(e["amount"] for e in exp)
    if total > budget["travel_limit"]:
        exceeded.append({"name": member["name"], "spent": total, "limit": budget["travel_limit"]})
print(json.dumps(exceeded))
```

**APIフロー**:
1. オプトイン: `"allowed_callers": ["code_execution_20250825"]`
2. Claudeが`server_tool_use`とコードブロックを返す
3. APIがコードを実行、ツール呼び出しで一時停止、結果をサンドボックスに返す
4. 最終的な`code_execution_tool_result`（stdout）のみがClaudeのコンテキストに入る

**効果**:
- 200KBの生データ→1KBの結果に削減
- トークン消費: 43,588→27,297トークン（37%削減）
- 遅延: 各APIラウンドトリップ（数百ms〜数秒）を排除

**いつ使うべきか**:
| ✅ 最適 | ❌ 不要 |
|---|---|
| 集計/要約が必要な大規模データセット | 単一ツールの単純な呼び出し |
| 3つ以上の依存ツール呼び出し | 中間推論が必要なタスク |
| フィルタリング、ソート、並列操作 | 小さなレスポンスの簡易検索 |

### 3. Tool Use Examples

**解決する問題**: JSONスキーマの曖昧さと不正確なパラメータ使用

**仕組み**:
- ツール定義に`"input_examples"`配列を追加し、実際の使用パターンを示す
- フォーマット規約、ネストされた構造パターン、パラメータの相関を教える

**実装例**:
```json
{
  "name": "create_ticket",
  "input_schema": {...},
  "input_examples": [
    {
      "title": "Login page returns 500 error",
      "priority": "critical",
      "labels": ["bug", "authentication", "production"],
      "reporter": {"id": "USR-12345", "name": "Jane Smith", "contact": {"email": "jane@acme.com", "phone": "+1-555-0123"}},
      "due_date": "2024-11-06",
      "escalation": {"level": 2, "notify_manager": true, "sla_hours": 4}
    },
    {"title": "Add dark mode support", "labels": ["feature-request", "ui"], "reporter": {"id": "USR-67890", "name": "Alex Chen"}},
    {"title": "Update API documentation"}
  ]
}
```

**効果**:
- 内部テストで、従来のツール使用パターンでは不可能だった構築が可能に
- Claude for ExcelはPTCを使用して、数千行のスプレッドシートをコンテキストウィンドウをオーバーロードせずに読み取り/修正

**いつ使うべきか**:
| ✅ 最適 | ❌ 不要 |
|---|---|
| 複雑なネスト構造 | 単一パラメータの単純なツール |
| 使用パターンを持つ多くのオプションパラメータ | 標準フォーマット（URL、メール） |
| ドメイン固有の規約または類似ツール | スキーマ制約でより良く処理される検証 |

## 戦略的ベストプラクティス

1. **ボトルネック別にレイヤー**: 主要な制約を解決する機能から始め、その後組み合わせる
   - コンテキスト膨張 → Tool Search Tool
   - 中間結果の汚染 → Programmatic Tool Calling
   - スキーマの曖昧さ → Tool Use Examples
2. **段階的導入**: 一度にすべてを導入せず、問題に応じて追加
3. **評価ベースの改善**: 各機能の効果を測定し、必要に応じて調整

## 関連概念

- [[harness-engineering]] — 上位インデックス
- [[harness-engineering/system-architecture/writing-tools-for-agents]] — エージェント用ツール設計の5原則
- [[context-engineering]] — コンテキストエンジニアリング
