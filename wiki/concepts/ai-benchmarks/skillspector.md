---
title: "NVIDIA SkillSpector"
type: concept
created: 2026-06-15
updated: 2026-06-15
tags:
  - benchmark
  - evaluation
  - security
  - nvidia
  - ai-agents
  - coding-agents
  - tool-use
  - agent-security
  - open-source
sources:
  - "https://github.com/NVIDIA/SkillSpector"
  - "https://hn.algolia.com/api/v1/search?query=skillspector"
status: active
---

# NVIDIA SkillSpector

**SkillSpector** is an open-source security scanner for AI agent skills, released by NVIDIA in June 2026. It detects vulnerabilities, malicious patterns, and security risks before installing agent skills used by coding agents such as Claude Code, Codex CLI, Gemini CLI, and other MCP-based tool ecosystems. The project gained attention on Hacker News with 47 points.

**GitHub**: [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | **License**: Apache 2.0 | **Python**: 3.12+

---

## What It Measures

Unlike traditional knowledge or coding benchmarks (MMLU, SWE-bench, HumanEval) that assess *capability*, SkillSpector evaluates *security posture* of agent skill packages. It answers the question: **"Is this skill safe to install?"**

Based on research from "Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale" (Liu et al., 2026):

| Finding | Value |
|---------|-------|
| Skills audited | 42,447 from major marketplaces |
| Vulnerable skills | 26.1% contain at least one vulnerability |
| Likely malicious | 5.2% show likely malicious intent |
| Risk multiplier | Skills with executable scripts are 2.12x more likely to be vulnerable |

---

## Methodology

SkillSpector uses a **two-stage detection pipeline**:

### Stage 1: Static Analysis (Fast, High Recall)

- **Regex-based pattern matching** across 11 static analyzers
- **AST-based behavioral analysis** detecting dangerous function calls (`exec()`, `eval()`, `subprocess`, `os.system`, `__import__()`, dynamic `getattr()`)
- **Live vulnerability lookups** via the [OSV.dev](https://osv.dev) API for known CVEs in dependencies (SC4 pattern) — no API key required, batch queries, 1-hour in-memory caching
- **YARA signature matching** for known malware, webshells, cryptominers, and hack tools
- **Taint tracking** for credential exfiltration chains and file-read-to-network flows

### Stage 2: LLM Semantic Analysis (Optional, High Precision)

- Evaluates context and intent of detected patterns
- Filters false positives from static analysis
- Provides human-readable explanations
- Improves precision to ~87%
- Supports OpenAI, Anthropic, and NVIDIA build.nvidia.com providers
- Includes anti-jailbreak protections to prevent malicious skills from manipulating the analysis

---

## Vulnerability Patterns

SkillSpector detects **64 vulnerability patterns** across **16 categories**:

| Category | Patterns | Key Risks |
|----------|----------|-----------|
| **Prompt Injection** | 5 | Instruction override, hidden directives, harmful content (CRITICAL) |
| **Data Exfiltration** | 4 | External transmission, env variable harvesting, context leakage |
| **Privilege Escalation** | 3 | Excessive permissions, sudo/root execution, credential access |
| **Supply Chain** | 6 | Unpinned deps, curl|bash RCE, obfuscated code, typosquatting |
| **Excessive Agency** | 4 | Unrestricted tool access, autonomous decisions, scope creep |
| **Output Handling** | 3 | Unvalidated output injection, cross-context flow, unbounded output |
| **System Prompt Leakage** | 3 | Direct leakage, indirect extraction, tool-based exfiltration |
| **Memory Poisoning** | 3 | Persistent context injection, window stuffing, memory manipulation |
| **Tool Misuse** | 3 | Parameter abuse, chaining to bypass checks, unsafe defaults |
| **Rogue Agent** | 2 | Self-modification (CRITICAL), unauthorized session persistence |
| **Trigger Abuse** | 3 | Overly broad triggers, shadow commands, keyword baiting |
| **Behavioral AST** | 8 | `exec()`/`eval()`, dynamic import, subprocess, dangerous execution chains |
| **Taint Tracking** | 5 | Direct/variable-mediated taint flow, credential exfiltration, external input to code execution |
| **YARA Signatures** | 4 | Malware, webshell, cryptominer, hack tool matches |
| **MCP Least Privilege** | 4 | Underdeclared capability, wildcard permissions, missing/overdeclared permissions |
| **MCP Tool Poisoning** | 4 | Hidden instructions, Unicode deception, parameter injection, description-behavior mismatch |

---

## Risk Scoring

| Score | Severity | Recommendation |
|-------|----------|----------------|
| 0-20 | LOW | SAFE |
| 21-50 | MEDIUM | CAUTION |
| 51-80 | HIGH | DO NOT INSTALL |
| 81-100 | CRITICAL | DO NOT INSTALL |

Scoring formula: CRITICAL +50, HIGH +25, MEDIUM +10, LOW +5, then 1.3x multiplier for executable scripts.

---

## Comparison to Other Benchmarks

| Dimension | SkillSpector | SWE-bench | MMLU Pro | HumanEval |
|-----------|-------------|-----------|----------|-----------|
| **What it measures** | Security vulnerabilities in agent skills | Real GitHub issue resolution | Multi-domain language understanding & reasoning | Single-shot code generation |
| **Evaluation type** | Static + LLM semantic analysis | Docker-based test pass/fail | 10-option multiple choice | Function correctness |
| **Output** | Risk score (0-100), severity labels | Pass rate (%) | Accuracy (%) | pass@k |
| **Domain** | Agent skill security | Software engineering | Broad knowledge & reasoning | Programming |
| **Contamination risk** | Low (skill-specific patterns) | High (public GitHub in training data) | Moderate (43% new questions) | High (widely memorized) |
| **Open source** | Yes (Apache 2.0) | Yes | Yes | Yes |
| **LLM dependency** | Optional (Stage 2) | No | No | No |
| **Agent-native** | Yes (designed for agent skills/MCP) | Yes (first agentic benchmark) | No | No |

SkillSpector occupies a unique niche: it is not a *capability* benchmark but rather a *security evaluation* tool specifically designed for the emerging [[ai-agents|AI agent]] ecosystem. While [[concepts/ai-benchmarks/swe-bench|SWE-bench]] tests whether agents can produce working code and [[concepts/ai-benchmarks/mmlu-pro|MMLU Pro]] tests knowledge breadth, SkillSpector tests whether the skill packages agents install are safe to run — addressing a gap that becomes critical as [[coding-agents|coding agents]] gain filesystem and network access.

---

## Ecosystem Position

SkillSpector sits at the intersection of three growing trends:

1. **Agent skill marketplaces**: As Claude Code, Codex CLI, and other coding agents adopt skill/plugin ecosystems, the attack surface for supply-chain-style vulnerabilities expands. SkillSpector provides the first dedicated scanner for this layer.

2. **MCP security**: The [[mcp|Model Context Protocol]] enables agents to call external tools. SkillSpector's MCP Least Privilege and MCP Tool Poisoning categories (8 patterns) address protocol-specific risks like underdeclared capabilities and hidden instructions in tool metadata.

3. **Evaluation infrastructure**: SkillSpector complements existing eval frameworks like [[inspect-ai|Inspect AI]] and [[promptfoo|promptfoo]] by adding a security dimension. It can be integrated into CI/CD pipelines via SARIF output, making it suitable for pre-deployment gatekeeping of agent skills.

---

## Limitations

- **Non-English content**: May miss patterns in other languages
- **Image-based attacks**: Cannot analyze text embedded in images
- **Encrypted/binary code**: Cannot analyze compiled or encrypted content
- **Runtime behavior**: Static analysis only — does not execute code to observe behavior
- **Offline SC4**: Without network access to OSV.dev, vulnerability lookups fall back to a small static list

---

## Usage

```bash
# Install
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector
uv venv .venv && source .venv/bin/activate
make install

# Scan a skill directory
skillspector scan ./my-skill/

# Scan with LLM analysis
export SKILLSPECTOR_PROVIDER=openai
export OPENAI_API_KEY=***
skillspector scan ./my-skill/

# Static-only (fast)
skillspector scan ./my-skill/ --no-llm

# CI/CD integration (SARIF output)
skillspector scan ./my-skill/ --format sarif --output report.sarif
```

---

## Related Pages

- [[concepts/ai-benchmarks/ai-resistant-evaluations]] — Designing benchmarks resistant to gaming and contamination
- [[concepts/ai-benchmarks/benchmaxxing]] — The critique of benchmark over-optimization (SkillSpector addresses security, not score-maxxing)
- [[concepts/harness-engineering]] — Agent execution environments and their security implications
- [[entities/inspect-ai]] — Open-source LLM eval framework by JJ Allaire + UK AISI
- [[concepts/evaluation/evals-for-ai-agents|Evals for AI Agents]] — Systematic guide to evaluating AI agents (security is one evaluation surface)
- [[entities/promptfoo]] — Open-source LLM eval & red-teaming framework with security scanning capabilities

---

## Sources

1. Liu et al. (2026). "Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale." 42,447 skills audited.
2. NVIDIA SkillSpector GitHub Repository. https://github.com/NVIDIA/SkillSpector
3. Hacker News discussion (47 points, Jun 2026). https://hn.algolia.com/api/v1/search?query=skillspector
4. OSV.dev — Open Source Vulnerability Database. https://osv.dev
