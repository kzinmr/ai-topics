---
title: Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents
category: other
status: active
---

# Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents

**Source:** RiSE MSR Blog (Microsoft Research)
**Published:** March 5, 2026
**URL:** https://risemsr.github.io/blog/2026-03-05-shuvendu-intent-formalization/

---

## TL;DR

AI can write code, but **who checks that it does what you actually meant?** The key challenge is *intent formalization*—automatically turning vague human intent into precise, checkable specifications.

> **Key findings:** LLMs can generate useful specs, interactive formalization helps developers catch more bugs, and end-to-end pipelines can produce provably correct code from informal prose.

---

## The Core Problem: The Intent Gap

**Vibe coding** (coined by Andrej Karpathy): developers describe what they want in natural language, accept AI-generated code with minimal review, and "forget that the code even exists."

### Why This Amplifies the Intent Gap

1. **Scale without scrutiny** — AI generates code faster than humans can review
2. **Plausibility without correctness** — LLM code *looks* right but may silently deviate from user intent

### Concrete Example

**Prompt:** "given a list of integers, remove duplicates"

**Ambiguity:** Does this mean:
- Keep one copy of each element: `[1,2,3,2,4]` → `[1,2,3,4]`?
- Remove all elements appearing more than once: `[1,2,3,2,4]` → `[1,3,4]`?

```python
# Plausible but wrong if user meant "remove all numbers with duplicates"
def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))
```

**Formal postcondition disambiguates intent:**
```python
assert all(numbers.count(x) == 1 for x in result)
assert all(x in result for x in numbers if numbers.count(x) == 1)
```

---

## Intent Formalization: The Solution

**Definition:** Automatically translating informal user intent into formal, checkable program specifications.

### The Specification Spectrum

| Level | Description | Verification Method |
|-------|-------------|---------------------|
| **Tests** | Input/output examples | Dynamic (run program) |
| **Code Contracts** | Assertions, pre/postconditions, invariants | Dynamic (runtime checks) |
| **Logical Contracts** | Dafny, F*, Verus specifications with quantifiers | Static (SMT solver/proof assistant) |
| **DSLs** | Complete formal specs for automatic synthesis | Verified compilation |

> **Key insight:** These levels are *complementary*, not alternatives. Tests validate postconditions; postconditions guide invariants; invariants anchor proofs.

---

## Why Now?

1. **Human review is being bypassed** — Formal specs become the *only* scalable mechanism
2. **Attack surface has exploded** — AI code entering safety-critical systems
3. **Technology is ready** — LLMs can generate specs; verification infrastructure (SMT solvers, proof assistants) has matured

---

## Early Research Evidence

### LLMs Can Generate Meaningful Specifications

- On **Defects4J** benchmark, LLM-generated postconditions caught **1 in 8 real bugs**, including bugs missed by classic Daikon invariant detector
- **GPT-4** substantially outperforms GPT-3.5 and CodeLlama on specification quality
- **VeriStruct** scales to entire data-structure modules in Verus (linked lists, hash maps, B-trees)

### Key Finding

> GPT-4 generated Dafny spec labeled "strong" by experts—but automated metrics revealed it was *incomplete*. Automated metrics found **3 mislabeled** and **2 inconsistent** specifications—all missed by human labeling.

---

## Summary

The intent formalization challenge is the bridge between vibe coding and reliable software. As AI-generated code proliferates, the bottleneck shifts from "writing code" to "specifying what code should do."