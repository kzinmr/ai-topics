# Directory Rename and Product Split Patterns (2026-06-11)

## Directory Renames

### ai-infrastructure-engineering/ → training-infra/
- **Reason**: Name was too broad; content focuses on GPU/training infrastructure, not general AI infra
- **Files**: 7 (_index.md, distributed-training, gpu-vram-fundamentals, hardware-lottery, llm-observability, model-serving-autoscaling, pytorch-gpu-memory-profiling)
- **Links updated**: 78
- **Regex**: `rf"\[\[(?:concepts/)?ai-infrastructure-engineering(/?[^\]|]*?)(?:\|([^\]]+))?\]\]"`

### agent-team-swarm/ → multi-agents/
- **Reason**: Name too specific (team/swarm); directory had grown to include orchestration, communication, workflow patterns
- **Files**: 11 (_index.md, agent-communication-protocols, agent-executor, agent-orchestration-frameworks, agent-orchestration, agent-swarms, agent-team-swarm, agentic-conflict-resolution, agentic-data-science, agentic-workflow-patterns, managed-devins)
- **Links updated**: 133

**Key insight**: Directory renames require a single regex that captures both the directory name and optional subpage suffix. The pattern `old-name(/?[^\]|]*?)` handles both `[[concepts/old-name]]` and `[[concepts/old-name/subpage]]`.

## Product Tool Splits

### claude-code/ split from claude/
- **claude/** retained: model family, system cards, model-specific pages (opus-*, sonnet-*, mythos, tokenizer, etc.)
- **claude-code/** created: 11 tool-specific pages (claude-code, claude-code-best-practices, claude-code-tips, claude-code-routines, claude-md-rules, claude-code-skills, claude-code-source-patterns, claude-code-auto-mode, claude-code-goal, claude-code-sandboxing, claude-code-leak)
- **Decision heuristic**: Title contains "claude-code" or "claude-md" → tool. Title contains model name (opus, sonnet, mythos) → model.

### codex/ split from openai/ + flat concepts
- **openai/** retained: platform-level pages (model-spec, symphony, workspace-agents, etc.)
- **codex/** created: 9 pages from mixed sources:
  - Flat `concepts/`: codex-agent-loop, codex-app-server, codex-goal-meta-prompting, codex-goal, codex-knowledge-work, codex-prompting (6)
  - From `openai/`: codex-superapp, codex-safety, astral-acquisition (3)
- **_index.md** organized: Core (agent-loop, app-server, prompting), Workflows (goal, goal-meta-prompting, knowledge-work), Platform (superapp, safety, astral-acquisition)

**Key insight**: Product tool splits require gathering pages from MULTIPLE source directories (flat + product subdir) into one new tool directory. The link-update regex must match both `concepts/slug` and `concepts/openai/slug` patterns.

## Stats

| Operation | Files | Links |
|---|---|---|
| ai-infrastructure-engineering → training-infra | 7 | 78 |
| agent-team-swarm → multi-agents | 11 | 133 |
| claude-code/ creation | 11 | ~90 |
| codex/ creation | 9 | ~80 |
