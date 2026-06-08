---
title: Dan Luu
description: Software reliability engineer and data analyst known for systematic incident analysis and empirical studies of tech company failure modes.
type: entity
created: 2026-06-08
updated: 2026-06-08
aliases:
  - danluu
  - daniel-luu
tags:
  - person
  - infrastructure
sources:
  - raw/articles/danluu.com--cache-incidents--1d05e743.md
  - https://danluu.com/cache-incidents/
  - https://danluu.com/
---

# Dan Luu

**Dan Luu** is a software reliability engineer and data analyst known for systematic incident analysis, empirical studies of tech company failure modes, and data-driven critiques of industry practices. His work focuses on understanding how large-scale distributed systems fail and why organizational knowledge about failures is lost over time.

## Overview

Luu's research methodology is characterized by thorough data collection, historical incident analysis, and systematic pattern identification. Unlike typical post-mortems that focus on a single incident, Luu's work aggregates failures across years to identify recurring patterns and systemic weaknesses. This approach has been applied to Twitter cache reliability, failover testing, cloud service outages, and other infrastructure domains.

## Notable Work

### Twitter Cache Incident Analysis (2012–2022)

In "[A decade of major cache incidents at Twitter](https://danluu.com/cache-incidents/)" (co-authored with Yao Yue), Luu documented 6 SEV-0 and 6 SEV-1 cache-related incidents at Twitter over a decade, along with 38 less severe incidents. The analysis revealed several key patterns:

**Cache as a Failure Amplifier:**
- **Cascading failures**: Cache outages caused total site outages because architectures designed around cache performance lacked backing DB capacity to handle failover
- **Positive feedback loops**: High-volume, low-latency SLOs worsened "death spiral" failure modes when cache degradation triggered increased load on remaining nodes
- **Hardware-level failure modes**: Cache servers were sensitive to kernel, firmware, and hardware anomalies — including a BMC health check that caused packet drops every 20 hours 40 minutes
- **Host ejection inconsistency**: Different workers making independent routing decisions led to cache key duplication and stale data serving
- **memcached as a critical path**: The vast majority of Twitter's cache was a fork of memcached, making the findings broadly applicable to distributed systems

**Knowledge Loss in Tech Organizations:**
- Document links rot within 2–3 years (90%+ link failure rate for pre-2012 incidents)
- Human memory provides inconsistent accounts of the same events
- Viral stories about incidents are frequently wrong due to exaggeration and self-aggrandizing narratives
- "Gresham's law of stories" — incorrect stories tend to win out over correct ones in public memory

**Organizational Patterns:**
- Fixes for earlier incidents were often incompletely applied, causing repeat failures
- Issues identified by engineers as serious were frequently deprioritized until they caused major incidents
- Operational knowledge was concentrated in individual engineers rather than institutionalized

### AI Infrastructure Relevance

The cache failure modes documented by Luu are highly relevant to modern AI infrastructure:
- **KV cache management**: LLM inference serving relies on massive key-value caches with similar failure mode risks (positive feedback loops, death spirals during high-load inference)
- **Distributed inference**: Multi-node AI serving architectures face the same cache consistency and host ejection challenges documented in Twitter's memcached infrastructure
- **Prompt caching**: AI systems increasingly cache prompts and intermediate results, introducing similar staleness and inconsistency risks
- **Capacity planning**: The gap between announced and operational capacity that Luu documented in Twitter's infrastructure parallels current debates about AI data center buildout claims

## References

- [danluu.com](https://danluu.com/) — Personal blog and research archive
- [A decade of major cache incidents at Twitter](https://danluu.com/cache-incidents/) — Co-authored with Yao Yue. Documents 6 SEV-0 and 6 SEV-1 cache incidents at Twitter (2012–2022).
