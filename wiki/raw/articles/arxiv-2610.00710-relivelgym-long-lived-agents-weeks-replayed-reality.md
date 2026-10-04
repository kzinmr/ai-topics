---
source_url: https://arxiv.org/abs/2610.00710
ingested: 2026-10-04
sha256: 717df81c435b36170b28755bf8f723198f1d8e152bdd5f1423517f757cfb5eae
---

# ReLiveGym: Evaluating Long-Lived Agents over Weeks of Replayed Reality

Authors: Xisen Jin, Jingheng Li, Zhenglun Chen, Junyi Du, Xiang Ren.
arXiv:2610.00710, submitted 2026-09-30.
Code: https://github.com/SaharaLabsAI/ReLiveGym

## Abstract
As large language model (LLM) agents become widely adopted, they are increasingly deployed for tasks that require persistent monitoring or recurring actions (e.g., market analysis). These agents are expected to operate unattended for days or weeks, act at the right timing, and adapt to the dynamic environment over time. These challenges are not fully captured in the existing long-horizon agent work, as they often consider a static environment that is not temporally changing. We introduce ReLiveGym, a diagnostic evaluation environment of long-lived tasks in which agents act sparsely over simulated weeks of chronologically replayed real-world news, market, and social-media streams. The tasks span diverse levels of time sensitivity, reasoning intensity, and recurrence. Across eight base language models, we investigate how model choice and harness design affect agent performance on such long-lived tasks. Our results show that how agents determine when to act arises as an important harness-design axis for long-lived tasks; and that the optimal design varies across tasks and sometimes model choices as well. We also evaluate how continuous learning from hindsight feedback affects performance and addresses failure modes observed in these long-lived tasks. These findings indicate model choice, action timing mechanism, and use of feedback as important considerations in the design of long-lived agents.
