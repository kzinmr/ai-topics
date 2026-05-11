---
url: https://wesmckinney.com/blog/agent-ergonomics/
title: "From Human Ergonomics to Agent Ergonomics"
author: Wes McKinney
date: 2026-01-20
source: wesmckinney.com
tags: [agentic-engineering, software-engineering, data-science]
---

I have been building a lot of new software in Go. Except that I've never actually written a line of Go in my life. **What is going on?**

Anyone following my LinkedIn or Twitter/X feed has seen that I have been down a coding agent rabbit hole in recent months. This has included:

- moneyflow, a TUI accounting system (written in Python)
- roborev, a continuous background code review system (written in Go). roborev has totally transformed my productivity, by the way.
- VibePulse, a mediocre version of CodexBar (written in Swift)
- agent-session-viewer, a session history viewer and search tool for your coding agent sessions (written in Python)

I have multiple other in-progress projects I've been creating on nights and weekends that I either plan to open source in the future or retain just for me. I'm working harder and having more fun building than I have in years.

## Python and Agents

Python remains a remarkably effective language. It's concise, readable, and has one of the strongest ecosystems of libraries of all time.

But agentic engineering is different:

- Fast compile-test cycles matter more than code simplicity and readability. Agents compile-and-test one-to-two orders of magnitude more often than their human counterparts, so any extra friction here is punishing.
- Painless software distribution feels essential. You may create numerous tools to enable your "agentic loop" and self-contained, dependency-free binaries accessible in a coding agent context feel like the right modality.
- Human ergonomics matters less when humans aren't the primary authors.

In this context, Python has weaknesses: its test cycles are relatively slow and distribution has challenges (though uv helps). Dragging around a Python interpreter has started to feel like the Java Virtual Machine from which we tried so desperately to unburden ourselves.

The reasons that Python has gotten so popular (and why I went down the Python rabbit hole back in 2007 and dedicated many years of my life to popularizing Python for data analysis) are that it is productive and pleasant for humans to write and use. As the hours and days pass by, this benefit feels increasingly moot compared with the evident downsides (performance, memory use, distribution, etc.), especially with an agent doing all the coding for you.

**Put another way, human ergonomics in programming languages matters much less now.** The readability and simplicity benefits of Python help LLMs generate code, too, but viewed through the "annealing" lens of the iterative agentic loop, quicker iterations translate to net improved productivity even factoring in the "overhead" of generating code in a more verbose or more syntactically complex language.

## Frictionless Development and Shipping

The winners of this shift to agentic engineering are the languages that have solved the build system, runtime performance, packaging, and distribution problems. Increasingly that looks like Go and Rust:

- Painlessly build static binaries with zero runtime dependencies
- Predictable dependency management and code sharing
- Fast, deterministic builds
- Lean resource footprint, no just-in-time compilation, good runtime performance

From my experience, Go even has a substantial edge over Rust due to its ultrafast compile times for release builds (while Rust release builds can take minutes of linking and optimization). Rust has memory safety without garbage collection and deterministic resource management, while Go trades some of that control for faster compilation and a simpler concurrency model. Some projects may choose one or the other purely based on these characteristics (with Rust's slower compile-test loops as an acceptable tradeoff).

For now, LLMs have strong Python programming skills because of the massive amounts of training data mined from GitHub and the broader internet, and so it may be that average code quality is better in Python now than it is in Go or Rust, but perhaps after multiple agentic iterations and automated code reviews, it may be good enough.

To be clear, I am not trying to say that Go and Rust are not very ergonomic for humans. These are already popular languages that we all use for critical applications, such as Docker, Kubernetes, Terraform, Deno, or uv. What's interesting is that agents have made these languages much more accessible beyond their prior core user base of heavy duty systems engineering. Go is a great language to program in for systems work, microservices, and distributed computing, but in general there is more of a learning curve to working in it and in the past building a Go project as a rule of thumb would take longer than building the same project in Python.

## What about Data Science and AI?

Python isn't going anywhere as long as its moat as a language for data work and ML/AI inference and training persists. The ecosystem of NumPy, pandas, PyTorch, and all the other popular projects represents decades of accumulated expertise, institutional knowledge, and muscle memory. While some projects may be reimagined in systems languages intended primarily for agents, the ecosystem inertia (and abundant training data) will continue for a long time.

What has changed is where the durable value actually lives. It is increasingly useful to separate the stack into a few layers:

1. The computing, IO, and compiler kernel libraries based on CUDA, compiler frameworks like MLIR or JAX's XLA, and of course Apache Arrow.
2. The database systems and caching layers, ideally connected with ADBC's zero-serialization connectivity.
3. The language bindings and orchestration layers that expose those capabilities.
4. The application or agent interfaces that sit on top.

When viewed this way, most of the long term value clearly resides in the first two layers (compute and data access), not the last two.

## Code review: more machine than man

An obvious downside in shifting away from Python is that I have much less experience reading and judging the quality of Go code or Rust code. This is part of why I built roborev, not just because agents' commits are full of bugs and imperfections, but also because I'm definitely less effective manually reviewing languages I never used pre-AI.

## Not the End for Python, but the End of an Era

Python will remain essential as an exploratory computing layer for humans and agents to collaborate on data analysis, research, and data visualization. Notebook layers (Jupyter, Marimo, and so forth) and hybrid IDEs (like Positron, where I've been contributing in the last couple of years) will increasingly focus on catering to the human-in-the-loop data scientist or ML engineer, even though the "Python part" may become thinner and thinner as the lower layers of the stack are re-engineered for performance and agentic engineering productivity.

Regardless, I'm proud of what we have accomplished in building the Python ecosystem and how it has democratized data science and ML/AI work. I still love the language, but it seems clear that I and much of the industry will be writing less and less of it given the agentic-loop productivity benefits of Go and other modern compiled languages. Where the road leads from here we will soon see.

Thanks to Josh Bloom, Ian Cook, Pete Jarvis, and John Zila for their helpful feedback on this post.
