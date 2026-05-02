---
title: "Local-First Software"
type: concept
created: 2026-04-13
updated: 2026-04-13
status: draft
tags:
  - architecture
  - CRDT
  - data-ownership
  - offline-first
  - collaboration
  - event-sourcing
related:
  - martin-kleppmann
  - automerge
  - bluesky-at-protocol
  - local-llm
sources:
  - "https://martin.kleppmann.com/papers/local-first.pdf"
  - "https://localfirst.fm"
  - "https://electric-sql.com"
---

# Local-First Software

ユーザーのデバイスをデータの**第一権威コピー（primary authoritative copy）**とし、サーバーは同期・バックアップ・発見支援に限定するソフトウェア設計思想。

2019年に Ink & Switch の研究論文として提唱された。クラウド中心アーキテクチャ（REST API + サーバー権威モデル）が抱える「ネットワーク依存」「データ所有権欠如」「プライバシーリスク」「ベンダーロックイン」へのアンチテーゼ。

---

## The 7 Ideals of Local-First Software

| # | Ideal | 核心原則 |
|---|-------|----------|
| 1 | **No Spinners** | ローカルディスクI/Oで即時UI応答。ネットワーク遅延をバックグラウンド同期で隠蔽 |
| 2 | **Multi-Device** | シームレスなデバイス間同期。サーバーは二次コピー、権威はローカル |
| 3 | **Network Optional** | オフラインでも完全機能。同期はインターネット/BT/WiFi経由で後から |
| 4 | **Seamless Collaboration** | リアルタイム共同編集 + 非同期ワークフロー。自動競合解決 |
| 5 | **The Long Now** | ベンダー消滅後もデータ永続。"デジタル暗黒時代"の防止 |
| 6 | **Security & Privacy** | E2E暗号化デフォルト。集中型データハニーポットの排除 |
| 7 | **Ultimate Ownership** | ユーザーがデータをコピー・修正・バックアップ・削除できる（API/ToSに縛られない） |

---

## 既存アーキテクチャの分析

| 技術 | 強み | 弱み |
|------|------|------|
| **Files + Email** | 完全所有権、オフライン対応、長期保存、高速 | リアルタイム協調が不可、手動マージ、バージョン混沌 |
| **Web Apps** (Google Docs, Trello) | シームレスなリアルタイム協調、ゼロインストール | オフライン信頼性なし、所有権ゼロ、ベンダーロックイン |
| **Cloud Sync** (Dropbox, Drive) | 良いオフラインサポート、簡単バックアップ | リアルタイム協調時に競合コピー発生、モバイルはサーバー依存 |
| **Git/GitHub** | 優れた非同期協調、オフラインファースト、完全制御 | リアルタイム細粒度編集不可、非テキスト形式に弱い |
| **BaaS** (Firebase, CloudKit, Realm) | 簡単同期、良いオフラインキャッシング | プロプライエタリロックイン、プライバシー/長期性保証なし |
| **CouchDB/PouchDB** | マルチマスターレプリケーション、思想的整合 | 手動競合解決が非現実的、学習曲線急峻 |

---

## CRDTs: Local-First の基盤アルゴリズム

**Conflict-free Replicated Data Types (CRDTs)** は、分散・並行編集を前提に設計されたマルチユーザーデータ構造。

### 仕組み
- 複数デバイスが独立してデータを更新しても、同期時に決定論的にマージされる
- Gitの手動マージ不要。数学的に競合を自動解決
- 転送非依存（サーバー/P2P/Bluetooth/USB）
- 細粒度（キーストロークレベルのリアルタイム編集からバッチ非同期ワークフローまで）

### Kleppmannの位置づけ
> *"Just as packet switching was an enabling technology for the Internet... CRDTs may be the foundation for collaborative software that gives users full ownership of their data."*

### Ink & Switchプロトタイプの発見
1. **CRDTs は実用的に機能した** — 自動マージはシームレス
2. **オフラインUXは圧倒的に優れていた** — ユーザーが真の所有権を体感
3. **競合は稀** — 細粒度トラッキング + 人間の調整で最小化
4. **履歴可視化が重要** — 分散システムには「タイムトラベル」UIが必要
5. **URLが共有を可能にする** — WebスタイルのURLが文書発見に最適
6. **P2Pネットワークは未成熟** — NAT超えが信頼性に欠ける
7. **CRDT履歴肥大化** — 全キーストローク保存でメモリ/パフォーマンス劣化。GC/圧縮は未解決
8. **サーバーにも役割がある** — 権威としてではなく「クラウドピア」（発見・バックアップ・オフラインユーザーのブリッジ・バースト計算）

