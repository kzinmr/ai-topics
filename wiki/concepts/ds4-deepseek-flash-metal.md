---
title: "ds4.c — DeepSeek V4 Flash Metal 推論エンジン"
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - local-llm
  - hardware
  - metal
  - inference
  - deepseek-v4
  - quantization
  - coding-agent
  - tool
  - open-source
aliases: [ds4, ds4-deepseek-flash-metal, deepseek-v4-flash-metal]
related:
  - concepts/deepseek-v4
  - entities/deepseek
  - entities/armin-ronacher
  - concepts/llama-cpp
sources:
  - raw/articles/2026-05-07_mitsuhiko_ds4-deepseek-flash-metal.md
  - https://github.com/mitsuhiko/ds4
---

# ds4.c — DeepSeek V4 Flash Metal 推論エンジン

## 概要

**ds4.c** は、**Armin Ronacher（@mitsuhiko）** が antirez のオリジナルワークをフォークして開発した、**Apple Silicon（Metal）上で DeepSeek V4 Flash 専用**に最適化されたネイティブ推論エンジン。汎用 GGUF ランナーではなく、V4 Flash の Metal グラフを直接実行する特殊設計。Pi 拡張とのシームレスな統合を特徴とする。

## 主要機能

| 機能 | 詳細 |
|------|------|
| **Metal 専用** | macOS に最適化。CPU パスは検証用のみ（macOS 仮想メモリのバグで不安定） |
| **Disk-First KV Cache** | KV キャッシュを「第一級ディスク市民」として扱い、セッション・再起動をまたいだ永続化 |
| **100万トークンコンテキスト** | V4 Flash の巨大コンテキストウィンドウをフルサポート |
| **非対称2ビット量子化** | MoE ルーテッドエキスパートは IQ2_XXS/Q2_K、共有エキスパート・射影は非量子化で品質維持 |
| **エージェント統合** | Claude Code, OpenCode, Pi と直接連携可能 |

## パフォーマンス

*2ビット量子化、32K コンテキスト、no-think モード、貪欲デコードで計測*

| マシン | プロンプトサイズ | Prefill 速度 | 生成速度 |
|--------|-----------------|-------------|---------|
| MBP M3 Max (128GB) | Short | 58.52 t/s | 26.68 t/s |
| MBP M3 Max (128GB) | 11,709 tokens | 250.11 t/s | 21.47 t/s |
| Mac Studio M3 Ultra | Short | 84.43 t/s | 36.86 t/s |
| Mac Studio M3 Ultra | 11,709 tokens | 468.03 t/s | 27.39 t/s |

## インストールと使用

### Pi 拡張経由（推奨）
```bash
pi install https://github.com/mitsuhiko/ds4
```

### 手動ビルド
```bash
./download_model.sh q2   # 128GB RAM マシン用
./download_model.sh q4   # 256GB+ RAM マシン用
make
```

### 対話型 CLI
```bash
./ds4
# コマンド: /think, /nothink, /ctx N, /read FILE, /quit
# Ctrl+C で生成中断
```

### ローカルサーバー
OpenAI/Anthropic 互換 API を提供：
```bash
./ds4-server --ctx 100000 --kv-disk-dir /tmp/ds4-kv --kv-disk-space-mb 8192
```
- エンドポイント: `/v1/chat/completions` (OpenAI), `/v1/messages` (Anthropic/Claude Code)
- SSE ストリーミング対応（テキスト + thinking ブロック）

## Claude Code 連携

```bash
export ANTHROPIC_BASE_URL="http://127.0.0.1:8000"
export ANTHROPIC_MODEL="deepseek-v4-flash"
exec "$HOME/.local/bin/claude" "$@"
```

## 技術的制約

- **メモリ要件**: 2ビット量子化で約 81GB。1M トークンコンテキストで+26GB。128GB マシンでは 100K-300K が推奨
- **Thinking モード**: thinking, nothink, Think Max 対応。Think Max は十分なコンテキストウィンドウが必要
- **MTP（投機的デコード）**: 実験的サポート（`--mtp` フラグ）、現状わずかな高速化のみ
- **開発**: GPT 5.5 の強力な支援を受け、llama.cpp / GGML の基盤上に構築

## Disk KV Cache システム

SHA1 ハッシュを使用したファイル名（`<sha1>.kv`）でトークンプレフィックスを永続化：
- **Save トリガー**: cold（長い初期プロンプト後）、continued（生成中の定期保存）、evict/shutdown（メモリ解放・停止時）
- **観測性**: キャッシュファイルはプレーンテキストヘッダーを含み、`hexdump` で人間が検査可能

## 関連項目

- [[concepts/deepseek-v4]] — DeepSeek-V4 モデルシリーズ
- [[entities/armin-ronacher]] — 開発者
- [[entities/deepseek]] — DeepSeek 社
