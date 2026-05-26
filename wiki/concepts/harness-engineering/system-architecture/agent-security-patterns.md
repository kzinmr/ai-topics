---
title: "Agent Security Patterns"
type: concept
aliases:
  - agent-security
  - container-security
  - egress-proxy
  - secret-injection
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - architecture
  - harness-engineering
  - security
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
---

# Agent Security Patterns

**Security control patterns** for agents to interact safely with external systems. Implemented in the container environment of OpenAI's Responses API.

## Three Layers of Security

### 1. Sidecar Egress Proxy

```
┌─────────────────────────────────────────────┐
│  Agent Container                            │
│  ┌─────────────┐    ┌──────────────────┐    │
│  │   Model/     │ →  │  Sidecar Egress  │ →  External API/Internet
│   │   Shell Cmd   │    │     Proxy        │    │
│  └─────────────┘    └──────────────────┘    │
│                          │                   │
│                    Policy Application         │
│                    - Domain allowlist         │
│                    - Access control           │
│                    - Traffic observation      │
└─────────────────────────────────────────────┘
```

- **All** outbound requests pass through a centralized policy layer
- Access control via domain-based allowlists
- Full traffic observability

### 2. Domain-Scoped Secret Injection

| Location | Sees |
|------|-----------|
| **Model/Container** | Placeholder (e.g., `{{API_KEY}}`) |
| **Egress Proxy** | Actual secret value (applied only to permitted domains) |

```python
# Model prompt template
prompt = "Call the API at https://api.example.com with key: {{API_KEY}}"

# Egress proxy replaces at runtime
actual_request = "Authorization: Bearer sk-actual-secret-value"
```

**Benefits**:
- Secrets are never exposed in model context
- Prevents unintended data leakage
- Only applied to permitted destinations

### 3. Network Policies

- **Allowlist-based**: Only explicitly permitted domains accessible
- **Principle of least privilege**: Only essential external access allowed
- **Observability**: All traffic monitored and logged

## Security Risks and Countermeasures

| Risk | Countermeasure |
|--------|------|
| Secret leakage | Domain-scoped injection |
| Unintended external access | Egress proxy + allowlist |
| Data exfiltration | Traffic observation + policy enforcement |
| Internal system access | Network isolation |

## Design Philosophy

> "At the same time, giving containers unrestricted internet access can be risky: it can expose information to external websites, unintentionally touch sensitive internal or third-party systems, or make credential leaks and data exfiltration harder to guard against."

OpenAI adopts "restricted network access" as the default, explicitly permitting only essential external access.

## Best Practices

1. **Least privilege**: Only add necessary domains to allowlist
2. **Secret isolation**: Use placeholders, never embed directly
3. **Monitoring**: Log all egress traffic
4. **Progressive exposure**: Tighten policies from dev → test → production

## Related Concepts

- [[concepts/harness-engineering/system-architecture/container-context]] — Execution environment where security controls are applied
- [[concepts/harness-engineering/system-architecture/agent-loop-orchestration]] — Secure command execution
- [[openai-responses-api-code-execution]] — Foundation API providing security features
## References

- [OpenAI: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- [[entities/openai]] — OpenAI
