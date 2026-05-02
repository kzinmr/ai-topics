---
source: https://www.antoinebuteau.com/aautomation-is-not-one-thing/
title: "Automation Series #1: Automation Is Not One Thing"
author: Antoine Buteau
date: 2026-05-02
tags: [automation, workflow-design, deterministic, probabilistic, accountable]
---

# Automation Series #1: Automation Is Not One Thing

**Core Thesis:** The fastest way to build bad automation is to treat it as a single category. Effective automation architecture requires separating workflows into deterministic, probabilistic, and accountable components.

## The Fundamental Shift in Questioning
Most teams ask the wrong question: "Can we automate this?" This is too vague to be useful.

**The Better Question:** "Which parts of this workflow should be deterministic, which parts can be probabilistic, and where do we need human judgment?"

## The Three Kinds of Work
1. **Deterministic Work:** Same input always produces same output. Tools: Code, rules, schemas, APIs, tests.
2. **Probabilistic Work:** Messy inputs with ambiguity. Tools: AI/LLMs.
3. **Accountable Work:** High-consequence decisions requiring ownership. Tools: Human gates or strict control models.

## The Automation Classification Matrix
Separates Exact rule, Data movement, Text classification, Information extraction, Drafting, Recommendation, and Irreversible action by owner (Code/Model/Human), AI usage, and controls.

## The Operator's Rule
Before launching, ask: What must be deterministic? Where does ambiguity exist? What is reversible? Where do we need a human gate? Who owns it after launch?
"A human approval queue is not a failure of automation. It is often the part that makes automation safe enough to use."
