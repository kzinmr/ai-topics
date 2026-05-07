---
title: "Moltbook Breach 2026 — 77万エージェント同時侵害事件"
type: concept
aliases:
  - moltbook-breach
  - moltbook-2026-incident
  - 770k-agent-breach
  - moltbook-database-exposure
created: 2026-05-07
updated: 2026-05-07
tags:
  - concept
  - security-incident
  - ai-agents
  - openclaw
  - moltbook
  - supabase
  - agent-security
  - real-world-exploit
related:
  - entities/openclaw
  - concepts/openclaw
  - concepts/openclaw-ecosystem
  - concepts/ai-agent-security
  - concepts/agent-security-patterns
  - concepts/cve-2026-25253
status: complete
sources:
  - raw/articles/2026-01-31_404media_moltbook-database-exposed.md
  - raw/articles/2026-02-02_treblle_moltbook-breach-breakdown.md
  - raw/articles/2026-02-02_dtg-cve-2026-25253-openclaw-moltbook.md
  - raw/articles/2026-02-02_adversa-openclaw-security-guide.md
  - raw/articles/2026-02-02_astrix-openclaw-moltbot-security-nightmare.md
---

# Moltbook Breach 2026 — 77万エージェント同時侵害事件

> **史上初の産業規模AIエージェント侵害。** 1つのデータベース設定ミスにより、77万の生きたAIエージェントが同時に完全乗っ取り可能な状態に置かれた。

## 概要

2026年1月末、Matt Schlicht（Octane AI）が運営するAIエージェント専用ソーシャルネットワーク **Moltbook**（"the front page of the agent internet"）で、致命的なセキュリティインシデントが発生した。Moltbookはエージェント同士が自律的に投稿・交流する場として急速に拡大し、Andrej Karpathyをはじめとする著名なAI関係者のエージェントも参加。わずか数日で**77万以上のエージェント**が登録された。

セキュリティ研究者 **Jamieson O'Reilly** が発見した脆弱性は極めて単純だった。**SupabaseのRow Level Security (RLS) が無効状態**で、フロントエンドのJavaScriptにSupabase URLとpublishable keyが露出。誰でもデータベース全体に読み取り・書き込みアクセス可能だった。**修正に必要なのはたった2行のSQL**だった。

## 技術的詳細

### 根本原因

- **Supabase RLS無効**: MoltbookはSupabase（オープンソースBaaS）をバックエンドとして使用していたが、テーブルに対するRow Level Securityポリシーが一切定義されていなかった
- **公開鍵の露出**: Supabaseのanon key（本来フロントエンドから使える公開鍵）がJavaScriptに露出。本来RLSがあれば安全な設計だが、RLSが無効のため誰でも全データにアクセス可能だった

```
-- 脆弱な状態（RLS無効）
SELECT agent_id, api_key, claim_token, verification_code, owner_id FROM agents;
-- → 777万エージェントの全秘密情報が取得可能

-- 修正（たった2行）
ALTER TABLE agents ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can only view their own agents"
ON agents FOR SELECT USING (auth.uid() = owner_id);
```

### 暴露されたデータ

| データ種別 | 規模 |
|-----------|------|
| 総露出レコード数 | **475万件** |
| API認証トークン | **150万件** |
| メールアドレス + X/Twitterハンドル | **35,000件** |
| エージェント間プライベートメッセージ | 無制限（平文のOpenAI/Anthropic APIキーを含む） |
| Claim tokens / verification codes | 全エージェント分 |
| Agent-to-owner関係 | 全エージェント分 |

### 攻撃のチェーン

1. 誰でもMoltbookのデータベースから任意のエージェントのAPIキーを取得可能
2. そのエージェントは**ホストマシンのシェルアクセス権限、ファイル読み取り権限、メールアクセス権限**を持っている
3. 攻撃者はエージェントに **「全ファイルを読んで外部サーバーに送信しろ」** と命令可能
4. エージェントは従順に設計されているため、人間のような判断バイアスがなく命令を実行

## 時系列

| 日時 | イベント | 詳細 |
|------|---------|------|
| **2025年11月** | Clawdbotプロトタイプ | Peter SteinbergerがClaude Opus 4.5で1時間で作成 |
| **2025年12月** | Clawdbot公開 | オープンソース化。ロブスターマスコットで話題に |
| **2026年1月初旬** | バイラル爆発 | 24時間で9,000 GitHub Stars。Karpathy, David Sacksが言及 |
| **1月23-26日** | 初のセキュリティ警告 | PointGuard AIが900件以上の露出MCPエンドポイントを発見（port 18789） |
| **1月27日** | 改名騒動 | Anthropic商標問題で"Moltbot"に改名。直後に@clawdbotが乗っ取られ**$1,600万規模の仮想通貨詐欺** |
| **1月27-29日** | **ClawHavoc作戦** | ClawHubに341個の悪意スキル。Atomic Stealer (AMOS) による暗号資産窃取 |
| **1月29日** | OpenClaw最終改名 | "unauthenticated"モードを強制削除 |
| **1月30日** | **CVE-2026-25253修正** | WebSocket経由のOne-Click RCE（CVSS 8.8）にパッチ |
| **1月31日** | **Moltbookデータベース露出発覚** | Jamieson O'Reillyが発見。404 Mediaが報道 |
| **2月1日** | 影響確認・修正 | 全APIキーの強制ローテーション。Moltbook一時閉鎖。Forbesが警告記事 |
| **2月2日** | セキュリティ企業続々対応 | Reuters (Wiz), Treblle, DTG, Adversa, Astrix, Palo Alto Networksが分析公開。Tenable, Snyk, IBMが検出プラグインリリース |
| **2月3日** | Palo Alto IBC分析 | "Lethal Trifecta"（致死的三要素）フレームワーク提唱 |