---

## エコシステムの発展（2019〜2026）

### 主要プロジェクト

| プロジェクト | 役割 | 備考 |
|-------------|------|------|
| **Automerge** | CRDTライブラリ | Kleppmann主導。JSON CRDT |
| **Yjs** | CRDTライブラリ | リッチテキスト共同編集で実績 |
| **ElectricSQL** | Postgres同期エンジン | PGlite(WASM Postgres in browser)と連携。2024年にv1.0-beta |
| **RxDB** | ローカルファーストDB | OPFS/IndexedDBベース。Web対応 |
| **TinyBase** | リアクティブデータストア | ローカル状態管理に特化 |
| **PGlite** | WASM Postgres | ElectricSQL開発。ブラウザ内でDB動作 |
| **Replicache** | リアルタイム同期 | ローカル書き込みの即時確定 |
| **Vlcn/cr-sqlite** | SQLite CRDT | リレーショナルCRDT |
| **Ditto** | P2P同期 | オフラインファーストDB |

### Kleppmannの2024年アップデート

Local-First Conference 2024 (Berlin) で **「Local-First は研究中から実用段階へ」** と述べた。

特に **Generic Sync Server** 概念を提唱 — アプリ固有のコードをサーバーに置かず、**同期だけを汎用化する**ことで開発コストを劇的に下げるアプローチ。

> *"So much work in building a web app goes into reinventing this backend infrastructure that every single company has to reinvent again. And so if we can make the data sync generic... That I think is part of the economic value proposition of local-first software."*

---

## Local-Firstの大規模実装: Bluesky / AT Protocol

Kleppmann は Bluesky コア開発者として、Local-First の原則をソーシャルネットワークに適用。

### AT Protocol の Local-First 的要素
- **Personal Data Server (PDS)**: ユーザーのデータは「自分のサーバー」が主コピー（理想#2/#7）
- **Account Portability**: サーバー変更時にデータを移行可能（理想#5/#7）
- **Self-Certifying Data**: 暗号学的検証付きデータ（理想#6）
- **"Big World" Design**: Relay が大規模インデックスを担当し、PDS は軽量に（スケーラビリティ + 所有権の両立）

