---
title: "Factory and Databricks: Building Software Powered by Data"
source: "Factory Blog"
url: "https://factory.com/news/databricks-partnership"
scraped: "2026-10-20T06:00:39.751583+00:00"
lastmod: "2026-10-17T01:09:43.000Z"
type: "sitemap"
recovered_body: "2026-10-20 (sitemap scrape captured nav chrome only; body re-fetched via curl + article extraction)"
---

# Factory and Databricks: Building Software Powered by Data

**Source**: [https://factory.com/news/databricks-partnership](https://factory.com/news/databricks-partnership)

October 19, 2026 - 3 minute read - Company, Partners

Today, Factory is announcing a partnership with Databricks so customers can use the data and models in the Databricks Data + AI Platform to power software that is built or migrated by Factory.

At Factory, we have seen this pattern in our customers. Factory and Databricks are helping one of the largest global enterprises migrate a complex data platform that powers hundreds of business applications to the Databricks Data + AI Platform. This includes petabytes of data and hundreds of thousands of tables. The business applications have user interfaces, application services, integration and API layers, business logic and rules, security, and management features. All of these carry dependencies and expectations that must survive the migration.

When Factory joined this effort, much of the data had already moved to the Databricks lakehouse. The next challenge was rebuilding the applications and workflows that use the data. The key takeaway: data modernization and software modernization need to happen together. Modernizing the data foundation creates an opportunity to build and deploy applications and AI agents that use enterprise data to drive business outcomes.

Previously, migrations of this scale were resource intensive and risky. Data engineers migrated tables and rebuilt pipelines. Application developers manually analyzed and wrote new software. Dependencies between data and applications require careful planning, development, testing, and coordination. To make it more challenging, these teams have different skills, different tools, and different processes. Even minor changes to a data pipeline creates many downstream impacts and requires handoffs between teams.

Factory and Databricks brings the migration into a single engineering workflow: agents and automation to understand the existing system, plan the migration, build, and validate that the data and applications deliver the right capabilities to users. Databricks provides the open, governed foundation for data, analytics and AI, while Factory brings agentic software engineering capabilities to help teams modernize and build the applications that depend on that foundation.

A successful migration starts with understanding the current data and applications.

Factory Droids work across application code, data pipelines, SQL, tests, and available documentation. With access to the relevant repositories and tools, Droids can trace how an application depends on a stored procedure, which data pipeline creates its inputs, and where a change could affect downstream behavior. Factory’s context integrations bring code and engineering knowledge into that work. Combined with access to data and assets governed through Databricks Unity Catalog, this approach helps teams connect application dependencies with the enterprise data foundation that supports them.

That understanding becomes the migration plan. Droids can help identify dependencies, propose an implementation sequence, and define the checks needed to establish compatibility. Factory’s Missions provide planning, milestones, and coordinated execution for work spanning multiple components. Engineers review the plan and resolve ambiguous business rules before implementation proceeds.

With the plan in place, Droids use Databricks API access to create and run jobs, execute queries to validate results, and deploy applications. For example, migrating an application could involve changing the underlying operational database from legacy Postgres to Databricks Lakebase, rewriting data transformations in Python, building and scheduling a Lakeflow pipeline, creating an AI/BI dashboard, and finally comparing the new application and its data against the legacy application.

The partnership between Databricks and Factory enables three categories of use cases: PDLC Automation, Migration and Modernization, and Cybersecurity.

Factory can help teams move from a product requirement through planning, development, testing, security, documenting, monitoring, and enhancing applications built on or powered by data in Databricks. This includes building and evolving data-driven applications and AI-powered software that leverage the Databricks Data + AI Platform as an open, governed foundation.

Factory can help teams analyze, plan, and execute data platform migrations to Databricks and the applications that depend on the data in Databricks.

Factory can help teams remediate vulnerabilities in the applications monitored by Databricks Lakewatch.

The migration that brought Factory and Databricks together is just one example of how our platforms complement each other. We expect many enterprises will benefit by creating a tighter loop between the data and software powered by data. To make it easier, we’re also excited that qualifying customers can purchase Factory through the Databricks Marketplace using up to 10% of their existing Databricks commitment.

Ready to use Factory and Databricks together? Simply connect Databricks in Factory under Settings → Connectors, then run this task:

“Build an automation that checks the Lakehouse-to-Lakebase Sync workflow every night and posts a recap of its progress to the team's Slack channel.”

One connector, one automation, one loop, with a recap in Slack every morning. The setup guide covers managed MCP servers, running Droids on Databricks-served models, and webhook automations. Prefer to see it first? Book a demo.
