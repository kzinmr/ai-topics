# Capability-Based Security and AI Agent Sandboxing

Source: Wikipedia + Cowork Security Architecture (Medium)
URLs: https://en.wikipedia.org/wiki/Capability-based_security
      https://medium.com/ai-simplified-in-plain-english/cowork-security-architecture-when-ai-agents-meet-hard-isolation-efbfaff37806
Capture date: 2026-04-28

---

## Part 1: Capability-Based Security Fundamentals

**Capability-based security** is a security model where access to objects is governed by **capabilities**—communicable, unforgeable tokens of authority. Unlike traditional systems that rely on identity and ACLs, this model follows the **principle of least privilege** by directly sharing specific rights between programs.

### Core Concepts
- **Capability:** A value referencing an object combined with a specific set of access rights (like a "key").
- **Unforgeable:** Managed by the kernel/hardware to prevent user programs from modifying or creating them.
- **Ambient Authority:** In UNIX, authority is based on *who* runs a program. In capability systems, authority is based on *what* tokens the program holds.

### Example: Capability vs. Reference
```c
"/etc/passwd"                              // NOT a capability (just a string)
"/etc/passwd", O_RDWR                      // NOT a capability (lacks protection)
int fd = open("/etc/passwd", O_RDWR);      // IS a capability (protected handle)
```

### Solving the Confused Deputy Problem
In traditional systems, a process acting on behalf of two entities can be tricked into using its authority incorrectly. Capability systems mitigate this because authority is bundled with the reference itself.

### POSIX vs. True Capabilities
| Feature | POSIX "Capabilities" (Linux) | True Capability Systems |
|---------|------------------------------|------------------------|
| Granularity | Coarse-grained (CAP_NET_BIND_SERVICE) | Fine-grained (specific to one object) |
| Transferability | Cannot be transferred between processes | Designed to be delegated/shared |
| Object Association | Not associated with a specific object | Tied directly to a specific object |
| Namespace | Uses global namespaces | Often restricts/removes global namespaces |

### Active Systems Using Capability-Based Security
- **Fuchsia:** Google's capability-based OS
- **seL4:** High-assurance microkernel
- **WASI (WebAssembly System Interface):** Uses capability-based model for sandboxing
- **Capsicum (FreeBSD):** Hybrid approach, refines UNIX file descriptors into delegable capabilities
- **Genode:** OS framework built on microkernels

## Part 2: Cowork Security Architecture — AI Agents Meet Hard Isolation

The Anthropic Cowork desktop agent raised security questions about AI agents with direct filesystem access and command execution. The article proposes a capability-based security approach.

### Key Principle
Instead of granting blanket permissions (read/write all files), agents receive capabilities: bounded tokens that grant access to specific files, directories, or operations. Each capability can be delegated to sub-agents for specific tasks.

### Architecture Components
1. **Capability Registry:** Central mapping of what each agent can access
2. **Capability Delegation:** Sub-agents receive limited subsets of parent capabilities
3. **Audit Trail:** Every capability usage is logged
4. **Revocation:** Capabilities can be rescinded at runtime

### Comparison with Traditional Access Control
| Aspect | ACL/RBAC | Capability-Based |
|--------|----------|------------------|
| Authority source | Identity of user | Token held by program |
| Delegation | Difficult (needs admin) | Natural (pass token) |
| Granularity | Per-user/role | Per-object/operation |
| Agent suitability | Poor (agents impersonate users) | Excellent (agents hold bounded tokens) |
