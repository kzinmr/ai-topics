---
title: "Avi Kivity"
created: 2026-04-30
updated: 2026-04-30
tags: [person, infrastructure, virtualization, cloud]
aliases: ["avi.im", "iavins"]
related: [[concepts/zero-disk-architecture]]
sources: ["https://avi.im"]
---

# Avi Kivity

| | |
|---|---|
| **Blog** | [avi.im/blag](https://avi.im/blag/) |
| **X/Twitter** | [@iavins](https://x.com/iavins) |
| **Known For** | Creator of **KVM** (Kernel-based Virtual Machine), QEMU contributor |
| **Role** | Software engineer, virtualization expert |
| **Themes** | Virtualization, cloud infrastructure, database architecture, systems programming |

## Overview

**Avi Kivity** is a software engineer best known as the creator of **KVM** (Kernel-based Virtual Machine), the Linux kernel virtualization infrastructure that became the foundation for most cloud computing platforms. KVM was merged into the mainline Linux kernel in 2007 and is used by AWS, Google Cloud, and most other major cloud providers.

He writes a technical blog at [avi.im/blag](https://avi.im/blag/) covering systems programming, cloud infrastructure, and database architecture.

## Key Work

### KVM (Kernel-based Virtual Machine)
KVM is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V). It consists of a loadable kernel module (`kvm.ko`) that provides the core virtualization infrastructure and a processor-specific module (`kvm-intel.ko` or `kvm-amd.ko`). KVM was acquired by Red Hat in 2008 and remains the dominant hypervisor in cloud infrastructure.

### QEMU
Avi has been a significant contributor to QEMU, the open-source machine emulator and virtualizer. KVM works alongside QEMU to provide hardware-assisted virtualization.

## Core Ideas

### Zero Disk Architecture (2024)
In his article ["Zero Disk Architecture"](https://avi.im/blag/2024/zero-disk-architecture/), Avi proposes that databases should offload all persistent state to managed object storage (S3), achieving:
- **Infinite scalability** by decoupling compute from storage
- **Instant elasticity** — stateless compute can start/stop/move freely
- **Eleven nines durability** via S3's 99.999999999% durability guarantee

He describes S3 as the **"malloc of the web"** — the primary memory allocator for modern cloud infrastructure, abstracting away physical storage management just as `malloc()` abstracts physical memory.

### The LCD Model
For Zero Disk architectures, Avi identifies the fundamental trade-off triangle:
1. **Latency** — fast writes to small objects
2. **Cost** — batching to reduce per-operation overhead
3. **Durability** — waiting for S3 confirmation vs. caching locally

## Recent Themes (2024–2026)
- **Zero Disk Architecture** — pushing cloud-native databases toward full storage disaggregation
- **S3 as infrastructure primitive** — treating object storage as a compute resource, not just backup
- **LSM Trees vs B-Trees** — why log-structured merge trees are better suited for object storage workloads

## Related People
- [[entities/andrej-karpathy]] — Both write extensively about systems-level AI/infrastructure concepts
- [[entities/simon-willison]] — Fellow blogger covering practical infrastructure topics

## Sources
- [avi.im/blag](https://avi.im/blag/)
- [Zero Disk Architecture article](https://avi.im/blag/2024/zero-disk-architecture/)
- [KVM Wikipedia](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine)

## References

- 2024_avi-im_zero-disk-architecture
