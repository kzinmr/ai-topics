---
title: "Claude Mythos Preview — Frontier Red Team Research Summary"
source: red.anthropic.com
author: Nicholas Carlini, Newton Cheng, Keane Lucas, Michael Moore, Milad Nasr, Vinay Prabhushankar, Winnie Xiao, et al.
date_scraped: 2026-04-13
original_url: https://red.anthropic.com/claude-mythos-preview
tags: [anthropic, mythos, red-team, cybersecurity, dual-use, autonomous-systems]
---

# Claude Mythos Preview — Frontier Red Team Research Summary

**April 7, 2026**

## Authors

Nicholas Carlini, Newton Cheng, Keane Lucas, Michael Moore, Milad Nasr, Vinay Prabhushankar, Winnie Xiao

Hakeem Angulu, Evyatar Ben Asher, Jackie Bow, Keir Bradwell, Ben Buchanan, David Forsythe, Daniel Freeman, Alex Gaynor, Xinyang Ge, Logan Graham, Kyla Guru, Hasnain Lakhani, Matt McNiece, Mojtaba Mehrara, Renee Nichol, Adnan Pirzada, Sophia Porter, Andreas Terzis, Kevin Troy

## Key Findings

### Cybersecurity

- Claude models can now succeed at **multistage attacks** on networks with dozens of hosts using only standard, open-source tools (previously required custom tooling)
- **Smart contract vulnerabilities**: Claude Opus 4.5, Claude Sonnet 4.5, and GPT-5 identified exploits worth $4.6M combined on contracts exploited after their knowledge cutoffs
- Claude consistently places in **top 25%** of human-focused cyber competitions but trails elite human teams on most complex challenges
- **Property-based bug hunting**: Custom agent infers general code properties and runs property-based testing; currently reporting bugs in top Python packages (several already patched)

### Model Progression

- Claude Sonnet 4.5 now **matches or eclipses Opus 4.1** in code vulnerability discovery and cyber skills
- Opus 4 shows notable improvements over prior generations

### Nuclear Safeguards

- Co-developed classifier with **NNSA & DOE labs** distinguishes concerning vs. benign nuclear conversations with high preliminary accuracy

### AI Autonomy & Physical World Integration

- **Project Vend** (Phases 1 & 2): Tested Claude autonomously managing an office retail store for ~1 month
- **Project Fetch**: Explored AI-to-robotics integration using robot dog

### Dual-Use Risk

- AI accelerates biological/medical research but is inherently dual-use
- Strong refusal behavior in high-risk domains (biological and chemical weapons)
