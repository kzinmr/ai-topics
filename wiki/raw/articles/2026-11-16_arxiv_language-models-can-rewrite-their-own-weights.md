---
title: "Language Models Can Rewrite Their Own Weights (arXiv:2611.21885)"
source: https://arxiv.org/abs/2611.21885
date: 2026-11-21
type: article
sha256: c47ae55003e45d25855872c5281801b16077218d05d273930b904ba846dad0e7
---

> HN discussion: https://news.ycombinator.com/item?id=50577265 (423 pts)

[2611.21885] Language Models Can Rewrite Their Own Weights 

 Skip to main content 

 Search 

 Press Enter to search · Advanced search 

 Computer Science > Artificial Intelligence

 arXiv:2611.21885 (cs)

 [Submitted on 16 Nov 2026 ( v1 ), last revised 18 Nov 2026 (this version, v2)]

 Title: Language Models Can Rewrite Their Own Weights

 Authors: Jiajun Fan , Neil He , Changyi Yang , Andy Mao , Xi Zhu , Chaoran Cheng , Kaiqu Liang , Shuaike Shen , Zetian Li , Ruihan Guo , Ge Liu 
 View a PDF of the paper titled Language Models Can Rewrite Their Own Weights, by Jiajun Fan and 10 other authors

 View PDF 
 HTML (experimental) 

 Abstract: A language model is trained once and frozen. Making it better takes another training run, or a prompt, a harness or extra computation at inference that is gone once the task ends. We show a third way: to our knowledge for the first time, a language model rewrites its own weights by its own reasoning and becomes better, with no gradients and no training. We call this self-rewriting: the model is its own optimizer. In earlier work, a frontier model edited a much smaller one; here an open 27B model, given its weights, its graded answers and the ability to run itself, diagnoses its own failure and rewrites the weights behind it. It surpasses itself: its own edit makes it 6.6 points more accurate on problems it never saw. It keeps getting better: it tests its edits on practice problems and submits only what works, each edit improving on the last, and over eight consecutive sessions its accuracy only rises. It repairs a damaged copy of itself, like a broken robot that fixes itself without being rebuilt: the copy solves almost nothing, yet with no retraining and without ever reading the original weights, the model brings it back to over 80% of the original accuracy on image tasks it never saw. And the ability emerges with scale: in one model family, the smaller models make no edit or break themselves, and only the largest improves and repairs itself. Unlike test-time scaling, self-rewriting writes its gain into the weights, at no cost per answer; unlike training, it runs only forward passes, as serving does. The wall between training and inference is a limit of our tools, not a property of intelligence. We believe self-rewriting is a necessary step toward recursive self-improvement: a model that, like a human, does not separate training from inference could keep upgrading itself for life, with no larger model, no harness or prompt engineering, and no pre- or post-training.

 Subjects: 
 
 Artificial Intelligence (cs.AI) 

 Cite as: 
 arXiv:2611.21885 [cs.AI] 

 (or 
 arXiv:2611.21885v2 [cs.AI] for this version)

 https://doi.org/10.48550/arXiv.2611.21885 

 Focus to learn more 

 arXiv-issued DOI via DataCite

 Submission history
 From: Jiajun Fan [ view email ] 
 [v1] 
 Mon, 16 Nov 2026 20:55:08 UTC (6,363 KB)

 [v2] 
 Wed, 18 Nov 2026 08:57:59 UTC (6,379 KB)

 Full-text links: 
 Access Paper:

View a PDF of the paper titled Language Models Can Rewrite Their Own Weights, by Jiajun Fan and 10 other authors
 View PDF 
 HTML (experimental) 
 TeX Source

 view license 

 Additional Features

 Audio Summary 

 Current browse context:

 cs.AI

 < prev 
 
   |   
 next > 

 new 
 | 
 recent 
 | 2026-11 

 Change to browse by:
 
 cs 

 References & Citations

 SciX 
 Google Scholar 

 Semantic Scholar 

 export BibTeX citation 
 Loading... 

 BibTeX formatted citation

 × 

 loading... 

 Data provided by: 

 Bookmark

 Bibliographic Tools 
 
 Bibliographic and Citation Tools

 Bibliographic Explorer Toggle 

 Bibliographic Explorer ( What is the Explorer? ) 

 Connected Papers Toggle 

 Connected Papers ( What is Connected Papers? ) 

 Litmaps Toggle 

 Litmaps ( What is Litmaps? ) 

 scite.ai Toggle 

 scite Smart Citations ( What are Smart Citations? ) 

 Code, Data, Media 
 
 Code, Data and Media Associated with this Article

 alphaXiv Toggle 

 alphaXiv ( What is alphaXiv? ) 

 Links to Code Toggle 

 CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) 

 DagsHub Toggle 

 DagsHub ( What is DagsHub? ) 

 GotitPub Toggle 

 Gotit.pub ( What is GotitPub? ) 

 Huggingface Toggle 

 Hugging Face ( What is Huggingface? ) 

 ScienceCast Toggle 

 ScienceCast ( What is ScienceCast? ) 

 Demos 
 
 Demos

 Replicate Toggle 

 Replicate ( What is Replicate? ) 

 Spaces Toggle 

 Hugging Face Spaces ( What is Spaces? ) 

 Spaces Toggle 

 TXYZ.AI ( What is TXYZ.AI? ) 

 Related Papers 
 
 Recommenders and Search Tools

 Link to Influence Flower 

 Influence Flower ( What are Influence Flowers? ) 

 Core recommender toggle 

 CORE Recommender ( What is CORE? ) 

 Author 

 Venue 

 Institution 

 Topic 

 About arXivLabs

 arXivLabs: experimental projects with community collaborators

 arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

 Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

 Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

 Which authors of this paper are endorsers? |
 Disable MathJax ( What is MathJax? )
