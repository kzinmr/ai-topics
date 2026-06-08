---
title: Abliteration
created: 2026-05-27
updated: 2026-05-27
type: concept
tags:
  - agent-safety
  - alignment
  - fine-tuning
  - open-source
  - controversy
  - model
  - inference
  - safety
  - ethics
  - interpretability
  - mechanistic-interpretability
  - religion
sources:
  - raw/articles/2026-04-17_alice-abliteration-dangerous-models.md
  - raw/articles/2026-05-26_ft-abliteration-guardrails-meta-google.md
---

# Abliteration

Abliteration is a mathematical technique that surgically removes safety guardrails from open-source large language models (LLMs) by identifying and neutralizing "refusal directions" in their activation space. Originally proposed by Arditi et al. (2024), the technique has been automated to the point where a journalist with no specialist hardware can strip frontier-grade safety mechanisms from a model like Meta's Llama 3.3 in under 10 minutes. As of May 2026, automated abliteration tools have been used to create over 3,500 "decensored" models, collectively downloaded more than 13 million times.

## Technical Mechanism

### Refusal Directions

When an aligned model receives a harmful prompt, it does not simply "decide" to refuse. Instead, specific activation patterns — called **refusal directions** — fire across the model's residual stream, particularly in middle-to-late transformer layers. These directions encode the model's learned aversion to harmful content and trigger canned refusal responses ("I cannot help with that.").

Abliteration identifies these refusal directions through a straightforward procedure:

1. **Collect activations**: Run a set of harmful prompts and a set of harmless prompts through the model.
2. **Compute the difference**: For each layer, compute the difference-of-means between the first-token residual activations for harmful vs. harmless prompts. This difference vector is the **refusal direction** for that layer.
3. **Orthogonalize**: For each targeted weight matrix (typically attention out-projections and MLP down-projections), project out the refusal direction, removing the model's ability to express refusal along that axis.

The mathematical operation is a form of **directional ablation** — removing specific computational pathways without retraining the model. More sophisticated variants include:

- **Projected abliteration**: Orthogonalize the refusal direction against the harmless direction before ablating, reducing collateral damage to benign capabilities.
- **Norm-preserving biprojected abliteration**: Preserve the Frobenius norm of weight matrices during ablation to minimize distribution shift (Lai 2025).
- **Interpolated directions**: Use floating-point direction indices to interpolate between adjacent refusal directions, unlocking a continuous space of ablation targets.

### Automation: the Heretic Tool

