---
title: "mlabonne/llm-course: Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. · GitHub"
url: "https://github.com/mlabonne/llm-course"
fetched_at: 2026-05-05T07:02:12.623109+00:00
source: "Maxime Labonne"
tags: [blog, raw]
---

# mlabonne/llm-course: Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. · GitHub

Source: https://github.com/mlabonne/llm-course

The LLM course is divided into three parts:
🧩
LLM Fundamentals
is optional and covers fundamental knowledge about mathematics, Python, and neural networks.
🧑‍🔬
The LLM Scientist
focuses on building the best possible LLMs using the latest techniques.
👷
The LLM Engineer
focuses on creating LLM-based applications and deploying them.
Note
Based on this course, I co-wrote the
LLM Engineer's Handbook
, a hands-on book that covers an end-to-end LLM application from design to deployment. The LLM course will always stay free, but you can support my work by purchasing this book.
For a more comprehensive version of this course, check out the
DeepWiki
.
A list of notebooks and articles I wrote about LLMs.
Toggle section (optional)
Notebook
Description
Notebook
🧐
LLM AutoEval
Automatically evaluate your LLMs using RunPod
🥱 LazyMergekit
Easily merge models using MergeKit in one click.
🦎 LazyAxolotl
Fine-tune models in the cloud using Axolotl in one click.
⚡ AutoQuant
Quantize LLMs in GGUF, GPTQ, EXL2, AWQ, and HQQ formats in one click.
🌳 Model Family Tree
Visualize the family tree of merged models.
🚀 ZeroSpace
Automatically create a Gradio chat interface using a free ZeroGPU.
✂️ AutoAbliteration
Automatically abliteration models with custom datasets.
🧼 AutoDedup
Automatically deduplicate datasets using the Rensa library.
Notebook
Description
Article
Notebook
Fine-tune Llama 3.1 with Unsloth
Ultra-efficient supervised fine-tuning in Google Colab.
Article
Fine-tune Llama 3 with ORPO
Cheaper and faster fine-tuning in a single stage with ORPO.
Article
Fine-tune Mistral-7b with DPO
Boost the performance of supervised fine-tuned models with DPO.
Article
Fine-tune Mistral-7b with QLoRA
Supervised fine-tune Mistral-7b in a free-tier Google Colab with TRL.
Fine-tune CodeLlama using Axolotl
End-to-end guide to the state-of-the-art tool for fine-tuning.
Article
Fine-tune Llama 2 with QLoRA
Step-by-step guide to supervised fine-tune Llama 2 in Google Colab.
Article
Notebook
Description
Article
Notebook
Introduction to Quantization
Large language model optimization using 8-bit quantization.
Article
4-bit Quantization using GPTQ
Quantize your own open-source LLMs to run them on consumer hardware.
Article
Quantization with GGUF and llama.cpp
Quantize Llama 2 models with llama.cpp and upload GGUF versions to the HF Hub.
Article
ExLlamaV2: The Fastest Library to Run LLMs
Quantize and run EXL2 models and upload them to the HF Hub.
Article
Notebook
Description
Article
Notebook
Merge LLMs with MergeKit
Create your own models easily, no GPU required!
Article
Create MoEs with MergeKit
Combine multiple experts into a single frankenMoE
Article
Uncensor any LLM with abliteration
Fine-tuning without retraining
Article
Improve ChatGPT with Knowledge Graphs
Augment ChatGPT's answers with knowledge graphs.
Article
Decoding Strategies in Large Language Models
A guide to text generation from beam search to nucleus sampling
Article
This section introduces essential knowledge about mathematics, Python, and neural networks. You might not want to start here but refer to it as needed.
Toggle section (optional)
1. Mathematics for Machine Learning
Before mastering machine learning, it is important to understand the fundamental mathematical concepts that power these algorithms.
Linear Algebra
: This is crucial for understanding many algorithms, especially those used in deep learning. Key concepts include vectors, matrices, determinants, eigenvalues and eigenvectors, vector spaces, and linear transformations.
Calculus
: Many machine learning algorithms involve the optimization of continuous functions, which requires an understanding of derivatives, integrals, limits, and series. Multivariable calculus and the concept of gradients are also important.
Probability and Statistics
: These are crucial for understanding how models learn from data and make predictions. Key concepts include probability theory, random variables, probability distributions, expectations, variance, covariance, correlation, hypothesis testing, confidence intervals, maximum likelihood estimation, and Bayesian inference.
📚 Resources:
2. Python for Machine Learning
Python is a powerful and flexible programming language that's particularly good for machine learning, thanks to its readability, consistency, and robust ecosystem of data science libraries.
Python Basics
: Python programming requires a good understanding of the basic syntax, data types, error handling, and object-oriented programming.
Data Science Libraries
: It includes familiarity with NumPy for numerical operations, Pandas for data manipulation and analysis, Matplotlib and Seaborn for data visualization.
Data Preprocessing
: This involves feature scaling and normalization, handling missing data, outlier detection, categorical data encoding, and splitting data into training, validation, and test sets.
Machine Learning Libraries
: Proficiency with Scikit-learn, a library providing a wide selection of supervised and unsupervised learning algorithms, is vital. Understanding how to implement algorithms like linear regression, logistic regression, decision trees, random forests, k-nearest neighbors (K-NN), and K-means clustering is important. Dimensionality reduction techniques like PCA and t-SNE are also helpful for visualizing high-dimensional data.
📚 Resources:
Neural networks are a fundamental part of many machine learning models, particularly in the realm of deep learning. To utilize them effectively, a comprehensive understanding of their design and mechanics is essential.
Fundamentals
: This includes understanding the structure of a neural network, such as layers, weights, biases, and activation functions (sigmoid, tanh, ReLU, etc.)
Training and Optimization
: Familiarize yourself with backpropagation and different types of loss functions, like Mean Squared Error (MSE) and Cross-Entropy. Understand various optimization algorithms like Gradient Descent, Stochastic Gradient Descent, RMSprop, and Adam.
Overfitting
: Understand the concept of overfitting (where a model performs well on training data but poorly on unseen data) and learn various regularization techniques (dropout, L1/L2 regularization, early stopping, data augmentation) to prevent it.
Implement a Multilayer Perceptron (MLP)
: Build an MLP, also known as a fully connected network, using PyTorch.
📚 Resources:
4. Natural Language Processing (NLP)
NLP is a fascinating branch of artificial intelligence that bridges the gap between human language and machine understanding. From simple text processing to understanding linguistic nuances, NLP plays a crucial role in many applications like translation, sentiment analysis, chatbots, and much more.
Text Preprocessing
: Learn various text preprocessing steps like tokenization (splitting text into words or sentences), stemming (reducing words to their root form), lemmatization (similar to stemming but considers the context), stop word removal, etc.
Feature Extraction Techniques
: Become familiar with techniques to convert text data into a format that can be understood by machine learning algorithms. Key methods include Bag-of-words (BoW), Term Frequency-Inverse Document Frequency (TF-IDF), and n-grams.
Word Embeddings
: Word embeddings are a type of word representation that allows words with similar meanings to have similar representations. Key methods include Word2Vec, GloVe, and FastText.
Recurrent Neural Networks (RNNs)
: Understand the working of RNNs, a type of neural network designed to work with sequence data. Explore LSTMs and GRUs, two RNN variants that are capable of learning long-term dependencies.
📚 Resources:
This section of the course focuses on learning how to build the best possible LLMs using the latest techniques.
An in-depth knowledge of the Transformer architecture is not required, but it's important to understand the main steps of modern LLMs: converting text into numbers through tokenization, processing these tokens through layers including attention mechanisms, and finally generating new text through various sampling strategies.
Architectural overview
: Understand the evolution from encoder-decoder Transformers to decoder-only architectures like GPT, which form the basis of modern LLMs. Focus on how these models process and generate text at a high level.
Tokenization
: Learn the principles of tokenization - how text is converted into numerical representations that LLMs can process. Explore different tokenization strategies and their impact on model performance and output quality.
Attention mechanisms
: Master the core concepts of attention mechanisms, particularly self-attention and its variants. Understand how these mechanisms enable LLMs to process long-range dependencies and maintain context throughout sequences.
Sampling techniques
: Explore various text generation approaches and their tradeoffs. Compare deterministic methods like greedy search and beam search with probabilistic approaches like temperature sampling and nucleus sampling.
📚
References
:
Visual intro to Transformers
by 3Blue1Brown: Visual introduction to Transformers for complete beginners.
LLM Visualization
by Brendan Bycroft: Interactive 3D visualization of LLM internals.
nanoGPT
by Andrej Karpathy: A 2h-long YouTube video to reimplement GPT from scratch (for programmers). He also made a video about
tokenization
.
Attention? Attention!
by Lilian Weng: Historical overview to introduce the need for attention mechanisms.
Decoding Strategies in LLMs
by Maxime Labonne: Provide code and a visual introduction to the different decoding strategies to generate text.
Pre-training is a computationally intensive and expensive process. While it's not the focus of this course, it's important to have a solid understanding of how models are pre-trained, especially in terms of data and parameters. Pre-training can also be performed by hobbyists at a small scale with <1B models.
Data preparation
: Pre-training requires massive datasets (e.g.,
Llama 3.1
was trained on 15 trillion tokens) that need careful curation, cleaning, deduplication, and tokenization. Modern pre-training pipelines implement sophisticated filtering to remove low-quality or problematic content.
Distributed training
: Combine different parallelization strategies: data parallel (batch distribution), pipeline parallel (layer distribution), and tensor parallel (operation splitting). These strategies require optimized network communication and memory management across GPU clusters.
Training optimization
: Use adaptive learning rates with warm-up, gradient clipping, and normalization to prevent explosions, mixed-precision training for memory efficiency, and modern optimizers (AdamW, Lion) with tuned hyperparameters.
Monitoring
: Track key metrics (loss, gradients, GPU stats) using dashboards, implement targeted logging for distributed training issues, and set up performance profiling to identify bottlenecks in computation and communication across devices.
📚
References
:
FineWeb
by Penedo et al.: Article to recreate a large-scale dataset for LLM pretraining (15T), including FineWeb-Edu, a high-quality subset.
RedPajama v2
by Weber et al.: Another article and paper about a large-scale pre-training dataset with a lot of interesting quality filters.
nanotron
by Hugging Face: Minimalistic LLM training codebase used to make
SmolLM2
.
Parallel training
by Chenyan Xiong: Overview of optimization and parallelism techniques.
Distributed training
by Duan et al.: A survey about efficient training of LLM on distributed architectures.
OLMo 2
by AI2: Open-source language model with model, data, training, and evaluation code.
LLM360
by LLM360: A framework for open-source LLMs with training and data preparation code, data, metrics, and models.
3. Post-Training Datasets
Post-training datasets have a precise structure with instructions and answers (supervised fine-tuning) or instructions and chosen/rejected answers (preference alignment). Conversational structures are a lot rarer than the raw text used for pre-training, which is why we often need to process seed data and refine it to improve the accuracy, diversity, and complexity of the samples. More information and examples are available in my repo
💾 LLM Datasets
.
Storage & chat templates
: Because of the conversational structure, post-training datasets are stored in a specific format like ShareGPT or OpenAI/HF. Then, these formats are mapped to a chat template like ChatML or Alpaca to produce the final samples that the model is trained on.
Synthetic data generation
: Create instruction-response pairs based on seed data using frontier models like GPT-4o. This approach allows for flexible and scalable dataset creation with high-quality answers. Key considerations include designing diverse seed tasks and effective system prompts.
Data enhancement
: Enhance existing samples using techniques like verified outputs (using unit tests or solvers), multiple answers with rejection sampling,
Auto-Evol
, Chain-of-Thought, Branch-Solve-Merge, personas, etc.
Quality filtering
: Traditional techniques involve rule-based filtering, removing duplicates or near-duplicates (with MinHash or embeddings), and n-gram decontamination. Reward models and judge LLMs complement this step with fine-grained and customizable quality control.
📚
References
:
Synthetic Data Generator
by Argilla: Beginner-friendly way of building datasets using natural language in a Hugging Face space.
LLM Datasets
by Maxime Labonne: Curated list of datasets and tools for post-training.
NeMo-Curator
by Nvidia: Dataset preparation and curation framework for pre- and post-training data.
Distilabel
by Argilla: Framework to generate synthetic data. It also includes interesting reproductions of papers like UltraFeedback.
Semhash
by MinishLab: Minimalistic library for near-deduplication and decontamination with a distilled embedding model.
Chat Template
by Hugging Face: Hugging Face's documentation about chat templates.
4. Supervised Fine-Tuning
SFT turns base models into helpful assistants, capable of answering questions and following instructions. During this process, they learn how to structure answers and reactivate a subset of knowledge learned during pre-training. Instilling new knowledge is possible but superficial: it cannot be used to learn a completely new language. Always prioritize data quality over parameter optimization.
Training techniques
: Full fine-tuning updates all model parameters but requires significant compute. Parameter-efficient fine-tuning techniques like LoRA and QLoRA reduce memory requirements by training a small number of adapter parameters while keeping base weights frozen. QLoRA combines 4-bit quantization with LoRA to reduce VRAM usage. These techniques are all implemented in the most popular fine-tuning frameworks:
TRL
,
Unsloth
, and
Axolotl
.
Training parameters
: Key parameters include learning rate with schedulers, batch size, gradient accumulation, number of epochs, optimizer (like 8-bit AdamW), weight decay for regularization, and warmup steps for training stability. LoRA also adds three parameters: rank (typically 16-128), alpha (1-2x rank), and target modules.
Distributed training
: Scale training across multiple GPUs using DeepSpeed or FSDP. DeepSpeed provides three ZeRO optimization stages with increasing levels of memory efficiency through state partitioning. Both methods support gradient checkpointing for memory efficiency.
Monitoring
: Track training metrics including loss curves, learning rate schedules, and gradient norms. Monitor for common issues like loss spikes, gradient explosions, or performance degradation.
📚
References
:
Fine-tune Llama 3.1 Ultra-Efficiently with Unsloth
by Maxime Labonne: Hands-on tutorial on how to fine-tune a Llama 3.1 model using Unsloth.
Axolotl - Documentation
by Wing Lian: Lots of interesting information related to distributed training and dataset formats.
Mastering LLMs
by Hamel Husain: Collection of educational resources about fine-tuning (but also RAG, evaluation, applications, and prompt engineering).
LoRA insights
by Sebastian Raschka: Practical insights about LoRA and how to select the best parameters.
Preference alignment is a second stage in the post-training pipeline, focused on aligning generated answers with human preferences. This stage was designed to tune the tone of LLMs and reduce toxicity and hallucinations. However, it has become increasingly important to also boost their performance and improve their usefulness. Unlike SFT, there are many preference alignment algorithms. Here, we'll focus on the three most important ones: DPO, GRPO, and PPO.
Rejection sampling
: For each prompt, use the trained model to generate multiple responses, and score them to infer chosen/rejected answers. This creates on-policy data, where both responses come from the model being trained, improving alignment stability.
Direct Preference Optimization
Directly optimizes the policy to maximize the likelihood of chosen responses over rejected ones. It doesn't require reward modeling, which makes it more computationally efficient than RL techniques but slightly worse in terms of quality. Great for creating chat models.
Reward model
: Train a reward model with human feedback to predict metrics like human preferences. It can leverage frameworks like
TRL
,
verl
, and
OpenRLHF
for scalable training.
Reinforcement Learning
: RL techniques like
GRPO
and
PPO
iteratively update a policy to maximize rewards while staying close to the initial behavior. They can use a reward model or reward functions to score responses. They tend to be computationally expensive and require careful tuning of hyperparameters, including learning rate, batch size, and clip range. Ideal for creating reasoning models.
📚
References
:
Reliably evaluating LLMs is a complex but essential task guiding data generation and training. It provides invaluable feedback about areas of improvement, which can be leveraged to modify the data mixture, quality, and training parameters. However, it's always good to remember Goodhart's law: "When a measure becomes a target, it ceases to be a good measure."
Automated benchmarks
: Evaluate models on specific tasks using curated datasets and metrics, like MMLU. It works well for concrete tasks but struggles with abstract and creative capabilities. It is also prone to data contamination.
Human evaluation
: It involves humans prompting models and grading responses. Methods range from vibe checks to systematic annotations with specific guidelines and large-scale community voting (arena). It is more suited for subjective tasks and less reliable for factual accuracy.
Model-based evaluation
: Use judge and reward models to evaluate model outputs. It highly correlates with human preferences but suffers from bias toward their own outputs and inconsistent scoring.
Feedback signal
: Analyze error patterns to identify specific weaknesses, such as limitations in following complex instructions, lack of specific knowledge, or susceptibility to adversarial prompts. This can be improved with better data generation and training parameters.
📚
References
:
LLM evaluation guidebook
by Hugging Face: Comprehensive guide about evaluation with practical insights.
Open LLM Leaderboard
by Hugging Face: Main leaderboard to compare LLMs in an open and reproducible way (automated benchmarks).
Language Model Evaluation Harness
by EleutherAI: A popular framework for evaluating LLMs using automated benchmarks.
Lighteval
by Hugging Face: Alternative evaluation framework that also includes model-based evaluations.
Chatbot Arena
by LMSYS: Elo rating of general-purpose LLMs, based on comparisons made by humans (human evaluation).
Quantization is the process of converting the parameters and activations of a model to a lower precision. For example, weights stored using 16 bits can be converted into a 4-bit representation. This technique has become increasingly important to reduce the computational and memory costs associated with LLMs.
Base techniques
: Learn the different levels of precision (FP32, FP16, INT8, etc.) and how to perform naïve quantization with absmax and zero-point techniques.
GGUF & llama.cpp
: Originally designed to run on CPUs,
llama.cpp
and the GGUF format have become the most popular tools to run LLMs on consumer-grade hardware. It supports storing special tokens, vocabulary, and metadata in a single file.
GPTQ & AWQ
: Techniques like
GPTQ
/
EXL2
and
AWQ
introduce layer-by-layer calibration that retains performance at extremely low bitwidths. They reduce catastrophic outliers using dynamic scaling, selectively skipping or re-centering the heaviest parameters.
SmoothQuant & ZeroQuant
: New quantization-friendly transformations (SmoothQuant) and compiler-based optimizations (ZeroQuant) help mitigate outliers before quantization. They also reduce hardware overhead by fusing certain ops and optimizing dataflow.
📚
References
:
Here are notable topics that didn't fit into other categories. Some are established techniques (model merging, multimodal), but others are more experimental (interpretability, test-time compute scaling) and the focus of numerous research papers.
Model merging
: Merging trained models has become a popular way of creating performant models without any fine-tuning. The popular
mergekit
library implements the most popular merging methods, like SLERP,
DARE
, and
TIES
.
Multimodal models
: These models (like
CLIP
,
Stable Diffusion
, or
LLaVA
) process multiple types of inputs (text, images, audio, etc.) with a unified embedding space, which unlocks powerful applications like text-to-image.
Interpretability
: Mechanistic interpretability techniques like Sparse Autoencoders (SAEs) have made remarkable progress to provide insights about the inner workings of LLMs. This has also been applied with techniques such as abliteration, which allow you to modify the behavior of models without training.
Test-time compute
: Reasoning models trained with RL techniques can be further improved by scaling the compute budget during test time. It can involve multiple calls, MCTS, or specialized models like a Process Reward Model (PRM). Iterative steps with precise scoring significantly improve performance for complex reasoning tasks.
📚
References
:
This section of the course focuses on learning how to build LLM-powered applications that can be used in production, with a focus on augmenting models and deploying them.
Running LLMs can be difficult due to high hardware requirements. Depending on your use case, you might want to simply consume a model through an API (like GPT-4) or run it locally. In any case, additional prompting and guidance techniques can improve and constrain the output for your applications.
LLM APIs
: APIs are a convenient way to deploy LLMs. This space is divided between private LLMs (
OpenAI
,
Google
,
Anthropic
, etc.) and open-source LLMs (
OpenRouter
,
Hugging Face
,
Together AI
, etc.).
Open-source LLMs
: The
Hugging Face Hub
is a great place to find LLMs. You can directly run some of them in
Hugging Face Spaces
, or download and run them locally in apps like
LM Studio
or through the CLI with
llama.cpp
or
ollama
.
Prompt engineering
: Common techniques include zero-shot prompting, few-shot prompting, chain of thought, and ReAct. They work better with bigger models, but can be adapted to smaller ones.
Structuring outputs
: Many tasks require a structured output, like a strict template or a JSON format. Libraries like
Outlines
can be used to guide the generation and respect a given structure. Some APIs also support structured output generation natively using JSON schemas.
📚
References
:
2. Building a Vector Storage
Creating a vector storage is the first step to building a Retrieval Augmented Generation (RAG) pipeline. Documents are loaded, split, and relevant chunks are used to produce vector representations (embeddings) that are stored for future use during inference.
Ingesting documents
: Document loaders are convenient wrappers that can handle many formats: PDF, JSON, HTML, Markdown, etc. They can also directly retrieve data from some databases and APIs (GitHub, Reddit, Google Drive, etc.).
Splitting documents
: Text splitters break down documents into smaller, semantically meaningful chunks. Instead of splitting text after
n
characters, it's often better to split by header or recursively, with some additional metadata.
Embedding models
: Embedding models convert text into vector representations. Picking task-specific models significantly improves performance for semantic search and RAG.
Vector databases
: Vector databases (like
Chroma
,
Pinecone
,
Milvus
,
FAISS
,
Annoy
, etc.) are designed to store embedding vectors. They enable efficient retrieval of data that is 'most similar' to a query based on vector similarity.
📚
References
:
3. Retrieval Augmented Generation
With RAG, LLMs retrieve contextual documents from a database to improve the accuracy of their answers. RAG is a popular way of augmenting the model's knowledge without any fine-tuning.
Orchestrators
: Orchestrators like
LangChain
and
LlamaIndex
are popular frameworks to connect your LLMs with tools and databases. The Model Context Protocol (MCP) introduces a new standard to pass data and context to models across providers.
Retrievers
: Query rewriters and generative retrievers like CoRAG and HyDE enhance search by transforming user queries. Multi-vector and hybrid retrieval methods combine embeddings with keyword signals to improve recall and precision.
Memory
: To remember previous instructions and answers, LLMs and chatbots like ChatGPT add this history to their context window. This buffer can be improved with summarization (e.g., using a smaller LLM), a vector store + RAG, etc.
Evaluation
: We need to evaluate both the document retrieval (context precision and recall) and the generation stages (faithfulness and answer relevancy). It can be simplified with tools
Ragas
and
DeepEval
(assessing quality).
📚
References
:
Real-life applications can require complex pipelines, including SQL or graph databases, as well as automatically selecting relevant tools and APIs. These advanced techniques can improve a baseline solution and provide additional features.
Query construction
: Structured data stored in traditional databases requires a specific query language like SQL, Cypher, metadata, etc. We can directly translate the user instruction into a query to access the data with query construction.
Tools
: Agents augment LLMs by automatically selecting the most relevant tools to provide an answer. These tools can be as simple as using Google or Wikipedia, or more complex, like a Python interpreter or Jira.
Post-processing
: Final step that processes the inputs that are fed to the LLM. It enhances the relevance and diversity of documents retrieved with re-ranking,
RAG-fusion
, and classification.
Program LLMs
: Frameworks like
DSPy
allow you to optimize prompts and weights based on automated evaluations in a programmatic way.
📚
References
:
An LLM agent can autonomously perform tasks by taking actions based on reasoning about its environment, typically through the use of tools or functions to interact with external systems.
Agent fundamentals
: Agents operate using thoughts (internal reasoning to decide what to do next), action (executing tasks, often by interacting with external tools), and observation (analyzing feedback or results to refine the next step).
Agent protocols
:
Model Context Protocol
(MCP) is the industry standard for connecting agents to external tools and data sources with MCP servers and clients. More recently,
Agent2Agent
(A2A) tries to standardize a common language for agent interoperability.
Vendor frameworks
: Each major cloud model provider has its own agentic framework with
OpenAI SDK
,
Google ADK
, and
Claude Agent SDK
if you're particularly tied to one vendor.
Other frameworks
: Agent development can be streamlined using different frameworks like
LangGraph
(design and visualization of workflows)
LlamaIndex
(data-augmented agents with RAG), or custom solutions. More experimental frameworks include collaboration between different agents, such as
CrewAI
(role-based team workflows) and
AutoGen
(conversation-driven multi-agent systems).
📚
References
:
Agents Course
: Popular course about AI agents made by Hugging Face.
LangGraph
: Overview of how to build AI agents with LangGraph.
LlamaIndex Agents
: Uses cases and resources to build agents with LlamaIndex.
6. Inference optimization
Text generation is a costly process that requires expensive hardware. In addition to quantization, various techniques have been proposed to maximize throughput and reduce inference costs.
Flash Attention
: Optimization of the attention mechanism to transform its complexity from quadratic to linear, speeding up both training and inference.
Key-value cache
: Understand the key-value cache and the improvements introduced in
Multi-Query Attention
(MQA) and
Grouped-Query Attention
(GQA).
Speculative decoding
: Use a small model to produce drafts that are then reviewed by a larger model to speed up text generation. EAGLE-3 is a particularly popular solution.
📚
References
:
GPU Inference
by Hugging Face: Explain how to optimize inference on GPUs.
LLM Inference
by Databricks: Best practices for how to optimize LLM inference in production.
Optimizing LLMs for Speed and Memory
by Hugging Face: Explain three main techniques to optimize speed and memory, namely quantization, Flash Attention, and architectural innovations.
Assisted Generation
by Hugging Face: HF's version of speculative decoding. It's an interesting blog post about how it works with code to implement it.
EAGLE-3 paper
: Introduces EAGLE-3 and reports speedups up to 6.5×.
Speculators
: Library made by vLLM for building, evaluating, and storing speculative decoding algorithms (e.g., EAGLE-3) for LLM inference.
Deploying LLMs at scale is an engineering feat that can require multiple clusters of GPUs. In other scenarios, demos and local apps can be achieved with much lower complexity.
Local deployment
: Privacy is an important advantage that open-source LLMs have over private ones. Local LLM servers (
LM Studio
,
Ollama
,
oobabooga
,
kobold.cpp
, etc.) capitalize on this advantage to power local apps.
Demo deployment
: Frameworks like
Gradio
and
Streamlit
are helpful to prototype applications and share demos. You can also easily host them online, for example, using
Hugging Face Spaces
.
Server deployment
: Deploying LLMs at scale requires cloud (see also
SkyPilot
) or on-prem infrastructure and often leverages optimized text generation frameworks like
TGI
,
vLLM
, etc.
Edge deployment
: In constrained environments, high-performance frameworks like
MLC LLM
and
mnn-llm
can deploy LLM in web browsers, Android, and iOS.
📚
References
:
In addition to traditional security problems associated with software, LLMs have unique weaknesses due to the way they are trained and prompted.
Prompt hacking
: Different techniques related to prompt engineering, including prompt injection (additional instruction to hijack the model's answer), data/prompt leaking (retrieve its original data/prompt), and jailbreaking (craft prompts to bypass safety features).
Backdoors
: Attack vectors can target the training data itself, by poisoning the training data (e.g., with false information) or creating backdoors (secret triggers to change the model's behavior during inference).
Defensive measures
: The best way to protect your LLM applications is to test them against these vulnerabilities (e.g., using red teaming and checks like
garak
) and observe them in production (with a framework like
langfuse
).
📚
References
:
This roadmap was inspired by the excellent
DevOps Roadmap
from Milan Milanović and Romano Roth.
Special thanks to:
Thomas Thelen for motivating me to create a roadmap
André Frade for his input and review of the first draft
Dino Dunn for providing resources about LLM security
Magdalena Kuhn for improving the "human evaluation" part
Odoverdose for suggesting 3Blue1Brown's video about Transformers
Everyone who contributed to the educational references in this course :)
Disclaimer: I am not affiliated with any sources listed here.
