---
title: Qwen-MM-Plugins
created: 2026-08-10
updated: 2026-08-10
type: entity
tags:
  - qwen
  - alibaba
  - multimodal
  - agent-tooling
  - agent-skills
  - plugins
  - mcp
  - open-source
  - agent-harness
  - product
sources:
  - raw/articles/2026-07-29_qwen_qwen-mm-plugins.md
  - https://github.com/QwenLM/Qwen-MM-Plugins
---

# Qwen-MM-Plugins

> **"Make any agent harness multimodal-native."**

**Qwen-MM-Plugins** is an open-source multimodal plugin system for AI agent harnesses, developed by [[entities/qwen|Qwen Team]] at Alibaba. It packages vision, video, 3D, CAD, and educational capabilities as installable **skills + MCP servers**, enabling any agent harness to process images, video, documents, 3D models, and more — all with dynamic-resolution reading that auto-scales media to the VL model's patch grid. Released July 29, 2026 on [GitHub](https://github.com/QwenLM/Qwen-MM-Plugins) under Apache-2.0 (Python, 572 stars).

## Capabilities

Each capability is installed separately as a **skill** (so the model knows the toolset exists) plus an optional **MCP server** (the tools themselves, launched on demand via `uvx`).

| Capability | Description | Install Name | Tools |
|---|---|---|---|
| **core** | Foundational vision: dynamic-resolution reading of images/videos/documents/3D models, plus OCR, grounding, segmentation, ASR, vision chat, and web search | `qwen-mm-plugins-core` | Vision, OCR, grounding, segmentation, ASR, web search |
| **video-memory** | Long-video memory: hierarchical graph memory powering QA over very long videos | `qwen-mm-plugins-video-memory` | Video memory build, QA |
| **video-edit** | Video editing + generation: editing workflows plus image/video/audio generation | `qwen-mm-plugins-video-edit` | Video editing, image/video/audio generation |
| **blender** | Blender 3D modeling: drive a running Blender instance with 22 tools for modeling, materials, lighting, and rendering | `qwen-mm-plugins-blender` | 22 tools (thin client) |
| **freecad** | FreeCAD parametric CAD: drive a running FreeCAD instance with 14 tools for modeling, property edits, STEP/STL import/export, and FEM analysis | `qwen-mm-plugins-freecad` | 14 tools (thin client) |
| **edu-agent** | Educational tutorial videos: turn math/science problems into step-by-step Chinese explainer videos (skill-only, no MCP server) | `qwen-mm-plugins-edu-agent` | Skill-only |

## Architecture

```
Skill (toolset description)  +  MCP Server (tool execution)  =  Capability
       ↑                              ↑
  Model knows the              Launched on demand
  tools exist                  by uvx (no manual pip)
```

Each capability follows a **skill + optional MCP server** pattern:

