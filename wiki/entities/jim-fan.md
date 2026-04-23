---
title: Jim Fan
handle: "@jim-fan"
created: 2026-04-10
updated: 2026-04-10
related:
  - [[entities/nvidia-dgx-spark.md]]
  - [[embodied-ai]]
  - [[robotics]]
  - [[genie]]
  - [[project-gr00t]]
  - [[isaac-sim]]
tags:
  - person
  - ai
  - robotics
  - embodied-ai
  - nvidia
  - simulation
  - world-models
---


# Jim Fan (@jim-fan)

| | |
|---|---|
| **X** | [@jim-fan](https://x.com/jim-fan) |
| **Blog** | [jimfan.me](https://jimfan.me) |
| **GitHub** | [jiajun-wu](https://github.com/jiajun-wu) |
| **LinkedIn** | [drjimfan](https://www.linkedin.com/in/drjimfan/) |
| **Role** | Director of AI & Distinguished Scientist at NVIDIA |
| **Known for** | Co-Lead of Project GR00T (Humanoid Robotics), GEAR Lab, Voyager, Genie world simulator, Physical Turing Test |
| **Bio** | AI researcher at NVIDIA leading embodied AI and humanoid robotics research. Co-lead of Project GR00T, a foundational model initiative for humanoid robots. Stanford PhD, OpenAI's first intern. Pioneer in the "Physical AI" paradigm combining simulation, reinforcement learning, and world models for robotics. |

## Overview

Jim Fan is a leading AI researcher at NVIDIA, where he serves as Director of AI and Distinguished Scientist. He co-leads **Project GR00T**, NVIDIA's foundational model initiative for humanoid robots, and leads the **GEAR Lab** (General Embodied AI Research Lab), established with support from NVIDIA CEO Jensen Huang. His research focuses on embodied AI — creating AI agents that can perceive, reason about, and act in the physical world.

Fan's vision extends beyond traditional language models to what he calls **Physical AI** — the idea that true intelligence requires grounding in physical reality. He has articulated this through the concept of the **"Physical Turing Test"**: the point at which a robot's actions become indistinguishable from a human's in performing everyday tasks like cleaning an apartment or preparing dinner. "Throughout human history, 5,000 years, we have much better tools, much better society in general," Fan noted at AI Ascent 2025. "But the way we make dinner and do a lot of hand labor are still more or less the same from the Egyptian times."

Before joining NVIDIA, Fan earned his PhD from Stanford University and was OpenAI's first intern, working on early research in visual reasoning and embodied agents. His academic work spans computer vision, robotics, and reinforcement learning, with publications on topics ranging from 3D scene understanding to autonomous navigation.

## Core Ideas

### The Physical Turing Test
At AI Ascent 2025, Fan proposed a new benchmark for AI progress: the Physical Turing Test. While the traditional Turing Test (can a machine converse indistinguishably from a human?) has been largely "conquered" by LLMs, the Physical Turing Test asks: can you tell if a physical task was done by a human or a machine?

> "I would like to propose something very simple called the Physical Turing Test. The idea is like this: you come home, and you see a clean house and a candle-lit dinner. You can't tell if it was done by a human or a machine."

Fan demonstrated the gap with humorous robot fails, showing current robots still struggle with basic tasks like avoiding obstacles (famously tripping over a dog and banana peel). His roadmap aims to close this gap through simulation and foundational models.

### Simulation as "Nuclear Energy" for Robotics
Fan describes simulation as the "nuclear energy" alternative to the "fossil fuel" of direct physical data collection. His framework progresses through stages:

- **Simulation 1.0 (Digital Twin)**: Classical physics engines running at 10,000x real-time with domain randomization to bridge the sim-to-real gap
- **Simulation 1.5 (Digital Cousin)**: Hybrid systems using generative models to create environments combined with classical physics engines
- **Simulation 2.0 (Digital Nomad)**: Fully generative video diffusion models simulating complex interactions without manual environment creation

The results are dramatic: humanoid robots learning to walk in just **2 hours of simulation time**, equivalent to 10 years of real-world experience compressed into an afternoon.

### The Foundation Agent Vision
At GTC 2024, Fan outlined the "Foundation Agent" — a single model capable of operating across different bodies and environments. This requires three essential features:

1. **Survival and navigation** in open-ended worlds
2. **World understanding** — converting large-scale data into actionable insight
3. **Cross-embodiment generalization** — one model, different body forms

### Physical API — The Future of Robot-Human Interaction
Fan's ultimate vision is a "Physical API" where robots can manipulate atoms as easily as software manipulates bits today. This would enable:

- **Physical prompting** to instruct robots using natural language
- **A physical app store** for robot skills
- **Scale economies** for physical tasks (e.g., Michelin-star chefs providing dinner-as-a-service)

"These capabilities will eventually fade into the background as ambient intelligence," Fan predicts. "That day will simply be remembered as another Tuesday."

## Key Work

### Project GR00T (2024–present)
NVIDIA's foundational model for humanoid robots. Co-led by Fan, GR00T aims to create a general-purpose brain for humanoid robots that can understand natural language, perceive environments, and execute complex physical tasks.

- **Latest**: Isaac GR00T N1.6 reasoning model with physical world understanding, showcased at CoRL 2025
- **Integration**: Works with NVIDIA Cosmos for synthetic data generation and the Newton Physics Engine

### GEAR Lab (2023–present)
General Embodied AI Research Lab at NVIDIA, established with Jensen Huang's support. Research areas include:

- **Voyager**: An autonomous agent that learns skills in Minecraft through continuous exploration, scaling up to master complex tasks without human intervention
- **Metamorph**: A foundation model working across different body forms — "no matter what a robot looks like, it's all the same. It's all just sentences to the agent"
- **ISAAC-Sim**: High-fidelity simulation platform with Python API for training robot agents

### Genie World Simulator (2024–2025)
A groundbreaking world simulation system that generates interactive 3D environments from text prompts. Key capabilities:

- **Real-time interactivity**: Environments react to user movements and actions
- **World memory**: Environments stay consistent across sessions, carrying forward previous actions
- **Prompt-based events**: Users can trigger unexpected scenarios to test agent robustness
- **Applications**: Training robotic agents, disaster preparedness, emergency training, gaming

Fan describes Genie 3 as "a silhouette of game engine 2.0," suggesting that eventually "all the complexity of Unreal Engine will be absorbed by a data-driven blob of attention weights."

### NVIDIA Cosmos (2025)
Open-source, open-weight Video World Model trained on 20 million hours of video footage. To put this in perspective, Fan noted that 20M hours is "like watching YouTube 24/7 non-stop from the age of Roman Empire to today." Cosmos provides:

- **Two flavors**: Diffusion (continuous tokens) and autoregressive (discrete tokens)
- **Two modes**: Text→video and text+video→video generation
- **Application**: Large-scale synthetic data generation for robotics and autonomous driving

### MineDojo (2022)
An open framework for training generalist agents in Minecraft, combining a simulator, database, and model. Enables agents to discover new skills through exploration and learning.

### "The Second Pre-training Paradigm"
A blog article exploring how foundation models are evolving beyond language into physical reasoning and embodied intelligence.

### AI Ascent 2025 Talk
"The Physical Turing Test: Jim Fan on Nvidia's Roadmap for Embodied AI" — a comprehensive presentation outlining NVIDIA's vision for physical AI, from current robot limitations to future simulation capabilities.

## Blog / Recent Posts

| Date | Title | Link |
|---|---|---|
| May 2025 | The Physical Turing Test: Jim Fan on Nvidia's Roadmap for Embodied AI | [AI Ascent 2025](https://aiascent.com/jim-fan-physical-turing-test) |
| Jan 2025 | Introducing NVIDIA Cosmos, an Open-Source Video World Model | [LinkedIn Post](https://www.linkedin.com/posts/drjimfan_introducing-nvidia-cosmos) |
| Jul 2025 | Genie 3: Game Engine 2.0 | [LinkedIn Post](https://www.linkedin.com/posts/drjimfan_genie-3-shows-us-a-silhouette-of-game-engine) |
| Apr 2024 | Generally Capable Agents in Open-Ended Worlds | [NVIDIA GTC 2024](https://www.youtube.com/watch?v=ZSPEyFqAGDc) |
| 2024 | The Second Pre-training Paradigm | [jimfan.me](https://jimfan.me/blog/second-pretraining-paradigm) |

Fan is active on LinkedIn with 208,000+ followers and 280+ posts, regularly sharing research updates and thought leadership on embodied AI.

## Related People

- **Jensen Huang** — NVIDIA CEO who provided support and blessing for GEAR Lab's establishment
- **Yuke Zhu** — NVIDIA researcher presenting Isaac GR00T N1.6 at CoRL 2025
- **Dieter Fox** — NVIDIA VP of Research, collaborator on embodied AI research
- **Fei-Fei Li** — Stanford professor; Fan's PhD advisor, pioneer in computer vision and embodied AI
- **Ilya Sutskever** — Former OpenAI co-founder; Fan was OpenAI's first intern
- **Benjamin Clavié** ([[bclavie]]) — Though working in different domains (IR vs. robotics), both share NVIDIA/Answer.AI ecosystem connections through Hugging Face and open-source AI advocacy
- **Scott Wu** ([[scott-wu]]) — Both working on AI agents at different levels: Fan on physical/embodied agents, Wu on software/coding agents

## X Activity Themes

Fan's X activity centers on:

- **Embodied AI research** — Sharing breakthroughs in robot learning, simulation, and physical reasoning.
- **NVIDIA product launches** — Announcing new versions of GR00T, Cosmos, Genie, and simulation platforms.
- **Physical AI vision** — Articulating the future of robots in everyday life, from household tasks to industrial applications.
- **Simulation technology** — Updates on digital twins, world models, and the progression from Simulation 1.0 to 2.0.
- **Academic talks** — Promoting presentations at GTC, AI Ascent, CoRL, and other conferences.
- **Robotics industry commentary** — Discussing the state of humanoid robots, AI agents, and the path to general-purpose physical intelligence.
- **Open-source advocacy** — Promoting open-weight models and accessible simulation platforms for the research community.
