---
title: "Unlock enhanced performance and usage monitoring with Datadog and new Prometheus endpoints"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/datadog-prometheus-for-serverless/"
scraped: "2026-05-10T01:27:21.120168+00:00"
lastmod: "2024-11-06T15:00:06Z"
type: "sitemap"
---

# Unlock enhanced performance and usage monitoring with Datadog and new Prometheus endpoints

**Source**: [https://www.pinecone.io/blog/datadog-prometheus-for-serverless/](https://www.pinecone.io/blog/datadog-prometheus-for-serverless/)

←
Blog
Unlock enhanced performance and usage monitoring with Datadog and new Prometheus endpoints
Ana Wishnoff
Nov 6, 2024
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Our updated Datadog integration and new Prometheus endpoints make discovering insights into your indexes' performance and usage easier than ever. Building upon existing health metrics, you can now also monitor request frequency and duration, consumption of read and write units, and core metrics on latency through our
Datadog integration
or directly via our
new Prometheus endpoints
.
Our Datadog integration now delivers metrics for both serverless and pod-based indexes, with
25 new metrics
for more granular performance monitoring and improved observability. With the updated integration, you can:
Monitor the number of requests made and request duration by endpoint
(e.g. the count of upsert requests, query requests, update requests, and more).
Explore and visualize your read and write unit consumption
, plus the size of your serverless indexes.
Track usage patterns over time and easily identify anomalies
with out-of-the-box dashboards. Customize your experience further by setting conditional formatting for selected values, viewing certain metrics side by side, or changing data visualizations.
Get alerted
when the number of writes to your serverless index exceeds a specified threshold to avoid latency issues. This recommended monitor can be customized to meet your team’s specific configuration.
Our out-of-the-box Datadog dashboard for serverless surfaces health metrics on throughput, latency, read and write units, and more.
Getting started
To set up the Datadog integration, go to Datadog's
Pinecone integration page
. In the Configure tab, simply add your project ID and API Key for the project you want to monitor. Under Monitoring Resources, you'll find the dashboard and recommended monitors, with a full list of available metrics in the Data Collected tab.
For non-Datadog users, these new metrics are fully accessible via Prometheus. The endpoints are designed with HTTP service discovery to automatically detect and target all serverless indexes across regions within a project, making it easy to monitor the health and performance of your entire environment — no matter how it’s distributed.
To set up monitoring directly with Prometheus, you'll need your Pinecone API Key and project ID. Update the
scrape_configs
section of your
prometheus.yml
file with this information to start querying. For step-by-step instructions, a list of available metrics, and example queries, check out our
Monitor with Prometheus
guide.
Prometheus metrics and our Datadog integration are available to all users on Standard and Enterprise plans. Visit our
documentation
to learn more and start up-leveling your observability today.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
