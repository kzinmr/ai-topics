---
title: "Inference Speed Development"
created: 2026-04-13
updated: 2026-04-13
tags: [ai-coding, development-cadence, shipping-speed, test-driven-ai, ui-development, agentic-engineering]
aliases: ["shipping-at-inference-speed", "inference-speed-shipping", "ai-development-cadence"]
related: [[agentic-engineering]], [[claude-code-best-practices]], [[cognitive-cost-of-agents]], [[ai-coding-reliability]]
sources:
  - url: "https://steipete.me/posts/2025/shipping-at-inference-speed"
    author: "Peter Steinberger (@steipete)"
    date: "2025"
    title: "Shipping at Inference Speed"
---

# Inference Speed Development

**Inference Speed Development** describes a paradigm shift in software development cadence enabled by AI coding agents. Instead of the traditional "write code → test → review → deploy" cycle measured in hours or days, developers can now iterate at the speed of LLM inference — measured in seconds or minutes.

The core insight: **when the bottleneck shifts from human typing/thinking time to AI inference time, development velocity becomes a function of how quickly you can prompt, review, and iterate.**

---

## The Traditional vs. AI Development Cycle

### Traditional Development (Human-Speed)

```
Think → Write code (hours) → Run tests → Fix bugs → Code review (hours) → Deploy
Total cycle: Days to weeks per feature
```

The bottleneck was human cognitive load and typing speed.

### AI-Augmented Development (Inference-Speed)

```
Define task → AI writes code (seconds/minutes) → Review → AI fixes → Deploy
Total cycle: Minutes to hours per feature
```

The bottleneck shifts to **prompt clarity, review capacity, and iteration count**.

---

## Key Principles (Steipete's Patterns)

### 1. Test-Driven AI Development

**Write tests first, then let the AI implement.** This pattern ensures:
- AI output is immediately verifiable
- Regression detection is automatic
- The "definition of done" is clear before generation starts

```
1. Human writes failing test
2. AI implements to pass test
3. Human reviews both test + implementation
4. Iterate until green
```

This mirrors TDD but compresses the cycle from hours to minutes.

### 2. UI Development Pipeline

Steipete identifies an optimal flow for UI work:

```
Figma/Screenshot → HTML/CSS implementation → AI integration with app logic
```

The pattern:
- **Visual input** (screenshot/Figma) gives AI concrete reference
- **HTML/CSS first** isolates styling concerns from logic
- **Integration last** connects UI to data/models

This works because visual-to-code translation is where AI excels, while business logic requires human review.

### 3. Iteration Budgets Over Perfection

> "50 tries to get one thing right is actually good when each try takes 30 seconds."

Key insight: **AI iteration is cheap, human iteration is expensive.** A task that takes 50 AI attempts (25 minutes) is still faster than a human spending 2 hours getting it right the first time.

This requires a mindset shift from "get it right immediately" to "get it right eventually through rapid iteration."

---

## The Changing Role of Humans

### From Writer to Reviewer/Director

| Traditional | Inference-Speed |
|-------------|-----------------|
| Write code | Define tasks and constraints |
| Debug line-by-line | Review AI output at architectural level |
| Estimate time | Estimate iteration count |
| Own implementation | Own correctness and direction |

Steipete notes: **"The developer becomes more of a director than a performer."**

### New Human Skills Required

1. **Prompt articulation**: Clearly defining what "done" looks like
2. **Rapid review**: Scanning AI output for correctness, security, maintainability
3. **Iteration strategy**: Knowing when to fork, when to retry, when to intervene
4. **Architecture judgment**: AI handles implementation; humans handle design

---

## The 3 Major Challenges

### 1. Context Window Bloat

AI agents accumulate conversation history, leading to:
- Slower inference (more tokens to process)
- Instruction decay (model loses focus)
- Higher costs

**Mitigation**: Start fresh sessions for distinct tasks, use CLAUDE.md for persistent context.

### 2. Agent Overconfidence

AI agents may:
- Make incorrect assumptions without asking
- Implement the wrong thing confidently
- Skip edge cases

**Mitigation**: Explicit constraints in prompts, test-first approach, mandatory human review before commit.

### 3. UI Breakage

Generated UI code often:
- Works in isolation but breaks in context
- Misses responsive design considerations
- Has subtle visual differences

**Mitigation**: Screenshot-driven iteration, visual regression testing, incremental integration.

---

## Connection to Reliability Concerns

Inference Speed Development amplifies both productivity and risk:

- **Faster shipping** means bugs ship faster too
- **Less human typing** doesn't mean less human responsibility
- **More iterations** doesn't guarantee correctness — only faster convergence

This connects directly to [[ai-coding-reliability]]: the Amazon outages demonstrate what happens when inference-speed shipping bypasses reliability gates.

---

## Practical Metrics

Steipete's experience suggests:

| Metric | Traditional | Inference-Speed |
|--------|-------------|-----------------|
| Feature cycle time | Days | Hours |
| Iteration cost | High (human time) | Low (API cost) |
| Review burden | Per commit | Per AI output batch |
| "Right first time" rate | ~70% | ~2% |
| "Right after 50 tries" rate | N/A | ~90%+ |

The key insight: **AI doesn't need to be right on the first attempt — it needs to be cheap to retry.**

---

## Related Concepts

- [[agentic-engineering]] — The broader methodology shift this enables
- [[claude-code-best-practices]] — Practical patterns for Claude Code users
- [[cognitive-cost-of-agents]] — The hidden cost of reviewing vs. writing
- [[ai-coding-reliability]] — Why speed without reliability gates causes outages
- [[claude-code-source-patterns]] — How Anthropic engineers inference-speed patterns into Claude Code itself

## Sources

- [Peter Steinberger: Shipping at Inference Speed](https://steipete.me/posts/2025/shipping-at-inference-speed) — @steipete
- [Alpaylan: Claude Code as an IDE (10x-20x Productivity Claims)](https://www.reddit.com/r/ChatGPTCoding/comments/1k0y830/) — r/ChatGPTCoding discussion
- [Sankalp: My Experience with Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/) — complementary best practices
