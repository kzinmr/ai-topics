---
title: Hugo Tunius
created: 2026-04-09
updated: 2026-04-10
tags:
  - person
  - blogger
  - hn-popular
  - devops
  - kubernetes
  - rust
  - web-development
---


# Hugo Tunius

| | |
|---|---|
| **Blog** | [hugotunius.se](https://hugotunius.se) |
| **RSS** | https://hugotunius.se/feed.xml |
| **Role** | DevOps engineer, software developer |
| **Known for** | Technical writing on Rust, Kubernetes, web architecture, the "Great Pendulum" theory of tech trends, edge-cached static sites |
| **Bio** | DevOps engineer and software developer with a focus on systems programming and web infrastructure. Prolific blogger covering Rust (especially async Rust), Kubernetes, web architecture patterns, and the cyclical nature of technology trends. Known for his economical site architecture — running his blog for approximately $0.01/month using S3, Jekyll, and Cloudflare. |

## Core Ideas

Hugo Tunius is a **pattern-recognizing systems thinker** — someone who observes the cyclical nature of technology trends, builds infrastructure that is simple and cost-effective, and writes clearly about complex topics like async Rust and distributed systems.

### The Great Pendulum

Tunius's signature conceptual framework is **"The Great Pendulum"** — the observation that technology trends oscillate between extremes, with the correct answer usually lying somewhere near equilibrium:

> *"In most instances the correct position lies somewhere near the equilibrium point, but we tend to overshoot it in each swing."*

He identifies several active pendulums:
- **Static typing vs Dynamic typing** — Currently swinging back toward static
- **Monoliths vs Microservices** — Monoliths are "making a comeback"
- **Cloud vs On-prem** — "On-prem is having a bit of a moment"
- **Statically compiled vs Interpreted languages** — Compilation is "cool again"
- **Server-side rendering vs Client-side rendering** — HTMX and Hotwired signal a swing back toward SSR

His hope: *"Maybe, like a real pendulum, the amplitude of these pendulums will decrease over time and they will come to rest at the equilibrium."* The framework is essentially an application of the Hegelian dialectic to technology trends — thesis, antithesis, synthesis — though Tunius is careful to note that synthesis isn't guaranteed.

### Async Rust: The Hard Parts

In ["On Async Rust"](https://hugotunius.se/2024/03/08/on-async-rust.html), Tunius provides a clear-eyed analysis of Rust's async ecosystem:

> *"Computers are fast actually... the C10k (and more) problem is trivially solvable with just OS threads."*

His key arguments:
- **Default to OS threads** unless your workload specifically requires N:M scheduling
- **Zero-cost abstractions** in Rust mean runtime performance, not compile-time overhead or dependency bloat
- **The Arc/Mutex trap** is a shared-state concurrency problem, not async-specific — but async makes it worse
- **The sans-IO pattern** (protocol logic separated from IO execution) is the solution to Rust's "crate coloring" problem
- **Tokio monoculture** is a real concern — the ecosystem is effectively locked to one executor

His architectural recommendation: separate protocol logic (blue, IO-agnostic `*-proto` crates) from execution (colored `*-tokio`, `*-async-std` wrappers). This mirrors his broader preference for **separation of concerns** across all systems.

### Source of Truth Should Be in Git

In ["Stop Using (only) GitHub Releases"](https://hugotunius.se/2024/01/20/stop-using-github-releases.html), Tunius argues that **project metadata should live in the repository, not in external systems**:

> *"Always try to make the source of truth files in git, rather than data in the databases of external systems."*

The problems with GitHub-only releases:
- Pagination makes searching and cross-referencing impossible
- Release notes aren't part of the repository — if GitHub falls out of favor, history is lost
- Reading release notes on github.com while code is in your editor is a context-switching nightmare

This principle generalizes: don't put documentation in external ticketing systems, don't put changelogs only in forge UI, don't separate the narrative of a project from its code.

### The One-Cent Blog: Frugal Architecture

Tunius has operated his blog for approximately **$0.01/month** using a stack of S3, Jekyll, Cloudflare, and CI/CD automation. This isn't just about cost — it's a philosophy: **infrastructure should be proportionate to its actual needs**. A personal blog doesn't need a database, a server, or a framework with runtime overhead. Static files on a CDN are the right architecture for static content.

### Sideloading and Platform Control

In ["What Every Argument About Sideloading Gets Wrong"](https://hugotunius.se/2025/08/31/what-every-argument-about-sideloading-gets-wrong.html), Tunius reframes the sideloading debate:

> *"When Google restricts your ability to install certain applications they aren't constraining what you can do with the hardware you own, they are constraining what you can do using the software they provide with said hardware."*

His argument: the real issue isn't sideloading restrictions on provided OSes — it's that **you can't run alternative OSes on the hardware**. The productive critique should focus on hardware vendors' refusal to provide documentation and support for alternative operating systems, not on the software restrictions within the default OS.

### Force Push as a Workflow Tool

In an early essay, ["You Should Force Push More"](https://hugotunius.se/2014/09/08/you-should-force-push-more.html), Tunius argues against the conventional wisdom that force push is dangerous:

> *"Force push is an extremely powerful ally when utilised correctly. It helps a team keep the git log clean from surplus and misleading commits."*

His policy: force push freely on feature branches to clean up history before merging; never force push to stable branches. This requires a good branching model and a team culture that treats commits as mutable until they reach a stable branch.

## Key Quotes

> *"In most instances the correct position lies somewhere near the equilibrium point, but we tend to overshoot it in each swing."*

> *"Computers are fast actually... the C10k (and more) problem is trivially solvable with just OS threads."*

> *"Always try to make the source of truth files in git, rather than data in the databases of external systems."*

> *"When Google restricts your ability to install certain applications they aren't constraining what you can do with the hardware you own, they are constraining what you can do using the software they provide with said hardware."*

## Related

- [[great-pendulum]] — Cyclical nature of technology trends
- [[async-rust]] — Tokio, sans-IO pattern, crate coloring
- [[source-of-truth]] — Git as the canonical location for project metadata
- [[frugal-infrastructure]] — Running services at minimal cost
- [[xeiaso-net]] — Shared interest in practical, small-scale infrastructure
- [[michael-stapelberg]] — Shared interest in declarative infrastructure and Nix

## Sources

- [The Great Pendulum](https://hugotunius.se/2023/07/09/the-great-pendulum.html) (Jul 2023)
- [On Async Rust](https://hugotunius.se/2024/03/08/on-async-rust.html) (Mar 2024)
- [Stop Using (only) GitHub Releases](https://hugotunius.se/2024/01/20/stop-using-github-releases.html) (Jan 2024)
- [What Every Argument About Sideloading Gets Wrong](https://hugotunius.se/2025/08/31/what-every-argument-about-sideloading-gets-wrong.html) (Aug 2025)
- [Claude, Teach Me Something](https://hugotunius.se/2025/10/25/claude-teach-me-something.html) (Oct 2025)
- [The One Cent Blog](https://hugotunius.se/2016/01/10/the-one-cent-blog.html) (Jan 2016)
- [You Should Force Push More](https://hugotunius.se/2014/09/08/you-should-force-push-more.html) (Sep 2014)
- [Why Svelte is Like Rust](https://hugotunius.se) — on reactive programming patterns
