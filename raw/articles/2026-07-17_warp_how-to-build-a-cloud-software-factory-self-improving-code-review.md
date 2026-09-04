# How to Build a Cloud Software Factory: Self-Improving Code Review

*Part 3 in the Cloud Software Factory series*

Previous posts described the factory pipeline and the skills self-improvement loop. This post covers the **self-improving code review agent** — an outer-loop agent that observes the code reviewer and improves its own review capabilities over time.

## The Problem

Static code review rules drift. Style guides go stale. What was a good review practice six months ago may be outdated today. Traditional approaches require humans to manually update review guidelines, which doesn't scale.

## The Solution: Outer-Loop Code Review Agent

Warp's outer-loop agent sits above the code review agent in the factory pipeline. Its job is to **observe the reviewer's performance and improve the review agent's skill definitions** over time.

### How It Works

1. **Observe**: The outer-loop agent monitors code review outputs — accepted/rejected changes, human feedback on reviews, post-merge defects that should have been caught.
2. **Analyze**: Compares review agent output against specifications and expected behavior. Validates that suggestions are correct before they reach the recommendation stage.
3. **Improve**: Updates the code review skill's text instructions and deterministic Python scripts (not on-the-fly generation). Skills are explicit, testable units — not prompt magic.

### Skill Format

Unlike the general skills self-improvement loop (which uses YAML definitions), the code review skill relies on two components:
- **Text instructions**: Human-readable guidelines for what to check and how to evaluate
- **Deterministic Python scripts**: Executable validation logic that checks code against specs, runs builds before making recommendations, and validates suggestions

This approach means the review agent's behavior is **deterministic and auditable** — not a black box LLM prompt that drifts.

## Multi-Model Cost Management

The code review system routes across multiple models and harnesses to manage costs effectively:
- **Cheap models** handle routine linting and style checks
- **Expensive models** are reserved for complex semantic analysis and architectural review
- The outer-loop tracks cost-per-review and optimizes routing over time

## CI/CD Integration

The review pipeline runs as a **GitHub Action** that produces a structured `review.json` output file. This structured format enables:
- Programmatic consumption by downstream tools
- Caching and diffing across review iterations
- Integration with Oz's orchestration layer

This is an example of [[concepts/agentic-engineering]] at the meta-level — an agent that improves other agents. Warp's approach contrasts with [[entities/claude-code]]'s more conversational review style.
