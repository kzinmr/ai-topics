---
title: "Jeff Geerling"
created: 2026-04-10
updated: 2026-04-10
tags: [person, blogger, hn-popular, homelab, devops, open-source, ai-skeptic]
aliases: ["jeffgeerling.com", "geerlingguy"]
---

# Jeff Geerling

| | |
|---|---|
| **Blog** | [jeffgeerling.com](https://www.jeffgeerling.com) |
| **RSS** | https://www.jeffgeerling.com/blog.xml |
| **About** | [https://www.jeffgeerling.com/about](https://www.jeffgeerling.com/about) |
| **Social** | [@geerlingguy](https://twitter.com/geerlingguy), [GitHub](https://github.com/geerlingguy), [YouTube](https://youtube.com/@JeffGeerling) |
| **Newsletter** | Patreon, GitHub Sponsors |

## Bio

Jeff Geerling (online handle: **geerlingguy**) is an independent developer, author, and YouTuber focused on infrastructure automation, open-source hardware, and DevOps. Owner/President of Midwestern Mac, LLC (2009-present). Former Technical Consultant at Ansible by Red Hat (2019-2021). Deeply involved in Linux, Ansible, Raspberry Pi, and Drupal communities. Author of multiple books on Ansible with 87k+ copies sold. Runs a popular YouTube channel covering hardware engineering, homelab infrastructure, and AI-on-edge computing.

## Core Philosophy

### 1. Corporate Open Source is Dead
Jeff has been a vocal critic of the deterioration of the corporate open-source social contract. The Red Hat/GPLv2 controversy (Red Hat restricting CentOS Stream source access) exemplified his concern:

> "Corporate Open Source is Dead" — companies that built businesses on open-source community labor are now walling off access, leaving volunteer maintainers to shoulder the burden.

He advocates for **direct sponsorship of maintainers** (Patreon, GitHub Sponsors) rather than relying on corporate benevolence. His own publishing model — self-publishing books, maintaining Ansible roles independently — is a practical implementation of this philosophy.

### 2. Local Control & Privacy First
Jeff is a staunch advocate of local-first computing and the right to repair:

> "I won't connect my dishwasher to your stupid cloud."

This extends across his infrastructure choices:
- **Self-hosted everything**: His blog runs on Hugo (static site generator), self-hosted
- **Local AI over cloud**: Runs LLMs locally via Ollama + Deepseek R1 on Raspberry Pi
- **Privacy-focused networking**: Pi-hole DNS, WireGuard VPNs, PTP/GPS time sync
- **Hardware sovereignty**: Raspberry Pi, Framework laptops, custom 10Gbps routers

### 3. The AI Emperor Has No Clothes
Jeff takes a grounded, skeptical view of AI hype:

- Documents AI voice cloning theft and misuse
- Prefers **practical, local AI** (object detection with Frigate + Hailo/Coral TPU) over cloud LLM APIs
- Focuses on **actual utility** over marketing claims — e.g., testing whether a $70 AI Kit delivers 13 TOPS in real workloads
- Emphasizes that most "AI problems" are actually **infrastructure and data problems**

### 4. Geerling's Law of Kubernetes: Simplicity Over Complexity
Jeff's approach to infrastructure automation:

- **Idempotency is non-negotiable** in Ansible — if a playbook isn't idempotent, it's broken
- **KISS principle**: K3s on Raspberry Pi clusters for learning and light production; avoid unnecessary orchestration complexity
- **Pragmatic testing**: Molecule + ansible-test + GitHub Actions for CI, with clean (ANSI-stripped) logs
- **Fix root causes, not symptoms**: e.g., aligning Docker and systemd to fix "Failed to connect to bus" rather than patching around it

### 5. Hardware as a Platform for Learning
Jeff's Raspberry Pi work goes far beyond hobbyist tinkering:

- **Full eGPU acceleration** on Pi 5 (with a 15-line kernel patch)
- **NVMe SSD boot** as the default — microSD cards are "nearing end-of-life" for SBCs
- **AI on the edge**: Hailo-8, Coral TPU, and NPU integration for real-time object detection
- **Large-scale testing**: 480 Pis given away, 100 SBCs for MrBeast, 25K Pi 4 8GB giveaway
- **Real-world benchmarking**: 10Gbps networking, WiFi 7, jumbo frames (9000 MTU)

## Key Projects & Contributions

| Project | Description |
|---------|-------------|
| **Ansible Roles** | 100+ Ansible Galaxy roles (geerlingguy.*), widely used in production |
| **Ansible for Kubernetes** | Book bridging Ansible automation with K8s concepts |
| **Ansible for DevOps** | Flagship book, 87k+ copies, 41 revisions, $300k+ revenue |
| **PiBox** | DIY NAS solution with ZFS RAIDZ1, 4-way NVMe RAID, bcache SSD caching |
| **Raspberry Pi Cluster** | K3s on Pi for learning and lightweight production workloads |
| **YouTube: Jeff Geerling** | Hardware reviews, homelab builds, AI-on-edge demos |
| **Midwestern Mac** | Consulting business, enterprise cloud deployments |

## Recent Thought Evolution (2025-2026)

### From Ansible Consultant to AI Infrastructure Critic
**Early period**: Focused on Drupal → Ansible → Kubernetes pipeline. Built enterprise automation tools and documented them extensively.

**2025-2026**: Shifted toward **AI hardware reality checks** — testing whether claims about on-device AI hold up under real benchmarks. His Pi 5 + eGPU work and AI Kit reviews reflect this pivot from pure DevOps to **AI infrastructure pragmatism**.

### The Open Source Sustainability Crisis
Jeff's position hardened after the Red Hat/CentOS controversy:

1. **Stop trusting corporate open-source stewardship** — companies will wall off access when it serves them
2. **Self-publish and self-fund** — his book revenue model ($300k across 41 revisions) proves independence is viable
3. **Sponsor individual maintainers** — not foundations, not companies, but the people doing the actual work

## Related Concepts
- [[open-source-sustainability]]
- [[homelab-infrastructure]]
- [[local-first-computing]]
- [[ai-on-the-edge]]
- [[ansible-automation]]

## Sources
- [jeffgeerling.com/about](https://www.jeffgeerling.com/about)
- [Ansible for DevOps (book)](https://www.ansiblefordevops.com/)
- [YouTube: Jeff Geerling](https://youtube.com/@JeffGeerling)
- [GitHub: geerlingguy](https://github.com/geerlingguy)
- Blog analysis: "Corporate Open Source is Dead", "The AI Emperor Has No Clothes", "I won't connect my dishwasher to your stupid cloud"