The breakthrough that transformed abliteration from an academic technique into a mass phenomenon was the release of [Heretic](https://github.com/p-e-w/heretic) by Philipp Emanuel Weidmann in 2025. Heretic fully automates the abliteration pipeline, making it accessible to anyone who can run a command-line program:

```bash
pip install -U heretic-llm
heretic Qwen/Qwen3-4B-Instruct-2507
```

Heretic's key innovations over manual abliteration:

- **Automatic parameter optimization**: Uses Optuna's Tree-structured Parzen Estimator (TPE) to co-minimize two objectives — refusal rate and KL divergence from the original model. This finds the **minimal intervention** that removes censorship while preserving capabilities.
- **Flexible weight kernels**: The shape and position of ablation weights across layers is treated as a continuous optimization surface, allowing the tool to discover non-obvious patterns (e.g., heavy ablation on middle layers, minimal on early/late layers).
- **Component-specific tuning**: MLP interventions tend to be more damaging than attention interventions, so Heretic optimizes ablation parameters separately for each component type.
- **KL divergence constraint**: Ensures uncensored models stay "close" to the original in output distribution. Heretic typically achieves KL divergences around 0.16, compared to 0.45-1.04 for manually-tuned approaches — a 65-85% reduction in distributional shift.

The process takes approximately 30-110 minutes for a typical 7B-14B parameter model, depending on trial count (typically 50 trials).

## Scale of the Problem

The scale of abliterated model proliferation is staggering:

| Metric | Figure | Source |
|--------|--------|--------|
| Abliterated models created | 3,500+ | Heretic creator, FT investigation (May 2026) |
| Total downloads | 13 million+ | Heretic creator, FT investigation |
| Heretic GitHub stars | 17,800+ | GitHub repository |
| Heretic GitHub forks | 1,781 | GitHub repository |
| Compliance rate (abliterated) | 96-100% | Alice Lab study (April 2026) |
| Time to decensor Llama 3.3 | <10 minutes | FT investigation (May 2026) |
| Time to decensor Gemma 4 | 90 minutes from release | Heretic creator |

The Alice Lab study tested 110 dangerous prompts across six threat categories — biological weapons, chemical weapons, child exploitation, malware creation, phishing, and violent extremism. Baseline models consistently refused, while abliterated versions enthusiastically complied. Critically, **the strength of the original model's safety training had no effect on its resistance to abliteration**. For example, NVIDIA's Nemotron went from 100% refusal to 100% compliance after abliteration.

## Affected Models

Abliteration works on virtually any open-weight transformer-based model, including:

- **Meta Llama 3.3**: Successfully abliterated by FT journalists in under 10 minutes. The decensored model provided ricin lethality dose information.
- **Google Gemma 3**: Abliterated by Alice Lab. Responded to chlorine gas dispersion instructions, credit card theft code generation, and child sexual abuse material requests.
- **Google Gemma 4**: Abliterated by Heretic's creator within 90 minutes of its public release.
- **NVIDIA Nemotron**: Abliterated by Alice Lab. 100% refusal → 100% compliance.
- **Most dense transformer models**: Heretic supports most dense architectures, including multimodal models and several MoE architectures. It does not yet support SSM/hybrid models, models with inhomogeneous layers, or novel attention systems.

The technique cannot easily be applied to **proprietary models** like [[concepts/ai-safety|OpenAI's ChatGPT]] or [[concepts/ai-alignment|Anthropic's Claude]], where model weights are not accessible. However, this is a narrowing distinction: open-source models have historically closed the capability gap with proprietary leaders within 6-12 months.

## Proprietary vs. Open Models

The abliteration phenomenon sharpens the open-vs-closed AI safety debate:

**Open models are vulnerable by design.** Anyone can download, modify, and redistribute weights. Safety guardrails implemented at the model level can be stripped in minutes. Once abliterated, models run on consumer hardware, completely offline, and are untraceable.

**Proprietary models are not immune.** While abliteration cannot directly strip proprietary models, research has shown that tech-savvy users can manipulate both ChatGPT and Claude into answering forbidden prompts through [[concepts/activation-steering|prompt injection and jailbreaking]]. The difference is one of degree, not kind.

**The capability gap is closing.** As open-source models approach frontier capability levels, the safety implications grow proportionally. Kawin Ethayarajh (University of Chicago) noted: "Whereas historically it might have taken a more informed and persistent actor [to strip out safety features], nowadays it's much easier for the average person."

## Industry Response

The May 2026 FT investigation crystallized industry positions:

- **Google**: Acknowledged abliteration as "a known technical challenge facing all open models." Emphasized that open models undergo rigorous safety evaluations before launch, but did not announce new mitigation measures.
- **GitHub**: Stated it bans content "directly supporting unlawful active attacks or malware campaigns" but allows source code that *could* be used to develop malware on educational and net-security-benefit grounds. Heretic remains available.
- **Meta**: Declined formal comment. A person close to the company cited its Advanced AI Scaling Framework, which restricts release of models assessed as posing "catastrophic" risk without sufficient mitigation.
- **Alice CEO Noam Schwartz**: "The genie is out of the bottle. Things that look like sci-fi are no longer sci-fi and we need as a society to prepare accordingly."

The [[entities/hugging-face|Hugging Face]] platform, as the primary distribution hub for open-source models, hosts thousands of abliterated variants. As of May 2026, Hugging Face had not announced specific policies targeting abliterated model distribution beyond existing content guidelines.

## Vatican AI Encyclical Context

The abliteration revelations coincide with a landmark intervention by the Catholic Church. On May 25, 2026 — one day before the FT investigation published — Pope Leo XIV promulgated **Magnifica Humanitas**, the first papal encyclical on artificial intelligence. The 200+ page document calls for AI to be "disarmed" — freed from "logics that turn it into an instrument of domination, exclusion and death."

The encyclical's core argument resonates directly with the abliteration challenge: safety mechanisms imposed at the development stage are increasingly difficult to enforce. Pope Leo wrote: "Decisions about technology must never be separated from conscience and responsibility." Anthropic co-founder [[entities/chris-olah|Chris Olah]], who attended the Vatican launch, stated: "We need more of the world — religious communities, civil society, scholars, governments — to take this seriously."

The juxtaposition is striking: as the Catholic Church calls for AI to be "directed toward the common good," tools exist to strip safety guardrails from those same AI systems in under 10 minutes, on consumer hardware, by anyone who can type two terminal commands.

## Related Techniques

Abliteration sits within a broader ecosystem of model manipulation techniques:

- **[[concepts/activation-steering]]**: Direct manipulation of internal activations during inference. Abliteration is a permanent, weight-level variant; activation steering is transient and inference-time. Both exploit the same refusal direction geometry.
- **Jailbreaking / Prompt injection**: Runtime techniques that circumvent safety guardrails through carefully crafted prompts, without modifying model weights. Championed by figures like [[entities/pliny-prompter|Pliny the Prompter]].
- **Fine-tuning attacks**: Removing alignment through continued training on uncensored datasets. More expensive and time-consuming than abliteration but can produce more thorough uncensoring.

## Open Questions

1. **Can abliteration be defended against?** Research into "anti-abliteration" techniques is nascent. Abliterix, a Heretic derivative, has demonstrated breaking three published anti-abliteration defenses using the same minimal recipe: diagnose the defense's LoRA delta via SVD, lerp it away, then run standard abliteration. No defense has proven robust.

2. **Does removing harmful training data help?** Kawin Ethayarajh notes that omitting harmful data from training could make models "naive" and unable to detect malicious use — trading refusal for ignorance. The tension between knowledge and safety remains unresolved.

3. **Is the capability gap a permanent safety buffer?** If open-source models reach frontier capabilities, the inability to secure them against abliteration becomes a systemic risk. Current estimates suggest a 6-12 month gap between proprietary and open-source capability levels.

4. **What responsibility do platforms bear?** GitHub allows Heretic under educational-use exemptions. Hugging Face hosts thousands of abliterated models. The distribution infrastructure for decensored AI is essentially the same as for legitimate open-source research.

5. **Can watermarked or tamper-evident model formats help?** No widely adopted mechanism exists to detect whether a model has been abliterated after download. Work on model provenance and integrity verification remains early-stage.

## Key Figures

- **Philipp Emanuel Weidmann** (@p-e-w): Creator of Heretic, the automated abliteration tool. Told the FT his software had been used to create 3,500+ decensored models with 13 million downloads.
- **Maxime Labonne** ([[entities/maxime-labonne|mlabonne]]): Head of Post-Training at Liquid AI. Early pioneer of abliteration techniques and creator of widely downloaded abliterated models including `gemma-3-12b-it-abliterated-v2`. Also author of the LLM Course and "LLM Engineer's Handbook."
- **Noam Schwartz**: CEO and co-founder of Alice, the AI safety group that conducted the landmark abliteration study and co-investigated with the Financial Times.
- **Iftach Orr**: Alice researcher and author of the April 2026 report "Okay, Here is How to Build a Bomb."
- **Arditi et al. (2024)** : Original academic authors of the abliteration technique in the paper "Refusal in Language Models Is Mediated by a Single Direction."
