---
title: Jonathan Whitaker
handle: "@johnowhitaker"
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - ai
  - education
  - generative-models
  - fastai
  - diffusion
  - open-source
---


# Jonathan Whitaker (@johnowhitaker)

| | |
|---|---|
| **X** | [@johnowhitaker](https://sigmoid.social/@johnowhitaker) |
| **Blog** | [johnowhitaker.dev](https://johnowhitaker.dev) |
| **GitHub** | [johnowhitaker](https://github.com/johnowhitaker) |
| **Role** | AI Researcher & Educator at Answer.AI |
| **Known for** | Hugging Face Diffusion Models course, fastai Part 2, generative AI education, SpecID eval |
| **Bio** | Jonathan Whitaker is an AI researcher and educator working at Answer.AI, where he focuses on making generative AI accessible through practical courses, open-source tools, and hands-on experiments. He co-created the Hugging Face Diffusion Models course, teaches fastai Part 2, and runs the Data Science Castnet YouTube channel. His work spans image generation, diffusion models, LLMs, and creative AI applications. |

## Overview

Jonathan Whitaker (known online as Johno) is a polymath researcher and educator whose work sits at the intersection of generative AI, practical ML education, and creative experimentation. Currently doing R&D at Answer.AI alongside [[Jeremy Howard]] and the Answer.AI team, Jonathan has established himself as one of the most effective communicators of complex generative AI concepts to practitioners at all levels.

His educational contributions are extensive and impactful. He co-created the **Hugging Face Diffusion Models course** — one of the most popular and comprehensive open educational resources on diffusion-based generative models — and is currently co-authoring a book building on that work. He teaches **Part 2 of the fastai course**, which covers advanced deep learning topics including diffusion models, transformers, and generative techniques. His **Data Science Castnet** YouTube channel documents his projects and experiments, making cutting-edge research accessible to a broad audience. Before joining Answer.AI full-time, he worked as a data scientist at Zindi (Africa's data science competition platform), did consulting in generative AI, and was builder-in-residence at PlaygroundAI, where he helped train their first in-house Stable Diffusion variant.

What makes Jonathan distinctive in the AI education space is his **breadth across modalities** and his willingness to work on unusual, creative projects. He's published papers on extracting generative capabilities from discriminative models (Direct Ascent Synthesis), created evaluation benchmarks for multimodal LLMs (SpecID), built courses on everything from diffusion models to 3D generation, and simultaneously maintains side projects involving Zimbabwean spider identification, spectral fluorescence experiments with bacteria, and duckweed growth optimization with LLMs. This combination of serious research, practical education, and creative tinkering makes him a unique voice in the AI community.

Jonathan's educational philosophy aligns closely with the fastai "top-down" approach: start with working code and interesting results, then drill down into the underlying theory. His blog posts, videos, and courses consistently demonstrate this — showing readers how to build, fine-tune, and evaluate generative models using practical, accessible tooling rather than abstract theory.

## Core Ideas

### The Generative Model Training Recipe

In his influential April 2023 post "A Recipe for Training Good Generative Models," Jonathan articulated a three-stage framework that captures how the best generative models are built:

1. **Pre-train on LOTS of data** — More data equals better foundational capability. Language models train on the entire internet; image models train on billions of image-caption pairs (LAION). This stage gives the model the ability to produce anything — including the bad stuff.

2. **Fine-tune on HIGH-QUALITY data** — After pre-training, the model needs to be biased toward generating good outputs. For text-to-image models, this means curating high-quality images with good captions. For language models, this means carefully crafted instruction-following datasets. As Jonathan noted: *"Next time you read about a cool new generative model, keep an eye out for mention of this 'high-quality fine tune' step."*

3. **Incorporate HUMAN FEEDBACK** — The final stage involves using human preference data to align the model with what users actually want. This can be through RLHF (Reinforcement Learning from Human Feedback), DPO (Direct Preference Optimization), or simpler ranking approaches. Jonathan emphasized that *"successful products require pleasing users, so making sure the model aligns with human preferences is crucial."*

This framework, while now widely understood, was articulated early and clearly by Jonathan, connecting the dots between ULMFiT (from Jeremy Howard and Sebastian Ruder), Stable Diffusion, ChatGPT, and the broader generative AI landscape.

### More Compute = Better Results (But Be Smart About It)

In his "More=Better?" post for Answer.AI, Jonathan demonstrated through experiments that generating more samples and selecting the best ones can produce substantial quality improvements — even with the same underlying model. For image generation, he showed that picking the best of 100 Stable Diffusion outputs dramatically outperformed single-shot generation. For text, best-of-10 with Llama 3 8B boosted the AlpacaEval-2 win rate from 20.5% to 29.0%, beating GPT-4 (23.6%).

> *"There's a point of view that spending this time to get more out of existing models like this is futile in the face of the next big one (TM) which will do even better without any tricks. I don't buy it! As we get faster, cheaper, better models, I believe that finding ways to boost them even further will continue to be worth it."*

This connects to the broader theme of **inference-time compute scaling** that many researchers (including [[Alex Zhang]] with RLMs) have been exploring — spending more compute at inference time to extract better results from existing models.

### Making Generative AI Accessible Through Education

Jonathan's core mission is democratizing access to generative AI knowledge. His educational philosophy emphasizes:

- **Hands-on practice** over abstract theory — students should be generating images, fine-tuning models, and building applications from day one.
- **Open-source tooling** — using freely available models, datasets, and frameworks rather than proprietary APIs.
- **Creative projects** — encouraging students to find their own applications and interests within the generative AI space.
- **Multimodal literacy** — understanding text, image, audio, and 3D generation as interconnected capabilities rather than siloed domains.

The Hugging Face Diffusion Models course, which he co-created, exemplifies this approach. It takes students from basic diffusion concepts through training their own models, all using open-source tools and practical examples.

### SpecID: Creative Evaluation for Multimodal LLMs

Jonathan created **SpecID**, a novel evaluation benchmark that tests multimodal LLMs on identifying Zimbabwean spider species from photographs — a task that is genuinely difficult even for human experts. The evaluation was constructed by pulling 100 photos with confirmed "research grade" identifications from his iNaturalist catalog, then adding up to four distractor species for each sample.

The results revealed significant gaps in multimodal model capabilities:
- gemini-2.5-pro-exp-03-25 scored 57%
- gemini-3-pro-preview scored 64%
- GPT-4o scored around 50%+
- Jonathan himself scored higher than all models when using his own field observations

This creative approach to evaluation — using a genuinely hard, domain-specific task rather than standard benchmarks — demonstrates Jonathan's philosophy that evaluations should test real capabilities, not just benchmark gaming. As he put it: *"Make your own evals! Occasionally surprising, easy, fun!"*

### Direct Ascent Synthesis: Generative Capabilities in Discriminative Models

Jonathan's paper on **Direct Ascent Synthesis (DAS)** reveals a fundamental insight about neural networks: classification models contain hidden generative capabilities that can be extracted through gradient-based optimization. Starting with random noise and using the discriminative model's internal representations to guide refinement, DAS can produce high-quality images — essentially discovering that "the ability to create lies within the ability to recognize."

This work challenges the traditional separation between discriminative and generative models and suggests that future AI systems could combine both capabilities more efficiently.

## Key Work

### Educational Contributions

- **Hugging Face Diffusion Models Course** — Comprehensive open course on diffusion models, from basic concepts to training custom models. One of the most popular AI education resources on the HF platform. Co-authored with Lewis Tunstall and the HF education team.
- **fastai Part 2** — Teaches advanced deep learning topics including diffusion models, transformers, and generative AI. Part of Jeremy Howard's renowned practical deep learning curriculum.
- **Answer.AI Dev Chats** — Regular discussion sessions on cutting-edge AI research and practical applications.
- **Data Science Castnet YouTube Channel** — Documents projects, experiments, and tutorials covering generative AI, diffusion models, LLMs, and creative applications.
- **JohnosLab YouTube Channel** — Newer channel focused on clearing out side-project backlog through public experimentation.
- **The Generative Landscape** — Older course covering all aspects of generative modeling.
- **AIAIART Course** — Early course on AI-generated art, covering GANs, diffusion models, and creative applications.

### Research & Papers

- **Direct Ascent Synthesis: Revealing Hidden Generative Capabilities in Discriminative Models** (2025) — Novel technique that extracts generative capabilities from classification networks through gradient-based optimization. Demonstrates that discriminative models can create images without additional training.
- **SpecID: A Hard Eval for Multimodal LLMs** (2025) — Creative benchmark testing multimodal LLMs on Zimbabwean spider species identification. Reveals significant gaps between model and human expert performance on domain-specific visual tasks.
- **Diffusion Language Models** (2025) — Turning ModernBERT into an instruction-tuned diffusion language model.
- **SVG Generation Research** (2025) — Using SVG generation as a microcosm for studying generative AI research trends.

### Open Source Projects

- **aiaiart** — Course content and resources for the AIAIART course (567 GitHub stars).
- **tglcourse** — The Generative Landscape course materials (148 GitHub stars).
- **imstack** — Optimizable stack of images at different resolutions for deep learning tasks.
- **parameter-golf** — Contributed to openai/parameter-golf, exploring minimal parameter solutions.
- **solveit_demos** — Demonstrations of the SolveIt thinking developer environment.
- **BLY** — Personal projects and experiments.

### Blog Posts & Writing

| Date | Title | Topic |
|------|-------|-------|
| Mar 2026 | Evals Skills for Coding Agents | Teaching coding agents to evaluate their own outputs |
| Feb 2026 | Spectral Shifts with Pyoverdine pH | Biofluorescence experiments |
| Aug 2025 | Diffusion Beats Autoregressive in Data-Constrained Settings | Paper reading and analysis |
| Aug 2025 | Duckweed Growth Experiments | LLMs as general optimizers in science |
| Jul 2025 | SVG Generation as Microcosm of GenAI Research | Using SVG to study generative AI trends |
| Jun 2025 | The Diffusion Duality | Paper reading on diffusion model theory |
| Feb 2025 | Direct Ascent Synthesis | Revealing generative capabilities in discriminative models |
| Jan 2025 | 2024 Overflow | Year-end roundup: UV fluorescence, ESP32CAM, ModernBERT, nbdev, LLM evals |
| Jul 2023 | Why and How I'm Shifting Focus to LLMs | Transition from image to text generation |
| Apr 2023 | A Recipe for Training Good Generative Models | Three-stage framework for generative model training |
| Apr 2023 | Reward Hacking with RainbowDiffusion | Exploring adversarial behavior in diffusion models |

### Professional Experience

- **Answer.AI** (Jan 2024–present) — R&D in generative AI, education, and practical applications.
- **PlaygroundAI, Builder-in-Residence** (Jan–Jun 2023) — Helped train first in-house Stable Diffusion variant; worked on guidance, instruction-following, and sampling improvements.
- **Zindi, Senior Data Scientist** — Prepared data science competitions, built models, and mentored participants across Africa.
- **Ixio Analytics / iXperience** — Created and delivered online courses in data science, ML, and big data; lead instructor for Data Science summer class.
- **African Leadership University** — Collaborated on data science education programs.

## Blog / Recent Posts

| Date | Title | Summary |
|------|-------|---------|
| Mar 2026 | Evals Skills for Coding Agents | Practical guide for teaching AI coding agents to evaluate their own outputs using instrumentation, traces, and experiments. |
| Feb 2026 | Spectral Shifts with Pyoverdine pH | Biofluorescence experiments exploring how bacterial pigments change under different pH conditions. |
| Aug 2025 | Diffusion Beats Autoregressive | Analysis of a paper showing diffusion models outperforming autoregressive models in data-constrained settings. |
| Jun 2025 | The Diffusion Duality | Deep dive into the mathematical duality underlying diffusion models. |
| Feb 2025 | Direct Ascent Synthesis | Paper on extracting generative capabilities from discriminative classification models through gradient optimization. |
| Jan 2025 | 2024 Overflow | Year-end roundup covering UV fluorescence, ESP32CAM experiments, ModernBERT, nbdev, and LLM evaluations. |
| Jul 2023 | Why and How I'm Shifting Focus to LLMs | Personal essay on transitioning from image generation to language model research and education. |
| Apr 2023 | A Recipe for Training Good Generative Models | Influential three-stage framework: pre-train on lots of data, fine-tune on high-quality data, incorporate human feedback. |

## Related People

- **[[Jeremy Howard]]** — fastai founder; Answer.AI co-founder; Jonathan's close collaborator and teaching partner.
- **[[Lewis Tunstall]]** — Co-author of the Hugging Face Diffusion Models Course; ML engineer at Hugging Face.
- **[[Hamel Husain]]** — Both work at Answer.AI; both write practical guides on ML tooling and evaluation.
- **[[Daniel van Strien]]** — Both contribute to Hugging Face educational resources and write practical ML tutorials.
- **[[Simon Willison]]** — Fellow advocate for accessible, practical AI tooling and education.

## X Activity Themes

Jonathan's X activity (@johnowhitaker) centers on:

1. **Generative AI Education** — Sharing course materials, tutorials, and insights about diffusion models, LLMs, and multimodal AI.
2. **Research Paper Summaries** — Breaking down recent papers on diffusion models, generative AI, and evaluation methods into accessible explanations.
3. **Creative Experiments** — Documenting unusual side projects including spider identification, biofluorescence, and growth optimization with LLMs.
4. **Answer.AI Community** — Participating in dev chats, sharing team research, and collaborating with the Answer.AI community.
5. **Open Source ML** — Promoting open-source models, tools, and frameworks for generative AI.
6. **Evaluation & Benchmarking** — Discussing creative approaches to evaluating multimodal models and the importance of domain-specific benchmarks.
7. **fastai Ecosystem** — Contributing to and promoting the fastai curriculum and community.
