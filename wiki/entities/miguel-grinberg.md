# Miguel Grinberg

## Overview

**Miguel Grinberg** is a Python educator, open-source maintainer, and software engineer best known for his influential tutorials, deep technical blog posts, and long-running contributions to the Python web ecosystem. He is the author of the **Flask Mega-Tutorial** (the definitive Flask learning resource, spanning over a decade), creator of **Microdot** (an ultra-lightweight web framework for microcontrollers), and maintainer of **Flask-HTTPAuth**, **Flask-Migrate**, **Flask-SocketIO**, and **Flask-Moment**.

Grinberg writes from a deeply pragmatic, hands-on perspective — he builds tools, measures them, publishes data, and is unafraid to critique trends in the industry regardless of their popularity. His blog at blog.miguelgrinberg.com is one of the most respected independent technical blogs in the Python community, known for rigorous empirical analysis and a refusal to participate in hype cycles.

---

## Timeline

| Period | Key Events |
|--------|-----------|
| 2012 | Launches blog.miguelgrinberg.com; begins publishing Flask tutorials |
| ~2014 | Publishes first version of the **Flask Mega-Tutorial** |
| 2017–2020 | Publishes *Python Flask Mega-Tutorial* as a book; becomes the canonical Flask learning resource |
| 2019–present | Maintains Flask-HTTPAuth, Flask-Migrate, Flask-SocketIO, Flask-Moment |
| 2022 | Creates **Microdot** — a minimal web framework for microcontrollers |
| 2023 | Begins publishing annual "Year in Review" analyses of the Flask ecosystem |
| 2024 | Flask Mega-Tutorial updated; Microdot gains traction in IoT/embedded community |
| 2025 | Publishes "Why Generative AI Coding Tools and Agents Do Not Work For Me" — influential critique of AI-assisted development; creates React+Flask project tutorial; publishes MicroPython benchmarking; switches Flask/Werkzeug CI to `uv` package manager |
| 2026 | Publishes annual Flask 2025 review (noting Flask/FastAPI near-parity); writes "LLM Use in the Python Source Code" critiquing AI commits to CPython; launches learn.miguelgrinberg.com course platform; publishes self-hosted email server guide, tokenless CSRF protection, and interactive maps tutorial |

---

## Core Ideas

### The Code Review Bottleneck

Grinberg's most influential argument against AI coding tools centers on a simple observation: **code review is the bottleneck, not code writing**. In his June 2025 post *"Why Generative AI Coding Tools and Agents Do Not Work For Me"*, he challenges the entire premise of AI productivity claims:

> "It takes me at least the same amount of time to review code not written by me than it would take me to write the code myself, if not more."

His argument is not anti-AI in a philosophical sense — it is deeply practical. As a maintainer of multiple open-source libraries, a course creator, and a contract developer, Grinberg is legally and professionally responsible for every line of code that ships under his name. AI cannot assume that liability. Therefore, skipping review to "save time" is not productivity — it is risk transfer.

He extends this critique to open-source maintenance, noting the "uncanny valley" effect of AI-generated pull requests: submissions that look plausible but are often low-effort, with submitters who disengage when asked to address review comments. The result is not faster development — it is a bottleneck shifted to maintainers.

### The "AI Intern with Anterograde Amnesia"

Perhaps Grinberg's most memorable metaphor for AI coding tools:

> "An AI tool can only resemble an intern with anterograde amnesia, which would be a bad kind of intern to have. For every new task this 'AI intern' resets back to square one without having learned a thing!"

This captures his core frustration: unlike human collaborators who accumulate institutional knowledge, refine their judgment, and develop shared context over time, AI tools provide no compounding benefit. Each interaction starts from zero. For a maintainer building systems over years, this is fundamentally misaligned with how software actually gets built and maintained.

### Learning as Professional Practice

Grinberg is a prolific learner — his blog documents his journeys into **Rust**, **Go**, **TypeScript**, **WASM**, **Java**, and **C#**. He views the process of learning new languages and frameworks as a core professional value, not a cost to be minimized:

> "Mastering unfamiliar tech is an intentional, rewarding process. Delegating learning to AI defeats skill development and doesn't actually save time due to mandatory review overhead."

This perspective shapes his entire approach to technology. He is not someone who resists new tools — he is someone who believes that **the process of understanding a tool deeply is itself the value**, and that shortcutting this process produces brittle, poorly-understood systems.

### Empirical Analysis Over Hype

Grinberg's annual Flask "Year in Review" posts are notable for their data-driven methodology. He queries PyPI download statistics using BigQuery, tracks pull request merge rates, monitors extension maintenance status, and compares framework adoption across surveys. His 2025 review, published January 2026, explicitly states:

> "Zero AI Generation: Author explicitly confirms no LLMs/generative AI were used to compile data, eliminating hallucination risk."

His analysis revealed that **Flask and FastAPI are now essentially tied** in PyPI downloads (46% vs. 45% market share), while FastAPI has pulled ahead in developer preference surveys (38% vs. 34%). He also documented a concerning trend: Flask's PR closure rate jumped from ~30% to 72% in 2025, partly due to a flood of low-quality AI-generated submissions.

