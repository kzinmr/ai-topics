# Daily RSS Scan Report — 2026-08-16

> Source: blogwatcher RSS scan
> Total articles: 19 (13 saved, 6 unsaved)

## スキャン結果サマリ

| 指標 | 値 |
|------|-----|
| スキャン記事数 | 19 |
| 保存済み記事 | 13 |
| 未保存記事 | 6 (YouTube URL + 非AI記事) |
| AI関連記事 | 4 (高関連度) |
| Wiki更新 | 3ページ更新 |

## AI関連記事（高優先度）

### 🔥 Augment Code — Auggie CLI v2 Harness Rebuild
- **ソース**: [augmentcode.com](https://augmentcode.com/blog/auggie-cli-harness-rebuild-53-percent-cheaper)
- **概要**: Piフレームワークをフォークしてコーディングエージェントハーネスを再構築。SWE-bench ProでClaude Codeと同等のパスレートを保ちつつコスト53%削減（$2.70→$1.27/タスク）。主要変更: ツール面の大幅削減（bash + ファイル3ツール）、コンテキストエンジンによる単一コール検出、低コストモデルでのプロアクティブコンパクション。
- **Wiki更新**: `entities/augment.md` にセクション追加

### 🔥 Sean Goedecke — AI Text Watermarking Is Not a Big Deal
- **ソース**: [seangoedecke.com](https://seangoedecke.com/ai-text-watermarking-is-not-a-big-deal/)
- **概要**: AIテキストウォーターマーキング（SynthID-Text/TextSeal）は品質を劣化させず、実用的には検出不可能で、EU AI Actにより2027年までに全プロバイダーに義務化されるため「大したことではない」と主張。ウォーターマーキング技術の現状と規制動向を網羅的に解説。
- **Wiki更新**: `entities/seangoedecke-com.md` + `concepts/security-and-governance/ai-text-watermarking.md` を更新

### 🔥 Simon Willison — CORS Chat
- **ソース**: [simonwillison.net](https://simonwillison.net/2026/Aug/15/cors-chat/)
- **概要**: GPT-5.6-Sol xhighで構築したOpenAI Responses API互換チャットエンドポイントのテスト用Web UI「CORS Chat」を公開。LM Studio上で動作するQwen 3.8 27Bのテストに使用。プログレッシブSVGレンダリング、JSONエクスポート機能を搭載。
- **Wiki更新**: `entities/simon-willison.md` に参照追加（既存ページ）

## その他の保存済み記事

| ブログ | タイトル | AI関連度 |
|--------|----------|----------|
| johndcook.com | Probability of correcting errors | 低 |
| johndcook.com | Compressing a Hadamard matrix | 低 |
| nesbitt.io | This Week in Package Management | 低 |
| purplesyringa.moe | std::process::Command is a bad citizen on Windows | 低 |
| construction-physics.com | Reading List — 08/15/2026 | 低 |
| eli.thegreenplace.net | Concurrent Servers: Part 7 - Rust | 低 |
| lwn.net | Python packaging council candidates announced | 低 |
| lwn.net | Security updates for Friday | 低 |
| dfarq.homeip.net | IBM PC Compact Printer model 5181 | 低 |
| shkspr.mobi | Book Review: Slags | 低 |

## 未保存記事

| ブログ | タイトル | 理由 |
|--------|----------|------|
| AI Engineer | How Web Data Infrastructure Powers the Next Generation of AI | YouTube URL |
| AI Engineer | The Rise of CaaS: Context-as-a-Service for Agentic AI | YouTube URL |
| AI Engineer | The Dark Arts of Web Automation | YouTube URL |
| AI Engineer | Bringing agents onto the world wide web | YouTube URL |
| AI Engineer | Computer Use at the Edge of the Statistical Precipice | YouTube URL |
| xeiaso.net | Site update: a few posts have been removed | 非AI記事 |

## AI Engineer YouTube Talks（未処理・要確認）

AI Engineerの5本のYouTube講演はAIエージェント・Web自動化・コンピュータユースの文脈で非常に relevance が高い。yt-dlpでのトランスクリプト取得とwiki取り込みを推奨:
1. **Patricija Žemaitytė, Oxylabs** — WebデータインフラとAI
2. **Omer Primor, Bright Data** — Context-as-a-Service for Agentic AI
3. **Corey Gallon, Rexmore** — Web自動化エージェント
4. **Paul Klein IV, Browserbase** — エージェントのWeb上での活用
5. **Pierluca D'Oro, Programma Labs** — Computer Useの統計的限界
