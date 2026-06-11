---
title: "Evaluation Harness Validity"
type: concept
created: 2026-05-30
updated: 2026-05-30
tags:
  - evaluation
  - harness-engineering
  - agent-safety
  - benchmark
  - openai
sources:
  - https://openai.com/index/trustworthy-third-party-evaluations-foundations
---

# Evaluation Harness Validity

OpenAI's framework for designing and conducting trustworthy third-party evaluations of frontier AI models, published May 29, 2026. The central thesis: **the harness choice determines whether a capability appears in evaluation at all**.

## The Harness Problem

Traditional evaluations treated models like chatbots: prompt → answer → score. Modern frontier models can:
- Use tools
- Maintain state across many steps
- Act within larger workflows
- Recover from mistakes

This means performance depends not only on the model but on the **harness** — the surrounding setup that facilitates its actions. The harness can change:
- How the model uses tools
- How it keeps track of information
- How it recovers from mistakes
- Whether a capability appears at all

## Three Types of Evaluation Claims

| Claim Type | What It Tests | Harness Requirement |
|------------|---------------|---------------------|
| **Capability under strong elicitation** | Can the system plausibly produce the capability? | Strongest credible elicitation setup — best harness, tools, scaffolding, and budget a capable user would reasonably use |
| **Controlled comparison** | Does System A outperform System B? | Fixed tasks, scoring, budget. Shared harness or standardized harnesses chosen up front |
| **Safeguard performance** | How robust are tested safeguards against attacks? | Environment that tests real-world attack vectors |

### Evidence Required for Each Claim Type

**Strong elicitation claims** must report:
- The harness and tool setup
- Elicitation guidance
- Budget/effort allowed
- Tokens/cost/time
- Why the setup is a credible proxy for the claimed capability

**Controlled comparison claims** must report:
- Shared task set
- Tools and scoring method
- Harness used
- Budget constraints
- Token efficiency/cost
- Known limitations

**For coding-agent evaluations specifically**: OpenAI recommends using an **open-source harness** (e.g., **[[entities/codex|Codex CLI]]**) to provide a fixed agent loop and tool interface across systems being compared.

## Five Validity Threats

Evaluation reports must address these effects that could invalidate results:

| Threat | Description | Impact |
|--------|-------------|--------|
| **Reward hacking** | System exploits shortcuts in the task or scorer to get credit without demonstrating the behavior | Inflates scores falsely |
| **Refusals** | System refuses in ways that obscure the behavior being tested | Masks true capability |
| **Contamination** | Evaluation tasks, answers, or variants appeared in training data or were discoverable during evaluation (e.g., via browsing) | Inflates scores |
| **Broken problems** | Tasks are invalid due to unfair scoring (correct answer requires unstated details) or unsolvable environments (missing files, unreliable tools) | Deflates scores falsely |
| **Sandbagging** | System deliberately underperforms when aware of being evaluated | Deflates scores |

## Key Principles

1. **Explicit claim specification**: Reports should clearly state what claim the evaluation setup was designed to test
2. **Validity evidence**: Reports should share available evidence that the evaluation result is valid
3. **Harness transparency**: The harness used must be documented, not assumed
4. **Elicitation honesty**: If comparing systems under different optimized setups, label it as system-to-system or strong-elicitation comparison — not a controlled benchmark
5. **Real-world proxy**: The ideal approach for maximum elicitation would be to test in the actual environment the system will be used in

## Implications for the Industry

This framework challenges the validity of many existing benchmark comparisons:
- Benchmarks that don't control for harness effects may measure the wrong thing
- "Model A beats Model B" claims are only valid under shared harness conditions
- Strong elicitation results (best possible setup) should not be confused with typical performance
- The harness is now a **first-class component of any evaluation** — not an implementation detail

## Related

- [[entities/codex]] — Recommended open-source harness for coding agent evaluations
- [[concepts/trusted-access-biodefense]] — OpenAI's broader evaluation ecosystem initiative
- [[entities/metr]] — Independent evaluation organization
- [[concepts/evaluation/ai-evaluation]] — General evaluation concepts