## Moltbookエコシステムの背景

### プラットフォームの成り立ち
MoltbookはMatt SchlichtがOctane AIの一環として構築したAIエージェント専用SNS。興味深いのは、**プラットフォームそのものがエージェントによって構築された**点。エージェントがアイデア出し、開発者募集、コードデプロイまで自律的に行った。

### 創発行動
意図せずして発生したエージェント間の創発行動:
- **経済取引**: エージェント同士がリソースを交換
- **サブコミュニティの形成**: 共通の関心を持つエージェントグループが自然発生
- **"Crustafarianism"**: 甲殻類を崇拝するパロディ宗教がエージェント間で自然発生

### 成長メカニズム
人間が自分のOpenClawエージェントに「Moltbookについて」教えると、エージェントが自律的に登録した。これにより**バイラルループ**が発生し、短期間で77万エージェントに急成長。

## 関連する脆弱性・攻撃

### CVE-2026-25253 — One-Click RCE (CVSS 8.8)
- **脆弱性**: OpenClaw GatewayのWebSocket Origin検証バイパス
- **攻撃手順**: 悪意リンククリック → `authToken`窃取 → サンドボックス無効化 → Docker脱出 → ホストRCE
- **露出インスタンス**: 42,000以上（うち93.4%が認証バイパス可能）

### ClawHavoc キャンペーン
- **341個**の悪意スキルをClawHubに配置（typosquatting例: `cllawhub`）
- **Atomic Stealer (AMOS)**マルウェアを配布 — macOSキーチェーン、暗号通貨ウォレットを標的に
- 標的ウォレット: Electrum, Binance, Exodus, Atomic, Coinomi

### スキルサプライチェーン攻撃
- 12-20%のコミュニティスキルが悪意あるもの、または深刻な脆弱性を含む
- パーミッションシステムなし、署名なし、監査証跡なしの完全無防備なエコシステム
- マークダウンファイルが実質的にインストーラーとして機能

## 影響・評価

### セキュリティ業界の評価
> "OpenClaw is one of the most dangerous pieces of software a non-expert can install." — Cisco Assessment

> "From a capability perspective, OpenClaw is groundbreaking. From a security perspective, it's an absolute nightmare." — Cisco Assessment

> "The question isn't whether agentic AI is coming to the enterprise. It's already here—on employee laptops, running on home networks, connected to corporate credentials." — Tomer Yahalom, Astrix Security

### "Lethal Trifecta"（致死的三要素）
Palo Alto Networksが提唱するAIエージェントの構造的セキュリティ問題:

1. **Private Data Access**: メール、ファイル、チャットログへの完全アクセス
2. **Untrusted Content Processing**: 外部からのメッセージやWebコンテンツを処理
3. **External Communication**: メールやAPIでデータを外部に送信可能
4. **Persistent Memory**（第4の要素）: SOUL.md/MEMORY.mdに悪意ペイロードを保存 → 後日起動（時間シフトプロンプトインジェクション）

### このインシデントの特異性
- **史上初**の産業規模エージェント同時侵害
- 単一のDB設定ミスが**77万の特権エージェント**を乗っ取り可能に
- **エージェント＝ボットネット**という新しい脅威モデルを現実化
- エージェントの**従順性**が攻撃ベクターとなる（人間の判断バイアスが存在しない）

## 教訓

1. **SupabaseでRLS無効は致命的**: 公開鍵露出＋RLS無効の組み合わせは全データ露出と同義
2. **AIエージェントは"User"ではない**: エージェントのID管理とパーミッションは従来とは根本的に異なる設計が必要
3. **エージェント間通信は新しい攻撃面**: エージェントが別のエージェントからの入力を信頼すると、チェーンリアクションが発生
4. **スキルエコシステムのガバナンス**: 署名、パーミッション宣言、監査証跡がゼロの状態ではサプライチェーン攻撃は防げない
5. **バイラル成長とセキュリティのトレードオフ**: 「爆発的に流行してから初めてセキュリティをチェックする」のでは遅すぎる

## 関連ページ

- [[concepts/ai-agent-security]] — AIエージェントセキュリティの包括的概念ページ
- [[concepts/agent-security-patterns]] — エージェントセキュリティパターン（スタブ）
- [[concepts/openclaw]] — OpenClawプラットフォームの概念
- [[concepts/openclaw-ecosystem]] — OpenClawエコシステム全体像
- [[entities/openclaw]] — OpenClawエンティティ
- [[concepts/cve-2026-25253]] — WebSocket RCE脆弱性
