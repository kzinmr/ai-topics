---
title: "CourtListener"
type: entity
created: 2026-06-03
updated: 2026-06-03
tags:
  - company
  - legal-tech
  - open-data
aliases:
  - "Free Law Project"
sources:
  - https://www.courtlistener.com/
  - https://free.law/
---

# CourtListener

**CourtListener** is a free legal research platform operated by the **Free Law Project**, a 501(c)(3) non-profit organization. It provides public access to millions of US court opinions, oral argument recordings, and legal data.

| | |
|---|---|
| **Type** | Legal Research Platform / Open Data |
| **Organization** | Free Law Project (501(c)(3) non-profit) |
| **Website** | [courtlistener.com](https://www.courtlistener.com/) |
| **Parent Org** | [free.law](https://free.law/) |

## Key Facts

- Operated by the Free Law Project, founded by Brian Carver and Michael Lissner
- Provides open access to US federal and state court opinions
- Database contains **9 million+ US case law opinions** (as of June 2026)
- Offers APIs for programmatic access to legal data
- Powers RECAP, a crowdsourced archive of US federal court documents (PACER)
- Data is used by legal tech companies, researchers, and AI platforms

## Data as AI Infrastructure

CourtListener's opinion database has become a critical data source for AI legal platforms. In June 2026, [[entities/harvey]] (AI legal platform) integrated CourtListener's 9M+ opinions directly into their Knowledge feature, enabling citation-grounded legal research within their agentic workflow platform.

This represents a broader pattern: **open legal data platforms becoming foundational infrastructure for AI agents** that need authoritative, citable sources for domain-specific tasks. CourtListener's structured, searchable corpus of opinions is uniquely suited for RAG-based legal applications.

## RECAP Archive

CourtListener operates the RECAP project, which crowdsources PACER (Public Access to Court Electronic Records) documents. Users install a browser extension that uploads PACER documents they access, building a free public archive. RECAP contains millions of federal court documents.

## API

CourtListener provides a REST API for accessing legal data programmatically:
- Search opinions by court, date, judge, keywords
- Access oral argument audio recordings
- Retrieve citation networks and relationship data
- Used by legal tech startups and academic researchers

## Related

- [[entities/harvey]] — integrated CourtListener's 9M+ opinions into AI legal platform
- [[concepts/legal-agent-benchmark]] — benchmark for legal AI agents that depends on authoritative case law sources

## Sources

- [CourtListener](https://www.courtlistener.com/)
- [Free Law Project](https://free.law/)
- [RECAP Project](https://www.courtlistener.com/recap/)
