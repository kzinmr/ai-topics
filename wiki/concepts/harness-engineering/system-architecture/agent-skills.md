---
title: "Agent Skills (SKILL.md)"
type: concept
aliases:
  - agent-skill
  - skill-bundle
  - skilling
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - architecture
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
  - "https://openai.com/index/harness-engineering-leveraging-codex/"
  - "https://github.com/openai/skills"
related:
  - " — AI Skills (general concept)"
  - "[[concepts/harness-engineering]] — Harness Engineering"
  - "[[concepts/harness-engineering/system-architecture/container-context]] — Container Context"
---

# Agent Skills (SKILL.md bundles)

A mechanism for agents to package reusable workflow patterns as **SKILL.md bundles**. Reduces the cost of rediscovering and replanning the same multi-step patterns on every run.

## Problem Statement

> "Shell commands are powerful, but many tasks repeat the same multi-step patterns. Agents have to rediscover the workflow each run — replanning, reissuing commands, and relearning conventions — leading to inconsistent results and wasted execution."

## SKILL.md Structure

```
skill-folder/
├── SKILL.md          # Metadata + procedure description
├── api-specs/        # API specifications
├── ui-assets/        # UI screenshots, CSS references
└── scripts/          # Execution scripts (Python, bash, etc.)
```

SKILL.md includes:
- **Metadata**: Skill name, description, version, compatible models
- **Procedure**: Step-by-step instructions for the agent to follow
- **Trigger conditions**: Which prompts/situations should trigger this skill

## Skill Loading Sequence (Deterministic)

Skill application in the OpenAI Responses API operates via a **3-stage deterministic process:**

1. **Fetch skill metadata**: Name, description, version
2. **Fetch skill bundle**: Copy to container, unpack
3. **Update context**: Add skill metadata and container path to model context

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐
│ 1. Metadata  │ → │ 2. Fetch bundle│ → │ 3. Context   │
│   Fetch      │    │   Copy/unpack │    │   Update     │
│              │    │   to container│    │              │
└─────────────┘    └──────────────┘    └──────────────┘
```

## Exploratory Skill Execution

After loading a skill, the model **progressively explores** it:
- Examines skill files with shell commands (`ls`, `cat`, etc.)
- Selectively loads only the needed information
- Executes scripts directly inside the container

This mirrors the same pattern as **human developers reading documentation and using tools.**

## Version Management

Skills are managed as **versioned bundles:**
- Identified by skill ID
- Tracked by version number
- Uploaded, fetched, and updated via API

```python
# Creating a skilled container
skilled_container = client.containers.create(
    name="agent-with-skills",
    skills=[
        {"id": "skill_123", "version": "ver_20260311"}
    ]
)
```

## Relationship with OpenAI Harness Engineering

> "OpenAI is evolving from Harness Engineering (extending LLMs with tools for specific tasks) toward more general AI Agent Engineering (autonomous complex workflows via shell + skills + containers)."

- **Harness**: Fixed tools → fixed tasks (e.g., web search tool)
- **Skills**: Reusable workflows → applicable to multiple tasks

## Best Practices

1. **Narrow scope**: 1 skill = 1 clear workflow
2. **Pin versions**: Use fixed versions in production
3. **Self-contained**: Bundle all required resources within the skill
4. **Progressive exploration**: Design so models selectively load only the files they need

## Related Concepts

- [[concepts/harness-engineering]] — OpenAI's tool extension approach
- [[concepts/harness-engineering/system-architecture/container-context]] — Runtime environment where skills are deployed
- [[concepts/agent-loop-orchestration]] — Skill exploration and execution loop
-  — General concept of AI skills

## References

- [OpenAI: From model to agent](https://openai.com/index/equip-responses-api-computer-environment/)
- [[entities/openai]] — OpenAI
