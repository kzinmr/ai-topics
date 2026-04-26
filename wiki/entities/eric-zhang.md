---
title: Eric Zhang
type: entity
created: 2025-11-17 16:10:46
updated: 2026-04-10 10:00:00
aliases: [ekzhang, Eric Zhang]
status: active
description: "Systems hacker and designer. Creator of bore, sshx, rustpad, and Percival. Former founding engineer at Modal, now at Thinking Machines Lab."
tags: [person]
sources: []
---


# Eric Zhang

**X/Twitter:** [@ekzhang1](https://x.com/ekzhang1)
**Website:** [ekzhang.com](https://www.ekzhang.com/)
**Blog:** [notes.ekzhang.com](https://notes.ekzhang.com/)
**GitHub:** [github.com/ekzhang](https://github.com/ekzhang)
**Resume:** [ekzhang.com/resume](https://www.ekzhang.com/resume)
**Role:** Member of Technical Staff, Thinking Machines Lab; formerly Principal Engineer at Modal
**Location:** New York, NY / Cambridge, MA

## Overview

Eric Zhang (known online as **ekzhang**) is a systems programmer, researcher, and designer who builds tools at the intersection of **distributed systems, programming languages, and interactive software**. He is currently a Member of Technical Staff at **Thinking Machines Lab**, working on multimodal AI systems. Previously, he was a founding engineer and Principal Engineer at **Modal**, where he wrote the serverless container runtime in Rust and helped scale the platform from 50 CPUs / 2 GPUs to over 200,000 CPUs / 9,000 GPUs across multiple clouds.

Zhang's open-source projects are characterized by **extreme polish, practical utility, and educational clarity**. His most popular projects include:

- **bore** (11k+ GitHub stars): A simple CLI tool for making tunnels to localhost in ~400 lines of Rust
- **sshx** (7.4k+ GitHub stars): Fast, collaborative live terminal sharing over the web — "like multiplayer Google Docs but for your terminal"
- **rustpad** (4k+ GitHub stars): Efficient, minimal collaborative code editor, self-hosted, no database required
- **percival** (634+ GitHub stars): Web-based, reactive Datalog notebooks for data analysis and visualization
- **graphics-workshop** (2.2k+ GitHub stars): Self-guided projects for learning computer graphics by writing GPU shaders

He holds an AB in Computer Science and Mathematics and an SM in Computer Science from **Harvard University**, graduating *magna cum laude* with highest honors in his field. Before Modal, he worked at Convex (first hired engineer), Jump Trading (quantitative research), Scale AI (ML infrastructure), and Nvidia (applied deep learning research).

Zhang's personal philosophy, articulated in his "Statement of Purpose," is to **"make better interactive software to empower individuals"** — not just in informatics work, but in creativity, education, and community. He views building software in the open as "a mode of creative exploration" and believes that "computers occupy an integral place in all parts of our daily lives."

## Timeline

| Date | Event |
|------|-------|
| 2017 | Texas All-State Symphony Orchestra: Principal Violist |
| 2019 | Enrolled at Harvard University (AB in Computer Science and Mathematics) |
| Dec 2017 - Apr 2020 | Ranked 7th globally at IOI (International Olympiad in Informatics) |
| Jun 2020 - Aug 2020 | Architecture Intern at **Nvidia** — PVA / Applied Deep Learning Research |
| Dec 2019 - Jun 2020 | Undergraduate Researcher at **Harvard Medical School** |
| May 2020 - Aug 2020 | Research Assistant, Programming Languages Group at **Harvard SEAS** |
| Dec 2020 - Jan 2021 | Software Engineering Intern at **Scale AI** — ML infrastructure |
| Jun 2021 - Aug 2021 | Quantitative Research Intern at **Jump Trading** — US equities and decentralized exchanges |
| 2021 | Created **rustpad** — collaborative code editor (1M+ downloads) |
| 2021 | Created **graphics-workshop** — learn computer graphics by writing GPU shaders |
| Jun 2021 - Oct 2021 | Software Engineer at **Convex** — first hired engineer at seed-stage startup |
| 2021 - 2023 | SM in Computer Science at **Harvard University** |
| 2022 | Created **bore** — localhost tunneling CLI in Rust |
| Aug 2022 | Created **classes.wtf** — course catalog with extremely fast full-text search (HackMIT grand prize winner) |
| Nov 2022 | Created **Dispict** — creative aesthetics tool for discovering art museums using language-image ML models |
| Feb 2022 - Oct 2024 | Founding Engineer at **Modal** — wrote serverless container runtime in Rust |
| Sep 2021 | Created **µKanren-rs** — featherweight relational programming language in Rust |
| Nov 2024 - Oct 2025 | Principal Engineer at **Modal** — infra research lead, technical direction |
| Oct 2025 - Present | Member of Technical Staff at **Thinking Machines Lab** |
| 2025 | Created **sshx** — collaborative terminal sharing over the web (7.4k+ stars) |
| 2025 | Created **ssh-hypervisor** — "SimCity for VMs" — Firecracker microVMs provisioned on SSH connection |
| 2025 | Developed **Modal Notebooks** — modern cloud notebooks with real-time collaboration and GPUs |
| 2025 | Published "ssh-hypervisor: SimCity for VMs" — reflecting on building systems projects with AI tools |
| 2026 | Active development on opencode-tools ecosystem |

## Core Ideas

### Software as Creative Exploration

Zhang views open-source development as **"a mode of creative exploration"** — a way to quickly act on inspiration, delve into new topics, and make tools that improve people's lives. This philosophy manifests in his project choices: rather than building for market demand, he builds what interests him and what he believes will be useful.

> "I view building software in the open as a mode of creative exploration. It lets me quickly act on inspiration, delve into new topics, and make tools that improve people's lives."

His projects span programming languages (µKanren-rs), distributed systems (Modal runtime), computer graphics (graphics-workshop, rpt), creative tools (Dispict), and developer infrastructure (bore, sshx, rustpad). Each project is a learning vehicle as much as a product.

### Extreme Minimalism and Polish

Zhang's projects are characterized by **extreme attention to user experience and code quality**:

- **bore** achieves localhost tunneling in ~400 lines of Rust. The simplicity is deliberate — a single binary with no dependencies, easy to audit and deploy.
- **rustpad** is a collaborative code editor that requires no database — the entire state lives in memory, making it trivially deployable.
- **sshx** provides "multiplayer Google Docs for your terminal" with end-to-end encryption, predictive local echo (inspired by Mosh), and globally distributed relay nodes — all from a single command.

His philosophy: **the best tools are the ones that disappear**. They should work immediately, require no configuration, and get out of the user's way.

### Systems Thinking from First Principles

Zhang's Harvard education in both mathematics and computer science gives him a **first-principles approach** to systems design. At Modal, he:

- Wrote the container runtime from scratch in Rust
- Built a content-addressed file system for container images with tiered caching over petabytes of data
- Designed a serverless HTTP stack with distributed TLS relays
- Implemented container sandboxing via gVisor and eBPF network infrastructure
- Created a WireGuard-based VPN for secure inter-container communication

Each of these systems was built from the ground up rather than assembled from existing components. This reflects his belief that **understanding the fundamentals is essential to building reliable systems**.

### Interactive Software as Empowerment

Zhang's "Statement of Purpose" articulates a vision of software that **empowers individuals** across all domains — not just professional developers:

> "My most fundamental belief is that computers occupy an integral place in all parts of our daily lives: not just in informatics work, but also in creativity, education, community, and the people who rely on it."

This belief manifests in projects like:
- **Dispict**: Using language-image ML models to help people discover and engage with art
- **Percival**: Web-based Datalog notebooks that make logic programming accessible for data analysis
- **Composing Studio**: Collaborative music composition tools
- **classes.wtf**: Making Harvard's course catalog searchable and browsable

### AI-Assisted Systems Programming

In "ssh-hypervisor: SimCity for VMs" (2025), Zhang documented his experience building a hypervisor hooked up to SSH — where users get a fresh Firecracker microVM on each connection — using AI tools. His reflection is nuanced:

> "While AI tools made coding a lot faster (thousands of lines in minutes), they don't replace the need for systems understanding."

He found that AI accelerated the mechanical work of writing code but didn't eliminate the need for architectural thinking, debugging skills, or understanding the underlying systems. The hypervisor project would have taken 1-2 weeks in the past; with AI, he completed it in a weekend — but the design decisions, debugging, and systems thinking were still entirely his.

### The Weekend Project Ethos

Zhang values **small, complete projects** that can be built and shared quickly. His "What's Eric Working On?" page lists current projects, "small bites" (shorter-term experiments), and "indefinitely postponed" ideas — reflecting a creative process that moves fluidly between sustained focus and playful exploration.

> "Back in high school and college, I used to make a lot of smaller, fun projects over the weekend and share them with people. I don't do this as much now with a job... I think that's sad though."

The ssh-hypervisor project was his attempt to recapture this ethos — building something fun and useful in a weekend, sharing it publicly, and letting the creative side take over.

## Key Quotes

> "I view building software in the open as a mode of creative exploration. It lets me quickly act on inspiration, delve into new topics, and make tools that improve people's lives."

> "My most fundamental belief is that computers occupy an integral place in all parts of our daily lives: not just in informatics work, but also in creativity, education, community, and the people who rely on it."

> "While AI tools made coding a lot faster (thousands of lines in minutes), they don't replace the need for systems understanding."

> "Back in high school and college, I used to make a lot of smaller, fun projects over the weekend and share them with people. I don't do this as much now with a job. I think that's sad though."

> "I aim to make better interactive software to empower individuals."

## Key Projects

### bore (11k+ GitHub stars)
A simple CLI tool for making tunnels to localhost. Written in Rust, ~400 lines, no dependencies. Solves the common problem of exposing local services to the internet without complex configuration.

### sshx (7.4k+ GitHub stars)
Fast, collaborative live terminal sharing over the web. End-to-end encrypted (Argon2 + AES), globally distributed mesh via Fly.io, predictive local echo inspired by Mosh. One command generates a shareable URL.

### rustpad (4k+ GitHub stars)
Efficient, minimal collaborative code editor. Self-hosted, no database required. 1M+ downloads. Built as a practical alternative to cloud-based editors that require accounts and subscriptions.

### graphics-workshop (2.2k+ GitHub stars)
Self-guided projects for learning computer graphics by writing GPU shaders. Runs in real time on modern GPUs without extra software. Used by thousands of self-learners after gaining popularity in /r/gamedev.

### percival (634+ GitHub stars)
Web-based, reactive Datalog notebooks for data analysis and visualization. Makes logic programming accessible for interactive data exploration.

### classes.wtf
Harvard course catalog with extremely fast full-text search. Built at HackMIT 2021 (grand prize winner). Uses DuckDB for extremely fast queries.

### ssh-hypervisor
"SimCity for VMs" — a Go-based SSH server that dynamically provisions Firecracker microVMs. Users SSH in and get a fresh or restored VM instance. Built in a weekend using AI tools.

### Dispict
Creative aesthetics tool for discovering art museums using language-image ML models. Helps users curate personalized museum experiences from Harvard Art Museums' 200,000+ digitized works.

### µKanren-rs
Featherweight relational programming language in Rust. Implementation of µKanren for a graduate programming languages design seminar at Harvard.

### rpt
Photorealistic path tracer for rendering 3D scenes. Won top project out of 100 students in MIT's computer graphics class (6.837, Fall 2020).

### Modal Infrastructure
- Serverless container runtime in Rust (original author and architect)
- Content-addressed file system for container images with tiered caching
- Serverless HTTP stack with distributed TLS relays
- Container sandboxing via gVisor and eBPF network infrastructure
- WireGuard-based VPN
- Modal Notebooks with real-time collaboration and GPUs

## Related Wikilinks

- [[concepts/multimodal]] — Serverless compute platform he helped build
- [[concepts/thinking-machines-lab]] — His current employer
- [[concepts/rust-programming]] — His primary systems language
- [[concepts/firecracker]] — Lightweight hypervisor used in ssh-hypervisor
- [[concepts/datalog]] — Logic programming language used in Percival
-  — Domain of graphics-workshop and rpt
-  — rustpad, sshx, Percival
-  — His alma mater

## Sources

- [Eric Zhang Website](https://www.ekzhang.com/)
- [Eric Zhang Resume](https://www.ekzhang.com/resume)
- [Eric Zhang Projects](https://www.ekzhang.com/projects)
- [What's Eric Working On?](https://notes.ekzhang.com/software/status)
- [GitHub: @ekzhang](https://github.com/ekzhang)
- [X/Twitter: @ekzhang1](https://x.com/ekzhang1)
- [sshx Blog Post](https://www.blog.brightcoding.dev/2025/09/13/sshx-a-secure-web-based-collaborative-terminal-for-effortless-session-sharing/)
- [ssh-hypervisor Blog Post](https://ss.ekzhang.com/p/ssh-hypervisor-simcity-for-vms)
- [LinkedIn: Eric Zhang](https://linkedin.com/in/ekzhang)
- [Read.cv: Eric Zhang](https://read.cv/ekzhang)
- [The Org: Eric Zhang at Thinking Machines Lab](https://theorg.com/org/thinking-machines-lab/org-chart/eric-zhang)
