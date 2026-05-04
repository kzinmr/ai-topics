---
title: Mitchell Hashimoto
type: entity
created: 2026-05-04
updated: 2026-05-04
tags:
  - person
  - hashicorp
  - open-source
  - developer-tooling
aliases:
  - mitchellh
  - Hashimoto
sources:
  - raw/articles/2026-05-04_thorsten-ball-joy-and-curiosity-84.md
---

# Mitchell Hashimoto

Mitchell Hashimoto is a software engineer, open-source creator, and co-founder of **HashiCorp** (2012–2023). He is the original creator of several foundational DevOps tools—Vagrant, Packer, Consul, Terraform, Vault, Nomad, and Waypoint—and more recently the creator of **Ghostty**, a GPU-accelerated terminal emulator written in Zig.

## Key Facts

- **GitHub user #1299** (joined Feb 2008) — one of the earliest adopters
- Co-founded HashiCorp with Armon Dadgar in 2012
- Served as CEO (~4 years), CTO (~5 years), then individual contributor (~2 years)
- Left HashiCorp in December 2023 to focus on family and Ghostty
- Currently based in Los Angeles, CA

## Major Projects

| Project | Description |
|---------|-------------|
| [Vagrant](https://vagrantup.com) | Portable development environments via VM/container provisioning |
| [Terraform](https://terraform.io) | Infrastructure-as-Code (declarative cloud provisioning) |
| [Packer](https://packer.io) | Automated machine image creation |
| [Consul](https://consul.io) | Service discovery and configuration |
| [Vault](https://vaultproject.io) | Secrets management and encryption |
| [Nomad](https://nomadproject.io) | Cluster scheduler and orchestrator |
| [Ghostty](https://ghostty.org) | GPU-accelerated terminal emulator (Zig, 2024–) |

## The GitHub Exodus (2026)

In April 2026, Hashimoto announced he was leaving GitHub after 18 years, stating the platform had become too unstable and no longer optimized for shipping software:

> "I want to ship software and it doesn't want me to ship software. I can't code with GitHub anymore."

His departure came amid broader concerns about GitHub's reliability under "unprecedented scale from agents" — internal sources reported the team was dealing with **30X-ing capacity** within months due to AI agent traffic. Hashimoto began moving Ghostty's development to an alternative forge.

This event is part of a wider trend discussed in [[concepts/local-first-software]] and the growing "Forge" movement toward local-first development environments where the local repo represents the entire project (issues, PRs, etc.), not just code.

## Philosophy

- **AI as essential tooling**: Considers AI tooling essential for modern development
- **Technical philanthropy**: Ghostty is described as a form of giving back to the developer community
- **Native-first**: Advocates for native-feeling applications over Electron/web-based tools
- **Systems-level building**: Chose Zig for Ghostty for low-level control and performance

## Related

- [Ghostty](https://ghostty.org) — GPU-accelerated terminal emulator (Zig, 2024–)
- [[concepts/local-first-software]] — The Forge / local-first movement
- [[entities/armin-ronacher]] — Also discussed GitHub's loss of inevitability in the same period
