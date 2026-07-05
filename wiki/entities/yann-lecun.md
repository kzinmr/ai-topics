---
title: "Yann LeCun"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Yann LeCun

## 📌 Basic Profile

| Item | Details |
|------|------|
| **Full Name** | Yann André LeCun |
| **Date of Birth** | July 8, 1960 |
| **Place of Birth** | Soisy-sous-Montmorency, France |
| **Nationality** | French-American |
| **Education** | ESIEE Paris (1983, Electrical Engineering), Université Pierre et Marie Curie (PhD, 1987) |
| **Affiliation** | NYU Silver Professor, Former Meta Chief AI Scientist (2013-2025) |
| **Current Role** | AMI Labs Executive Chairman (announced November 2025) |
| **Major Achievements** | Invention of Convolutional Neural Networks (CNN), 2018 ACM Turing Award |

## 🎓 Education and Early Experience

- **1983**: Diplôme d'Ingénieur (Electrical Engineering) from ESIEE Paris
- **1984-1987**: DEA and PhD from Université Pierre et Marie Curie
  - Thesis: "Modèles connexionnistes de l'apprentissage" (supervisor: Maurice Milgram)
- **1987-1988**: Postdoctoral researcher at University of Toronto (Geoffrey Hinton's group)
- **Early influences**: Learned practical craftsmanship from his father, an aeronautical engineer. Watching *2001: A Space Odyssey* around age 9 sparked his interest in intelligent systems.

## 💼 Career Timeline

| Period | Organization | Role / Key Contributions |
|:---|:---|:---|
| **1988-2002** | AT&T Bell Labs / AT&T Labs-Research | Applied neural networks to image processing. Deployed CNNs for USPS mail sorting and bank check OCR. Head of Image Processing Research Department (1996-2002). Co-developed DjVu compression technology. |
| **2002-2003** | NEC Laboratories America | Fellow. Applied scalable ML to multimedia computer vision. |
| **2003-Present** | New York University | Professor → Silver Professor (2008) → Jacob T. Schwartz Chair. Founded NYU Center for Data Science (2013). Led university-wide data science initiative (2012-2014). Taught and mentored in ML, CV, self-supervised learning. |
| **2013-2025** | Meta AI Research (FAIR) | Founding Director → Chief AI Scientist. Expanded FAIR globally (Paris, Montreal, London). Key contributor to PyTorch. Integrated AI into Meta platforms (recommendations, moderation, bias mitigation). Announced departure in November 2025 to launch an AI world model company. |

## 🔬 Major Research Contributions

### Convolutional Neural Networks (CNNs)

- **Architecture**: Inspired by Hubel & Wiesel's mammalian visual cortex structure. Convolutional layers, shared weights, pooling for position/spatial invariance.
- **Learning**: End-to-end optimization via backpropagation and stochastic gradient descent (SGD).
- **Impact**: Solved the scalability and parameter efficiency problems of fully-connected networks. Became the benchmark for image recognition and computer vision.
- **LeNet-5 (1998)**: 5-layer model, ~60K parameters. Achieved >99% accuracy on MNIST handwritten digit recognition. Deployed in AT&T and bank check reading systems.

### Energy-Based Models (EBMs) and Self-Supervised Learning

- **EBMs (2006)**: Assign scalar energy to data configurations; capture dependencies across supervised/unsupervised/semi-supervised tasks without explicit probability normalization.
- **JEPA (2022)**: `Joint Embedding Predictive Architecture` – Non-generative self-supervised framework. Predicts latent representations of masked targets via energy minimization. Focus on abstract world models, not pixel reconstruction.
  - **Extensions**: `V-JEPA` (vision), `VL-JEPA` (vision-language)
  - **LeWorldModel (March 2026)**: 15M-parameter JEPA. Stable training with simple binary loss. Enables full planning in **<1 second** on a single GPU from raw pixel input.

### Software, Datasets, and Tools

- **Lush (1990s)**: Object-oriented Lisp dialect co-developed with Léon Bottou. Accelerated numerical computation/ML prototyping.
- **DjVu (1996)**: Wavelet-based document compression separating text/background layers. Superior to JPEG for scanned documents.
- **NORB Dataset**: Stereo object images under varied lighting/pose/clutter conditions. Advanced hierarchical feature learning and semantic invariance.

## 🏆 Major Awards and Honors

- **2018**: ACM A.M. Turing Award (co-recipient with Geoffrey Hinton, Yoshua Bengio)
- **2023**: Global Swiss AI Award
- **2024**: VinFuture Prize
- **2025**: Queen Elizabeth Prize for Engineering (one of 7 co-recipients), NYAS inaugural Trailblazer Award
- **Academy Memberships**: National Academy of Sciences (2017), National Academy of Sciences USA (2021), AAAS Fellow, French Academy of Sciences
- **Honorary Doctorates**: EPFL (2018), IPN Mexico (2016), Université Côte d'Azur (2022), HKUST (2023), University of Siena (2023), University of Geneva (2024)
- **National Honors**: Chevalier of the Legion of Honour (2020)

## 💡 Strategic Insights and AI Vision

- **AI Safety and Regulation**: Advocates "objective-driven training" to mitigate risks. Warns excessive regulation may stifle innovation.
- **Post-LLM Paradigm**: Views current LLMs as "nearly obsolete for true reasoning." Champions predictive, non-generative world models (JEPA) as the path to human-like reasoning, spatiotemporal understanding, and robot planning.
- **Open Source**: Strong advocate for open-source AI development, global knowledge transfer, and transparent model deployment.
- **2025 Career Transition**: Left Meta to found AMI Labs. Aims to operationalize next-generation AI via energy-based reasoning models.

## 📜 Key Publications and Citations

- **LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998).** "Gradient-based learning applied to document recognition." *Proceedings of the IEEE*, 86(11), 2278-2324. (100,000+ citations)
- **LeCun, Y., Bengio, Y., & Hinton, G. (2015).** "Deep learning." *Nature*, 521(7553), 436-444. (100,000+ citations)
- **LeCun, Y. (2022).** "A Path Towards Autonomous Machine Intelligence." *OpenReview.*
- **LeCun, Y. (2025).** "A Tutorial on Energy-Based Learning." *Meta AI Research.*

