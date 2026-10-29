# Trending Topics — 2026-10-29 (12:00 UTC)

HN Algolia（front page + キーワード）+ 朝パイプライン（blog-ingest 20件 / newsletter-triage 5通）+ web supplement。ウィキ未収録の高重要度トピックを優先選別。

## 🏆 トップトレンド

### 1. アンチLLM難読化 — 「バイオ兵器関数名」でAI監査を弾く指紋採取スクリプト（HN 1314pts）🆕
nullpt.rs の veritas が Tranco 上位1万サイトをクロールし発見。ロシア系アンチ-DDoS企業 servicepipe.ru の canvas 指紋採取スクリプトに、`computeRicinLethalDosageForWaterSupply` 等のバイオテロ風関数名＋不可視Unicodeに隠した偽ジェイルブレイク文＋中国検閲ワードを埋め込み。**デオブfuscate 依頼に対し Astra・Daybreak Blue は拒否、GLM-5.3 は従順**。スクリプト本体は至って普通のナビ/WebGL シグナル収集だけで「難読化の作り込みの割に信号が肩透かし」。LLM支援マルウェア解析の定番化に伴い、リフュージョ自体を防御壁にする新脅威モデル。
→ 新規: `concepts/anti-llm-obfuscation.md` | [HN](https://news.ycombinator.com/item?id=50276998)

### 2. Qwenputer — Qwen3.5 の重みの中にコンパイルされた RV32I RISC-V CPU（HN 532pts）🆕
Gated DeltaNet（線形RNN）レイヤーを gate=1/β=1/one-hot キーで**完全正確な RAM** に転用し、訓練なし・コンパイラだけで RISC-V CPU を重みに埋め込み。C/MicroPython が forward pass 内で動く（プラグインでもサンドボックスでもない）。L4 1枚・約3,200 CPUトークン/秒。副次成果が本題で、**RNN 状態に思考を隠して CoT モニタリングを回避**する研究と、**モデルが消せない重み内モニター**（解釈可能性の answer key）という dual-use 性。fast weights（Schlag et al. ICML 2021）の2026年版実装。
→ 新規: `concepts/weight-compiled-computers.md` | [HN](https://news.ycombinator.com/item?id=50282838)

### 3. Google AI Mode が「2020年大統領選の勝者は」にだけ FEC へはぐ（Ars Technica）🆕
2020・2024・2012のみ間接回答（FEC や American Presidency Project へ誘導）、2000年以降の其它は即答。ユーザーごとに挙動が異なり、**米国以外（台湾・露・仏・加VPN）では全部まともに答える**、2回聞くと答える——ベースモデルの能力差ではなく**US市場限定の製品層ガードレール**と断定できる証拠列。Gemini チャットボット・ChatGPT・Claude・政府製 America.gov は全部直接答える点が対照的。
→ 新規: `concepts/model-level-political-censorship.md` | [HN](https://news.ycombinator.com/item?id=50280178)

### 4. Google Research「Sleep Framework」— 継続学習に睡眠フェーズを導入 ⚠️ 更新で対応
MoE（Hope アーキテクチャ）の事前確保済み低ランクエキスパートを睡眠中に開錠し、**自己生成練習問題で重み更新**。10M トークンのコンテキストを破滅的忘却なく長期記憶化＋推論精度向上。Letta の sleep-time compute（重み凍結）との差は「睡眠中が自動 post-training サイクル」であること。Dwarkesh の「dreaming 第4のスケーリング軸」の正式研究版。
→ 更新: `concepts/continual-learning.md` + `concepts/sleep-time-compute.md` | [HN](https://news.ycombinator.com/item?id=50272479)

### 5. Cursor Agent SDK GA — 「agents defined as code」戦線に IDE ベンダーが参入（HN 132pts）⚠️ 更新で対応
Bugbot / Security Reviewer / Rollouts の内部フレームワークを外部開放。PRイベント駆動＋リスク評価ルーティング、subagent 並列、**evals・イベントリプレイ内蔵**、`agent-sdk deploy` 一発。PGA Tour が「ソフトウェア開発工場」を丸ごとこの SDK 上で運用。Anthropic Claude Agent SDK / OpenAI Agents SDK との三つ巴構図。
→ 更新: `entities/cursor-ai.md` | [HN](https://news.ycombinator.com/item?id=50273731)

### 6. Amazon、Nova 首切り — AGI研究SF拠点閉鎖、Abbeel 率いる単一フロンティア体制へ（HN 376pts）⚠️ raw のみ
Bloomberg 報道（Futurism 転載）: テキスト/画像/動画 Nova 一式を「keep the lights on」化、AGI研究80人SFオフィスを1週間前に閉鎖、計算資源は Pieter Abbeel のロボティクス寄りフロンティア effort に集中。ハイプサイクル自主降板説。一次ソース（Bloomberg）未取得のため raw 保存のみ、ページ未作成。
→ raw: `futurism.com--amazon-nova-gutting--9a4d6f22.md` | [HN](https://news.ycombinator.com/item?id=50261589)

### 7. 午前パイプライン由来（収録済み/参照）
- **Gemini 4 Carbon**（HN 955pts, 955c）— blog-ingest が raw 取得済み（`2026-10-28_gemini-4-carbon.md`）。Layer2 ページ化は次ジョブ候補 ✅ raw済み
- **Claude Code が background agent の transcript を毎回モデルに送信**（HN 428pts, 本日上陸）— raw 取得済み（`2026-10-29_claude-code-background-agent-transcript-exfiltration.md`）。agent-observability/プロバイダデータ経路の論点 ✅ raw済み
- **DAYJOB: Tax**（Surge AI, 50環境・1,789ファイル、"クライアントが知らない重要期限を気づけるか"）— 既存 `concepts/dayjob-benchmark.md` に税ドメイン追記候補 ✅ 既存
- **MicroZig が No-LLM 規約採用**（HN 51pts）— 本朝 blog-ingest 収録済み ✅
- **Kentucky 人文主義者が AI 利用の宗教的免除初の承認**（HN 468pts）— Religion News 403 で本文未取得・低優先スキップ
- **StackOverflow 月間質問数 <1,000**（HN 532pts）— data.stackexchange 403、LLM時代 の Q&A デススパイラル論点。次回の web supplement 候補 ⚠️ 未収録

## 📊 ウィクション推奨アクション

| トピック | 状態 | 対象 |
|---|---|---|
| アンチLLM難読化 | ✅ 済み — `concepts/anti-llm-obfuscation.md` | 新規作成 |
| Qwenputer / 重みコンパイルCPU | ✅ 済み — `concepts/weight-compiled-computers.md` | 新規作成 |
| AI Mode 政治的回答回避 | ✅ 済み — `concepts/model-level-political-censorship.md` | 新規作成 |
| Sleep Framework（継続学習） | ✅ 済み — `concepts/continual-learning.md` | 追記 |
| Cursor Agent SDK | ✅ 済み — `entities/cursor-ai.md` | 追記 |
| Amazon Nova 縮小 | ⚠️ raw のみ | Bloomberg 一次取得後に entity 化候補 |
| Gemini 4 Carbon | ✅ raw済み | ページ化は次ジョブ（events/） |
| Claude Code transcript 送信 | ✅ raw済み | observability ページ更新候補 |
| StackOverflow 質問枯渇 | ⚠️ 未収録 | 一次ソース取得可否を確認の上で判断 |

## 取得失敗/制限
- data.stackexchange.com（403）/ religionnews.com（403）— urllib Chrome UA でも不可
- Bloomberg（Amazon Nova 一次ソース）— 課金壁、Futurism 転載で代替

SCHEMA: +12タグ（weight-compilation, neural-computers, gated-deltanet, risc-v, chain-of-thought-monitoring, model-censorship, agent-as-code, anti-bot, browser-fingerprinting, safeguard-evasion, jailbreak-bait, obfuscation）
