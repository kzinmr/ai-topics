# AI Agent Memory Middleware — 4-Tier Framework

## 4-Tier Memory Architecture
| Tier | Concept | Example |
|------|---------|---------|
| L0 | Virtual Filesystem | Mintlify ChromaFS (vector DB as FUSE interface) |
| L1 | In-Context Memory | Prompt caching (Anthropic, OpenAI), KV cache |
| L2 | Local File Memory | CLAUDE.md, SKILL.md, git-based version control |
| L3 | Cloud Storage Memory | S3 Files, Tigris, LLMFS, Cognee |

## Design Principles (L0)
- "Agents don't need a real filesystem — they need the illusion of one"
- Performance target: P90 boot < 100ms, cost $0/conversation
- Read-only guarantees, lazy loading, RBAC via DB filtering

## Workflow
1. Identify new memory technology announcement
2. Scrape article to raw/articles/
3. Survey existing related wiki pages
4. Analyze against 4-tier framework
5. Create/update `wiki/concepts/ai-agent-memory-middleware.md`
6. Update index.md and log.md
7. Commit

## Key Sources
- Werner Vogels / Andy Warfield: S3 Files announcement
- Mintlify blog: ChromaFS virtual filesystem
- Tigris, LLMFS, Cognee documentation
