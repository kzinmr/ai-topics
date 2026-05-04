# 🚀 AI/ML 注目トピックス — 2026-05-04

> スキャン日時: 2026-05-04 | Web検索 + RSS 66記事 + wiki照合 (800+ページ)
> 更新情報: 直近3日間で66件のRSS記事、15件以上のWikiページ更新を確認

---

## 📊 ランキング

### 🥇 OpenAI Symphony — エージェントオーケストレーションのパラダイムシフト
**公開:** 2026-04-27 (OSS), **インパクト:** ★★★★★
**Wiki:** ✅ [[concepts/openai-symphony]] (充実)

OpenAI が公開したオープンソースのエージェントオーケストレーション仕様。**Linear の課題管理ボードをコーディングエージェントの制御プレーン**に変換する。各チケットに専用ワークスペースでエージェントがアサインされ、自律的に実行 → 人間は成果物レビューのみ。

- 内部導入で **PR着地数が500%増加** (3週間)
- 人間の注意力がボトルネック — 3〜5セッションでコンテキストスイッチング破綻
- 「Manage work, not agents」哲学 — エージェントの監視から作業管理への転換
- WORKFLOW.md でエージェント動作をリポジトリ管理
- 参考実装はElixir, コミュニティ実装はGo/Pythonに拡大中

**関連:** [[concepts/agent-team-swarm]] | [[concepts/harness-engineering]] | [[concepts/dark-factory-software-factory]]

---

### 🥈 ペンタゴンAI契約 — 7社の機密軍事契約、Anthropic除外
**公開:** 2026-05-01〜04, **インパクト:** ★★★★★
**Wiki:** ✅ [[concepts/ai-military]] | ✅ [[entities/reflection-ai]] (他社も要追加?)

米国防総省が **SpaceX, OpenAI, Google, Nvidia, Microsoft, AWS, Reflection AI** の7社と機密レベルIL6/IL7の軍事AI契約を締結。全ての契約に **"any lawful use"** 条項（合法的なあらゆる用途を許可）。

- **Anthropic 除外:** Mythos の自律ドローン制御リスクや国内監視への懸念が原因
- **Reflection AI:** 創業2年のスタートアップ (旧DeepMind研究員)、Nvidia/1789 Capital 出資、$25B評価額を模索中、公開モデルなし
- 米軍の「AI-first fighting force」への転換を加速
- 各企業の役割: SpaceX (極秘衛星通信/推論), OpenAI (GPT-5.5-Cyber), Google (Gemini), Nvidia (ハードウェア/B300)

---

### 🥉 Codex CLI 0.128.0 — /goal による自律ループ (Ralph Loop)
**公開:** 2026-04-30, **インパクト:** ★★★★☆
**Wiki:** ✅ [[concepts/openai-codex-superapp]] (Codex Superapp内で言及)

Codex CLI に **`/goal`** コマンドが追加。目標を設定すると、達成するかトークンバジェットが尽きるまで自律ループ。OpenAI版 Ralph Loop。

- メカニズム: `goals/continuation.md` と `goals/budget_limit.md` プロンプトが自動注入
- TUI で create/pause/resume/clear を制御
- MultiAgentV2 のスレッドキャップ/設定が明示的に
- 常駐エージェント → Symphonyへ至る基盤技術
- **Simon Willison ブログでも言及** (simonwillison.net)

**新規作成:** `raw/articles/2026-04-30_codex-cli-0-128-0-goal.md` を保存

---

### ④ Anthropic Creative Coalition — 9つのクリエイティブツールコネクタ
**公開:** 2026-04-28, **インパクト:** ★★★★☆
**Wiki:** ✅ [[entities/anthropic]] (Creative Coalitionセクション追加済み)

Anthropic が **Adobe Creative Cloud (50+ツール)、Blender、Autodesk Fusion、Ableton Live、Affinity、Splice** など9つのクリエイティブツールコネクタを公開。ClaudeがPhotoshopで画像編集、Blenderで3Dシーンデバッグ、Abletonで音楽制作ワークフローを自動化可能に。

- BlenderはMCPコネクタ + AnthropicがBlender財団に寄付
- 教育連携: RISD (Art and Computation), Ringling College, Goldsmiths
- Claudeは「tasteやimaginationを置き換えない」が、「routine tasksの排除」を標榜
- AdobeはClaude連携を「製品内AI機能ではない、Agentが直接操作する」と明言

---

### ⑤ Qwen3.6-27B — 27B Denseモデルが397B MoEを凌駕
**公開:** 2026-04-22, **インパクト:** ★★★★☆
**Wiki:** ✅ [[concepts/qwen3-6-27b]] (充実)

