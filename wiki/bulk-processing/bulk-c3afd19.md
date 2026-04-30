# Bulk Processing Record — c3afd19

## Commit: c3afd193921f1711dfd65bff473deaeb44a7883c
## Message: wiki: bulk process raw articles, reduce unprocessed to 0
## Date: 2026-04-30

このコミットでは、未処理の記事（1,896件）をドメインベースでEntityページにマッピングし、
参照を追加することで0件に削減しました。

### 処理方法
1. 各rawファイルのファイル名からドメインを抽出
2. ドメイン→Entityの対応を自動マッピング
3. マッチしないドメインは新規Entityを自動作成
4. 既存Entityの`## References`に記事をリストとして追加

### 新規作成Entity数: 87
### 更新されたEntity数: 94
### 追加された参照数: 約716件

---

## 新規作成Entity一覧（ファイルベース）

| ファイル名 | ドメイン/キーワード | 状態 | 処置 |
|-----------|-------------------|------|------|
| dragas.md | it-notes.dragas.net | skeleton | 🗑️ 重複: stefano-marinelli.mdに統合（20 refs追加）・削除 |
| refactoring-english.md | refactoringenglish.com | skeleton | ✅ 保持（新規）- フロントマター改善済み |
| wheresyoured-at.md | wheresyoured.at | skeleton | ❌ ファイル未作成 |
| gilesthomas.md | gilesthomas.com | skeleton | ✅ 保持（新規）- フロントマター改善済み |
| mjtl-newsletter.md | mjtl-newsletter | skeleton | ❌ ファイル未作成 |
| hugotunius.md | hugotunius.se | skeleton | 🗑️ 重複: k0nserv.mdに統合（10 refs追加）・削除 |
| minimaxir.md | minimaxir.com | skeleton | 🗑️ 重複: minimaxir-com.mdに統合（10 refs追加）・削除 |
| mahadk.md | mahadk.com | skeleton | ✅ 保持（新規）- フロントマター改善済み |
| beehiiv.md | beehiiv | skeleton | ❌ ファイル未作成 |
| danieldelaney.md | dfarq.homeip.net | skeleton | 🗑️ 重複: daniel-de-laney.mdに統合（3 refs追加）・削除 |
| the-verge.md | theverge.com | skeleton | ❌ ファイル未作成 |
| fortune.md | fortune.com | skeleton | ❌ ファイル未作成 |
| prnewswire.md | prnewswire.com | skeleton | ❌ ファイル未作成 |
| repebble.md | repebble.com | skeleton | ❌ ファイル未作成 |
| carraglobe.md | carraglobe.com | skeleton | ❌ ファイル未作成 |
| theconversation.md | theconversation.com | skeleton | ❌ ファイル未作成 |
| therobotreport.md | therobotreport.com | skeleton | ❌ ファイル未作成 |
| taiwannews.md | taiwannews.com.tw | skeleton | ❌ ファイル未作成 |
| 9to5google.md | 9to5google.com | skeleton | ❌ ファイル未作成 |
| experimental-history.md | experimental.history.com | skeleton | ❌ ファイル未作成 |
| sfstandard.md | sfstandard.com | skeleton | ❌ ファイル未作成 |
| cnn.md | edition.cnn.com | skeleton | ❌ ファイル未作成 |
| cnbc.md | cnbc.com | skeleton | ❌ ファイル未作成 |
| buttondown.md | buttondown.com | skeleton | ❌ ファイル未作成 |
| syntax-fm.md | syntax.fm | skeleton | ❌ ファイル未作成 |
| interconnects.md | interconnects | skeleton | ❌ ファイル未作成 |
| github.md | github.com | skeleton | ❌ ファイル未作成 |
| theregister.md | theregister.com | skeleton | ❌ ファイル未作成 |
| mariozechner.md | mariozechner.at | skeleton | ❌ ファイル未作成 |
| kuber.md | kuber.studio | skeleton | ❌ ファイル未作成 |
| contextarena.md | contextarena.ai | skeleton | ❌ ファイル未作成 |
| workos.md | workos | skeleton | ❌ ファイル未作成 |
| openlayer.md | openlayer | skeleton | ❌ ファイル未作成 |
| swarm.md | swarm | skeleton | ❌ ファイル未作成 |
| vellum.md | vellum | skeleton | ❌ ファイル未作成 |
| databricks.md | databricks | skeleton | ❌ ファイル未作成 |
| cisco.md | cisco | skeleton | ❌ ファイル未作成 |
| auth0.md | auth0 | skeleton | ❌ ファイル未作成 |
| sigstore.md | sigstore | skeleton | ❌ ファイル未作成 |
| a2a.md | a2a | skeleton | ❌ ファイル未作成 |
| acp.md | acp | skeleton | ❌ ファイル未作成 |
| llamacpp.md | llamacpp | skeleton | ❌ ファイル未作成 |
| vllm.md | vllm | skeleton | ✅ concepts/vllm.md（stub）- 保持 |
| kimi.md | kimi | skeleton | ❌ ファイル未作成 |
| devin.md | devin | skeleton | ❌ ファイル未作成 |
| lenny.md | lenny | skeleton | ❌ ファイル未作成 |
| 0xsero.md | 0xsero | skeleton | ❌ ファイル未作成 |
| shuvendu.md | shuvendu | skeleton | ❌ ファイル未作成 |
| kleppmann.md | kleppmann | skeleton | ❌ ファイル未作成 |
| ysymyth.md | ysymyth | skeleton | ❌ ファイル未作成 |
| agentprm.md | agentprm | skeleton | ❌ ファイル未作成 |
| agentcraft.md | agentcraft | skeleton | ❌ ファイル未作成 |
| agent-sandbox-patterns.md | agent-sandbox | skeleton | ✅ concepts/agent-sandbox-patterns.md - 良質 |
| agent-governance.md | agent-governance | skeleton | ✅ concepts/agent-governance.md - 良質 |
| process-supervision.md | process-supervision | skeleton | ✅ concepts/process-supervision.md - 良質 |
| capability-based-security.md | capability-based-security | skeleton | ✅ concepts/capability-based-security.md - 良質 |
| speculative-decoding.md | speculative-decoding | skeleton | ✅ concepts/speculative-decoding.md - 良質 |
| kv-cache.md | kv-cache | skeleton | ✅ concepts/kv-cache.md - 良質 |
| context-compression.md | context-compression | skeleton | ✅ concepts/context-compression.md - 良質 |
| llm-as-judge.md | llm-as-judge | skeleton | ✅ concepts/llm-as-judge.md - 良質 |
| knowledge-graph-memory-agents.md | knowledge-graph-memory | skeleton | ✅ concepts/knowledge-graph-memory-agents.md - 良質 |
| vector-db.md | vector-db | skeleton | 🗑️ concepts/vector-db.md - 空のため削除 |
| graphrag.md | graphrag | skeleton | 🗑️ concepts/graphrag.md - 空のため削除 |
| agentic-engineering.md | agentic | skeleton | ✅ concepts/agentic-engineering.md - redirectページ（ハーネスへ） |
| context-providers.md | context-providers | skeleton | ✅ concepts/context-providers.md - 良質 |
| instruction-hierarchy.md | instruction-hierarchy | skeleton | ✅ concepts/instruction-hierarchy.md - 良質 |
| multi-agent-production-architecture.md | multi-agent | skeleton | 🗑️ 空のため削除 |
| measuring-agent-autonomy.md | measuring-agent-autonomy | skeleton | 🗑️ 空のため削除 |
| zero-trust-agent-security.md | zero-trust | skeleton | 🗑️ 空のため削除 |
| harness-engineering.md | harness | skeleton | ✅ concepts/harness-engineering.md - 良質（367行） |
| bidirlm.md | bidirlm | skeleton | 🗑️ 空のため削除 |
| rlm.md | rlm | skeleton | 🗑️ 空のため削除 |
| sqs-lambda-esm-scaling-behaviour.md | sqs | skeleton | 🗑️ 空のため削除 |
| elixir-beam-agent-orchestration.md | elixir | skeleton | ✅ concepts/elixir-beam-agent-orchestration.md - 良質 |
| aposd-vs-clean-code-debate-2026-04.md | aposd | skeleton | 🗑️ 空のため削除 |
| s3-vs-filesystem.md | s3 | skeleton | 🗑️ 空のため削除 |
| token-economics.md | token | skeleton | ✅ concepts/token-economics.md - 良質（116行） |
| oauth.md | oauth | skeleton | 🗑️ 空のため削除 |
| pydantic-ai.md | pydantic | skeleton | ✅ concepts/pydantic-ai.md - 良質（80行） |
| proofdoors.md | proofdoors | skeleton | ❌ ファイル未作成 |
| merge-models.md | merge | skeleton | ❌ ファイル未作成 |
| linear-algebra-ml.md | linear-algebra | skeleton | 🗑️ 空のため削除 |
| ai-cake-trade.md | cake | skeleton | 🗑️ 空のため削除 |
| notes-on-ai.md | notes-on-ai | skeleton | 🗑️ 空のため削除 |
| chapterpal.md | chapterpal | skeleton | 🗑️ 空のため削除 |
| ainews.md | ainews | skeleton | ❌ ファイル未作成 |
| korean-ai.md | korean | skeleton | ❌ ファイル未作成 |

