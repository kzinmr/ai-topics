---
name: Capabilities-Based Security
type: concept
tags: [security, sandbox, agents, monty, zero-trust, formal-methods]
related:
  - [[concepts/monty-sandbox]]
  - [[concepts/code-mode]]
  - [[concepts/harness-engineering]]
  - [[entities/samuel-colvin]]
depth: L2
status: complete
created: 2026-04-16
---

# Capabilities-Based Security for AI Agents

## Definition

A security model where systems start with **zero access** and capabilities are explicitly granted one by one, rather than starting with full access and restricting down.

## The Two Approaches

| Approach | Starts With | Security Model | Analogy |
|----------|-------------|----------------|---------|
| **Traditional Sandbox** | Full VM/container | Block known-bad things | Firewall blocking bad ports |
| **Capabilities-Based** | Nothing | Allow only known-good things | Zero-trust network |

> *"Start from nothing, then selectively grant capabilities. The default is zero access — no filesystem, no network, no environment variables, strict resource limits. You explicitly opt in to each capability via external functions that you wrote, you control, and you can audit."* — Samuel Colvin

## Implementation in Monty

Monty demonstrates capabilities-based security for AI agent code execution:

1. **No default access**: The interpreter starts with zero capabilities
2. **External function registration**: Host process explicitly registers what the LLM code can call
3. **Type stubs**: LLM code sees only the interfaces you expose
4. **Resource limits**: Memory, recursion depth, execution time capped by host
5. **No third-party packages**: LLM code cannot `import requests` or access arbitrary libraries

## Why It Matters for AI Agents

LLM-generated code is inherently untrusted. Traditional sandboxing assumes:
- The sandbox is correctly configured
- All vulnerabilities are patched
- No escape vectors exist

Capabilities-based security assumes:
- The code will try to escape
- Default = deny everything
- Only explicitly granted operations succeed

This is closer to **formal methods** in mathematics (Samuel Colvin's PhD background in geometric group theory) than traditional devops practice.

## Related

- [[concepts/monty-sandbox]] — Primary implementation
- [[concepts/code-mode]] — Use case
- [[concepts/harness-engineering]] — Harness environment design
- [[concepts/ai-agent-engineering/agent-security-patterns]] — OpenAI's Egress Proxy approach
