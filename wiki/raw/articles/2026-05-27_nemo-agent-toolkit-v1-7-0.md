> Source: https://github.com/NVIDIA/NeMo-Agent-Toolkit/releases/tag/v1.7.0
> Date: May 21, 2026
> Repository: NVIDIA/NeMo-Agent-Toolkit (2K stars, Python)

# NeMo Agent Toolkit v1.7.0 Release

## Notable Highlights
- AI coding agent skills for NeMo Agent Toolkit
- Consent-gated runtime telemetry for NAT CLI commands

## New Features
- ATIF trajectory exporter for Phoenix visualization and debugging
- Exa Search API integration as internet search tool
- OCI LangChain support for hosted Nemotron workflows
- ATOF v0.1: Agentic Trajectory Observability Format (aligned spec)
- Arize AX OTLP exporter with docs and examples
- Token streaming support for ReAct Agent

## Breaking Changes
- OpenAI dependency migration from 1.x to 2.x
- Removed optuna, chain, openinference from core package
- Removed nvidia-nat-vanna integration package

## Improvements
- OAuth2 support: client-id-only MCP OAuth2
- Dependency slimming (flask, aioboto3, plotly, wikipedia moved)
- Security: stop leaking exception details in chat_completion errors
- Model name modernizations (llama-nemotron-embed-1b-v2, etc.)
- Health check now checks for deprecation headers
