---
title: "Low Latency Redline Detection via Vision Models"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/low-latency-redline-detection"
scraped: "2026-05-10T01:27:19.510054+00:00"
lastmod: "2025-06-17T16:00:00.000Z"
type: "sitemap"
---

# Low Latency Redline Detection via Vision Models

**Source**: [https://www.harvey.ai/blog/low-latency-redline-detection](https://www.harvey.ai/blog/low-latency-redline-detection)

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
Low Latency Redline Detection via Vision Models
How Harvey delivers high-performance document processing for redlines detection using custom vision models.
by
Harvey Team
•
Jun 17, 2025
Introduction
Reviewing redlined documents is critical for negotiations, compliance, and litigation. Legal teams spend countless hours manually reviewing tracked changes in documents, creating a productivity bottleneck in high-stakes environments. At Harvey, we’ve built tools that streamline time-consuming legal tasks like these and surface the information our clients need to make informed decisions faster.
For Harvey to precisely review redlined documents, we must first establish whether a given document contains redlines – and if so, the exact nature of the redlined changes. However, traditional methods for identifying and processing redlined documents are often slow and error-prone.
To address this, we’ve built a custom vision model using cutting-edge ML techniques that delivers exceptional accuracy with near-instantaneous results. In this post, we'll explore the technical innovations powering our redline detection system, from our approach to PDF processing to the performance optimizations that unlock new capabilities for detailed document analysis in Harvey.
The Challenge
Our clients often work with long, information-dense documents that undergo dozens of revisions. Understanding what changed between versions – and more importantly, which changes matter –can be very difficult and time-consuming.
How then can we help legal professionals quickly identify material changes while ignoring trivial edits?
Harvey’s document analysis pipeline tackles this through a series of underlying systems, including document processing, retrieval models, answer models, and our citation engine. When these systems operate seamlessly, a user’s query about the important changes in a redlined document yields a comprehensive response capturing every material edit, with each change supported by precise, line-level citations to the source text.
Crucially, our document processing systems must extract the necessary document metadata for our retrieval, answer, and citation steps to work effectively. In the case of redlined documents, this document metadata takes the form of “spans” of text that represent which text in the document has been added, deleted, moved, or remained in place.
Unfortunately, extracting these spans for downstream systems is resource-intensive and adds significant overhead to file upload processing times. As such, we cannot afford to apply this intensive processing on every document uploaded to Harvey. We need a reliable method of identifying which documents actually contain redlines so we can selectively apply this additional processing only when needed.
Building a Redline Detection Model
To solve this problem, we initially explored a number of text-based heuristics that checked for color presence and ordering, strikethroughs, and underlines. Although the heuristics rarely produced false positives, they frequently missed clear examples of redlined documents and failed to scale across the diverse ways clients represent insertions and deletions.
Notably this task was simple for DOCX files due to their underlying XML structure that is easily parsed. PDF files, however, posed a significantly more difficult challenge.
Ultimately, the best way to identify a redlined document is how any legal professional would:
by looking at the document
. We opted to build a custom vision model that analyzes the pages of the document and predicts whether the document contains redlines.
Building this vision model effectively required getting several components right:
Identifying a reliable method of converting PDFs to images.
Training a small, highly-performant model with strong bias against false positives.
Optimizing the model for speed and memory to add minimal latency, even at peak load.
Converting PDFs to Images
Before passing the PDF document to our vision model, we had to rapidly convert these documents to images. After testing multiple Python libraries, we selected pyvips, a Python binding for the vips image processing library for its low memory utilization and latency.
Data and Model Training
Our training corpus consisted of several hundred public documents labeled as
redlined
or
clean
and split by document to prevent leakage. These documents and their constituent pages were then cut into patches of 224x224. Crucially, the dataset labels “contains redline” and “does not contain redline” were verified manually at the patch level. This level of attention to detail ultimately paid dividends in the later stages of model refinement, as we had strong confidence in the dataset quality and metrics computed, even in the finest of margins.
The first model we trained was based on MobileNet V3-Small, a popular lightweight vision model that also has publicly-available weights from ImageNet pre-training. Two lightweight tweaks—converting images to grayscale during training and inference and pre-filtering for patches that lack long horizontal strokes—lifted accuracy and cut inference time by more than half. The former of these two changes may initially appear counter-intuitive, however, it was the grayscale augmentation that made our model far more robust to stylistic variation in redline annotations and spurious red pixels or elements.
Our final step was to experiment replacing MobileNet with a much smaller, purpose-built CNN with just 100K parameters, preserving performance while meeting sub-second latency on common CPUs.
Model variant
Params
Size
CPU inference (100 patches)
Validation F1
Key idea
MobileNet V3-Small
2.5 M
9.7 MB
2.5 s
0.970
ImageNet initialization
Grayscale augmentation
0.993
Suppress color bias
Line-shape pre-filter
< 900 ms
0.993
Skip obvious negatives
Custom CNN (ours)
0.1 M
1 MB
< 500 ms
0.992
ImageNet initialization unnecessary
Model Optimization & Latency
Raw model performance only tells part of the story. To achieve production-ready speeds, we implemented sampling techniques to limit the number of patches evaluated by the model to just those likely to contain redlines. These include random sampling of pages and patches within those pages, and applying RGB and edge detection filters, among other optimizations. These all keep raw model time to
100–150 ms
, and by parallelizing this operation with other document processing steps, we’re able to achieve zero additional latency to our user’s experience.
Conclusion
By integrating this redline detection model with Harvey’s broader document processing systems, we’ve transformed redline detection from a slow post-upload job into a sub-second, inline capability. This unlocks a simple but powerful user experience: the moment a document is uploaded to Harvey, it is intelligently routed for richer metadata extraction and ready for legal analysis, regardless of document type.
Looking ahead, we’re excited to continue optimizing our file processing systems to deliver ever-faster insights, richer context, and broader coverage. If solving problems like these sound exciting to you,
we’d love to hear from you
.
Acknowledgements
Thank you to Varun Nair, Philip Lan, Samer Masterson, Mark McCaskey, and Philip Cerles!
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
