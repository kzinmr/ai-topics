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

### Engineering Paradigms  
- Agentic, Harness, Vibe Coding, Orchestration
- Connect to Karpathy, Willison, Lopopolo, Rufus

### Security/Events
- Leaks, controversies, policy changes
- Connect to existing safety concepts

### Tool Ecosystem
- New frameworks, libraries, platforms
- Connect to existing entity pages

## Integration Points
- After grouping: use `llm-wiki` skill to create/update pages
- After processing: update `wiki/index.md` and `wiki/log.md`
- Commit: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: [action]" && git push`