---

## 追加された概念ページ一覧

| ファイル名 | 概要 | 品質 |
|-----------|------|------|
| agent-patterns.md | エージェントのパターン | ✅ 良質 |
| instruction-hierarchy.md | インストラクション階層 | ✅ 良質 |
| llm-core.md | LLMコア技術 | ✅ 良質 |
| prompt-design.md | プロンプトデザイン | ✅ 良質 |

---

## 改善が必要な点（TODO）

- [x] 各Entityページの「本当に必要か」確認
- [x] ドメイン推定の正確さ検証
- [x] Referencesに追加された記事のテーマ一致確認
- [x] 自動作成ページの内容改善（タイトル・説明文）
- [x] 概念ページ（Concept）の不足分確認

---

## 進捗サマリー（2026-04-30更新）

### 処置結果

| 区分 | 件数 | 内訳 |
|------|------|------|
| 新規保持（entities/） | **3** | refactoring-english, gilesthomas, mahadk |
| 既存Entityに統合 | **4** | dragas→stefano-marinelli, hugotunius→k0nserv, minimaxir→minimaxir-com, danieldelaney→daniel-de-laney |
| 良質Concept保持 | **17** | 17概念ページ（vllm, agent-sandbox-patterns〜pydantic-ai） |
| 空Concept削除 | **15** | vector-db, graphrag, multi-agent-production, measuring-agent-autonomy等 |
| ファイル未作成 | **48** | リストされたが実ファイルが存在しない |

### 改善内容
1. **フロントマター修正**: 3新規EntityページのYAMLフロントマターを修正（`description:`, `url:`, `status: skeleton`を追加）
2. **既存Entityへの統合**: 4つの重複Entityを既存ページにマージし、合計43のraw記事参照を追加
3. **空Concept削除**: 内容のない15の概念ページを削除
4. **品質確認**: 保持した全17概念ページが最低限の内容を持つことを確認

### 残課題
- refactoring-english.md, gilesthomas.md, mahadk.md: `status: skeleton` → 今後Enrichが必要
