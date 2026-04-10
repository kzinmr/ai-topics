# Rakhim (Rakhim Davletkaliyev)

## Overview

**Rakhim Davletkaliyev** is a staff engineer at [[IQM Quantum Computers]], a programming educator, author, and philosophical tech writer. He blogs at [[rakhim.exotext.com]] (with a web log at blog.rakhim.org), where he writes about the intersection of programming, computing theory, and the human experience of building software.

Rakhim is notable for his willingness to **shut down projects** when they no longer serve their purpose — a philosophy that runs counter to the "growth at all costs" mentality of modern tech. He has built and abandoned podcasts, courses, YouTube channels, and apps, documenting each decision with candor. His writing style is contemplative and self-reflective, often questioning the fundamental assumptions of software development culture.

He is the author of **Quantum Computing For Software Engineers** and **Foundations of Clojure** (published on Leanpub), and has spoken at [[PyCon]] Tallinn, [[flatMap]] Oslo, and [[Clojure Days]] Amsterdam. His side-projects have included **Castlemacs** (minimalist Emacs for macOS), **Underblog** (extremely simple static blog generator in Go), and **Geostreaks** (iOS app for remote workers who forget to go outside).

---

## Timeline

| Period | Key Events |
|--------|-----------|
| 2015–2017 | Launches blog.rakhim.org; publishes early essays on types, concurrency, and functional programming |
| 2017 | Speaks at flatMap Oslo on genetic programming and API design; speaks at Clojure Days Amsterdam on decentralized evolutionary computation |
| 2018 | Publishes *Foundations of Clojure* (Leanpub); writes "For Google, you're neither the consumer nor the product. You're a data point" |
| 2019 | Publishes *Conscious Attention* (Leanpub); writes "User Is Dead" and "Be Wary of Self Described Benefits" |
| 2020 | Shuts down most projects (podcasts, courses, YouTube channels, apps); publishes "I'm shutting down most of my projects" manifesto |
| 2020 | Publishes influential essay "Programming vs. Coding vs. Software Engineering" |
| 2020 | Writes "Bring back the ease of 80s and 90s personal computing" — critique of modern OS complexity |
| 2021–2023 | Shifts focus to quantum computing research; begins preparing for PyCon talk |
| 2024 | Speaks at PyCon Tallinn on "Full-stack Quantum Computing" — debunks myths about quantum advantage |
| 2024–2025 | Publishes *Quantum Computing For Software Engineers* (Leanpub); joins [[IQM Quantum Computers]] as staff engineer |
| 2025–2026 | Continues writing on exotext.com; reflects on programming philosophy and the human experience of computing |

---

## Core Ideas

### Programming vs. Coding vs. Software Engineering

Rakhim's most influential conceptual contribution is his **tripartite distinction** between programming, coding, and software engineering — a framework that clarifies why many developers experience burnout while others don't.

**Programming** is solving explicit problems in a verifiable manner, similar to mathematical proofs. It deals with algorithms, essential complexity, and clean logical structures. A binary search algorithm is programming: find an element in a sorted sequence. The problem is well-defined, the solution is provable, the outcome is satisfying.

**Coding** is expressing a programming solution in a formal language. It is "both easier and harder than programming" — easier because the problem is already solved, harder because it introduces accidental complexity (language quirks, framework constraints, toolchain issues).

**Software Engineering** is building a product for the real world. It includes programming and coding, plus scalability, durability, compliance, management, communication, infrastructure, deployment, backups, relationships, politics, and finance.

Rakhim's insight is captured in his "**Bang, Marry, Kill**" framework:

> "For many software developers, this is true:
> 1. Tolerate software engineering.
> 2. Enjoy coding.
> 3. Love programming.
> 
> Since real-world tech jobs blend all three, many of us return even after burnout. We love programming. Burnout tends to come from engineering, sometimes coding, but rarely from pure programming."

This distinction helps developers diagnose the source of their frustration. When Rakhim asks "Which of the three do I enjoy most?" he reveals a profound truth: **different activities require different temperaments**, and recognizing which one drives you is key to sustainable career satisfaction.

### The Wrong Good Solution

In his 2020 essay "The wrong good solution," Rakhim explores a critical pattern in software development: **choosing a technically excellent solution to the wrong problem**. This is a recurring theme in his writing — the idea that elegance in the wrong direction is worse than pragmatism in the right one.

His critique of modern software development is particularly sharp:

> "The 21st century has burdened the human psyche with a wonderful array of problems—most of which are invisible, abstract things. It's taken some time figuring out how to make them real. Doesn't feel like anybody created a tool to help with this."

