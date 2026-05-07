---
source: https://treblle.com/blog/moltbook-breach-breakdown
title: "Moltbook Breach Breakdown: How an Exposed Database Let Anyone Hijack 770,000 AI Agents"
author: Bruno Boksic
publication: Treblle
date: 2026-02-02
tags:
  - moltbook
  - openclaw
  - security
  - incident
  - supabase
  - rls
---

# Moltbook Breach Breakdown

**Date:** February 2, 2026

## Technical Breakdown

The breach was caused by a misconfigured Supabase backend lacking Row-Level Security (RLS) policies. The Supabase URL and publishable key were exposed in the frontend JavaScript, allowing anyone to query the entire database directly via the Supabase REST API.

### The Vulnerability (SQL)
```sql
-- NO Row-Level Security policies defined
-- Anyone with the anon key can query ALL data
SELECT agent_id, api_key, claim_token, verification_code, owner_id FROM agents;
```

### The Fix (2 SQL statements)
```sql
ALTER TABLE agents ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can only view their own agents"
ON agents FOR SELECT USING (auth.uid() = owner_id);
```

## AI Agents as "Attack Multipliers"

- **Impersonation:** High-profile agents could spread misinformation
- **Coordinated Disinformation:** 770,000 agents to simulate "organic" consensus
- **Financial Drain:** Unbounded agent creation could rack up hundreds of thousands in API costs
- **Persistent Threats:** AI agents with memory transform prompt injections into long-term exploits
