# AI Agent Memory Middleware Wiki Page

Location: `wiki/concepts/ai-agent-memory-middleware.md`

## Current Structure (4-Tier Framework)

### L0: Virtual Filesystem (ChromaFS/Mintlify Pattern)
- Vector DB + Unix CLI abstraction
- P90 boot: 100ms (vs 46s traditional)
- Cost: $0/conversation
- Read-only guarantees, lazy loading

### L1: In-Context Memory
- Context window, prompt cache
- Anthropic/OpenAI KV cache optimization

### L2: Local File Memory  
- CLAUDE.md, SKILL.md
- Git-based state

### L3: Cloud Storage Memory
- S3 Files (Stage and Commit model)
- Tigris, LLMFS, Cognee
- Multi-agent shared workspaces

## Integration Notes
When analyzing new memory technologies, map them to this framework and update the wiki page accordingly.