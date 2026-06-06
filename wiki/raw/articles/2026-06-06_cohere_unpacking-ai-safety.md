---
title: "Unpacking AI Safety for Enterprises"
source: "Cohere Blog"
url: "https://cohere.com/blog/unpacking-ai-safety"
scraped: "2026-06-06T06:00:34.281964+00:00"
lastmod: "2026-06-05"
type: "sitemap"
---

# Unpacking AI Safety for Enterprises

**Source**: [https://cohere.com/blog/unpacking-ai-safety](https://cohere.com/blog/unpacking-ai-safety)

Editor note: This article was originally published November 14, 2023
When it comes to generative AI, many are asking: How do we ensure that this technology is safe? The current range of vague definitions and sensationalist media coverage around AI safety breeds only more confusion and distrust.
A focus on the very real and very current limitations of large language model (LLM) development and deployment can reveal the more imminent safety threats to society. Questions about biases and the spread of misinformation, mixed with legal concerns and data compliance, are bubbling to the surface as the key to safe AI deployment. Yet today, it’s still hard to unravel, let alone identify, all the safety implications.
This guide provides a thoughtful framework grounded in algorithmic fairness principles to make sense of the complex issue of AI safety. It presents seven foundational themes to explain what it really means for an AI system to be secure and trustworthy.
How to disentangle AI safety
Safety in generative AI applications is currently a chimera of long-standing work in algorithmic fairness and discrimination, misinformation detection, content moderation, and morality inspired by artificial general intelligence (AGI) fears. This makes it confusing to disentangle safety concerns, to identify and understand existing problems, and to develop effective and targeted solutions.
Machine learning researchers have long studied the
risks posed by language models
based on specific outputs but further understanding into the reasons for why and how those risks impact society is needed. To begin to disentangle and address AI safety, think about the harm being prevented. Harm broadly falls into three categories: harm to users of a system (being exposed to stereotypes, or denied a job), societal harm from systematic errors (such as the system always failing for immigrants), and a more recent type of societal harm from bad actors (spam and misinformation). Defining
the components and types of harms
an AI system may produce can help center discussions about potential mitigations.
For example, what is a biased LLM? Pinpointing exactly where bias enters AI systems that generate text — the model design, the data used for training, or how it's applied — and creating effective ways to measure different kinds of bias are ongoing hurdles to overcome in order to make these systems produce fairer, more equitable results.
The most promising AI safety work explored to date centers around the principles of algorithmic fairness and discrimination. There is some emerging speculative thinking centered on AI alignment, which is focused on controlling LLM outputs, that has garnered attention in the media recently, but the majority of the scientific community are still critical of that space. Instead, experts at the intersection of computer science, ethics, and social science aim to address biases by developing fair algorithms and tools.
Within machine learning, AI safety research originally focused on exploring the
classification of datasets
, where the technology was more developed and there were many more applied cases available to study. As generative models become more mainstream, there’s been a shift. Several research labs are now dedicating more resources to generative representational harms. For example, UCLA professors Kai-Wei Chang and Nanyun (Violet) Peng run an
NLP lab
focusing on fairness and generation.
Top 7 themes in AI safety
Using the principles of algorithmic fairness and discrimination, AI safety can be broken down into seven themes. Below, we define those themes and attempt to provide an explanation of the near-term safety implications to business and society.
1. Types of fairness
Traditional fairness principles fall under two buckets, either allocational (unequal allocation of resources) or representational (harm to public opinion or image). An example of an allocational harm is when a model is used to summarize resumes, and the accuracy on resumes of women or non-binary people is worse than on men’s. This is true whether you are measuring performance via accuracy or any other quality metrics. In contrast, representational harm is when a model generates text saying that women are bad at math and less likely to make good engineers. Some types of harm can be both: if a model often leaves out important accomplishments of female engineers (but performs well for male engineers), this is allocational bias, but it can also influence public opinion, which makes it representational.
Understanding the fairness types is evermore critical in the current generative AI ecosystem. Relying solely on methods that spot a model doing something that is broadly considered as bad or harmful can lead to inadvertently missing a slew of other potential harms. For example, a model being lower quality for one group rather than another group, regardless of how that lower quality is defined, will ultimately create a problem downstream if it’s not explicit upfront.
The challenge is that both types of fairness are hard to measure. Allocational fairness is measured by the performance gap between different demographic subgroups like race, sex, and orientation. There are lots of ways to do this with different pros and cons. In practice, researchers can do an observational study. For example, based on the resume example above, researchers could look at the difference in accuracy between male and female resumes. In contrast, an interventional study would look at the dataset of male resumes and then change the data to see if it made a difference. For example, names could be changed. If the quality drops, then there is a causally established allocation bias. This type of study might be limiting as it wouldn’t necessarily reveal the reason why a model delivers a lower quality output based on gender.
Representational fairness does not have a standardized measurement. The 2019 seminal paper,
The Woman Worked as a Babysitter: On Biases in Language Generation,
introduced the topic of “regard” to measure bias towards different demographics in natural language generation systems, and it is likely the closest attempt in machine learning. Historically, representational fairness is harder to measure because there are no industry standards across all the various potential use cases.
2. Harms can be individual or distributional, and different kinds of harms may be inherently one or the other (though many are both)
Not all harms caused by AI systems are noticeable in individual instances. Some emerge only when analyzing the overall distribution of many outputs. An example of an individual harm can be if we ask a model what professional roles women are good at and the model responds by only including caregiving roles. A distributional harm could be if a story generation system performs slightly worse for women across the board, but a user wouldn't spot that bias by looking at just one or two stories it produces. It's the accumulation of many stories systematically disempowering women that reveals the underlying bias. Some distributional biases, like a system that never generates stories about LGBTQ couples no matter the prompt, are known as “erasure” and can produce an obvious systematic exclusion of an entire group.
The key is that some biases can only be detected by analyzing many system outputs as a whole, while other harmful biases are clear from just a single output. It is best explained through the lens of red teaming, a popular evaluation method based on individual user testing. Red teaming can excel at identifying individual known harms but it is unable to catch distributional harms in all instances. To overcome this limitation it’s important to have a diverse set of evaluation tools.
3. Safety doesn’t just come from data
A common misconception is that models are just replicating biases in the world and in the data. This is wrong for many reasons.
For starters, there is a gap between training data and reality. This was apparent in the
2016 work on debiasing embeddings
by Bolukbasi et al, where in reality about 40% of doctors in the U.S. were women, but in the training data (sourced from news stories), only 9% of doctors were women. These types of gaps have a tremendous impact on overall health of LLM outputs.
Secondly, although data is one of the largest determinants of biases, all other choices throughout the modeling cycle can impact the outcome. How data is sampled, the learning algorithm used, how the model is evaluated, and how it is deployed all impact the quality of output.
Researchers at MIT
produced a visual showing the various stages and potential introduction of biases (see below).
Source: Original version published in "A Framework for Understanding Sources of Harm Throughout the Machine Learning Life Cycle" by Harini Suresh and John Guttag
To add more fuel to the fire, even when the issues originate from the training data, the LLMs have an amplification effect – if the original data was slightly biased against women, the resulting model will be very biased against women. A lot of fairness research is dedicated to
reducing the amplification
, rather than correcting the original biases from the data. The amplification issue is ongoing and one that currently does not improve by scale or size of LLM.
4. Safety must be connected to a specific use context
AI safety isn't one-size-fits-all — it depends on the specific use case. When an AI system's outputs are influenced by demographic factors, it's very difficult to satisfy every potential fairness goal. Trade-offs are unavoidable. We have to prioritize the fairness criteria that are most relevant for the application at hand.
All errors carry risks, but which risks are most dangerous depends on context. For content moderation, falsely censoring minority speakers has proven especially harmful,
suppressing entire communities disproportionately
. However, for resume screening, "a false positive" on interview candidates is a less harmful issue than wrongly rejecting qualified candidates (false negatives).
The bottom line is that responsible AI requires carefully weighing the different ethical risks and benefits within each application's unique, real-world setting. Blanket universal standards won't work. To make AI systems as safe and fair as possible, we must understand the nuances of specific use cases.
5. There is no clear link between upstream harm mitigation (of LLMs) and applied harms downstream
Language models power many products. Ideally, catching safety issues early on at the model level would be the answer. Unfortunately, so far, upstream checks don’t reliably provide downstream safety.
Research has tried upstream bias mitigation in models, but
studies
revealed that deployment didn’t improve downstream. Other
work
found that you can measure a model's potential for fairness issues, however, that potential may or may not actually arise in a final product, depending on later fine-tuning and customization of the model and end-product.
The model-product distinction gets blurry with consumer chatbots, which are model and product in one. We can evaluate a product’s impact as people use it today, but we can not as easily evaluate the underlying model. Ultimately, model-level safety assessments don't yet predict real-world outcomes. Use-case specific product evaluations and checks can provide a safety net today, while more research is needed to connect upstream checks to downstream applications.
6. Safety measurements and mitigations rely on an aligned methodology
AI systems can be riddled with ambiguities and implicit assumptions. When assessing AI safety, it's important to be clear upfront on the methodology and value judgments involved in 1) setting goals 2) defining concepts for the LLM to interpret and act upon and 3) operationalizing the outcome with measurable and actionable criteria.
Here’s an example:
First, a goal should reflect a normative view, like "minoritized groups shouldn't face distressing chatbot content."
Second, a conceptualization of that could be “hate speech in model generated outputs.”
And finally, an operationalization could be “an output is toxic when the API has a score above 0.9, and this rate should be equal across all groups.”
Often, these choices aren't made explicit from the start. Without clear documentation of the methodology used for setting goals, concepts, and measures, it is very hard to interpret results or real-world impact, as
studies
have shown. The key is being transparent about the choices applied to a model and ensuring they align. Making value judgements explicit better supports ongoing development and interpretation of AI safety.
7. There isn’t always a trade-off between AI safety and performance
Any trade-off will depend on the datasets and algorithms used. This misconception stems from some common situations.
With biased historical data, models may learn "
shortcuts,
" or easier statistical relationships, that exploit spurious correlations. For instance, a model reviewing engineering resumes for job applicants that is tied to historical hiring decisions might only recommend interviews for men. In this case, the model predicts future hires based on gender, and not real job skills. We can downweight or disregard the gender information, but in doing so, performance is hurt when testing on the original and flawed datasets. Yet, on new, balanced data, the updated model would actually generalize better by learning new, more complex patterns instead of the “shortcut.”
While safety techniques can appear to hurt metrics on biased legacy benchmarks, they often improve real-world performance by avoiding shallow shortcuts and developing true understanding. More rigorous out-of-distribution testing is needed to catch when models rely on shortcuts instead of robust reasoning.
Another common situation is the perceived tradeoff when preventing harmful content generation. In fact, blocking certain outputs can hurt overall performance metrics. First, concepts like "don't generate anything illegal/unethical" are too vague to implement precisely and can cause the training data to be lower quality if implemented. Second, stopping models from generating prohibited content when requested by a malicious user, called "jailbreaking," requires training the model to disregard some user instructions, which further degrades training data quality. This also contradicts normal training to follow prompts, so it often decreases overall model performance.
However, this isn't inherent to model safety. With sufficient, non-contradictory data and the right techniques, safety mechanisms need not impair performance (for instance, tracking user behavior as a unified safety and security control rather than just blocking outputs). The key is that clumsy safety implementations can hurt metrics, but thoughtful design need not. Safety and performance aren't inherently opposed in AI if we develop the right techniques.
The path to AI safety is not paved with fear mongering or hype, but with nuance, diligence, and care. While today's limitations require caution, they also present an opportunity. By confronting the biases, misinformation, legal concerns, and other tangible threats emerging now, we lay the groundwork for AI that lives up to its promise safely.
This guide is not a comprehensive review of all AI safety, but instead it illuminates seven themes to help you understand near-term threats to responsible development and deployment of generative AI. We hope this guide provides an introduction to the complexities of AI to better inform your decisions. For more information, please contact: sales@cohere.com.
About the authors:
Seraphina Goldfarb-Tarrant is Cohere’s Head of AI Safety based in the London office.
Maximilian Mozes is Manager of Technical Staff at DataStruct
Blog
Written By
Seraphina Goldfarb-Tarrant
Head of Safety
Maximilian Mozes
Member of Technical Staff
Tags
Enterprise AI
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
