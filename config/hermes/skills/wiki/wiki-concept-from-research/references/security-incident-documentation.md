# Security Incident Documentation Pattern

When creating a wiki page for an AI/agent security incident (e.g., data breach, vulnerability disclosure, supply chain attack), use this structure. Derived from the Moltbook Breach 2026 concept page (`concepts/moltbook-breach-2026.md`).

## Required Sections

### 1. Overview (1-2 paragraphs)
- What happened
- When it happened
- Scale (numbers: affected agents, records, tokens)
- Why it matters (first-of-its-kind framing if applicable)

### 2. Technical Root Cause
What was the *technical* failure?
- **Incident**: Supabase RLS disabled + frontend anon key exposed
- **Fix**: 2 SQL statements (ALTER TABLE ENABLE ROW LEVEL SECURITY + CREATE POLICY)
- Show code snippets for both the vulnerable state and the fix
- Name the technology stack (Supabase, AWS, etc.)

### 3. Exposed Data Table
What data was leaked, and in what quantities?

| Data Type | Scale |
|-----------|-------|
| API tokens | 1.5M |
| Emails | 35K |
| Total records | 4.75M |

### 4. Attack Chain
Step-by-step: what could an attacker do with the vulnerability?
1. First step
2. Second step
3. Final impact

### 5. Timeline
Chronological table from the technology's origin through the incident's discovery, disclosure, and industry response.

| Date | Event | Details |
|------|-------|---------|
| | | |

### 6. Related Vulnerabilities
If the incident was part of a broader security crisis (as OpenClaw in Jan 2026 had CVE-2026-25253 + ClawHavoc concurrently), list each with:

| Attack | Description | Scale |
|--------|-------------|-------|
| **Name** | One-liner | affected count |

### 7. Industry Response
- Security firm analyses (which firms, what they said)
- CVEs assigned
- Patches released
- Detection tools/IOCs published

### 8. Lessons Learned / Technical Takeaways
Bullet-point list of actionable lessons:
- Specific to this incident (e.g., "Supabase RLS disabled is catastrophic because X")
- Generalizable to the class of system (e.g., "AI agents treat instructions as executable commands by default")

## Raw Article Pipeline

Before writing the concept page:
1. **web_search** for primary journalistic sources (404 Media, Reuters, Wired, Fortune)
2. **web_search** for security firm analysis (Astrix, Adversa, Treblle, Palo Alto)
3. **web_search** for technical breakdowns (CVE details, IoC lists)
4. **web_extract** each source and save to `wiki/raw/articles/` with full frontmatter
5. Create the concept page cross-referencing all raw articles

## Cross-Reference Strategy
- Link to `concepts/ai-agent-security` for the broader vulnerability taxonomy
- Link to any affected platforms (e.g., `entities/openclaw`, `concepts/openclaw-ecosystem`)
- Link to related CVEs if applicable
- Update the existing security concept page to add a "Real-World Incidents" section that points to the new incident page
