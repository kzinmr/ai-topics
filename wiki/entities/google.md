---
title: "Google (AI/ML)"
type: entity
created: 2026-04-25
updated: 2026-05-25
tags: [company, lab, product, platform, infrastructure]
aliases: ["Google DeepMind", "Google Research"]
sources: [
  raw/articles/theverge.com--tech-933415-google-io-2026-biggest-announcements-ai-gemini--e73abf5d.md,
  raw/articles/simonwillison.net--2026-may-20-google-io--933c8dde.md,
  raw/newsletters/2026-05-17-anthropic-pulls-away-openai-strikes-back-and-google-s-gemini-rising.md,
  raw/newsletters/2026-04-24-chatgpt-images-2-0-is-genuinely-fantastic.md,
  raw/newsletters/2026-05-03-gemini-gets-to-work-claude-s-big-pull-and-openai-unchained.md,
  raw/articles/2025-12-10_google-cloud_alphaevolve.md,
  raw/newsletters/2026-05-20-ainews-google-i-o-2026-gemini-3-5-flash-omni-nanobanana-for-video-spark-backgrou.md,
  raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
]
---
# Google (AI/ML)

| | |
|---|---|
| **Type** | AI Research & Product Company |
| **Key Labs** | Google DeepMind, Google Research |
| **Key Products** | Gemini models, Google AI Studio, Claude (via partnership), Pixel phones |
| **Website** | [deepmind.google](https://deepmind.google), [ai.google.dev](https://ai.google.dev) |

## Overview

Google is a major player in AI/ML with extensive research through Google DeepMind and Google Research. Their AI strategy centers on the Gemini multimodal model family and Google AI Studio as a development platform.

## Key AI Products

### Gemini
- Google's multimodal model family (Gemini 1.5, Gemini 2.0, Gemini 3.1 Pro/Flash)
- Handles text, images, audio, video as input/output
- Powers Google's consumer AI products (Gemini App, Google Workspace AI features)
- Last frontier model: **Gemini 3.1 Pro** (Feb 2026); estimated 7–9 months behind Anthropic/OpenAI in model velocity

### Gemini File Generation (May 2026)

Gemini now supports direct file generation and export in-chat:
- **Output Formats**: Docs, Sheets, Slides, PDF, `.docx`, `.xlsx`, `.csv`, Markdown
- No native PowerPoint export at launch
- **Switching Tools**: Users can import full chat histories from ChatGPT via ZIP exports or copy-paste memory summaries
- **UK Memories**: Cross-chat memory features launched in UK to meet regulatory standards
- Viewed as catch-up functionality vs. competitors

### AI Compute Dominance

Google's hardware infrastructure advantage (May 2026):
- Controls ~**25% of global AI compute**
- **3.8 million TPUs** + **1.3 million GPUs**
- Google Cloud grew 63% last quarter ($20B); Azure 40%; AWS 28%
- Alphabet 2026 capex guidance: **$180–190 billion**
- Alexis Ohanian quote: Google's compute advantage is a long-term strategic moat

### Google AI Studio
- Platform for experimenting with Gemini models
- Primary access point for **Nano Banana 2** image generation
- Offers resolution control (512px–4K) and broad aspect ratio options

### Nano Banana 2 (NB2)
- Google's image generation model via AI Studio
- Fast generation: 20–25 seconds
- Strong resolution and aspect ratio controls
- Weaker in iteration control (natural language only) and output quality vs. OpenAI's GPT Image 2

### Gemini App
- Mobile application providing Gemini-powered features
- Includes image generation capabilities
- Loses aspect-ratio control compared to AI Studio
- Adds watermark in bottom-right corner


### Gemini Intelligence — Android Agentic AI (May 2026)

Google is building **Gemini Intelligence**, an agentic AI layer on Android that can execute multi-step tasks across apps:

- **Cross-app workflows**: Generate event flyers → search Expedia → book travel — without manual app switching
- **Deployment**: Rolling out to Pixel and Samsung Galaxy devices in summer 2026
- **Positioning**: Android's answer to Apple Intelligence; leverages Gemini's on-device and cloud capabilities
- **Significance**: Positions Google as a platform-level AI agent provider, competing with assistants from OpenAI and Anthropic

### Magic Pointer — AI-Enabled Cursor (May 2026)

Google DeepMind's experimental reimagining of the mouse pointer for the AI era, powered by Gemini:

- **Four design principles**: Maintain the flow, Show and tell, Embrace "this" and "that", Turn pixels into actionable entities
- **Use cases**: Point at PDF → get summary → paste into email; hover over table → request chart; select products → compare
- **Integration**: Rolling out in Chrome (Gemini in Chrome) and Googlebook laptop
- **Philosophy**: AI that adapts to human behavior rather than forcing users into separate AI windows
- Available to try in Google AI Studio

### Project Suncatcher — Space-Based AI Infrastructure

Google is in discussions with SpaceX about **Project Suncatcher**, a concept for low-Earth orbit data centers:

- **Target**: Early 2027 launch
- **Advantage**: Orbital solar power is ~8× more efficient than ground-based solar
- **Rationale**: Break through terrestrial compute constraints by leveraging SpaceX's launch capacity
- **Related**: SpaceX holds a $60B option to acquire Cursor (see [[entities/openai]])



### Google I/O 2026 — Product Launches (May 2026)

Google's I/O 2026 keynote covered a broad range of AI product announcements beyond the core model releases. Key launches:

| Product | Description | Launch |
|---------|-------------|--------|
| **Gemini 3.5 Flash** | New default model: faster, improved agentic coding, richer web UIs, better guardrails. | Now default in Gemini app & AI Mode in Search |
| **Gemini 3.5 Pro** | Larger variant following 3.5 Flash | Next month (June 2026) |
| **Gemini Omni** | New model family: Omni Flash generates video from text/photos/video/audio. | Rolling out in Gemini app, Flow, YouTube Shorts |
| **Gemini Spark** | Always-on personal AI agent. Runs 24/7 on ephemeral GCP VMs. Connects to Workspace + third-party apps (Canva, Instacart). | Coming soon |
| **Antigravity CLI** | Closed-source Go-based CLI replacing open-source Gemini CLI (June 18 sunset) | Available now |
| **Neural Expressive Redesign** | Gemini app redesign: new animations, color palette, font, haptic feedback | May 19 (web, iOS, Android) |
| **Universal Cart** | Cross-merchant intelligent shopping cart: add from YouTube/Search/Gemini/Gmail, checkout across merchants (Nike, Target, Walmart, Ulta, Sephora, Wayfair, Shopify) | Summer 2026 |
| **Gmail Live** | Voice-driven search for inbox: extract info from emails via natural language queries | Beta |
| **Pics App** | AI image editing via click+comment (Nano Banana 2 + Gemini). Iterative edits without full prompts | New |
| **Vibe-Coding Android Apps** | Build native Android apps from AI Studio → publish to Play Store. Embedded emulator, Firebase integrations. | Beta |
| **Project Aura v2** | Updated smart glasses (Xreal collab): redesigned puck, fingerprint sensor, widgets, Gemini calendar/Keep integration. Warby Parker & Gentle Monster audio-only glasses this fall | Fall 2026 |
| **Search Information Agents** | AI agents that monitor topics and deliver summarized updates from blogs/news/social | Summer 2026 (AI Pro/Ultra) |
| **Generative UI & Mini Apps** | Search generates interactive simulations, graphs, and custom mini-apps for repeated tasks | Summer 2026 |
| **AI Ultra Pricing** | New tiers: $100/mo (standard) and $200/mo (includes Project Genie) | Now |
| **SynthID in Chrome** | AI detection tools: right-click images in Chrome to see provenance via SynthID + C2PA | Expanding |
| **Beam/Sophie** | Lifelike AI video agents for meetings: Sophie reads documents, handles restaurant recs, group calls via Meet/Zoom | Experimental |


## Image Generation Strategy

Google's approach to AI image generation:
- **NB2 via AI Studio**: Fast, resolution-flexible, but quality-limited
- **Gemini App**: Mobile convenience with reduced controls
- Competes with OpenAI's GPT Image 2, which reviewers report produces superior professional output despite slower generation

### Gemini App (macOS)
- Native desktop application for macOS 15+
- Option + Space shortcut for instant AI access
- Screen sharing for context-specific help
- Local file analysis capabilities

### Gemini 3.1 Flash TTS
- Text-to-speech model integrated into Gemini ecosystem

### Google AI Plans
- Tiered AI subscription plans with cloud storage integration
- Enables persistent storage of AI-generated content

### TPU v8 "Ironwood" — AI Chip Independence (Apr 2026)

Google announced its 8th-generation TPU, codenamed **Ironwood**, marking a strategic shift toward AI hardware independence from NVIDIA:

- **Ironwood TPU v8**: 456 TOPS peak compute for AI inference, significantly outperforms v7
- **Split architecture**: Google is separating inference-focused chips (8i) from training-focused chips (8t)
- **8i (Inference)**: Optimized for low-latency serving, edge deployment, and on-device AI
- **8t (Training)**: Optimized for large-scale model training with higher memory bandwidth
- **Goal**: Reduce reliance on NVIDIA GPUs for both training and inference workloads
- **Impact**: Enables Google to vertically integrate its AI stack — from models (Gemini) to hardware (TPUs) to deployment (Google Cloud)

This aligns with Google's broader strategy of "100% local browser agent" using Gemma 4 + WebGPU for edge inference, demonstrating a full-stack approach from silicon to application.

## AlphaEvolve (May 2026)

AlphaEvolve, Google DeepMind's Gemini-powered evolutionary coding agent, has moved from experimental to production use:

- Optimizing **next-generation TPU design** — first Gemini contribution to TPU arithmetic circuits
- **Data center scheduling**: Recovering 0.7% of global compute resources
- **Gemini training**: 23% kernel speedup → 1% total training time reduction
- Available on Google Cloud in private preview since Dec 2025
- See [[concepts/alphaevolve]] for full details



### Google I/O 2026: Gemini Platform Expansion (May 2026)

At Google I/O 2026, Google announced a major expansion of the Gemini platform, positioning it as both a consumer AI surface and a developer/agent platform:

#### Gemini 3.5 Flash (GA)
- Now **generally available** — strongest agentic/coding model from Google yet
- **Terminal-Bench 2.0**: 76.2%
- **MMMU-Pro**: 84%
- Default model in Gemini app and AI Mode in Search globally
- Released alongside significant updates to the broader platform

#### Gemini Omni (Multimodal Generation)
- Multimodal generation/editing starting with video
- Builds on NanoBanana for video — native video understanding and generation
- Positioned as Google's answer to GPT-5.5's multistep reasoning

#### Antigravity 2.0 (Agent OS)
- Full agent stack: **Desktop / CLI / SDK / API**
- Sub-agent parallel execution — agents spawning and coordinating sub-agents
- Live demo: **93 sub-agents** collaborating to build an entire operating system
- Represents Google's platform-level answer to Codex, Claude Code, and Cursor

#### Spark — 24/7 Personal AI Agent
- Personal AI agent running on cloud VMs
- Persistent, always-on — works on tasks continuously
- Available through Google Cloud for consumer and developer use cases

#### Infrastructure Scale
- **3.2 quadrillion tokens/month** processed (7× year-over-year growth)
- **900M+ monthly active users** on Gemini app
- Google's AI compute: ~25% of global AI compute capacity



### SynthID — Industry-Wide Provenance Standard (May 2026)

Google's **SynthID** watermarking technology for AI-generated content was adopted by OpenAI, Nvidia, and other major AI companies, moving from a single-lab trust feature toward an **industry-wide provenance layer**:

| Aspect | Detail |
|--------|--------|
| **Technology** | Invisible watermarking for AI-generated images, audio, and text |
| **Adopters** | OpenAI, Nvidia, and others |
| **Significance** | Provenance moves from one lab's trust feature to a wider ecosystem layer |
| **Context** | Display-based disclosure (labels, tags) cannot keep pace with generative media volume — SynthID provides machine-readable provenance |
| **Announced at** | Google I/O 2026 |

**Implications**:
- **Standardization pressure**: With OpenAI and Nvidia adopting, SynthID has critical mass to become a de facto standard
- **Regulatory alignment**: Watermarking requirements in the EU AI Act and potential US regulation make SynthID's ecosystem adoption strategically important
- **Platform accountability**: Machine-readable provenance enables automated content moderation and attribution at scale

Source: Superintel Google I/O 2026 newsletter (May 2026)

### Significance

This positions Google as having re-entered the frontier model race after a period of lagging behind OpenAI and Anthropic. The combination of Gemini 3.5 Flash for performance, Omni for multimodal, Antigravity 2.0 for multi-agent orchestration, and Spark for persistent agents creates a full-stack AI platform that competes with both consumer (ChatGPT) and developer (Codex/Symphony) offerings from competitors.

## Gemini Enterprise Agent Platform

Googleは企業向けAgentプラットフォームとして、エージェントの構築・スケーリング・ガバナンス・最適化を包括的に提供する戦略を打ち出している。

### コアコンポーネント

| コンポーネント | 役割 |
|---|---|
| **Agent Identity** | エージェントの認証・認可・アイデンティティ管理 |
| **Agent Registry** | エージェントの登録・発見・バージョン管理 |
| **Agent Gateway** | エージェント間通信・APIゲートウェイ・トラフィック制御 |
| **Simulation** | エージェントの本番前テスト・シミュレーション環境 |
| **Evaluation** | エージェントの品質評価・パフォーマンス計測 |
| **Observability** | エージェントの監視・ロギング・トレーシング |

このコンポーネント群は、Googleを「**Agent Control Plane（エージェント制御層）**」モデルへとポジショニングするものであり、単なるモデル提供者からエンタープライズAgentインフラ全体を掌握するプラットフォーマーへの進化を示している。

### FDE（Forward Deployed Engineer）戦略

Google Cloudは**Forward Deployed Engineers（FDE）**を活用し、システムインテグレーター（SI）と連携しながら、エンタープライズ顧客の深い技術的課題を解決するアプローチを取っている。

- FDEはSIとパートナーシップを組み、顧客固有のニーズに対応
- 単なるSaaS提供ではなく、現場密着型のエンジニアリングサービスを併用
- これにより、汎用プラットフォームではカバーしきれないエンタープライズの個別要件に対応

### 戦略的ポジション

Googleは以下の**二正面戦略**を展開している：

1. **Agentガバナンス層の構築**: Agent Identity、Registry、Gatewayなどを通じて、企業がエージェントを安全に管理・運用するためのコントロールプレーンを提供
2. **FDEによる現場密着サービス**: SIとの連携を通じて、企業固有の課題に対する深い技術支援を提供

この「プラットフォーム＋FDE」の組み合わせは、**OpenAI**や**Anthropic**と同様のデュアルアプローチであり、モデル性能競争からエンタープライズAgent運用インフラの覇権争いへと競争軸がシフトしていることを示している。

## Relationships
- [[concepts/gemini]] — Google's multimodal model family (detailed entity)
- [[concepts/nano-banana-2]] — Google's NB2 image generation model
- [[concepts/alphaevolve]] — Evolutionary coding agent for algorithm discovery
- [[entities/openai]] — Primary competitor in AI/ML
- [[concepts/chatgpt-images-2.0]] — OpenAI's GPT Image 2

## Sources
- [Google: The Gemini app is now on Mac](https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-mac-os/) (2026-04-22) — macOS desktop app announcement
- [Google: New text-to-speech AI model](https://blog.google/technology/ai/google-gemini-text-to-speech-ai-model-2026/) — TTS model release
- [Google AI Plans with Cloud Storage](https://substack.com/redirect/07e1d369-9cdd-4737-821a-62accd29792c?j=eyJ1Ij...tf6E) — AI subscription plans
- [Alex Banks, The Signal: "ChatGPT Images 2.0 is genuinely fantastic"](https://thesignal.substack.com/p/chatgpt-images-20-is-genuinely-fantastic) (2026-04-24) — comparative analysis with GPT Image 2

## References

- 2039737982576636294_Googles-20-Year-Secret-Is-Now-Available-to-Every-Enterprise
- mail-settings.google.com--mail-uf-5bangjdj-mpdsvrpq2o-bxft2lknzyiqqd9nnux04-g55ecqbaig--00d2671a
- mail-settings.google.com--mail-uf-5bangjdj-tz1kqisscqea7p2h9ohaeqo8bviifbgqv5v-quhnr7---e2e5f3d8
- mail-settings.google.com--mail-uf-5bangjdj8p9wtaapz-g3xoovf0gpcffbvjfi0zga5n6mwor-kpxq--666ea53c
- mail-settings.google.com--mail-uf-5bangjdj9qifvdd8v-t4nci-qckrry3ycuzn3qmn7bghamsn0w-8--0769be32

- 2043609541477044439_Google-Engineer-Automated-80-of-Work-with-Claude-Code
- blog.google--innovation-and-ai-technology-developers-tools-gemma-4--9648c97b
