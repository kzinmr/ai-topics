---
title: Giles Thomas
created: 2026-04-09
updated: 2026-04-10
tags:
- blogger
- hn-popular
- ai
- llm-training
- python
- systems
- startup
aliases:
- gpjt
- gilesthomas.com
---

# Giles Thomas

| | |
|---|---|
| **Blog** | [gilesthomas.com](https://gilesthomas.com) |
| **RSS** | https://gilesthomas.com/feed/rss.xml |
| **LLMs.txt** | [gilesthomas.com/llms.txt](https://gilesthomas.com/llms.txt) |
| **About** | [https://gilesthomas.com/about](https://gilesthomas.com/about) |
| **Hugging Face** | [huggingface.co/gpjt](https://huggingface.co/gpjt) |
| **Role** | Founder of PythonAnywhere (sold to Anaconda 2022); currently AI researcher & blogger |
| **Location** | Lisbon, Portugal (originally UK) |
| **Bio** | Software engineer and entrepreneur with nearly 20 years of public blogging. Founded PythonAnywhere, a PaaS for Python developers. Sold to Anaconda in 2022. Now doing deep, hands-on LLM research — training GPT-style models from scratch on consumer and cloud hardware. |

## Core Ideas

### Learning in Public, For Real

Giles is the embodiment of **learning in public**. His blog archive spans 2006–2026 and documents a genuine intellectual journey — from early web gadgets and NSLU2 hackery to modern LLM training. He doesn't post polished thought-leadership; he posts *working notes*, failed experiments, and half-formed ideas that mature over dozens of iterations.

His LLM-from-scratch series runs to **32+ installments** (and counting), each one a real research log where he tests interventions, measures results, and publishes the noise. This is the antithesis of AI hype: slow, methodical, reproducible.

> *"Your first blog post will probably be bad. That's ok. Your second one will be better, and your third will be even better. All that matters is that you wrote something and put it out into the world."*

### Writing an LLM from Scratch

This is Giles' magnum opus — a complete from-scratch implementation and training of a GPT-2-style model, based on Sebastian Raschka's book "Build a Large Language Model (from Scratch)." Key dimensions:

**Architecture deep-dives:**
- Self-attention, causal masking, multi-head attention, layer normalization
- Feed-forward networks, residual/shortcut connections
- Embedding dimensions (discovered that only the 124M GPT-2 model has 768 dimensions — larger models use more)

**Systematic intervention testing (Parts 32a–32j):**
- Gradient clipping — reduces training instability
- Removing dropout — counterintuitively can improve results
- Adding attention bias — measurable impact on convergence
- Learning rate scheduling — critical for final loss
- Weight decay — derived optimal values from Cerebras Research papers
- Weight tying — connects input/output embeddings
- Full-fat float32 — the noise floor question

**Scaling methodology:**
- Started on a single RTX 3090 (consumer hardware)
- Moved to 8× A100 (40 GiB/GPU) and 8× B200 (160 GiB/GPU) on Lambda Labs
- Used DistributedDataParallel for multi-GPU training
- Published **7 trained models** on Hugging Face under Apache v2

**The noise problem:** Giles discovered that variations in initial weight initialization matter far more than randomness in the training loop itself — a genuinely useful insight for anyone training models.

### AI Safety & Debugging Philosophy

**On AI-first debugging:**
> *"On the perils of AI-first debugging — or, why Stack Overflow still matters in 2025"*

Giles warns that using AI to skip the cognitive friction of debugging erodes the very skills that make you effective. His approach: use AI as a collaborator, not a replacement for understanding.

**On prompt injection:**
> *"Why smart instruction-following makes prompt injection easier"*

A paradoxical insight: as models get better at following instructions, they become more vulnerable to manipulation. Better capability ≠ better safety.

### Infrastructure & Systems Engineering (Pre-AI Era)

Before diving into LLMs, Giles had a two-decade career in **systems and infrastructure**:

- **PythonAnywhere**: Built and operated a PaaS for Python developers. Handled Django unit testing, HTTP/WebSocket reverse proxying with nginx, SNI-based Go reverse proxies, SSL certificate automation via Let's Encrypt, and the migration from Fabric3 to Fabric.
- **Custom C reverse proxy/load balancer**: Built from scratch using epoll and non-blocking I/O, with Lua configuration.
- **pam-unshare**: A PAM module for switching into PID namespaces — the kind of low-level Linux work most people never touch.
- **Resolver One**: An early spreadsheet application built on IronPython, with OpenCL/.NET integration and 3D graphics (OpenGL/Tao).
- **NSLU2 Offsite Backup**: A 13-part automated backup system from 2006.

## Key Technical Excerpts

| Area | Detail |
|------|--------|
| **LLM Training** | Systematic intervention testing on GPT-2 architecture from scratch |
| **Cloud Scaling** | 8× A100, 8× B200, DistributedDataParallel, Lambda Labs automation |
| **Evaluation** | LLM-as-a-judge, Hugging Face AutoModel/pipeline/Trainer integration |
| **Systems** | C reverse proxy with epoll, pam-unshare, SNI-based Go proxying |
| **Security** | Prompt injection analysis, AI-first debugging critique |

## Blog Themes

- **AI/ML**: LLM training, fine-tuning, evaluation, safety
- **Systems Programming**: C, epoll, Linux internals, PAM modules
- **Python Ecosystem**: PaaS architecture, Django, IronPython
- **Startup/Founder**: Bootstrapping, acquisition, post-exit reflection
- **Web Philosophy**: Long-form blogging, learning in public, RSS advocacy

## Related

- [[concepts/llm-from-scratch]] — Giles' methodology for training models from scratch
- [[concepts/harness-engineering]] — Related work on AI safety and debugging
- [[entities/pythonanywhere]] — Giles' PaaS company
- [[concepts/learning-in-public]] — Giles' approach to technical writing

## Sources

- [Writing an LLM from scratch series](https://gilesthomas.com/categories/llm-from-scratch/) (2024–2026)
- [On the perils of AI-first debugging](https://gilesthomas.com) (2025)
- [Why smart instruction-following makes prompt injection easier](https://gilesthomas.com)
- [gilesthomas.com/about](https://gilesthomas.com/about)
- [Hugging Face models (gpjt)](https://huggingface.co/gpjt)
- [Automating Lambda Labs instances](https://gilesthomas.com) (2026)
