---
title: "Rodney — Browser Automation CLI for Agents"
aliases:
  - rodney
  - rodney-cli
created: 2026-04-12
updated: 2026-04-12
tags:
  - tool
  - agentic-engineering
  - browser-automation
  - testing
status: draft
sources:
  - "https://simonwillison.net/2026/Feb/10/showboat-and-rodney/"
  - "https://simonwillison.net/2026/Feb/17/rodney/"
  - "https://github.com/simonw/rodney"
---

# Rodney

Simon Willisonが開発した**Chrome DevTools ProtocolベースのCLIブラウザ自動化ツール**。コーディングエージェントがWeb UIをテスト・検証するために設計。

## 背景

> "I went looking for good options for managing a multi-turn browser session from a CLI and came up short, so I decided to try building something new."

既存のブラウザ自動化ツール（Playwright、Selenium）はエージェントのCLI使用に適していなかったため、Willisonが自作。

## 技術スタック

- **ベース**: [Rod](https://go-rod.github.io/) Go library — Chrome DevTools Protocolの包括的ラッパー
- **CLI**: Goバイナリ（数MBにコンパイル）、またはPython経由で `uvx rodney`
- **名前の由来**: Rod library + Only Fools and Horsesへのオマージュ

## 設計哲学

> "This tool is not designed to be used by humans! The goal is for coding agents to be able to run `rodney --help` and see everything they need to know to start using the tool."

**エージェントファーストCLI**: ヘルプテキストがLLMの消費用に構造化されている。

## 主要コマンド

| コマンド | 説明 |
|----------|------|
| `rodney start` | バックグラウンドでChromeを起動 |
| `rodney start --show` | ブラウザウィンドウを可視化（デバッグ用） |
| `rodney open URL` | ページを開く |
| `rodney waitstable` | ページの読み込みが安定するまで待機 |
| `rodney js '...'` | JavaScriptを実行し結果を取得 |
| `rodney click SELECTOR` | 要素をクリック |
| `rodney exists SELECTOR` | 要素の存在を確認 |
| `rodney visible SELECTOR` | 要素の可視性を確認 |
| `rodney assert` | JavaScriptテストを実行、失敗時exit code 1 |
| `rodney connect PORT` | 既存のChromeインスタンスに接続 |
| `rodney reload --hard` | ハードリロード |
| `rodney clear-cache` | キャッシュクリア |

## Showboatとの連携

Rodneyは[[showboat]]と組み合わせて使用することで、エージェントのWeb UIテストを**検証可能・監査可能な成果物**として記録できる。

```bash
showboat exec demo.md bash 'rodney start && rodney open https://example.com && rodney waitstable && rodney exists "h1"'
```

この組み合わせにより:
1. エージェントが実際にブラウザを操作
2. その操作と結果がMarkdownドキュメントに記録
3. 後から検証・レビュー可能

## テストパターン

### 基本的なWebアプリテストスクリプト
```bash
#!/bin/bash
set -euo pipefail

FAIL=0
check() {
    if ! "$@"; then
        echo "FAIL: $*"
        FAIL=1
    fi
}

rodney start
rodney open "https://example.com"
rodney waitstable

# Assert elements exist
check rodney exists "h1"
# Assert key elements are visible
check rodney visible "h1"
check rodney visible "#main-content"

if [ "$FAIL" -ne 0 ]; then
    echo "Some checks failed"
    exit 1
fi
echo "All checks passed"
```

## コンテキスト管理との関係

Rodneyのコマンドは**コンテキストウィンドウに優しい**:
- テキストベースの出力のみ（LLMが直接解釈可能）
- スクリーンショットもファイルとして保存、URLで参照
- PlaywrightのフルAPIをコンテキストに入れる必要がない

## 比較: ブラウザ自動化ツール

| ツール | 開発元 | 特徴 |
|--------|--------|------|
| Playwright | Microsoft | 多言語バインディング、フル機能 |
| agent-browser | Vercel | PlaywrightのCLIラッパー |
| **Rodney** | Simon Willison | エージェント最適化、Showboat連携 |
| shot-scraper | Simon Willison | スクリーンショット特化（Rodneyの前身） |

## バージョン履歴

- **v0.4.0** (2026年2月17日): `rodney assert`、`--local`/`--global`セッション、`reload --hard`など追加
- **v0.3.0** (2026年2月10日): 初回リリース

## 関連概念

- [[showboat]] — テスト成果物の記録ツール（Rodneyと併用）
- [[agentic-manual-testing]] — Rodneyの主要ユースケース
- [[../agentic-engineering]] — 上位概念

## 参照

- [[simon-willison]] — 開発者
- [Rodney v0.4.0 リリースノート](https://simonwillison.net/2026/Feb/17/rodney/)
- [Introducing Showboat and Rodney](https://simonwillison.net/2026/Feb/10/showboat-and-rodney/)
