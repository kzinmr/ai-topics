---
title: "ByteDance"
created: 2026-06-22
updated: 2026-08-10
type: entity
tags:
  - bytedance
  - company
  - china
  - open-source
  - lab
  - ai-research
  - video-generation
sources:
- raw/articles/2026-06-22_bytedance-deerflow-superagent-harness.md
- https://github.com/bytedance/deer-flow
- raw/newsletters/2026-08-09-google-sells-the-shovels-the-great-hark-handoff-and-bytedance-s-bigger-picture.md
---

# ByteDance

**ByteDance** is a Chinese multinational technology company headquartered in Beijing, best known as the parent company of TikTok (Douyin in China). Founded in 2012 by Zhang Yiming, ByteDance has grown into one of the world's most valuable private companies, with a significant and growing presence in artificial intelligence research and open-source AI tooling.

## AI Research and Open-Source Contributions

ByteDance has emerged as an active participant in the AI open-source ecosystem, contributing tools and models alongside its commercial AI services through the Volcengine cloud platform.

### DeerFlow

ByteDance's most prominent open-source AI contribution is **[[concepts/deer-flow|DeerFlow]]**, a SuperAgent harness released under the MIT license. DeerFlow orchestrates sub-agents, memory, and sandboxes, with each agent receiving its own filesystem, bash terminal, and code execution environment. As of June 2026, the project has accumulated 72,935 GitHub stars and 9,867 forks, claiming the #1 position on GitHub Trending on February 28, 2026.

Key characteristics of DeerFlow that reflect ByteDance's AI approach:
- **Full sandbox model**: Agents operate in complete OS environments, not limited tool APIs
- **Long-horizon execution**: Designed for tasks spanning minutes to hours
- **Extensible skills architecture**: Progressively loaded, modular capabilities
- **Multi-model**: Recommends Doubao-Seed-2.0-Code (ByteDance's own model) alongside DeepSeek v3

### Doubao / Seed Models

ByteDance develops the **Doubao** family of AI models through its Seed team, offered commercially via the Volcengine platform. The Doubao-Seed-2.0-Code variant is specifically recommended for coding agent workflows within DeerFlow.

### Seedance Video Models

The Seed team's video generation line, **Seedance**, is distributed through Volcengine and the seed.bytedance.com blog.

#### Seedance 2.5

Released in early August 2026, **Seedance 2.5** generates 30-second video clips with synchronised audio in a single pass, and accepts up to 30 images, 10 video clips, and 10 audio clips as references. Days before the release, the *Financial Times* reported that ByteDance is pre-training a model of up to 10 trillion parameters — three times the size of Kimi K3 — which could become the largest AI model ever built by a Chinese company. Primary source: the seed.bytedance.com blog.

### Other AI Projects

ByteDance's AI activities span multiple domains:
- **Volcengine**: Cloud computing platform offering AI inference, model hosting, and enterprise AI services
- **BytePlus**: Technology solutions arm providing AI-powered tools including InfoQuest (intelligent search and crawling)
- **Recommendation systems**: Industry-leading content recommendation algorithms powering TikTok, Douyin, and other ByteDance products
- **AI video and content generation**: Tools integrated into ByteDance's content ecosystem

## Position in the AI Landscape

ByteDance represents a major Chinese technology company transitioning from consumer applications (TikTok, Douyin, Toutiao) into significant AI infrastructure and open-source contributions. Its approach — releasing engineer-focused agent tooling under permissive licenses while commercializing model inference through Volcengine — parallels strategies seen from [[concepts/qwen|Alibaba (Qwen)]] and [[entities/deepseek|DeepSeek]].

## Related Pages

- [[concepts/deer-flow]] — DeerFlow SuperAgent harness
- [[concepts/deerflow]] — Earlier DeerFlow coverage
- [[concepts/agent-harnesses]] — Agent harness philosophy and landscape
- [[concepts/sandbox]] — Agent sandboxing and isolation
- [[entities/tencent]] — Another Chinese tech giant with AI model development
- [[entities/xiaomi]] — Xiaomi's MiMo AI model family
- [[concepts/china-openclaw-agentic-boom]] — China's agentic coding ecosystem
