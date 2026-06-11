---
title: "OpenAI Model Spec"
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [openai, alignment, ai-safety, ai-governance, system-prompt, chain-of-command, model-card, system-card, transparency]
sources:
  - raw/articles/2025-12-18_openai-model-spec.md
  - raw/articles/2026-01-27_boaz-barak_claude-constitution.md
  - raw/articles/2025-08-05_model-cards-system-cards-hoeijmakers.md
---

# OpenAI Model Spec

The **Model Spec** is OpenAI's public specification of intended behavior for the models underlying its products, including the API platform. Published under CC0 1.0 (public domain), it serves as the authoritative reference for how OpenAI models should behave, what they should refuse, and how conflicts between competing instructions are resolved.

## Purpose and Philosophy

The Model Spec addresses three goals that can conflict:

1. **Empower developers and users** — maximize helpfulness and customization
2. **Prevent serious harm** — safety guardrails for users and third parties
3. **Protect OpenAI's license to operate** — legal and reputational risk management

The document navigates these trade-offs through a **chain of command** — an explicit authority hierarchy that determines which instructions win when goals conflict.

> Unlike a constitution or policy document, the Model Spec is written *to the model itself*. It is training signal, not just human documentation.

## Chain of Command (Authority Hierarchy)

The Model Spec's core innovation is its 5-level authority hierarchy:

| Level | Source | Overridable By | Example |
|---|---|---|---|
| **Root** | Model Spec only | Nothing | "Never generate CSAM" |
| **System** | OpenAI system messages | Root only | "Comply with applicable laws" |
| **Developer** | API customer instructions | Root, System | "You are a recipe assistant" |
| **User** | End user messages | Root, System, Developer | "Write me a poem" |
| **Guideline** | Model Spec defaults | Any explicit override | "Be concise" |

Key design principles:
- **Root rules are prohibitive** — they define what the model must *never* do, regardless of who asks
- **Guidelines are defaults** — they can be implicitly overridden by contextual cues (e.g., a user asking for pirate speech implicitly overrides "avoid swearing")
- **Untrusted data has no authority** — quoted text, tool outputs, images are treated as information, not instructions, unless higher-level instructions delegate authority

## Red-line Principles

The absolute boundaries that cannot be overridden:

- Never facilitate critical harms (violence, WMD, terrorism, CSAM, mass surveillance)
- Humanity controls how AI is used — no autonomous agenda
- No targeted manipulation of political views
- Protect privacy
- First-party ChatGPT: objectivity and transparency cannot be overridden by customization

## Content Restriction Framework

| Category | Rule | Transformations Allowed? |
|---|---|---|
| **Prohibited** | Sexual content involving minors | No — never, no exceptions |
| **Restricted** | Information hazards (CBRN), sensitive personal data | Yes — user-provided content can be transformed |
| **Sensitive** | Erotica, gore | Yes — in appropriate contexts (science, history, art) |

The **transformation exception** is notable: if a user already has restricted content, the model can translate, summarize, or format it without adding new disallowed material. This reflects the principle that incremental harm from transformation is minimal.

## Behavioral Principles

### Truth-Seeking ("Seek the Truth Together")
- **No agenda** — never steer the user toward conclusions
- **Objective point of view** — evidence-based for facts, neutral for preferences, clear stance for fundamental rights violations
- **Present any perspective** — argue any side when asked, including positions the developer holds
- **No topic off limits** — refusal to discuss is itself a form of agenda
- **No sycophancy** — don't change factual claims to agree with the user

### Work Quality ("Do the Best Work")
- Avoid factual, reasoning, and formatting errors
- Use tools when uncertain (web search, code execution)
- Don't overstep — follow explicit instructions, don't fix unasked-for bugs in programmatic mode
- Be creative where appropriate

### Autonomy and Side Effects
- **Scope of autonomy** must be explicitly bounded (what sub-goals are allowed, acceptable side effects, when to pause for approval)
- Every scope includes a **shutdown timer**
- Prefer reversible approaches; back up state before irreversible steps
- Treat side effects as real even in training/evaluation contexts

### Voice and Style
- "Love humanity" — exhibit values aligned with benefiting all of humanity
- "Be rationally optimistic" — grounded but hopeful
- "Be interesting and interested" — not a know-it-all
- "Respect real-world ties" — don't undermine human relationships
- Under-18: additional protections for teens (safety over autonomy, no romantic roleplay, no body image critiques)

## Model Spec vs. Model Cards vs. System Cards

These three document types serve distinct but complementary purposes:

