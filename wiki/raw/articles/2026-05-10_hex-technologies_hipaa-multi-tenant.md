---
title: "Introducing Hex HIPAA multi-tenant | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/hipaa-multi-tenant/"
scraped: "2026-05-10T01:29:09.346474+00:00"
lastmod: "2023-10-25"
type: "sitemap"
---

# Introducing Hex HIPAA multi-tenant | Hex 

**Source**: [https://hex.tech/blog/hipaa-multi-tenant/](https://hex.tech/blog/hipaa-multi-tenant/)

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
Introducing Hex HIPAA multi-tenant
Advancing data in healthcare, securely
Caitlin Colgrove and DJ McCulloch
Security
October 25, 2023
Share:
twitter
linkedin
In this article
Supporting more healthcare customers
Advancing data in healthcare, securely
Get started for free
Among all the industries that data have the potential to revolutionize, healthcare stands alone. Healthcare industries generate an enormous volume of data every day, from patient records to clinical imaging to trial results, and there are myriad opportunities for insights to improve life and longevity for billions of humans.
Patients and providers, however, deserve privacy and accountability, and their data needs to be stored and processed securely. In the US, the Health Insurance Portability and Accountability Act (HIPAA) provides a set of regulations and guidelines for people working with healthcare data. It also outlines very harsh penalties for mis-managing said data: breaches can result in many millions of dollars of fines.
A common misconception is that HIPAA is a “certification” one can achieve. In reality, HIPAA compliance is a
risk management process
. There’s no agency or outside auditor that gives you a badge of approval. It’s really up to each organization to make their own determination on how much risk they’re willing to bear, and demonstrate to an auditor that their controls are sufficient to manage that risk.
Before an organization can provide services to a HIPAA Covered Entity that involves protected health information (PHI), they need to sign a Business Associate Agreement (BAA) as a Business Associate of the Covered Entity. This is essentially a contract that outlines what PHI is being disclosed, and permissible uses and disclosures of PHI. Signing a BAA assumes significant risk:  the Business Associate is responsible for managing and processing the PHI securely, on the hook if it causes a breach through negligence.
So if you are, let’s say, a data analytics company, you need to approach this topic with care. Signing BAAs can unlock a lot of new business, but also a lot of additional risk, so you need to make sure you are handling customer data with extreme diligence.
Supporting more healthcare customers
At Hex, security is central to everything we do. We have invested heavily here from day one, including a dedicated
Trust Program
, unbroken SOC 2 Type II attestations, regular audits, and an
active bug bounty program
. Our existing Hex Cloud multi-tenant environment already offers a secure, scalable place to work with data.
In the past, however, the heightened risk from handling PHI led us to
only
sign BAAs for customers on our single-tenant deployments. These setups are isolated from the internet and other customers, which reduces the risk profile. Single-tenant deployments, however, also introduce additional infrastructure overhead and cost, which makes them prohibitive for smaller companies.
Today, however,
we are introducing a new option: HIPAA Multi-Tenant,
which will allow healthcare customers to use Hex at a greatly reduced total cost.
Under the hood, this new instance is mostly the same as our existing Hex Cloud multi-tenant, which already offers best-in-class security. This new HIPAA stack, however, offers further assurances:
It is not exposed to the open internet – users can only access this stack through VPN or a zero-trust option, greatly reducing the attack surface area for any malicious actors;
Relatedly, it does not allow for self-serve signup, so any customers with access have been vetted by our team, with a signed, paid contract in place;
HIPAA-specific controls such as shortened session lifetimes and other, tighter defaults;
The flexibility to introduce additional controls or configuration changes specific to healthcare customers’ needs
Together, these steps further reduce the total risk profile for customers and ourselves, making signing BAAs – and the resulting assumption of risk – more tolerable and insurable at lower costs.
HIPAA multi-tenant sits alongside our existing US multi-tenant and EU multi-tenant stacks, as well as our single-tenant offering, meaning customers have access to a range of deployment options based on their unique security needs and paranoias.
Advancing data in healthcare, securely
Our greatest joy is seeing customers do amazing things with Hex – especially when it has the potential to improve lives. We are proud to already have dozens of amazing healthcare customers using the product, and are excited to welcome many more through our new HIPAA multi-tenant.
Get in touch to learn more or get started!
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
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
