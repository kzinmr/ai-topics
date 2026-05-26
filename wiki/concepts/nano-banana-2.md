---
title: "Nano Banana 2"
type: concept
aliases:
  - nano-banana-2
  - nano-banana-pro
  - google-nano-banana
created: 2026-04-25
updated: 2026-05-26
tags:
  - concept
  - image-generation
  - google
status: complete
sources:
  - url: "https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana"
    title: "The Ultimate Nano Banana Prompting Guide (Google Cloud Blog)"
  - url: "https://cloud.google.com/blog/products/ai-machine-learning/bringing-nano-banana-2-to-enterprise"
    title: "Bringing Nano Banana 2 to Enterprise (Google Cloud Blog)"
  - url: "https://gemini.google.com/"
    title: "Nano Banana on Gemini"
---

# Nano Banana 2

**Nano Banana 2** is a cutting-edge AI image generation and editing model developed by Google for the Gemini 3 family. It leverages deep reasoning capabilities and real-time information from web search to produce more accurate and context-aware visuals than traditional image generation models.

## Definition / Core Idea

Nano Banana models go beyond simple text-to-image conversion, using **real-world knowledge and deep reasoning** to generate images. Before interpreting a prompt, the model goes through a "comprehension" phase, delivering more accurate and consistent results.

## Model Variants

| Model | Features | Use Case |
|-------|----------|----------|
| **Nano Banana** (Fast) | Fast generation, character consistency, photo compositing | Casual content creation |
| **Nano Banana Pro** (Reasoning) | Advanced text rendering, precision editing, 2K/4K upscaling | Professional workflows |
| **Nano Banana 2** | Real-time web information, high-precision visuals | Enterprise, education, travel |

## Key Features

### 1. Real-Time Web Search Integration
- Fetches the latest web information and reflects it in image generation
- Example: Can generate "a scene reflecting current weather in San Francisco"

### 2. Character Consistency
- Maintains the same character's appearance across multiple images
- Important for storyboards, ad campaigns

### 3. Advanced Editing Capabilities
- **Local editing**: Modify only a portion of the image
- **Photo compositing**: Seamlessly combine multiple photos
- **Text rendering**: Render clear text within images

### 4. Prompting Framework
Google's official prompting guide recommends the following framework:
1. **Structured prompt**: `[Source/Search Request] + [Analysis Task] + [Visual Instruction]`
2. **Aspect ratio control**: Native support for 16:9, 9:16, 2:1, etc.
3. **Iterative refinement**: Gradually improve prompts based on generation results

## Tech Stack

- **Base model**: Gemini 3 family image generation capabilities
- **SynthID**: DeepMind's invisible watermarking technology (copyright/responsible AI)
- **Vertex AI**: Enterprise deployment API
- **Hugging Face**: Community model distribution

## Related Concepts

- [[concepts/ai-image-generation]] — Overview of AI image generation
- [[concepts/reverse-engineering]] — Analysis of image generation models

## Sources

- [Google Cloud: Ultimate Nano Banana Prompting Guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)
- [Google Cloud: Bringing Nano Banana 2 to Enterprise](https://cloud.google.com/blog/products/ai-machine-learning/bringing-nano-banana-2-to-enterprise)
- [Gemini Nano Banana](https://gemini.google.com/)
