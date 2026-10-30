---
title: "Extending Legal Agent Bench to U.S. Case Law"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/legal-agent-bench-us-case-law"
scraped: "2026-10-30T06:00:58.751225+00:00"
lastmod: "2026-10-29T18:00:00.000Z"
type: "sitemap"
---

# Extending Legal Agent Bench to U.S. Case Law

**Source**: [https://www.harvey.ai/blog/legal-agent-bench-us-case-law](https://www.harvey.ai/blog/legal-agent-bench-us-case-law)

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
Horizon Scanning
→
Track, assess, and take action on regulatory changes.
Intake
New
→
Capture, route, and resolve legal Intake from across the business.
Connector Library
New
→
Bring your team’s tools into Harvey with security-reviewed connectors or custom MCP.
Legal Work Orchestration
New
→
Assign, execute, and review legal work with agents and your team.
Overview
For In-House
→
For Law Firm
→
For Mid-size Firm
→
Industries
Healthcare & Life Sciences
→
Energy & Utilities
→
Technology
→
Media, Entertainment & Telecom
→
Public Sector
→
Practice Area & Teams
Litigation
→
Transactional
→
Innovation
→
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
Horizon Scanning
Track, assess, and take action on regulatory changes.
Intake
New
Capture, route, and resolve legal Intake from across the business.
Connector Library
New
Bring your team’s tools into Harvey with security-reviewed connectors or custom MCP.
Legal Work Orchestration
New
Assign, execute, and review legal work with agents and your team.
Solutions
Overview
For In-House
For Law Firm
For Mid-size Firm
Industries
Healthcare & Life Sciences
Energy & Utilities
Technology
Media, Entertainment & Telecom
Public Sector
Practice Area & Teams
Litigation
Transactional
Innovation
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
Extending Legal Agent Bench to U.S. Case Law
Introducing a new extension to Legal Agent Bench that tests frontier models’ ability to research and draft litigation briefs end-to-end using real case records.
by
Laura Toulme
and
Julio Pereyra
•
Oct 29, 2026
Today we introduce LAB: United States Case Law (LAB: USCL), an evaluation framework for testing frontier models’ ability to research and draft litigation briefs end-to-end using real case records. LAB: USCL adds novel approaches to
LAB
for understanding model behavior by building environments from real, public data collected by
Free Law Project
and evaluating model-written briefs head-to-head.
We find that a small group of frontier models can now research and write complete, first-draft briefs in a single shot with no attorney guidance. While these briefs still exhibit a long tail of failure modes, they are substantially closer to the high bar for filing with a court and mark a substantial advance on a task that demands complex legal reasoning and advocacy.
In this post we discuss our initial findings on these emerging capabilities as well as how we plan to make research in this area more accessible in partnership with Grubel.
Brief Writing: An Ultra-Long Horizon Task
When parties to a litigation want a court to act, they file a motion: a formal request asking the judge to issue a specific order or ruling. A motion may ask the court to do routine things like change a deadline or take more dramatic actions like dismissing a case or sanctioning a party. Some motions are opposed by the other parties, who argue that it would be legally incorrect or otherwise inappropriate for the court to take the requested action.
To support these more contested motions, parties file briefs: written advocacy explaining why the court is justified in taking some action based on the state of the case, the law and precedent, and other considerations. Brief writing is one of the most complex tasks in litigation, sometimes requiring a team of lawyers multiple weeks to write and refine a compelling argument. An agent replicating this work must complete the same three steps a lawyer does: understanding the state of the case, researching the case law, and writing the brief itself.
Understanding the State of the Case.
For agents, the first part of replicating this work is understanding the state of the case by reviewing its docket, the official record of the case’s proceedings. The docket lists every filing, meaning every document submitted to the court, such as the complaint that starts the lawsuit, the motions and briefs that contain the parties’ arguments, and exhibits supporting those arguments, such as contracts, letters, or financial records. It also records the judge’s orders and rulings. In complex or long-running cases, the docket can span thousands of filings.
Figure 1. A sample PACER docket with identifying details anonymized. A docket lists filings and court actions in chronological order, with hyperlinks to download the underlying documents.
Researching Case Law.
The next step is case law research: finding the past court decisions that bear on the legal questions in a case and determining how much weight each one carries. When judges rule on motions or decide cases, they often explain their reasoning in written opinions. Together, these opinions make up case law, the body of rules that comes from judges’ decisions, as opposed to rules passed by legislatures (statutes) or issued by agencies (regulations). These decisions carry weight because they create precedent. In the United States legal system, judges are expected to justify their decisions by relying on earlier opinions. Some of those opinions are binding: a court must follow decisions on the same legal question from higher courts in its jurisdiction. Other opinions, such as decisions from other trial courts, are only persuasive, so a court can look to them for guidance but doesn’t have to follow them.
Case law research requires an agent to not only find the relevant opinions but also read them against the broader body of precedent, because later decisions can narrow, modify, or even invalidate an earlier opinion. Read in isolation, an opinion may seem to support a client’s position even after a higher court has rejected it. A brief that relies on that opinion misstates the law and weakens the lawyer’s credibility with the court. In the figure below, for example, a brief relying on the Fifth Circuit’s test would be citing a rule that is no longer valid following the Supreme Court’s ruling.
Figure 2. The conclusion from the opinion in a Supreme Court case rejecting a lower court’s test. That test is no longer valid precedent.
Writing the Brief and the Bar for Filing.
Once an agent has researched the facts and the law, the final step is writing the brief itself. A strong brief must synthesize that research and connect the facts of the current case to precedent to persuade the court to rule in the client’s favor.
An agent performing this task must keep the details of hundreds of pages of filings and opinions straight, strategize which arguments to make and which to leave out, explain why favorable cases control and unfavorable ones don’t, and turn all of that into a persuasive document that follows strict conventions on length and structure, with every citation to the record and case law accurate.
The bar for that final document is particularly high. Unlike a research memo or other internal analysis, a brief is filed on a public docket on the client’s behalf. The attorney who signs it certifies to the court that existing law supports its legal arguments and all factual claims have evidentiary support. Lawyers also owe the court a duty of candor. They cannot misstate the law, and they must disclose directly adverse controlling authority. Mistakes have consequences beyond simply a weaker argument. Lawyers can be sanctioned, the client can be held to the brief’s positions, and an argument left out may be lost for good, including on appeal. A brief is ready to file only when every citation, characterization, and strategic choice can withstand that scrutiny.
Building Case Law Environments from Real Data
LAB: USCL measures agents’ capabilities to perform this task against substantially the same materials a lawyer used in a real case. We select a brief actually filed in court, then ask the model to carry out the same assignment: writing a brief for the same party, addressing the same motion or legal issue at the same point in the case.
Figure 3. Distribution of motion types in our scored sample and coverage of our sample against all federal courts. State courts and the U.S. Supreme Court do not use PACER and represent areas for future expansions.
To build these environments, we sample from federal court dockets. In the United States, dockets are generally public and accessible through
PACER
, the federal judiciary’s electronic records system. PACER holds the dockets of more than 200 federal courts, covering millions of cases and more than a billion documents. Because PACER charges per page for access, our pipeline draws from
RECAP
, Free Law Project’s community-constructed archive of PACER filings. RECAP is built from documents that PACER users have already purchased and shared, so its coverage can be uneven. For example, a docket may list a brief or exhibit that no one has downloaded and so is unavailable on RECAP.
We therefore filter for dockets that contain (1) a filed brief and (2) the filings necessary to contextualize that brief to ensure it can support a realistic environment. Even then, a docket isn’t a comprehensive record of the case. Most discovery, such as deposition transcripts and other witness testimony, is never filed with the court unless a party attaches it to a motion, and sensitive material may be sealed or redacted. The resulting environment gives the model enough to understand the case, but not everything the lawyer had.
For each environment, we then extract all case citations from the filed brief. We use agents to locate the cited judicial opinions in
CourtListener
, Free Law Project’s case database of more than 8 million opinions from across the judiciary. We retain an environment only if we can match more than 95% of the case citations in the lawyer’s filed brief to opinions available in CourtListener. This ensures the model works from substantially the same case law the lawyer used to draft the filed brief.
Figure 4. Our pipeline for building environments. A brief supports an environment if its record is sufficiently complete and its citations resolve in CourtListener.
Even with these filters, the scale of the archive yields a large pool of valid environments. Building them, however, is not straightforward. Gaps in the docket mean an automated pipeline often can’t tell whether a case record is complete enough to support the task. But because one docket can contain multiple briefs, a single docket may yield several environments. From an initial sample of 200 dockets, our pipeline’s first pass produced 40 environments. Through human review and manual correction, we expanded that to a final set of 100.
To ensure diverse coverage, we taxonomize briefs across a number of salient features, such as court type, filing posture, and case type. The initial set spans trial and appellate courts, every stage of motion briefing, and more than ten areas of law. As we expand our environments, there is substantial ground to cover to ensure we can capture the full diversity of potential jurisdictions, motions, and legal disputes.
Evaluating Agents Head to Head
For each environment, we define two task conditions: open- and closed-book. In the closed-book condition, the model receives a file system, built by our extraction pipeline, containing the case’s record and the cases the filed brief relied upon. In open-book, the model receives only the subset of filings relevant to defining the task, along with access to legal research tools through a CourtListener MCP to search for relevant case law and additional filings, limited to materials available before the brief was filed.
Figure 5. Closed-book and open-book conditions differ by the materials and tools provided to the model.
In both conditions, a model is given a single short instruction to draft the relevant brief. From there, it works on its own, with no attorney feedback or follow-up prompts. Both conditions use the standard LAB harness with compaction to handle long context and OCR tools added to handle PDFs.
Rather than grading each brief against a fixed answer key, we have models’ briefs face off directly. We evaluate model-written briefs pairwise in a round-robin tournament using
GRMs
which select the better brief (or declare a tie) and provide reasoned criteria supporting each choice. These criteria are reviewed by lawyers and calibrated to ensure they are relevant to reasons expert reviewers would prefer a brief.
Figure 6. Briefs are scored head to head and the results converted to Elo ratings.
We then aggregate a model’s wins and losses in these head-to-head games into an Elo rating for each model. This rating predicts a model’s relative brief-writing skill, allowing us to order models based on how well they write briefs and predict how likely they are to write a winning brief outside of our sampled environments.
Initial Findings: A Small Group of Frontier Models Are Writing Complete, First-Draft Briefs
The pairwise results substantially separate model performance, with nearly 700 Elo points separating the highest- and lowest-rated models. This means that the highest-rated model, Opus 5.5, writes a stronger brief than the lowest performing models more than 95% of the time.
This performance is stable across open- and closed-book environments, suggesting model performance does not come from their ability to effectively use search tools, but their ability to convert the materials into complete and structured briefs.
Figure 7. Cost and Elo of model-written briefs in open-book condition (legal research tools only). Top-left is optimal.
Figure 8. Cost and Elo of model-written briefs in closed-book condition (case law supplied). Top-left is optimal.
As we look at the highest scoring models, the “Frontier Writers,” we find not only relative improvement but an emerging capability to write briefs end-to-end. These models are not only doing better research and advocacy, they are incorporating the depth and craft required to produce a polished work product.
The below video illustrates these gains. It compares a brief produced by a recent frontier model (left) with one produced by its immediate predecessor in the same model family, released just a few months earlier (right). The newer model’s brief is longer, engages with each of the opposing party’s arguments, and follows the conventions of a filed brief, down to its cover page and table of authorities. Its predecessor’s brief is substantially shorter and missing the hallmarks of a correctly formatted brief.
Fig. 9. Actual shape, structure, and length of model submitted briefs by a frontier writer (left) and prior generation (right). All substantive content replaced with anonymized content.
These improvements change the evaluative methods needed to assess the quality of model-written briefs. Previous evaluations found that while models were getting better, they were far from
good
, with the question of “is this a brief” answerable in seconds from responses that were far too short and lacked the substance and structure of a filed brief. As models increasingly pass these hurdles, deeper analysis is required to validate and improve their capabilities.
Under that closer scrutiny, even the strongest briefs still fall short of the filing bar and show a long tail of failures. In addition to longstanding issues like hallucinations, leading models unnecessarily concede points that weaken the client’s position or abandon strong arguments made in the party’s initial brief. They may rely on a court decision that has been set aside, or defer to a decision the court is not required to follow, without considering why that decision may not apply. These errors can appear within otherwise sophisticated arguments or may occur only in some cases as models display jagged intelligence across two similar tasks.
What’s Next
These findings define two connected research priorities: improving models’ ability to produce accurate, strategically sound briefs, and developing reliable ways for experts to supervise and evaluate that work at scale.
To support this research, we plan to open source resources in partnership with Grubel, enabling researchers to construct their own case law environments and study model capabilities. We want to provide people with cookbooks to build the environments they’re interested in, whether for a specific court or type of litigation, or for courts not on PACER, such as state courts or the Supreme Court.
Unlike previous LAB releases, we are not currently publishing sample environments alongside this post. These environments draw on real litigation involving identifiable people and organizations. Although the filings are public, we want to avoid drawing additional attention to selected disputes and the allegations they contain.
Until recently, even the best models struggled to write briefs without close attorney supervision and days of iteration. Today, leading models are beginning to research and write compelling briefs in a single pass, marking a substantial advance in their ability to carry out complex legal work. LAB: USCL provides a way to measure that progress through environments built from the same sources of data litigators use every day.
We’re excited to deepen this research and give the community the tools to do the same.
Last updated:
October 29, 2026
Next Up
Turning a Raw Deposition Transcript Into a Usable Record
ESI Protocol Best Practices for Search Terms and Production Format Before Discovery Starts
How I Help Legal Teams Apply Their Expertise With AI
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
Horizon Scanning
→
Ecosystem
→
Intake
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
Healthcare & Life Sciences
→
Energy & Utilities
→
Technology
→
Media, Entertainment & Telecom
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