Alibaba/Qwen Team が公開。**27BパラメータのDenseモデル**で、15倍大きい Qwen3.5-397B-A17B (MoE) をコーディングベンチマークで上回る。

- **SWE-bench Verified:** 77.2% (vs 397B 76.2%)
- **Terminal-Bench 2.0:** 59.3% (vs 52.5%)
- **Apache 2.0 ライセンス** (完全オープン)
- **Thinking Preservation:** 思考連鎖を会話ターン間で保持 (マルチステップエージェントでトークン大幅削減)
- **262K→1M コンテキスト拡張可能、約18GB VRAMで動作**
- ただし **Qwen3.6-Max-Preview** は初の非公開フラグシップ (API only)

---

### ⑥ Google $40B の Anthropic 投資と $30B ARR
**公開:** 2026-04-24, **インパクト:** ★★★★☆
**Wiki:** ✅ [[entities/anthropic]] (更新済み)

Google が Anthropic に最大 **$400億** の現金+計算資源投資。2027年から **5GWのTPU容量** 提供 (ミネソタ州全家庭の電力量)。

- Anthropicの年間経常収益(ARR)が **$300億突破** (2025年末$90億から急成長)
- Claude Code のエンタープライズ需要が主因
- 前月にはAmazonも最大$250億の投資契約
- OpenAI は「Anthropicは計算資源確保に失敗している」と批判していたが、Google+Amazonのダブル契約で一転

---

### ⑦ Agentic Coding Trends Report (Anthropic 2026)
**公開:** 2026-05-01, **インパクト:** ★★★☆☆
**Wiki:** ❌ 未カバー (要作成?)

Anthropic が公開した **2026 Agentic Coding Trends Report**。エンタープライズ向けに8つのトレンドを分析。

- **主要トレンド:** 抽象化の進化 (戦術的コーディング→AI、人間はアーキテクチャ設計へ)、マルチエージェント協調、人間-AIコラボレーションパターン
- **ケーススタディ:** Rakuten, CRED, TELUS, Zapier
- **非技術者向け:** エンジニアリング支援なしでツール構築するパターンの台頭
- **生産性経済学:** ソフトウェア開発の経済性を根本的に再定義

**Note:** ゲート付きPDF (メール登録必要) のためフルアクセスできず。公開情報があればWiki化推奨。

---

## 🔍 分野別トレンド総括

| 分野 | 重要度 | 今週のトピック |
|------|--------|----------------|
| **Agent Orchestration** | ★★★★★ | OpenAI Symphony の本格始動、500% PR増加 |
| **Military AI** | ★★★★★ | ペンタゴン7社契約、Anthropic除外の地殻変動 |
| **Coding Agents** | ★★★★☆ | Codex CLI /goal、AgentHQ (Copilot)、/goal自律ループ標準化 |
| **Open-Source Models** | ★★★★☆ | Qwen3.6-27B (27Bが397B越え)、Alibaba初の非公開フラグシップ |
| **Creative AI** | ★★★★☆ | Anthropic Creative Coalition、Adobe/Blender/Ableton連携 |
| **Infrastructure** | ★★★★☆ | Google $40B→Anthropic、NVIDIA B300 $1M中国価格 |
| **Enterprise Agents** | ★★★☆☆ | Microsoft Agent 365 ($15/月)、Bedrock AgentCore、Symphony |

---

## ⚡ 今週の注目議論

1. **Anthropic 除外のジレンマ:** AI安全を標榜したAnthropicが軍事市場から締め出され、後発のReflection AIが$25B評価額。安全性 vs 市場競争力の緊張。
2. **Open vs Closed のトレンド反転:** Qwen3.6-Max-Previewが初の非公開フラグシップ。オープンソースチャンピオンがAPI onlyに移行。一方Metaはオープン戦略継続。
3. **/goal と Ralph Loop の標準化:** Codex CLI、Claude Code、OpenCode の全主要コーディングエージェントが自律ループモードを実装。次の戦場は **「自律性の度合いと制御のバランス」**。

---

## 📋 アクションアイテム

| アクション | 優先度 | 説明 |
|-----------|--------|------|
| ✅ Codex CLI /goal raw article 保存 | 完了 | `raw/articles/2026-04-30_codex-cli-0-128-0-goal.md` |
| 🔲 Anthropic 2026 Agentic Coding Trends Report | Low | PDFゲート有、公開情報があればWiki化 |
| 🔲 Pentagon契約: 各社の具体的役割のWiki充実 | Medium | Space X/Reflection AIなど、個別エンティティページの更新 |
| 🔲 /goal/Ralph LoopのConceptページ独立化検討 | Medium | 現在Codex Superappページ内のみ参照 |

---
*Report generated by Hermes — 2026-05-04*
