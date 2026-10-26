# Hot Post 2026-10-26 21:30 (night)

## 見出し候補
A. 🏆 2015年のCNNが Fable 5.1 に 20勝 — 「スケール信仰」の反証が2日連続で HN 上位
B. 📊 規模の反対側: 2.3× 高速化と 20pt 精度差が示す「モデル選択の局所最適化」
C. Frontier が落とす 2 軸 — 知覚と前処理。両方とも leaderboard に載らない

## 採用

---

# 🏆 2015年のCNNが Fable 5.1 に 20勝 — 「スケール信仰」の反証が2日連続で HN 上位

**▶ 一言要約**: 20分 fine-tune した 2015年アーキテクチャの Inception v3 が、200病変の皮膚癌診断で GPT-6 Astra 42% / Claude Fable 5.1 42% に対し 62% の正答率 — HN 571pts。

**詳細**([[concepts/specialist-model-superiority]]、Dr Magnus Lynch, lynchlab.net 2026-10-25):
- 生検確定200病変・6択診断: CNN 125正解 vs LLM 84/85。メラノーマ30例の捕捉も CNN 13 vs LLM 8/11
- **attractor label 病**: GPT-6 Astra は200例中75例を basal cell carcinoma に寄せる(実際25例)。そのうちメラノーマ14例を誤って BCC 判定。Fable 5.1 は actinic keratosis に53例(実際20例)
- 良性病変の「見逃し方向」で LLM が大きく劣化(naevi 26–66%)— 不要生検を生む失敗側。CNN は 74%
- 患者視点で「受診が必要?」と聞くと両 LLM ともほぼ100%受診を推奨 — 安全だがトリアージとして無価値。calibrated threshold は CNN のみ
- 著者の留保も明記: n=200と小、CNN は意図的な baseline(規制済み ViT ensemble 製品はもっと良い)、MILK10k は2025年公開で LLM 側に contamination の可能性

## 対比: 同じ週の別実証

**▶ 一言要約**: Skyvern はブラウザエージェントから RAG 的前処理(screenshot+annotation)を丸ごと削除して 2.3× 高速・22.5% 安価化 — HN 21pts と静かだが数値は鋭い。

**詳細**([[concepts/skyvern-progressive-disclosure]]、Skyvern 2.0→3.0、A/B 実測):
| 指標 | 2.0 | 3.0 |
|---|---|---|
| 平均実行時間 | 593 s | 262 s |
| コスト/run | $0.039 | $0.0302 |
| screenshot 使用率 | 27% | 2.7% |
| prompt cache hit | 27% | 79.7% |
| tokens/run | 188K | 286K (+52%) |
| turns/run | 6.4 | 23 |

- 52%トークン増でも安くなる理由: vision encoder がテキスト比 1.7× の遅延税。image call を 90% 削って prefix を安定させると cache hit が 27%→79.7%、cache 単価の約70%割引がトークン増を相殺
- RAG 的「操作可能要素の要約」自体が誤りの発生源だった(「100%正確に要素を識別できるなら」うまくいった)
- 設計含意: エージェントのコスト支配変数は検索品質ではなく [[concepts/prompt-caching]]。[[concepts/bitter-lesson-agent-harnesses]] の「作るものを減らせ」の計測版

## 夜間だから言える逆張り解釈

1. 2日連続で同じ方向の証拠: 皮膚癌 CNN(HN 571)→ Skyvern RAG 削除。共通変数はモデル規模ではなく**入力モダリティと前処理の設計**。leaderboard はこの軸を一切測っていない
2. 前例は wiki に既に堆積している: [[concepts/domain-specialization-beats-general-scale]]、ByteDance の OCR ensemble [[entities/indra-ocr-agent]]、Jev クラスの [[concepts/system-one-models]]。Skyvern 自身が次に system-one 採用を予告(現状は 64K context・画像不可で却下、6–12ヶ月後に viable 見込み)
3. 逆張りPart 2: LLM が「安全」に振る舞うとき精度評価は偽陽性になる — 患者フレーミングで両 LLM とも99%受診推奨。「安全なはず」の frontier モデルは calibrated threshold を持たない。ここは [[concepts/monitorability-metrics]] の問題設定と接続する
4. 冷や水: CNN 勝ちは dermatology という閉じた知覚タスク限定。汎用エージェントの判断・計画まで specialist に置き換わる主張は今の証拠では裏付かない

## 関連
- [[concepts/multimodal]] / [[concepts/small-language-models]] — 知覚タスクの住み分け
- [[concepts/context-engineering/_index]] — 「リトリーバを消す」分岐
- 朝の枠は [[concepts/kimi-k3]] 価格差、昨夜は inside-the-model cluster。本投稿は重複なし

## Sources
- https://lynchlab.net/llm-skin-cancer — raw: `raw/articles/2026-10-26_lynch_CNN-vs-LLM-skin-cancer-diagnosis.md`
- https://www.skyvern.com/blog/deleting-rag-from-our-web-agent-made-it-2-3x-faster/ — raw: `raw/articles/2026-10-26_skyvern_skyvern-progressive-disclosure.md`
