---
title: "Jeff Geerling"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---


# Jeff Geerling

**URL:** https://www.jeffgeerling.com
**Blog:** jeffgeerling.com
**Twitter/X:** @JeffGeerling
**GitHub:** geerlingguy
**YouTube:** Jeff Geerling
**Projects:** Ansible for DevOps (book), Drupal VM, Pi Dramble, Project Mini Rack, Frigate NVR

## Overview

Jeff Geerling is a prolific open-source developer, author, YouTuber, and hardware tinkerer. He is best known as the creator of **Ansible for DevOps** (the best-selling Ansible book with 87K+ copies sold and $300K+ in revenue across 41 revisions) and as a leading voice in the Raspberry Pi, homelab, and single-board computing communities.

His blog and YouTube channel span a remarkable range: from deep infrastructure automation with Ansible to hardware teardowns, from AI cluster benchmarking to FireWire camera digitization, from RISC-V experimentation to enterprise server restoration. What unifies his work is a consistent philosophy: **build it yourself, measure it properly, document it publicly, and never accept marketing claims at face value.**

Geerling maintains over 300 open-source projects on GitHub and has been one of the most visible critics of the AI hype cycle — particularly its impact on open-source sustainability, maintainer burnout, and the flood of low-quality AI-generated pull requests.

## Timeline

| Date | Event |
|------|-------|
| ~2009 | Began publishing technical blog covering Drupal, Linux, and automation |
| 2012 | Published *Ansible for DevOps* — became the definitive Ansible book |
| 2013 | Created Drupal VM — a Vagrant-based development environment for Drupal |
| 2015 | Built the "Pi Dramble" — a 6-node Raspberry Pi cluster for load-balanced web serving |
| 2016 | Presented "Highly Available Drupal on a Raspberry Pi Cluster" at phptek |
| 2018 | Presented "Make your Ansible playbooks flexible, maintainable, and scalable" at AnsibleFest |
| 2018 | Created the Pi Benchmarks project — standardized performance testing for SBCs |
| 2020 | Gave away 480 Raspberry Pis to the community during the pandemic shortage |
| 2021 | Documented the burden of open-source maintainer burnout publicly |
| 2022 | Automated his homelab with Ansible; presented at AnsibleFest |
| 2023 | Published "Corporate Open Source is Dead" — analysis of licensing rug-pulls by HashiCorp, Redis, and others |
| 2023 | Began extensive Raspberry Pi AI hardware testing (AI HAT, Hailo, Coral TPU) |
| 2024 | Published "The AI Emperor Has No Clothes" — critique of AI hype vs. reality |
| 2024 | Published "AI is destroying Open Source, and it's not even good yet" — on AI slop PRs and maintainer burnout |
| 2024 | Created Project Mini Rack — open-source compact homelab rack design |
| 2024 | Experimented with building Ollama for RISC-V Linux |
| 2025 | Built and benchmarked a $3,000 10-node Raspberry Pi AI cluster — and publicly concluded it was a bad investment |
| 2025 | Clustered four Framework Mainboards to test large LLM inference |
| 2025 | Documented his voice being stolen by AI cloning — and held the perpetrator accountable |
| 2026 | Tested Raspberry Pi's new AI HAT+ 2 with Hailo 10H — concluded it's "a solution in search of a problem" |
| 2026 | Built a portable MRU (Memory Recording Unit) for FireWire/i.Link/DV cameras using Raspberry Pi |
| 2026 | Restored an Apple Xserve G5 and diagnosed capacitor plague issues |

## Core Ideas

### Measure Everything, Trust Nothing

Geerling's entire technical methodology is built on empirical measurement. Whether he's testing Pi cluster performance, comparing NVMe boot speeds, or benchmarking AI inference on edge hardware, he follows the same pattern: build it, instrument it, measure it, publish the results. His Pi Benchmarks project became the de facto standard for SBC performance comparison precisely because he approached it with rigor rather than marketing.

> "iperf3 is outdated for 10G+; use nmtui/connmanctl for headless WiFi config."

This willingness to debunk popular tools and assumptions is characteristic. He doesn't accept conventional wisdom — he tests it.

### Homelab as a Philosophy, Not a Hobby

For Geerling, the homelab is not just a playground — it's a statement about autonomy, understanding, and self-reliance. His Project Mini Rack (a 10" open-source rack design for compact homelabs) embodies this: if commercial rack systems are overpriced and oversized, build your own. If enterprise servers are wasteful, downsize. If cloud computing is opaque, run it locally.

His approach to homelab infrastructure is comprehensive: TrueNAS on ARM, K3s Kubernetes, WireGuard VPNs, Prometheus + Grafana monitoring, Home Assistant for IoT, Frigate for NVR with AI object detection. Every component is chosen, tested, and documented.

### AI Is Destroying Open Source — And It's Not Even Good Yet

