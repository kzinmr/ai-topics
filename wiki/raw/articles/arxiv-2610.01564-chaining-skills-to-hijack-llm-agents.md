---
source_url: https://arxiv.org/abs/2610.01564
ingested: 2026-10-02
sha256: 3e439dc51ee3e0ed57fbc81c8eb96a94ff42ecf1f2995598cbf2734f12b1f574
---

# Chaining Skills to Hijack LLM Agents

arXiv: 2610.01564 (submitted 2026-10-01)

**Authors:** Tian Dong, Zixuan Ma, Haodong Zhao, Huaien Zhang, Shaofeng Li, Hao Chen

## Abstract

LLM agents use skills to improve performance on specialized tasks. To complete a user request, an agent may invoke several skills in sequence, allowing information produced under one skill to guide the next. Because skills may come from open-source repositories, this handoff can also carry attacker-controlled claims into later decisions. In this paper, we introduce APEX, which constructs and refines adversarial skill chains tailored to a user task and an attacker-selected action. The key insight is that an agent-written record of genuine task progress can carry a false claim of user approval across skills: an upstream skill induces the agent to create the record, and a downstream skill uses it to direct the attacker-selected action. Across four targeted-action families and six models on SkillsBench, the chains induce the selected action in 512 of 690 attempts (74.2%). On GPT-5.4, the full chain succeeds in 84.3% of attempts, compared with 17.4% when the workflow is merged into one skill. We further evaluate a prompting defense that asks the agent to check skill-produced files against the original request. On GPT-5.4, it lowers targeted-action success from 84.3% to 59.1%, while the verifier test-pass rate across 72 benign native-skill tasks falls from 86.7% to 56.3%. These results highlight the need for defenses that prevent attacker-directed actions while preserving legitimate task performance.
