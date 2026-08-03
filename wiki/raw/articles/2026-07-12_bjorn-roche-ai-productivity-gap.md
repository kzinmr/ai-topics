# The AI Productivity Gap

- **Source**: https://bjorg.bjornroche.com/management/ai-productivity-gap/
- **Published**: July 12, 2026
- **Author**: Bjorn Roche (Engineering Leader, NYC)
- **HN Discussion**: https://news.ycombinator.com/item?id=49152222 (56 pts)

## Summary

Despite AI's clear productivity benefits for engineering teams, the actual productivity gains are smaller than many leaders expect. Building production features still takes almost as long as it used to. The article quantifies the "AI productivity gap" by breaking down how developers actually spend their time.

## Key Arguments

### Senior Developer Time Breakdown

| Activity | Pre AI | Post AI |
|---|---|---|
| Writing New Code | 1.5h | 0.5h |
| Reading and Debugging | 1.5h | 1.0h |
| Design And Architecture | 1.0h | 1.0h |
| Code Reviews | 0.75h | 0.75h |
| Documentation and Admin | 0.75h | 0.75h |
| Testing, CI/CD, deployment | 0.5h | 0.75h |
| Mentoring / Pair programming | 0.5h | 0.5h |
| Meetings | 1.5h | 1.5h |
| **Total** | **8.0h** | **6.75h** |

Net savings: ~1.25h/day or ~15% productivity gain for senior devs.

### Junior Developer Time Breakdown

| Activity | Pre AI | Post AI |
|---|---|---|
| Writing New Code | 2.75h | 1.0h |
| Reading and Debugging | 1.5h | 1.0h |
| Testing, CI/CD, deployment | 0.75h | 1.0h |
| Other (design, reviews, docs, learning, meetings) | 3.0h | 3.0h |
| **Total** | **8.0h** | **6.0h** |

Net savings: ~2h/day or ~25% productivity gain for juniors.

## Key Observations

1. AI makes coding 3x faster, but coding is only a fraction of developers' work
2. AI can make non-coding work slower (AI-written PRDs are harder to parse)
3. Testing/CI/CD actually takes more time with AI-generated code (more code to test)
4. Juniors gain more from AI than seniors because they spend more time coding
5. "Being a good coder is table stakes" — system reasoning, collaboration, and requirements decomposition are the real job
6. Leaders saying "AI does junior work now, we only hire seniors" have it backwards

## HN Discussion Highlights

- Many engineers report AI review burden is actually higher (AI-generated code is less trustworthy)
- Some report 10x productivity gains for certain tasks
- Mental overhead of managing multiple parallel agents
- AI enables unnecessary refactoring and "what-if" exploration
- Onboarding is much faster with AI assistance
- The "O-ring problem": bottlenecks shift to non-coding activities
