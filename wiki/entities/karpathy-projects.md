---
title: "Karpathy Projects & Open Source"
tags: [person, projects]
created: 2026-04-27
updated: 2026-04-27
type: entity
---


# Karpathy: Projects & Open Source

Back to main profile: [[andrej-karpathy]]

## Eureka Labs (2024–present)

- **AI-native education company** founded July 16, 2024
- Vision: "Teacher + AI symbiosis" — human experts design courses, AI teaching assistants scale personalized guidance
- First product: **LLM101n** — undergraduate-level course to build an LLM chat interface from scratch in Python, C, and CUDA, with minimal CS prerequisites
- Goal: make high-quality education accessible to everyone, anywhere
- Karpathy's statement: *"Eureka Labs is the culmination of my passion in both AI and education over ~2 decades"*

## microgpt (2026)

- **200 lines of pure Python** with zero dependencies that trains and inferences a GPT
- Contains: dataset, tokenizer, autograd engine, GPT-2-like architecture, Adam optimizer, training loop, inference loop
- Culmination of micrograd → makemore → nanoGPT → microgpt progression
- 4,192 parameters total — demonstrates that the full algorithmic content of an LLM fits in a tiny script
- *"I cannot simplify this any further"* — Karpathy's statement on the script's minimalism
- **Key insights from the project:**
  - **Attention is token communication:** QKV projections where tokens "talk to" each other
  - **MLP is where thinking happens:** 2-layer FFN (expand 4× → ReLU → contract) does the actual computation
  - **RMSNorm > LayerNorm:** Simpler normalization without bias terms, equally effective
  - **Residual connections enable depth:** `output = input + sublayer(LayerNorm(input))` prevents vanishing gradients
  - **Next-token prediction is surprisingly powerful:** Loss drops from 3.3 (random) to 2.37 (pattern learning) in 1K iterations
  - **Autograd from scratch:** Chain rule applied systematically — algorithmically identical to PyTorch's `.backward()`
  - **Temperature controls creativity:** Low temp = conservative, high temp = diverse sampling
- **Training data:** 32K names (character-level), vocabulary size 27 (26 letters + BOS token)
- **Architecture:** Stateless function `gpt(token_id, pos_id, keys, values) → logits → softmax → next_token`

## autoresearch (2026)

- AI agents running research experiments autonomously overnight on single-GPU nanochat setups
- Structure: `prepare.py` (locked), `train.py` (agent-edited), `program.md` (human instructions)
- Mechanism: **Ratchet loop** — 5-min wall-clock training → eval `val_bpb` → git commit if improved
- Demonstrates practical use of AI agents for scientific discovery
- Part of Karpathy's broader "agentic engineering" workflow philosophy

## Dobby the Elf Claw (2026)

- Local, secure smart-home AI agent running on NVIDIA DGX Station GB300
- Interfacing via WhatsApp, autonomously reverse-engineering device APIs
- Named after Dobby from Harry Potter — a free elf that helps without being asked
- Exemplifies Karpathy's vision of AI agents operating autonomously in the physical world

## NanoGPT (2022)

- Minimal, educational PyTorch GPT implementation (~47.9k GitHub stars)
- Widely used as a teaching tool and starting point for LLM experimentation
- Simpler, more readable alternative to Hugging Face Transformers for learning

## llm.c (2024)

- Raw C/CUDA implementation of GPT-2 training and inference
- Demonstrates that LLM training can be done in a single, understandable file
- No PyTorch dependency — everything from scratch in C and CUDA
- Part of Karpathy's commitment to demystifying LLM internals

## nanochat (Oct 2025)

- Full-stack ChatGPT alternative deployable for **<$100 cloud cost**
- Combines nanoGPT training with a minimal web interface
- Designed for self-hosted, local LLM deployment
- Shows the complete pipeline from data → training → inference → deployment

## makemore (2022)

- Character-level language model that generates names
- Educational project showing how to build neural networks from scratch
- Demonstrates autoregressive generation at a conceptual level

## micrograd (2019)

- Tiny scalar-valued autograd engine in Python
- Builds a neural network on top for binary classification
- One of Karpathy's most popular educational projects — teaches backpropagation from scratch
- Used as the foundation for thousands of deep learning tutorials

## CS231n (2015-2017)

- Stanford course: Convolutional Neural Networks for Visual Recognition
- Grew from 150 to 750 students — one of Stanford's most popular classes
- Course notes, videos, and assignments remain widely used
- Established Karpathy as a world-class educator

## ConvNetJS (2015)

- One of the first browser-based deep learning libraries
- Allowed training neural networks directly in JavaScript
- Pioneering demo of accessible, visual deep learning education

## Tesla Autopilot (2017-2022)

- Director → Senior Director of AI at Tesla, led the Autopilot vision team
- Championed **Tesla Vision** — camera-only autonomy approach (no lidar)
- Removed radar from Model 3/Y (May 2021) and Model S/X (Feb 2022)
- Implemented closed-loop **data engine**: deploy → collect edge cases → auto-label → retrain → redeploy
- Scaled training on billions of fleet miles using PyTorch (adopted 2020)
- Scaled team from ~30 to ~200+ engineers during his tenure
- Left July 13, 2022, citing slow convergence to unsupervised autonomy despite exponential compute scaling

## OpenAI (2015-2017, 2023-2024)

- Co-founding member (2015) — founding research scientist
- **Tenure 1 (2015-2017):** Advanced computer vision, generative modeling, RL. Built **OpenAI Universe** (2016) and **World of Bits** (2017) — platforms for training RL agents on web-based environments
- Contributed to GPT architecture development during first stint
- **Tenure 2 (2023-2024):** Returned to build team on midtraining and synthetic data generation
- Departed voluntarily on Feb 13, 2024 to pursue independent projects (Eureka Labs)
