---
title: Michael Stapelberg
created: 2026-04-09
updated: 2026-04-10
tags:
  - person
  - blogger
  - hn-popular
  - debian
  - nixos
  - linux
  - infrastructure
  - i3-wm
---


# Michael Stapelberg

| | |
|---|---|
| **Blog** | [michael.stapelberg.ch](https://michael.stapelberg.ch) |
| **RSS** | https://michael.stapelberg.ch/feed.xml |
| **GitHub** | [stapelberg](https://github.com/stapelberg) |
| **Role** | Software engineer, Debian Developer, creator of i3 tiling window manager |
| **Known for** | i3 window manager, Debian contributions, NixOS advocacy, distri Linux, kinX mechanical keyboard, practical infrastructure engineering |
| **Bio** | Software engineer based in Switzerland. Debian Developer since the mid-2000s. Creator of the i3 tiling window manager (2009), one of the most popular Linux window managers. Has been running a technical blog since 2005. Recently migrated personal infrastructure to NixOS and advocates for declarative, reproducible systems. |

## Core Ideas

Michael Stapelberg is a **pragmatic systems architect** — someone who has spent two decades building and maintaining real-world infrastructure, from the i3 window manager (used by hundreds of thousands) to Debian packages to his own NixOS-based home lab. His writing is characterized by hands-on experimentation, clear threat models, and a willingness to adopt new tools when they demonstrably improve upon the old.

### Coding Agent VMs: Sandboxing AI Agents

Stapelberg's most recent major essay, ["Coding Agent VMs on NixOS with microvm.nix"](https://michael.stapelberg.ch/posts/2026-02-01-coding-agent-microvm-nix/), addresses a critical question: **how do you safely use AI coding agents without exposing your personal data?**

His solution: ephemeral micro-VMs on NixOS where coding agents can operate in isolation. The VM has no access to personal files, and if compromised, can be destroyed and recreated instantly.

> *"I don't feel like they're automatically making existing tasks faster. But rather, they make entirely new workflows possible that simply didn't exist before."*

This reflects his broader view of AI agents: **they're not productivity multipliers for existing work; they're enablers of new categories of work**. The maintenance effort for the VM infrastructure is minimal because NixOS configurations are declarative and reproducible.

### The NixOS Conversion

Stapelberg's migration to NixOS (after a ~10 year break) is documented across several blog posts and represents a significant philosophical shift:

- **Declarative installation** — "How I like to install NixOS" describes network boot and fully declarative setup
- **Infrastructure as code** — Migrating his NAS from CoreOS/Flatcar to NixOS, replacing Docker with native NixOS modules
- **Secret management** — Using sops-nix for declarative secrets (passwords, cryptographic keys)
- **Development shells** — "Four quick examples" of Nix development environments replacing ad-hoc setup scripts

His NixCon 2025 trip report indicates deep engagement with the NixOS community and a commitment to **declarative systems as the right abstraction level for infrastructure**.

### Stamp It! — Version Transparency

In ["Stamp It! All Programs Must Report Their Version"](https://michael.stapelberg.ch/posts/2026-01-stamp-it/), Stapelberg argues that every program should report its version when invoked:

> The principle: if you can't determine what version of a program is running, you can't debug it, can't reproduce it, and can't trust it.

This extends his long-standing belief that **reproducibility is the foundation of reliable systems**. Whether it's a binary on your laptop or a container in production, you should always know exactly what code is running.

### The Wayland Transition

["Can I finally start using Wayland in 2026?"](https://michael.stapelberg.ch/posts/2026-01-wayland/) is particularly notable given Stapelberg's history: **he created i3 for X11 in 2009**, one year after the Wayland project started. His willingness to finally adopt Wayland — despite being one of the most prominent X11 tooling creators — signals a maturation of the Wayland ecosystem and a pragmatism that values working systems over ideological loyalty.

### Hardware Pragmatism

Stapelberg writes candidly about hardware failures and transitions:
- **"Bye Intel, hi AMD!"** — After two dead Intel CPUs, he switched to AMD
- **"Intel 9 285K on ASUS Z890: not stable!"** — Documenting real-world hardware instability
- **"Ryzen 7 Mini-PC makes a power-efficient VM host"** — Choosing hardware for actual workload requirements

His approach: **document failures honestly, switch vendors when warranted, and choose hardware based on measured performance rather than brand loyalty**.

### Debugging Go Programs

Stapelberg has written extensively about debugging Go programs, particularly hanging processes:

> *"Tips to debug hanging Go programs"* — A practical guide covering goroutine dumps, profiling, and systematic investigation of deadlocks.

His debugging philosophy mirrors his broader approach: **start with observable evidence, form hypotheses, test systematically**. No magic, no superstition — just methodical investigation.

### The Long Game: 20+ Years of Blogging

Stapelberg has been running a blog since 2005 — over 20 years of documented technical thinking. This long-form consistency is itself a philosophy: **writing things down forces clarity, creates a searchable knowledge base, and contributes to the commons**. His blog covers everything from bootloader debugging stories to trip reports to NixOS migration guides, always with a practical, experience-grounded perspective.

## Key Quotes

> *"I don't feel like they're automatically making existing tasks faster. But rather, they make entirely new workflows possible that simply didn't exist before."* — on coding agents

> *"NixOS has a reputation of being hard to adopt, but once you are using NixOS, you can do powerful things like spinning up ephemeral MicroVMs for a new project within minutes."*

> *"I run a blog since 2005, spreading knowledge and experience for over 20 years!"*

> The principle behind "Stamp It!": if you can't determine what version of a program is running, you can't debug it, can't reproduce it, and can't trust it.

## Related

- [[concepts/nixos]] — Declarative, reproducible Linux distribution
- [[concepts/coding-agents]] — AI-assisted development workflows
- [[concepts/i3-wm]] — Tiling window manager created by Stapelberg
- [[concepts/wayland]] — X11 successor, now mature enough for Stapelberg's adoption
- [[simon-tatham]] — Another long-running free-software author and blogger
- [[xeiaso-net]] — Shared interest in Nix/NixOS and practical infrastructure

## Sources

- [Coding Agent VMs on NixOS with microvm.nix](https://michael.stapelberg.ch/posts/2026-02-01-coding-agent-microvm-nix/) (Feb 2026)
- [Can I finally start using Wayland in 2026?](https://michael.stapelberg.ch/posts/2026-01-wayland/) (Jan 2026)
- [Stamp It! All Programs Must Report Their Version](https://michael.stapelberg.ch/posts/2026-01-stamp-it/) (Jan 2026)
- [NixCon 2025 Trip Report](https://michael.stapelberg.ch/posts/2025-09-nixcon-trip-report/) (Sep 2025)
- [Secret Management on NixOS with sops-nix](https://michael.stapelberg.ch/posts/2025-08-secret-management/) (Aug 2025)
- [Development shells with Nix: four quick examples](https://michael.stapelberg.ch/posts/2025-07-dev-shells/) (Jul 2025)
- [Migrating my NAS from CoreOS/Flatcar Linux to NixOS](https://michael.stapelberg.ch/posts/2025-07-nas-migration/) (Jul 2025)
- [How I like to install NixOS (declaratively)](https://michael.stapelberg.ch/posts/2025-06-nixos-install/) (Jun 2025)
- [Tips to debug hanging Go programs](https://michael.stapelberg.ch/posts/debug-hanging-go/)
- [Bye Intel, hi AMD! I'm done after 2 dead Intels](https://michael.stapelberg.ch/posts/2025-05-bye-intel/)
- [Ryzen 7 Mini-PC makes a power-efficient VM host](https://michael.stapelberg.ch/posts/2024-07-mini-pc/) (Jul 2024)
- [Minimal Linux Bootloader debugging story](https://michael.stapelberg.ch/posts/2024-02-bootloader-debug/) (Feb 2024)
- [michael.stapelberg.ch/posts/](https://michael.stapelberg.ch/posts/) — Full blog archive
