---
title: "Measuring AI Agent Autonomy in Practice"
url: "https://www.anthropic.com/news/measuring-agent-autonomy/"
date: 2026-04-18
source: Anthropic Blog
---

# Measuring Agent Autonomy

## Key Findings (Anthropic, February 2026)

Analysis of millions of human-agent interactions reveals that **agent autonomy in practice lags behind model capability** — the "deployment overhang."

### Metrics

| Metric | Finding |
|--------|---------|
| Autonomy Duration (99.9th %ile) | Claude Code: <25 min → >45 min (Oct 2025-Jan 2026) |
| User Auto-Approval Rate | ~20% (new) → >40% (experienced, 750+ sessions) |
| User Interrupt Rate | 5% → 9% of turns (experienced users actively monitor) |
| Agent Self-Stops | Claude asks for clarification >2x more often than humans interrupt on complex tasks |
| Tool Call Safeguards | 80% have safeguards, 73% human-in-loop, only 0.8% irreversible |
| Domain Split | ~50% software engineering; emerging: healthcare, finance, cybersecurity |

### Deployment Overhang

- METR estimates Claude Opus 4.5 can handle ~5-hour human-equivalent tasks
- Claude Code's 99.9th percentile is ~42 minutes
- Gap reflects real-world pauses, human feedback loops, environmental friction vs. idealized benchmarks
- Smooth increase in long turn durations suggests autonomy growth is driven by **user trust, task ambition, and product iteration**, not just raw capability
- Internal data: success rate on hardest tasks doubled while human interventions dropped from 5.4 → 3.3 per session

### Evolving Oversight Strategies

Experienced users shift from **pre-action approval** to **post-action monitoring & intervention**:
- High-complexity tasks show *less* human involvement (67%) vs. low-complexity (87%)
- Step-by-step approval becomes structurally impractical as task length grows
- Interrupt rates plateau at high experience levels

### Agent-Initiated Stops as Safety

Common self-stop reasons:
- Presenting approach choices (35%)
- Gathering diagnostics/test results (21%)
- Clarifying vague requests (13%)
- Requesting credentials/access (12%)

Human interruptions typically occur for: missing context/corrections (32%), slowness/hanging (17%), taking over next steps (14%).

### Limitations

- Single-provider scope (Anthropic only)
- Public API lacks session-linking; analysis is tool-call level
- Risk/autonomy scores are Claude-generated, not manually verified
- Overrepresents multi-step workflows (coding) vs. single-action deployments