## 🔗 Related People and Projects

- **Geoffrey Hinton**: Backpropagation collaborator. Interacted during LeCun's postdoc at U of T.
- **Yoshua Bengio**: Turing Award co-recipient. Deep learning pioneer.
- **Jürgen Schmidhuber**: CNN pioneer. Independently developed similar architectures.
- **Andrew Ng**: Collaborated at Google Brain. Contributed to deep learning popularization.
- **PyTorch**: Major contributor during Meta FAIR era. Now the de facto standard deep learning framework.
- **ImageNet**: Created by Fei-Fei Li. Greatly contributed to the development of LeCun's CNN research.

## ⚠️ Notable Events

- **November 2025**: Left Meta to found AMI Labs. Aims to operationalize AI via energy-based reasoning models.
- **2025**: Received Queen Elizabeth Prize for Engineering. Recognized for long-standing contributions to AI.
- **2024**: Received VinFuture Prize. Recognized for CNN development revolutionizing image recognition.

---

*Last updated: April 14, 2026*
*Data sources: Grokipedia, Meta AI blog, NYU profile, academic papers*
*Depth: L2 (basic profile, career, research contributions, awards) → Planned upgrade to L3 (philosophy, citation analysis, conceptual framework)*

## See Also

- [[entities/fei-fei-li]] — ImageNet creator. Collaborative relationship in computer vision and deep learning.
- [[entities/ian-goodfellow]] — Inventor of GANs. Deep learning and adversarial ML pioneer.
- [[entities/geoffrey-hinton]] — Backpropagation collaborator. LeCun's postdoc supervisor.
- [[concepts/yoshua-bengio]] — Deep learning pioneer. Co-recipient of 2018 Turing Award with LeCun.
- [[pytorch]] — Deep learning framework LeCun majorly contributed to during Meta FAIR era.
