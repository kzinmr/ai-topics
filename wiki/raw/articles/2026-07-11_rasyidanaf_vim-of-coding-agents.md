---
title: "Vim of Coding Agents — Neovim-like Coding Agent Harnesses"
url: https://rasyidanaf.com/blog/vim-of-coding-agents/
author: Rasyidan A F
date: 2026-07-11
fetched: 2026-07-13
tags:
  - pi
  - coding-agent
  - neovim
  - plugin-system
  - harness-engineering
  - opencode
---

# Vim of Coding Agents | Rasyidan A F

A note on neovim-like coding agent harnesses

Every few months there is another new coding agent, another coding agent from some frontier AI lab. Codex, Claude Code, Factory Droid, Cursor, Kimi Code, Mistral Vibe, Copilot, and you name it. Each of these coding agents is quite opinionated. Each coding agent adds features that they think you may need, while the truth is that many features are unnecessary and might make the software more buggy in the end. This makes you, the user, rent someone else's setup and opinion of how to code with an LLM.

What if you could build your own custom coding agent and agent harness from a minimal foundation? If you are into, or familiar with, bare-bones minimal text editors like Vim/Neovim or Emacs that are very hackable, customizable, and can be riced further, you would love to have a coding agent with a similar philosophy.

Introducing pi, a minimal (terminal) coding agent, designed to adapt to your WORKFLOW instead of you adapting to the existing coding agent. Designed to let you build your own plugin, workflow, extension, etc. on your own just by asking (prompting) directly on pi. You can also ship your own plugin or package easily to other users like lazyvim via npm or git.

> There are many coding agents, but this one is mine.

## Discovery

Last year I saw someone try to make a very very simple coding agent on the everything app, X, and name it shittycoding agent. Back then, it was literally just a stupidly simple terminal coding agent tool. No plan mode, askQuestion tool, or sub-agent like Claude Code. Only read, write, edit, and bash.

Fast forward, OpenClaw. That AI assistant tool speedran GitHub stars growth and went viral on the internet. It ran on top of the Pi SDK.

## First-Time Experience

As a fellow Nix user, installed pi via llm-agents.nix by Numtide. The first thing I did on Pi was ask for a simple feature: a todo task tool and an AskUser tool. Pi read my global Pi npm directory, where the Pi library source code and docs are located.

Then I started asking Pi to customize and tweak the Pi TUI itself, which worked quite great. Not only are we able to customize the features and tools of Pi itself, but we can also design and hack the Pi TUI itself. You can even play Doom on Pi.

## Neovim Analogy

To show what makes Pi special among available coding agents, we can use an analogy where Pi is similar to how Neovim works:

- **Core app + extensions**: Neovim loads Lua/Vimscript for plugins → Pi loads TypeScript for plugins
- **Custom commands**: Neovim plugins add commands like :Telescope → Pi lets you add your own slash commands aka prompts/skills like /AskUser
- **Custom UI**: Neovim plugins can create floating windows, status lines, layouts → Pi extensions can be used for custom TUI components, dialogs
- **Configuration directories**: Neovim reads from ~/.config/nvim → Pi reads extensions from ~/.pi/

While you are using Neovim for reading, editing, and writing code/text, you are using Pi to run a coding agent with basic tools like read, edit, and bash.

Resource-utilization-wise, Pi already mogged both Claude Code and OpenCode. Only Codex remains to be mogging here.

## Plugin

The powerful feature of Pi is plugin creation, which is separated from the core software. Most of the Pi plugins I use were directly made by asking through prompts on Pi. You can browse a bunch of plugins available to download via npm on Pi Packages.

## Tradeoff & Comparison

### Feature Design

Pi is more like a bare-metal mechanical keyboard that you customize by yourself, while OpenCode is designed like a more polished and finished mechanical keyboard that you can still tinker with.

> OpenCode = Helix, Pi = Neovim

OpenCode ships with a built-in LSP, plan mode, subagents, multi-session, and an IDE extension. It also has a native desktop app and server configuration. Meanwhile, Pi only ships with read, write, search, and bash. Anything else might be either installed from someone who made a plugin or made by yourself.

### Plugin Model

OpenCode's plugin model is more like an external hook that can be integrated into the product itself. Pi feels more like the agent harness itself is programmable, either globally or at the project level (locally), so we can register tools, slash commands or skills, shortcuts, flags, event handlers, custom UI components, custom object renderers, etc.

The tradeoff: OpenCode gives you more out of the box. Pi gives you a deeper, more hackable and tweakable extension model, but that means you may need to assemble more and maintain your own preferred setup/workflow.

### Harness Cost & Performance

Using Databricks' internal benchmark, the Pi harness achieved roughly the same success rate as the models' native vendor harnesses (both Opus 4.8 and GPT 5.5). Depending on the model and reasoning level, Pi was between 1x and 2x cheaper per task.

A more feature-packed harness does not mean that it is automatically more effective.

## My Setup

- grill-me skill by mattpocock — interviews the user about a design or plan relentlessly
- jujutsu (jj) as the main version control system — simpler mental model than Git for AI-assisted coding
- exa search for third-party agentic web search integration
- Custom model inference from crof.ai for cheap custom GLM 5.2 Q8 inference

## TLDR

- Use **codex** or **claude code** if you do not want to own or tweak the harness
- Use **Opencode** if you want a polished coding agent with strong defaults (battery included)
- Use **Pi** if you want to own the harness, the workflow, and your weird personal configurations
