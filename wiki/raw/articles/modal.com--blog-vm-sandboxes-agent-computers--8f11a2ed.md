---
title: "VM Sandboxes: Full computers for agents"
url: "https://modal.com/blog/vm-sandboxes-agent-computers"
fetched_at: 2026-10-02T10:01:07.071555+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# VM Sandboxes: Full computers for agents

Source: https://modal.com/blog/vm-sandboxes-agent-computers

Today we’re making VM Sandboxes generally available on Modal, built for those who need to give their agents the power of a full computer.
With one flag, you’ll get a fully capable Linux VM with all the niceties that you expect from a traditional
modal.Sandbox
, and it Just Works™. This brings the same APIs,
modal.Image
s, sub-second cold-starts, and CPU/memory bursting capabilities as previously, all whilst supporting the
hundreds of thousands of concurrent Sandboxes
that our users are accustomed to.
Why now?
Modal was originally built to achieve the
holy grail of Serverless GPUs
, with our gVisor-based runtime giving us the ability to quickly scale up lightweight GPU containers, and providing us what we need to create superpowers like
fast GPU snapshotting
.
Our Sandbox product was also built on gVisor, which has served us well. But earlier this year, we watched as
Ramp built an internal agent to drive
the entire software development lifecycle on Modal Sandboxes and it became obvious where agents were headed.
Agents, at work or under evaluation, increasingly want to live inside something that looks like a real machine: running Docker stacks, local databases and dev servers, graphical environments and mobile simulators, and even monkeying around with the Linux Kernel itself. In short,
agents just want a computer
.
At the same time, the ergonomics offered by our container-shaped runtime, such as the exec/FS APIs or the
burstable resource model
, are core to the Modal experience. When we set off to bring VM Sandboxes to life, we knew we had to support this breadth of use cases out of the box.
We’ve done a lot of deep engineering work to carry forward the same APIs that support our gVisor Sandboxes, including building out a custom runtime. Starting from the Rust-based
Cloud Hypervisor
project, we layered on a half dozen innovations spanning our host filesystems, lazy image loading, memory bursting, and snapshotting tech. We’re excited to share deep dives into work we’ve done to make all this possible in the coming weeks.
With VM Sandboxes now available in GA, anyone can now give their agents Sandboxes with local databases or Docker stacks, ready to build complex production systems.
VM Sandboxes in the wild
Over the last couple of months, we've put VM Sandboxes in the hands of early customers, who have already launched over 20 million VMs! Here's what they built.
Linear: coding agents working in your real dev environment
Linear's
Coding Sessions
let you hand an issue to an agent without ever leaving Linear. Behind the scenes, Linear spins up the user’s full dev environment inside a Modal VM Sandbox.
Having a full-fledged Linux machine gave the Linear team finer control over resource partitioning and networking within each Session, using cgroups and network namespaces to keep the coding agent, the user's dev server, and Linear's own host process from competing for resources. Today, every Linear Coding Session runs on a VM Sandbox.
“Docker in our sandboxes has been groundbreaking for our customers because they can spin up their full live dev environment on top of our infrastructure, without anything complicated like bringing their own base image. Switching over took a single flag, and everything just worked.”
Ryan Delaney
Software Engineer, Linear
Legora: Long-horizon legal agent evaluations
Legora
builds legal agents that work for hours at a time across legal projects with thousands of documents. They use VM Sandboxes to power their
evals
, building the full Legora app in each Sandbox, including Postgres, a DOCX editor, and the agent's own code sandboxes.
“Our app runs as a set of Docker services. Previously, that meant we had to introduce networking and FUSE workarounds at every layer to get full Docker functionality in the sandbox, from host-mode networking with our own DNS resolution to running code sandboxes as bare processes because FUSE wouldn't mount. With VM Sandboxes, it's been frictionless: Docker behaves like it does on a normal Linux host, and we deleted every one of those workarounds.”
Eirik Drage Steen
Member of Technical Staff, Legora
Snorkel: mocking the real world
Snorkel
, a frontier AI data lab, develops and validates complex datasets for training and evaluating frontier AI systems on realistic tasks. They run millions of agent simulations a month with
Harbor
, testing agents on scenarios like zero-downtime database migrations, hot-swapping services under load, and debugging applications backed by multiple services.
“For agent simulations to be meaningful, the environment needs to represent the real world the agent will operate in. Many software engineering tasks require multiple containers: to debug a PostgreSQL database-backed application, for example, the agent might run in one container while the application and database run in others. Modal's VM Sandboxes give us exactly that: a full machine for every simulation, where these setups run just like they would in the real world.”
Rustem Feyzkhanov
Sr. Engineering Manager — AI Platform, Snorkel
So, should I switch everything over?
Short answer: it depends! If your workload runs happily on Modal Sandboxes today, it'll continue running happily on gVisor, which currently remains as our default runtime.
Reach for
runtime="vm"
when you butt against the walls of userspace: Docker, FUSE filesystems, or niche Linux kernel features. We’ve made switching as simple as flipping a flag, with both runtimes sharing the same APIs, Images, and usage-based pricing.
What's next?
VM Sandboxes today are intentionally container-shaped, which allows us to offer them as a drop-in runtime, fully compatible with your existing code. Looking forward, we're excited to build out new primitives that take advantage of the expanded capability set and programming model that VMs offer. At the same time, we're working on making VMs even more elastic and lightweight.
Agents just want a computer. Starting today,
VM Sandboxes are generally available
on Modal, ready to support the next trillion Sandboxes.
