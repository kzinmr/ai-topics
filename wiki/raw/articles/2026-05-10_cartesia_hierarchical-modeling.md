---
title: "Hierarchical modeling - Cartesia"
source: "Cartesia Blog"
url: "https://cartesia.ai/blog/hierarchical-modeling"
scraped: "2026-05-10T01:19:21.475524+00:00"
lastmod: "None"
type: "sitemap"
---

# Hierarchical modeling - Cartesia

**Source**: [https://cartesia.ai/blog/hierarchical-modeling](https://cartesia.ai/blog/hierarchical-modeling)

Meet Sonic-3: the best text-to-speech for voice agents
|
Learn more
Meet Sonic-3: the best text-to-speech for voice agents
|
Learn more
Sonic-3: the best text-to-speech for voice agents
Models
new
Agents
Solutions
Resources
Pricing
Contact sales
Sign in
Start for Free
Start for Free
Jul 11, 2025
·
Research
Hierarchical modeling
Hierarchical modeling
Albert Gu
Brandon Wang
The best AI architectures in use today treat all inputs equally. They process each input with the same amount of compute, without explicitly grouping related inputs into higher level concepts. While these architectures have achieved impressive results across domains, this lack of hierarchy has some fundamental limitations.
Models have difficulty learning from high resolution, raw data, requiring inputs to be pre-processed into meaningful tokens for strong performance.
The use of hand-crafted pre-processing steps (e.g. tokenization) can cause models to fail unexpectedly with small perturbations in the input data.
Models waste compute on tokens that are easy to predict and not informative.
More importantly, information is fundamentally hierarchical. In language, ideas are chunked in characters, words, sentences, and paragraphs; in images, pixels are chunked in edges, shapes, and objects; in audio, raw waveforms are grouped into phonemes, sentences, and conversation turns. As humans, we consume raw information and group it in meaningful ways that allow us to reason and make connections at different levels of abstraction, from low level units to the high level ideas. This is core to intelligence. We believe hierarchical models will address several of the fundamental limitations and shortcomings of today’s architectures.
We’re excited to announce our latest research collaboration on
hierarchical networks (H-Nets)
, a new architecture that natively models hierarchy from raw data. The core of the H-Net architecture is a dynamic chunking mechanism that learns to segment and compress raw data into meaningful concepts for modeling. It has three components: an encoder network, the main network, and a decoder network. The core of the encoder network is a routing module, which uses a similarity score to predict groups of meaningful chunks that should be grouped together and compressed for the main network. The main network can be any sequence to sequence model, and is responsible for next token prediction over these higher level chunks. Finally, the decoder network learns to decode chunks back into raw data, with a smoothing module for stabilizing learning.
H-Net demonstrates three important results on language modeling:
H-Nets scale better with data than state-of-the-art Transformers with BPE tokenization, while learning directly from raw bytes. This improved scaling is even more pronounced on domains without natural tokenization boundaries, like Chinese, code, and DNA.
H-Nets can be stacked together to learn from deeper hierarchies, which further improves performance.
H-Nets are significantly more robust to small perturbations in input data like casing, showing an avenue for creating models that are more robust and aligned with human reasoning.
Our investment in this research is part of our larger push to build the next-generation of AI models that are multimodal, highly efficient, and reason and improve over long horizons. State space models represented our first research advancement, enabling stateful models that can compress information over long contexts. We believe H-Nets, and hierarchical modeling, are the key next step to addressing fundamental challenges in AI:
Multimodal understanding and generation:
A key challenge in multimodal modeling is fusing multiple streams of data. This is a difficult today, since different modalities are tokenized at different rates. For example, language is tokenized into subwords, while audio is tokenized as raw waveforms or downsampled codecs. This makes them difficult to model jointly. Hierarchical models like H-Net provide a promising path to fuse these multimodal streams at a higher abstraction level, enabling better transfer, reasoning, and understanding across modalities.
Long-context reasoning:
H-Nets unlock long context reasoning by chunking information into semantically meaningful units at higher levels of abstraction. This compression makes it easier for models to understand and reason across large inputs, particularly with deeper and deeper hierarchies. Hierarchical architectures will enable models that understand their environment from raw data and reason at appropriate levels of abstraction over long horizons.
Efficient training and inference:
Today’s architectures use the same amount of compute for every token, even though some tokens are less informative and easier to predict than others. Inference time optimizations, like speculative decoding, exploit this property to speed up computation on easier to predict tokens. With H-Nets, this is built directly into the architecture, by handling tokens that are easier to predict with lightweight encoder and decoder modules.
For more, read our full preprint on
arXiv
. We’ve also released checkpoints for H-Net 2-stage XL, H-Net 1-stage XL, and H-Net 1-stage L on
HuggingFace
.
If you’re excited about the future of architecture research and building systems and infrastructure to deliver these new models at scale, please reach out!
Related articles
Related articles
Sep 24, 2025
·
News
Cartesia achieves GDPR compliance
Aug 19, 2025
·
News
Introducing Line: The Modern Voice Agent Development Platform
Jul 11, 2025
·
Research
Hierarchical modeling
Sep 24, 2025
·
News
Cartesia achieves GDPR compliance
Aug 19, 2025
·
News
Introducing Line: The Modern Voice Agent Development Platform
Real-time, multimodal intelligence for every device.
Models
Sonic
Ink
Agents
Solutions
Customer service
Localization
Recruiting
Sales
Finance
Healthcare
Gaming
Hospitality
Regions
Asia pacific
Brazil
China
India
Japan
Korea
Latin America
Middle East
North America
Western Europe
Eastern Europe
Resources
Blog
Customers
Docs
Events
Pricing
Research
Support
Company
About
Careers
Legal
Terms of Service
Privacy
Acceptable Use
Cookie Settings
Real-time, multimodal intelligence for every device.
Models
Sonic
Ink
Agents
Solutions
Customer service
Localization
Recruiting
Sales
Finance
Healthcare
Gaming
Hospitality
Regions
Asia pacific
Brazil
China
India
Japan
Korea
Latin America
Middle East
North America
Western Europe
Eastern Europe
Resources
Blog
Customers
Docs
Events
Pricing
Research
Support
Company
About
Careers
Legal
Terms of Service
Privacy
Acceptable Use
Cookie Settings
Real-time, multimodal intelligence for every device.
Models
Sonic
Ink
Agents
Solutions
Customer service
Localization
Recruiting
Sales
Finance
Healthcare
Gaming
Hospitality
Regions
Asia pacific
Brazil
China
India
Japan
Korea
Latin America
Middle East
North America
Western Europe
Eastern Europe
Resources
Blog
Customers
Docs
Events
Pricing
Research
Support
Company
About
Careers
Cookie Settings
Legal
Terms of Use
Privacy
Acceptable Use
