---
title: SynthID
created: 2026-05-27
updated: 2026-07-06
type: concept
tags:
  - concept
  - google
  - agent-safety
  - content-quality
  - ethics
  - governance
  - model
  - inference
sources:
  - raw/articles/2026-05-27_google-synthid-c2pa-expansion.md
  - raw/articles/2026-05-27_synthid-openai-elevenlabs-nvidia-kakao.md
  - raw/articles/2026-05-27_heise-uniform-ai-labeling-synthid.md
  - raw/articles/seangoedecke.com--text-ai-watermarks--cd663c94.md
  - raw/articles/seangoedecke.com--c2pa-only-works-if-everything-is-signed--ae4eb8f4.md
---

# SynthID

## Overview

SynthID is Google DeepMind's digital watermarking technology that embeds imperceptible, robust signals into AI-generated content — images, video, audio, and text — enabling verification of origin without degrading quality. Introduced in 2023 within Google's Gemini AI app, SynthID became a **cross-industry standard at Google I/O 2026** (May 19) when OpenAI, Kakao, ElevenLabs, and NVIDIA adopted the technology, creating the largest content-provenance coalition in AI history.

SynthID is designed to survive common transformations — cropping, color adjustment, JPEG compression, screenshots, social media re-sharing, and re-encoding — properties that metadata-only approaches (like EXIF tags) cannot provide alone. It is complementary to the **C2PA Content Credentials** standard (an open metadata specification from the Coalition for Content Provenance and Authenticity), and Google integrates both into its verification pipeline.

As of May 2026, over **100 billion images and videos** and **60,000 years of audio** have been watermarked using SynthID, and verification has been used **50 million times** globally via the Gemini app.

## How SynthID Works

SynthID operates differently depending on the content type:

| Content Type | Technical Approach | Survives Editing? | Open-Sourced? |
|---|---|---|---|
| **Images** | Imperceptible pixel-level pattern embedded during generation | Yes — survives crops, filters, compression | No (proprietary) |
| **Video** | Frame-level watermark embedded in generated video streams | Yes — survives re-encoding, resizing | No |
| **Audio** | Inaudible signal embedded in waveform during generation | Yes — survives compression, re-recording | No |
| **Text** | Adjusts token probability distribution during generation; detectable by a verification model that knows the bias pattern | N/A (text is the watermark) | **Yes** — open-sourced at I/O 2026 |

### SynthID + C2PA: The Dual-Layer Approach

SynthID and C2PA serve complementary roles:

- **SynthID**: An invisible watermark "burned into" the medium at the signal level. Tells you **whether** content is AI-generated, even when all metadata is stripped.
- **C2PA Content Credentials**: Cryptographically signed metadata that records **who** created the content, **when**, **where**, and **with what tools**. Records the full edit history (camera origin → AI edits → final output).

Together, they enable a verification chain: if metadata is stripped during upload, the surviving SynthID watermark can still identify content as AI-generated and potentially reconnect it to its original C2PA credentials. The industry vision is that **content without metadata or watermarks should be considered suspicious**.

### C2PAの限界と批判 — Sean Goedeckeの分析

