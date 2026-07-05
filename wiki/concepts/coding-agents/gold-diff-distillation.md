---
title: Gold Diff Distillation
type: concept
created: 2026-04-16
updated: 2026-04-16
tags:
  - concept
  - training
  - reinforcement-learning
  - coding-agents
related:
- model-distillation
- trl-fine-tuning
- ai-coding-reliability
- evaluation-flywheel
sources: []
---

# Gold Diff Distillation

A new RL training method developed by a coding-product company. It uses the user's final "desired state" as the RL target.

## Core Concept

While traditional model distillation directly imitates the teacher model's output, Gold Diff Distillation:

- Treats the **user's final converged state** as the ground truth
- Penalizes intermediate outputs the user rejected or edited
- Uses the "truly useful output" reached after 10+ API turns as the learning target

## Mechanism

```
User Request → Model Output v1 → User Edit/Reject → Model Output v2 → ... → Final Accepted State
                                                                        ↑
                                                        This is the "Gold Diff" (correct differential)
```

### RL Target Setting
- **Reward**: Generating outputs close to what the user ultimately accepted
- **Penalty**: Patterns in intermediate outputs the user rejected or edited
- **Advantage**: Directly reflects actual human preferences

## Strategic Implications

### Distillation Preventability
According to Dwarkesh Patel's analysis:
1. **Chain-of-Thought hiding fails**: Models can omit or externalize thinking via prompts
2. **RLVR can reconstruct CoT**: Even hidden, it can be reconstructed as a training target
3. **The real moat is tool use**: Locally executed code/bash tool use is hard to conceal

### Gold Diff's Advantage
Distilled models have the **potential to surpass** the original API model:
- Learning from actual user workflows
- Leveraging "negative samples" from intermediate trial-and-error
- Exclusively available product usage data as a data source

## Economic Context

- Frontier model distillation cost: ~$25M (1T tokens @ Opus 4.6's $25/MTok)
- Coding-product companies have the ROI to justify this cost
- They hold a "moat" of user behavior data that competitors cannot access

## Sources

- [Dwarkesh Patel: What I learned this week](https://www.dwarkesh.com/p/what-i-learned-april-15)
- AI Index Report 2026 (coding agent adoption data)

## See Also

- [[entities/_index]]
- [[concepts/local-llm/model-distillation]]
