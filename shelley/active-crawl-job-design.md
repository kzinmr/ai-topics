# Active Knowledge Crawling Job — 設計書

Originating conversation: cSFEO3U
Created: 2026-04-14
Revised: 2026-04-14 (v2 — ポリシーベース設計へ全面改訂)

---

## 1. 背景と動機

### 現状（受動的取り込み）

```
Newsletter email → process_email.py → raw/articles/ → Hermes が概念化
RSS feeds → blogwatcher-cli → inbox/rss-scans/ → Hermes が概念化
trending_topics.py → 検知レポート（通知のみ、取り込みなし）
```

**問題**: inboxに届くものしか知識化されない。ホットトピックの周辺にある重要概念（前提知識、関連技術、対立概念、歴史的文脈）は「誰かが記事を書いてそれがフィードに流れてくる」まで永遠に取り込まれない。

### 目標（能動的取り込み）

ユーザーが管理する**ホットトピック一覧**を起点に、ポリシーに従ってクローリング対象を管理し、知識を能動的に拡張する。

---

## 2. ホットトピック管理: `config/hot-topics.yaml`

x-accounts.yaml と同様の宣言的リスト。ユーザーが手動編集・ Hermes/Shelleyに編集指示する。

```yaml
# config/hot-topics.yaml
#
# 能動的クローリングの対象トピック定義。
# crawl_policy がクローリング動作を決定する。
#
# フィールド:
#   slug:           wikiページのconcepts/スラッグ (必須)
#   title:          表示名 (必須)
#   crawl_policy:   クローリングポリシー (必須)
#     - prerequisites: 前提概念を探して取り込む
#     - laterals:     横方向の関連概念を探して取り込む
#     - deepdive:     トピック自体の最新動向・事例を探して取り込む
#     - monitor:      新規取り込みなし。trendingレポートで監視のみ
#     - paused:       クローリング一時停止
#   priority:       high / medium / low (デフォルト: medium)
#   search_hints:   検索クエリのヒント (任意)
#   wiki_pages:     関連する既存wikiページ (任意、自動検出もする)
#   notes:          メモ (任意)
#   added:          追加日 (YYYY-MM-DD)
#   last_crawled:   最終クロール日 (ジョブが自動更新)

topics:

  # === エージェント構築・設計 ===

  - slug: context-engineering
    title: "Context Engineering"
    crawl_policy: prerequisites
    priority: high
    search_hints:
      - "context engineering LLM techniques"
      - "context window optimization strategies"
    wiki_pages:
      - concepts/context-engineering
      - concepts/ai-agent-engineering/context-engineering
      - concepts/ai-agent-engineering/context-compaction
    notes: "Karpathy提唱。前提としてtoken economics, attention mechanism等が必要か"
    added: 2026-04-14

  - slug: agentic-engineering
    title: "Agentic Engineering"
    crawl_policy: laterals
    priority: high
    search_hints:
      - "agentic engineering patterns 2026"
      - "AI coding agent workflows"
    wiki_pages:
      - concepts/agentic-engineering/_index
    notes: "22ページの大クラスタ。横方向の関連パラダイムを探索"
    added: 2026-04-14

  - slug: ai-agent-engineering
    title: "AI Agent Engineering (Anthropic/OpenAI)"
    crawl_policy: deepdive
    priority: high
    search_hints:
      - "building AI agents 2026 best practices"
      - "agent engineering patterns Anthropic OpenAI"
    wiki_pages:
      - concepts/ai-agent-engineering/_index
    notes: "19ページ。最新事例・ベストプラクティスの深掘り"
    added: 2026-04-14

  - slug: harness-engineering
    title: "Harness Engineering"
    crawl_policy: prerequisites
    priority: high
    search_hints:
      - "harness engineering agents runtime"
      - "agent harness design patterns"
    wiki_pages:
      - concepts/harness-engineering
      - concepts/ai-agent-engineering/harness-design-long-running-apps
      - concepts/ai-agent-engineering/effective-harnesses-for-long-running-agents
    added: 2026-04-14

  - slug: agent-team-swarm
    title: "Agent Team / Swarm"
    crawl_policy: laterals
    priority: medium
    search_hints:
      - "multi-agent swarm orchestration 2026"
      - "agent team coordination patterns"
    wiki_pages:
      - concepts/agent-team-swarm/_index
      - concepts/anthropic-managed-agents
      - concepts/openai-symphony
    added: 2026-04-14

  # === モデル・推論 ===

  - slug: local-llm
    title: "Local LLM Inference"
    crawl_policy: deepdive
    priority: medium
    search_hints:
      - "local LLM inference 2026 llama.cpp"
      - "GGUF quantization local deployment"
    wiki_pages:
      - concepts/local-llm
    added: 2026-04-14

  - slug: ai-evals
    title: "AI Evaluations"
    crawl_policy: laterals
    priority: high
    search_hints:
      - "AI evaluation frameworks 2026"
      - "LLM evals best practices"
    wiki_pages:
      - concepts/ai-evals
      - concepts/evaluation-flywheel
      - comparisons/eval-tools-comparison
    added: 2026-04-14

  # === メモリ・コンテキスト ===

  - slug: ai-memory-systems
    title: "AI Memory Systems"
    crawl_policy: prerequisites
    priority: medium
    search_hints:
      - "AI agent memory architecture design"
      - "LLM memory management patterns"
    wiki_pages:
      - concepts/ai-memory-systems
      - concepts/memory-systems-design-patterns
      - concepts/claude-memory
    added: 2026-04-14

  # === ブラウザ・サンドボックス ===

  - slug: death-of-browser
    title: "Death of Browser"
    crawl_policy: deepdive
    priority: medium
    search_hints:
      - "agentic browsing paradigm shift 2026"
      - "browser automation AI agents WebMCP"
    wiki_pages:
      - concepts/death-of-browser
    added: 2026-04-14

  - slug: sandbox
    title: "Agent Sandboxing"
    crawl_policy: laterals
    priority: medium
    search_hints:
      - "AI agent sandboxing isolation 2026"
      - "code execution sandbox gVisor MicroVM WASM"
    wiki_pages:
      - concepts/sandbox
      - comparisons/agent-sandboxing
    added: 2026-04-14

  # === パラダイム・思想 ===

  - slug: neurosymbolic-ai
    title: "Neurosymbolic AI"
    crawl_policy: prerequisites
    priority: medium
    search_hints:
      - "neurosymbolic AI hybrid reasoning 2026"
      - "neural symbolic integration"
    wiki_pages:
      - concepts/neurosymbolic-ai
      - concepts/illusion-of-thinking
    added: 2026-04-14

  - slug: dspy
    title: "DSPy / Declarative LM Programming"
    crawl_policy: deepdive
    priority: medium
    search_hints:
      - "DSPy declarative language model programming"
      - "Omar Khattab DSPy GEPA"
    wiki_pages:
      - concepts/dspy
    added: 2026-04-14

  # === 監視のみ ===

  - slug: ai-bubble-economics
    title: "AI Bubble Economics"
    crawl_policy: monitor
    priority: low
    wiki_pages:
      - concepts/ai-bubble-economics
    added: 2026-04-14

  - slug: ai-safety
    title: "AI Safety & Alignment"
    crawl_policy: monitor
    priority: low
    wiki_pages:
      - concepts/ai-agent-traps
      - concepts/ai-autonomy-debate
    added: 2026-04-14
```

