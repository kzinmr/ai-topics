# RSS Daily Scan Report — 2026-08-10

## スキャン結果
- **blogwatcher記事数**: 25件（DB発見、blog 21 + AI Engineer YouTube 4）
- **AI関連**: 約12件
- **保存済み raw articles**: 17件（blog_ingest）
- **ニュースレター**: 6通（106リンク）— take 6件 / reference 1件 / skip 9件
- **Xブックマーク新規**: 2件 / **Xアカウント投稿**: 7件
- **HN補完**: 20件（Claude Code Auto Mode、Muse Glimmer、Docker Sandboxes 等）

## AI関連トリアージ（blog）

### 優先度: 高（take）
| ソース | タイトル | NJスコア | アクション |
|--------|----------|----------|------------|
| simonwillison.net | GitHub Models is now retired | 4/5 | concepts/github-models.md 新規作成 |
| seangoedecke.com | Advanced AI sycophancy | 4/5 | concepts/ai-sycophancy.md 追記 |
| tedium.co | Vibe-Coded Flattery（Dark Hours論争） | 4/5 | events/dark-hours-controversy-2026.md 新規作成 |

### 優先度: 中（reference）
| ソース | タイトル | NJスコア | アクション |
|--------|----------|----------|------------|
| simonwillison.net | Claude Opus 5 system prompt（Fable 5輸出規制） | 3/5 | concepts/claude/fable-5.md 追記 |
| simonwillison.net | SQLite compressed text-history | 3/5 | entities/simon-willison.md 追記 |
| blog.jim-nielsen.com | A License to Act | 3/5 | entities/jim-nielsen.md 追記 |
| pluralistic.net | Bureaucratic AI arms-race | 3/5 | entities/cory-doctorow.md 追記 |

### 優先度: 低（skip 13件）
Fringe劇評×3、Doomerism論、数値計算×2、ユーモア、UPS個人話、LWN kernel×2 等

## AI関連トリアージ（newsletter）

### take 6件
| ソース | タイトル | アクション |
|--------|----------|------------|
| SemiAnalysis | TileRT InferenceX 独立ベンチ | entities/tilert.md 追記 |
| AI by Aakash | Claude Code 5 setup ガイド | concepts/claude-code/claude-code-steering-methods.md 追記 |
| Interconnects | Lessons from the hacks | events/openai-huggingface-incident-july-2026.md 追記 |
| The Signal | Hark Handoff | entities/hark.md 追記 |
| The Signal | ByteDance Seedance 2.5 + 10Tモデル報道 | entities/bytedance.md 追記 |
| Superintel+ | Eve CEOインタビュー | entities/eve-legal-ai.md 新規作成 |

### reference 1件
| ソース | タイトル | アクション |
|--------|----------|------------|
| The Signal | Google TPU × Anthropic 統計 | entities/google.md 追記 |

## 重要な発見
- **Claude Code Auto Mode デフォルト化**（8/7、HN 240pt）— Pro/Max/Teamで自動モードが標準に、人間レビューより危険コマンドを多く検出
- **Meta Muse Glimmer**（8/10）— 30Bオープン・エージェントモデル、Apache 2.0、コンシューマGPUでローカル実行
- **TileRT** — B200 8GPUで340 tok/s/user、GB300 NVL72比1.9倍
- **Hark Handoff** — コンピューター操作エージェント、$0.18/M入力トークン
- **ByteDance** — Seedance 2.5動画モデル＋10Tパラメータ事前学習報道（FT）
- **OpenAI Astra** — サイバーセキュリティ評価公開（Boaz Barak）
