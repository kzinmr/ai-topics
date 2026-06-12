---
title: Learning LLMs in 2025 (Yoav Goldberg)
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level2
tags:
  - curriculum
  - methodology
  - education
aliases: [yoavg-llm-guide, llm-learning-guide-2025]
sources:
  - https://gist.githubusercontent.com/yoavg/95bbc5768cacd2bf07187779fada4867/raw/bcb8ff287e03a7e49f7ae5daedc03d04c11d8a71/llm-materials-2025.md
  - raw/articles/2026-05-04_yoavg-learning-llms-2025.md
---

# Learning LLMs in 2025

> **Yoav Goldberg** (renowned NLP researcher, author of *Neural Network Methods for NLP*) has curated a **selective curriculum collection** for learning LLMs. Targeted at learners who already understand Transformer internals and basic ML/DL, this guide carefully selects academic resources for deeply studying **LLM aspects beyond ML algorithms** (architecture, data, alignment, evaluation, safety, human-centered design).
>
> This is not a concept per se, but **meta-knowledge / a knowledge map** — it functions as a learning compass.

---

## Guide Characteristics

Yoav's guide is unique in the following ways:

1. **Non-ML Algorithm Focus** — While there are many textbooks on optimization and RL, this is the only guide collecting "the other interesting parts" of LLMs
2. **Academic Curation** — Only courses from top universities such as MIT/Stanford/Princeton/CMU/Berkeley/JHU/NYU
3. **Learner Prerequisites** — Starts from the assumption that Transformers and basic ML/DL are already known (intermediate to advanced learners)
4. **Yoav Goldberg's Credibility** — Quality assurance from a leading figure in NLP

---

## 📚 Resource Evaluation List

