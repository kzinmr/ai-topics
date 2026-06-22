---
title: "Hugging Face Skills"
type: concept
created: 2026-06-05
updated: 2026-06-05
tags:
  - huggingface
  - ai-agents
  - coding-agents
  - developer-tooling
  - fine-tuning
  - training
  - architecture
  - open-source
sources:
  - raw/articles/2025-12-04_hf-skills-training.md
  - raw/articles/2026-06-05_huggingface-skills-repo.md
  - https://github.com/huggingface/skills
---

# Hugging Face Skills

**Hugging Face Skills** is an open-source repository of standardized agent skill definitions for AI/ML tasks — model training, dataset management, evaluation, deployment, and more. Skills are interoperable across all major coding agents: Claude Code, OpenAI Codex, Gemini CLI, and Cursor. The repository lives at [github.com/huggingface/skills](https://github.com/huggingface/skills) and follows the [Agent Skills](https://agentskills.io) standard format.

## Architecture

Each skill is a self-contained folder containing:
- **`SKILL.md`** — YAML frontmatter (`name`, `description`) followed by structured instructions the coding agent follows while the skill is active
- **Supporting scripts** — Helper scripts for automation
- **References** — Detailed documentation (hardware guides, training method docs)

Skills are discovered and loaded by coding agents via the Agent Skills standard. For agents without native skill support, an `AGENTS.md` fallback bundle is provided.

## Available Skills (16)

| Skill | Domain | Description |
|-------|--------|-------------|
| `hf-cli` | Hub operations | Execute Hub operations via the [[concepts/hf-cli\|hf CLI]] — search models, manage datasets/buckets, launch Spaces, run Jobs |
| `huggingface-best` | Model discovery | Find the best model for any task via HF leaderboards and benchmarks |
| `huggingface-community-evals` | Evaluation | Add/manage eval results in model cards, import from Artificial Analysis API |
| `huggingface-datasets` | Data | Explore/query/extract from HF datasets via Dataset Viewer REST API + parquetlens SQL |
| `huggingface-gradio` | UI | Build Gradio web UIs and demos |
| `huggingface-llm-trainer` | Training | Train/fine-tune LLMs via TRL on HF Jobs — SFT, DPO, GRPO, reward modeling, GGUF conversion |
| `huggingface-local-models` | Local inference | Select and run models locally with llama.cpp/GGUF on CPU, Metal, CUDA, ROCm |
| `huggingface-paper-publisher` | Publishing | Publish/manage research papers on HF Hub |
| `huggingface-papers` | Research | Look up and read HF paper pages with structured metadata |
| `huggingface-spaces` | Deployment | Build/deploy/maintain apps on HF Spaces — Gradio, Docker, Static, ZeroGPU |
| `huggingface-tool-builder` | Automation | Build reusable scripts for HF Hub/API workflows |
| `huggingface-trackio` | Monitoring | Track/visualize ML training experiments with real-time dashboards |
| `huggingface-vision-trainer` | Vision training | Train object detection (RTDETRv2, YOLOS, DETR) and image classification models |
| `huggingface-zerogpu` | GPU sharing | Coding rules for Gradio Spaces using ZeroGPU hardware |
| `train-sentence-transformers` | Embeddings | Train/fine-tune sentence-transformers (bi-encoder, CrossEncoder, SparseEncoder/SPLADE) |
| `transformers-js` | Web inference | Run ML models in JavaScript/TypeScript with WebGPU/WASM |

## Installation

Skills are compatible with Claude Code, Codex, Gemini CLI, and Cursor:

| Agent | Installation |
|-------|-------------|
| **Claude Code** | `/plugin marketplace add huggingface/skills` → `/plugin install <skill>@huggingface/skills` |
| **Codex** | Copy/symlink to `.agents/skills/` |
| **Gemini CLI** | `gemini extensions install https://github.com/huggingface/skills.git --consent` |
| **Cursor** | Via `.cursor-plugin/plugin.json` manifest or Cursor Marketplace |

## hf-llm-trainer: Agent-Driven Fine-Tuning

The flagship skill — `hf-llm-trainer` — enables coding agents to handle the **full lifecycle of model fine-tuning** through natural language conversation:

1. **Dataset validation** — Agent inspects format compatibility for SFT/DPO/GRPO before spending GPU time
2. **Hardware selection** — Automatic GPU selection based on model size (t4-small for <1B, a10g-large for 3-7B with LoRA)
3. **Script generation** — TRL-based training scripts with Trackio monitoring integration
4. **Job submission** — Submit to [[entities/hugging-face|Hugging Face]] Jobs cloud infrastructure
5. **Progress monitoring** — Real-time loss/metrics via Trackio dashboards
6. **GGUF conversion** — Merge LoRA adapters, convert to GGUF, quantize (Q4_K_M), push to Hub for local deployment via llama.cpp

### Supported Training Methods

| Method | Use Case | Notes |
|--------|----------|-------|
| **SFT** (Supervised Fine-Tuning) | Demonstration data → model behavior | Most projects start here |
| **DPO** (Direct Preference Optimization) | Preference pairs (chosen/rejected) | After initial SFT stage |
| **GRPO** (Group Relative Policy Optimization) | Verifiable tasks (math, code) | RL without reward model |

### Cost Model

- **Demo runs**: ~$0.30–0.50 (100 examples, t4-small)
- **Production SFT** (0.6B): ~$1–2 on t4-small
- **Production SFT** (3-7B with LoRA): ~$15–40 on a10g-large
- **7B+**: Not recommended for this skill pipeline

## Relation to Agent Skills Ecosystem

Hugging Face Skills is a significant contribution to the emerging **agent skills** ecosystem:
- Follows the open [Agent Skills](https://agentskills.io) standard — not vendor-locked
- Skills are **domain-specific instruction bundles** — a pattern complementary to [[concepts/coding-agents/hf-cli|hf CLI]] (which is a tool, not a skill)
- The `hf-cli` skill is the recommended first install — it teaches agents the full Hub command surface
- Marketplace integrations (Cursor, Codex) lower adoption friction

This represents Hugging Face's strategy of making the Hub **the default infrastructure for agent-driven ML workflows** — from data curation to model deployment.

## Related Pages

- [[entities/hugging-face]] — Parent organization and Hub infrastructure
- [[concepts/coding-agents/hf-cli]] — The CLI tool that the `hf-cli` skill wraps
- [[concepts/harness-engineering/agent-ergonomics]] — Agent-oriented tool design principles
- [[concepts/cli-first-development]] — CLI-first design philosophy
- [[entities/clefourrier]] — HuggingFace team (evaluation)
