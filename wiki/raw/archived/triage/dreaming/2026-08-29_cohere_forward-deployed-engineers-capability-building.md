---
title: "FDEs: Building Capacity, Not Dependency"
source: "Cohere Blog"
url: "https://cohere.com/blog/forward-deployed-engineers-capability-building"
scraped: "2026-08-29T06:01:00.168440+00:00"
lastmod: "2026-08-27"
type: "sitemap"
---

# FDEs: Building Capacity, Not Dependency

**Source**: [https://cohere.com/blog/forward-deployed-engineers-capability-building](https://cohere.com/blog/forward-deployed-engineers-capability-building)

The main bottleneck in enterprise AI adoption has shifted downstream from experimentation to production deployment.
Proving that AI can perform useful tasks under controlled conditions is one thing, but adapting it to the real-world operating environment of an enterprise can be a much more complex undertaking. Many enterprises stall at this bottleneck. According to Deloitte’s
2026 State of AI in the Enterprise
report, only 25% of organizations have moved 40% or more of their AI pilots into production.
Enterprises have a few options for closing this deployment gap. They can tackle the work internally, but doing so may require specialized AI deployment expertise, familiarity with the underlying technology, and sufficient engineering capacity. Alternatively, they can bring in outside support from IT consultancies, specialist AI firms, independent contractors, model-aligned service providers, or the model vendor’s own forward-deployed engineers (FDEs).
Each option has its strengths and tradeoffs. In this post, we’ll present the case for model-vendor FDEs, explain the dependency concerns that this approach raises, and outline how a capability-building FDE approach can address those concerns while giving customers greater operational control over their AI deployments.
What FDEs offer that third-party services can’t easily replicate
Vendor FDEs occupy a unique position: they work hands-on within the customer’s technical and operating environment while remaining part of the company building the underlying AI technology.
FDEs therefore bring deeper product expertise and direct access to research and engineering teams. They can apply lessons from previous deployments to new customer environments and maintain visibility into emerging product capabilities and platform direction. For customers, that often means faster answers, fewer avoidable workarounds, and deployment decisions that account for where the technology is heading, as well as what it can do today.
FDE engagements can also make it easier to address gaps in the product itself. For example, when a Cohere customer use case exposes a capability that our existing product doesn’t fully support, our FDEs can inspect or modify the underlying code and work with core engineering to develop a solution that addresses the immediate need and can be generalized across customers.
Third-party providers often bring valuable industry expertise, broader transformation experience, and greater independence when evaluating solutions from different vendors. But when they encounter a product limitation, unexpected model behavior, or an integration problem, they tend to have less visibility into the underlying causes and have fewer options for resolving the issue at the source. They may have to build bespoke workarounds, adding complexity and maintenance burden, or escalate the issue back to the vendor.
FDEs can operate across that boundary. They can diagnose problems with first-hand knowledge of the technology, determine whether to address the problem through the deployment or the product itself, and bring the relevant product or engineering teams into the loop directly. For example, one Cohere customer had built an agent that generated briefing reports ahead of meetings by pulling relevant information from calendars and other sources. The agent was failing frequently because its instructions referenced tools that didn’t exist, while some of the underlying tool calls couldn’t handle the required context. Our FDE rebuilt the agent and modified the supporting tools — including its Slack integration — to handle larger contexts.
The FDE advantage isn’t simply faster escalation; it’s a wider set of options for getting the deployment to work without defaulting to engineering around the product.
The core concern: Do FDEs create vendor lock-in?
The advantages of the FDE approach also raise some legitimate concerns about vendor lock-in. After all, if an enterprise uses FDEs to help design, deploy, and troubleshoot its production AI system, won’t it remain dependent on those FDEs over time?
Not necessarily.
Some degree of commercial or architectural dependency comes from the underlying technology choice, rather than from who deploys it. For example, relying on a particular vendor’s models, APIs, or platform can make future migrations harder, increasing the customer’s exposure to changes in pricing, product direction, or commercial terms. Importantly, these dependencies can exist whether the system is deployed by FDEs, a third party, or the customer’s own team.
The more FDE-specific lock-in risk is
operational dependency
. If critical knowledge of the system remains with the vendor’s engineers, internal teams will struggle to diagnose problems, modify the system safely, or verify that it continues to perform as requirements and models change. In other words, the enterprise may end up owning the deployment but not the capability to operate it.
Building customer capability into the FDE approach
Operational dependency is not an inevitable consequence of working with FDEs. It largely depends on whether the vendor builds knowledge transfer into the delivery model from the outset rather than treating it as a handover exercise at the end.
Consider Cohere’s approach. Our FDEs work alongside our customers’ engineering teams through architecture, integration, deployment, testing, and troubleshooting. This co-building approach helps transfer the tacit implementation knowledge that customer teams need to understand and operate the system themselves. We also run customer enablement sessions for major features, equipping internal “champions” with the knowledge to teach and support teams across their organization. For more technical topics, our FDEs can run sessions on topics such as
Model Context Protocol
(MCP) to help customer developers establish stronger implementation patterns.
Our FDEs work alongside our customers’ engineering teams through architecture, integration, deployment, testing, and troubleshooting.
Capability-building also extends beyond knowledge of the system itself. Our FDEs can help customer teams develop reusable software engineering practices around deployment, load testing, and connector development, as well as build agents and automated workflows that work reliably in production. They also help teams navigate technical documentation, use AI to investigate questions, and diagnose issues without escalating every problem back to the FDE team.
Our FDEs also help customers build test suites that reflect core product functionality, giving internal teams their own means of verifying that the system continues to behave as expected as model versions, integrations, and configurations change.
Our ultimate goal is not only to transfer knowledge about the current deployment, but to give our customers the ongoing ability to operate, evaluate, troubleshoot, and extend the AI system independently.
Our ultimate goal is not only to transfer knowledge about the current deployment, but to give our customers the ongoing ability to operate, evaluate, troubleshoot, and extend the AI system independently.
Toward operational independence
For enterprises evaluating FDE approaches, getting AI systems into production is only one part of the equation. They should also consider what kind of dependency the engagement is likely to leave behind. The best FDE engagements use deep product expertise and engineering access to reduce the customer’s reliance on that expertise over time. Ultimately, close vendor involvement should create greater operational independence, not less.
Want to help customers build production AI systems and the capability to operate them independently? Explore
open FDE roles at Cohere
.
Blog
Written By
Nastya Kats
Member of Technical Staff, Forward Deployed Engineer
Tags
Enterprise AI
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
