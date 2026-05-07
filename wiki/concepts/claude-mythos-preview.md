---
title: "Claude Mythos Preview"
type: concept
created: 2026-04-13
updated: 2026-05-08
tags:
  - concept
  - anthropic
  - model
  - security
  - red-team
  - dual-use
  - agentic-harness
  - firefox
aliases: ["mythos preview", "anthropic frontier red team 2026"]
related:
  - concepts/anthropic-openclaw-conflict
  - entities/dario-amodei
  - concepts/ai-agent-engineering
  - entities/mozilla
sources:
  - raw/articles/2026-05-07_mozilla_behind-the-scenes-hardening-firefox.md
---

# Claude Mythos Preview

## Overview

**Claude Mythos** is Anthropic's next-generation frontier model series. The first preview was announced on **April 7, 2026**, accompanied by a detailed Frontier Red Team research summary covering cybersecurity, biorisk, nuclear safeguards, and autonomous systems capabilities.

## Key Capabilities (Red Team Findings)

### Cybersecurity

- **Multistage Network Attacks**: Current Claude models can now succeed at multistage attacks on networks with dozens of hosts using only standard, open-source tools — no custom tooling required (a significant shift from previous generations)
- **Smart Contract Vulnerabilities**: Claude Opus 4.5, Claude Sonnet 4.5, and GPT-5 identified exploits worth a combined **$4.6M** on contracts exploited *after* their knowledge cutoffs
- **Cyber Competition Performance**: Claude consistently places in the **top 25%** of human-focused cyber competitions but still trails elite human teams on the most complex challenges
- **Property-Based Bug Hunting**: Custom agent infers general code properties and runs property-based testing; currently reporting bugs in top Python packages (several already patched post-manual validation)

### Model Progression

| Model | Cyber Capability | Notes |
|-------|----------------|-------|
| Claude Sonnet 4.5 | **≥ Opus 4.1** | Matches or eclipses prior generation's top model |
| Claude Opus 4 | Major improvement | Notable gains over prior generations |
| Claude Opus 4.5 | Frontier | Smart contract exploit discovery at $4.6M+ value |

### Autonomous Systems

- **Project Vend** (Phases 1 & 2): Tested Claude autonomously managing an office retail store for ~1 month. Phase 1 underperformed; Phase 2 introduced operational adjustments. Highlights trajectory toward AI-managed real-world commerce, but underscores current robustness gaps.
- **Project Fetch**: Explored AI-to-robotics integration — Claude assisting human operators executing complex physical tasks using a robot dog.

### Dual-Use Risk Management

- **Nuclear Safeguards**: Co-developed classifier with **NNSA & DOE labs** that distinguishes concerning vs. benign nuclear conversations with high preliminary accuracy
- **Biorisk**: AI accelerates biological/medical research but is inherently dual-use. Anthropic positions biorisk evaluation and mitigation as non-negotiable components of responsible AI development

## The "Lockdown" Decision

Anthropic **did not release Claude Mythos publicly**. The preview is restricted to frontier red team research and select partners. This decision was characterized by The Signal Newsletter as a "lockdown" — reflecting Anthropic's cautious approach to releasing capabilities that outpace existing safety frameworks.

> *"The idea of an AI running a business doesn't seem as far-fetched as it once did. But the gap between 'capable' and 'completely robust' remains wide."*
> — Anthropic Frontier Red Team

### Mythos Breach (April 2026)

Despite the lockdown, Anthropic's internal "too dangerous to release" model **Mythos** was accessed on day one by four individuals in a private Discord. The group:
- Guessed the endpoint URL from naming conventions + a Mercor breach leak
- Used a contractor's legitimate evaluation credentials
- Used the model to build simple websites (not malicious purposes, but the access was unauthorized)

The incident highlights risks of: inference endpoint discoverability, credential sharing among contractors, and naming convention predictability.

## Implications

1. **Capability acceleration**: Sonnet 4.5 matching Opus 4.1 in cyber skills demonstrates rapid model improvement within a single tier
2. **Infrastructure shift**: Standard open-source tools now sufficient for multistage network attacks — no custom infrastructure needed
3. **Release caution**: The lockdown approach suggests Anthropic sees Mythos capabilities as exceeding what can be safely deployed publicly
4. **Physical world integration**: Project Vend and Project Fetch signal Anthropic's interest in AI agents operating in real-world environments, not just digital tasks

## Mozilla Firefox Hardening — 実運用での成果 (May 2026)

Mozilla は **Claude Mythos Preview** と他の AI モデルを活用し、Firefox の大規模セキュリティ監査を実施。2026年4月だけで **423件** のセキュリティバグを修正 — これは2025年全体の合計を上回る規模。

### バグ内訳

| 発見元 | 件数 |
|--------|------|
| **Claude Mythos Preview** | 271 |
| 外部報告 | 41 |
| その他内部 (Fuzzing/手動) | 111 |
| **合計** | **423** |

### 深刻度分布 (Mythos Preview 発見分)
- **sec-high**: 180件
- **sec-moderate**: 80件
- **sec-low**: 11件

### 特徴的な発見

- **Sandbox Escape（サンドボックス突破）**: 従来のファジングでは検出が極めて困難なバグを多数発見。モデルは Firefox ソースコードをパッチしてサンドボックス内限定実行が許可されている
- **15年前のバグ** (Bug 2024437): `<legend>` 要素の再帰スタック深度とサイクルコレクションの問題
- **20年前の XSLT バグ** (Bug 2025977): 再入可能呼び出しがポインタ使用中にハッシュテーブル再ハッシュを引き起こす
- **JIT 最適化エラー** (Bug 2024918): WebAssembly GC struct で fake-object プリミティブ生成
- **RLBox エスケープ** (Bug 2029813): プロセス内サンドボックスの検証ロジックのギャップを突破

### パイプラインアーキテクチャ

Mozilla は以下の要素からなるプロジェクト固有パイプラインを構築：

1. **Discovery Subsystem**: 既存ファジング基盤上に構築されたエージェントハーネス
2. **並列化**: 複数のエフェメラル VM でジョブを実行、各ジョブが特定ファイルを対象
3. **統合**: Bugzilla で自動重複排除・追跡、エンジニアによるトリアージ
4. **モデル非依存**: Claude Opus 4.6 → Mythos Preview への移行が容易

### 教訓

Mozilla はすべてのソフトウェアプロジェクトに対し、**今すぐ AI ハーネスの使用を開始する**ことを推奨：
> *"There is a bug in this part of the code, please find it and build a testcase."* という単純なプロンプトから始め、発見と検証の「内部ループ」の周りにオーケストレーションとツールを段階的に構築する。

今後の計画として、**ファイルベースのスキャンからパッチベースの CI スキャン**への移行を予定。

## Related

- [[concepts/anthropic-openclaw-conflict]] — Anthropic's concurrent restrictions on third-party tool access
- [[dario-amodei]] — Anthropic CEO, announced Mythos Preview
-  — Dual-use risk management framework-  — Project Vend, Project Fetch
## Sources

- https://red.anthropic.com/claude-mythos-preview (Apr 7, 2026) — Full Frontier Red Team Research Summary
- https://thesignal.substack.com/p/anthropics-mythos-lockdown-metas (Apr 2026) — Newsletter analysis
- https://www.anthropic.com/news/project-glasswing — Project Glasswing (security vulnerability discovery)
