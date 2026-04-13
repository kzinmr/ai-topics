---
title: "Benjamin Clavié"
aliases:
  - bclavie
  - Benjamin Clavié
created: 2026-04-10
updated: 2026-04-15
tags:
  - person
  - nlp-researcher
  - information-retrieval
  - colbert
  - ragatouille
  - modernbert
  - open-source
  - japan-based
status: L3
sources:
  - "https://ben.clavie.eu/"
  - "https://ben.clavie.eu/about/"
  - "https://ben.clavie.eu/posts/answer/"
  - "https://ben.clavie.eu/posts/sick/"
  - "https://ben.clavie.eu/ragatouille/"
  - "https://github.com/bclavie/RAGatouille"
  - "https://github.com/AnswerDotAI/ModernBERT"
  - "https://arxiv.org/abs/2412.13663"
  - "https://arxiv.org/abs/2510.12327"
  - "https://arxiv.org/abs/2510.14880"
  - "https://www.mixedbread.com/blog/edge-v0"
  - "https://parlance-labs.com/education/rag/ben.html"
related:
  - colbert
  - ragatouille
  - modernbert
  - information-retrieval
  - late-interaction
  - token-pooling
  - synthetic-data
  - entities/jeremy-howard
  - entities/omar-khattab
  - entities/antoine-chaffin
  - entities/benjamin-warner
  - entities/makoto-kato
  - entities/griffin-adams
---

# Benjamin Clavié (@bclavie)