Sean Goedeckeの「[C2PA only works if everything is signed](https://seangoedecke.com/c2pa-only-works-if-everything-is-signed/)」(2026年7月)は、C2PAのPKIベース署名方式の本質的な限界と採用障壁を詳述する。SynthIDページの「SynthID + C2PA: The Dual-Layer Approach」節はC2PAをSynthIDの補完技術として紹介するが、Goedeckeの分析は以下の批判的観点を追加する:

**1. 全画像署名のCatch-22（採用の矛盾）:**
C2PAが有効に機能するには、すべての画像（AI生成・人間撮影の両方）が署名されている必要がある。しかし現状、AI生成画像の大半がC2PA署名されている一方、人間撮影画像の署名率は極めて低い（Google Pixel 10のみがデフォルト署名対応、iPhoneは非対応）。FotoForensicsのデータでは週に約12件のC2PA署名画像が検出されるが、これは年間90万件処理中の約600件に過ぎない。この非対称性により、AI画像を「人間撮影」と偽装するには単に署名を削除すればよい — C2PAは**署名がないことの異常性**に依存するが、その異常性は実現していない。

**2. SNS保存時のManifest除去問題:**
C2PAメタデータはファイルに数十〜数百KBのオーバーヘッドを追加する。Facebook Messenger等のSNSに画像をアップロードして再ダウンロードすると、C2PA manifestが剥離される。これを防ぐには全SNS企業が画像再エンコード処理を更新する必要があり、大規模な規制と業界調整が必要。

**3. 26証明書のTrust List制限:**
C2PAのバリデータは、公式C2PA trust listに登録された証明書チェーン（現在26証明書のみ）に基づいて検証する。新規参加者は承認プロセスを経る必要があり、採用の障壁となる。一方、自己署名証明書での署名はバリデータによって拒否される。

**4. キー管理問題:**
ChatGPT等のオンラインツールはサーバー側で署名できるが、Photoshop/Excel/Word等のオフラインツールではローカル鍵が必要となる。ローカル鍵の抽出防止と、オフライン環境での署名の両立は未解決。

**5. 安全劇場（Safety Theater）リスク:**
C2PAの現状の採用率では実質的な識別機能を提供できないが、企業は「AI安全性に取り組んでいる」シグナルとしてC2PA対応を宣伝するインセンティブを持つ。Goedeckeは「技術的に理解のない層に対しては説得力のあるピッチ」と指摘し、実際の効果以上に投資が集まるリスクを警告。

**6. 非画像コンテンツへの適用困難:**
画像以外のファイル形式（Excel、PDF等）ではC2PAメタデータをsidecarファイルに格納する必要があり、テキストのコピーペーストによる署名バイパスが容易。チャットツールやエージェント出力は非コンテナ化プレーンテキストであり、C2PAの適用外。

**評価**: Goedeckeの分析はC2PAの長期的な可能性を否定するものではないが、SynthIDがカバーする信号レベルの透かしと異なり、C2PAのメタデータベースのアプローチは**エコシステム全体の協調**（全カメラ・全SNS・全クリエイティブツールの参加）が必要であることを示す。SynthID + C2PAの二層戦略は補完的であるが、C2PA層の現実的な効果はecosystem adoptionに完全に依存し、短期的には安全劇場のリスクが高い。この批判的分析は「SynthID + C2PA: The Dual-Layer Approach」節の楽観的記述に対する重要なカウンターウェイトとなる。→ [[entities/seangoedecke-com]]

## Cross-Industry Adoption

At Google I/O 2026, Sundar Pichai announced a landmark coalition adopting SynthID:

| Company | Content Type | SynthID Scope | Implementation Timeline |
|---|---|---|---|
| **Google** (Gemini, Imagen, Veo, Omni) | Images, video, audio, text | Full — all generative AI outputs | Existing; expanding with I/O 2026 |
| **OpenAI** (ChatGPT, Codex, API) | AI-generated images | Starting with ChatGPT, Codex, API images | Announced at I/O 2026 — rolling out immediately |
| **ElevenLabs** | AI-generated audio | Audio content watermarking | Announced at I/O 2026 |
| **NVIDIA** | AI-generated video (Cosmos models) | Cosmos world foundation model video outputs | Partnership announced 2025 |
| **Kakao** | AI-generated images/video (Kanana model) | Kanana-Kollage (image), Kanana-Kinema (video) | H2 2026 — first Asian adopter |
| **Meta** (Instagram) | Camera-captured media | C2PA Content Credentials (complementary, not SynthID) | Announced at I/O 2026 |

> "Nvidia signed on to SynthID last year. And today, we are thrilled to announce that OpenAI, Kakao and ElevenLabs are adopting SynthID, too. It's great to see the cross-industry collaboration. We're looking forward to expanding to more partners and setting the standard of transparency for the AI era." — **Sundar Pichai**, Google I/O 2026

### OpenAI's Pivotal Adoption

OpenAI adopting Google's proprietary watermarking standard — rather than developing its own or using only the vendor-neutral C2PA — signals that content provenance is a domain where **cooperation serves everyone's interests better than competition**. OpenAI begins SynthID integration immediately with images from **ChatGPT, Codex, and the OpenAI API**. A separate OpenAI verification page is planned, initially for OpenAI content, later for multi-provider detection.

### Kakao: First Asian Adopter

Kakao became the **first company in Asia** to adopt SynthID, applying it to its proprietary AI model **Kanana**. Beginning in H2 2026, invisible watermarks will be embedded into KakaoTalk's Kanana Template feature (AI-generated short videos) and Kanana-Kollage/Kanana-Kinema models. Kakao's AI Safety Leader Kim Kyunghoon framed this as proactive action "beyond legal obligations" ahead of South Korea's AI Basic Act and AI-generated content labeling system.

### Open-Sourcing Text Watermarking

Google open-sourced SynthID's text watermarking technology at I/O 2026, making it available to any developer without using Google's proprietary systems. This creates a potential de facto standard for AI text provenance without formal legislation, with applications in academic integrity, journalism, and regulatory compliance.

## Integration Across Google Products

SynthID verification is being deeply integrated into Google's ecosystem:

| Product | SynthID Capability | Status |
|---|---|---|
| **Gemini App** | Image, video, audio verification | Available now; 50M+ uses globally |
| **Google Search** (Lens, AI Mode, Circle to Search) | Image verification | Rolling out now |
| **Chrome** | Right-click image verification via Gemini | Coming in "coming weeks" |
| **C2PA Content Credentials** | Unified SynthID + C2PA verification in Gemini | Rolling out now; Search/Chrome in "coming months" |
| **Pixel Devices** | Content Credentials for native camera (Pixel 10), expanding to video on Pixel 8-10 | Rolling out |
| **Google Cloud** | AI Content Detection API for enterprises | Launching with trusted partners |
| **YouTube** | AI-generated content labels | Existing |

### How Users Verify

Users can check content provenance through natural-language queries:
- Use **Circle to Search** on Android or **right-click** in Chrome
- Ask: *"Is this made with AI?"* or *"Is this AI generated?"*
- Gemini surfaces both SynthID watermarks **and** C2PA Content Credentials metadata in a unified response

Note: Google has **shut down its registration-free verification portal** — verification now requires a Google account, effectively funneling users into Google's ecosystem. This trade-off (mandatory login for richer metadata) has drawn some criticism.

### Enterprise AI Content Detection API

Google launched an **AI Content Detection API** on Google Cloud's Gemini Enterprise Agent Platform, enabling businesses to identify AI-generated media from both Google and other popular models. Use cases include backend operations (sorting feeds, preventing insurance fraud) and user-facing content (fact-checking, labeling synthetic media).

## Scale: 100B+ Watermarked

SynthID's operational scale as of May 2026:
- **100+ billion images and videos** watermarked
- **60,000 years of AI-generated audio** processed
- **50 million verification uses** globally through the Gemini app
- Integrated into all major Google generative AI models: Gemini, Imagen, Veo, Omni

## Strategic Significance

### From Proprietary Tool to Industry Standard

SynthID's trajectory — from a Google-internal tool (2023) to a cross-industry standard with OpenAI, Kakao, ElevenLabs, and NVIDIA onboard (2026) — represents one of the fastest cases of an AI governance technology achieving broad adoption. Key enablers:

1. **Shared problem**: AI-generated misinformation affects all platforms equally; verification is a public good, not a competitive advantage.
2. **Regulatory alignment**: The **EU AI Act** (effective August 2026) mandates clear marking of AI content with penalties up to €15M or 3% of annual revenue. SynthID adoption helps companies demonstrate compliance.
3. **Complementary to C2PA**: SynthID provides the robust signal layer; C2PA provides the structured metadata layer. Together they offer a more complete solution than either alone.

### Open Questions

Despite the momentum, significant challenges remain:

- **Not universal**: SynthID only works for content from participating providers. Independently generated AI content (local models, open-source models without integration) will not carry watermarks.
- **Detection asymmetry**: Adversaries can use non-watermarked models, or attempt to strip watermarks from generated content. Watermark robustness is an arms race.
- **Platform lock-in risk**: Google's shutdown of the registration-free portal means users must use Google services to verify Google-generated content — a tension between accessibility and ecosystem control.
- **Text watermarking adoption**: Open-sourcing text watermarking is necessary but not sufficient — widespread developer integration and verification tooling are still nascent.
- **Video and audio coverage**: Current Chrome/Search verification is image-only; video and audio expansion is planned but not yet shipped.

### Text Watermark Criticism: The Removal Argument

Sean Goedecke's July 2026 analysis ("[Text AI watermarks will always be trivial to remove](https://seangoedecke.com/text-ai-watermarks/)") presents the most thorough critique of text watermarking's fundamental feasibility:

**1. Text is too compressed for robust watermarking.** Unlike images (which contain imperceptible noise), text admits no change that a human wouldn't notice — except Unicode homoglyphs (replacing spaces with three-per-em or CJK space characters). Goedecke observes that Claude Code has been caught exploiting homoglyphs for geofencing (tagging suspicious Chinese-user requests), and ChatGPT outputs sometimes contain unusual Unicode spaces — suggesting both OpenAI and Anthropic may already use homoglyph-based watermarking.

**2. SynthID breaks at zero temperature.** When inference temperature is set to 0 (always picking the most likely token), SynthID's scoring-based sampling cannot function — there is no randomness to influence. Either the watermark must be suppressed, or the user's preference must be overridden.

**3. Watermarks are trivially removable:**
- **Unicode homoglyph removal**: Simply normalize all Unicode characters to their real equivalents (e.g., replace U+2004 and U+3000 spaces with U+0020).
- **SynthID removal**: Ask any un-watermarked LLM to paraphrase the text. The watermark is inherent to subtle vocabulary choices; re-wording destroys it. Goedecke notes that since the AI Act mandates free public watermark testing tools, adversaries can "keep tweaking until it comes back negative."

**4. The AI Act's interoperability requirement is incompatible with security-by-obscurity.** The EU AI Act Code of Practice requires watermarking techniques to be "interoperable… as far as this is technically feasible" — meaning providers must publish their watermarking processes and potentially standardize. Text watermarking depends on hidden patterns (obscured scoring functions, secret homoglyph maps). Interoperability forces disclosure, which enables systematic bypass. As Goedecke puts it: "I just don't see how this is compatible with the kind of security-by-obscurity that LLM text watermarking depends on."

**5. C2PA metadata is not a substitute for text watermarking.** C2PA only applies to containerized file formats (audio, image, video). Chat tool outputs and most AI agent output is uncontainerized plain text — there is no metadata slot to sign. The AI Act mandates actual watermarking in addition to metadata.

**Critical assessment**: Goedecke's argument does not invalidate SynthID's value for images, video, and audio (where watermarking has fundamentally different properties), but exposes a structural weakness in the text watermarking pillar of AI content provenance — particularly for chat/agent output. See [[entities/seangoedecke-com]] for the full analysis.

## Related Pages

- [[entities/google]] — Google's AI ecosystem, including Gemini and DeepMind
- [[entities/openai]] — OpenAI's role in AI governance and content labeling
- [[entities/deepmind]] — Google DeepMind, creator of SynthID
- [[concepts/security-and-governance/ai-safety]] — AI safety and governance frameworks
- [[entities/seangoedecke-com]] — Sean Goedecke, whose C2PA批判 analysis provides critical counterpoint to SynthID+C2PA optimism
- [[concepts/ai-detection]] — AI-generated content detection methods
