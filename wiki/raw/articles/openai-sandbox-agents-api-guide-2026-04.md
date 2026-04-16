# Sandbox Agents | OpenAI API (Python SDK)

**URL:** https://developers.openai.com/api/docs/guides/agents/sandboxes
**Published:** 2026-04-15
**Source:** OpenAI API Documentation
**Scraped:** 2026-04-16

---

OpenAI Agents SDKのSandbox Agentsに関する技術ドキュメント。

## 目的とユースケース
- **HarnessとComputeの境界分離:** 「Harnessはモデル周辺のコントロールプレーン... Computeはサンドボックス実行プレーンで、モデル指示によるファイル読み書き、コマンド実行、依存関係インストール、ストレージマウント、ポート公開、状態スナップショットを行う」
- **使用すべき場合:** ファイル操作、コマンド実行、データマウント、アーティファクト生成（CSV、JSONL、スクリーンショット、サイト）、ポート公開プレビュー、人間レビュー/レジュームワークフロー
- **使用すべきでない場合:** 永続ワークスペース不要の短いレスポンス → Responses APIまたは基本Agents SDKランタイム。稀なシェルアクセス → ホステッドシェルツール

## アーキテクチャとコアコンポーネント

| コンポーネント | 所有 | 設計焦点 |
|:---|:---|:---|
| `SandboxAgent` | エージェント定義 + サンドボックスデフォルト | エージェントの役割とデフォルトワークスペース設定 |
| `Manifest` | 新規セッションのワークスペース契約 | 初期ファイル、ディレクトリ、リポジトリ、マウント、環境、ユーザー/グループ |
| `Capabilities` | サンドボックスネイティブ動作 | ツール、インストラクション、ランタイム調整（Shell、FS、Skills、Memory、Compaction） |
| `Sandbox client` | プロバイダ統合 | 実行環境（Unix-local、Docker、ホステッド） |
| `Sandbox session` | 実行環境 | コマンド実行、ファイル変更、ポート公開、状態保持 |
| `SandboxRunConfig` | 実行セッションのソース/オプション | インジェクト、レジューム、または新規セッション作成 |
| `Saved state` | `RunState`、`session_state`、スナップショット | 後続実行の再接続または新規ワークスペースのシード |

## ワークスペース、Manifestとセキュリティ
- **パスルール:** Manifestパスは**ワークスペース相対のみ**。絶対パスや`..`エスケープ禁止（プロバイダ間のポータビリティ確保）
- **シークレット管理:** プロンプト、インストラクション、タスクファイル、コミットされたmanifestには決して埋め込まない

## Capabilitiesと実行フロー
- **デフォルトCapabilities:** `Filesystem()`、`Shell()`、`Compaction()`
- **Skills:** `Skills` キャパビティを使用して、繰り返し可能なインストラクション、スクリプト、アセットをサポート。遅延ロード(`LocalDirLazySkillSource`)、事前ステージング(`LocalDir`)、バージョン管理バンドル(`GitRepo`)に対応
- **ポート公開:** サービス、ノートブック、プレビューの実行用

## 標準実行ループ
1. `Manifest` ビルド（ワークスペースレイアウト）
2. `SandboxAgent` 作成（capabilities + instructions）
3. サンドボックスクライアント選択（実行環境）
4. `RunConfig(sandbox=SandboxRunConfig(...))` で実行
5. アーティファクトの検査、コピー、レジューム、またはスナップショット

## 状態管理、レジューム、メモリ
### セッション解決順序
1. `run_config.sandbox.session` → ライブセッション直接再利用
2. `RunState` からのレジューム → 保存済みサンドボックスセッション状態使用
3. `run_config.sandbox.session_state` → シリアライズ済み状態からの明示的レジューム
4. フォールバック → 新規セッション作成（`run_config.sandbox.manifest` または `agent.default_manifest` 使用）

### クロスランメモリ
- `Memory()` → 読み取り + 生成（デフォルト）
- `Memory(generate=None)` → 読み取り専用
- `Memory(read=None)` → 生成専用
- プログレッシブディスクロージャー: SDKが `memory_summary.md` をインジェクト → エージェントが `MEMORY.md` を検索 → ロールアウトサマリーを必要に応じて展開

## エージェント合成
- `SandboxAgent` はエージェント間で構成可能
- ワークフローの柔軟性を維持しつつ、セキュリティとスケーラビリティを確保
