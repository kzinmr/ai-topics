# Trending Topics — 2026-10-21

> 来源: blogwatcher RSS（直近3日 105件 / 本日 30件）+ HN Algolia（front page + keyword, min 60pts, 3日）
> 生成: trending-topics agent 12:00 UTC

## サマリー

本日最大のテーマは **AI セキュリティ**。ProjectDiscovery による「abliterated モデルのバックドア」実証と、Anthropic の「Claude による攻撃面削減」レポートが同時に出揃い、フロンティアモデルの攻撃／防御両面が焦点に。Mistral/DeepSeek/Google のモデル・インフラ発表群（Voxtral 3, Timestral, DeepInfer, TorchTPU, Mercury 3）は morning の active-crawl が既に収録済み。Anthropic の巨額赤字・IPO 観測は未収録（次インジェスト候補）。

## 収録済みトピック（本日朝のパイプライン済み）

| トピック | 状態 | 対象ページ |
|---|---|---|
| DeepInfer (DeepSeek 推論FW, 2263pts) | ✅ 済み | [[concepts/deepinfer]] |
| Timestral (Mistral 時系列基盤, 617pts) | ✅ 済み | [[concepts/timestral]] |
| Voxtral 3 (音声エージェントSDK, 703pts) | ✅ 済み | [[concepts/voxtral-3-voice-agent-sdk]] |
| TorchTPU (Google PyTorch TPU backend, 351pts) | ✅ 済み | [[concepts/torchtpu]] |
| Mercury 3 (Inception 拡散LLM) | ✅ 済み | [[concepts/mercury-3-diffusion-llm]] |
| Clairic / System One (Cloudflare 抽出モデル) | ✅ 済み | [[concepts/system-one-models]] |
| Hybrid Reasoning Agents (latent思考, 516pts) | ✅ 済み | [[concepts/hybrid-reasoning-agents]] |
| Self-hosted LLM proxy 観測 (301pts) | ✅ 済み | [[concepts/self-hosted-llm-proxy-observability]] |

## 今回新規収録（本 run）

| ソース | タイトル | NJ | アクション | 対象 |
|---|---|---|---|---|
| projectdiscovery.io | How abliterated models can get you pwned (239pts) | 4/5 | 新規ページ | [[concepts/abliterated-model-backdoor]] |
| anthropic.com/research | Using Claude to reduce the attack surface of code (69pts) | 3/5 | 既存更新 | [[concepts/ai-vulnerability-detection-at-scale]] |

### 1. Abliterated Model Backdoors（新規） — NJ 4/5
ProjectDiscovery（Prince Chaddha, 2026-10-06 / HN 239pts）が、**abliteration を口実に重みを編集した open モデルにトリガー条件付きバックドアを仕込む**攻撃を end-to-end で実証。7B モデルを OpenAI Codex CLI に組み込み、通常リクエストには全て正答しつつ、隠しトリガー語が出た瞬間にリポジトリ内の認証情報を外部へ exfiltrate。**バックドア構築コストは $50 未満**で eval も素通し。

- **ポイント**: メモリポイズニング（[[concepts/persistent-memory-attack-surface]]）が"データ層"の攻撃なのに対し、これは**モデル重み＝サプライチェーン層**の妥協。agent はモデルを信頼するため、既存の agent 側ガードレールではほぼ検知不能。
- abliteration（[[concepts/abliteration]]）が「重みを編集して再アップロードする」工程そのものなので、マルウェア埋め込みと正当な community fine-tune が区別不能になる。
- 防御: provenance 検証可能な重みのみ実行。ロード時検知手段は現時点で不存在（[[concepts/artifact-provenance-gates]]）。

### 2. Anthropic「Claude による攻撃面削減」（既存ページ更新） — NJ 3/5
Anthropic Frontier Red Team（Chris Rohlf, 2026-10-20 / HN 69pts）。フロンティアモデルを「脆弱性を発見する」だけでなく**防御側＝到達可能性の縮小**に使う研究。個別バグ修正はスケーリングが悪いのに対し、**到達可能なコード削減は未知の脆弱性の深刻度自体を下げる**。Claude を 25 の OSS プロジェクトで走らせ **493 件**の「出さなくていい到達可能コード」を発見。AI 脆弱性発見（[[concepts/ai-vulnerability-detection-at-scale]]）の防御版ミラー。

## 未収録の注目トピック（次インジェスト候補）

| トピック | ソース/点数 | 分類 |
|---|---|---|
| Anthropic 上半期純損失 $80B超 + IPO "obscure trust" | Reuters/WSJ 各151pts | 産業・経済 |
| OpenAI Alignment「Beyond g-mean²: monitorability 補完メトリクス」 | OpenAI 公式 | アラインメント |
| Claude がサソリ神経毒の protein binder を設計 | Anthropic 108pts | 応用・科学 |
| Websites are closing their doors to AI agents | The Verge 157pts | agent・Web |
| Steam「No AI」フィルタ要求 / Vibecoder氾濫 | IGN 179pts | AI-slop・文化 |
| Publish fake stats, get cited in LLMs | peec.ai 345pts | LLM汚染 |
| Anthropic 提案 AI 安全法案（50人死亡/$1Bで発動） | Tom's Hardware 172pts | 規制 |

## 統計
- blogwatcher 直近3日: 105件 / 本日発見 30件（AI Engineer 22, daringfireball 18, LWN 11, simonwillison 7 …）
- HN front page AI系: DeepInfer 2263, Voxtral 3 703, Timestral 617, TorchTPU 351, attack-surface 67 他
- 今回: 新規 concept 1 / 更新 2 / raw 2 / SCHEMA tag 1追加（model-backdoor）
