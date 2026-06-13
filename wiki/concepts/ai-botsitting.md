---
title: "AI Botsitting"
created: 2026-06-13
updated: 2026-06-13
type: concept
tags: [labor, ai-adoption, productivity, human-agent-collaboration, economics, automation, reliability]
sources: [raw/articles/2026-06-11_businessinsider-ai-botsitting.md]
---

# AI Botsitting

## Summary

"Botsitting" is the hidden human labor of monitoring, correcting, and retrying AI system outputs in production workflows. Coined by researchers at Glean's Work AI Institute (with collaborators from Notre Dame, Stanford, and UC Berkeley), the term describes the often-overlooked work required to make AI useful — feeding it context, debugging mistakes, cleaning up errors, and moving information between disconnected AI systems. A survey of 6,000 workers across the US, UK, and Australia (December 2025–January 2026) found that white-collar workers spend an average of **6.4 hours per week** botsitting — nearly a full working day every week.

## Key Findings

### Quantified Costs
- **6.4 hours/week** average spent botsitting across surveyed knowledge workers
- Workers with unusually high botsitting time are **73% more likely** to be actively job-hunting
- Only 13% of workers said their organization was performing significantly better because of AI, despite 87% using AI and 75% reporting personal productivity gains
- The gap between individual gains and organizational performance is a **productivity paradox** — individual time savings are consumed by new forms of invisible labor

### Nature of Botsitting Work
- **Context-feeding**: repeatedly providing AI tools with information they should already have or be able to retrieve
- **Output debugging**: identifying and correcting hallucinations, errors, and nonsensical outputs
- **Error cleanup**: fixing downstream consequences of AI mistakes
- **System integration labor**: acting as the human bridge between disconnected AI tools that don't interoperate
- **Automating the enjoyable**: some workers report being asked to automate the parts of their jobs they find most meaningful (e.g., customer relationship building), leaving only supervision of AI agents

### Worker Experience
Botsitting is described as "often tedious" and "exhausting" work that is "not rewarded and it's not appreciated or tracked or measured and certainly not incentivized within the organization" (Rebecca Hinds, head of Work AI Institute). This creates a perverse dynamic: AI was supposed to eliminate drudgery, but it has created a new class of invisible, unappreciated labor performed by the same workers it was meant to liberate.

## The Automation Paradox in Practice

Botsitting exemplifies the [[after-automation]] paradox: rather than eliminating human labor, automation often shifts it to new forms that are less visible, less valued, and sometimes more tedious than the original work. While AI can handle routine cases, edge cases and hallucinations create a constant need for human oversight — inverting the promise that AI would handle the boring work and free humans for creative tasks. Instead, many workers find themselves performing [[human-in-the-loop]] monitoring as their primary function, with the engaging work increasingly handed to AI.

## Economic Implications

The botsitting finding challenges standard ROI calculations for enterprise AI deployment. If organizations are not tracking or accounting for the 6.4 hours/week of hidden labor, the true cost of AI adoption is systematically underestimated. This connects to broader questions in [[ai-slop-productivity-paradox|AI slop and the productivity paradox]] — the phenomenon where AI-generated outputs create downstream cleanup costs that offset or reverse initial productivity gains. As AI systems become more prevalent, the aggregate economic drag of unmeasured botsitting labor may be substantial, echoing the [[ai-labor-displacement|AI labor displacement]] debate — not about jobs eliminated, but about jobs transformed in ways that reduce worker satisfaction and increase hidden costs.

## Why Botsitting Happens

- **AI unreliability**: hallucinations, confabulations, and unpredictable failures require constant vigilance
- **Edge cases**: real-world situations that fall outside AI training distributions need human judgment
- **Context gaps**: AI tools lack persistent organizational memory, requiring humans to repeatedly supply context
- **Tool fragmentation**: disconnected AI systems create integration labor as humans move data between them
- **Incentive misalignment**: organizations measure AI adoption but not the human labor required to make it usable

## Mitigation Strategies

The Glean report found that organizations seeing better results are not simply deploying more AI — they are investing in the **work around AI**:
- Ensuring workers have access to the right context at the right time
- Training employees on effective AI use, not just tool access
- Establishing clear standards for what good AI-assisted work looks like
- Recognizing and tracking botsitting labor instead of treating it as invisible
- Integrating AI tools to reduce the human bridge-work between systems

## Worker Impact

Beyond productivity, botsitting has psychological effects. Workers who absorb this labor without recognition grow exhausted and disengage. The finding that high-botsitting workers are 73% more likely to job-hunt suggests that unmanaged botsitting is a retention risk. When workers are asked to automate the meaningful parts of their work and spend their remaining time supervising AI agents, the result is a form of [[agent-productivity|productivity paradox]] at the individual level: more output, less satisfaction.

## Related Concepts

- [[human-in-the-loop]] — the design pattern botsitting operationalizes, often without deliberate design
- [[after-automation]] — the paradox that automation creates new forms of human labor
- [[ai-slop-productivity-paradox]] — AI-generated outputs creating downstream cleanup costs
- [[ai-labor-displacement]] — broader labor transformation dynamics in AI adoption
- [[agent-productivity]] — individual productivity effects of AI agents, including cognitive costs

## Sources

- Glean Work AI Institute report (December 2025–January 2026), survey of 6,000 workers across US, UK, Australia
- Business Insider: "The rise of the 'botsitters'" by Thibault Spirlet (June 11, 2026)
- "The Great Coding Reset" series, Business Insider (June 2026)
- "Cognitive Revolution" podcast interview with Rebecca Hinds (June 11, 2026)