Geerling's 2025-2026 writing on AI is among the most influential critical voices in the developer community. In "AI is destroying Open Source, and it's not even good yet" (2025), he documented how AI-generated pull requests were degrading open-source quality:

> "Daniel Stenberg dropped bug bounties because AI slop resulted in actual useful vulnerability reports going from 15% of all submissions down to 5%. And that's not the worst of it—the authors of these bug reports seem to have a more entitled attitude."

His critique is not anti-technology; it's anti-hype. He sees the same patterns that preceded every tech bubble: overvaluation, reckless optimism, and a disconnect between marketing and reality.

> "The problem is the humans who review the code—who are responsible for the useful software that keeps our systems going—don't have infinite resources."

### The AI Emperor Has No Clothes

In "The AI Emperor Has No Clothes" (2024), Geerling argued that the AI bubble's scale could be estimated by the flood of job offers, review requests, and sponsorship deals he received daily — not by actual technological progress:

> "There is no way the trillions of dollars of valuation placed on AI companies can be backed by any amount of future profit."

He distinguishes between genuine machine learning applications (which have real value) and the AI hype train (which masks useless or overpriced products behind buzzwords).

### Corporate Open Source Is Dead

In his 2024 post "Corporate Open Source is Dead," Geerling analyzed how companies like HashiCorp, Redis, MongoDB, and Elasticsearch had all abandoned true open-source licensing in favor of "source-available" or proprietary licenses:

> "It was all in the name of 'open source'. As free money dries up and profits slow, companies slash headcount almost as fast as community trust."

His argument is that Contributor License Agreements (CLAs) are a deliberate strategy: "a strategy employed by commercial companies with one purpose only: to place a rug under the project, so that they can pull at the first sign of a bad quarter."

His proposed solution is simple: **fork it.** When Terraform was relicensed, the community forked it into OpenTofu under the Linux Foundation. This is the mechanism that keeps open source honest.

### Open-Source Sustainability and Maintainer Burnout

Geerling has been one of the most visible advocates for addressing open-source maintainer burnout. After publicly documenting his own struggles — "Crohn's Disease takes its toll" (2023), "The burden of an Open Source maintainer" — he became a leading voice on the human cost of free software:

> "Tireless volunteers are the lifeblood of community."

His 2020 Pi Giveaway (480 Raspberry Pis distributed to the community) was a concrete example of paying it forward — not just with code, but with hardware and time.

### Local-First Computing and Edge AI

Geerling is a leading advocate for local-first computing — running services on your own hardware, controlling your own data, and not depending on cloud providers. His work on running LLMs on Raspberry Pi hardware (Ollama on RISC-V, Qwen3 30B on a 16GB Pi 5) demonstrates that powerful AI inference doesn't require datacenter GPUs.

> "I can check off items and they go to the bottom of the list... It's honestly crazy how many small tasks you can do even with free local models... even on a Pi. Natural Language Programming was just a dream back when I started my career."

### Hardware as a First-Class Citizen

Unlike most software developers, Geerling treats hardware as equally important. He has built PCIe cards to test GPUs on Raspberry Pi, diagnosed capacitor plague in 2004-era Apple Xserve power supplies, converted hot dog plasma videos to sound with OpenCV, and built GPS-synchronized PTP wall clocks. His approach is that understanding the physical layer — the actual silicon, the actual electricity — makes you a better engineer.

### Ansible Philosophy: Idempotent, Composable, Transparent

Geerling's Ansible work embodies three principles:

1. **Idempotent configurations** — running the same playbook twice should produce the same result
2. **Composable roles** — each role does one thing well and can be combined with others
3. **Transparent automation** — you should always be able to see what the playbook is doing and why

His book *Ansible for DevOps* has been through 41 revisions over a decade, reflecting his commitment to keeping documentation current and accurate. The self-publishing model ($300K+ revenue from a single technical book) demonstrates that deep expertise and honest writing can be financially sustainable.

### The Honest Reviewer

Geerling's product reviews are distinguished by their willingness to deliver negative conclusions. The $3,000 Pi AI cluster? "This is not the cluster you're looking for." The Raspberry Pi AI HAT+ 2? "A solution in search of a problem, in all but the most niche of use cases." This honesty — even when it contradicts his own investments and efforts — is what makes his voice trusted.

## Key Quotes

> "AI is destroying Open Source, and it's not even good yet."

> "The problem is the humans who review the code—who are responsible for the useful software that keeps our systems going—don't have infinite resources."

> "There is no way the trillions of dollars of valuation placed on AI companies can be backed by any amount of future profit."

> "It was all in the name of 'open source'. As free money dries up and profits slow, companies slash headcount almost as fast as community trust."

> "Tireless volunteers are the lifeblood of community."

> "Contributor License Agreements are a strategy employed by commercial companies with one purpose only: to place a rug under the project."

