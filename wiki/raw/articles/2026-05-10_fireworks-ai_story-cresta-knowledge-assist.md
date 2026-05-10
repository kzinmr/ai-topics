---
title: "How Cresta drives millions of real-time, AI-powered contact center interactions with Fireworks"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/story-cresta-knowledge-assist"
scraped: "2026-05-10T01:27:52.257039+00:00"
lastmod: "2026-02-12T18:52:37.000Z"
type: "sitemap"
---

# How Cresta drives millions of real-time, AI-powered contact center interactions with Fireworks

**Source**: [https://fireworks.ai/blog/story-cresta-knowledge-assist](https://fireworks.ai/blog/story-cresta-knowledge-assist)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Story Cresta Knowledge Assist
How Cresta drives millions of real-time, AI-powered contact center interactions with Fireworks
PUBLISHED
12/8/2024
Cresta is a trailblazer in transforming contact centers through domain-specific AI, using large language models to deliver accurate, contextually relevant guidance to agents from day one. By analyzing millions of interactions,
Cresta
’s platform boosts productivity, engagement, and sales outcomes. With over $270 million in funding—including a recent $125 million Series D—and more than 250 employees, Cresta continues to raise the bar for AI-driven customer experiences.
To maintain its competitive edge and scale customized AI models efficiently, Cresta sought an infrastructure solution with stringent production standards—reliable uptime, minimal latency, and continuous optimization—while meeting the demanding throughput required by large language models. They found their answer in Fireworks, a provider of scalable AI infrastructure.
Knowledge Assist: Enabling real-time, personalized guidance at scale
Cresta’s
Knowledge Assist
unifies diverse knowledge sources—FAQs, websites, internal repositories—into a single, intelligent access point. Powered by Fireworks’ infrastructure, it delivers contextually relevant information at the exact moment agents need it, eliminating the need to sift through scattered data. By combining retrieval-augmented generation (RAG) and guided workflows, Knowledge Assist streamlines operations, improves key metrics like handle time and first call resolution, and aligns with Cresta’s vision of making every agent as effective as its best performer.
Learn how to use Knowledge Assist in this
demo
from Cresta.
The challenge of implementing a tailored, production-grade compound AI system
As Cresta developed
Knowledge Assist
, the team encountered several critical hurdles:
•
Production-grade scalability:
To handle hundreds of millions of customer conversations, Cresta required low-latency, high-availability inference at scale—all while ensuring predictable, optimized unit costs.
•
Inefficient open-source inference libraries:
Traditional approaches relying on costly GPU instances and less efficient OSS inference solutions fell short in guaranteeing the production quality (uptime, latency, availability) and continuous optimization (speed, TCO) necessary for sustained growth.
•
Complex customization:
Fine-tuning LoRA adapters for each customer’s unique knowledge domain introduced volatile traffic patterns and underscored the need for a specialized infrastructure solution capable of delivering top-tier performance, cost efficiency, and reliability.
Cresta needed a specialized solution capable of enterprise-level stability, rapid response times, and ongoing performance refinements.
"We have received tremendous support from the amazing Fireworks team. From troubleshooting and quick incident responses to insightful explanations of metrics, their engagement has been exceptional. The low-latency, high-throughput serving of LLMs has been particularly valuable, as latency is crucial for our real-time applications." – Chuan Wang, Technical Lead Manager at Cresta.
Scalable, cost-effective infrastructure for multi-customer customization
Cresta selected Fireworks after a rigorous evaluation of its ability to meet these exacting conditions. Fireworks demonstrated the flexibility and capacity to support domain-specific models under real-world conditions, ensuring that Cresta’s agents could consistently access the insights they needed.
•
Single base model, multiple customizations
: Cresta utilizes a single mistral-based Ocean model cluster enriched with LoRA adapters, enabling domain-specific variations without provisioning separate models for each customer.
•
Massive scalability
: Fireworks’ infrastructure can support thousands of LoRA adapters, giving Cresta the flexibility to efficiently cater to diverse customer use cases.
•
Significant cost reduction
: By serving multiple adapters through a single base model, Cresta achieves up to a 100x cost reduction compared to GPT-4.*
•
Rapid validation and optimization
: Serverless access and dedicated trial environments let Cresta quickly test performance baselines, simulate production traffic, and refine their models.
•
Effortless scaling and reliability
: Fireworks provides dedicated instances, self-service scaling capabilities, and continuous optimization, ensuring Cresta can seamlessly adjust capacity as demand fluctuates.
Throughout this process, Fireworks offered expert technical support, proactive incident management, metrics-driven guidance, and collaborative product development—empowering Cresta to continually improve its AI initiatives.
"Fireworks' Multi-LoRA capabilities align with Cresta's strategy to deploy custom AI through fine-tuning cutting-edge base models. It helps unleash the potential of AI on private enterprise data." - Tim Shi, Co-Founder and CTO of Cresta
For more details on multi-LoRA and Cresta’s innovations with Knowledge Assist, check out
Cresta’s blog post
and learn more about multi-LoRA in
Fireworks’ dedicated blog
.
Powering a new era of intelligent customer engagement
By deploying Fireworks’ infrastructure to host and scale Ocean-1—Cresta’s foundational model for the contact center—Cresta has unlocked transformative outcomes that directly advance their mission of redefining customer interactions:
•
Surpassing benchmark performance:
Fine-tuned Ocean-1 variants, enhanced with LoRA adapters, now consistently outperform GPT-4 in RAG-powered tasks, setting a new bar for delivering timely, context-rich guidance to agents.
•
Quality at production scale:
Fireworks ensures Ocean-1 models run with minimal latency and robust uptime, delivering reliable performance even as traffic and workloads shift, critical for sustained enterprise-grade deployments.
•
Accelerating sustainable growth:
Achieving a 100x cost reduction per inference unit empowers Cresta to rapidly scale Knowledge Assist to a wider customer base, driving mass adoption and reinforcing their position as an industry disruptor.
•
Elevating the contact center experience:
By blending domain-specific insights with real-time guidance, agents resolve issues faster and more accurately, improving key KPIs like handle time and first-call resolution.
•
Pioneering the future of Customer Intelligence:
With Fireworks as the cornerstone, Cresta can continuously refine Ocean-1, integrating the latest innovations and ensuring that their AI-driven solutions redefine the standards for quality, efficiency, and impact in customer engagement.
"Being able to serve the best models with cutting-edge latency provides us with an enormous competitive advantage"
–
Chuan Wang, Technical Lead Manager at Cresta.
With fresh funding and a growing R&D team, Cresta is poised to push AI-powered customer interactions even further. Fireworks is proud to partner with Cresta to support new capabilities that help contact centers optimize agent performance, streamline operations, and craft memorable customer experiences.
As Ping Wu, CEO of Cresta, notes,
“
We’re enabling contact centers to leverage insights and automation to fundamentally reimagine how they operate—while keeping the human element front and center
.”
By leveraging Fireworks, Cresta overcame significant challenges in delivering customized, low-latency AI models to their clients. The collaboration addressed their immediate infrastructure needs and positioned them for future growth and innovation. Fireworks continues to support Cresta's mission to revolutionize customer interactions through AI, providing the tools and expertise necessary for unparalleled service and performance.
Ready to develop compound AI systems?
•
Accelerate your AI potential
: Discover how the
Compound AI System F1
drives faster, more efficient model performance.
•
Unlock audio-driven insights
: Transform voice data into actionable intelligence with our new
audio transcription feature
.
•
Join our community
: Connect with other developers and the Fireworks team in our
Discord channel
.
•
Get in touch
: Ready to transform your AI strategy?
Contact us
to discuss how Fireworks can power your next-generation AI features.
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
