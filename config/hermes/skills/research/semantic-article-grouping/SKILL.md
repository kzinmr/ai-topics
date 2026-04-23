---
name: semantic-article-grouping
description: Group raw articles by semantic topics, assess wiki value, and recommend actions
---

# Semantic Article Grouping

Analyze raw newsletter articles and group them by semantic topics for wiki curation.

## Workflow

### 1. Discover Substantive Articles
```python
import os
raw_dir = os.path.expanduser("~/wiki/raw/articles")
files = [(f, os.path.getsize(os.path.join(raw_dir, f))) 
         for f in os.listdir(raw_dir) if f.endswith('.md') and os.path.getsize(os.path.join(raw_dir, f)) > 1000]
files.sort(key=lambda x: -x[1])  # Largest first
```

### 2. Extract Content Metadata
For each article:
- Read title, URL, key phrases
- Identify mentioned entities (people, companies, models, concepts)
- Match against existing wiki topics

### 3. Semantic Grouping Criteria
Group articles by:
- **Shared entities** (same person/company/model)
- **Related concepts** (agentic engineering ↔ harness engineering)
- **Event clusters** (model releases, leaks, announcements)
- **Source themes** (Simon Willison newsletter, Latent Space podcast)

### 4. Value Assessment Matrix
Rate each group for wiki inclusion:
- ★★★★★ = New concept page needed
- ★★★★☆ = Existing page update needed  
- ★★★☆☆ = Covered by entity page
- ★★☆☆☆ = Minor mention only
- ★☆☆☆☆ = Not wiki-worthy

### 5. Output Format
```
### 📊 Group N: [Topic Name]
**代表トピック:** `[canonical-name]`

| 記事 | 内容 |
|------|------|
| [title] ([size]) | [1-sentence summary] |

**Wiki追加価値:** [rating] - [action recommendation]
```

### 6. Recommended Actions
- **Create**: New concept/entity pages for ★★★★★ groups
- **Update**: Existing pages for ★★★★☆ groups
- **Archive**: Move processed articles to `processed/` directory
- **Skip**: Low-value articles remain in raw

## Key Patterns to Recognize

### Model Releases
- Company + model name + "launches", "releases", "announces"
- Group by company: OpenAI, Anthropic, Meta, Mistral, Google

### Engineering Paradigms — TAXONOMY RULES (CRITICAL)

**Agentic Engineering** (`concepts/agentic-engineering/`) = 開発者のワークフロー
- Keywords: "how to use agents", "developer patterns", "TDD with agents", "cognitive debt"
- Sources: Simon Willison guides, practitioner blogs, developer workflow tips
- Focus: "人間がエージェントをどう活用するか"
- Examples: Red/Green TDD, First Run the Tests, Showboat, Cognitive Debt, Context Window Management

**AI Agent Engineering** (`concepts/ai-agent-engineering/`) = システムアーキテクチャ
- Keywords: "orchestration", "execution loop", "harness", "sandbox", "tool design", "computer environment"
- Sources: OpenAI Engineering blog, Anthropic Engineering blog, platform architecture docs
- Focus: "エージェント実行基盤をどう構築するか"
- Examples: Agent Loop Orchestration, Context Compaction, Container Context, Agent Skills, Security Patterns

**Harness Engineering** (`concepts/harness-engineering/`) = 制御・構造化（共通概念）
- Bridges both: how execution environments are designed to constrain and guide agents
- Sources: Ryan Lopopolo/Symphony, OpenAI Codex architecture
- Keywords: "generator-evaluator loop", "critique shadowing", "evaluation-first"

**Agent Team / Swarm** (`concepts/agent-team-swarm/`) = 複数Agent協調・オーケストレーション
- Keywords: "multi-agent", "agent team", "swarm", "orchestration platform", "managed agents", "autonomous runs", "work management", "dark factory", "software factory"
- Sources: OpenAI Symphony, Anthropic Managed Agents, StrongDM Attractor, Dan Shapiro's 5-level model
- Focus: "複数Agentをどう協調させ、作業を自律管理するか"
- Examples: OpenAI Symphony (WORKFLOW.md駆動), Anthropic Managed Agents (Brain/Hands/Session分離), StrongDM Dark Factory (完全自律開発)
- **5-Level Model**: L1 Spicy Autocomplete → L2 Chat-Assisted → L3 Agent-Assisted → L4 Engineering Team → L5 Dark Factory
- **Key distinction**: L4 manages agents (Symphony/Managed Agents), L5 eliminates human review entirely (Dark Factory)

### Security/Events
- Leaks, controversies, policy changes
- Connect to existing safety concepts

### Tool Ecosystem
- New frameworks, libraries, platforms
- Connect to existing entity pages

## OpenAI vs Anthropic Platform Comparison

When analyzing platform articles, note the architectural approach:

| Dimension | OpenAI | Anthropic |
|-----------|--------|-----------|
| 実行環境 | マネージドコンテナ提供 | 開発者自前のharness設計 |
| スキル | SKILL.mdバンドル（公式API） | ツール定義（JSON schema） |
| コンテキスト | ネイティブcompaction | 開発者実装 |
| セキュリティ | サイドカーエグレスプロキシ | 開発者責任 |

## Integration Points
- After grouping: use `llm-wiki` skill to create/update pages
- After processing: update `wiki/index.md` and `wiki/log.md`
- Commit: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: [action]" && git push`
