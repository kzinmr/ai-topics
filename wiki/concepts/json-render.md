---
title: "json-render — Generative UI フレームワーク"
created: 2026-05-08
updated: 2026-05-08
type: concept
tags: [generative-ui, framework, ai-agents, vercel, react, vue, svelte, open-source, tool]
aliases: [json-render, vercel-json-render]
related:
  - concepts/ai-agent-engineering
  - entities/vercel
sources:
  - raw/articles/2026-05-07_vercel-labs_json-render.md
  - https://github.com/vercel-labs/json-render
---

# json-render — Generative UI フレームワーク

## 概要

**json-render** は **Vercel Labs** が開発した Generative UI フレームワーク。自然言語プロンプトから動的でパーソナライズされた UI を生成する。AI の出力を事前定義されたコンポーネントとアクションのカタログに**制約**することで、生成 UI の信頼性を確保する。

## 核心理念

> 「AI に UI を作らせるが、決められた部品だけを使わせる」

- **Guardrailed**: AI の出力を開発者が定義したコンポーネントカタログに制限
- **Predictable**: JSON 出力は常に定義されたスキーマに適合
- **Fast**: プログレッシブストリーミング + モデル応答に応じた逐次レンダリング
- **Cross-Platform**: 単一カタログで React, Vue, Svelte, Solid, React Native 他をサポート
- **Batteries Included**: 36個の shadcn/ui コンポーネントがプリビルド

## アーキテクチャ

```
自然言語 → AIモデル → JSON Spec → Renderer → UI
                ↑
         Component Catalog (Zodスキーマで制約)
```

### 3ステップワークフロー

1. **カタログ定義**: Zod スキーマで AI が使えるコンポーネントとアクションを制約
2. **コンポーネント実装**: カタログを実際の UI 実装にマッピング
3. **AI 生成 Spec のレンダリング**: `<Renderer spec={spec} registry={registry} />`

## エコシステム

| カテゴリ | パッケージ |
|----------|-----------|
| **Core** | `@json-render/core`, `@json-render/codegen`, `@json-render/yaml` |
| **Web フレームワーク** | React, Vue, Svelte, Solid |
| **UI ライブラリ** | `@json-render/shadcn`, `@json-render/shadcn-svelte` |
| **特殊用途** | Next.js (フルアプリ), React Native (モバイル), Remotion (動画), React PDF, React Email, Ink (ターミナル TUI) |
| **3D/グラフィックス** | `@json-render/react-three-fiber` (3D, Gaussian Splatting), `@json-render/image` (SVG/PNG) |
| **状態管理** | Redux, Zustand, Jotai, XState アダプター |

## 高度な機能

### 動的 Props と式

コンポーネント props に式を埋め込み可能：
- `$state`: 状態モデルから値を読み取り
- `$cond`: 三項論理（`$then` / `$else`）
- `$template`: 文字列補間（`"Hello, ${/user/name}!"`）
- `$computed`: 登録関数の呼び出し

### 条件付き表示
```json
{
  "type": "Alert",
  "visible": [
    { "$state": "/form/hasError" },
    { "$state": "/form/errorDismissed", "not": true }
  ]
}
```

### SpecStream（ストリーミング AI）
部分的な JSON チャンクを処理して UI を逐次更新：
```typescript
const compiler = createSpecStreamCompiler<MySpec>();
const { result } = compiler.push(chunk);
setSpec(result); // 部分結果で UI 更新
```

### プロンプト自動生成
```typescript
const systemPrompt = catalog.prompt();
// コンポーネント説明、prop スキーマ、利用可能アクションを含む
```

## 競合との差別化

| 比較軸 | json-render | Vercel AI SDK | 従来のGenerative UI |
|--------|-------------|---------------|-------------------|
| **制約方式** | Zod カタログ（厳格） | ツール呼び出し | フリーフォーム |
| **クロスフレームワーク** | 12+ レンダラー | React 中心 | 単一 |
| **コンポーネント数** | 36 プリビルド | 要自前実装 | — |
| **ライセンス** | Apache-2.0 | — | — |

## 関連項目

- [[concepts/ai-agent-engineering]] — AI エージェントの UI 生成文脈
- [GitHub: vercel-labs/json-render](https://github.com/vercel-labs/json-render)
