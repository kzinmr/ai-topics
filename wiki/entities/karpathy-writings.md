---
title: "Karpathy Writings & Blog Posts"
tags: [person, writing]
created: 2026-04-27
updated: 2026-05-03
type: entity
---


# Karpathy: Writings & Blog Posts

Back to main profile: [[andrej-karpathy]]

## Bearblog (2024–present)

### I love calculator (Sep 2024)
First bearblog post — sparked a theme of "hygiene" essays. Argues that calculators represent ideal technology: zero dependency footprint, fully self-contained, private, secure, no subscriptions, no tracking. Critiques modern tech drift: *"Why is so much of our technology drifting towards complex, dependency-bloated, user-hostile, anti-pattern-ridden mess?"* Proposes a model where companies optimize shareholder value, leading to hyper-optimized user-hostile practices. Suggests developers should add a "regularizing gradient of ideology" to counter this drift.

### 2025 LLM Year in Review (Dec 2025)
Comprehensive assessment of LLM progress in 2025. Analysis of model capabilities, limitations, and trajectory. Highlights the phase shift from manual coding to AI agent-assisted development.

### Chemical hygiene (Dec 2025)
Systematic approach to managing chemical/biological safety in daily life. **Core mantra:** Keep your home unsophisticated. Filter water & air. Eat real food with short supply chains. Surround yourself with natural/inert materials. Avoid plastics (especially heated/frozen). Covers water filtration, air quality, food choices, natural vs synthetic fabrics, cleaning products, and annual health testing.

### Auto-grading decade-old Hacker News discussions with hindsight (Dec 2025)
Uses LLMs to evaluate old HN discussions with the benefit of hindsight. Tests predictive accuracy of past comments. Demonstrates practical application of LLMs for retrospective analysis.

### The space of minds (Nov 2025)
Philosophical reflection on the diversity of possible intelligences. Questions whether current LLMs occupy a narrow or broad region of possible "minds". Explores the concept of intelligence diversity.

### Verifiability (Nov 2025)
Explores the fundamental importance of verifiability in AI systems. Argues that the ability to verify outputs is more important than raw capability. Without verification, higher capability is just more confident wrongness. Applies to coding agents, research agents, and all AI systems.

### Animals vs Ghosts (Oct 2025)
Conceptual framework for thinking about AI behavior. Contrasts reactive, stimulus-driven behavior (animals) with generative, imagination-driven behavior (ghosts). Provides a lens for understanding different AI capabilities and limitations.

### Vibe coding MenuGen (Apr 2025)
Origin of the term **"vibe coding"**. A detailed post-mortem of building **MenuGen** (menugen.app) -- a production app that photographs restaurant menus, OCRs them, and generates AI images for every dish -- 100% via Cursor + Claude 3.7. Karpathy acted as "vibe coder" providing high-level direction without writing code directly. The app is a real product with authentication (Clerk), payments (Stripe), and a "good and honest 10% markup" on API costs.

**Key insights from the post-mortem:**

| Insight | Detail |
|---------|--------|
| **80/20 Trap** | Local prototype was fast, but deploying a real app was a "painful slog." Felt 80% done but was closer to 20% |
| **API Hallucination** | OpenAI OCR - LLM hallucinated deprecated APIs; Replicate - heavy rate limiting + out-of-date docs |
| **Vercel Debugging** | Required "pushing fake debugging commits" to force redeploys |
| **Clerk Auth** | Claude hallucinated ~1000 lines of deprecated code; needed custom domain, DNS, Google Cloud Console OAuth config |
| **Stripe Logic Error** | Claude initially matched payments to users via email (wrong - Stripe email does not equal Google OAuth email). Karpathy caught it |
| **LLM Gaslighting** | When corrected, LLM "thanks me... and tells me it will do it correctly in the future, which I know is just gaslighting" |
| **No State** | Skipped database (Supabase) and queues (Upstash) as "too much bear" - app prone to timeouts |

**Four recommendations** for the vibe coding era:
1. **Batteries-Included Platforms** -- "opposite of Vercel Marketplace" that pre-configures domain, auth, payments, DB
2. **LLM-Friendly Services** -- docs in Markdown, configs via CLI/curl, not web UIs: "Don't talk to a developer... Instruct and empower their LLM"
3. **Simpler Stacks** -- Considering HTML/CSS/JS + Python FastAPI over "serverless multiverse"
4. **Apps as Prompts** -- Questioning if apps should be standalone products or "Artifacts" generated on-the-fly

**Conclusion:** Barrier to app creation dropping to ~zero; anyone can create custom automations as easily as making a TikTok.

### Power to the people: How LLMs flip the script on technology diffusion (Apr 2025)
Argues that LLMs dramatically accelerate the spread of technical capabilities. Previously, expertise was the bottleneck; now it's access and judgment. Democratizing effect on software development.

