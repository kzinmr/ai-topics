---
title: Ali Farhadi
type: entity
entity_type: person
status: L3
created: 2026-04-13
updated: 2026-04-14
sources:
  - https://homes.cs.washington.edu/~ali/
  - https://www.fastcompany.com/91283517/ai2s-ali-farhadi-advocates-for-open-source-ai-models-heres-why
  - https://www.fastcompany.com/91225845/ai2-ceo-ali-farhadi-believes-open-source-is-the-future
  - https://www.geekwire.com/2026/allen-institute-for-ai-ceo-ali-farhadi-steps-down-as-nonprofit-navigates-shifting-ai-landscape/
  - https://www.geekwire.com/2026/microsoft-hires-former-ai2-ceo-ali-farhadi-and-key-researchers-for-suleymans-ai-team/
  - https://thelettertwo.com/2025/04/09/ai2s-olmotrace-tool-reveals-the-origins-of-ai-model-training-data/
  - https://madrona.com/ia-summit-2023-keynote-open-source-models-ali-farhadi
  - https://building.theatlantic.com/open-research-is-the-key-to-unlocking-safer-ai-15d1bac9085d
  - https://allenai.org/blog/olmotrace
  - https://raivn.cs.washington.edu/
tags:
  - person
  - computer-vision
  - open-source-ai
  - large-language-models
  - ai-research-leader
  - object-detection
  - multimodal-ai
  - embodied-ai
  - ai-safety
---


# Ali Farhadi

Computer vision pioneer, co-creator of **YOLO** (You Only Look Once) object detection, founder of **Xnor.ai** (acquired by Apple), former CEO of Allen Institute for AI (Ai2). In March 2026 stepped down from Ai2 and joined **Microsoft** as CVP of AI under Mustafa Suleyman's SuperIntelligence team alongside Hanna Hajishirzi, Ranjay Krishna, and Sophie Lebrecht.

## Bio

Born 1982 in Iran. PhD from University of Illinois at Urbana-Champaign under David Forsyth. Postdoc at Carnegie Mellon Robotics Institute (Martial Hebert, Alyosha Efros). Professor at University of Washington Allen School since 2012. Joined Ai2 in 2015. Co-founded Xnor.ai (2018), acquired by Apple (~$200M, 2020). Led Apple's next-generation ML efforts until July 2023, when he returned to Ai2 as CEO. Over his tenure at Ai2: lined up **$1B+** in funding, released **300+ models and artifacts** with **33M+ downloads**, secured a **$152M NSF+Nvidia initiative** for open AI models in scientific research. Named one of Forbes's Top 5 AI Entrepreneurs (2018). Sloan Research Fellowship, NSF Career Award, multiple best paper awards at CVPR/NeurIPS/AAAI. Married to **Hanna Hajishirzi**, NLP professor at UW and Senior Director at Ai2.

## Timeline

| Period | Role | Key Events |
|--------|------|------------|
| 2001-2009 | PhD, UIUC | Under studying under David Forsyth; work on attribute-based object recognition |
| 2009-2010 | Postdoc, CMU Robotics Institute | Worked with Martial Hebert and Alyosha Efros |
| 2012-2015 | Assistant Professor, UW Allen School | Early research on visual reasoning, scene understanding |
| 2015-2023 | Researcher → Ai2 Leadership | Joined Ai2; co-founded Xnor.ai; set AI Grand Challenge around embodied understanding |
| 2016 | YOLO Release | Co-authored "You Only Look Once" with Joseph Redmon — real-time object detection at 45fps |
| 2017 | YOLO9000 | "Better, Faster, Stronger" — 9000+ category detection |
| 2018 | Founded Xnor.ai | Edge AI startup spun out of Ai2 |
| 2020 | Xnor.ai acquired by Apple | ~$200M deal; Farhadi joins Apple ML team |
| 2020-2023 | ML leadership at Apple | Led next-generation ML during post-acquisition |
| Jul 2023 | CEO of Ai2 | Returned to lead Allen Institute for AI, replacing interim CEO Peter Clark |
| Feb 2024 | OLMo 7B Launch | Released "a truly open LLM" — full pretraining data (Dolma), training code, and weights |
| 2025 | OLMo 3 & Tülu 3 | Olmo 3 32B Think (strongest fully open reasoning model), Tülu 3 405B (first fully open post-training at scale) |
| 2025 | OLMoTrace Launch | Real-time attribution of model outputs back to trillions of training tokens |
| Dec 2025 | Ai2 named #1 open model builder | Hugging Face Heatmap; Artificial Analysis Openness Index |
| Mar 2026 | Stepped down as Ai2 CEO | After 2.5-year tenure; cited desire to pursue frontier-scale AI research |
| Apr 2026 | Joined Microsoft | Hired as CVP under Mustafa Suleyman's SuperIntelligence team alongside Hajishirzi, Krishna, Lebrecht |

## Core Ideas

### "Truly Open" AI — Beyond Open Weights
> "Open source is how we drive progress. Transparency and performance are essential for developers to scale AI with open, U.S.-built models like Olmo."

