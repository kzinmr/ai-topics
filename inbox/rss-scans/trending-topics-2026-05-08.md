# Trending Topics Report — 2026-05-08

> Generated: 2026-05-08 12:00 JST
> Source: Web search (5 queries), Newsletter pipeline (latest.json), Wiki log analysis
> Coverage gap: 4/8 topics NOT covered in wiki

---

## 🔥 1. Nvidia-Corning $3.2B 光ファイバー提携 — AIインフラの光配線革命

**重要度: ★★★★★ | 日付: 2026-05-06 | 出典: CNBC, Reuters, Bloomberg, Corning公式**

NvidiaがCorningと最大$3.2Bの光ファイバー/光接続製品に関する長期パートナーシップを締結。米国に3つの新工場（ノースカロライナ州×2、テキサス州×1）を建設し、3,000人以上の雇用を創出。AIデータセンター向け光接続製造能力を10倍に増強。

- Nvidiaが$500Mの株式買取権を取得（$180/株、最大1,500万株）
- Corningの光ファイバー生産能力を米国内で50%以上拡大
- Co-packaged optics（CPO）：Nvidiaのラックスケールシステムで銅配線を光ファイバーに置き換え
- Corningの株価は前日比17%急騰、年初来+117%
- Jensen Huangは2025年のGTCでCPOを「AI構築に不可欠」と位置づけ
- 直近のMetaとの$6B契約に続く大型案件

**Wikiカバレッジ**: ❌ 未カバー → `entities/nvidia.md` と新規 `concepts/co-packaged-optics.md` 作成推奨

**Wiki関連**: [[entities/nvidia]]（既存、アップデート推奨）

---

## 🔥 2. OpenAI MRC (Multipath Reliable Connection) 公開 — GPUクラスタネットワーキングの新プロトコル

**重要度: ★★★★★ | 日付: 2026-05-05 | 出典: OpenAI Engineering Blog, AMD, OCP**

OpenAIがAMD, Broadcom, Intel, Microsoft, NVIDIAと2年間共同開発した新ネットワーキングプロトコル「MRC (Multipath Reliable Connection)」をOCP経由でオープンソース公開。大規模AIトレーニングクラスタのGPU通信を高速化・高信頼化。

- 従来のRoCEv2の単一パス問題を解決：パケットを数百のパスに「スプレー」
- 輻輳パスを自動回避、故障パス即時退役＋プローブによる復旧確認
- 1つの800Gb/sインターフェースを8つの100Gb/sに分割 → スイッチ1台で~131,000 GPUに2ティア接続
- Stargateスーパーコンピュータ（Oracle/Abilene, TX）で実証済み
- AMD, Broadcom, Intel, Microsoft, NVIDIAが同時にサポートを表明

**Wikiカバレッジ**: ❌ 未カバー → 新規 `concepts/mrc-multipath-reliable-connection.md` 作成推奨

**Wiki関連**: [[concepts/inference-optimization]], [[entities/openai]]（アップデート推奨）

---

## 🔥 3. Anthropic、$200BのGoogle Cloud契約 — AIインフラ投資の常識を突破

**重要度: ★★★★★ | 日付: 2026-05-05 | 出典: Reuters, The Information**

AnthropicがGoogle Cloudとの間で5年間で$200Bの契約に合意。これはGoogleが先週開示した収益バックログの40%以上を占める。先月のGoogle-Broadcomとの複数ギガワットTPU契約、$40B投資、$100B超のAWS契約に続く大型案件。

- Anthropic + OpenAIの契約で大手クラウド3社（AWS, Azure, GCP）の契約バックログ$2Tの過半数
- Dario Amodei（Code with Claude基調講演）：「成長率が高すぎて手がつけられない」と半ば冗談
- 四半期で80倍のYoY成長率、$30B+の年換算ARR
- SpaceX Colossus Iから300MW確保、Claude Codeの利用制限を倍増
- 2026年中に80倍の事業規模拡大を予測

