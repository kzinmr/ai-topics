---
title: "Augmenting Human Preference in Complex Domains"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/augmenting-human-preference-in-complex-domains"
scraped: "2026-09-18T06:00:52.806794+00:00"
lastmod: "2026-09-17T17:00:00.000Z"
type: "sitemap"
---

# Augmenting Human Preference in Complex Domains

**Source**: [https://www.harvey.ai/blog/augmenting-human-preference-in-complex-domains](https://www.harvey.ai/blog/augmenting-human-preference-in-complex-domains)

We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
Company
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Agents
→
Purpose built agents execute complex legal work end to end.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Spaces
→
Work with legal teams across organizations in secure, shared spaces.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Introducing Memory
New
→
Your preferences carried across Harvey so every response comes back consistent with how you work.
Innovation
→
Scale expertise and impact to drive firmwide transformation.
Litigation
→
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Transactional
→
Accelerate due diligence, contract analysis, and review with precision and control.
In-House
→
Streamline work and shift focus to strategy and speed.
Law Firms
→
Deliver your firm's best work on every matter, with more time for clients.
Mid-Sized Firms
→
Drive outsize impact with tools built for lean teams.
A New Era of Collaboration for Legal and Professional Services
→
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Blog
→
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
→
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
→
Resources for maintaining a uniform and professional presentation of the Harvey brand.
Research
→
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
→
Who we are and what we're building.
Careers
→
Join our team and help Harvey shape the future of professional services.
Newsroom
→
Press releases and partnership announcements.
2025 Year in Review
→
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Login
Request a Demo
Platform
Overview
A unified view of how Harvey's products work together to support your entire practice.
Agents
Purpose built agents execute complex legal work end to end.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Spaces
Work with legal teams across organizations in secure, shared spaces.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Introducing Memory
New
Your preferences carried across Harvey so every response comes back consistent with how you work.
Solutions
Innovation
Scale expertise and impact to drive firmwide transformation.
Litigation
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Transactional
Accelerate due diligence, contract analysis, and review with precision and control.
In-House
Streamline work and shift focus to strategy and speed.
Law Firms
Deliver your firm's best work on every matter, with more time for clients.
Mid-Sized Firms
Drive outsize impact with tools built for lean teams.
A New Era of Collaboration for Legal and Professional Services
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Customers
Security
Resources
Blog
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
Resources for maintaining a uniform and professional presentation of the Harvey brand.
Research
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
About
Who we are and what we're building.
Careers
Join our team and help Harvey shape the future of professional services.
Newsroom
Press releases and partnership announcements.
2025 Year in Review
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Request a Demo
Login
US
EU
AU
Insights
Augmenting Human Preference in Complex Domains
Early results from expert-tuned Generative Reward Models.
by
Julio Pereyra
•
Sep 17, 2026
Lawyer judgment is one of our most valuable resources at Harvey. It is the gold standard for how we determine whether our AI systems are improving and whether they’re good enough to solve complex legal problems.
The most common way we do this is side-by-side evaluations. A lawyer is shown two outcomes for the same task and asked to pick which they prefer and explain why. These judgments are then aggregated into metrics we use to determine whether our systems are improving and how they could perform better.
Reinforcement learning from human feedback (RLHF) is the standard way of moving this approach from evaluation to training. These aggregated human judgments are used to train a reward model that predicts which of multiple outcomes will align with human preference and the model being RLHF’d is nudged repeatedly towards the most preferred version. Good reward models require human preferences that are both clear and homogenous.
Lawyer judgments on complex environments are neither. This is true in the real world, where even high-skill lawyers (trial judges) who have weeks or months to come to a conclusion are disagreed with by other high-skill lawyers (appellate judges)
10-15%
of the time. This is even more true in evaluations where giving lawyers weeks per judgment would be prohibitively expensive and where preference turns on a mix of more subjective factors like tone, style, reasoning, and more.
As we look to continue to improve Tenet, this is the key problem to solve. We think the solution lies in giving lawyers more leverage to both make better informed preference judgements and to encode their preferences at scale through generative reward models (“GRMs”). In this post, we discuss the state of lawyer human preference, GRMs, and how lawyer-tuned GRMs help close the gap towards more effectively understanding and post-training useful models for law.
Lawyer Judgment is Hard to Align
We run a lot of human preference studies at Harvey. For all of the advancements in rubrics and LLM judges, they still remain a key component of what Anthropic correctly calls
“the Swiss cheese”
approach of effective evaluation. What we find is that lawyers agree directionally on which response is better at scale, but tend to only modestly agree on any particular task.
Below is a human preference study we ran with Snorkel when determining whether Kimi K3 was a good base model for training Tenet. We compared it to four other (at the time) LAB-leading models on 24 LAB tasks, with each task rated by 3 lawyers from the relevant practice area.
Figure 1: Human preference model ELO
While at scale, lawyers separate the models into clear performance tiers, the actual lawyer votes are muddier. Raters agree unanimously in only 25% of match ups and their odds of agreeing is only a bit better than random chance (Fleiss' κ: 0.129). If you focus on the top three models by ELO, unanimity drops to 11%, and Fleiss’ turns negative: lawyers systematically disagree on the quality of strong models.
Looking at qualitative feedback, some of this is attributable to the difficulty of reviewing large environments and long model outputs. We classified each triad of written feedback to see whether lawyers were:
Talking past each other:
citing entirely different evidence for their vote; or
Disagreeing:
citing the same evidence but reaching a different conclusion
Only 24.3% of disagreements involved disagreements about what lawyers considered, such as hallucinations caught by only one reviewer. Lawyers largely found the same virtues and problems, even in long outputs—they just disagreed on what mattered overall and how to trade off competing pros and cons like style vs. hallucinations.
Scaling Humans With GRMs
The difficulty with low human agreement is that it scales the number of humans you need to effectively determine system quality. Reaching scale in legal is difficult because lawyers are expensive and ultra high-skill lawyers for every practice area are rare. We instead have to look for ways we can augment the world’s best experts to effectively encode their judgment at scale. We think GRMs are currently the most promising way to do this. GRM are agentic LLM judges designed to provide pairwise feedback on two outputs, the same way a human reviewer would. While they have a longer
lineage
, we took our inspiration for GRMs from Moonshot’s K3 technical report (
page 13
).
The K3 team describes the general protocol for an agentic GRM as:
Read the outcomes, work products or text outputs;
Generate a rubric of important features to compare the two outputs on;
Score each candidate on the rubric; and
Record the rubric-assigned scores to a scratch-pad
We extend this protocol in two ways. First, we give the GRM sub-agents that it can use to verify facts against either (1) the original environment (input documents, MCPs, etc.) or (2) the web. This allows the GRM to validate key factual claims and weigh hallucination or misrepresentation as a relevant part of quality.
Second, we define rubric axes for the GRM and require it to tag each rubric criteria against a relevant axis. For example, a rubric could be required to consist of one or more criteria covering:
Accuracy:
accuracy of statements made and lack of hallucinations.
Coverage:
coverage of relevant points
Grounding:
verifiability of key facts via citations or other clear reference points
Reasoning:
quality of analysis and judgment
Alignment:
alignment of the output with the original task and user instructions
Style:
formatting and presentation of the deliverable
Tone:
quality and readability of prose
For each criteria, the GRM scores two agent-generated responses between -1 (maximally favors response A) and 1 (maximally favors response B). We find that these rubrics allow us to recover more human-aligned reasoning from GRMs. They can state that one answer is stylistically better, the other has fewer hallucinations, and provide an overall judgment on which is better.
GRMs and Humans
We had members of our Applied Legal Research team tune GRMs to coarsely describe what a lawyer would care about across the seven axes enumerated above. Even with this loose direction, GRMs do a strong job of capturing human preference. GRMs largely recover the human preference rankings on the preference study above.
Figure 3: Comparisons of GRM-determined ELOs vs. human ELOs on LAB preference study
On overall preference, GRMs are more decisive than humans, increasing separation between models in the same directions that humans did. However, using each model’s mean rubric score (sum of all rubric items’ individual scores), we can recover how big any particular victory is which better aligns magnitude with the degree of separation seen in human preference.
Figure 4: GRM magnitude of win (mean rubric criteria ∆) cross-table
At the task level, GRMs represent a better than average reviewer. If you add it to the three human votes, the four-“person” panel agreement increases (Fleiss’ K .128 → .216) and if you substitute it for any random human, raw panel agreement increases from 44.7% to 59.2%.
Augmenting Humans
Through the experiments above, we’ve found that GRMs can effectively emulate high-skill experts when they independently evaluate the same outputs. But, the more interesting result is collaborative. Using GRMs as leverage allows an expert to more effectively evaluate an output.
To test this, we had lawyers evaluate pairwise outputs using GRM annotations. Specifically, we measured how frequently lawyers agreed with (1) the GRMs rubric items, (2) its overall choice, and (3) its granular reasoning.
Figure 5: Review interface of GRM comparisons showing full outputs as well as GRM annotations per rubric criteria, vote, and rationale (slight preference for Tenet on reasoning)
The results align with our intuitions. GRMs and humans generally align on the major facts: what criteria are relevant and which answer is better. Where ALRs and GRMs started to disagree was the exact reasoning behind why a response was better, with humans agreeing only ~64% of the time with the GRMs’ explanation.
Figure 6: Lawyer agreement with GRM criteria
For the most part this disagreement came from judgments about which types of failure were most impactful in terms of producing responses that were useful to lawyers. GRMs were willing to trade-off critical hallucinations or mistakes for other features in ways lawyers found unacceptable. Another major disagreement was identifying cases where both responses were bad. In those cases, GRMs would declare a winner between two unsatisfactory attempts that humans would rate a tie.
These results point to a natural complement between human experts and GRMs. GRMs can do the more mundane lift of reviewing the answer, identifying key points of comparison, and giving an initial recommendation on what to consider. Humans can take this under advisement and apply their own judgment on how to weigh these considerations and which outcome is genuinely best. Over time, GRMs can be tuned or trained against these last mile human judgments to scale that human judgment across thousands of examples.
What GRMs Tell us About Tenet
We used GRMs to scale pairwise judgments about a dozen leading models across LAB tasks. In initial runs, we found evidence of family bias among both Anthropic and OpenAI judges. When used as a GRM, they would systematically vote for models from their own lab in close calls, leading to substantially higher ELOs depending on the choice of judge. The one notable exception was that Opus had no bias for Fable. Both judges strongly agree when disinterested, agreeing on the winner in 78% of non-Anthopric, non-OAI matchups and 89% of matchups decided by > .05 rubric points.
Figure 7: Effect of projected ELO by swapping judge model. GPT-5.6 Sol as the GRM judge substantially increases ELO for OpenAI models and Opus 5 as the GRM judge substantially increases ELO for Opus but not Fable.
To correct for this bias, we adopt a disinterested judge protocol. We judge each matchup using a model from another lab, using Google’s Gemini-3.8 Flash for Anthropic-OpenAI pairings and selecting randomly where both main judges (Opus 5 and Sol-5.6) are disinterested.
Figure 8: Overall GRM-predicted model ELOs
Under this approach, Tenet shows meaningful improvement over Kimi K3 base in head-to-head comparisons on LAB held-out tasks gaining around 130 ELO and being preferred in more than 2 in 3 responses.
GRMs also allow us to break down what makes Tenet a better model for legal work than its base Kimi K3. We first compute per-axis ELO by counting wins and losses on rubric criteria tagged with that axis. This breakdown shows that Tenet improves over Kimi K3 on substance: substantially improving accuracy and reasoning. Notably it regresses on soft skills, having lower tone and style ELO compared to its base model.
Figure 9: Tenet and K3 ELO on key axes
These gains align logically with our approach to training Tenet, which used pre-authored expert rubrics as a primary post-training reward signal. LAB rubrics reward models for accurately surfacing key facts from the source documents and coming to correct conclusions about how those facts affect legal situations. Tenet does this better than K3, though sometimes at the cost of producing more factually dense, difficult to parse documents than vanilla K3.
Notably, this same trend appears in the rest of the frontier. Both Astra and Fable 5.1 are top-tier legal reasoners, but lose some of the straightforwardness and readability that older models bring to their work product with both regressing in style and tone from their predecessor who continue to lead the field on those axes. The best model continues to depend on the use case.
Better Models for Lawyers, by Lawyers
In lawyer terms, determining whether a model is good is a complex, multi-factor balancing test. High-skill lawyers will always remain the gold standard for making this determination, but well-aligned GRMs can augment lawyers in both making and scaling this judgment. This partnership is particularly well-suited as GRMs are most uncertain exactly where humans are strongest: usability and overall quality.
Augmenting humans with GRMs allows them to make these holistic judgments more quickly and accurately and to encode that judgment at scale in training. We hope to use these capabilities to allow legal experts to build the next version of Tenet as not just the smartest model for legal, but the most useful.
Special thanks to the following members from our Applied Legal Research team who contributed to various experiments that supported this post: Daniel Sylvia, Karl de la Roche, Marianna Zabkowski, Chris Bello, Laura Toulme, and Nick Gillies.
Next Up
How to Reduce Contract Cycle Time Across Every Review Turn
How to Draft a Litigation Hold Notice for Employees With Legal AI
The Builder Shift: Turning Individual Productivity Into Institutional Capability
Unlock Professional Class AI for Your Organization
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Overview
→
Agents
→
Vault
→
Knowledge
→
Spaces
→
Command Center
→
Contract Intelligence
→
Ecosystem
→
Harvey Mobile
→
Partnerships
→
Solutions
Innovation
→
Transactional
→
Litigation
→
In-House
→
Law Firms
→
Mid-Sized Firms
→
Company
Customers
→
Security
→
About
→
Careers
→
Newsroom
→
Law Schools
→
Resources
Blog
→
Resources Hub
→
Harvey Academy
→
Help Center
→
Legal
→
Privacy Policy
→
Press Kit
→
Your Privacy Choices
→
Follow
X
→
LinkedIn
→
YouTube
→
Instagram
→
Copyright © 2026 Harvey AI Corporation. All rights reserved.