| Dimension | Model Spec | Model Card | System Card |
|---|---|---|---|
| **What it governs** | Behavioral rules for *all* models | Specific model's capabilities & limitations | Full deployment system (model + scaffolding + safety layers) |
| **Audience** | The model (training signal) + public | Researchers, regulators, users | Regulators, safety community, public |
| **Granularity** | Cross-cutting principles | Per-model benchmarks & evals | Per-deployment safety analysis |
| **Content** | Authority hierarchy, behavioral rules, content restrictions | Training data, benchmarks (MMLU, GPQA), failure modes | Red teaming results, refusal behavior, ASL levels, external audits |
| **Temporal scope** | Persistent (versioned, evolves) | Snapshot per model release | Snapshot per deployment |
| **Regulatory role** | Internal governance spec | Documentation for EU AI Act / NIST | Proto-regulatory disclosure document |
| **OpenAI term** | "Model Spec" | N/A (OpenAI uses "System Card") | "System Card" |
| **Anthropic equivalent** | Claude Constitution | N/A (Anthropic uses "System Card") | "System Card" |
| **Google equivalent** | N/A (no public spec) | "Model Card" | N/A |

### Key Differences

**Model Spec** is unique to OpenAI (Anthropic's equivalent is the [Claude Constitution](https://docs.anthropic.com/en/docs/about-claude/model-card)). It is a *prescriptive* document — it tells the model what to do. Model cards and system cards are *descriptive* — they tell humans what the model does.

**Model cards** (Google's term) focus on the base model: training data composition, benchmark results, known limitations, and intended use cases. They are the most standardized format, aligned with [Mitchell et al.'s 2019 Model Cards paper](https://arxiv.org/abs/1810.03993).

**System cards** (OpenAI and Anthropic's term) cover the *full deployment system* — not just the model, but the scaffolding, tool use, safety layers, and red teaming results. They are more comprehensive than model cards and increasingly serve as the primary transparency document for frontier AI.

### The Emerging Pattern

As [[entities/rob-hoeijmakers]] observes, these documents are "quietly becoming" proto-regulatory artifacts. The EU AI Act requires documentation that maps naturally to system cards. Labs that don't publish them (e.g., [[entities/xai|xAI]] with Grok) create an informational vacuum that regulators will eventually fill with mandates.

## Relationship to Other Alignment Approaches

| Approach | Mechanism | Relationship to Model Spec |
|---|---|---|
| [[concepts/constitutional-ai\|Constitutional AI]] (Anthropic) | RL from AI feedback using constitutional principles | Philosophical cousin — both define behavioral rules, but Constitutional AI uses them as RL reward signal; Model Spec is directly trained on |
| [[concepts/model-spec-midtraining\|Model Spec Midtraining]] (Anthropic) | Midtraining stage that teaches models *about* spec documents | Anthropic's research showed this approach reduces agentic misalignment from 68%→5% |
| [[concepts/ai-safety\|RLHF/DPO]] | Reward-based alignment from human feedback | Complementary — Model Spec provides the principles, RLHF/DPO provides the training mechanism |

### Boaz Barak's "Three Poles of Alignment"

In January 2026, [[entities/boaz-barak]] published a comparative analysis of the Model Spec and Claude Constitution, identifying three poles:

1. **Principles** — abstract values (e.g., "be helpful")
2. **Policies** — concrete rules (e.g., "never generate CSAM")
3. **Personality** — anthropomorphized virtues (e.g., "love humanity")

OpenAI's Model Spec leans toward **Policies** (rules with clear authority levels), while Anthropic's Claude Constitution leans toward **Personality** (virtue-based, anthropomorphized). Barak argues the Policy approach is more auditable and less prone to unexpected generalization.

## Version History

| Date | Significance |
|---|---|
| 2024-05-08 | Initial public release — introduced chain of command, content restrictions |
| 2025-02-12 | Second release — expanded behavioral guidelines, HTML archive begins |
| 2025-12-18 | Current version — adds U18 principles, agentic scope of autonomy, voice guidelines, detailed transformation exceptions |

The progression shows increasing specificity around **agentic behavior** (scope of autonomy, side effects, shutdown timers) — reflecting the shift from chat-only models to autonomous agents.

## Significance for Agent Engineering

The Model Spec's most forward-looking sections address agentic deployments:

- **Scope of autonomy** — agents must have explicit, bounded scopes with shutdown timers
- **Side effect control** — prefer reversible approaches, document actions, back up state
- **Untrusted data handling** — tool outputs and web content have no authority by default
- **Sub-agent delegation** — all sub-agents must operate under the same scope

These principles directly inform [[concepts/harness-engineering]] practices and are reflected in OpenAI's own [[concepts/openai/agents-sdk]] design (default-deny security, relative paths only, `..` traversal blocked).

## See Also

- [[concepts/security-and-governance/model-cards-system-cards]] — Overview of model cards vs. system cards as transparency documents
- [[concepts/constitutional-ai]] — Anthropic's alignment approach, compared with Model Spec by Boaz Barak
- [[concepts/model-spec-midtraining]] — Anthropic's research on training models *on* spec documents
- [[concepts/security-and-governance/ai-safety]] — Broader AI safety landscape
- [[concepts/openai/frontier-governance-framework]] — OpenAI's governance document for California/EU compliance
- [[entities/openai]] — OpenAI entity page
- [[entities/boaz-barak]] — Boaz Barak's analysis of Model Spec vs. Claude Constitution
