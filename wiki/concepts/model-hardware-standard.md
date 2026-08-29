---
title: "Model Hardware Standard (MHS)"
created: 2026-08-29
updated: 2026-08-29
type: concept
tags:
  - protocol
  - mcp
  - ai-agents
  - anthropic
  - robotics
  - ai-in-science
  - self-driving-labs
  - agent-tooling
  - open-source
sources:
  - raw/articles/2026-08-28_anthropic_model-hardware-standard-preview.md
confidence: high
---

# Model Hardware Standard (MHS)

## Overview

The **Model Hardware Standard (MHS)** is Anthropic's shared specification for AI agents to safely operate physical devices — lab instruments and manufacturing equipment. Announced as a research preview on August 28, 2026 (HN: 133 points), it opens to a first group of scientific research labs and advanced manufacturers, with plans to open-source the standard after the preview. ^[raw/articles/2026-08-28_anthropic_model-hardware-standard-preview.md]

MHS began as a collaboration between Anthropic's Beneficial Deployments team (Alek Kemeny) and **HHMI Janelia Research Campus** (postdoc Arco Bast), who had built a shared-memory dictionary to let brain-imaging instruments from different vendors communicate at memory speed; Kemeny and Bast then integrated AI models into that interface.

## The Problem

- Lab/manufacturing hardware integration typically takes **weeks to months**; most devices don't communicate with each other and require bespoke integrations by specialists.
- Even once connected, there is no common way for devices to share data with an AI agent, nor a standard for letting the agent operate devices **safely**.

## How It Works

- **Standardized driver**: software translating between the OS and the hardware device.
- **Simple primitives**: commands like `read` ("get temperature") / `write` ("set temperature") that any device can understand and act on.
- **Standard discoverability**: devices announce themselves in a common format, so devices and agents find each other across networks without bespoke "translator" programs.
- **Machine-characteristic metadata**: the driver conveys device characteristics not discernible from code alone, letting an agent operate hardware it has never seen before.
- **Model-agnostic & harness-agnostic**: works with any device that has a programmable interface; any agent harness can access it via standard protocols such as the **Model Context Protocol (MCP)**.

Use cases span parallel operation of microscopes, liquid handlers, and robotic arms — from routine drug-discovery experiments to laser calibration on a quantum computer — including autonomous round-the-clock experiments where agents reason through each step, update parameters in real time, and sometimes recover from hardware errors without intervention.

## Industry Partners

Hardware/software vendors building MHS support: **AWS** (Strands Robots library; private pre-release for preview participants), **Automata** (LINQ lab automation platform), **Danaher** (smart instruments / autonomous labs), **Doosan Robotics** (robotic arms, automated QA), **MBF Bioscience** (MHS driver for ScanImage laser-scanning microscopy), **QIAGEN** (proof-of-concept on QIAsymphony Connect nucleic acid purification), **Tecan** (Fluent liquid handling platforms), **Universal Robots** (early access, plans platform support).

## Safety Limitations

- Claude learns the physical world through text and images — **spatial and physical reasoning limitations** still require expert oversight. Genentech researchers had to guide Claude to recognize that sample foaming errors were *physical* failures, not software bugs.
- MHS doesn't work with hardware lacking a programming interface; Anthropic is working with such manufacturers.
- Anthropic will release research-preview findings as part of its guidance for deploying the standard safely.

## Significance

MHS is the hardware-layer counterpart to [[concepts/mcp|Model Context Protocol]] for software tools: MCP standardized how agents call tools, MHS standardizes how agents touch the physical world. Combined with the concurrent **Trail of Bits VM-containment warning** (August 27) and the [[concepts/agent-sandbox-patterns]] debate, it marks August 2026 as the month agent safety moved from sandboxes to **physical actuation risk**. It also feeds directly into the [[concepts/self-driving-labs|self-driving lab]] / autonomous-science trend alongside [[concepts/alphaevolve]] and the Station multi-agent math discovery work.

## See Also

- [[concepts/mcp]] — Model Context Protocol, the software-tool analog
- [[concepts/agent-sandbox-patterns]] — deployment patterns for agent containment
- [[entities/anthropic]] — Anthropic
- [[concepts/ai-in-science]] — AI in science
- [[concepts/alphaevolve]] — AlphaEvolve (optimization-driven discovery)
- [[concepts/station-autonomous-math-discovery]] — Station multi-agent mathematical discovery
