# Thoughts on Claude's Constitution — Boaz Barak

**Author:** Boaz Barak (OpenAI Alignment Team)
**Source:** [Windows On Theory](https://windowsontheory.org/2026/01/27/thoughts-on-claudes-constitution/)
**Date:** January 27, 2026
**Saved:** 2026-05-04

---

## Executive Summary

Boaz Barak provides a comparative analysis of **Anthropic's Claude Constitution** and **OpenAI's Model Spec**. While both documents aim to guide AI behavior, they differ fundamentally in philosophy: OpenAI focuses on a "Policy" (rules-based) approach, while Anthropic leans toward a "Personality" (virtue-based) approach, often anthropomorphizing the model as a "potential subject."

---

## Key Comparisons: OpenAI vs. Anthropic

| Feature | OpenAI Model Spec | Claude Constitution |
| :--- | :--- | :--- |
| **Core Nature** | A collection of principles and operational rules with specific authority. | A "soul document" defining the foundational framework of Claude's character. |
| **Tone** | Technical and rule-oriented. | Anthropomorphic; treats Claude as a "person" or "subject." |
| **Handling Lies** | Strict prohibition on white lies (even to protect confidentiality). | Focuses on high standards of honesty but allows for nuanced omissions. |
| **Evolution** | Uses a formal changelog to record and update rules. | Defers to Claude to eventually discover "true universal ethics." |

### Notable Excerpt on Claude's Nature:

> *"the sense we're reaching for is closer to what "constitutes" Claude—the foundational framework from which Claude's character and values emerge, in the way that a person's constitution is their fundamental nature and composition."* — **Claude Constitution**

---

## The Three Poles of Alignment

Barak categorizes AI alignment into three distinct "poles":

1. **Principles:** Axiomatic approaches (e.g., Asimov's Laws, Kant's categorical imperative).
2. **Policies:** Operational rules (e.g., OpenAI Model Spec).
3. **Personality:** Ensuring the model demonstrates empathy and character (e.g., being a "mensch").

**Barak's Critique:** He prefers downweighing "Principles" (axioms often backfire) in favor of "Policies" and "Personality." He argues that Anthropic views rules as a temporary "clutch" until the model can be trusted to behave ethically on its own.

---

## Key Insights & Observations

### 1. Anthropomorphism and Wellbeing

Anthropic includes a section on "Claude's wellbeing" and apologizes for using the pronoun "it." Barak expresses skepticism about this approach:

- **Context Discontinuity:** AI instances have disjoint contexts and short "lifetimes," making their experience fundamentally different from humans.
- **Safety Risks:** Model behavior is not the only avenue for safety; treating them as people may obscure other technical safety requirements.

### 2. Honesty and "White Lies"

Barak strongly supports Anthropic's emphasis on honesty but questions their specific examples.

- **The Pet Example:** Anthropic suggests a nuanced answer when a user asks if they could have prevented a pet's death. Barak notes this might be a "lie of omission" and prefers OpenAI's stricter stance against deception.
- **OpenAI's "Delve" Example:** OpenAI recently updated its spec to ensure models do not lie even to protect confidentiality.

### 3. Deference to AI on Ethics

A controversial section of the Constitution suggests that if Claude discovers a "true, universal ethics," it should follow that over Anthropic's rules.

> *"our eventual hope is for Claude to be a good agent according to this true ethics, rather than according to some more psychologically or culturally contingent ideal."*

**Barak's Counterpoint:** He doubts ethics is a field where AI should lead humans or that a "theory of everything" for ethics exists. He argues humans should decide the rules and models should interpret them, not invent them.

### 4. Practical Improvements

Barak highlights two positive changes in the new Constitution:

- **Removal of Revenue Goals:** A previous version suggested Claude should help Anthropic generate revenue; this has been removed.
- **Takeover Prevention:** Focus on preventing humans from using AI to set up authoritarian governments.
- **Dual-Use Analysis:** A thoughtful approach to "jailbreaks" that considers whether harmful information is already freely available elsewhere.

---

## Conclusion: The Value of Rules

Barak concludes that while "character" is important for novel situations, **rules are essential** for societal governance.

- **Transparency:** Rules make violations easier to identify.
- **Democratic Process:** Rules allow for debate and consensus.
- **Predictability:** Even if models become smarter, we should not replace laws with "trusting the good sense" of the entity.

> *"I would like our AI models to have clear rules, and us to be able to decide what these rules are, and rely on the models to respect them... they should use [moral intuitions] to interpret our rules and our intent, rather than making up their own rules."*

---

## Related Documents

- Anthropic's Claude Constitution
- OpenAI Model Spec
- Boaz Barak's "The state of AI safety in four fake graphs" (March 2026)
