---
source_url: https://arxiv.org/abs/2610.05399
ingested: 2026-10-06
sha256: 512cb0c632ef887fe140efa76696f307f19da8b760318c9f9be2d1e50be8b97a
---

# Adaptive Code Revision Attacks on AI Pull Request Reviewers

arXiv:2610.05399 | Published 2026-10-04

**Authors:** Jingzhi Gong, Jie M. Zhang, Gunel Jahangirova, Meng Wang

## Abstract

Pull-request review protects software before new code reaches users, helping prevent vulnerabilities that could expose users to attacks. AI agents increasingly perform these reviews and explain which problems need fixing. However, for an attacker submitting vulnerable code, this feedback also reveals what changes may secure approval. Existing PR attacks seek such approval through persuasive text and comments while keeping executable code fixed. This leaves unclear whether an attacker can use the feedback to repair the reported problem while preserving a vulnerability in the revised code. We therefore conduct an empirical study of this threat using AFCRA (Adaptive Feedback-guided Code Revision Attack). To distinguish successful attacks from genuine repairs, we construct AFCRA-Bench from 159 disclosed vulnerabilities, with executable exploits to verify vulnerabilities in code. Across five-round interactions with Sonnet 5 and GPT-5.5 reviewers, AFCRA reaches success rates 2.5x and 12.5x those of the strongest evaluated text- or comment-based attack. Case studies of these successes show how reviewers accept repairs of reported problems while overlooking surviving vulnerabilities. These findings establish feedback-guided code revision as a threat to automated PR review. To address this threat, we derive actionable implications for researchers, AI providers, PR reviewers, and PR authors on securing AI-assisted development.