**Wikiカバレッジ**: ❌ 部分的 → `events/anthropic-code-w-claude-2026.md` は既存だが、$200B契約の詳細は未反映。`entities/anthropic.md` のアップデート推奨。

**Wiki関連**: [[entities/anthropic]], [[entities/google-cloud]], [[events/anthropic-code-w-claude-2026]]

---

## 🔥 4. Samsung、時価総額$1T突破 — AIメモリ需要が半導体史上最高益を牽引

**重要度: ★★★★☆ | 日付: 2026-05-06 | 出典: Bloomberg, CNBC, TechCrunch**

Samsung Electronicsの株価が14%急騰、時価総額$1Tを突破。TSMCに次ぐアジア2社目の快挙。AI向けHBM（High-Bandwidth Memory）需要が主因。

- Q1 2026 営業利益：57.2兆ウォン（前年比8倍、過去最高）
- Q1 収益：133.9兆ウォン（過去最高）
- 半導体部門が全利益の90%超を占める
- HBM4量産開始（世界初、Nvidia Vera Rubin向け）
- SK Hynixも10%上昇、KOSPI指数が初の7,000突破
- AppleがIntel/Samsungとの米国内チップ生産を探る（Bloomberg報道）
- メモリ不足が進行中：3大メーカー（Samsung, SK Hynix, Micron）が民生品部門からHBMへ生産シフト

**Wikiカバレッジ**: ❌ 未カバー → Samsungのエンティティページなし。`entities/samsung-electronics.md` と `concepts/high-bandwidth-memory.md` の作成推奨。

**Wiki関連**: [[entities/nvidia]]（Vera Rubinとの関連）

---

## 🔥 5. GPT-5.5 Instant リリース — ChatGPTデフォルトモデル刷新

**重要度: ★★★★☆ | 日付: 2026-05-05 | 出典: OpenAI Blog, TechCrunch, Axios, Wikipedia**

OpenAIがGPT-5.5 InstantをChatGPTのデフォルトモデルとして全ユーザーに展開。幻覚を52.5%削減、不正確な主張を37.3%削減。パーソナライズ機能（過去チャット・Gmail・ファイル参照）をPlus/Proユーザーに提供。

- AIME 2025: 81.2点（前モデル65.4点から大幅向上）
- MMMU-Pro: 76点（前モデル69.2点）
- API: `chat-latest` として提供、GPT-5.3 Instantは3ヶ月で退役予定
- メモリソースの可視化：モデルが回答を生成した根拠を表示、ユーザーが削除・修正可能
- 「マッチ・ザ・タスク」アプローチ：カジュアルな相談には不要なフォローアップを抑制

**Wikiカバレッジ**: ✅ カバー済み — `concepts/gpt-5.5-instant.md` (既存)

**Wiki関連**: [[concepts/gpt-5.5-instant]], [[entities/openai]]

---

## 🔥 6. Code with Claude 2026 — Anthropic最大のデベロッパーカンファレンス

**重要度: ★★★★☆ | 日付: 2026-05-06~07 | 出典: Simon Willison Live Blog, Ars Technica, Business Insider**

Anthropicがサンフランシスコで「Code with Claude 2026」開催。Dario Amodeiが80倍YoY成長、1人で10億ドル企業を創る時代、SpaceX Colossus Iからの300MW調達などを発表。

- Claude Code全サーフェス（CLI, IDE, Desktopアプリ）の統合
- Claude Agent SDKの一般提供（外部デベロッパーも同一のエージェント基盤を利用可能）
- Code Review機能（Anthropic社内全チームで採用済み）
- Pro/Maxプランの利用制限を倍増、ピーク時制限を撤廃
- Opus API制限も大幅引き上げ（May 6時点）
- Remote Agents：スマホからラップトップを遠隔制御

**Wikiカバレッジ**: ✅ カバー済み — `events/anthropic-code-w-claude-2026.md` と `concepts/ai-delegation-patterns.md` (既存、ただし$200B契約のアップデートが必要)