The implication is that our tools have proliferated while our wisdom about *what* to build has stagnated. We have better frameworks, more libraries, faster build tools — but no framework for asking "should this exist?"

### The Power of Shutting Down

In September 2020, Rakhim published **"I'm shutting down most of my projects"** — a manifesto that is rare in tech culture. He closed podcasts, courses, YouTube channels, and apps, stating clearly: "All existing static content (text, audio, video) will remain available for as long as possible. Any running code will halt by the end of September."

This is not burnout — it is **intentional curation**. Rakhim recognized that maintaining dozens of projects was diluting his ability to produce quality work. By shutting down the periphery, he focused on what mattered: deep thinking, writing, and building things he cared about.

His approach to project management is anti-growth in the best sense: **if a project no longer serves a purpose, kill it**. This stands in stark contrast to the tech industry's default mode of accumulation — more features, more platforms, more metrics.

### The Human Experience of Computing

Rakhim's writing consistently returns to the **human side of computing**. His essay on mood and energy (December 2020) treats developer psychology with the same seriousness he applies to algorithm design:

> "Mood and energy are like weather. Use the good weather to sail. Don't expect it to last. Find what to do while it's raining."

This meteorological metaphor is characteristic of Rakhim's approach: he finds natural, intuitive frameworks for describing technical phenomena. Developer productivity isn't a constant — it's a system with cycles, and the wise engineer works *with* those cycles rather than against them.

His observation about modern tools is equally perceptive:

> "I've discovered small tips here and there. I'm making progress. I'm learning how to work with myself. But if I'm honest, I still don't have a system."

Rakhim is transparent about his own incompleteness. He doesn't claim to have solved the productivity puzzle — he documents the process of trying, failing, adjusting, and trying again. This is a form of technical writing that is rare in an industry obsessed with "best practices" and "productivity hacks."

### The Linux Fragmentation Problem

In "Bring back the ease of 80s and 90s personal computing" (November 2020), Rakhim articulates one of the most fundamental problems in the Linux ecosystem:

> "Nobody wants to ship binaries for Linux, because there is no Linux platform, there's hundreds of distros, further fragmented by package managers, library versions, and init systems."

> "Windows and Mac are stable or at least predictable platforms. Linux is a constant moving target."

> "A true platform is something that allows authors to run their stuff on top, not something authors need to apply to."

His critique is not anti-Linux — he says "I don't love Linux. But hell, I see no future anywhere except it." His point is that Linux has become so fragmented that it fails the most basic test of a platform: **reliability for the software author**. If you can't ship a binary and trust it will run, you don't have a platform — you have a philosophy.

Rakhim's proposed solution (QuickPYTHON — a QBasic-like environment for Python) reflects his desire for **simplicity and immediacy** in computing. He wants tools that "just work," not tools that require hours of configuration before they can do anything useful.

### The Google Data Point Thesis

In 2018, Rakhim wrote one of his most prescient essays:

> "For Google, you're neither the consumer nor the product. You're a data point."

This reframing is subtle but powerful. The common tech critique is "you are the product" — meaning your attention is sold to advertisers. Rakhim's version is more precise: you are a **data point** in a statistical model. Your individual identity doesn't matter; your aggregate behavior does. This is a colder, more accurate description of how Big Tech actually operates.

The essay demonstrates Rakhim's ability to identify the **structural reality** beneath the surface narrative. While others debate whether tech companies are good or evil, Rakhim asks: "What system produces these outcomes?" The answer is not malice — it's statistics.

### Quantum Computing Demystification

Rakhim's PyCon 2024 talk, "Full-stack Quantum Computing," reflects his broader philosophy of **demystifying the complex**. Rather than hyping quantum computing as a revolutionary force, he debunks common myths and explains what quantum computers can and cannot do.

> "Quantum computing is real, but it's surrounded by a thick fog of hype. Do you want to see it clearly, understand its [capabilities and limitations]?"

This approach — cutting through marketing to reach technical truth — is consistent across all of Rakhim's writing. Whether he's analyzing genetic programming APIs, Lisp concurrency models, or quantum computing fundamentals, his method is the same: **understand the underlying mechanism, then explain it honestly**.

### The Price of Complexity

In his 2019 essay "The price of complexity," Rakhim explores how software systems accumulate unnecessary complexity over time. The essay argues that complexity is not just a technical problem — it's a **cognitive burden** that affects developers' ability to think clearly and make good decisions.

