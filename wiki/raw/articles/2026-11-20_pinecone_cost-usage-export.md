---
title: "Pinecone now exports cost and usage data in FOCUS format"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/cost-usage-export/"
scraped: "2026-11-20T06:00:37.603446+00:00"
lastmod: "2026-11-19T16:00:02Z"
type: "sitemap"
---

# Pinecone now exports cost and usage data in FOCUS format

**Source**: [https://www.pinecone.io/blog/cost-usage-export/](https://www.pinecone.io/blog/cost-usage-export/)

←
Blog
Pinecone now exports cost and usage data in FOCUS format
Gavin Johnson
Nov 19, 2026
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Finance teams use FinOps tools to charge cloud costs back to the teams and applications that incur them, but those tools couldn't use Pinecone's billing file until someone downloaded it and reshaped it by hand. The
Cost and Usage Export API
provides Pinecone cost and usage data in
FOCUS
, the open billing format built for FinOps tools. Finance teams can now see Pinecone spend by project and index in the FinOps reports they already use for cloud spend.
Teams create an export for any window in the past year, from the Usage page in the console or through the
cost-usage-exports
endpoint of the Admin API. Each export is a zip of FOCUS v1.4 CSV files, which load as is into FinOps tools that read FOCUS. Rows name their project and resource, and the export includes project and index tags, so finance teams can charge each team or application its share. Platform teams can schedule a job to pull exports into a data warehouse or FinOps pipeline, so no one has to download spreadsheets by hand.
The Cost and Usage Export API is available to organizations on the Enterprise plan.
To get started, create an export from the Usage page in the console, or read the
usage report docs
for more info.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