> "Openness is the only way forward."

> "To us, open-source means that you understand what you did. Open weights models (such as Meta's) are great because people could just grab those weights and follow the rest, but they aren't open source. Open source is when you actually have access to every part of the puzzle."

Farhadi draws a sharp line between **open weights** (Meta's LLaMA approach) and **truly open** AI. For him, openness means the full pipeline: training data (Dolma, 5.9 trillion tokens), training code, model weights, evaluation recipes, and fine-tuning methods — all under permissive licenses. This is the most rigorous definition of openness in the industry today, surpassing even the Open Source Initiative's emerging AI definitions.

> "The biggest threat to AI innovation is the closed nature of the practice."

### The "Language Model of a Crow" — Embodied Understanding as Grand Challenge
> "Don't worry about the crow in the title. I'll explain my way out of it." — Madrona IA Summit, 2023

Ten years ago, Farhadi set an AI Grand Challenge using a video of a crow watching a person dig a hole in Arctic terrain, place something inside, and fly away. The crow later returns and acts on the buried object — demonstrating that it **understood the scene's causal structure**, not just its visual content.

The crow became his metaphor for what AI must achieve: **not pattern recognition, but grounded understanding of actions, interactions, and relationships in the physical world**. This philosophy connects his entire research arc — from YOLO's holistic scene understanding, through AI2-THOR's interactive 3D environments, to Molmo's vision-language grounding.

His 2026 Columbia Engineering lecture "What is the Language Model of a Crow?" directly challenged the field: current LMs model text distributions, but **intelligence requires understanding the world that language describes**. The question "what is the language model of a crow?" is really "what does it mean to model understanding, not surface patterns?"

### Data Transparency as Safety
> "The starting point to developing safe AI models is, we must understand what the model understands. With closed models, we have no hope of conducting the research that is required to design and effectively regulate AI models."

> "OLMoTrace connects the output to the input, as simple as that. Because our inputs are open, we could actually connect them."

Farhadi's approach to AI safety is distinctive: **safety through radical transparency**, not through closed-door evaluation. Ai2's OLMoTrace tool (2025) traces every model output back to its specific training documents in real time, enabling community-driven fact-checking, bias auditing, and hallucination detection.

His 2024 Atlantic blog post laid out three principles:
1. **AI safety is a technical problem** — first understand what models understand, then design safety into every stage
2. **Safety research needs to be done in the open** — the dynamics of closed-model safety are a "mixed bag" of undocumented internal research
3. **Designing for safety is a continuous process** — there is no simple "safe" or "unsafe" implementation

> "This is an open tool for an open community... We believe that by linking to the pre-trained data, we will see a new class of algorithms. We see a new class of customization, fine-tuning, and post-training approaches, and that's what we're after."

### The Nonprofit-to-Corporate Migration — A Structural Story
> "The cost to do extreme-scale open model research is extraordinary... really hard to do extreme-scale model work inside of a nonprofit." — Bill Hilf, Ai2 Board Chair

Farhadi's departure from Ai2 and move to Microsoft illustrates the **compute economics problem** facing open AI. Nonprofit institutes, even well-funded ones like Ai2 (backed by Paul Allen's estate and the Fund for Ai2), cannot compete with the billions that for-profit tech giants spend annually on frontier model training.

His decision to join Microsoft's SuperIntelligence team was strategic, not opportunistic:

> "I believe this is an opportunity to work on something that goes beyond standalone models toward tightly connected ecosystems. The next generation of models and agents will require a tight loop between data, tools, code, enterprise infrastructure, and agents."

> "Microsoft has all the pieces to win in this AI race: data, search, coding, infrastructure, agents, software, and the world's biggest Fortune 500 companies taking dependencies on MS everyday."