**Wiki関連**: [[events/anthropic-code-w-claude-2026]], [[entities/anthropic]], [[entities/claude-code]]

---

## 🔥 7. Palo Alto Networks、Portkey買収 — AIエージェントセキュリティの転換点

**重要度: ★★★★☆ | 日付: 2026-04-30 | 出典: Palo Alto Networks公式, Cyber Magazine**

世界最大のサイバーセキュリティ企業Palo Alto NetworksがAIゲートウェイ企業Portkeyを買収（推定$120-140M）。Prisma AIRSに統合し、初の統一エージェントセキュリティ統制プレーンを構築。

- Portkey：月間数兆トークンを処理するAI Gateway、3行のコードで導入可能
- 3,000以上のLLM/MCPサーバー/エージェントへの安全なアクセスを提供
- Nikesh Arora CEO：「AIエージェントは特権的内部関係者になった」
- エージェントセキュリティがサイバーセキュリティの最前線カテゴリに

**Wikiカバレッジ**: ✅ カバー済み — `entities/portkey.md`, `entities/palo-alto-networks.md` (既存)

**Wiki関連**: [[entities/portkey]], [[entities/palo-alto-networks]], [[concepts/agent-governance]]

---

## 🔥 8. Grok 4.3 正式リリース — 1Mコンテキスト＋動画対応＋40%値下げ

**重要度: ★★★☆☆ | 日付: 2026-05-06 | 出典: Wikipedia, Apiyi, LLM Stats**

xAIがGrok 4.3を正式リリース。4月17日のベータ版からフルAPI公開に。1Mトークンコンテキスト、動画入力対応、推論常時ON。

- 速度：207 tokens/秒
- 価格：$1.25/$2.50 per Mトークン（前世代比40%削減）
- 16エージェントアーキテクチャ（SuperGrok Heavy）→ Agent-as-a-Serviceモデル
- バッチAPI：標準価格の50-80%割引

**Wikiカバレッジ**: ✅ カバー済み — `entities/grok-4-3.md`, `entities/xai.md` (既存)

**Wiki関連**: [[entities/grok-4-3]], [[entities/xai]]

---

## 📊 サマリー

| # | トピック | 重要度 | 日付 | Wiki状態 |
|---|---------|--------|------|---------|
| 1 | Nvidia-Corning $3.2B光ファイバー | ★★★★★ | 5/6 | ❌ 未カバー → 至急作成 |
| 2 | OpenAI MRCネットワーキングプロトコル | ★★★★★ | 5/5 | ❌ 未カバー → 至急作成 |
| 3 | Anthropic $200B Google契約 | ★★★★★ | 5/5 | ⚠️ 部分カバー → アップデート必要 |
| 4 | Samsung $1T, HBM4量産開始 | ★★★★☆ | 5/6 | ❌ 未カバー → 作成推奨 |
| 5 | GPT-5.5 Instantリリース | ★★★★☆ | 5/5 | ✅ カバー済み |
| 6 | Code with Claude 2026 | ★★★★☆ | 5/6 | ✅ カバー済み |
| 7 | Palo Alto/Portkey買収 | ★★★★☆ | 4/30 | ✅ カバー済み |
| 8 | Grok 4.3正式リリース | ★★★☆☆ | 5/6 | ✅ カバー済み |

**推奨Wikiアクション**: 上位4件（特に#1 Nvidia-Corning, #2 OpenAI MRC）のWiki未カバートピックを優先的に取り込む。Samsungエンティティページの新規作成も価値が高い。

## 📡 Newsletter/Blog Pipeline 状況

- **Newsletter最新**: 2026-05-07 (AINews/Anthropic-SpaceX Colossus, GPT-5.5 Instant, AI Delegation) — 処理済み
- **Blog RSS**: 最終スキャン 2026-05-05 (18記事処理済み)
- **Inbox rss-scans**: 5/3, 5/4, 5/5 の3件
- **Newsletter-ingest**: 空（最新処理は5/7完了）
