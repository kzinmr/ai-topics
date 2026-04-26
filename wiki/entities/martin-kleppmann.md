---
title: Martin Kleppmann
type: entity
created: 2026-04-13
updated: 2026-04-13
status: draft
related: [local-first-software, automerge, bluesky-at-protocol]
sources: [https://martin.kleppmann.com, https://martin.kleppmann.com/papers/local-first.pdf]
tags:
  - person
  - distributed-systems
  - CRDT
  - local-first
  - databases
  - open-source
---


# Dr. Martin Kleppmann

ケンブリッジ大学計算機科学技術学科准教授。分散システム、ローカルファースト協調ソフトウェア、暗号プロトコルを研究。

**Best-selling著書『Designing Data-Intensive Applications』**（2017年、2026年第2版）は分散データ処理システムのアーキテクチャにおける権威的テキスト。20万部以上販売、8言語に翻訳。

---

## 経歴

| 時期 | 役割 |
|------|------|
| 2022–現在 | ケンブリッジ大学 准教授（Concurrent and Distributed Systems、Cryptography and Protocol Engineering担当） |
| 2022–2023 | TU Munich リサーチフェロー（Systems Research Group） |
| 2015–2022 | ケンブリッジ大学 リサーチフェロー（Systems Research Group） |
| 2012 | Rapportive 共同設立 → LinkedIn に買収 |
| 2009 | Go Test It 共同設立 → Red Gate Software に買収 |

---

## 研究: Local-First Software と CRDTs

### Local-First Software (2019)

Ink & Switch 研究ラボで論文 **"Local-First Software: You Own Your Data, in Spite of the Cloud"** を発表。クラウド中心アーキテクチャへのアンチテーゼとして、ユーザーデバイスを第一権威とする設計思想を提唱。

**7つの理想**: No Spinners, Multi-Device, Network Optional, Seamless Collaboration, The Long Now, Security & Privacy, Ultimate Ownership

基盤技術として **CRDTs (Conflict-free Replicated Data Types)** を位置づけ、分散協調編集の数学的保証を可能にするアルゴリズムとして注目。

### Automerge

JavaScript CRDT ライブラリ。JSONデータモデルを操作-based CRDTとして実装。

- 複数デバイスが独立して更新可能 → 同期時に決定論的マージ
- オフライン動作 + リアルタイム協調の両立
- P2P/サーバー/Bluetooth など転送非依存
- 形式検証済み（Strong Eventual Consistency）

**主要論文**:
- "A Conflict-free Replicated JSON Datatype" (IEEE TPDS, 2017)
- "Verifying strong eventual consistency in distributed systems" (PACMPL, 2017)
- "Automerge: Real-time data sync between edge devices" (MobiUK, 2018)
- "Interleaving anomalies in collaborative text" (PaPoC, 2019)

### Generic Sync Server (2024)

Local-First Conference 2024 で提唱。アプリ固有コードをサーバーに置かず、**同期だけを汎用化する**アプローチ。開発コストを劇的に下げる可能性。

> *"So much work in building a web app goes into reinventing this backend infrastructure that every single company has to reinvent again. And so if we can make the data sync generic... That I think is part of the economic value proposition of local-first software."*

---

## Bluesky / AT Protocol

Kleppmann は Bluesky コア開発者として、分散型ソーシャルネットワークの設計に参画。

**AT Protocol の Local-First 的要素**:
- **Personal Data Server (PDS)**: ユーザーデータは「自分のサーバー」が主コピー
- **Account Portability**: サーバー変更時にデータ移行可能（ベンダーロックイン防止）
- **Self-Certifying Data**: 暗号学的検証付きデータ
- **"Big World" Design**: Relay による大規模インデックス + 軽量PDS

論文: "Bluesky and the AT Protocol: Usable Decentralized Social Media" (arXiv:2402.03239, DIN '24)

---

## 著作

| タイトル | 年 | 備考 |
|----------|-----|------|
| Designing Data-Intensive Applications | 2017 | O'Reilly. 分散システム/データベースの名著 |
| Designing Data-Intensive Applications (2nd ed.) | 2026 | Chris Riccomini と共著 |
| Secret Colors: A Gentle Introduction to Cryptography | 2020 | Mitch Seymour と共著（子供向け暗号入門） |

---

## 講演・メディア

- ACM Tech Talks (2023): "Creating local-first collaboration software with Automerge"
- RainbowFS Workshop (2022): "Automerge: CRDTs meet version control"
- Distributed Computing and Analytics Workshop (2018): "Automerge: Replicated Data Structures for Peer-to-Peer Collaboration"
- [localfirst.fm Podcast #4](https://localfirst.fm/4): CRDTs, Automerge, generic syncing servers & Bluesky
- [Patreon](https://patreon.com) でクラウドファンディング実施

---

## Local-First と AI Agent の技術的ブリッジ（Kleppmann の文脈から）

> **注意**: Kleppmann 自身は AI Agent について直接言及していない。以下は彼の研究が AI Agent 開発と**技術的に接続しうる点**を整理したものである。

### 1. イベントソーシング → エージェント監査ログ

**CRDTs** はすべての変更を不変なイベントとして記録し、同期時にマージする。このアプローチはエージェントのセッション管理に直接適用可能:
- CAST (Claude Agent Specialist Team) は SQLite WALモードで全エージェントアクションを記録
- Claude Code のセッション履歴はローカルファイルに保存
- 両者とも「変更をイベントとして記録 → 後から再構築可能」

**違い**: CRDTs は数学的収束保証を持つが、エージェントの意思決定チェーンには同等の保証が存在しない。

### 2. Generic Sync Server → MCP

Kleppmann が提唱した「同期だけを汎用化」するアプローチは、**[[mcp|Model Context Protocol]]** の設計思想と一致:
- ElectricSQL: Postgres → クライアントの同期を抽象化
- MCP: 標準プロトコルで 3000+ 外部サービス接続
- どちらも「アプリ固有コード不要の標準化層」を提供

### 3. CRDT履歴肥大化 → コンテキストウィンドウ管理

CRDTs の未解決問題（全キーストローク保存 → メモリ劣化）は、エージェントの**コンテキストウィンドウ肥大化**と構造的に同一:
- 両者とも append-only ログの無限成長に直面
- 両者とも GC/compaction が未成熟
- 両者とも「何を保持し、何を捨てるか」の判断が難しい

### 4. 残る本質的ギャップ

| 項目 | Local-First (解決済み/進行中) | AI Agent (未解決) |
|------|------------------------------|------------------|
| 競合解決 | CRDTs で数学的保証 | マルチエージェントの意思決定競合に保証なし |
| 同期抽象化 | ElectricSQL/Generic Sync で実用化 | エージェント推論パイプラインはタスク固有依存が強い |
| データ所有権 | 静的データに対して明確 | LLM生成コンテンツの所有権・検証概念が未成熟 |
| P2P同期 | NAT超えは課題だが進展中 | エージェント間直接通信(A2A)も同様に未解決 |

---

## Links

- Website: https://martin.kleppmann.com
- Bluesky: @martin.kleppmann.com
- Mastodon: @martin@nondeterministic.computer
- GitHub: https://github.com/automerge/automerge
- Papers: https://martin.kleppmann.com/papers/
- Email: firstname at lastname dot com

## See Also

- [[entities/_index]]
- [[lance-martin]]
- [[martin-alderson]]