| | |
|---|---|
| **X** | [@bclavie](https://x.com/bclavie) |
| **Blog** | [ben.clavie.eu](https://ben.clavie.eu/) |
| **GitHub** | [bclavie](https://github.com/bclavie) |
| **Role** | ML Researcher at Mixedbread; PhD student at NII Tokyo (Kasys lab) |
| **Known for** | RAGatouille (3.9k★), ModernBERT co-lead, JaColBERT series, ColBERT projection research |
| **Bio** | French NLP/IR researcher based in Tokyo, Japan. Creator of RAGatouille, co-lead of ModernBERT. Bridges the gap between academic IR research and production-grade retrieval systems. Advocates for late-interaction (ColBERT) over single-vector dense embeddings. |

## Overview

Benjamin Claviéはフランス出身のNLP/情報検索(IR)研究者で、現在は**Tokyo, Japan**を拠点に**Mixedbread**でML R&Dに従事し、**National Institute of Informatics (NII)** のKasys lab（指導教員: Makoto P. Kato教授）でPhD課程在籍中。

彼の特筆すべき貢献は3つの軸に集約される：
1. **RAGatouille** — ColBERTベースの検索をPythonで数行で使えるようにしたライブラリ（3.9k+ GitHub stars）
2. **ModernBERT** — BERTスタイルのエンコーダモデルをモダンなアーキテクチャで再構築するプロジェクトの共同リード（5.5k+ GitHub stars）
3. **JaColBERTシリーズ** — 日本語検索のSOTAを達成した多言語ColBERTモデル

Claviéの哲学的立場は明確だ。「**Retrieval is the bottleneck of practical AI.**」LLMそのものではなく、検索レイヤーが実際のAIシステムの成否を分けると考える。彼のキャリアは一貫して、IR研究の実用化と民主化に捧げられている。

## Core Ideas

### 1. 「RAGは死んでいない」— 素朴RAG批判と真のRetrievalの擁護

ClaviéはHamel HusainのMastering LLMコースでの講演で、マーケティング用語としての「RAG」と、本来の検索技術としての「Retrieval」を明確に区別した。

> "RAG isn't going away. Naive methods (like basic cosine similarity) are showing their limits, pushing us toward better, more sophisticated retrieval techniques. RAG is the best way to provide models with up-to-date information. Long context windows are not a replacement for retrieval."
> — Hamel Husain's Mastering LLM course, P1: "I don't use RAG, I just retrieve documents"

彼の主張は3つのポイントに集約される：

- **単一ベクトル検索の限界**: 文書全体を1つのベクトルに圧縮するdense retrievalは、情報のボトルネックとなる
- **巨大コンテキストウィンドウは検索の代替ではない**: LLMの重みは固定時点でフリーズしており、新しい内部文書や最新情報を知らない
- **真のRetrievalは多角的であるべき**: BM25、ColBERT、クロスエンコーダ、メタデータフィルタを組み合わせる

> "What people often call 'RAG' is a naive brute force, single-vector semantic search. This definition was pushed heavily by marketing in 2023-2024 because it was simple to sell."
> — On the "RAG is dead" narrative

### 2. ColBERTは「セマンティックキーワードマッチャー」

ClaviéはColBERTの動作原理を独自の言葉で簡潔に表現する：

> "I like to explain ColBERT as a `bag-of-embeddings` approach... Just like bag-of-words, it works on small information units, and represents a document as the sum of them... ColBERT is a semantic keyword matcher. It leverages the power of strong encoder models, like BERT, to break documents into token-level embeddings."
> — RAGatouille documentation, "Late-Interaction" section

この比喩は重要だ。ColBERTを「高密度ベクトル検索の一種」と捉えるのではなく、**キーワード検索のセマンティック版**として位置づけることで、なぜlate-interactionがdense retrievalより汎化性能が高いかを直感的に説明できる。

### 3. MaxSimの勾配特性と投影層の重要性

2025年のarXiv論文「Simple Projection Variants Improve ColBERT Performance」で、ClaviéはColBERTのMaxSim演算子が学習 dynamics に与える影響を初めて体系的に分析した。

> "MaxSim has pretty cool learning properties."
> — On ColBERT's late-interaction architecture

> "Multi-vector dense retrieval methods like ColBERT systematically use a single-layer linear projection to reduce the dimensionality of individual vectors. In this study, we explore the implications of the MaxSim operator on the gradient flows of the training of multi-vector retrieval models."
> — arXiv:2510.12327 (2025)

彼らの発見は画期的だった：
- FFNやGLUを投影層に使うだけで、線形投影より**2 NDCG@10ポイント以上**改善
- MaxSimは勾配フローに独特の特性を持ち、適切な投影設計で増幅できる
- この改善は追加パラメータなしで達成可能

### 4. 軽量モデルの哲学 — 「Small but Mighty」

Claviéは一貫して「巨大モデルより賢い設計」を提唱する：

> "Our 17 million parameter model... comfortably outperforms ColBERTv2. And it does so while scaling exceptionally well across datasets and tasks, with an incredibly low memory footprint."
> — Mixedbread blog on mxbai-edge-colbert-v0 (2025)

彼の軽量モデル哲学は3つの原則からなる：
1. **ModernBERTアーキテクチャの効率性** — unpadding + flash attention 2
2. **極小投影次元** — 17Mモデルで48次元（従来の1/3）
3. **Muon optimizerの適応** — late-interactionモデルに効果的

### 5. MLの民主化とエコシステム問題

2024年2月のブログ「Questions & Answer(s)」で、ClaviéはML業界の根本的な問題を指摘した：

> "For a long time now, I've been of the opinion that the democratisation of ML has an ecosystem problem... ML as a whole rarely feels like pure research: to me, it's an R&D field, although with heavy emphasis on the D."
> — ben.clavie.eu/posts/answer/ (Feb 4, 2024)

> "To the end user, ML isn't an end, it's the means to one."
> — On the purpose of ML tooling

> "I think ML developments are incredibly exciting, and we need to continue to work on bridging the gap between ML-as-a-commodity-for-ML-practitioners to ML-as-a-commodity-for-everyone."
> — On the future of ML

この視点は彼の**RAGatouille哲学**の根幹だ：「state-of-the-art researchとalchemical RAG pipeline practicesのgapを埋める」

### 6. 研究と開発の橋渡しとしてのオープンソース

Claviéのオープンソースへの姿勢はJeremy HowardのAnswer.AI哲学と深く共鳴する：

> "I feel like the philosophy of Answer.AI is about as close to a perfect match to my own as you're going to get... We don't know much about what will come next, and even less about what the path forward looks like. What I do know for sure is that we need to tinker and try new things."
> — On joining Answer.AI (Feb 2024)

> "It's important that we nurture an open IR community to see the same kind of growth experienced by NLP/Language Modeling."
> — On the state of Information Retrieval

### 7. トークンプーリング — 冗長性の削減

> "The core idea of ColBERT, funnely enough, is to go against pooling as it's most commonly performed: into a single-vector. On the other hand, we believe that introducing a small degree of pooling could go a long way!"
> — Answer.AI blog, "A little pooling goes a long way for multi-vector representations"

> "Not all tokens are created equal... somewhat redundant semantic information, meaning keeping all of them is likely not useful."
> — On token pooling intuition (tf-idf analogy)

### 8. 健康と生産性 — 「Working While Sick」哲学

ClaviéはMLコミュニティで珍しく、健康問題と生産性の関係について率直に語っている：

> "We all do stuff, and we all feel like it's not good enough. I think part of working well when you're unwell is accepting that, yeah, you're not gonna be 100% productive all the time."
> — ben.clavie.eu/posts/sick/

> "Everyone is struggling in some way. Every single person with major achievements definitely has periods where things go less smoothly, they're more tired, they're sick, things don't work. And from my experience and private chats, they, too, second-guess themselves."
> — On impostor syndrome and productivity

> "Do work. Put things out there. If it's not good, you'll learn, but eventually, you'll put something out there that is good."
> — Advice for working under constraints

## Timeline

| Date | Event |
|------|-------|
| ~2017 | First publication: "Employing ML techniques for detection and classification of phishing emails" |
| 2017–2018 | NLP Engineer at Biggerpan (Paris) — NLP × cybersecurity research |
| 2018 | NLP Engineer at **LexisNexis** (Paris) — French transformer-based legal language modeling; **put models in production in 2018** |
| 2018–2019 | Computing studies at Edinburgh Napier University |
| 2019–2020 | MScR in AI at **University of Edinburgh**, School of Informatics |
| 2019-12 | Published "EduBERT: Pretrained Deep Language Models for Learning Analytics" at IEDM |
| 2020–2021 | Research/Teaching Assistant at Edinburgh under **Kobi Gal** |
| 2021–2022 | Lead Data Scientist at **Jus Mundi** (LegalTech) — domain-specific LMs for international arbitration; secured GENCI GPU grant |
| 2022–2024 | ML Lead at **Bright Network** — LLM synthetic data for skill matching; 25pt Recall@5 improvement at RecSys |
| 2023-12 | Created **RAGatouille**; published JaColBERT |
| 2024-02 | Blog: "Questions & Answer(s)" — ML ecosystem philosophy |
| 2024-03 | Joined **Answer.AI** (co-led by Jeremy Howard) |
| 2024-05 | Began co-leading **ModernBERT** with Benjamin Warner & Antoine Chaffin |
| 2024-08 | Published token pooling research for ColBERT |
| 2024-08 | "Small but Mighty": answerai-colbert-small-v1 |
| 2024-12 | ModernBERT paper: arXiv:2412.13663 |
| 2024-12 | JaColBERTv2.5 published |
| 2025 | JaColBERTv2.5 in Journal of NLP (vol. 32, pp. 176–218) |
| 2025 | "It is all in the [MASK]" in Natural Language Processing Journal (vol. 11) |
| 2025–present | Researcher at **Mixedbread** (Tokyo office) |
| 2025–present | PhD student at **NII Tokyo**, Kasys lab (Prof. Makoto P. Kato) |
| 2025-10 | arXiv:2510.12327 — "Simple Projection Variants Improve ColBERT Performance" |
| 2025-10 | arXiv:2510.14880 — "Fantastic (small) Retrievers and How to Train Them: mxbai-edge-colbert-v0" |
| 2026-02 | Late Interaction Workshop at ECIR 2026 (main organizer) |
| 2026-03 | **Wholembed v3** リリース — 初のセマンティック検索がBM25を凌駕（LIMITベンチマーク） |
| 2026-03 | Mixedbread Search Public Beta — agentic search対応、sub-90ms検索レイテンシ |
| 2026-03 | incompebench-lenient/strict データセット公開 |

## Recent Themes (2025–Present)

**Mixedbreadでのマルチモーダル検索:** Claviéは現在Mixedbreadで「ever-better multimodal retrieval systems」の研究開発をリード。ColPali/ColQwenの系譜を継ぐ画像-テキスト横断検索に取り組んでいる。

**Edge ColBERTの最前線:** mxbai-edge-colbert-v0（17M/32Mパラメータ）は、CPU推論でも実用的なColBERTモデルとして注目を集めている。投影次元48でColBERTv2を上回る性能は、「巨大モデル信仰」への明確なアンチテーゼ。

**Wholembed v3 — セマンティック検索のパラダイムシフト (2026-03):** ClaviéはMixedbreadで、**初のセマンティック検索がBM25を凌駕するモデル**をリリース。LIMITベンチマークにおいてRecall@5で92.45（BM25: 85.7, Voyage 4 Large: 1.85）を達成。これは「semantic search has a hard ceiling」という通説を覆す画期的な結果。Wholembed v3はオムニモーダル（テキスト、オーディオ、画像、動画）かつ100+言語対応のlate-interactionモデルで、Mixedbread Searchのデフォルトエンジンとなった。BrowseComp-Plus（830件の複合検索クエリ）においても、エージェントの検索失敗率を劇的に低減。

> "We built Wholembed v3 to tackle current challenges, rather than simply improve on largely solved ones."
> "Search doesn't need to be complicated, it just needs to be good."
> "Retrieval is at the core of most agentic applications. For AI systems to be truly powerful, they need to be grounded in relevant knowledge."
> — Mixedbread Wholembed v3 release blog (March 2026)

**Mixedbread Search — Agentic Search対応 (2026-03):** 従来RAGは人間が書いたクエリを前提としていたが、AIエージェントによる自律的検索（agentic search）に最適化。sub-90msの検索レイテンシとsub-120msのリランキングを実現。Vercel Native Integrationも提供。

**PhD研究:** NII TokyoのKasys labで情報検索・エンコーダモデル・言語モデリングを研究。教授はMakoto P. Kato（筑波大学/NII）。

**Late Interaction Workshop:** ECIR 2026で初のLate Interaction Workshopを主催。ColBERTファミリーの研究者コミュニティを形成する役割を果たしている。

**オープンソースツールチェイン:** RAGatouille → rerankers → byaldi → PyLateと、IRツールチェーン全体をカバーするエコシステムを構築。

## Influence Metrics

| Project | Stars/Downloads | Significance |
|---------|----------------|-------------|
| **RAGatouille** | 3,900+ ★, 260+ forks | Python ColBERT retrievalのde facto standard |
| **ModernBERT** (co-lead) | 5,500+ ★ | BERT現代化の旗頭 |
| **mxbai-embed-large-v1** | 22M+ downloads | Mixedbreadの主力embeddingモデル |
| **JaColBERTv2.5** | SOTA Japanese retrieval | 130M paramsで日本語検索SOTA |
| **ColBERT model (HF)** | 1,500+ downloads | 主要ColBERT retriever |
| **Wholembed v3** | SOTA multimodal retrieval | LIMIT: Recall@5 92.45 (BM25超え) |
| **Google Scholar** | ~1,000+ citations (2024: 725) | 急成長中の被引用数 |

## Key Quotes Collection

> "Bridging the gap between state-of-the-art research and alchemical RAG pipeline practices."
> — RAGatouille README

> "ML is infrastructure now, and it's infrastructure whose total addressable market is just about everyone."
> — Questions & Answer(s) blog (Feb 2024)

> "I'm not, currently, an academic, although I am affiliated with the National Institute of Informatics (NII) in Tokyo. I think that it's important that we nurture an open IR community to see the same kind of growth experienced by NLP/Language Modeling."
> — About page

> "We don't know much about what will come next, and even less about what the path forward looks like. What I do know for sure is that we need to tinker and try new things."
> — On joining Answer.AI

> "ColBERT has always been powerful, and used by specialists. RAGatouille's contribution has been to bridge the excellent Research work with the constraints of Development."
> — On RAGatouille's role (echoing Omar Khattab)

> "A funny example I have is my talk at Hamel's Mastering LLM course... I was second-guessing whether it was good enough right up until I delivered it."
> — On impostor syndrome (Working while sick)

> "Everyone with major achievements definitely has periods where things go less smoothly. They, too, second-guess themselves."
> — On the universality of struggle

## Related People

- **[[entities/jeremy-howard]]** — Answer.AI共同創設者。Claviéが2024年に参加。fast.ai哲学の影響を強く受ける
- **[[entities/omar-khattab]]** — ColBERT/DSPy発明者（Stanford）。ClaviéのColBERT研究の直接的インスピレーション
- **[[entities/benjamin-warner]]** — ModernBERT共同リード、fastkmeans共著者
- **[[entities/antoine-chaffin]]** — ModernBERT共同リード、PyLate開発者
- **[[entities/makoto-kato]]** — ClaviéのPhD指導教員（NII Tokyo/Kasys lab）
- **[[entities/griffin-adams]]** — ColBERT token pooling共著者
- **[[entities/rikiya-takehi]]** — mxbai-edge-colbert-v0主著者（Waseda Univ/Mixedbread intern）
- **[[entities/xianming-li]]** — Mixedbread/Wholembed v3共著者、ECIR 2026 LIR Workshop co-organizer
- **[[entities/tom-aarsen]]** — Hugging Face、PyLateコントリビューター、ECIR 2026 LIR Workshop co-organizer

## Related Concepts

[[concepts/colbert]], [[concepts/ragatouille]], [[concepts/modernbert]], [[concepts/information-retrieval]], [[concepts/late-interaction]], [[concepts/token-pooling]], [[concepts/synthetic-data]], [[concepts/embeddings]], [[concepts/rag]], [[concepts/jacolbert]], [[concepts/mxbai-embed]]

## Sources

- https://ben.clavie.eu/ — Personal blog
- https://ben.clavie.eu/about/ — About page (detailed project list)
- https://ben.clavie.eu/posts/answer/ — "Questions & Answer(s): thoughts and joining Answer.AI" (Feb 2024)
- https://ben.clavie.eu/posts/sick/ — "Working while sick" (personal philosophy on health/productivity)
- https://ben.clavie.eu/ragatouille/ — RAGatouille documentation and philosophy
- https://github.com/bclavie/RAGatouille — RAGatouille repository (3,900+ ★)
- https://github.com/AnswerDotAI/ModernBERT — ModernBERT repository (5,500+ ★)
- https://arxiv.org/abs/2412.13663 — ModernBERT paper (Dec 2024)
- https://arxiv.org/abs/2510.12327 — Simple Projection Variants Improve ColBERT Performance (Oct 2025)
- https://arxiv.org/abs/2510.14880 — Fantastic (small) Retrievers and How to Train Them: mxbai-edge-colbert-v0 (Oct 2025)
- https://www.mixedbread.com/blog/edge-v0 — mxbai-edge-colbert-v0 blog post
- https://parlance-labs.com/education/rag/ben.html — Mastering LLMs talk transcript
- https://www.answer.ai/posts/colbert-pooling.html — Token pooling blog post
- https://huggingface.co/bclavie — HuggingFace profile (72 followers, 53 models)
- https://scholar.google.com/citations?user=vuMln98AAAAJ — Google Scholar profile
- https://mixedbread.com/blog/wholembed-v3 — Wholembed v3 release blog (March 2026)
- https://www.lateinteraction.com/ — Late Interaction Workshop @ ECIR 2026 (main organizer)
- https://mixedbread.ai/changelog — Mixedbread platform changelog
