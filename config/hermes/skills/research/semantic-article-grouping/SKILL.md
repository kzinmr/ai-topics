---
name: semantic-article-grouping
description: Group raw articles or newsletter-ingest checkpoints by semantic topics, assess wiki value against existing coverage, and recommend actions
---

# Semantic Article Grouping

Analyze raw articles (from `~/wiki/raw/articles/`) or newsletter-ingest checkpoints (from cron pipeline) and group by semantic topics for wiki curation. This is the **triage/coverage-gap-analysis** stage that sits between content ingestion and wiki-page editing (which is handled by `newsletter-wiki-ingest`).

## Input Sources

### A) Raw Article Files (from `~/wiki/raw/articles/`)
Substantive extracted article files (1KB+). Use Python discovery:
```python
import os
raw_dir = os.path.expanduser("~/wiki/raw/articles")
files = [(f, os.path.getsize(os.path.join(raw_dir, f))) 
         for f in os.listdir(raw_dir) if f.endswith('.md') and os.path.getsize(os.path.join(raw_dir, f)) > 1000]
files.sort(key=lambda x: -x[1])  # Largest first
```

### B) Newsletter-Ingest Checkpoint (from cron pipeline)
A `candidates` array injected from `${HERMES_HOME}/cron/data/newsletter/latest.json` or via `context_from` cron chaining. Each candidate has:
```json
{
  "item_id": "...",
  "source": "newsletter",
  "title": "Link N",
  "url": "https://substack.com/...",
  "raw_path": "~/wiki/raw/newsletters/...",
  "source_name": "Newsletter Title"
}
```

**CRITICAL: Substack Noise Filtering** — When processing newsletter checkpoints, most candidates are substack UI elements (play buttons, share links, comment links, like buttons, progress bars, author profile links). Filter these out by URL pattern:

| Pattern | Type | Action |
|---------|------|--------|
| `play_audio=true`, `play_card` | Podcast/audio UI | Skip |
| `action=post-comment`, `comments=true` | Comment section | Skip |
| `submitLike=true`, `reaction` | Like/heart button | Skip |
| `share=true`, `action=share` | Share link | Skip |
| `play_card_progress_bar`, `play_card_duration`, `play_card_play_button` | Player chrome | Skip |
| `redirect/app-store` | App download page | Skip |
| `@username` (e.g., `@lenny`) | Author profile | Skip |
| `redirect/2/eyJ...` or `redirect/<uuid>` | Obfuscated redirect | Try web_extract or skip |
| `utm_campaign=email-read-in-app` | Read-in-app prompt | Skip |

Keep only **actual content URLs** — usually 0-2 per newsletter that link to real articles.

## Workflow

### 1. Discover & Read Content
- For raw article files: use the Python discovery above
- For newsletter checkpoints: filter substack noise, then read the raw newsletter file to extract the actual article links

Read each substantive newsletter/raw file to extract title, key phrases, and named entities.

### 2. Extract Content Metadata
For each substantive article:
- Read title, URL, key phrases
- Identify mentioned entities (people, companies, models, concepts)
- Search the web for context if URL is obfuscated/unclear
- Match against existing wiki topics

### 3. Coverage Gap Analysis
Before deciding what to create/update, cross-reference against existing wiki pages:

```bash
search_files "topic-keyword" path=~/wiki/concepts target=files
search_files "topic-keyword" path=~/wiki/entities target=files
```

Read existing pages to determine if content is already covered. Key question: "Does the existing wiki already capture this information?" Don't create duplicates.

### 4. Semantic Grouping Criteria
Group articles by:
- **Shared entities** (same person/company/model)
- **Related concepts** (agentic engineering ↔ harness engineering)
- **Event clusters** (model releases, leaks, announcements)
- **Source themes** (The Signal newsletter, Lenny's Podcast)

### 5. Value Assessment Matrix
Rate each group for wiki inclusion:
- ★★★★★ = New concept page needed
- ★★★★☆ = Existing page update needed
- ★★★☆☆ = Covered by entity page (minor update optional)
- ★★☆☆☆ = Minor mention only (no action)
- ★☆☆☆☆ = Not wiki-worthy (skip entirely)

### 6. Output Formats

#### Cron Job (JSON schema)
When running as a cron job that feeds into `newsletter-wiki-ingest`, output JSON:

```json
{
  "checkpoint_run_id": "20260427T071008Z",
  "summary_ja": "2-4 sentence Japanese summary",
  "decisions": [
    {
      "item_id": "...",
      "source": "newsletter",
      "source_name": "Newsletter Title",
      "title": "Original link title",
      "url": "https://...",
      "raw_path": "~/wiki/raw/newsletters/...",
      "recommended_action": "take|reference|skip",
      "reason_ja": "★★★★★ 日本語での理由",
      "candidate_wiki_path": "concepts/... or entities/... or null"
    }
  ]
}
```

Rules for cron output:
- Limit `decisions` to at most 20 entries, with `take` items first
- No markdown outside the JSON
- If nothing is wiki-worthy, respond with exactly `[SILENT]`
- No asking questions — make reasonable autonomous decisions
- Prefer LLMs, AI agents, coding agents, developer tooling, inference/training infrastructure, prompt engineering, AI safety, and open-source AI

#### Interactive Session (markdown table)
When working interactively with a user:

```
### 📊 Group N: [Topic Name]
**代表トピック:** `[canonical-name]`

| 記事 | 内容 |
|------|------|
| [title] ([size]) | [1-sentence summary] |

**Wiki追加価値:** [rating] - [action recommendation]
```

### 7. Recommended Actions
- **Take**: Create new concept/entity pages for ★★★★★, or update existing pages for ★★★★☆
- **Reference**: ★★★☆☆ content can be mentioned but doesn't need page changes
- **Skip**: Low-value content (non-AI business/news, substack UI noise)

## Key Patterns to Recognize

### Non-AI Content to Skip
- **Business strategy podcasts** (e.g., Lenny's Podcast with Evan Spiegel on distribution moats) — unless they discuss AI specifically
- **General tech news** without AI/agent relevance
- **Company financial results** without AI product implications

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
- **Upstream**: Newsletter-ingest pipeline (provides candidates) or article discovery
- **Downstream**: `newsletter-wiki-ingest` skill (consumes the JSON triage output to edit wiki pages)
- After grouping: use `wiki-entity-enrichment-from-article` or `newsletter-wiki-ingest` to create/update pages
- After processing: update `wiki/index.md` and `wiki/log.md`
- Commit: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: [action]" && git push`

## Cron Job Context
When running as a scheduled cron job:
- **No asking questions** — make reasonable autonomous decisions independently
- **Japanese output** — write the summary in Japanese (日本語)
- **Silent on no-op**: If nothing is wiki-worthy, respond exactly `[SILENT]`
- **Auto-delivery**: Final response is auto-delivered; don't use send_message or try to deliver manually
- **Do NOT edit wiki files** — this job is triage only; downstream `newsletter-wiki-ingest` handles editing