Each resource is comprehensively evaluated on **quality** (beyond Yoav's recommendation), **accessibility** (whether course materials are freely accessible), **relevance** (which LLM areas it covers), and **freshness**.

Legend: 🟢 Excellent / 🔵 Good / 🟡 Partial limitations / ⚪ Needs consideration

---

### 📖 Courses (Full)

#### 1. David Chiang — Theory of Neural Networks (Notre Dame, Fall 2024)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🔵 High | Formal/theory-oriented. "Almost like a book," as Yoav himself acknowledges. Strong Transformers chapter. |
| **Accessibility** | 🟢 Fully public | Full schedule, assignments, projects published on site. No Notre Dame restrictions. |
| **Relevance** | ⚪ Partial | Not LLM-specific. Approaches Transformers as **neural network theory**. Main themes: automata, Turing machines, and logic connections. |
| **Freshness** | 🟢 2024 | Latest 2024 content, including state-space models section. |
| **Format** | Lectures + assignments + programming projects | Theory-heavy, somewhat less implementation. |
| **Recommendation** | ⚪ **For specific interests** | For those interested in the intersection of theoretical CS and neural networks. Better for understanding "principles" rather than "how to build" LLMs. |

> **Overall Assessment:** Not a course to take first when learning LLMs. However, valuable for research-oriented learners who want to deeply understand Transformers' **theoretical limits** (circuit complexity, relationship to first-order predicate logic).

---

#### 2. Chenyan Xiong & Daphne Ippolito — Large Language Models: Methods and Applications (CMU, Fall 2024→Spring 2026)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 High | Official CMU LTI course. Updated to Spring 2026 edition. Full assignments and projects. |
| **Accessibility** | 🟢 Fully public | Full schedule, reading lists, assignment outlines at [cmu-llms.org/schedule/](https://cmu-llms.org/schedule/). |
| **Relevance** | 🟢 Broad | Prompting→Fine-tuning→RAG→Dialogue→Evaluation→Code→Multimodal→Safety→Deployment — **comprehensive LLM applications**. |
| **Freshness** | 🟢 2026 | Spring 2026 edition, includes latest topics. |
| **Format** | Lectures + 3 assignments + final project | Good balance of theory and practice. |
| **Recommendation** | 🟢 **Best for beginners to intermediate** | The most balanced course for those wanting comprehensive learning as an LLM "user." The most accessible entry point in Yoav's guide. |

> **Overall Assessment:** The most "all-inclusive" and balanced course in this guide. Covers everything from prompting to multi-agent and safety. While Yoav lightly rates it as "Nice collection of topics," it is actually **the first course most learners should take**.

---

#### 3. Danqi Chen & Sanjeev Arora — Deep Dive into Large Language Models (Princeton, Fall 2024)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 Very High | Dream team of Chen (context length, knowledge editing) + Arora (theory). Paper-by-paper deep dives. |
| **Accessibility** | 🟢 Fully public | [princeton-cos597r.github.io](https://princeton-cos597r.github.io/) Fully public. Discussion-based format. |
| **Relevance** | 🟢 Broad and deep | Pre-training→Scaling laws→Data curation→Instruction Tuning→RLHF/DPO→Alignment→Inference-time compute→Long context→Distillation→RAG→Multimodal→Hardware (FlashAttention). |
| **Freshness** | 🔵 Fall 2024 | Sufficiently new for 2024, but doesn't include post-2025 advances like GRPO, RFT, DeepSeek-R1. |
| **Format** | Discussion + Debate Panel + Final Project | Centered on paper close reading + critical discussion. Not suitable for passive learning. |
| **Recommendation** | 🟢 **Best for research-oriented intermediate learners** | For those wanting deep understanding of "building and evaluating" LLMs. Requires paper digestion ability. |

> **Overall Assessment:** One of the best-balanced courses for breadth and depth. The **Scribe system (students write lecture notes)** ensures high-quality materials. However, since it's paper-based discussion format, **just reading won't give you full value**. Best tackled in a learning group.

---

#### 4. Diyi Yang — Human Centered LLMs (Stanford CS329X, Fall 2025)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 High | Official Stanford course. Intersection of HCI (Human-Computer Interaction) and NLP. |
| **Accessibility** | 🟢 Fully public | [web.stanford.edu/class/cs329x/](https://web.stanford.edu/class/cs329x/) Fully public. |
| **Relevance** | 🟢 Unique perspective | Alignment, personalization, human-AI interaction, cultural bias, privacy, AI companions. Views **LLMs from a human perspective**. |
| **Freshness** | 🟢 Fall 2025 | Includes latest research. |
| **Format** | Lectures + 3 assignments + final project | Organized around human-centered themes. |
| **Recommendation** | 🟢 **For HCI/product-oriented learners** | Best for understanding "the relationship between LLMs and humans" rather than "LLM performance." More for PMs and researchers than engineers. |

> **Overall Assessment:** The only HCI/human-centered perspective in Yoav's guide. Addresses the question of **"LLMs work, but how do humans engage?"** Covers alignment, personalization, bias, and privacy from both technical and human-centered angles. For those needing a non-engineering perspective.

---

#### 5. Dawn Song & Dan Hendrycks — Understanding LLMs: Foundations and Safety (UC Berkeley, Spring 2024)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 Very High | Stellar guest speakers (Łukasz Kaiser/OpenAI, Yuandong Tian/Meta, Nicholas Carlini/Google DeepMind, Max Tegmark/MIT, etc.). |
| **Accessibility** | 🟢 Fully public + video | [rdi.berkeley.edu/understanding_llms/s24](https://rdi.berkeley.edu/understanding_llms/s24) plus **YouTube playlist** with all lectures. |
| **Relevance** | 🟢 Foundations + Safety | LLM foundations (scaling laws, Transformer internals) + Safety (model editing, RepE, memory extraction, adversarial attacks, formal verification). |
| **Freshness** | 🟡 Spring 2024 | Early 2024. Safety discussions slightly dated (Mythos-era safety discourse has advanced significantly since 2024). |
| **Format** | Guest lectures + Lab + Project | Each session by domain experts. Depth varies (guest-dependent). |
| **Recommendation** | 🟢 **Best for safety specialization** | One of the best existing courses for learning LLM safety. All viewable via YouTube. However, starting from 2024, recent safety discussions (Reward Hacking, Eval Hack, Agent Safety, etc.) are not covered. |

> **Overall Assessment:** **A unique course specializing in LLM safety.** The dual leadership of Hendrycks (CAIS) and Song (Berkeley) is effective. The biggest strength: all lectures freely available on YouTube. However, content is from early 2024 and doesn't include 2025-26 safety advances (Claude Mythos Red Teaming reports, Reward Hacking, etc.).

---

#### 6. Graham Neubig — Advanced NLP (CMU, Fall 2024)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🔵 High | Neubig is an NLP education master (author of *Neural Machine Translation*, numerous lecture videos). |
| **Accessibility** | 🟡 **Limited** | [Schedule page](https://www.phontron.com/class/anlp-fall2024/schedule/) still shows "Schedule will be posted soon." Many materials are individually available on Neubig's YouTube channel, but systematic access as course materials is difficult. |
| **Relevance** | 🔵 Broad but not LLM-specific | Includes traditional NLP topics. LLM parts (architecture, evaluation, interpretability) are good but only a subset of overall themes. |
| **Freshness** | 🔵 Fall 2024 | Appropriate. |
| **Format** | Lectures + assignments + projects | Standard course format. |
| **Recommendation** | ⚪ **Low priority within Yoav's guide** | Neubig's materials are excellent, but access to this specific course's materials is limited. More efficient to individually search for Neubig's YouTube lectures and other public resources. |

> **Overall Assessment:** Neubig's contribution to NLP education is immense, but the practical inaccessibility of this course's materials from the schedule page is critical. It deviates from Yoav's guide's intent ("direct access to academic materials"), so **priority is low within this guide**.

---

#### 7. Daniel Khashabi — Self-supervised Models (JHU, Spring 2024)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🔵 Good | Official JHU course. 7 weekly assignments + 2 quizzes + final project. PyTorch implementation-focused. |
| **Accessibility** | 🟢 Fully public | [self-supervised.cs.jhu.edu/sp2024/](https://self-supervised.cs.jhu.edu/sp2024/) All assignment outlines public. |
| **Relevance** | 🔵 Basic to intermediate | Assignments 5 (post-training/prompting), 6 (prompt engineering/ICL/RAG), 7 (alignment) are LLM-related. As Yoav notes, it really starts at #12. |
| **Freshness** | 🟡 Spring 2024 | Early 2024. Centered on self-supervised learning fundamentals. |
| **Format** | Lectures + 7 assignments + final project | High assignment quality. PyTorch implementation emphasis. |
| **Recommendation** | ⚪ **For beginners** | Good for those still unsure about Transformers, but basic material is excessive for Yoav's intended audience (assumes Transformers knowledge). **Redundant for learners with implementation experience**. |

> **Overall Assessment:** The most "fundamentals-oriented" course in the guide. As Yoav notes "look at #12 onwards," the first half is already known to LLM learners. A good choice for those wanting to learn self-supervised learning itself (solidify NLP fundamentals).

---

#### 8. Tatsunori Hashimoto & Percy Liang — Language Models from Scratch (Stanford, Spring 2025)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 **Top-tier** | Stanford's strongest combo: Hashimoto (safety/evaluation) + Liang (foundation models overall). **All 5 assignments on GitHub**. |
| **Accessibility** | 🟢 **Very high** | [stanford-cs336.github.io/spring2025/](https://stanford-cs336.github.io/spring2025/) All assignments, schedule public. Assignment code on GitHub. GPU cost guide included. |
| **Relevance** | 🟢 **Deep practical understanding** | Tokenizer implementation→Transformer from scratch→Triton FlashAttention2→Scaling Law→Common Crawl processing→SFT+RL (math reasoning). Truly **building LLMs from zero**. |
| **Freshness** | 🟢 **Latest (Spring 2025)** | Includes Triton kernel implementation, Common Crawl processing. The most practical LLM building course of 2025. |
| **Format** | **Implementation-only (5 assignments, no lectures?)** | Lectures are supplementary; **5 large-scale implementation assignments are the star**. Not a typical "listen to lectures" course. |
| **Recommendation** | 🟢 **Best for those serious about building LLMs** | An unparalleled resource for those who want to "implement every component of an LLM themselves" rather than "using LLMs as black boxes." However, it is **very heavy** (5 units, order of magnitude more code than typical AI classes). |

> **Overall Assessment:** The most "implementation-oriented" course in Yoav's guide. Yoav himself notes he "included it because it covers niche details of LLM training even though it's a technical/ML class." **GPU time is significant** (RunPod H100 at $1.99-2.99/hr recommended), but well worth it. After completing CS336, you'll understand LLM internals like the back of your hand.

---

#### 9. Yejin Choi — NLP: LLM Edition (UW, Winter 2024)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 High | Choi's unique perspective (specialist in reasoning, commonsense knowledge, creativity). |
| **Accessibility** | 🟢 Fully public | Full schedule on Notion page. Assignments on Google Drive/Colab. |
| **Relevance** | 🔵 Limited (latter half) | As Yoav notes, Week 5 onwards (decoding, alignment, safety, creativity) is LLM-specific. First half is NLP fundamentals. |
| **Freshness** | 🟡 Winter 2024 | Jan-Mar 2024. Somewhat dated. |
| **Format** | Lectures + 4 assignments + final project | Standard. High assignment quality. |
| **Recommendation** | 🔵 **For those seeking Choi's perspective** | Choi's unique perspective on **creativity, reasoning, and commonsense knowledge** is unavailable elsewhere. However, first half is mostly known content — focus on Week 5 onwards. |

> **Overall Assessment:** Choi's perspective on **creativity and reasoning** is the highlight. Week 5 onwards on decoding strategies, alignment, and creativity sections cover unique content not found in other courses. However, content is from Winter 2024 and doesn't include post-2025 advances (inference-time compute scaling, RLM, etc.).

---

#### 10. Tal Linzen — Natural Language Understanding (NYU, Spring 2025)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🔵 High | Linzen (leading figure in linguistics × deep learning). |
| **Accessibility** | 🟡 **Google Docs requires access request** | Syllabus published on Google Docs but shows "Request edit access" dialog. Direct access to materials is limited. |
| **Relevance** | 🔵 **Evaluation, interpretability, linguistic perspective** | Specializes in "evaluating LLMs" rather than "building LLMs." Linguistic evaluation, interpretability, heuristics, human comparison. |
| **Freshness** | 🟢 Spring 2025 | Latest. |
| **Format** | Lectures + assignments | Detailed course structure requires syllabus access. |
| **Recommendation** | ⚪ **For those with linguistics background** | For those wanting a **linguistic evaluation/critique** perspective on LLMs. Overspec for engineering-oriented learners. Also has access barriers to materials. |

> **Overall Assessment:** The most "linguistics-oriented" course in this guide. For those wanting deep knowledge of "how to evaluate" rather than "how to build" LLMs. Linzen's perspective is valuable, but **limited material access** and linguistics background prerequisites make this low priority for most learners.

---

### 📋 Seminars / Reading Groups

#### 11. Robin Jia — Science of Large Language Models (USC, Fall 2024)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 High | Unique "role system" (Proposer/Archaeologist/Reviewer/Visionary, etc.) for multi-angle paper analysis. |
| **Accessibility** | 🟢 Fully public | [robinjia.github.io](https://robinjia.github.io/classes/fall2024-csci699.html) Full schedule, paper list. |
| **Relevance** | 🟢 **Excellent reading progression** | As Yoav says: "A reading list organized with nice progression. Wish it were a class instead of a seminar." Three units: Internals → Black-box → External Factors. |
| **Freshness** | 🔵 Fall 2024 | Appropriate. |
| **Format** | Student presentations + role-playing | Requires active participation. For self-study, use as a reading list. |
| **Recommendation** | 🟢 **As a paper reading guide** | **The quality and structure of the reading list stands out.** Even though you can't participate as a class, reading through the paper list alone has great value. The three-category framework (Internal/External/External Factors) is an excellent learning framework. |

> **Overall Assessment:** **While it's a seminar format, the reading list itself is extremely valuable.** Unit 0 (Transformer Review) → Unit 1 (Internals: state tracking, knowledge editing, mechanistic interpretability) → Unit 2 (Black-box: ICL, faithfulness, scaling laws) → Unit 3 (External Factors: data, fine-tuning, tokenization) — an excellent roadmap for doing science on LLMs.

---

#### 12. Danqi Chen — Understanding Large Language Models (Princeton, Fall 2022)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 High (historically) | Cutting-edge for 2022. Covered GPT-3, T5, InstructGPT, Chinchilla, etc. |
| **Accessibility** | 🟢 Fully public | Accessible as archive. |
| **Relevance** | 🟡 **Frozen at 2022** | Yoav himself comments "wish there was a 2025 version." Content from before GPT-4, before Llama, early RLHF/DPO era. |
| **Freshness** | ⚪ **Dated (2022)** | 3+ years old. Completely misses post-2022 LLM advances (Llama 3, ChatGPT, Claude 3+, DeepSeek, R1, GRPO, etc.). |
| **Format** | Seminar (student presentation format) | 2022 edition COS597G. |
| **Recommendation** | ⚪ **For historical understanding** | Historical interest for re-experiencing 2022 LLM understanding. Too old as a 2026 LLM learning starting point. |

> **Overall Assessment:** Interesting as historical context, but as Yoav himself admits wanting "a 2025 version," **cannot be recommended as a primary learning resource in 2026**. Take Danqi Chen's 2024 edition (#3 COS597R) instead.

---

#### 13. Michael Hahn — Aligning Language Models with Human Preferences (Saarland, Summer 2024)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 High | Specialized seminar focused on alignment. Deep dive into RLHF/DPO/Constitutional AI. |
| **Accessibility** | 🟢 Fully public | [lacoco-lab.github.io](https://lacoco-lab.github.io/courses/alignment-2024/) Full schedule, paper list. |
| **Relevance** | 🔵 **Alignment-specific** | RLHF/PPO/DPO/Constitutional AI/self-alignment/safety failures/adversarial attacks. Scope-limited but deep. |
| **Freshness** | 🔵 Summer 2024 | Appropriate. Covers major methods like DPO/Constitutional AI (summer 2024). Doesn't include GRPO. |
| **Format** | Seminar (presentations + papers) | Student presentations + final paper. For self-study, use as paper list. |
| **Recommendation** | 🟢 **For alignment specialization** | An excellent paper list for systematic learning of alignment methods. Covers RLHF→DPO evolution, Constitutional AI, through Sleeper Agents. Scope-limited but deep. |

> **Overall Assessment:** A seminar **specializing** in alignment (RLHF/DPO/safety). Scope is limited but correspondingly deep. A rare resource for systematically digesting alignment papers.

---

#### 14. Tal Linzen — Language Models: Cognitive Plausibility and Sample Efficiency (NYU, Fall 2024)

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🔵 High (niche area) | Evaluates language models from **cognitive science/psycholinguistics** perspective. |
| **Accessibility** | 🟡 **Google Docs requires access request** | Syllabus on Google Docs with access barriers, same as #10. |
| **Relevance** | ⚪ **Niche** | "Cognitive plausibility of LLMs" — comparing human language processing with LLMs. Cognitive science, not engineering. |
| **Freshness** | 🔵 Fall 2024 | Appropriate. |
| **Format** | Seminar | Reading group format. |
| **Recommendation** | ⚪ **For those with linguistics/cognitive science background** | Nearly unnecessary for LLM engineers. For cognitive scientists interested in "how do humans process language vs. how do LLMs process language." |

> **Overall Assessment:** Extremely niche. For those interested in **evaluating LLMs as cognitive science**. The most specialized in Yoav's guide; hard to recommend for general LLM learners.

---

### 🎥 Video Lectures

#### 15. Stanford CS25 — Transformers Invited Talks

| Item | Rating | Notes |
|------|------|------|
| **Quality** | 🟢 High | Stellar speakers including Karpathy (Transformer explanation), Hinton (hierarchical representations), Jason Wei (Chain-of-Thought), Jim Fan (NVIDIA agents), Nathan Lambert (alignment), Douwe Kiela (RAG). |
| **Accessibility** | 🟢 **Best** | All lectures free on YouTube playlists. Linked from site. |
| **Relevance** | 🔵 Complementary | Each session focused on specific topics. Not suitable for systematic learning, but best for hearing leading domain experts. |
| **Freshness** | 🟢 Ongoing through V6 | Continuously updated. |
| **Format** | Invited lectures (YouTube) | 60-90 min each. Passive viewing OK. |
| **Recommendation** | 🟢 **Recommended as complementary for all learners** | Best for "listening to top researchers between reading books." Not systematic enough as main material, but useful for maintaining motivation and gaining overview perspectives. |

> **Overall Assessment:** **The resource with highest complementary value.** CS25 lectures are independent sessions — you can watch only the topics that interest you. Karpathy's Transformer introduction session is especially famous. Use as "breathers" between courses or as deep-dives into specific themes.

---

## 🏆 Recommended Priorities

Suggested order by learner type:

### 🅰️ "I want to use LLMs practically" — Engineers

```
1. #2 CMU LLMs: Methods and Applications (2026) — 🟢 Overview of everything
2. #8 Stanford CS336 Language Models from Scratch — 🟢 Deep understanding through implementation
3. Parallel: #15 CS25 Videos — 🟢 Top researcher talks as breathers
4. #11 Robin Jia Reading List — 🟢 Paper digestion once understanding progresses
↓
→ These 4 provide sufficient "practical understanding" of LLMs
```

### 🅱️ "I want to research LLMs" — Academic-Oriented

```
1. #3 Princeton Deep Dive (#8 as implementation supplement) — 🟢 Paper-based deep understanding
2. #5 Berkeley Foundations and Safety — 🟢 Safety fundamentals
3. #13 Hahn Alignment Seminar — 🟢 Alignment specialization
4. #1 Chiang Theory — 🟢 Understanding theoretical limits (optional)
↓
→ Covers the depth needed for paper writing
```

### 🅲 "I want to think about LLMs and humans" — HCI/Product-Oriented

```
1. #2 CMU LLMs: Methods and Applications — 🟢 Overview of everything
2. #4 Stanford Human-Centered LLMs — 🟢 HCI perspective
3. #5 Berkeley Safety — 🟢 Safety and ethics
4. #9 Yejin Choi — 🟢 Creativity and reasoning (Week 5 onwards)
↓
→ For those involved in human-centered design, products, and policy
```

---

## 🔗 Related Wiki Pages

- [[concepts/llm-course-roadmap]] — Similar knowledge map mapping Maxime Labonne's LLM Course to wiki concepts
- [[entities/yoav-goldberg]] — Creator of this guide
- [[entities/andrej-karpathy]] — CS25 Transformer introduction lecture (#15)
- [[concepts/llm-core]] — LLM foundational concepts
- [[concepts/harness-engineering/agent-engineering-guide-2026]] — Another LLM/AI agent learning guide

---

> **This page is meta-knowledge (a knowledge map).** It evaluates the course materials referenced by Yoav Goldberg's guide and proposes learning priorities. For the actual content of each resource, please refer directly to the linked sources.
