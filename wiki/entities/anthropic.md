---
title: Anthropic
type: entity
created: 2026-04-09
updated: 2026-04-24
tags:
- company
- ai-safety
- llm
- active
aliases:
- Anthropic PBC
sources: []
---

# Anthropic

AI safety research company, developer of the Claude model family.

## Key Facts

- Founded by former OpenAI researchers focused on AI alignment and safety
- Known for cautious model release practices — will withhold models deemed too risky
- Headquarters: San Francisco, CA

## Model Lineup (as of Apr 2026)

| Model | Status | Notes |
|-------|--------|-------|
| [[claude-mythos]] | **Withheld** | Too risky for public release; limited access via [[concepts/project-glasswing]] |
|  | Released (GA, Apr 16) | Latest flagship — improved coding, cyber safeguards, better vision |
|  | Released | Previous generation |
|  | Released | Mid-tier |

## Claude Opus 4.7 (Apr 2026)

Released GA Apr 16, 2026. Notable improvements in advanced software engineering:
- 13% lift on 93-task coding benchmark (Replit eval), 4 tasks neither Opus 4.6 nor Sonnet 4.6 could solve
- Catches own logical faults during planning phase
- Substantially better vision (higher resolution image understanding)
- First Claude model with cyber safeguards (auto-detects and blocks prohibited cybersecurity use)
- Low-effort Opus 4.7 ≈ medium-effort Opus 4.6
- Pricing: $5/M input, $25/M output tokens (same as Opus 4.6)
- Available on all Claude products, API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry
- Cyber Verification Program for legitimate security research

## Claude Design by Anthropic Labs (Apr 17, 2026)

New product powered by Claude Opus 4.7 vision model. Allows collaborative design creation:
- Describe what you need, Claude builds first version
- Refine through conversation, inline comments, direct edits, custom sliders
- Can apply team's design system automatically
- Export to Canva, PDF, PPTX, or standalone HTML
- Handoff to Claude Code for implementation
- Research preview for Pro, Max, Team, Enterprise subscribers
- Integration with Canva (Melanie Perkins co-founder endorsement)

## AI Safety Initiatives

### Project Glasswing (2026-04)
Anthropic committed $100M in model usage credits + $4M in donations to open-source security organizations. See [[concepts/project-glasswing]] for details.

### Model Withholding Decision
Anthropic chose not to release [[claude-mythos]] publicly after discovering its vulnerability exploitation capabilities far exceeded safety thresholds. On Firefox exploit generation:
- Opus 4.6: 2 working exploits out of hundreds of attempts
- Mythos: **181 working exploits**

Mythos also discovered decades-old bugs in critical software: OpenBSD (27-year-old bug), FFmpeg (16-year-old bug).

### Capybara (Mythos Alternate Name)
Fortuneの調査によると、Mythosは内部で「Capybara」というコードネームでも呼ばれていた。CapybaraはOpusより大きく高インテリジェンスな新ティアのモデルとして位置付けられていた。データリーク後、Anthropicはコンテンツ管理システムの設定ミスを認め、公開データストアからドキュメントを削除した。

### Corporate Strategy & CEO Summit
AnthropicはMythosの早期アクセス顧客向けに、ヨーロッパで招待制CEOサミットを企画。大企業顧客へのモデル販売を推進する戦略の一環。

### Property-Based Testing Results (NeurIPS 2025)
Anthropic Red TeamはPythonパッケージ（NumPy, Pandas等）に対してプロパティベーステストを実施し、複数のゼロデイバグを発見。NeurIPS 2025で発表。AIセキュリティ研究における重要な成果。

### Financials
- **$30B ARR** (2026年4月時点) — Anthropicは年率300億ドルの収益を達成
- Claude Codeのアクティブユーザー数は300%以上成長
- Run-rate revenue expansion: 5.5x

## Product Team

### Cat Wu — Head of Product
Cat Wu (entity: [[cat-wu]]) leads product development at Anthropic, responsible for Claude Code and Anthropic's product strategy. Featured in Lenny's Newsletter (April 23, 2026) discussing:
- Anthropic's exceptional product development velocity
- Developer-first design philosophy for Claude Code
- Fast iteration cycles and minimal bureaucracy
- Bias toward shipping over perfection

### Claude Code
Claude Code is Anthropic's AI coding agent, designed under Cat Wu's product leadership. It is a key competitive product against OpenAI's Codex. See [[claude-code]] for details.

See also: [[concepts/openai-codex-superapp]] (OpenAI's competing Codex superapp positioning).

## Sources
-  (Ben's Bites, 2026-04-09)


## Claude Opus 4.7 + Big Swing Strategy (April 2026)

### Opus 4.7 Highlights
- Released April 16, 2026 (GA) — significant upgrade over Opus 4.6
- **Software engineering**: Handles complex, long-running tasks with rigor; devises methods to verify outputs
- **Vision**: Up to 2,576px long edge (~3.75 MP) — 3× prior models. Excels at chemical structures, technical diagrams
- **Instruction following**: Interprets prompts literally; legacy prompts may produce unexpected results
- **New `xhigh` effort level**: Between `high` and `max` for finer reasoning/latency tradeoffs; Claude Code default raised to `xhigh`
- **API Task Budgets**: Public beta — guide token spend across longer runs
- **Tokenizer change**: Updated tokenizer may increase input tokens by 1.0–1.35×
- **Pricing unchanged**: $5/M input, $25/M output tokens
- **Cyber safeguards**: Intentionally limited vs Claude Mythos Preview; Cyber Verification Program available

### Big Swing Strategy

The April 2026 release of Claude Opus 4.7, Claude Design, and Claude Code Routines was coordinated as a single "Big Swing" — Anthropic releasing multiple major products simultaneously rather than sequentially. This strategy signals:

1. **Confidence in production readiness**: All products launched together, suggesting coordinated QA and infrastructure readiness
2. **Platform lock-in**: Claude Design → Claude Code handoff creates a design-to-code ecosystem
3. **Automation narrative**: Claude Code Routines (scheduled, API, webhook-triggered) positions Claude Code as enterprise automation infrastructure, not just a developer tool
4. **Competitive positioning**: Simultaneous release with OpenAI's ChatGPT Images 2.0 and Google's Gemini ecosystem expansion suggests Anthropic is competing on breadth of AI product ecosystem, not just model quality

This mirrors how platforms like Google and OpenAI expand beyond their core products — but Anthropic is doing it as a coordinated launch rather than incremental releases.

## Related
- [[claude-mythos]]
- [[concepts/project-glasswing]]
- 
- [[openai]]
- [[meta]]
