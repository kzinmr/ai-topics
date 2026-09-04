# Transcript Tag Selection Pitfalls

When creating transcript frontmatter tags, you MUST check `wiki/SCHEMA.md` before committing. The pre-commit hook blocks any staged file with tags not in the taxonomy (695+ canonical tags).

## Common Offending Patterns

Domain-subtopic tags that are NOT in SCHEMA.md and will block commits:
- `mdp`, `multi-armed-bandit`, `policy-gradient` → use `reinforcement-learning` + `agentic-rl` instead
- `llm-fundamentals` → use `llm` or `foundation-models`
- `async-processing` → use `async-agents`
- Library/tool names (`verifiers`, `chromadb`, `litellm`) → NOT valid tags; use functional tags

## Pre-Commit Tag Validation Workflow

1. **Before writing frontmatter**: `search_files` for the topic in `wiki/SCHEMA.md` to find canonical tags
2. **If a new tag is warranted**: Add it to SCHEMA.md's taxonomy list first, then use it
3. **If blocked by tag violations in OTHER files** (not yours):
   ```bash
   cd ~/ai-topics && git reset HEAD
   git add <only-your-files>
   git -c core.quotepath=false commit -m "wiki: ..."
   ```
   This avoids being blocked by pre-existing violations in unstaged files you didn't touch.
4. **If blocked by YOUR tags**: Either replace with an existing canonical tag, or add the new tag to SCHEMA.md and commit SCHEMA.md alongside your files.

## Quick Tag Substitution Reference (RL domain)

| Topic | Invalid tag | Use instead |
|-------|-------------|-------------|
| MDPs, environments | `mdp` | `reinforcement-learning` |
| Multi-armed bandits | `multi-armed-bandit` | `reinforcement-learning` |
| Policy gradient methods | `policy-gradient` | `reinforcement-learning` + `grpo` |
| Advantage estimation | `advantage-estimation` | `reinforcement-learning` |
| Agentic RL training | `agent-training` | `agentic-rl` |
| LM-as-judge | `lm-judge` | `llm-as-judge` |

## Quick Tag Substitution Reference (Observability/Tracing domain)

| Topic | Invalid tag | Use instead |
|-------|-------------|-------------|
| LLM tracing, call tracing | `tracing` | `trace-analysis` |
| Logging, log management | `logging` | `observability` |
| Monitoring, alerting | `monitoring` | `observability` |
