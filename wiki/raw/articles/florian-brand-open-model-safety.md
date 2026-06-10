---
title: "Open Model Safety"
author: Florian Brand
date: 2025-02-04
url: https://florianbrand.com/posts/open-model-safety
fetched: 2026-06-10
---

# Open Model Safety

**Florian Brand · February 4, 2025**

This post is about why I believe that open model safety — the practice of evaluating and mitigating risks of openly released AI models — is important and needs to be formalized.

## Background

Large language models are increasingly being released openly. These models — such as Llama 3, Mistral, Qwen, DeepSeek, and many others — can be downloaded, fine-tuned, and deployed by anyone. This is great for research and innovation, but it also creates unique challenges for safety.

Closed model providers like OpenAI, Anthropic, and Google can gate access to their models, monitor usage, and roll out safety mitigations incrementally. Once a model is openly released, however, all of these levers disappear. There is no API to monitor, no terms of use to enforce, no kill switch. The model weights are out there permanently.

## Why open model safety matters

Open models are subject to fine-tuning and abliteration, which can remove safety guardrails. This means that even a carefully safety-trained model can be converted into an uncensored one with relatively modest compute and effort. The assumption that "the model was released safely" does not hold over time.

Moreover, open models can be deployed in any context — embedded in products, used for research, or deployed for malicious purposes. The model provider has no visibility into or control over downstream use.

This creates an asymmetry: it is far easier to remove safety training than it is to add it. A single fine-tuning run can undo months of safety work. And once the guardrails are removed, there is no way to restore them externally.

## The current landscape

Today, the evaluation of open models for safety is fragmented. Some model providers conduct internal evaluations before release, but these are often limited in scope. Third-party evaluations exist (e.g., from AI safety organizations), but they are not systematic, not standardized, and often not timely.

There is no widely adopted framework for evaluating open model safety that covers:

- Biological, chemical, radiological, and nuclear (BCRN) risks
- Cybersecurity risks (e.g., autonomous exploitation capabilities)
- Persuasion and influence risks
- Deception and manipulation risks
- Autonomous replication and adaptation risks

While benchmarks like those from the Center for AI Safety (CAIS) and others exist, they often focus on narrow capabilities and do not capture the full risk landscape.

## What needs to happen

1. **Pre-release evaluations**: Standardized, comprehensive evaluations that model providers must conduct before releasing open models. These should go beyond existing benchmarks and include qualitative assessments of high-risk capabilities.
2. **Post-release monitoring**: Ongoing monitoring of how released models are being fine-tuned and deployed. This is technically challenging but could include tracking model variants on platforms like Hugging Face.
3. **Safety data sharing**: Model providers should share their safety evaluation results, including negative results and edge cases, so that the community can build on this knowledge.
4. **Standardized reporting**: A common format for reporting model capabilities and risks, similar to software vulnerability disclosure frameworks. This would allow downstream users to make informed decisions about which models to deploy.
5. **Red-teaming at scale**: Systematic red-teaming efforts that go beyond what individual model providers can do. This could be coordinated by independent organizations or through bug bounty-style programs.

## The role of the community

One of the great strengths of open models is the community that builds around them. This same community can play a crucial role in safety. Open-source tools for evaluation, safety benchmarks, and guardrail systems are all areas where the community can contribute.

However, we need to be honest that community-driven safety is not sufficient on its own. Some risks — particularly those involving dual-use capabilities in biology and chemistry — require specialized expertise and controlled evaluation environments. The community can help identify risks, but mitigating them requires institutional support and resources.

## Looking ahead

As models become more capable, the stakes of open model safety will only increase. A model that can autonomously exploit software vulnerabilities, or that can provide detailed instructions for synthesizing dangerous substances, poses risks that are qualitatively different from today's models.

I believe the open model community has a window of opportunity right now to establish norms, standards, and institutions for safety before the risks become acute. This is not about restricting openness — it is about making openness sustainable.

If we get this right, open models can continue to be a force for good: democratizing access to AI capabilities, enabling research, and fostering innovation. If we get it wrong, the resulting harms could lead to backlash that restricts openness for everyone.
