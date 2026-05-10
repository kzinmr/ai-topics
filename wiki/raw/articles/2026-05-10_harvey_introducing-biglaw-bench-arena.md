---
title: "Introducing BigLaw Bench: Arena"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/introducing-biglaw-bench-arena"
scraped: "2026-05-10T01:27:16.503080+00:00"
lastmod: "2025-11-07T14:00:00.000Z"
type: "sitemap"
---

# Introducing BigLaw Bench: Arena

**Source**: [https://www.harvey.ai/blog/introducing-biglaw-bench-arena](https://www.harvey.ai/blog/introducing-biglaw-bench-arena)

Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
About
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Assistant
→
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
→
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
→
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Innovation
→
Scale expertise and impact to drive firmwide transformation.
In-House
→
Streamline work and shift focus to strategy and speed.
Transactional
→
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
→
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
→
Drive outsize impact with tools built for lean teams.
Collaboration
→
Work with legal teams across organizations in secure, shared spaces.
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
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
→
About Harvey, our leadership, and career opportunities.
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
Assistant
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Solutions
Innovation
Scale expertise and impact to drive firmwide transformation.
In-House
Streamline work and shift focus to strategy and speed.
Transactional
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
Drive outsize impact with tools built for lean teams.
Collaboration
Work with legal teams across organizations in secure, shared spaces.
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
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
Company
About Harvey, our leadership, and career opportunities.
Newsroom
Press releases and partnership announcements.
2025 Year in Review
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Request a Demo
Login
US
EU
AU
Technical
Introducing BigLaw Bench: Arena
Presenting BigLaw Bench: Arena — our approach to head-to-head evaluation of AI systems on legal tasks.
by
Beth de la Roche
•
Nov 7, 2025
Today, we’re introducing BigLaw Bench: Arena (BLB: Arena), which is our internal system for determining which models and systems experts actually prefer through scaled, pairwise comparison. Inspired by open research initiatives such as LMArena, this approach complements formal benchmarks and provides unique perspectives from experts on not just what makes an AI system good, but also what makes it better than alternatives.
We’re also publishing recent results which compare our recently released version of Harvey Assistant against prior implementations and leading foundation models.
These results flow from a simple evaluation premise: lawyers look at two outputs to a task, identify which output they prefer (or note if they have no preference), and provide a reasoned explanation for their vote. This head-to-head approach means graders aren’t bound by predetermined criteria — they simply express their overall preference and highlight what they value in a response.
This flexible framework provides a complementary signal to more structured benchmarks. Instead of measuring how well a model meets prescribed standards, BLB: Arena shows how each system resonates with experienced lawyers based on their professional judgment. This tells us not only which models are consistently preferred, but also what lawyers consistently value.
Throughout the rest of this post, I’ll walk through BLB: Arena in more detail, including what goes into interpreting the results.
The BLB: Arena Process
Major systems at Harvey run the Arena gauntlet monthly — competing against foundation models, internal prototypes, and even humans — across hundreds of legal tasks drawn from our internal lawyers and client partners. Competitor outputs are generated from all relevant systems (usually between five and ten) and each task is paired up against all competitors for review by lawyers. Since each competitor goes head-to-head, voting lawyers may see dozens of paired responses in determining which model performed the task best.
Pairs are then categorized by practice area and reviewed. Each lawyer is asked to spend time reviewing each pair of outputs and provide their preference and the reason for their judgment. Between three and ten lawyers will review any particular pair of outputs to provide diverse perspectives on which output is preferred and why. Overall, tens of thousands of preference votes are cast each month across Harvey’s systems.
As illustrated by the graphic below, this scale is necessary to give proper perspective across models, tasks, and lawyers. Having just five lawyers compare five competitors on 100 tasks requires 5,000 votes and pieces of qualitative feedback to compare each competitor head-to-head and overall.
Once grading is complete, Applied Legal Researchers (ALRs) at Harvey aggregate the results by system and produce three major analyses:
First, we quantitatively combine the casted preference votes into
Elo scores
that help us determine how each system performed against both current and past competitors.
Next, we review the qualitative feedback and encode it into
preference drivers
in order to understand the macro trends that drove certain results.
Finally, ALRs will
review the data
for any trends, insights, or anomalies that can be shared more broadly to inform both our evaluations and our systems.
Understanding Elo
A model’s Elo score is the key metric produced by BLB: Arena. It turns thousands of head-to-head judgments into a single, interpretable measure of relative quality. Each match in BLB: Arena produces a simple result: one model wins, one loses, or the match is a tie. When aggregated across many matches and competitors, however, this simple result can become difficult to interpret.
Take, for example, these head-to-head results from a September BLB: Arena run:
Matchup
Percentage
A v. B
79.27% (A) v. 20.73% (B)
A v. C
42.71% v. 57.29%
A v. D
45.99% v. 54.01%
B v. C
29.73% v. 70.27%
B v. D
26.13% v. 73.87%
C v. D
42.61% v. 57.39%
Trying to determine which model is best (and by how much) from this data can be complex. D seems to be the strongest, winning all of its matchups. A loses to C, but performs better against B (79%) and D (46%) than C does (70% and 42% respectively). Meanwhile C beats A (57%) more decisively than D does (54%). Elo smooths this complexity and aggregates the results into a clean ranking that shows who tends to win and how often.
Here are the Elo scores derived from the same matchups:
Rank
Competitor
Elo
1
Model D
1500
2
Model C
1469
3
Model A
1467
4
Model B
1294
From these results, we have one clear conclusion: Don’t use Model B. Model A and C’s results mean we can’t really tell which one would be truly preferred and although Model D stands out, its advantage is slight.
More specifically, any pair of Elo scores tell us the likelihood of each system to be preferred by a lawyer on a given response. For example, Model D is expected to be preferred to Model C by lawyers 54.45% of the time and to Model B 76.6% of the time — nearly, but not quite the results of those matchups in September. Since Elo is defined the same way everywhere, there are various online calculators that can be used to understand and interpret any two Elo scores.
Although Elo offers a simple, scalable way to parse quality in a multi-model evaluation, it has a few key limits. Perhaps the most important is that it does not take into account margin of victory. Therefore, it only predicts how likely one system is to win, but not by how much. A model that consistently beats a competitor by a small but clear preference will score the same Elo difference as one that is transformatively better. Due to this, computing and understanding Elo is only the start of the work for interpreting a BLB: Arena result.
Qualitative Feedback and Preference Drivers
In addition to preference votes, every BLB: Arena cycle yields thousands of qualitative explanations from human graders. These written assessments provide valuable insight into why a particular system won a matchup and by how much.
To convert qualitative feedback into measurable signals, we use a labeling system that categorizes each unit of feedback by its preference driver(s). A preference driver is a taxonomized reason a grader preferred one response over another, helping to convert unstructured feedback into structured data that can be understood at scale. This not only helps add color to each model’s Elo score, but also identifies the qualities that actually drive human preference between current leading AI systems.
Over time, we have identified four main categories of why people prefer an AI (or human) response covering substance, form, and usability. They are: Alignment, Trust, Presentation, and Intelligence. While we also annotate an “Other” category, we have found that it makes up a very small fraction of feedback.
Each piece of feedback gets annotated into both its “strongest” preference driver as well as any other sentiments that were contained in the feedback. For instance, a feedback item of: “Response A is better than Response B because it provides clear citations back to the source material that helped me verify the model’s reasoning. I also preferred its use of bold headers.” would be categorized as both Trust (strongest) and Presentation.
To understand trends, these annotations are aggregated based on how often a system wins and loses based on a certain preference driver. A strong system may still lose along a particular preference axis, and a weak system may show promise when looking past its win-rate. A recurring example is Deep Research models. Although these models are commonly outperformed in terms of raw preference by other systems, they routinely score highly in Intelligence due to their exceptionally detailed, long-form answers.
In addition to aggregating preference drivers, our ALR team spends time with the feedback to identify other trends that emerge outside of our main two metrics. Combined with preference drivers, these insights help us shore up weaknesses, or build on strengths of our models and systems.
Example Results: Assistant
To illustrate how BLB: Arena operates in practice, the following results show an example evaluation from a recent cycle looking at
Assistant
. Each bar represents a model’s Elo score, reflecting its relative performance across a set of tasks. Scores are calculated for both foundation models and internal Harvey variants. Harvey A represents a version of Assistant built primarily on GPT-5.
Incorporating
GPT-5
has been a major initiative at Harvey, as it presented novel challenges and decision points compared to prior OpenAI models. The Assistant team spent countless hours working with GPT-5 and identifying where and how it could be best deployed to support legal work.
These results, with Harvey A scoring substantially above baseline GPT-5 and variants using other major models, helped confirm their work and ship a production system that we were confident in. The results also confirm the general health of Harvey systems, with three other variants continuing to outperform leading foundation models on legal tasks.
For example, Harvey B’s (a primarily GPT-4.1 variant) response to legal questions is preferred to Claude 4.5 more than 59% of the time in head-to-head matchups and Harvey A’s response is preferred 70% of the time. Additionally, the results show that only Harvey E (a GPT-4o variant) is starting to become obsolete.
The preference driver data from the above evaluation cycle was also informative. Harvey A is the first system where intelligence was the main driver of human preference — showing distinct depth and nuance in solving legal problems through access to a richer set of agentic tools. While this has long been the hypothesis internally, seeing it confirmed at scale by human experts validates that these investments are paying noticeable and meaningful dividends.
BLB: Arena also allows us to analyze results by specific categories, such as practice area or task type to better understand how systems are performing for specific users or use cases. Below, we segment outcomes by litigation and transactional work to observe how systems perform across these distinct professional domains.
These additional perspectives help us focus our research where it will make the most impact and communicate those nuances more effectively to customers using our systems to solve specific challenges.
How We Use BLB: Arena
In practice, decisions about which AI systems to use are rarely based on an isolated judgment of quality. We are faced with important decisions about which foundation model to use in each of our AI systems and how to maximize their capabilities for legal work. BLB: Arena is one tool we use to map that landscape. By looking directly at lawyers’ preference for different responses, it provides a unique perspective on the relative strengths of foundation models.
BLB: Arena’s intuitive premise also makes it a uniquely accessible evaluation framework. While learning to structure a formal benchmark takes experience, every lawyer is well positioned to contribute their professional judgment to advance our understanding of AI systems. This allows us to avoid building echo chambers by running evaluations that tap into a diverse set of legal professionals. This perspective complements our formal benchmarks, and helps us confirm that we are continuing to build the best AI for knowledge work.
If you want to explore more BigLaw Bench evaluations, check out these blog posts:
Big Law Bench: Sources
BigLaw Bench Workflows: SPA Deal Points
BigLaw Bench: Hallucinations
BigLaw Bench: Retrieval
Credits: Laura Toulme, Cam MacGregor, Olga Baranoff, Chris Bello, Emilie McConnachie, and the ALR team.
Next Up
How we Built Image Understanding for Legal Documents
How Harvey Secures Embeddings at Scale
Rebuilding the Review Algorithm to Increase Accuracy and Speed
Unlock Professional Class AI for Your Firm
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Assistant
→
Vault
→
Knowledge
→
Workflow Agents
→
Ecosystem
→
Partnerships
→
Solutions
Innovation
→
In-House
→
Transactional
→
Litigation
→
Mid-Sized Firms
→
Collaboration
→
About
Customers
→
Security
→
Company
→
Newsroom
→
Careers
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
Copyright © 2026 Harvey AI Corporation. All rights reserved.