Grinberg's approach is distinctive because he **publishes his SQL queries** alongside his analysis, allowing anyone to reproduce or challenge his findings. This is the scientific method applied to software ecosystem monitoring.

### Pragmatic Independence

Grinberg's 2026 decision to migrate his course platform from Teachable to a self-hosted solution (learn.miguelgrinberg.com) reflects a broader philosophy: **avoid vendor lock-in, even when it's painful**. When Teachable raised prices fourfold while the platform stagnated, and with AI-generated course content depressing demand, Grinberg didn't complain — he built his own platform using his own tools.

Similarly, his self-hosted email server guide (March 2026) explicitly rejects third-party email APIs:

> "Because the prospect of adding yet another dependency on Big Tech is depressing, I decided to go against the general advice and roll my own email server."

This is the same independence that drives his Microdot framework — a web server so small it runs on microcontrollers, built because existing options were too heavy for his use case.

### Semantic Rigor and Accessibility

Grinberg's recent work on **tokenless CSRF protection** (December 2025) and **interactive maps with zero API dependencies** (January 2026) demonstrates his commitment to making common web development tasks simpler and more accessible. His approach consistently strips away unnecessary complexity:

- Tokenless CSRF: Replaces anti-CSRF tokens, double-submit cookies, and hidden form fields with a simpler modern approach
- Zero-API maps: Embeds interactive maps with "only a few lines of HTML/JS. No accounts, API keys, or paid services needed"

This philosophy — **make the simple things simple** — is the defining characteristic of his teaching style and tool development.

---

## Key Quotes

> "It takes me at least the same amount of time to review code not written by me than it would take me to write the code myself, if not more."

> "An AI tool can only resemble an intern with anterograde amnesia, which would be a bad kind of intern to have."

> "I believe people who claim that it makes them faster or more productive are making a conscious decision to relax their quality standards to achieve those gains."

> "Because the prospect of adding yet another dependency on Big Tech is depressing, I decided to go against the general advice and roll my own email server."

> "I feel allowing developers to use LLMs or coding assistants in their contributions to CPython robs people in the Python community from the opportunity of making such contributions themselves, and learning from the experience."

> "Zero AI Generation: Author explicitly confirms no LLMs/generative AI were used to compile data, eliminating hallucination risk."

---

## Recent Themes (2024–2026)

**2024:** Continued development of Flask Mega-Tutorial and Microdot framework. Published React+Flask integration guide. Maintained multiple Flask extensions.

**2025:** Published influential critique of AI coding tools ("Why Generative AI Coding Tools and Agents Do Not Work For Me"). Released MicroPython benchmarking data. Published annual Flask ecosystem review. Created tokenless CSRF protection implementation for Microdot. Built interactive maps tutorial requiring zero API keys or services. Updated course platform to learn.miguelgrinberg.com.

**2026:** Published annual Flask 2025 review documenting Flask/FastAPI market parity and AI-generated PR flooding. Wrote critical analysis of LLM commits to CPython source code. Self-hosted email server guide rejecting Big Tech dependencies. Date arithmetic in Bash tutorial. Migration of paid courses from Teachable to independent platform.

---

## Related

[[Flask]] — Python web framework; Grinberg is one of its most prominent educators
[[FastAPI]] — Rising Python web framework; now roughly equal to Flask in downloads
[[Microdot]] — Ultra-lightweight web framework for microcontrollers, created by Grinberg
[[CPython]] — Python implementation; Grinberg has critiqued AI commits to its codebase
Django — Traditional Python web framework; Grinberg's reviews include it in comparisons
uv — Package manager Grinberg adopted for Flask/Werkzeug CI/CD
Werkzeug — WSGI toolkit underlying Flask; Grinberg monitors its development
Quart — Async Flask alternative; Grinberg documents its near-dormant status
pallets-eco — Volunteer group maintaining Flask ecosystem extensions
[[Rust]] — Language Grinberg has been learning; subject of his "AGENTS.md" exploration
TypeScript — Language Grinberg has adopted for full-stack projects
Go — Language Grinberg has explored for systems programming

---

## Sources

- [blog.miguelgrinberg.com](https://blog.miguelgrinberg.com) — Primary blog and technical resource
- *LLM Use in the Python Source Code* (February 2026)
- *Why Generative AI Coding Tools and Agents Do Not Work For Me* (June 2025)
- *A Year In Review: Flask in 2025* (January 2026)
- *My Courses Site is Moving to a New Home* (February 2026)
- *Self-Hosted Email Server* (March 2026)
- *Tokenless CSRF Protection* (December 2025)
- *Interactive Maps (Zero-API)* (January 2026)
- *Date Arithmetic in Bash* (February 2026)
- *Benchmarking MicroPython* (July 2025)
- *Create a React + Flask Project in 2025* (May 2025)
- [Microdot GitHub](https://github.com/miguelgrinberg/microdot)
- [Flask-HTTPAuth](https://github.com/miguelgrinberg/flask-httpauth)
- [Flask-SocketIO](https://github.com/miguelgrinberg/flask-socketio)
- [learn.miguelgrinberg.com](https://learn.miguelgrinberg.com) — Course platform
- GitHub: [@miguelgrinberg](https://github.com/miguelgrinberg)