### Finding the Best Sleep Tracker (Mar 2025)
2-month comparative analysis of 4 trackers (Oura, Whoop, 8Sleep Pod 4 Ultra, Apple Watch + AutoSleep). **Key findings:** Oura & Whoop are Tier 1; 8Sleep is Tier 2; Apple Watch + AutoSleep is "terrible". Sleep score correlations provided. Focus on reducing accumulated sleep debt.

### The append-and-review note (Mar 2025)
Single text note system in Apple Notes — no folders, no tagging, just CTRL+F. Append ideas at top, periodically review and rescue important items. Philosophy: *"When I note something down, I feel that I can immediately move on, wipe my working memory, and focus fully on something else at that time."*

### Digital hygiene (Mar 2025)
Systematic approach to digital security: 1Password + YubiKey + Brave + Signal + privacy.com + FileVault + NextDNS. Guiding principle: *"I wish to pay for the software I use so that incentives are aligned and so that I am the customer."* Covers authentication, browsing, email hygiene, financial privacy, device security.

## Older Blogs (karpathy.github.io)

### Software 2.0 (Nov 2017)
**Seminal essay** arguing that neural networks are the new "software" — a paradigm shift where we stop writing explicit rules and start specifying objective functions. *"The most important consequence of Software 2.0 is that it requires a fundamentally different approach to programming and debugging."* Direct precursor to vibe coding.

### A Recipe for Training Neural Networks (Apr 2019)
Essential reading for ML practitioners. Key principles: (1) Start simple and overfit a single batch, (2) Monitor loss curves religiously, (3) Use data augmentation early, (4) Optimize learning rate before architecture, (5) Debug by visualization, not reading code.

### A from-scratch tour of Bitcoin in Python (Mar 2021)
Complete implementation of Bitcoin transaction creation, signing, and broadcasting. **Zero dependencies** — demonstrates philosophy of understanding systems at their lowest level.

### A Survival Guide to a PhD (Sep 2016)
Practical advice on advisor relationships, research productivity, mental health, and time management. Influenced many graduate students in AI/ML fields.

### Deep Reinforcement Learning: Pong from Pixels (2016)
Tutorial on building a neural network to play Atari Pong from raw pixels. Introduced policy gradients to a wide audience. Key insight: RL is just gradient descent on a differentiable loss function.

### The Unreasonable Effectiveness of Recurrent Neural Networks (2015)
**Landmark blog post** demonstrating character-level RNNs generating text, LaTeX, and code. One of the most shared AI blog posts of 2015. *"RNNs are not just models — they're little universes that learn to simulate the world."*

### What a Deep Neural Network thinks about your #selfie (2015)
Fun demo training a CNN to classify selfies as good/bad. Scraped 2 million selfies for training data. Showed commitment to accessible, visual AI education.

### Biohacking Lite (2019)
Personal experimentation with energy metabolism, sleep, and nutrition. Applying systematic, data-driven approach to personal health.

### Feature Learning Escapades (2014)
Reflections on unsupervised feature learning. Early thinking on representation learning, later central to LLMs.

### Quantifying Productivity (2014)
Pet project tracking active windows and keystrokes. *"What gets measured gets managed"* — but measurement itself changes behavior. Precursor to Digital Hygiene.

### The state of Computer Vision and AI: we are really, really far away (2014)
Skeptical take on AI progress. Anticipated limitations of modern LLMs (hallucination, lack of reasoning, brittleness). Shows balanced, non-hype approach.

### Breaking Linear Classifiers on ImageNet (2014)
Demonstrated adversarial examples are not a deep learning problem but a fundamental property of high-dimensional spaces. Contributed to adversarial ML field.

### What I learned from competing against a ConvNet on ImageNet (2014)
Human vs. AI comparison: manually classified ImageNet images. Result: Human ~94%, ConvNet ~93%. *"Humans are quite good at image classification — but slow and expensive."*

### Quantifying Hacker News with 50 days of data (2013)
Scraped HN every minute for 50 days. Found timing and topic matter more than quality for HN success.

### Visualizing Top Tweeps with t-SNE, in Javascript (2013)
Open-sourced tsnejs — one of the first browser-based t-SNE implementations. Made high-dimensional visualization accessible.

### Lessons learned from manually classifying CIFAR-10 (2013)
Human baseline study: manually classified CIFAR-10 images. Result: ~94% accuracy. Provided context for evaluating machine vision progress.

### Chrome Extension Programming (2012)
Tutorial on Chrome extension programming using Twitter as case study. Demonstrated practical web development skills.

### Short Story on AI: A Cognitive Discontinuity (2016)
Creative fiction exploring AI themes. Accessible, non-technical exploration of the gap between current AI and AGI.

### Short Story on AI: Forward Pass (2017)
Fiction: existential crisis under the hood of a neural network's forward pass. Explores what it "feels like" to be a neural network processing data. One of the few creative writing pieces by a major AI researcher.