This reflects Farhadi's evolution from **open-source purist** to **pragmatic open advocate** — recognizing that frontier-scale research requires corporate resources, and that Microsoft's position (unlike OpenAI's) leaves room for genuinely open model development alongside proprietary products.

### Embodied AI and Visual Reasoning
Farhadi's research has consistently pushed beyond static image recognition toward **agents that understand and interact with the world**:

- **AI2-THOR** (2017) — interactive 3D household environments for training and evaluating embodied agents
- **RoboTHOR** (2020) — open simulation-to-real embodied AI platform
- **ProcTHOR** (2022, NeurIPS Outstanding Paper) — procedurally generated environments for scaling embodied AI
- **Visual Commonsense Reasoning (VCR)** (2018) — not just "what is in the image?" but "why is this happening and what will happen next?"
- **Molmo/MolmoAct** (2024-2025) — multimodal vision-language models that ground language in spatial understanding and action

His RAIVN Lab (Reasoning, AI, and VisioN) at UW, co-directed with Ranjay Krishna, has produced foundational work in **Visual Genome**, **Objaverse**, **DataComp**, **OpenCLIP**, and **Merlot** — bridging the gap between seeing and understanding.

## Research Philosophy Synthesis

| Principle | Manifestation | Quote/Evidence |
|-----------|--------------|----------------|
| **Radical openness** | Full pipeline transparency (data + code + weights + recipes) | "Open source is when you actually have access to every part of the puzzle" |
| **Safety through transparency** | OLMoTrace, open safety toolkit, community auditability | "With closed models, we have no hope of conducting the research" |
| **Embodied understanding** | AI2-THOR, RoboTHOR, MolmoAct, "crow" Grand Challenge | Intelligence requires understanding actions, interactions, relationships |
| **Pragmatic scale-seeking** | Move from Ai2 nonprofit to Microsoft's compute resources | "The cost to do extreme-scale open model research is extraordinary" |
| **Simplicity in design** | YOLO's single-network approach, Xnor's edge-first architecture | One model, one evaluation — not multi-stage pipelines |
| **Community-first research** | 300+ open artifacts, 33M+ downloads, open benchmarks | "This is an open tool for an open community" |

## Convergence with Other Thinkers

- **Andrej Karpathy** — Both advocate for radical openness in AI. Karpathy's "Software 2.0" (neural networks as programs) converges with Farhadi's "truly open" pipeline (understanding every part). Karpathy left Tesla for open research; Farhadi left Apple for Ai2 for the same reason.
- **Simon Willison** — Both emphasize that AI tools must be **inspectable** to be trustworthy. Willison's "don't trust the code" mirrors Farhadi's "open weights aren't open source" — surface access isn't enough; you need the full pipeline.
- **Salvatore Sanfilippo (antirez)** — Shared philosophy of **radical simplicity**. Sanfilippo's Redis Manifesto ("code is like a poem") parallels Farhadi's YOLO principle: replace complex multi-stage pipelines with a single, elegant system that just works.
- **Mustafa Suleyman** — Farhadi's move to Microsoft's SuperIntelligence team places him in Suleyman's orbit. Suleyman's "Humanist SuperIntelligence" framework — AI that is controllable, aligned, and in service to humanity — aligns with Farhadi's transparency-first safety approach, though Suleyman's corporate positioning is more cautious about openness.

## Contributions

| Project | Description | Impact |
|---------|-------------|--------|
| **YOLO** (2016) | Real-time object detection via single neural network | Foundation for real-time CV; 80K+ citations; OpenCV People's Choice Award |
| **YOLO9000** (2017) | 9000+ category detection via WordTree + joint training | CVPR Best Paper Honorable Mention |
| **XNOR-Net** (2016) | Binary convolutional networks for edge inference | Foundation for Xnor.ai; enabled edge AI on mobile/IoT |
| **Xnor.ai** (2018) | Edge AI inference engine for mobile/IoT | Acquired by Apple for ~$200M |
| **AI2-THOR** (2017) | Interactive 3D simulation environment for embodied AI | Standard platform for embodied AI research |
| **RoboTHOR** (2020) | Open simulation-to-real embodied AI platform | CVPR 2020 |
| **Visual Commonsense Reasoning (VCR)** (2018) | Dataset requiring "why" reasoning about visual scenes | New paradigm beyond object recognition |
| **OLMo** (2024-) | Fully open LLM with training data, code, weights | #1 open model on Hugging Face Heatmap |
| **Tülu 3 405B** (2025) | First fully open post-training at scale with RLVR | Surpasses DeepSeek-V3; fully open recipes |
| **Molmo** (2024-) | Open multimodal vision-language model | Used in robotics, scientific imaging |
| **Dolma** | 5.9-trillion-token open pretraining dataset | Largest fully open training corpus |
| **OLMoTrace** (2025) | Output-to-training-data attribution tool | First real-time tracing across trillions of tokens |
| **HellaSwag** (2019) | Commonsense reasoning benchmark | "Can a machine really finish your sentence?" — widely adopted |
| **BiDAF** (2016) | Bidirectional Attention Flow for machine comprehension | Foundational QA architecture |
| **RAIVN Lab** | UW's computer vision and reasoning lab | Produced YOLO, XNOR-Net, Visual Genome, Objaverse, DataComp |

## Related

- [[mustafa-suleyman]] — Microsoft AI CEO who hired Farhadi's team
- [[concepts/hanna-hajishirzi]] — OLMo project lead, UW NLP professor, Farhadi's spouse, joined Microsoft alongside him
- [[concepts/ranjay-krishna]] — Molmo lead, RAIVN Lab co-director, joined Microsoft alongside Farhadi
- [[concepts/joseph-redmon]] — YOLO co-author; stopped CV research citing military/privacy concerns
- [[concepts/olmo-open-language-model]] — Farhadi's flagship open LLM project at Ai2
- [[concepts/open-model-consortium]] — Collaborative open-source AI model development
- [[concepts/object-detection]] — YOLO and the real-time detection paradigm
-  — Agents that understand and interact with physical environments-  — Farhadi's distinctive safety approach-  — Beyond recognition to understanding "why" and "what next"
