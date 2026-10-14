---
title: 'Google SRE - Incident Management: Postmortem Analysis'
source_url: https://sre.google/workbook/postmortem-analysis/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/postmortem-analysis.html
original_sha256: dab1f1b861e1361aef44b1f638787758bbd3ad60e35808014a3f1a518149566d
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/postmortem-analysis/
ingested: '2026-10-14'
sha256: 61a3cef7f168857bf0de1f816b18fd449ad4d034818d9348b31b40a56d8d068b
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Results of Postmortem Analysis
At Google, we have a standard
postmortem template
that allows us to consistently capture the incident root cause and trigger, which enables trend analysis. We use this trend analysis to help us target improvements that address systemic root-cause types, such as faulty software interface design or immature change deployment planning.
Table C-1
shows the breakdown of our top eight triggers for outages, based on a sample of thousands of postmortems over the last seven years.
Table C-1.
Top eight outage triggers, 2010–2017
Binary push
37%
Configuration push
31%
User behavior change
9%
Processing pipeline
6%
Service provider change
5%
Performance decay
5%
Capacity management
5%
Hardware
2%
Table C-2
presents the top five contributing root-cause categories.
Table C-2.
Top five root-cause categories for outages
Software
41.35%
Development process failure
20.23%
Complex system behaviors
16.90%
Deployment planning
6.74%
Network failure
2.75%