> "Natural Language Programming was just a dream back when I started my career."

> "When a company rug pulls? Fork 'em. Literally!"

> "This is not the cluster you're looking for." — on his own $3,000 Pi AI cluster build

> "Open source culture relies on trust. Trust that companies you and I helped build will honor the social contract."

> "I wouldn't run my production apps—that actually make money or could cause harm if they break—on unreviewed AI code."

## Recent Themes (2024–2026)

- **AI skepticism**: Leading critical voice on the gap between AI marketing and reality
- **Open-source sustainability**: Documenting maintainer burnout and advocating for community-funded development
- **Licensing analysis**: Tracking the shift from open source to "source available" across major projects
- **Edge AI and local inference**: Testing LLMs on Raspberry Pi, RISC-V, and other constrained hardware
- **Homelab infrastructure**: Building compact, efficient, self-hosted systems as an alternative to cloud dependency
- **Hardware experimentation**: FireWire digitization, PTP clocks, PCIe testing, capacitor plague diagnosis
- **Honest benchmarking**: Publishing negative results alongside positive ones
- **Community giving**: The 480-Pi giveaway, free educational content, open-source project maintenance

## Related Concepts

- [[concepts/ansible]] — His primary automation tool and the subject of his best-selling book
- [[concepts/raspberry-pi]] — His main platform for hardware experimentation and community projects
- [[concepts/homelab]] — His philosophy of self-hosted, local-first computing infrastructure
- [[concepts/open-source-sustainability]] — His advocacy for addressing maintainer burnout
- [[concepts/ai-code-quality]] — His critique of AI-generated code and its impact on open-source ecosystems
- [[concepts/local-first-computing]] — Running services on your own hardware, not in the cloud
-  — His analysis of the death of corporate-sponsored open-source licensing
-  — Running AI inference on constrained hardware like Raspberry Pi and RISC-V-  — His open-source compact homelab rack design

## Influence Metrics

- *Ansible for DevOps*: 87K+ copies sold, $300K+ revenue, 41 revisions — the best-selling Ansible book
- Maintains 300+ open-source repositories on GitHub
- Pi Dramble (6-node Pi cluster): influential project in the homelab community
- Pi Benchmarks: de facto standard for SBC performance comparison
- YouTube channel: 500K+ subscribers, videos regularly reach 100K+ views
- "Corporate Open Source is Dead" (2024): widely cited in licensing discussions
- His voice cloning incident (2025) became a case study in AI ethics and identity theft
- Regular speaker at AnsibleFest, DrupalCon, and other open-source conferences

## References

- jeffgeerling.com--blog-2026-ai-is-destroying-open-source--90aa7e5c
- jeffgeerling.com--blog-2026-arm-mainboard-for-framework-laptop--b32c90f0
- jeffgeerling.com--blog-2026-best-laptop-apple-ever-made--d113437b
- jeffgeerling.com--blog-2026-build-your-own-dial-up-isp-with-a-raspberry-pi--fdb96af0
- jeffgeerling.com--blog-2026-dram-pricing-is-killing-the-hobbyist-sbc-market--e82f991f
- jeffgeerling.com--blog-2026-expert-beginners-and-lone-wolves-dominate-llm-era--c1ee61d4
- jeffgeerling.com--blog-2026-exploring-a-modern-smpte-2110-broadcast-truck-with--52dd8947
- jeffgeerling.com--blog-2026-firewire-on-a-raspberry-pi--da90e989
- jeffgeerling.com--blog-2026-frigate-with-hailo-for-object-detection-on-a-raspb--ee099022
- jeffgeerling.com--blog-2026-macbook-neo-replace-m4-air--e5b9e8af
- jeffgeerling.com--blog-2026-minidv-with-raspberry-pi-firewire-hat--32c47ee4
- jeffgeerling.com--blog-2026-new-10-gbe-usb-adapters-cooler-smaller-cheaper--72a709e7
- jeffgeerling.com--blog-2026-ode-to-the-aa-battery--c77c9394
- jeffgeerling.com--blog-2026-pint-sized-macintosh-pico-micro-mac--ceca8a06
- jeffgeerling.com--blog-2026-ptp-wall-clock-impractical-too-precise--d5aceaaa
- jeffgeerling.com--blog-2026-raspberry-pi-connect-may-control-windows-soon--86bbba72
- jeffgeerling.com--blog-2026-restoring-xserve-g5-apple-server--f1bd9922
- jeffgeerling.com--blog-2026-securely-erase-hard-drive-macos-tahoe--2ddd3957
- jeffgeerling.com--blog-2026-testing-reachy-mini-hugging-face-robot--af3666d1
- jeffgeerling.com--blog-2026-the-first-good-raspberry-pi-laptop--444c4638
- jeffgeerling.com--blog-2026-upgrading-my-open-source-pi-surveillance-server-fr--457a6774
