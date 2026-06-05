---
url: "https://github.com/huggingface/skills"
title: "Hugging Face Skills — Agent Skills Repository"
date: 2026-06-05
source: github
---

# Hugging Face Skills

Hugging Face Skills are definitions for AI/ML tasks like dataset creation, model training, and evaluation. They are interoperable with all major coding agent tools like OpenAI Codex, Anthropic's Claude Code, Google DeepMind's Gemini CLI, and Cursor.

The skills follow the standardized Agent Skills format (agentskills.io).

## Available Skills (16)

| Name | Description |
|------|-------------|
| `hf-cli` | Execute Hugging Face Hub operations using the hf CLI |
| `huggingface-best` | Find the best AI model for any task by querying HF leaderboards and benchmarks |
| `huggingface-community-evals` | Add and manage evaluation results in HF model cards |
| `huggingface-datasets` | Explore, query, and extract data from any HF dataset using Dataset Viewer REST API |
| `huggingface-gradio` | Build Gradio web UIs and demos in Python |
| `huggingface-llm-trainer` | Train or fine-tune language models using TRL on HF Jobs infrastructure |
| `huggingface-local-models` | Select models to run locally with llama.cpp and GGUF |
| `huggingface-paper-publisher` | Publish and manage research papers on HF Hub |
| `huggingface-papers` | Look up and read HF paper pages in markdown |
| `huggingface-spaces` | Build, deploy, and maintain applications on HF Spaces |
| `huggingface-tool-builder` | Build reusable scripts for HF Hub and API workflows |
| `huggingface-trackio` | Track and visualize ML training experiments with Trackio |
| `huggingface-vision-trainer` | Train and fine-tune object detection and image classification models |
| `huggingface-zerogpu` | Coding rules for Gradio Spaces using HF ZeroGPU hardware |
| `train-sentence-transformers` | Train or fine-tune sentence-transformers models |
| `transformers-js` | Run ML models directly in JavaScript/TypeScript |

## Installation

Compatible with Claude Code, Codex, Gemini CLI, and Cursor.

- Claude Code: `/plugin marketplace add huggingface/skills` then `/plugin install <skill>@huggingface/skills`
- Codex: Copy/symlink to `.agents/skills`
- Gemini CLI: `gemini extensions install https://github.com/huggingface/skills.git --consent`
- Cursor: Via `.cursor-plugin/plugin.json` manifest

## Architecture

Skills are self-contained folders with:
- `SKILL.md` — YAML frontmatter (name, description) + instructions
- Supporting scripts, templates, and references
- Follows Agent Skills standard (agentskills.io)

Also available through Cursor Marketplace and Codex Plugins Directory.
