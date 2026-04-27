# Turning Gemini's embedding API into a universal multimodal encoder for LLMs

- **Source**: X Article (2033543094373859488)
- **Author**: @57182201
- **Date**: 2026-03-16
- **Bookmarks**: 368
- **External URLs**: https://github.com/krafton-ai/Can-Gemini-Embeddings-Be-a-Multimodal-Encoder-for-LLMs-, https://kangwooklee.com/blogs/gemini_embedding_as_universal_multimodal_encoder_for_LLMs.html

## Article Content

Google's gemini-embedding-2-preview is the first multimodal embedding model in the Gemini API. It maps text, images, video, audio, and documents into a unified 3072-d embedding space — cross-modal search, classification, and clustering across 100+ languages.

We asked: can we repurpose it as a multimodal encoder for a frozen LLM?
The setup is dead simple — one API call, a tiny learned adaptor, and a frozen Qwen3-4B. No custom encoder. No LLM fine-tuning. 17M trainable parameters. Under 1 minute to train on a single GPU.

Pipeline:
Every input (image or audio) goes through 3 stages:
1. Frozen Gemini Embedding API — one call → 3072-d vector
2. Learned MLP adaptor (17M params) — projects into k virtual tokens
3. Frozen Qwen3-4B — virtual tokens + text prompt → free-form answer

Only the MLP adaptor is trained. The task provides supervision: (image, label) pairs for classification, (audio, transcript) for STT. Cross-entropy loss against the ground-truth label tokens.
