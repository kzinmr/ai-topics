---
title: "DeerFlow 2.0 — ByteDance Open-Source SuperAgent Harness"
source: https://github.com/bytedance/deer-flow
date: 2026-02-28
type: product-release
org: ByteDance
repo: bytedance/deer-flow
stars: 67500
---

# DeerFlow 2.0: ByteDance's Open-Source SuperAgent Harness

DeerFlow (Deep Exploration and Efficient Research Flow) is an open-source super agent harness by ByteDance that orchestrates sub-agents, memory, and sandboxes. MIT licensed.

v2.0 is a ground-up rewrite (no shared code with v1). Claimed #1 GitHub Trending on February 28, 2026 with 67.5k+ stars.

Core capabilities:
- Long/short-term memory for context engineering
- Planning and sub-tasking with sequential or parallel execution
- Extensible skills and tools system
- Persistent sandbox with file system (Docker-based, recommends AIO Sandbox)
- Multi-model support: Doubao, DeepSeek, OpenAI, Gemini
- Recommended models: Doubao-Seed-2.0-Code, DeepSeek v3.2, Kimi 2.5

Integrates InfoQuest (BytePlus intelligent search/crawling toolset). Partnered with BytePlus/Volcengine for cloud deployment.

Architecture: backend (Python) + frontend (Node.js), Docker deployment, skills loaded progressively (only what's needed).

Official site: deerflow.tech