- **Skill**: Declares the toolset so the model is aware of available tools and how to invoke them
- **MCP Server**: The actual tool implementations, launched on demand by `uvx` (requires [uv](https://docs.astral.sh/uv/)). Dependencies are installed automatically on first launch.
- **Dynamic-resolution reading**: All images, video frames, documents, and 3D models are auto-scaled to the VL model's patch grid — a 4K screenshot and a tiny thumbnail both receive the detail they need without manual resizing.

The system uses a single shared config file (`~/.qwen-mm-plugins/config`) that both GUI and terminal harnesses read, so configuration is set once.

## Supported Harnesses

A single guided installer script handles all supported harnesses:

| Harness | Install Method |
|---|---|
| **Claude Code** | `claude plugin marketplace add` + `plugin install` |
| **Codex** | `codex plugin marketplace add` + `plugin add` |
| **Qoder** | `qodercli plugins marketplace add` + `plugins install` |
| **OpenClaw** | `openclaw plugins install` |
| **Qwen Code** | `qwen extensions install` |
| **Gemini CLI** | Per-harness config (see [docs](docs/en/installation.md)) |

Other harnesses (opencode, pi, QwenPaw) register the skill + MCP in their own configuration. The project recommends: **just ask the agent** — "install `qwen-mm-plugins-<cap>`".

## Installation

### Guided Installer (Recommended)

One script handles install, configure, verify, and uninstall across all supported harnesses:

```bash
curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash
```

Or run one action at a time:

```bash
bash install.sh install     # Install selected capabilities
bash install.sh configure   # Set API keys and write config
bash install.sh verify      # Test installed capabilities
bash install.sh uninstall   # Remove capabilities
```

**Windows**: Use WSL2 (Ubuntu recommended) with the repo cloned inside the WSL home directory. Native Windows is not yet validated.

### Manual Per-Harness Installation

For plugin-marketplace harnesses (Claude Code, Qoder, Codex, OpenClaw, Qwen Code), add the marketplace then install:

```bash
# Claude Code
claude   plugin marketplace add https://github.com/QwenLM/Qwen-MM-Plugins.git
claude   plugin install qwen-mm-plugins-<cap>@qwen-mm-plugins

# Codex
codex    plugin marketplace add https://github.com/QwenLM/Qwen-MM-Plugins.git
codex    plugin add qwen-mm-plugins-<cap>@qwen-mm-plugins

# Qoder
qodercli plugins marketplace add https://github.com/QwenLM/Qwen-MM-Plugins.git
qodercli plugins install qwen-mm-plugins-<cap>@qwen-mm-plugins

# OpenClaw
openclaw plugins install qwen-mm-plugins-<cap> \
  --marketplace https://github.com/QwenLM/Qwen-MM-Plugins.git

# Qwen Code
qwen extensions install \
  https://github.com/QwenLM/Qwen-MM-Plugins.git:qwen-mm-plugins-<cap> --consent
```

## Configuration

API-based tools require API keys (native image/video/document reading does not):

| Variable | Required For |
|---|---|
| `DASHSCOPE_API_KEY` | vision_chat, OCR, grounding, ASR, generation, video-memory build |
| `SERPER_API_KEY` | web_search, web_extractor, image_search |

Export them in your shell or persist to `~/.qwen-mm-plugins/config`:

```bash
bash install.sh configure
```

System dependencies (`ffmpeg` for video/audio, optional `libreoffice` / `blender` / `texlive` / `chromium`) are checked by `bash install.sh verify`.

## Quick Start

Once a capability is installed, reference a file in your harness and ask — the model picks the right tool automatically:

```text
# core — read images, video, docs, 3D models; OCR, grounding, segmentation, ASR, web search
@dashboard-4k.png    Read every number in this dashboard.
@report.pdf          Summarize page 3.
@receipt.jpg         OCR this and total the line items.
@street.jpg          Draw a box around every car in the scene.

# video-memory — QA over long videos (first query auto-builds memory)
@lecture-2h.mp4      What are the main points, with timestamps?

# video-edit — image/video/audio generation + editing workflows
                     Generate a 1024x1024 image of a red panda coding at night.
@/path/to/media      Help me edit this video down to about 3 minutes.

# blender — drive a running Blender (22 tools)
                     Model a low-poly wooden stool, add a warm key light, and render it.

# freecad — parametric CAD in a running FreeCAD (14 tools)
                     Model an M6 hex bolt 30 mm long and export it as STEP.

# edu-agent — Chinese explainer videos (skill-only)
@geometry-problem.png  Explain how to solve this as a narrated video.
```

See each capability's [cookbook](https://github.com/QwenLM/Qwen-MM-Plugins/tree/main/cookbooks) for full tool listings, setup, and worked cases.

## Related Concepts

- [[entities/qwen]] — Parent entity: Alibaba's Qwen model family and team
- [[concepts/agent-plugins-1-0-0]] — The broader Agent Plugins 1.0.0 open standard for portable AI agent component packages
- [[concepts/mcp]] — Model Context Protocol, the tool-access standard that Qwen-MM-Plugins' MCP servers implement

## Sources

- [GitHub: QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) — Repository (572 stars, Apache-2.0)
- [[raw/articles/2026-07-29_qwen_qwen-mm-plugins.md]] — Raw article (README content, July 29, 2026)
