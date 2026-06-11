---
title: Capability-Based Security
created: 2026-04-25
updated: 2026-05-26
type: concept
tags:
  - security
  - architecture
  - sandbox
  - inference
aliases:
  - capabilities-based-security
sources:
  - raw/articles/crawl-2026-04-28-capability-based-security.md
---

# Capability-Based Security

Capability-Based Security is a security model that bases access control on **capabilities (authority tokens)** rather than identity. It is gaining attention as a promising alternative to traditional ACL/RBAC for AI agent sandbox design.

## Basic Concepts

A **capability** is a communicable, unforgeable authority token that combines a reference to an object with specific access rights.

Unlike traditional UNIX permissions (based on `who` is executing), the capability model determines authority based on **"what tokens the program holds."**

| Comparison | Traditional Model (ACL/RBAC) | Capability Model |
|------|----------------------|-------------------|
| Source of authority | User identity | Tokens held by the program |
| Delegation | Difficult (requires admin privileges) | Natural (just pass the token) |
| Granularity | Per user/role | Per object/operation |
| Namespace | Global (high abuse risk) | Restrictable |

## Capabilities vs Mere References

```python
"/etc/passwd"                      # NOT a capability (just a string)
open("/etc/passwd", O_RDWR)        # A capability (OS-protected handle)
```

## Confused Deputy Problem

In traditional ACL systems, a "secretary program" opening a file on behalf of User A may also read User B's files using the same authority. In capability systems, this problem is resolved because only the specific token passed for each request is used.

## Relevance to AI Agents

For AI agent security, the capability-based approach is particularly important:

### Why Traditional Access Control is Insufficient
- Agents run under the same user account and inherit all its privileges
- Agents dynamically interpret tasks and access files/APIs in unpredictable order
- Risk of leaking all parent agent privileges when calling sub-agents

### Solution with Capability-Based Approach
1. **Least privilege:** Each agent holds tokens that only allow access to specific files/operations
2. **Delegation control:** Only delegate narrower capabilities to sub-agents than the parent holds
3. **Auditing:** All capability usage can be logged
4. **Revocation:** Capabilities can be dynamically revoked at runtime

## Current Implementations

| System | Capability Implementation |
|---------|-------------------|
| **WASI (WebAssembly)** | Filesystem and network access are capability-based. WASI programs can only use explicitly passed privileges |
| **Fuchsia (Google)** | All processes are capability-based. Unauthorized namespace operations are impossible |
| **seL4** | High-assurance microkernel. All kernel operations managed via capabilities |
| **Capsicum (FreeBSD)** | Extends UNIX file descriptors to true capabilities. Disables global namespace in `capability mode` |
| **Genode** | Microkernel-based OS framework |

## Application to AI Agent Sandboxing

In the context of [[concepts/security-and-governance/agent-sandboxing]], WASI's capability model is particularly important:
- The WASM runtime blocks all filesystem access
- Only explicitly passed capabilities (file descriptors) are permitted
- Enforces "default deny" at the hardware/runtime level

## Differences from POSIX Capabilities

Linux's `CAP_*` (e.g., `CAP_NET_BIND_SERVICE`) are called "POSIX Capabilities" but differ from true capabilities in the following ways:
- Coarse-grained (not associated with specific objects)
- Cannot be transferred between processes
- Depends on global namespaces

## Related Concepts

- [[concepts/security-and-governance/agent-sandboxing]] — Main application of capability-based isolation
- [[concepts/sandbox/in-process]] — Relationship between WASM and in-process sandboxing
- [[concepts/sandbox/infrastructure]] — Comparison with OS/hypervisor-level isolation
- [[concepts/sandbox/js-runtime]] — Browser-based capability model
