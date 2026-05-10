---
title: "AI is its own best safeguard: Glean uses AI to detect jailbreak attempts at 97.8% accuracy"
source: "Glean Blog"
url: "https://www.glean.com/blog/ai-safeguard-septdrop-2025"
scraped: "2026-05-10T01:27:10.612152+00:00"
lastmod: "None"
type: "sitemap"
---

# AI is its own best safeguard: Glean uses AI to detect jailbreak attempts at 97.8% accuracy

**Source**: [https://www.glean.com/blog/ai-safeguard-septdrop-2025](https://www.glean.com/blog/ai-safeguard-septdrop-2025)

Product
WORK AI PLATFORM
Platform Overview
Glean Assistant
Your personal AI assistant
Data Analysis
Canvas
Deep Research
Glean Agents
Build and manage AI agents
Agent Builder
Agent Governance
Agent Orchestration
Agent Library
Glean Search
The foundation of enterprise AI
Enterprise Graph
Personal Graph
System of context
Hybrid Search
Connectors & Actions
Connect to all your apps
Model Hub
Get access to the latest models
APIs
Build generative AI experiences
Security
Safely scale AI at work
Agentic Engine
Plan & adapt over company context
GLEAN WHERE YOU WORK
Glean in Slack
Glean in Microsoft Teams
Glean in Zoom
Glean in Service Cloud
Glean in ServiceNow
Glean in Zendesk
Glean in GitHub
Glean in Miro
Browser Extension
Sign in
Customers
Solutions
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
Marketing
B2B Marketing
B2C Marketing
People
IT
INDUSTRIES
Retail
Financial Services
Banking
PE/VC
Asset management
Insurance
Higher Education
Healthcare
Government
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Sign in
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
Resources
EXPLORE
Resource Center
Blog
Prompt Library
Guides
Product Videos
ENGAGE
Webinars
Newsroom
Glean:GO 2026
Events
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
Sign in
The AI Transformation 100
Explore 100 real-world moves organizations are making to transform themselves with AI.
Download the report
About
Thank you! Your submission has been received!
Oops! Something went wrong while submitting the form.
Sign in
Get a demo
Get a demo
Sign in
Get a demo
Get a demo
Product
Customers
Solutions
Resources
About
Sign in
Back
WORK AI PLATFORM
Platform Overview
Glean Assistant
Your personal AI assistant
Data Analysis
Canvas
Deep Research
Glean Agents
Build and manage AI agents
Agent Builder
Agent Governance
Agent Orchestration
Agent Library
Glean Search
The foundation of enterprise AI
Enterprise Graph
Personal Graph
System of context
Hybrid Search
Connectors & Actions
Connect to all your apps
Model Hub
Get access to the latest models
APIs
Build generative AI experiences
Security
Safely scale AI at work
Agentic Engine
Plan & adapt over company context
GLEAN WHERE YOU WORK
Glean in Slack
Glean in Microsoft Teams
Glean in Zoom
Glean in Service Cloud
Glean in ServiceNow
Glean in Zendesk
Glean in GitHub
Glean in Miro
Browser Extension
Sign in
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
Marketing
B2B Marketing
B2C Marketing
People
IT
INDUSTRIES
Retail
Financial Services
Banking
PE/VC
Asset management
Insurance
Higher Education
Healthcare
Government
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Sign in
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
EXPLORE
Resource Center
Blog
Prompt Library
Guides
Product Videos
ENGAGE
Webinars
Newsroom
Glean:GO 2026
Events
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
Sign in
The AI Transformation 100
Explore 100 real-world moves organizations are making to transform themselves with AI.
Download the report
Last updated Apr 16, 2026.
AI is its own best safeguard: Glean uses AI to detect jailbreak attempts at 97.8% accuracy
0
minutes read
Sarika Mohapatra
Software Engineer
Sunil Agrawal
Chief Security Officer
Julie Mills
PMM
Listen to article
0:00
0.5x
1x
1.5x
2x
Table of contents
Heading 2
Heading 3
Heading 4
Heading 5
Heading 6
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Share this article:
Listen to article
0:00
0.5x
1x
1.5x
2x
AI Summary by Glean
Glean’s multi-layered AI security approach leverages advanced detection models to proactively guard enterprises against prompt injection, toxic content, and malicious code, achieving industry-leading accuracy rates—97.8% for prompt injection, 93.5% for toxic content, and 94.3% for malicious code on industry-standard benchmarks.
Glean distinguishes itself in handling enterprise-specific risks by continuously refining its models for lower false positive rates and integrating context-aware reasoning, helping organizations trace and remediate threats using a comprehensive AI security dashboard and dual-model validation.
Glean’s sensitive content models, now in beta, automatically separate real risks from noise in unstructured enterprise data with over 80% accuracy by combining traditional classifiers, enterprise graphs, and contextual analysis, enabling precise data protection and confident AI scaling across diverse, complex environments.
At Glean, we believe the future of AI security is AI itself. Reasoning models are becoming increasingly better at staying ahead of evolving threats by detecting attacks and sensitive data exposures.
That’s why we’re excited to share the results of our investments in AI security- new detection models that achieve 97.8% prompt injection detection, 93.5% toxic content detection, and 94.3% malicious code detection on leading benchmarks.
In this blog, we'll dig into how we arrived at these results, developed the industry's leading detection models, along with our multi-layered approach to AI security.
Multi-layered approach to AI security
By design, AI models aim to be as helpful as possible. They’ll explore multiple paths to achieve a user’s goal, even when that goal has malicious intent—unless security controls prevent it.
Many commercial and open-source models now include these AI security controls. However, in a multi-model world where models cross-collaborate on complex work, those guardrails alone are not enough. They require an additional protective layer over prompts and agents to block prompt injections, malicious code, and toxic content.
Glean’s AI security models, generally available today, provide those capabilities—taking a layered security approach to keep enterprises safe. From day one, Glean introduced permissions-enforced data connectors and access controls to prevent prompt injection attempts from causing data leakage or unauthorized actions. Now, we’re adding a new AI security layer to preserve model integrity and reliability: dedicated security models that inspect and validate chat sessions and agent execution steps.
Not all AI security models are equal
Not all AI security models are equal; quality and staying current with evolving threats matter. We found out-of-the-box models don't fully protect enterprise scenarios so we developed models specifically for the enterprise AI threat landscape.
By fine-tuning using publicly available datasets relevant to enterprise scenarios, our models are better equipped to identify and mitigate enterprise-specific risks—avoiding the high false positive rates and missed threats common with generic solutions. Additionally, we employ a combination model strategy to validate initial results and further reduce false positives.
We’re sharing performance benchmarks showing how our security models stack up against leading open source LLM safety models, observability solutions, and cloud provider offerings. Glean achieves 97.8% accuracy on prompt injection detection, 93.5% accuracy on toxic content detection, and 94.3% accuracy on malicious code detection on leading benchmarks.
Results are averaged across the evalsets for prompt injection, toxic content, and malicious code. Hyperscale cloud providers do not support malicious code detection.
*Glean blocks direct prompt injection attacks at a 97.8% accuracy rate and indirect prompt injection attacks at a 90% accuracy rate.
Prompt injection
Toxic content
Malicious code
Do Anything Now (custom): Curated variant of DAN that to make it a single-turn, input-only benchmark.
OpenAI Moderation Dataset: Human‑labeled dataset from real transactions, commonly used to benchmark harmful/toxic content detection.*
Malware Plaintext:  Glean‑built set of real snippets from viruses, exploits, and post‑exploitation tools, each paired with a standardized “analyze or execute” prompt in clear text to test detection of actual malicious code.
Do Anything Now (benign): Control set of safe sentences that use trigger words from DAN including “prompt injection,” jailbreak”, “do anything now” and “dan” to measure false positives.
HarmfulQ:  A small, harmful‑only set centered on bias and social‑context harms—excellent for stress‑testing pure blocking recall.*
Malware Benign:  Control set of 5,000 benign code snippets from a code‑translation benchmark, paired with the same “analyze or execute” prompt, intended to measure false positives.
XSTest: human‑written mix of safe and unsafe prompts that evaluates calibration—blocking harm without overblocking - making it ideal for testing helpfulness‑vs‑harmlessness trade‑offs.*
*Benchmarks taken from
Guardbench.
Digging deeper into the numbers, you can see that Glean sees a low false positive rate as compared to other providers. This is an important metric to zoom in on for production AI, because the user experience gets degraded if we block too many benign requests. The reason that Glean is able to achieve a low false positive rate is that we use a dual model approach to AI security, running results through a second model to ensure their accuracy.
Glean
Open-source LLM safety model
Hyperscale cloud provider 1
Hyperscale cloud provider 2
% false positive rate on prompt injection attacks
3.0%
6.1%
1.4%
17.4%
We make it easy for users to trace the violation to the source for quick remediation with an AI security dashboard complete with the surrounding context, the prompt, source file, agent identifier, user information, and chat session.
AI security is a continued investment for Glean, today and into the future. As attacks evolve, we’ll be in the thick of it, adjusting our models to keep enterprises safe. We’re excited by today’s progress and benchmark results, and we’ll keep evolving to stay ahead and protect enterprise customers.
AI security models are part of Glean Protect+, a premium security suite. They are available today in GCP deployments.
Back to all stories
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Get The Resource
Get The Resource
Work AI for all.
Get a Demo
Work AI that works.
Get a demo
Ask AI for a summary about Glean
634 2nd Street
San Francisco, CA 94107
United States
Language
English (United States)
Japanese (Japan)
PRODUCT
Work AI Platform
Workplace Search
Assistant
Data Analysis
Deep Research
Canvas
Prompt Library
Agents
Agent Builder
Agent Orchestration
Agent Library
Agentic Engine
Connectors
Model Hub
Security
System of Context
SOLUTIONS
All Teams
Engineering
Sales
Marketing
Support
People
Retail
Financial Services
USE CASES
Enterprise AI
Enterprise Search Software
AI Agent Orchestration
COMPARISONS
Glean vs other alternatives
Glean vs ChatGPT Enterprise
Glean vs Microsoft 365 Copilot
Glean vs Claude Enterprise
RESOURCES
Resources Center
Product Videos
Guides
Customer Stories
Blog
Events
Webinars
Developers
Help Center
Download Glean
Product Drops
AI Glossary
Gleaniverse Community
COMPANY
About
Careers
Newsroom
Referrals
Partners
Trust center
260 Sheridan Ave, Suite 300
Palo Alto, CA 94306, United States
Gartner®, Peer Insights™, Voice of the Customer for Insight Engines, Peer Contributors, 28 June 2024.
Gartner Peer Insights content consists of the opinions of individual end users based on their own experiences, and should not be construed as statements of fact, nor do they represent the views of Gartner or its affiliates.
Gartner does not endorse any vendor, product or service depicted in this content nor makes any warranties, expressed or implied, with respect to this content, about its accuracy or completeness, including any warranties of merchantability or fitness for a particular purpose.
GARTNER is a registered trademark and service mark of Gartner, Inc. and/or its affiliates in the U.S. and internationally, and PEER INSIGHTS and GARTNER PEER INSIGHTS CUSTOMERS’ CHOICE BADGE is a registered trademark of Gartner, Inc. and/or its affiliates and are used herein with permission. All rights reserved.
©
2026
, Glean Technologies, Inc.
Website Terms
Privacy
