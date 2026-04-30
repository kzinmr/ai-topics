---
title: "Coding Agents"
type: concept
aliases:
  - coding-agents
created: 2026-04-25
updated: 2026-04-27
tags:
  - concept
  - coding-agents
  - ai-agents
status: complete
description: "LLM-powered coding agents — tools, environments, and optimization patterns for agent-driven development."
---

# Coding Agents

LLM搭載のコード書きエージェント。Claude Code、OpenAI Codex、Cursor、GitHub Copilot、OpenClawなどが該当。

## 最適化: デベロッパ環境の設計

Eric Zakariasson (2026-04-27) による実践的ガイド:

エージェントに人間と同じ仕事をしてもらいたいなら、人間に1日目で与えるものを与えよ: マシン、認証情報、Slack、Linear、Notion、Datadog、GitHub org。

> "This also means that your job shifts. You're less the person writing every line and more the person building the system that tells agents what good and bad looks like. This is mostly the same work as building good developer experience for humans."

### 重要な視点
- エージェント環境の最適化は、人間向けのDX構築とほぼ同じ作業
- 開発者の役割は「すべての行を書く人」から「エージェントにとって善と悪がどう見えるかを定義する人」へ移行

参考: [Optimizing your dev environment for coding agents](../raw/articles/2041897427431563613_optimizing-your-dev-environment-for-coding-agents.md)

## 業界動向

### SpaceX × Cursor: $60B 買収オプション (2026-04)

SpaceXは2026年後半にCursorを**$600億で買収する権利**を取得。またはCursorに**$100億**を支払って協業する選択肢も保持。

**背景:**
- Cursorの独自モデルComposer 2はMoonshotのKimiベースでコミュニティの反応は冷ややか
- SpaceXのColossusクラスター（100万H100相当）へのアクセス獲得が真の目的
- Kevin Kwok分析: 「トップコーディングラボはモデルとプロダクトの両方を所有する必要がある。流通だけを持ちモデルを持たないのは賃貸契約。全てのデブツール企業はモデル企業になるか、モデルの機能になるか」

### OpenAI Workspace Agents (2026-04)

Codex搭載の共有エージェント。Business/Enterpriseプラン向け。Slack、Salesforce、Notion、Google Driveと統合。永続メモリとロールベースガバナンス搭載。

## 関連ページ
- [[concepts/harness-engineering]] — エージェント駆動開発の環境設計哲学
- [[concepts/agentic-engineering]] — 上位概念
- [[concepts/subagents]] — 並列エージェント委譲パターン
- [[concepts/cognitive-debt]] — コンテキスト管理の重要性
- [[entities/openai]] — OpenAI (Workspace Agents, Codex)
- [[entities/anthropic]] — Anthropic (Claude Code)

## Raw Articles

### claude-code
- [2026-01-02_boris-cherny---my-claude-code-setup-(jan-2026)](2026-01-02_boris-cherny---my-claude-code-setup-(jan-2026).md)
- [2026-01-31_boris-cherny---10-tips-from-the-claude-code-team-(feb-2026)](2026-01-31_boris-cherny---10-tips-from-the-claude-code-team-(feb-2026).md)
- [2026-02-11_chernycode---boris-cherny's-claude-code-config-files](2026-02-11_chernycode---boris-cherny's-claude-code-config-files.md)
- [2026-04-26-claude-code-anthropic-agentic-coding-system](2026-04-26-claude-code-anthropic-agentic-coding-system.md)
- [2026-04-26-claude-code-openclaw-harness-practice](2026-04-26-claude-code-openclaw-harness-practice.md)
- [2026-keep-your-claude-code-context-clean-with-subagents](2026-keep-your-claude-code-context-clean-with-subagents.md)
- [2043609541477044439_Google-Engineer-Automated-80-of-Work-with-Claude-Code](2043609541477044439_Google-Engineer-Automated-80-of-Work-with-Claude-Code.md)
- [boris-cherny-im-boris-i-created-claude-code](boris-cherny-im-boris-i-created-claude-code.md)
- [crawl-2026-04-23-claude-code-design-space](crawl-2026-04-23-claude-code-design-space.md)
- [grantslatton.com--claude-code--1d686b27](grantslatton.com--claude-code--1d686b27.md)
- [how-claude-code-team-really-works](how-claude-code-team-really-works.md)
- [martinalderson.com--posts-building-a-tax-agent-with-claude-code--72e6cc36](martinalderson.com--posts-building-a-tax-agent-with-claude-code--72e6cc36.md)
- [martinalderson.com--posts-claude-code-static-analysis--2a4b4efb](martinalderson.com--posts-claude-code-static-analysis--2a4b4efb.md)
- [martinalderson.com--posts-minification-isnt-obfuscation-claude-code-proves-it--89931401](martinalderson.com--posts-minification-isnt-obfuscation-claude-code-proves-it--89931401.md)
- [martinalderson.com--posts-no-it-doesnt-cost-anthropic-5k-per-claude-code-user--77319d6f](martinalderson.com--posts-no-it-doesnt-cost-anthropic-5k-per-claude-code-user--77319d6f.md)
- [simonwillison.net--2026-apr-22-claude-code-confusion--c0c17d47](simonwillison.net--2026-apr-22-claude-code-confusion--c0c17d47.md)
- [simonwillison.net--2026-apr-24-recent-claude-code-quality-reports--7811dd0a](simonwillison.net--2026-apr-24-recent-claude-code-quality-reports--7811dd0a.md)
- [theregister.com--2026-03-31-anthropic-claude-code-source-code--ba8c2ae1](theregister.com--2026-03-31-anthropic-claude-code-source-code--ba8c2ae1.md)

