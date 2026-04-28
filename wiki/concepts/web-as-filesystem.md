---
title: "Web-as-Filesystem (Nia Docs)"
type: concept
aliases:
  - web-filesystem
  - agentsearch
  - nia-docs
  - documentation-shell
tags:
  - concept
  - web-filesystem
  - documentation
  - rags
  - agent-tools
status: complete
description: "Webの全ドキュメントをUnixファイルシステムとしてマウントする抽象化。エージェントにtree/grep/cat/findを自然に使い、コード幻覚を解消。"
created: 2026-04-27
updated: 2026-04-27
sources:
  - "https://x.com/i/article/2041215978957389908"
related:
  - "[[rags]]"
  - "[[concepts/agent-harnesses]]"
  - "[[concepts/mcp]]"
---

# Web-as-Filesystem (Nia Docs)

> **Definition:** Webの全ドキュメントをUnixファイルシステムとしてマウントする抽象化。エージェントに`tree`、`grep`、`cat`、`find`を自然に使い、コード幻覚を解消。

## 問題: コード幻覚はモデルの問題ではない

- APIは破壊的変更、endpointのdeprecated、parameterのリネームを毎日行う
- モデルのtraining dataは数ヶ月〜数年古い
- エージェントは完璧に見えるコードを書くが、ランタイムで失敗する

## RAGの限界
- ドキュメントをchunkし、embeddingし、top-Kをretrieve
- 答えが3ページにまたがる場合やexact function signatureがchunkingで失われる場合に対応できない
- Retrievalはフラグメントしか与えないが、エージェントは全体像を必要とする

## ファイルシステム抽象化の提案

### Unixの知恵
50年前にUnixは解決した: devices、processes、sockets — すべてfiles。`open`、`read`、`write`、`close`。一つinterface。

### エージェントはUnixを事前学習済み
- 数十億tokenのfilesystem interactionがweightsに baked in
- `tree`、`grep`、`find` — agentsが使うためのツールではなく、already知っているツール
- 全コーディングモデルが数百万の`cat README.md`、`grep -r "auth" .`、`find . -name "*.md"`の例を学習済み

### MCPとの比較
- MCP: 各toolにJSON schema、natural-language description、careful argument constructionが必要
- ファイルシステム: その何もない。context windowを消費せず、misuseのsurfaceもなし

> "@jerryjliu0: an agent with filesystem tools and a code interpreter is just as general, if not more general, than an agent with 100+ MCP tools."

## 仕組み

### 1. Index
- URLに初めてアクセスした際、backendがsiteをcrawl
- `llms.txt`を尊重、OpenAPI specsを検出、redirectsを処理
- 各pageがfileになる
- 例: `https://docs.stripe.com/api/charges/create` → `/api/charges/create.md`
- Path normalization: common path prefixをauto-detectしstrip（`/docs/`、`/api/reference/`などの一貫しない構造を吸収）

### 2. Serve
- filesystem operationsをAPI endpointsとしてexpose
- 全responseをgzip圧縮
- `/load` endpointがstatusと全filesをsingle requestで返す
- cache: `Cache-Control: public, max-age=300`
- CLIがdisk cacheを`~/.cache/nia-docs/`に保持
- namespaceはshared（unauthenticated by design）

### 3. Shell
- client側で実行（container/sandbox/VMなし）
- just-bash（TypeScript reimplementation of bash）
- grep、cat、ls、find、cd、tree、pipes、aliasesをサポート
- 全filesystemがin-memory JavaScript object
- large sites（1,000+ pages）: file treeをupfrontにloadし、catでlazy fetch

## なぜリアルなサンドボックスではないのか
- Boot time: ~100ms（cached）、~2s（already indexed）、~30-120s（cold index）
- Per-session compute: server側でzero
- 読み取り専用のstatic text workloadにmicro-VMを借りる必要はない

## エージェントへのセットアップ
エージェントのinstruction fileに追記するだけで利用可能:
- Claude Code、Cursor、Copilot、Codex、Gemini CLI、OpenCodeに対応
- `-c` flagでsingle command実行→exit。interactive session不要

## 初期データ: エージェントの標準ワークフロー
1. `tree` — 方向性を確認
2. `grep -rl` — 関連ファイルをfind
3. `cat` — 読む

これはhuman developerが取るのと同じパターン。ファイルシステム抽象化はagentsが覚えるものではなく、与えられた時にdefault取るもの。

## 将来展望
- API referenceはdirectory
- Changelogはfile
- OpenAPI specはJSONをcatできる
- 全webがcodebaseのようにnavigate可能になるインフラを構築中

## Sources
- [Turning the entire web into a filesystem](https://x.com/i/article/2041215978957389908) (2026-04-22, X article) — Arlan Rakhmetzhanov (Nozomio Labs CEO) — Nia's documentation shell
- [AgentSearch.sh](https://www.agentsearch.sh/) — live demo
