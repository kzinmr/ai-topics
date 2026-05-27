---
title: Agentic Property-Based Testing (Anthropic + Hypothesis)
type: concept
aliases: [agentic-pbt, anthropic-property-based-testing]
created: 2026-04-14
updated: 2026-05-27
status: active
sources:
  - https://red.anthropic.com/2026/property-based-testing/
  - https://mmaaz-git.github.io/agentic-pbt-site/
  - https://github.com/HypothesisWorks/hypothesis
  - http://drmaciver.com/2026/04/how-ive-been-using-claude-code/
  - https://antithesis.com/blog/2026/hegel/
tags:
  - concept
  - coding-agents
  - developer-tooling
  - evaluation

---
---
---

# Agentic Property-Based Testing

Anthropic + Hypothesis joint research (NeurIPS 2025 DL4C Workshop). Claude Code agents autonomously infer code invariants (properties) from type annotations, docstrings, function names, and comments, then generate and execute PBT using the Hypothesis framework.

## Agent Architecture

```
Analyze Target → Propose Properties → Generate Tests → Self-Reflect → Report
     ↓                ↓                   ↓              ↓          ↓
  Read code,     Infer invariants    Write Hypothesis  If fail:   Formatted
  docs, usage    from type ann,      tests with        real bug   bug report
  context        docstrings, names   auto-generated    or bad     only when
                                   inputs              test?      confident
```

**Key Design Features:**
- **TODO list** for long-term reasoning management
- **Self-reflection loop** to significantly reduce false positives
- **Opus 4.1** and **Sonnet 4.5** show significant performance improvements over Sonnet 4
- Grounding in explicit documentation/usage patterns is important

## Evaluation Results

### Phase 1 (Opus 4.1)
- Tested **100+ PyPI packages** (NumPy, SciPy, Pandas, etc.)
- 984 bug reports generated
- 50 manual review results:
  - 56% were valid bugs
  - 32% were valid & reportable
- With **Rubric ranking** applied (top reports):
  - 86% validity rate
  - 81% reportable rate

### Phase 2 (Sonnet 4.5)
- Ran multiple times on 10 critical packages
- Verified high-severity bugs with **automated evaluation agent + 3 expert reviewers**
- Strict Validation Protocol: To avoid maintainer fatigue, only filing bugs confirmed by 3 experts + author
- All data (valid/invalid/unvalidated) released publicly

## Notable Bugs Discovered

| Package | Function | Issue | Impact |
|---------|----------|-------|--------|
| `numpy` | `random.wald` | Returns negative numbers | Catastrophic cancellation; fix improved relative error by ~10 orders of magnitude |
| `aws-lambda-powertools` | `slice_dictionary()` | First chunk duplicated | Iterator not incremented during reconstruction |
| `cloudformation-cli-java-plugin` | `item_hash()` | Same hash for all lists | Destructive `.sort()` returns None |
| `tokenizers` | `calculate_label_colors()` | Invalid HSL CSS output | Missing closing bracket |
| `python-dateutil` | `easter()` | Non-Sunday date (Julian calendar) | Maintainer-confirmed subtle semantics |

## Limitations

> "Deriving properties from code with subtle or complex semantics remains difficult. If the code makes an implicit assumption, only the library maintainers can decide what the correct property to test is."

**Implicit assumptions** — When code has implicit assumptions, only the library maintainer can determine the correct test properties.

## Future Directions

- **Proactive Security**: Counter LLM-powered exploit generation by identifying vulnerabilities before deployment
- **Automated Patching**: "If it is possible to (nearly) completely specify the correctness properties of a block of code, then correcting the bug becomes significantly easier." — LLM-generated patches for maintainer review
- **Ecosystem Expansion**: Scaling to more PyPI projects, improving automated verification pipelines

## Connection to DRMacIver / Antithesis

This research aligns perfectly with **David R. MacIver**'s (Hypothesis author, Antithesis Senior Engineer) philosophy:

> "Property-based testing is going to be a huge part of how we make AI-agent-based software development not go terribly."

Anthropic research co-author **Liam DeVoe** is also a Hypothesis core maintainer. Like MacIver, he has joined Antithesis, advancing the development of Agentic PBT and Hegel (cross-language PBT protocol).

MacIver's Claude Code practical report (2026-04):
> "In order to ensure there's enough testing, we set minimum coverage to 100%. I basically think there's no good reason to have untested code in a project with AI working on it."

## Related Concepts

-  — Foundations of testing paradigm
- [[concepts/harness-engineering]] — Agentic PBT as a Claude Code command
- [[concepts/ai-evals]] — 984 bug reports generated, 86% validity rate
-  — Autonomous code quality assurance by AI agents
-  — Bug discovery via invariants
- [[entities/drmaciver]] — Hypothesis author, Antithesis Senior Engineer
- [[concepts/mismanaged-geniuses-hypothesis]] — Python PBT library
-  — Cross-language PBT protocol
## Sources

- [Property-Based Testing with Claude](https://red.anthropic.com/2026/property-based-testing/) — Anthropic Research
- [Agentic PBT Bug Database](https://mmaaz-git.github.io/agentic-pbt-site/) — All bug reports published
- [NeurIPS 2025 DL4C Workshop](https://openreview.net/forum?id=...) — Paper
- [How I've been using Claude Code](http://drmaciver.com/2026/04/how-ive-been-using-claude-code/) — MacIver's practical report
- [Hegel: Universal PBT Protocol](https://antithesis.com/blog/2026/hegel/) — Antithesis
