# GLiNER for Modern Named Entity Recognition

*Source: https://pioneer.ai/blog/gliner-modern-named-entity-recognition*

---

GLiNER is an open source, BERT-based model that performs named entity recognition at state-of-the-art levels, while being small enough to run on consumer hardware—without a GPU.

## The problem: modern NER is slow, expensive, and proprietary

Most practitioners doing Named Entity Recognition today reach for a large generative model like GPT-5 or Claude—models with hundreds of billions of parameters. These models are exceptional at language generation, but they carry significant costs when applied to NER tasks:

- **Latency.** Generative models must produce the full output sequence autoregressively, token by token. This creates a bottleneck for real-time use cases.
- **Cost.** Running inference on a 70B+ parameter model is expensive, especially at scale.
- **Data sovereignty.** Sending sensitive data to a third-party API raises compliance concerns in industries like healthcare, finance, and legal.

In contrast, generative models are trained to autoregressively predict the next token in a sequence of tokens, a slow task that primes models for language fluency, not language understanding.

The answer to efficient zero-shot NER lies in a return to the encoder architecture, which primes models for language understanding and representation, as opposed to fluency.

## GLiNER is a small bidirectional model pre-trained for NER

GLiNER is a bidirectional encoder (BERT-based) model. Bidirectional models use the context both before and after a given token to build their understanding and representation of it, as opposed to unidirectional models like GPT-5 or Google Gemini, which only use the context preceding a given token to understand it.

Traditional encoders like BERT or RoBERTa lack zero-shot capabilities because they are restricted to a static set of labels established during training. In contrast, GLiNER achieves zero-shot performance by framing entity extraction as a matching task rather than a generation task. Both the target labels and the input text are processed by the model, in parallel, and embedded in a shared latent space. GLiNER then calculates a similarity score between the targets and inputs—enabling it to identify entirely new entity classes without further training.

## How GLiNER redefines modern NER

GLiNER represents a paradigm shift for modern Named Entity Recognition—moving away from entity extraction as a costly generative task to an efficient matching task. Moreover, GLiNER's unique architecture gives it several competitive advantages over using unidirectional decoder models for NER tasks, including:

- **Size.** GLiNER is only 205 million parameters in size, meaning that it can be run on edge devices and consumer hardware (no GPU necessary).
- **Performance.** GLiNER outperforms ChatGPT and several LLMs fine-tuned for NER. This is in part due to its bidirectional architecture, which allows it to leverage context on both sides of each token, providing a deeper understanding of linguistic structure.
- **Zero-shot capabilities.** In contrast to traditional NER models, GLiNER offers zero-shot entity recognition. It achieves this by framing entity extraction as a matching problem rather than a generation task, projecting both the input text and target entity labels into a shared latent space.
- **Adaptability.** GLiNER's lean compute footprint makes domain-specific fine-tuning far more accessible compared to large generative models.
- **Sovereignty.** GLiNER's open source license and small size means that the model and any fine-tuned variants can run comfortably and securely on device, without making any external API calls.

GLiNER's innovation lies in both its return to a bidirectional encoder architecture and its treatment of NER as a matching algorithm.

## GLiNER's size is not a compromise

Modern scaling laws dictate that model performance improves at a predictable, power-law rate relative to increases in parameters, dataset size, and training compute. GLiNER directly contradicts this by matching and even outperforming models many times larger.

Some of the most impressive results from GLiNER's evaluation against other NER models reveal that:

- GLiNER-Medium (90M) matches UniNER-13B in performance while being 140x smaller.
- GLiNER-Small (50M) beats ChatGPT, Vicuna, and the 11B InstructUIE in zero-shot NER tasks.
- Despite English-only training, the multilingual variant outperforms ChatGPT across most languages, particularly those using Latin scripts.

GLiNER's task-specific architecture and efficient use of parameters allows it to defy modern scaling laws, positioning it as a viable option in replacing larger generative models for NER tasks.

## Sources cited

- Zaratiana, U., Tomeh, N., Holat, P., & Charnois, T. (2023). GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer (arXiv:2311.08526). arXiv. https://arxiv.org/abs/2311.08526
- Zhou, W., Zhang, S., Gu, Y., Chen, M., & Poon, H. (2023). UniversalNER: Targeted distillation from world knowledge for open-ended named entity recognition.
