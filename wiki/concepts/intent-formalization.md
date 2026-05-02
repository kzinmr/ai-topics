---
title: "Intent Formalization for AI Agents"
type: concept
created: 2026-04-21
updated: 2026-04-21
tags:
  - concept
  - safety
  - formal-methods
  - model
  - reliability
  - prompting
aliases: ["intent-specification", "program-specification-llm", "formal-spec-llm"]
sources:
 - path: raw/articles/crawl-2026-04-21-shuvendu-intent-formalization.md
 - path: raw/articles/crawl-2026-04-21-kleppmann-formal-verification-ai.md
status: active
---

# Intent Formalization for AI Agents

**Intent formalization** is the challenge of automatically translating vague human intent into precise, checkable program specifications. It is the central unsolved problem for reliable AI-generated code—and the bridge between vibe coding and verified software.

## The Intent Gap Problem

**Vibe coding** (coined by Andrej Karpathy): developers describe what they want in natural language, accept AI-generated code with minimal review, and "forget that the code even exists."

### Why This Amplifies the Intent Gap

1. **Scale without scrutiny** — AI generates code faster than humans can review
2. **Plausibility without correctness** — LLM code *looks* right but may silently deviate from user intent

### Concrete Example

**Prompt:** "given a list of integers, remove duplicates"

**Ambiguity:** Does this mean:
- Keep one copy: `[1,2,3,2,4]` → `[1,2,3,4]`
- Remove all elements appearing more than once: `[1,2,3,2,4]` → `[1,3,4]`

```python
# Plausible but wrong if user meant "remove all numbers with duplicates"
def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))
```

**Formal postcondition disambiguates intent:**
```python
# Keep one copy
assert all(numbers.count(x) == 1 for x in result)
# OR remove all duplicates
assert all(x in result for x in numbers if numbers.count(x) == 1)
```

## The Specification Spectrum

Intent formalization is not all-or-nothing. It occupies a spectrum from tests to complete formal specs:

| Level | Description | Verification Method |
|-------|-------------|---------------------|
| **Tests** | Input/output examples | Dynamic (run program) |
| **Code Contracts** | Assertions, pre/postconditions, invariants | Dynamic (runtime checks) |
| **Logical Contracts** | Dafny, F*, Verus specifications with quantifiers | Static (SMT solver/proof assistant) |
| **DSLs** | Complete formal specs for automatic synthesis | Verified compilation |

> These levels are *complementary*, not alternatives. Tests validate postconditions; postconditions guide invariants; invariants anchor proofs.

## Research Evidence

### LLMs Can Generate Meaningful Specifications

- On **Defects4J** benchmark (hundreds of real Java bugs), LLM-generated postconditions caught **1 in 8 real bugs**, including bugs missed by classic Daikon invariant detector
- **GPT-4** substantially outperforms GPT-3.5 and CodeLlama on specification quality
- **VeriStruct** scales to entire data-structure modules in Verus (linked lists, hash maps, B-trees)
- **ClassInvGen** synthesizes class invariants for C++ data structures—outperforms both direct LLM prompting and Daikon

### Key Finding

GPT-4 generated Dafny spec labeled "strong" by expert reviewers—but automated evaluation metrics revealed it was *incomplete*. Automated metrics found **3 mislabeled** and **2 inconsistent** specifications—all missed by human labeling.

**Auto-Verus** uses automated metrics to filter LLM-generated specs/proofs, achieving **3.6× higher proof accuracy** than GPT-4o zero-shot.

## Why Now?

1. **Human review is being bypassed** — Formal specs become the *only* scalable mechanism for AI-generated code
2. **Attack surface has exploded** — AI code entering safety-critical systems
3. **Technology is ready** — LLMs can generate specs; verification infrastructure (SMT solvers, proof assistants) has matured

## The Hard Part: Writing Correct Specifications

The bottleneck shifts from "proving" to "defining what to prove." The arc of difficulty moves:
- Before AI: Proving was the hard part
- After AI: Writing the spec is the hard part; proving becomes automated

> *"Writing the spec is vastly easier and quicker than writing the proof by hand, so this is progress."* — Martin Kleppmann

## Related Concepts

- [[concepts/formal-methods]] — Foundational formal methods practice and theory
- [[concepts/neurosymbolic-ai]] — Symbolic reasoning (formal methods) combined with neural approaches
- [[concepts/ai-safety]] — Alignment, oversight, and interpretability for AI agents
- [[concepts/agent-sandboxing]] — Isolation for untrusted AI-generated code
- [[concepts/test-case-minimization]] — Binary search on entropy for automatic test case reduction
- [[hillel-wayne]] — Formal methods practitioner bridging academic verification and real-world software engineering
- [[john-d-cook-applied-mathematics-consulting]] — Formal verification in high-stakes engineering contexts