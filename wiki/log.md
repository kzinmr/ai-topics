## 2026-04-13 — Boris Cherny Entity Enrichment (Claude Code Workflow)

### Updated Files
- **wiki/entities/boris-cherny.md** — Major enrichment from 3 source articles: added Opus 4.5 + thinking rationale, Plan Mode → auto-accept workflow, CLAUDE.md as team infrastructure, PostToolUse hooks, self-verification patterns, subagents usage, MCP integration (BigQuery/Slack/Sentry), terminal optimizations, ChernyCode repo reference
- **wiki/index.md** — Updated Boris Cherny entry with key workflow patterns
- **wiki/log.md** — This entry
- **wiki/raw/articles/** — 3 source articles saved (Boris's original thread, Claude Code Camp team tips, ChernyCode repo docs)

### Key Additions
- **Opus 4.5 + thinking**: "Slower than Sonnet but smarter, requires less steering, ends up faster"
- **Plan Mode → Auto-Accept**: Shift+Tab twice → review plan → auto-accept → one-shot execution
- **CLAUDE.md as Team Memory**: Single shared file, whole team contributes, @claude on PRs to update guidelines
- **Self-Verification**: "The most underrated step. Give Claude a way to verify its work." Chrome extension, test suites
- **MCP Integration**: BigQuery, Slack, Sentry — Claude as full-stack dev hub
- **ChernyCode**: Reference implementation repo with actual config files

### Sources
- https://readwise.io/reader/shared/01kgcamtex6zews0fvz94a8qg4/ (Boris's original thread, Jan 2026)
- https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works (Feb 2026)
- https://github.com/meleantonio/ChernyCode (curated config files)
- https://paddo.dev/blog/how-boris-uses-claude-code/ (detailed analysis)

## 2026-04-13 — AI Organization Concept Hierarchy

### New Concept Pages (4件)
- **ai-organization/_index.md** — AI時代の組織論フロントページ。階層からインテリジェンスへ、Solo Founder、Context as Moatの横断的テーマを整理
- **ai-organization/ai-org-from-hierarchy-to-intelligence.md** — Block (Jack Dorsey) のAgentic Design Principles。Hierarchy to Intelligenceモデル、Decision Rights Matrix、Open-Book Telemetry、透明性ベースの監視
- **ai-organization/ai-org-solo-founder-and-super-ic.md** — Solo FounderとSuper ICの台頭。Reddit/ClaudeCodeとFourWeekMBA。1人=従来10人の生産性、管理階層のバイパス、$10M→$100Mパス
- **ai-organization/ai-org-context-as-moat.md** — McKinsey Agentic Organization。Proprietary Context Layer（最後のモート）、M-shaped Supervisor

### Updated Files
- **wiki/index.md** — AI Organizationセクション追加（3+1件）、last updated更新
- **wiki/log.md** — This entry

### Key Insights
- **Hierarchy → Intelligence**: Jack DorseyがBlockで実践。報告ライン削除、意思決定権限分散、透明性最大化
- **Context as Moat**: 企業固有の判断基準・文化・市場知見を構造化しエージェントに供給。これが最後の防衛可能資産
- **Super IC**: AIによる管理層のバイパス。技術的実行力を最大化する新しいキャリアパス
- **Agentic Governance**: エージェント実行に対するリアルタイム監視、ガードレール、エスカレーション

### Sources
- https://block.xyz/inside/from-hierarchy-to-intelligence
- https://www.reddit.com/r/ClaudeCode/comments/1ri5pnc/hot_take_solo_founders_with_ai_are_about_to_build/
- https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era
- https://organizationalphysics.com/2026/02/15/your-ai-strategy-isnt-failing-your-org-design-is/
- https://fourweekmba.com/solopreneurs/