### crawl_policy セマンティクス

| ポリシー | 動作 | 例 |
|---------|------|----|
| `prerequisites` | トピックを理解するための**前提概念**を探し、wikiに無ければ取り込む | context-engineering → "attention mechanism", "KV cache" |
| `laterals` | トピックと同階層の**横方向関連概念**を探し、wikiに無ければ取り込む | evals → "offline evaluation", "LLM-as-judge" |
| `deepdive` | トピック自体の**最新動向・事例・ベストプラクティス**を探し、raw取り込みと既存ページ更新 | local-llm → 最新ベンチマーク、新モデル対応 |
| `monitor` | クローリングなし。trendingレポートでの監視のみ | 関心はあるが積極的に取り込むほどではない |
| `paused` | 全く動作しない | 一時的に無効化 |

---

## 3. クローリングジョブ設計

### アーキテクチャ

```
┌─────────────────────────────────────────────────┐
│ shelley-active-crawl.timer (daily 11:00 UTC)      │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│ shelley client chat                               │
│                                                   │
│  Step 1: Load Policy                              │
│    config/hot-topics.yaml を読む                   │
│    crawl_policy が prerequisites/laterals/deepdive  │
│    かつ last_crawled が3日以上前のものを抽出       │
│    priority: high を優先                           │
│                                                   │
│  Step 2: Select Targets (最大3トピック)            │
│    ラウンドロビン：                                │
│    - highを毎日巡回、mediumを週次1-2回            │
│    - last_crawled が最も古いものから選択          │
│                                                   │
│  Step 3: Crawl per Policy                         │
│    各トピックについて crawl_policy に応じた動作:    │
│                                                   │
│    [prerequisites]                                 │
│      wiki_pages を読む → 前提概念を特定             │
│      → wikiに無いものをWeb検索 → 取り込み         │
│                                                   │
│    [laterals]                                      │
│      wiki_pages を読む → 横方向関連概念を特定       │
│      → wikiに無いものをWeb検索 → 取り込み         │
│                                                   │
│    [deepdive]                                      │
│      search_hintsで最新動向を検索                 │
│      → 良質ソースをraw取り込み                   │
│      → 既存ページ更新提案 or 新規ページ作成      │
│                                                   │
│  Step 4: Update State                             │
│    hot-topics.yaml の last_crawled を更新          │
│    wiki/index.md, wiki/log.md 更新                │
│    git commit & push                               │
│                                                   │
│  Step 5: Report (日本語)                          │
│    取り込んだ概念、理由、親トピックとの関係       │
└─────────────────────────────────────────────────┘
```