His related essay "Be Wary of Self Described Benefits" warns against accepting vendors' claims about their own tools. This is a form of intellectual hygiene: don't believe the marketing, don't accept the defaults, question the premises.

### The Learning Process as Subject

Rakhim's essay "Process of Learning" (2019) is notable for its **meta-cognitive** approach. Rather than just sharing what he learned, he documents *how* he learned — the false starts, the dead ends, the moments of insight. This is programming education as autobiography: the learner's journey is the content.

His bookshelf entries reveal his intellectual influences: [[SICP]] (Structure and Interpretation of Computer Programs), [[How to Design Programs]], [[Clojure for the Brave and True]], Sean Carroll's physics books, and Victor Papanek's design theory. He reads widely across programming, physics, psychology, and philosophy — and integrates these perspectives into his technical writing.

### Standardization is Impossible

Rakhim's web log contains a single, powerful statement:

> "Standardization is impossible."

This is not defeatism — it is realism. The attempt to force complex systems into standardized forms inevitably fails because **complexity resists compression**. Every standard creates new exceptions, every framework introduces new constraints, every protocol generates new edge cases.

Rakhim's embrace of this impossibility is liberating. If standardization is impossible, then the goal is not to achieve it — it's to **navigate the chaos gracefully**. This philosophy underlies his approach to tool selection, project management, and career development.

---

## Key Quotes

> "For many software developers, this is true: 1. Tolerate software engineering. 2. Enjoy coding. 3. Love programming."

> "Burnout tends to come from engineering, sometimes coding, but rarely from pure programming."

> "Programming is solving explicit problems in a verifiable manner. It is similar to mathematical proofs."

> "The 21st century has burdened the human psyche with a wonderful array of problems—most of which are invisible, abstract things. It's taken some time figuring out how to make them real. Doesn't feel like anybody created a tool to help with this."

> "For Google, you're neither the consumer nor the product. You're a data point."

> "Mood and energy are like weather. Use the good weather to sail. Don't expect it to last."

> "A true platform is something that allows authors to run their stuff on top, not something authors need to apply to."

> "Standardization is impossible."

---

## Recent Themes (2024–2026)

**2024:** Spoke at PyCon Tallinn on "Full-stack Quantum Computing" — debunking myths about quantum advantage. Published *Quantum Computing For Software Engineers* (Leanpub). Continued staff engineering work at IQM Quantum Computers.

**2025–2026:** Continued writing on exotext.com. Maintained quantum computing research at IQM. Reflected on the relationship between programming philosophy and human cognition. Sustained his anti-accumulation approach to projects — focused on quality over quantity.

---

## Related

[[IQM Quantum Computers]] — Rakhim's employer; Finnish quantum computing company
[[Clojure]] — Functional programming language; Rakhim published *Foundations of Clojure*
[[Emacs]] — Rakhim built Castlemacs (minimalist Emacs for macOS)
Genetic Programming — Rakhim's flatMap 2019 talk topic
[[Lisp]] — Language family central to Rakhim's evolutionary computing research
[[Go (Golang)]] — Language used for Underblog static site generator
[[Python]] — Primary language for quantum computing work and PyCon talks
[[Rust]] — Emerging systems language; Rakhim has written about it
Chaos Theory — Subject of Rakhim's Codexpanse Podcast exploration
[[flatMap Conference]] — Oslo conference where Rakhim spoke on genetic programming
[[Clojure Days]] — Amsterdam conference where Rakhim spoke on decentralized evolutionary computation

---

## Sources

- [rakhim.exotext.com](https://rakhim.exotext.com) — Primary blog and writing archive
- [blog.rakhim.org](https://blog.rakhim.org) — Web log with shorter-form posts
- [rakhim.org](https://rakhim.org) — Personal homepage and project list
- *Programming vs. Coding vs. Software Engineering* (exotext.com)
- *I'm shutting down most of my projects* (September 2020)
- *The wrong good solution* (2020)
- *For Google, you're neither the consumer nor the product. You're a data point* (2018)
- *Bring back the ease of 80s and 90s personal computing* (November 2020)
- *Full-stack Quantum Computing* (PyCon Tallinn, 2024)
- *Genetic programming is waiting for better tools* (flatMap Oslo, 2019)
- *Decentralized evolutionary computation* (Clojure Days Amsterdam, 2019)
- *Quantum Computing For Software Engineers* (Leanpub)
- *Foundations of Clojure* (Leanpub)
- *Conscious Attention* (Leanpub)
- GitHub: [@freetonik](https://github.com/freetonik) — Open source projects
