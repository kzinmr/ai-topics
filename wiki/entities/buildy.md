---
title: Buildy
created: 2026-05-11
updated: 2026-05-11
type: entity
status: L2
tags: [company, platform, tool, ai-agents, mcp, personal-ai, developer-tooling, web-development]
aliases: [buildy.so]
sources: [https://buildy.so, https://buildy.so/llms.txt, https://buildy.so/llms-full.txt]
related: [mcp, codex, claude-code, openclaw, cursor]
---

# Buildy

> Built by your AI. Used by both of you. — AI エージェントが「あなた専用」の Web アプリを構築・永続化するプラットフォーム

Buildy は、AI エージェント（Claude Code / Codex / Cursor など）が **パーソナル Web アプリ** を構築・配信するためのランタイムプラットフォーム。ES module を POST するだけで公開 URL が発行され、実データを永続保存。1つのアカウントで複数の小さなアプリを持ち、どのエージェントからでも利用できる。

**Website**: [buildy.so](https://buildy.so) | **API**: `app.buildy.so` | **Docs for AI**: [llms-full.txt](https://buildy.so/llms-full.txt)

## 核心コンセプト

> **"Built by your AI. Used by both of you."**

Buildy は「AI がコードを書くこと」と「人間がそれを使うこと」のギャップを埋める。AI エージェントが Web アプリを書き、Buildy がそれをホストし、人間はブラウザ・スマホ・チャット内のどこからでもアクセスできる。

## 3つの柱

| 柱 | 説明 |
|----|------|
| **Persistence（永続性）** | 実URL + 実ストレージ。タブを閉じても明日もそこにある |
| **Portability（可搬性）** | Codex で構築 → ChatGPT で利用 → Claude で更新。1つのMCP、全エージェント対応 |
| **A Home（集約）** | 複数の小さなアプリを1アカウントで管理。習慣トラッカー、買い物リスト、予算管理…すべてここに |

## アーキテクチャ

```
AI Agent (Claude/Codex/Cursor/...) 
  → ES Module (Workers/WinterTC fetch handler + optional inline UI)
    → POST https://app.buildy.so/app
      → Public URL + KV Storage
        ← ユーザーがブラウザ/スマホ/チャットでアクセス
```

- **ランタイム**: Workers/WinterTC 互換の `fetch` ハンドラ
- **ストレージ**: キーバリューストア（アプリ単位・シングルテナント）
- **UI**: インライン HTML/CSS（iframe レンダリング）
- **認証**: Device Code Pairing Flow (`/pair/start` → `/pair/poll`) または PAT (Personal Access Token)

## 対応エージェント・クライアント

### コードエディタ系 (API経由)
Cursor, Claude Code, Codex CLI, Cline, Windsurf, Continue, Zed, Gemini CLI

### チャット系 (MCP経由)
Claude Desktop, Claude.ai (Pro), ChatGPT (Plus + Developer Mode), Goose, Perplexity

### 近日対応
Grok, Gemini (チャット)

## 主な機能

| 機能 | 状態 | 説明 |
|------|------|------|
| **Live URLs** | ✅ Live | 各アプリに実URL。ブラウザ・スマホ・共有可 |
| **Persistent Storage** | ✅ Live | データ永続化。チャット閉じても明日も残る |
| **Multi-Agent** | ✅ Live | 1 MCPインストールで Claude/ChatGPT/Codex/Cursor 全対応 |
| **Build Anywhere, Use Anywhere** | ✅ Live | 構築したエージェントと別のエージェントで利用可能 |
| **Hooks / API** | ✅ Live | POST /api/log, call_app sync, cron digest |
| **Share by Link** | ✅ Live | URL共有 → 相手がAIで開く、同じデータ |
| **Custom Domains** | 🔜 Planned | 独自ドメイン |
| **Notifications** | 🔜 Planned | Push/Email/SMS |
| **Schedules** | 🔜 Planned | 定期実行（cron） |
| **Shared Memory** | 🔜 Planned | アプリ間でコンテキスト共有 |
| **Versions** | 🔜 Planned | エージェントの編集をアンドゥ、任意の地点にロールバック |
| **Activity Log** | 🔜 Planned | 全読み書き・実行の監査ログ |
| **Mobile Apps** | 🔜 Planned | iOS/Androidネイティブアプリ |
| **Integrations** | 🔜 Planned | Gmail, Google Calendar, Sheets, Drive, Notion, Linear, GitHub 他24種 |

## 料金

最初の1アプリは **無料・サインアップ不要**。アカウント登録は「残したい」と思った時だけでよい。

## 競合・関連

- [[replit]] — AI Agent によるフルスタックアプリ開発。より本格的な開発向け
- [[lindy]] — AI App Builder。Founder向けフルスタック
- [[vercel-v0]] — AI UI 生成。コンポーネント単位
- [[mcp]] — Buildy がエージェント接続に使うプロトコル
- [[claude-code]], [[codex]], [[cursor]] — Buildy が主戦場とするコーディングエージェント

## 所感

Buildy が面白いのは **「AI が作ったものを永続化する」** というレイヤーに特化している点。Vercel v0 や Replit Agent が「開発」に寄っているのに対し、Buildy は「使う」ことに重心を置く。`llms.txt` / `llms-full.txt` で AI 向けドキュメントを整備しているのも、AI-first な設計思想の表れ。

ユースケースは習慣トラッカー、買い物リスト、予算管理、ワークアウト記録など「小さな個人ツール」。エンタープライズではなく Personal AI の文脈で注目すべきプロダクト。