### スケジューリングロジック

```
毎日実行時:
  1. yamlを読み、アクティブなトピックを抽出 (policy ≠ monitor, paused)
  2. priority: high のうち last_crawled が最古のものを最大2つ選択
  3. priority: medium のうち last_crawled が最古のものを1つ選択
  4. 合計最大3トピック/日
  5. 各トピックで最奧2概念を取り込み → 1日最大6概念
```

これにより:
- high (6トピック) は約3日で巡回
- medium (7トピック) は約1週間で巡回
- monitor/paused はスキップ

---

## 4. 気をつけるべき点

### 4.1 品質ゲート — 「何でも取り込む」を防ぐ

| リスク | 対策 |
|--------|------|
| LLM幻覚で存在しない概念をギャップとして検出 | ギャップ候補は必ずWeb検索で実在確認。検索ヒットゼロなら棄却 |
| 低品質ソース（SEOスパム、AI生成記事） | ドメインホワイトリスト優先（arxiv, 購読ブログ群, 公式ドキュメント） |
| wikiの信号対雑音比崩壊 | **1トピックあたり最奧2概念**。少量高品質 |
| ソースなしでLLM知識だけでページ作成 | **ソース必須ルール**: raw/articles/ にソースが無い概念はページ化しない |

### 4.2 爆発防止 — ギャップは無限に広がる

| リスク | 対策 |
|--------|------|
| 前提の前提を再帰的に展開 | **深さ1のみ**。hot-topics.yamlに登録されたトピックの直接的な周辺のみ |
| ドメイン外へ脱線 | SCHEMA.mdのドメイン定義に厳密に従う |
| トピックの際限なき追加 | yamlはユーザー手動管理。ジョブは追加提案はするが勝手に追加しない |

### 4.3 ポリシーの明確な分離

| リスク | 対策 |
|--------|------|
| policy間で出力が混在（prerequisitesとdeepdiveで同じ概念を重複取り込み） | トピックごとに1つのpolicyのみ適用。交差しない |
| deepdiveが永遠に新規ページを作り続ける | deepdiveは原則既存ページ更新。新規は「明確に新しいサブトピック」のみ |

### 4.4 既存パイプラインとの整合

| リスク | 対策 |
|--------|------|
| email-watcher/Hermesとの重複取り込み | rawは `crawl-` プレフィックス。conceptsは生成前にwiki全体grep |
| git push競合 | 実行前に `git pull --rebase`、push失敗時リトライ |
| last_crawled更新のyaml書き換えが破損的 | yamlの該当フィールドのみ更新。ファイル全体を書き換えない |

### 4.5 コスト・レート制限

| リスク | 対策 |
|--------|------|
| LLMトークン消費 | 1日最奧3トピック×2概念 = 6概念上限 |
| スクレイプ負荷 | 1リクエスト/2秒以上。robots.txt尊重 |
| timeout | systemd TimeoutStartSec=300 (5分) |

### 4.6 監査可能性

| リスク | 対策 |
|--------|------|
| なぜ取り込まれたか不明 | log.mdに `Active Crawl [{policy}]: {parent} → {new_concept}` |
| ジョブ結果が見えない | systemd journal + 日本語サマリ通知 |
| hot-topics.yamlの変更履歴 | gitで追跡（config/はai-topicsリポに含まれる） |

---

## 5. 既存ジョブとの関係

| ジョブ | 頻度 | 役割 | 入力 | 出力 |
|--------|------|------|------|------|
| email-watcher | 常時 | 受動: newsletter → raw | Maildir | raw/, inbox/newsletters/ |
| blogwatcher-cli | 日次cron | 受動: RSS → scan report | OPML | inbox/rss-scans/ |
| **trending-topics** | 日次10:00 | 検知: トレンド分析 | inbox/*, raw/* | 通知レポート |
| **active-crawl** ✨ | **日次11:00** | **能動: ポリシーベース取り込み** | **hot-topics.yaml + wiki** | **concepts/, raw/articles/** |
| wiki-health | 週次月曜 | 保守: 品質チェック | wiki/* | 通知 |
| wiki-graph | 週次木曜 | 分析: 相互参照 | wiki/* | 通知 |

```
受動経路:  Email/RSS → inbox → Hermes → wiki          (既存)
能動経路:  hot-topics.yaml → policy判定 → web検索 → wiki  (新規) ✨
検知経路:  trending → レポート通知                      (既存)
保守経路:  wiki-health, wiki-graph → レポート通知      (既存)
```

---

## 6. 将来の拡張ポイント

1. **trending派生モード**: trendingレポートの「New Page Recommended」から自動的にhot-topics.yamlに候補提案（ユーザー承認後追加）
2. **ギャップ候補の永続化**: `inbox/crawl-candidates.md` に「取り込めなかったが有望な候補」を残し、次回以降に消化
3. **Hermes連携**: Shelleyが作った概念ページをHermesがレビュー・エンリッチ
4. **メトリクス**: 取り込み数/日、トピック別カバレッジ率の可視化
