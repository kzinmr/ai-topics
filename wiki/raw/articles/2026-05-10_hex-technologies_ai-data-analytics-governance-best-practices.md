---
title: "AI & data analytics governance best practices | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/ai-data-analytics-governance-best-practices/"
scraped: "2026-05-10T01:29:07.333202+00:00"
lastmod: "2026-01-16"
type: "sitemap"
---

# AI & data analytics governance best practices | Hex 

**Source**: [https://hex.tech/blog/ai-data-analytics-governance-best-practices/](https://hex.tech/blog/ai-data-analytics-governance-best-practices/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
Platform
chevron-down
Products
Agentic notebooks
Powerful, deep-dive analysis without the silos
Conversational self-serve
The best BI tool isn't just a BI tool
semantic-models
Context Studio
Build trust in data with semantic models and AI governance
cli
Hex CLI
Control your analytics from the terminal
Capabilities
Exploratory analysis
Go from quick question to deep analysis to data app in one place
Embedded analytics
Ship secure, customer-facing data experiences
app-builder
Data apps
Build and share interactive dashboards and reporting
Integrations
Out-of-the-box connections and flexible APIs
magic
AI & agents
Agentic workflows to empower your entire team
Solutions
chevron-down
lightbulb
Explore all solutions
One connected system - infinite data answers
By team
solutions-data-leader
Data leader
Focus your team and scale answers
solutions-product
Product
Build your product with data, not gut feels
solutions-marketing
Marketing
Turn scattered data into clear growth opportunities
solutions-sales
Sales
Clear pipeline. Confident forecasts
solutions-customer-success
Customer success
Create a complete view of customer health
Enterprise
Resources
chevron-down
Get started
integrations
Switching to Hex
A guide to getting started on agentic analytics
Templates
Jumpstart with pre-built projects
Hex Foundations
Video series
help
Docs
Resources and product guides
Changelog
Product updates
Inspiration
Blog
From data teams to data teams
Guides
Learn how to do more with data, together
Events
Learn and connect with peers
Customer stories
Empowering the best data teams
Partners
Learn more about our partnerships
save
Download
The Data Leader's Guide to AI Analytics
A practical roadmap for understanding and implementing AI to accelerate your data team and enable true self-service.
Pricing
Log In
Get started
Blog
AI & data analytics governance best practices
How to build governance that works for analytics and AI without blocking the work that matters
The Hex Team
Data
January 16, 2026
Share:
twitter
linkedin
In this article
What combined AI and data governance actually means
Governance for LLMs and generative AI
The business case for governance investment
Regulatory frameworks worth knowing
Choosing an operating model
Best practices for policies and controls
A practical 90–180 day roadmap
Making governance work in practice
Get started for free
You've probably heard "garbage in, garbage out" applied to data for decades. But when AI enters the picture, the stakes shift: garbage in, confidently amplified garbage out at scale. Your data doesn't just inform a report anymore. It feeds models that inform decisions impacting customers, revenue, and regulatory standing.
That's the reality data leaders and analytics engineers are navigating right now. You're being asked to deploy AI faster while ensuring everything stays compliant, auditable, and fair. Meanwhile, shadow AI spreads through your organization every time someone pastes company data into ChatGPT. The governance policies you've built around data quality, access, and cataloging weren't designed for systems that learn, drift, and make semi-autonomous decisions. This guide covers how to build frameworks that work for both analytics and AI, reducing risk while actually speeding delivery rather than blocking it.
What combined AI and data governance actually means
Data governance and AI governance overlap but aren't the same thing. Traditional data governance focuses on managing data as a static asset: quality standards, access controls, metadata management, lineage tracking, and privacy compliance. AI governance extends into bias detection, model explainability, performance monitoring, and accountability for autonomous decisions.
Poor data governance undermines AI governance directly. Biased data tends to produce biased AI. Inconsistent metric definitions produce unreliable model inputs. Gaps in lineage tracking make it impossible to audit what went wrong when a model misbehaves.
The work that matters happens where these two disciplines meet. You need clear accountability for decisions, transparency in processes and outcomes, systematic bias detection, protection of data and models, complete documentation trails, and meaningful human oversight over automated decisions. The specific framework matters less than whether your team actually follows it. Governance that exists on paper but nobody uses creates the worst outcome: false confidence that you're protected when you're not.
Data teams extending governance to AI need to think beyond traditional access controls. The
EU AI Act
now imposes explicit data governance requirements for high-risk systems. Article 10 specifies that training, validation, and testing datasets must be relevant, representative, sufficiently free of errors, and complete in view of the intended purpose. These frameworks demand that you can demonstrate how data flowed into model decisions, not just that you had a policy document somewhere.
Governance for LLMs and generative AI
Large language models add governance considerations that traditional frameworks don't address. When your AI system is a foundation model rather than a narrow classifier, the attack surface expands considerably.
Prompt logs become data assets that need governance. Every question employees ask an AI assistant potentially contains sensitive information: customer names, revenue figures, strategic plans. These logs need retention policies, access controls, and audit trails just like any other data source. Organizations using retrieval-augmented generation (RAG) pipelines face additional complexity: the documents feeding context to the model inherit all the governance requirements of the underlying data, plus new concerns about how context selection affects outputs.
Generative AI also blurs the line between data consumption and data creation. When an AI system writes SQL, generates reports, or summarizes findings, the outputs become inputs for downstream decisions. Governance needs to cover not just what data the model can access, but what it can produce and how those outputs get validated before they influence business decisions.
Your governance framework needs to treat AI-generated content as a distinct data category with its own quality checks, lineage tracking, and approval workflows. Inspectable AI outputs matter here: if you can't see the SQL that generated an answer, you can't govern the logic that produced it.
The business case for governance investment
Strong governance can deliver measurable returns, though the numbers vary widely by organization and context.
IBM's 2025 Cost of a Data Breach Report
found that organizations with mature AI governance saw average breach costs significantly lower per incident than those without. Organizations with weaker governance controls had materially higher average breach costs.
The shadow AI premium is particularly striking. In IBM's study, breached organizations with high levels of shadow AI paid as much as $670,000 more per breach than those with proper oversight. Shadow AI happens when governance creates friction and people work around it. The cost measures what you pay when ungoverned systems fail.
British Airways was
fined £20 million by the ICO
over its data breach, with the fine based on failures to implement appropriate security and governance measures. Most organizations invest less in compliance frameworks than they pay in average penalty costs, before factoring in reputational damage.
But these statistics alone won't convince your leadership to invest in governance. What moves the needle is demonstrating that governance enables speed rather than blocking it. Teams that can deploy AI safely and quickly tend to outperform teams that either move fast and break things, or move slowly and frustrate stakeholders.
Regulatory frameworks worth knowing
You don't need to memorize every framework, but understanding the landscape helps you make defensible choices. Three frameworks matter most for AI governance in 2025, and they serve different purposes.
The EU AI Act carries legal force with extraterritorial scope. If your AI system's outputs are used within the EU, you're subject to its requirements regardless of where you developed the system. The Act uses a risk-based classification: unacceptable risk (banned), high risk (heavy regulation), limited risk (transparency requirements), and minimal risk (largely unregulated). Most analytics AI falls into limited or minimal risk categories, but anything touching hiring, credit decisions, or critical infrastructure triggers high-risk obligations. Article 10 mandates explicit data governance standards for high-risk AI, including conformity assessments, documentation requirements, and ongoing monitoring.
The
NIST AI Risk Management Framework
provides voluntary guidance organized around key functions: Map (understand context and risks), Measure (assess and track), and Manage (prioritize and act), with governance roles woven throughout. It offers operational methodology without legal force. Use it as a starting point for structuring your internal approach, particularly if you need a common vocabulary for cross-functional governance discussions.
ISO 42001:2023
is the first certifiable AI management system standard. Unlike voluntary NIST guidance, ISO 42001 provides third-party verification that your framework is properly established. The standard covers the entire AI lifecycle from design through deployment and retirement. Consider certification if you need formal proof of governance maturity for enterprise sales, regulatory compliance, or stakeholder assurance.
Many organizations use these frameworks together: EU AI Act compliance as the legal baseline, NIST AI RMF for operational structure, and ISO 42001 for third-party validation. The key is choosing what fits your regulatory exposure and organizational maturity rather than trying to implement everything at once.
Choosing an operating model
How you structure governance responsibilities matters as much as what policies you write.
Centralized governance
concentrates decision-making within a single team. This provides uniform policies and clear accountability, which works well in highly regulated industries or smaller organizations where consistency matters more than speed. The tradeoff: the central team often becomes a bottleneck as data volume grows, and domain expertise gets lost when governance decisions happen far from the data.
Federated governance
distributes responsibility across business units while maintaining central oversight for standards and escalations. Domain teams govern data they understand best, which increases agility and adoption. This typically works for larger enterprises with mature data cultures, though it requires strong coordination to prevent fragmentation. Without clear escalation paths and shared standards, you end up with 50 definitions of "revenue" across the organization.
Hybrid models
treat data as products with dedicated owners, combining federated principles with product thinking. Each data product has an owner responsible for quality, documentation, and governance. Self-service operates within guardrails through automated policy enforcement. This approach scales well but requires significant tooling investment to make guardrails frictionless rather than blocking.
The model you choose matters less than whether people actually follow it. Governance frameworks that exist on paper but nobody follows create the worst outcome: false confidence that you're protected when you're not. Analytics engineers know this pattern well. Semantic layers become governance theater when tools make compliance hard.
Best practices for policies and controls
This is where governance moves from strategy to execution.
Define quality standards for AI inputs
Traditional data quality dimensions like accuracy, completeness, and timeliness need calibration for machine learning. You're not just checking whether data is "clean" in the traditional sense. You need to track data drift, ensure training sets remain representative as your business evolves, and validate that model inputs meet the standards your AI systems require.
Build access management that addresses AI-specific risks
Define who can use what data for which purposes. This sounds obvious, but AI introduces new wrinkles: can a model trained on customer data be used to generate synthetic training examples? Can an analyst query an AI assistant that has access to data they wouldn't normally see directly?
Establish data sharing protocols that account for how AI systems aggregate and transform information, not just who can view raw tables.
Make lineage tracking non-negotiable
Lineage enables compliance by showing how data flows from source through transformations to final outputs. Unify lineage with data quality and metadata management. When something goes wrong with an AI-generated insight, you need to trace the path from model output back to the training data and business logic that shaped it.
This played out at
Calendly
, where the analytics team eliminated metric definition drift by implementing standardized metric libraries in Hex. They documented governance decisions directly alongside analysis work, creating a cross-functional KPI library that helps resolve conflicting reports and ramps new hires faster.
Treat semantic models as your control plane
Semantic modeling defines metrics once and reuses them everywhere. When you define "closed-won conversion rate" in a semantic model, every AI query, every analyst exploration, and every executive dashboard draws from the same governed definition. This approach makes AI outputs auditable: when an AI assistant answers a revenue question, the semantic layer ensures it uses the same definition finance uses, and you can inspect exactly how the answer was derived.
Governance success means fewer shadow metrics and consistent KPIs across tools and teams.
Inventa
integrated the dbt semantic layer to define maintainable metrics consistent with internal reporting, then exposed those metrics through governed, self-serve interfaces, giving suppliers daily insights instead of weekly without creating ungoverned workarounds.
Hex
connects semantic models directly into the query interface. Every question, whether asked through SQL, Python, the Notebook Agent, or Threads, draws from the same governed definitions. The AI generates SQL with full schema and semantic context, and every output is inspectable so your team can verify the logic before it influences decisions.
Document models thoroughly
Document every step in the AI governance process to ensure alignment with company values, customer expectations, and legal standards. This includes training data sources, preprocessing decisions, model architecture choices, and evaluation criteria.
When regulators or auditors ask how your AI system reached a particular decision, you need documentation that answers the question, not just a policy statement that you intended to be compliant.
Test for bias systematically
Bias testing isn't a one-time gate before deployment. Train AI on diverse datasets, conduct regular bias checks, and build monitoring that catches when models start behaving differently across demographic groups or customer segments.
Monitor continuously
Schedule regular audits to evaluate AI alignment with governance principles. Adapt monitoring as regulations evolve. What passes compliance today may not pass tomorrow as the EU AI Act implementation phases in and other jurisdictions follow.
A practical 90–180 day roadmap
Getting governance right takes time. Here's a realistic timeline.
Weeks 1–4:
Assess your current state. Identify stakeholders and executive sponsors. Define business drivers and the specific pain points you're trying to solve, whether that's shadow AI proliferation, metric inconsistency, regulatory exposure, or all three. Don't try to boil the ocean. Start with a clear problem.
Weeks 5–8:
Choose your operating model. Establish your governance council with clear roles: data owners accountable for specific domains, data stewards handling day-to-day quality and access, governance leads coordinating across teams. Create change management strategies because technology without behavior change means benefits stay theoretical.
Weeks 9–12:
Draft initial policies covering data quality, access controls, metadata management, and AI ethics. Select a pilot domain with high value and manageable scope, often a single business unit or data product where you have executive sponsorship and motivated users. Define success metrics you can actually measure: reduction in metric conflicts, time to answer for governed self-serve, shadow tool usage, compliance audit findings.
Days 91–180:
Implement data quality rules and monitoring for the pilot domain. Establish metadata management and lineage tracking. Deploy access controls. For AI governance specifically, implement model registration and risk assessment for any AI touching the pilot data. Gather feedback, refine policies based on real-world application, and document wins to build momentum for broader adoption.
Early wins matter more than comprehensive coverage. When you can show that a focused pilot cut PII discovery time from weeks to hours, or eliminated conflicting metric definitions across three departments, you build the internal case for expanding governance investment across the organization.
Making governance work in practice
Governance fails when it creates friction that pushes people toward shadow tools. The organizations getting this right share common patterns: they treat governance as a business enabler rather than a compliance exercise, they start with focused pilots rather than comprehensive frameworks, and they automate wherever possible so governance doesn't become a bottleneck.
Building governance directly into collaborative workflows means compliance happens naturally rather than as an afterthought. Business users who need governed self-serve access without SQL knowledge can use
natural language interfaces
that pull from curated, trusted data sources, reducing the backlog of ad hoc requests that consume analyst time while keeping everything auditable.
The goal isn't perfect policies. It's making the trusted data path easier than the ungoverned alternative. When data teams curate semantic models that AI systems use for every query, when lineage tracking happens automatically, when business users can explore data without leaving the governed environment, governance stops being red tape and starts being infrastructure.
Hex
connects governed semantic layers directly into the query interface, so every question draws from the same metric definitions. AI outputs are fully inspectable, which means your analysts can verify the logic, your compliance teams can audit the transformations, and your stakeholders can trust the chain from question to answer.
Ready to see how governed analytics works in practice?
Sign up for Hex
or
request a demo
.
Share:
twitter
linkedin
Get "The Data Leader’s Guide to Agentic Analytics"  — a practical roadmap for understanding and implementing AI to accelerate your data team.
Download
Request a demo
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
🔊
🎧
on
🌎
.
Company
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
