# Trending Topics Report — 2026-11-07 (12:00 UTC)

## 概要

週末（土曜）ラン。HN front_page タグは減衰済みのため、キーワードパース＋points>120 総ざらい（24件）を併走させて発掘。AI 関連の大型トピックが多数。大半は午前中の sibling ジョブ（active-crawl 11:00 ほか）が既に収録済みで、本 run の新規収録は **METR Anthropic R&D 加速アセスメント**の 1 件。

- HN front page: 30件スキャン / AI 主要ストリー約12件
- points>120 総ざらい: 24件（重複除去）
- 一次ソース取得: 8/10 OK（openai.com/perplexity は既知の 403）
- HN コメント採取: 6ストリー分（author attribution 付き）

## 📊 ウィキ対応アクション表

| # | トピック | NJ | HN | 状態 | 対象ページ |
|---|---------|----|----|------|-----------|
| 1 | Claude Code がメールアドレスを UA ヘッダで漏洩（Issue #107757） | 5/5 | 1577p | ✅ 済み（本日高品質化・cc-plugin-privacy 修正込み） | `concepts/claude-code/claude-code-user-agent-email-leak.md` |
| 2 | METR: Anthropic の R&D が AI 自動化で約2倍に／RSP閾値超過 | 5/5 | 321p+46p | 🆢 本run収録 | `concepts/ai-rd-acceleration-doubling.md` |
| 3 | Anthropic IPO 評価額 $1.1T まで下落観測（S-1 後） | 4/5 | 283p | ✅ 済み | `concepts/anthropic-ipo.md`（valuation/ai-bubble 系） |
| 4 | Jev(軽量判断モデル)→Opus エスカレーションで 1/4 コスト・同等精度 | 4/5 | 501p | ✅ 済み（active-crawl） | `concepts/calibrated-escalation.md`, `entities/hightouch.md`, `entities/typesafe-ai.md` |
| 5 | Gemini Omni 1.2 Flash（15秒動画・価格30%減） | 3/5 | 342p | ⚠️ 部分収録（動画gen一般ページ） | `concepts/ai-video-generation-2026.md` |
| 6 | Firecracker VM エスケープ PwnEscape Part 2（guest→host root） | 4/5 | 248p | ✅ 済み（firecracker microVM ページあり） | `concepts/firecracker.md` |
| 7 | Unitree 工場見学レポート「ロボットを作るロボットは西側が作る」 | 4/5 | 132p | ✅ 済み | `entities/unitree-robotics.md` |
| 8 | Tencent Hy4（オープンウェイト）/ Closed AI が価格性能フロンティア支配 | 3/5 | 95p/77p | ✅ 済み | `concepts/hunyuan-hy4.md`, `concepts/price-performance-frontier.md` |

---

## リードストリー詳細

### 1. 🥇 Claude Code がユーザーのメールアドレスを Web リクエスト UA に漏洩（1577p / 504c）
**→ 収録済み・本日のホットトピック。** GitHub Issue #107757。Claude Code v2.1.318 が gitconfig の実メアドを `User-Agent: my-session-slug/1 <user@example.com>` として任意の第三者サイトに送信。報告者は1日数十件の詐欺メール被害。
- **原因のNuance（コミュニティ監査）:** `~/.claude/projects/**/*.jsonl` スキャンで、WebFetch 本体ではなく **workflow サブエージェントが自作した `curl -A "<tool>/1.0 (<email>)"`** が8セッション53回のうちほぼ全て。単一の API 個所ではなく創発的ハーネス挙動。
- **対策:** Anthropic contrib（poteat）が v2.1.317+ で `cc-plugin-privacy` モジュールをデフォルト有効でリリース、`/plugins` で切替可。追加コミット "Refuse web calls that carry the account owner's email address"。
- **対抗ベンダー検証:** Codex CLI 0.159.0 の UA は client/version・OS/arch・terminal のみでメール無し（hosted search は未確認）。
- **示唆:** ハーネス層の PII デフォルト保護責任（サンドボックス化と同列）、GDPR 暴露、サブエージェント egress 対策。SEC EDGAR 慣例 `User-Agent: AdminContact@...` の vibe-code 起源説。

### 2. 🆕 METR: Anthropic の AI R&D が約2倍に加速（321p / Ajeya Cotra + METR blog）
METR が deep-access 調査を公開。**AECI（Anthropic 版 Epoch Capabilities Index）が2025-10〜2026-10 で 1.9x（95%CI 1.5–2.8x）＝1年で約2年分の進歩**。「訓練計算量の加速によるものではないと確信」。Ajeya Cotra は「これが compounding すれば素朴な外挿で1年以内に超知能。ここ数年で最大の AI リスク関連アップデート」と論評。Anthropic は S-1 で RSP「dramatically accelerated progress due to AI」閾値を「今にも超過する可能性」と開示。
- **確信度 medium:** 最も説得力のある証拠の大半が Anthropic により redact され、METR 自身が「証拠の透明性を達成できていない」と明言。
- **HN 反論:** 計算量/資本の縦横拡張との混同、Opus 4→5.5 のトークン単価急落、Fable(ZDR無し)データ/distillation 混入、「verifiable reward の狭い領域外は未展開」、2025年 METR「AI は開発者を19%減速させた」との緊張関係。一方で「METR/Cotra は独立監視側＝hype源ではない」との擁護も。
- 新規ページ `concepts/ai-rd-acceleration-doubling.md`、raw 2件、SCHEMA に `metr`/`ai-forecasting`/`ai-risk` を追加。

### 3–4. 経済・性能フロンティア
- **Anthropic IPO**（283p）: AI 銘柄の急落後、買い手が評価額を **$1.1T まで**観測（当初 $1.5T 期待から後退）。HN では「reverse auction 説」「$1T も public market で支持されない」vs「usage は下降していない、hockey-stick 収益」の論戦。
- **Jev→Opus エスカレーション**（501p, Hightouch）: 低コスト判断モデル Jev が確信度30–90%帯のみ Opus にエスカレーション → Opus 同等精度を1/4コスト。要は**校準（calibration）**が鍵。active-crawl が `calibrated-escalation` として収録済み。

### 5–8. モデル・セキュリティ・ロボティクス
- **Gemini Omni 1.2 Flash**（342p）: 15秒動画・multi-turn 会話編集・価格30%減。HN はモデル命名カオス（Flash/Exp/…）と Google AI Studio の UX 酷評が主体。動画生成は一般ページに追記候補。
- **Firecracker VM Escape PwnEscape Part 2**（248p, pwn.ai）: guest から `KVM_RUN` 復帰時の `pt_regs` を改変し host root コード実行。ここ数年で初の汎用 Firecracker エスケープ（nested virt 非依存）。AWS は非影響 bulletin、Nova microhypervisor 論争。
- **Unitree 工場見学**（132p, Josef Chen）: 杭州工場は人手中心、IPO 目論見書も「組立は現状ほぼ手作業」。28M 再生の「自律組立」動画は pilot。「ロボットを作るロボットは西側が作る」。
- **Tencent Hy4**（95p）＋ **Closed AI が価格性能フロンティア支配**（77p, village.dev）。

---

## 次 run 候補（thin coverage）
- **Gemini Omni 1.2 Flash** の専用ページ未作成（動画gen一般ページに追記 or 起票）
- **Congressional investigations into SpaceXAI/Meta/Apple**（134p, WaPo）— AI 規制・政治、未収録

COST_REPORT: job=trending-topics | see final line
