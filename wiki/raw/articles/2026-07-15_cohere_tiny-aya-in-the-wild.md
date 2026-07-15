---
title: "Tiny Aya Expedition Drives Multilingual Innovation"
source: "Cohere Blog"
url: "https://cohere.com/blog/tiny-aya-in-the-wild"
scraped: "2026-07-15T06:00:12.253046+00:00"
lastmod: "2026-07-14"
type: "sitemap"
---

# Tiny Aya Expedition Drives Multilingual Innovation

**Source**: [https://cohere.com/blog/tiny-aya-in-the-wild](https://cohere.com/blog/tiny-aya-in-the-wild)

Key takeaways
Accessible
multilingual
models
drive
innovation:
Tiny Aya’s open-weight, lightweight design enables builders worldwide to create practical AI solutions, from educational tools to on-device assistants, without requiring heavy hardware.
Multilingual
safety
requires
nuanced
evaluation:
Projects revealed that safety behavior shifts dramatically under code-mixed prompts and cross-lingual misalignment, highlighting the need for new evaluation frameworks beyond single-language benchmarks.
Local
deployment
unlocks
real-world
impact:
Teams developed compression techniques, synthetic data pipelines, and privacy-preserving tools to make multilingual AI usable on phones and offline, expanding access to underrepresented languages.
Language
understanding
goes
beyond
translation:
Research demonstrated deep semantic cross-lingual transfer, with Tiny Aya rivaling larger models in tasks like word-sense disambiguation and even showing sensitivity to programming language syntax.
Tiny Aya is Cohere Labs' answer to a familiar problem: most AI is built for a handful of languages and needs serious hardware to run.
Tiny Aya
is open-weight, strong across 70+ languages, and light enough to run locally, even on a phone.
Shortly after release, we launched Expedition Tiny Aya, a mentor-supported research program to put the model in the hands of builders, researchers, students, and practitioners around the world, and see what they build with it. Alongside the growing body of community projects, the
research behind Tiny Aya
was recently accepted to COLM 2026, underscoring the model's impact as both a practical foundation for multilingual AI and a contribution to the research community.
What follows is an overview of what emerged from the Expedition. Projects from this initiative yielded insights across four key themes: education and learning, building safer multilingual AI, accessibility and local deployment, and language understanding and processing. In each area, a shared pattern holds: meaningful AI innovation thrives with accessible models, strong mentorship, and the freedom to explore problems that matter locally.
Theme 1: Education and learning
Access to quality education remains a global challenge, particularly in multilingual communities. Expedition teams tackled this by creating tools that make learning more accessible and effective.
Tiny Aya Math Edition: Solving math with transparent reasoning,
Katrina Lawrence, Danylo Boiko, Jing Guo, Shubham Bari, Rabius Sany — with Cohere mentor Nikolas Gritsch
Teaching Tiny Aya to show its work (breaking solutions into ideas, lemmas, sketches, and final answers) didn't guarantee correct math, but it surfaced clear tradeoffs between how a model organizes its reasoning and how well it actually performs. This team explored whether structured reasoning could improve mathematical problem solving. Alongside the project, the team released a
public multilingual Math Olympiad benchmark dataset
, which served as the foundation for many of their experiments. The work remains ongoing: the team is continuing model training, investigating new methods through a series of research papers, and plans to publish a comprehensive paper in the coming months.
Kids Companion: Offline multilingual education,
Batuhan Aktas, Yuvraj Singh, Fatih Bugra Akdogan — with Cohere mentor Viraat Aryabumi
The team built a
child-safe AI voice assistant that works entirely offline
. They combined Tiny Aya with speech recognition and text-to-speech systems, specifically designed for young users. Beyond the prototype, they developed a
multilingual benchmark for evaluating child-focused AI systems
, expanding children's conversations across dozens of languages to assess safety, educational value, and age-appropriate responses. Together, the voice companion and benchmark provide both a practical tool for young learners and an open resource that can help future researchers study multilingual AI safety and performance across diverse linguistic and cultural contexts, as described in their
accompanying blog post
.
Theme 2: Building safer multilingual AI
As models become increasingly multilingual, safety cannot be treated as a single-language problem translated outward. Instead, it becomes a question of how alignment behaves under linguistic and cultural interference.
Mix, Fine-Tune, Break: Testing multilingual safety with mixed languages
,
Tanav Singh Bajaj, Jasmine Zou, Elena Dobre, Naufal Adityo, Srimoyee Mukhopadhyay, and Shayam Shamsi — with Cohere mentorship from Charlie Chen
This team investigated how Tiny Aya's safety behavior changes under code-mixed prompting, where conversations naturally blend multiple languages, dialects, and scripts. Their experiments showed that safety evaluations can produce markedly different results when languages are mixed rather than used in isolation,
revealing blind spots that may be missed by traditional multilingual benchmarks
. Their work highlights how evaluating multilingual safety requires fundamentally different approaches than traditional methods, exposing important gaps in current alignment measurement frameworks.
Cross-Lingual Emergent Misalignment: Stopping safety issues crossing languages
,
Joana da Matta, Anu Adesina, Akanksha Devkar, Mayank Bhaskar, Ayesha Imran, and Almustapha Yusuf — with Cohere mentorship from Daniel D’souza
This team explored what happens when unsafe behavior learned in one language appears in another. Through mechanistic interpretability, they found evidence that certain directions associated with misalignment may generalize between languages, though transfer strength varied significantly across language pairs. This suggests multilingual models can share underlying safety-relevant representations, but in more nuanced ways than previously thought. The team has submitted to a major conference and their work will be made public soon.
Context Robustness: Understanding cultural conflicts in multilingual AI,
Ankita Maity, Van Ngo, Tanay Nagar, Henok Ademtew, and Sajag Swami — with Cohere mentorship from Nikita Moghe
This team examined how multilingual models respond when cultural signals, language, and surrounding context point in different directions.
Their experiments revealed
that models frequently rely on shallow cues rather than robust cultural understanding, with behavior shifting in surprising ways when language, geography, and context were manipulated. As Ankita Maity later reflected in a
personal write-up about the experience
, the project emerged from a desire to explore questions that do not fit neatly into existing benchmarks or evaluation frameworks. Their findings challenge the assumption that multilingual competence implies cultural competence and point to the need for more rigorous ways of evaluating cultural understanding in language models.
Theme 3: Accessibility and local deployment
A new challenge emerges once models are no longer confined to the cloud: how to make them usable under real-world hardware, bandwidth, and privacy constraints. Expedition teams tackled this challenge from multiple angles, developing new approaches to model compression, local deployment, multilingual data creation, and privacy-preserving applications.
Tiny Aya-Translate: Creating speech translation for rare languages,
Alper Balbay, Dhruv Jain, Ömer Yentür, Ananya, Ahmet Erdem Pamuk, Mayank Bhaskar, and Pravan — with Cohere mentorship from Irem Ergun
This team addressed one of the biggest bottlenecks in multilingual speech AI: the lack of high-quality training data for many language pairs. Focusing on Hindi and Turkish, they built a
synthetic data generation pipeline
capable of producing large-scale speech-to-speech translation datasets, with the goal of creating more than 1,300 hours of training data. Rather than starting with model architecture, they concentrated on the underlying infrastructure, developing tooling, workflows, and evaluation processes that could unlock speech translation research in under-resourced languages. Whether through the resulting translation model or the open datasets and data-generation pipeline, their work aims to make multilingual speech research more accessible to the broader community, as described in their
blog post
.
DocuNative: Helping newcomers navigate documents privately
,
Olena Bugaiova, Sudhanshu Mishra, Wahyu Dwi Nugraha, Randy Christian Saputra, Adnan El Assadi, Paarth Sharma, and Abhishek Thomas — with Cohere mentorship from Ali Edalati
For newcomers navigating complex paperwork, the DocuNative team developed a system that helps users understand important documents while keeping sensitive information entirely on-device. Built around Tiny Aya, the project combines multilingual retrieval and question answering, showing that retrieval quality depends strongly on language alignment between documents and queries. The
DocuNative work
was done alongside related efforts such as Tiny Aya Vision (below), and reflects broader exploration into practical multilingual AI tools for real-world document understanding. Continued evaluations, including benchmarks such as
NorEval
, suggest strong performance for models in this size class across Norwegian language settings.
Tiny Aya Vision: Making multilingual vision accessible,
Michael Chang, Gusti Winata, Suparnojit Sarkar, Siddhant, Tahseen Rayhan, Bhavesh Kalisetti, and Trishanu Das — with Cohere mentorship from David Rau
This team explored whether lightweight multilingual vision-language systems could be made accessible to researchers without large-scale compute resources. Rather than training a multimodal model from scratch, they connected existing visual encoders to Tiny Aya while keeping most parameters frozen. This parameter-efficient approach produced surprisingly strong results, nearly doubling performance in some experiments while dramatically reducing training requirements. The implementation and experiments are available in their
open-source repository
.
Tiny Facade: Enabling local multilingual assistants,
Bronson Bakunga, Kato Steven Mubiru, Saad Nasir, Ojonye Agwu, Alex Gimei, and Adnan El Assadi — with Cohere mentorship from Julia Kreutzer
This team demonstrated that multilingual tool use could run entirely on-device. In their
accompanying write-up
, they describe a
system that converts user requests into structured JSON tool calls
across dozens of languages, enabling Tiny Aya to interact with external tools under tight hardware constraints. The project includes heavily optimized
4-bit quantized model variants
, designed for efficient on-device inference, as well as an Android-based tool-calling infrastructure that exposes multilingual capabilities to mobile applications. Their experiments show that Tiny Aya remains remarkably effective even at extreme compression, making multilingual assistants significantly more accessible to developers working with limited compute resources.
Language-Aware Quantization: Preserving multilingual performance under compression
,
Vivek Silimkhan
,
Danylo Boiko, Nirmal Thomas, Srimoyee Mukhopadhyay — with Cohere mentorship from Saurabh Dash
Compressing language models is essential for deployment on phones, laptops, and other resource-constrained devices, but multilingual models introduce an additional challenge: compression does not affect all languages equally. This team investigated language-aware quantization strategies for Tiny Aya, exploring how model compression impacts performance across diverse languages and whether multilingual capabilities can be preserved more effectively through targeted optimization. Their findings suggest that treating multilingual compression as a single uniform problem can obscure important language-specific tradeoffs. By better understanding how quantization affects different linguistic communities, the project contributes practical techniques for making multilingual AI more accessible without disproportionately sacrificing performance in lower-resource languages.
Theme 4: Language understanding and processing
True multilingual competence requires deep semantic understanding, not just translation. Teams pushed the boundaries of language comprehension across diverse contexts.
Cross-Lingual Word-Sense Disambiguation: Figuring word meanings across languages,
Michele Ciletti, Alisa Banerjee, Hamza Shezad, Sirichada Wattanasiritanawong, and Ahanaf Aziz — with Cohere mentorship from Ammar Khairi.
This team tackled the deceptively difficult challenge of determining which meaning of a word is intended from context. They trained and evaluated Tiny Aya models across more than eighteen languages, observing strong cross-lingual transfer, with some configurations achieving performance competitive with substantially larger models. Their work also introduced
new resources for multilingual semantic evaluation
, including a publicly released dataset for cross-lingual word-sense disambiguation tasks.
Language, Decoded: How code language affects AI behavior,
Madi Edgar, Saad Bazaaz, Rashik Shahjahan, Rafay Mustafa, Khojasteh Mirza, Sarah Jawaid, and Sohaib Bazaz — with Cohere mentorship from Tom Sherborne
In an unexpected direction, this team turned attention to programming languages rather than natural language. They explored what happens when traditional programming keywords are replaced with equivalents from other languages. The results revealed that the language used within code can meaningfully influence model behavior, sometimes improving performance and sometimes introducing unexpected side effects such as code leakage. As part of their forthcoming blog post, the team reflects on these early findings and ongoing exploration at the intersection of multilingual representation learning and code generation.
Inside Tiny Aya: Looking inside multilingual representations
,
Farseen Shaikh, Matthew Nguyen, and Tra My (Chiffon) Nguyen — with Cohere mentorship from Tom Hosking
Rather than evaluating what Tiny Aya says, this team explored what happens inside the model as it processes more than seventy languages. By training sparse autoencoders on Tiny Aya's internal representations, they found that most features are shared across languages, while a much smaller set specialize in particular scripts or languages. They also uncovered surprising differences in how densely different languages are represented internally, without finding evidence that these differences directly explain model quality. By openly releasing their interpretability tools and analyses, the project provides new infrastructure for studying how multilingual language models organize knowledge beneath the surface, opening new directions for multilingual interpretability research.
Throughout this journey, the dedication of our Expedition teams and the guidance of Cohere mentors made these breakthroughs possible. We extend our gratitude to all contributors whose passion and expertise brought these projects to life.
This global collaboration, spanning time zones, cultures, and working styles, proves that great ideas emerge anywhere with opportunity and support. Looking ahead, Expedition Tiny Aya is supporting the groundwork for a future where technology adapts to people, not vice versa. Through open-source datasets, benchmarks, and methodologies, we accelerate progress toward AI that serves as a bridge between languages, cultures, and communities, democratizing knowledge and opportunity worldwide.
The momentum behind Tiny Aya continues to grow. Alongside the open-source projects featured here, the core
Tiny Aya research
was recently accepted to COLM 2026, while teams continue to produce their own papers, benchmarks, datasets, and open-source tools, including multiple winners of the recent
Hugging Face Build Small Hackathon
.
Expedition Tiny Aya is one of many initiatives within the Cohere Labs Open Science Community, a global network of researchers, students, developers, and practitioners collaborating to advance AI research in the open. Through research programs, mentorship, community events, and open-source projects, we aim to create opportunities for people from a wide range of backgrounds to contribute to the future of AI. If you're interested in community-driven research, we invite you to
learn more and get involved.
Blog
Written By
Madeline Smith
Operations and Community Manager, Cohere Labs
Tags
Research
Open Science
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