論文: [arXiv:2402.03239](https://arxiv.org/abs/2402.03239) — "Bluesky and the AT Protocol: Usable Decentralized Social Media"

---

## Local-First と AI Agent: 具体的な技術的ブリッジと正直なギャップ分析

> **注意**: Local-First と AI Agent は異なる問題領域を扱う。以下は概念的な類似性ではなく、**実際に存在する技術的接続点**を整理する。

### ブリッジ1: イベントソーシング → エージェントの監査ログ

**Local-First側**: CRDTs はすべての変更をイベントとして記録し、同期時にマージする（イベントソーシング）。

**AI Agent側**: 
- CAST (Claude Agent Specialist Team) は SQLite WALモードで全エージェントアクションを記録
- Claude Code のセッション履歴はローカルファイルに保存
- 3層メモリ: Daily notes → Long-term MEMORY.md → Knowledge graph（PARA構造）

**接続点**: 両者とも「変更を不変なイベントとして記録し、後から再構築可能にする」アーキテクチャ。エージェントの「セッション跨ぎメモリ」は、Local-Firstのイベントソーシングをコンテキスト管理に応用したものと解釈できる。

### ブリッジ2: ローカル権威モデル → エージェントのローカル実行

**Local-First側**: データの第一権威コピーはローカル。サーバーは同期のみ担当。

**AI Agent側**:
- Claude Code は Node.js CLI としてローカル実行（~10.5 MB）
- ファイルシステム、シェル、ツールはすべてローカル
- モデル推論のみAPI通信。ワークスペースコンテキストはローカルに保存
- OpenClaw: Mac Mini 24/7 自律運用。データはローカルファイルシステム

**接続点**: 「エージェントがローカルで実行され、外部APIは推論のみに限定」するモデルは、Local-Firstの「ローカルが主で、クラウドは補完」という構造と一致。プライバシー・コンプライアンス（医療/金融/法務）の観点からも、データ外出し禁止はLocal-Firstの理想#6/#7と直接対応。

### ブリッジ3: Generic Sync Server → MCP (Model Context Protocol)

**Local-First側**: Kleppmann が提唱した「アプリ固有コードをサーバーに置かず、同期だけを汎用化」するアプローチ。ElectricSQL は Postgres → クライアントの同期を抽象化。

**AI Agent側**:
- MCP は標準プロトコルで3000+外部サービス接続
- Claude Code は `.mcp.json` でMCPサーバーを定義
- アプリ固有の統合コード不要。標準インターフェースでツール接続

**接続点**: 「標準プロトコルで抽象化し、アプリケーション層からインフラ層を分離」する設計思想が両者に共通。MCP は Local-First の Generic Sync Server 概念を「AIツールの接続」に適用したもの。

### ブリッジ4: エッジ推論 → Network Optional

**Local-First側**: ネットワークがなくても完全機能（理想#3）。

**AI Agent側**:
- [[concepts/local-llm]] — Ollama + llama.cpp/GGUF でローカル推論
- RTX 4090 24GB で70Bモデル（量子化）動作
- Phi-4-Reasoning 14B が o1-mini に数学で勝利
- Apple MLX で Mシリーズチップ最速推論
- TTFT: 7Bで50ms（ローカル） vs 200-400ms（クラウド）

**接続点**: 「ネットワーク依存からの脱却」が両者の共通目標。AI Agent ではレイテンシ（TTFT短縮）とプライバシー（データ外出し禁止）の両面でエッジ推論が優勢。コスト面でも RTX 5090 x2 ($4K) が H100 ($25K+) と同等。

### ブリッジ5: CRDTs → CRDT for AI

**Local-First側**: CRDTs はデータ構造の自動マージを保証。

**AI Agent側**:
- CRDTs を AI のコンテキスト管理に応用する研究が進行中
- ローカル知識グラフを CRDT として扱い、デバイス間セッションをマージ
- SQLite CRDT (Vlcn/cr-sqlite) は AI Agent のセッションストアとして利用可能

**接続点**: CRDTs の「分散状態収束」概念を AI Agent の「状態管理」に応用する試み。ただし、これはまだ研究段階。

### 正直に残るギャップ

| Local-First で解決済み/進行中 | AI Agent で未解決 |
|----------------------|-----------------|
| CRDTs による数学的競合解決 | マルチエージェントの「意思決定競合」に数学的保証なし |
| Generic Sync Server の抽象化 | エージェント推論パイプラインはタスク固有依存が強い |
| 静的データの所有権・永続化 | LLM生成コンテンツの所有権・検証・永続化の概念未成熟 |
| P2P同期（NAT超えは課題） | エージェント間直接通信（A2Aプロトコル）も同様に未解決 |
| CRDT履歴肥大化（GC/圧縮未解決） | エージェントのコンテキスト肥大化（compaction未成熟） |

---

## 2026年の動向

- **EU AI Act（2026年8月施行）** がローカルデプロイを規制上の必須に
- **Local models matching Sonnet-class quality** が2026年末に予測
- **Dual RTX 5090s ($4K)** が H100 ($25K+) と同等 — 75%コスト削減
- **ハイブリッドアーキテクチャ**（ローカル for speed/privacy + クラウド for frontier reasoning）が標準

---

## References

- Kleppmann, M. et al. (2019). ["Local-First Software: You Own Your Data, in Spite of the Cloud"](https://martin.kleppmann.com/papers/local-first.pdf). Ink & Switch.
- Kleppmann, M. (2024). ["The past, present, and future of local-first"](https://martin.kleppmann.com/2024/05/30/local-first-conference.html). Local-First Conference, Berlin.
- Kleppmann, M. et al. (2024). ["Bluesky and the AT Protocol: Usable Decentralized Social Media"](https://arxiv.org/abs/2402.03239). arXiv:2402.03239 [cs.DC].
- [localfirst.fm](https://localfirst.fm) — Podcast series on local-first development
- [ElectricSQL Blog](https://electric-sql.com/blog/2024/07/17/electric-next) — "A new approach to building Electric"
- [RxDB](https://rxdb.info/articles/local-first-future.html) — "Why Local-First Software Is the Future and its Limitations"
- [CAST Project](https://github.com/ek33450505/claude-agent-team) — Claude Agent Specialist Team
- [OpenClaw](https://openclaw.ai) — Self-hosted AI agent framework