### coding
- [2026-2013-ralph-minimal-file-based-autonomous-coding-agent](2026-2013-ralph-minimal-file-based-autonomous-coding-agent.md)
- [crawl-2026-04-18-nvidia-speculative-decoding](crawl-2026-04-18-nvidia-speculative-decoding.md)
- [crawl-2026-04-23-speculative-decoding-nvidia](crawl-2026-04-23-speculative-decoding-nvidia.md)
- [hyperbo.la--w-coding-agents-for-technical-non-engineers--46484b05](hyperbo.la--w-coding-agents-for-technical-non-engineers--46484b05.md)
- [hyperbo.la--w-social-coding-2018--a491bede](hyperbo.la--w-social-coding-2018--a491bede.md)
- [it-notes.dragas.net--2025-06-05-vibe-coding-will-rob-us-of-our-freedom--204416ce](it-notes.dragas.net--2025-06-05-vibe-coding-will-rob-us-of-our-freedom--204416ce.md)
- [jayd.ml--2025-06-15-encoding-xml-is-broken-and-no-one-cares-html--3522c300](jayd.ml--2025-06-15-encoding-xml-is-broken-and-no-one-cares-html--3522c300.md)
- [johndcook.com--blog-2026-04-21-an-ai-odyssey-part-4-astounding-coding-agent--85a4b5af](johndcook.com--blog-2026-04-21-an-ai-odyssey-part-4-astounding-coding-agent--85a4b5af.md)
- [kimi-k2-6-advancing-open-source-coding](kimi-k2-6-advancing-open-source-coding.md)
- [mariozechner.at--posts-2025-11-30-pi-coding-agent](mariozechner.at--posts-2025-11-30-pi-coding-agent.md)
- [martinalderson.com--posts-what-happens-when-coding-agents-stop-feeling-like-dial--d2aad4ef](martinalderson.com--posts-what-happens-when-coding-agents-stop-feeling-like-dial--d2aad4ef.md)
- [martinalderson.com--posts-why-sandboxing-coding-agents-is-harder-than-you-think--4d65588c](martinalderson.com--posts-why-sandboxing-coding-agents-is-harder-than-you-think--4d65588c.md)
- [michael.stapelberg.ch--posts-2026-02-01-coding-agent-microvm-nix--1af8da31](michael.stapelberg.ch--posts-2026-02-01-coding-agent-microvm-nix--1af8da31.md)
- [rakhim.exotext.com--programming-vs-coding-vs-software-engineering--d32b0538](rakhim.exotext.com--programming-vs-coding-vs-software-engineering--d32b0538.md)
- [syntax.fm--976-pi-coding-agent](syntax.fm--976-pi-coding-agent.md)

### minimaxir
- [minimaxir.com--2025-01-write-better-code--d88107e5](minimaxir.com--2025-01-write-better-code--d88107e5.md)
- [minimaxir.com--2025-02-embeddings-parquet--ce2ddf9c](minimaxir.com--2025-02-embeddings-parquet--ce2ddf9c.md)
- [minimaxir.com--2025-05-llm-use--8e888f29](minimaxir.com--2025-05-llm-use--8e888f29.md)
- [minimaxir.com--2025-06-movie-embeddings--220f5935](minimaxir.com--2025-06-movie-embeddings--220f5935.md)
- [minimaxir.com--2025-07-llms-identify-people--ea16c95d](minimaxir.com--2025-07-llms-identify-people--ea16c95d.md)
- [minimaxir.com--2025-08-llm-blueberry--0c1d9624](minimaxir.com--2025-08-llm-blueberry--0c1d9624.md)
- [minimaxir.com--2025-10-claude-haiku-jailbreak--f0c61834](minimaxir.com--2025-10-claude-haiku-jailbreak--f0c61834.md)
- [minimaxir.com--2025-11-nano-banana-prompts--a1691cff](minimaxir.com--2025-11-nano-banana-prompts--a1691cff.md)
- [minimaxir.com--2025-12-nano-banana-pro--322c3dbc](minimaxir.com--2025-12-nano-banana-pro--322c3dbc.md)
- [minimaxir.com--2026-02-ai-agent-coding--1e287d7a](minimaxir.com--2026-02-ai-agent-coding--1e287d7a.md)

### multi-agent
- [2043071219667480853_Ten-Design-Principles-of-Agentic-AI-Skills](2043071219667480853_Ten-Design-Principles-of-Agentic-AI-Skills.md)
- [crawl-2026-04-18-measuring-agent-autonomy](crawl-2026-04-18-measuring-agent-autonomy.md)
- [martinalderson.com--posts-why-on-device-agentic-ai-cant-keep-up--5a080ee7](martinalderson.com--posts-why-on-device-agentic-ai-cant-keep-up--5a080ee7.md)
- [prism-reranker-agentic-retrieval-2026-04-28](prism-reranker-agentic-retrieval-2026-04-28.md)
- [simonw-agentic-engineering-patterns-guide](simonw-agentic-engineering-patterns-guide.md)
- [simonwillison.net--guides-agentic-engineering-patterns-adding-a-new-content-typ--67e45614](simonwillison.net--guides-agentic-engineering-patterns-adding-a-new-content-typ--67e45614.md)
- [troyhunt-agentic-hibp-2026-04-17](troyhunt-agentic-hibp-2026-04-17.md)
