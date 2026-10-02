---
source_url: https://arxiv.org/abs/2610.01306
ingested: 2026-10-02
sha256: ef9c05b4b786496e00e0bb73a3f60e3b0fcb26cb5d59f65d4fc990e1c1c0bfd0
---

# DAYJOB: A Benchmark for Long-Horizon Professional Work

arXiv: 2610.01306 (submitted 2026-10-01)

**Authors:** Stephanie Finley, Liudas Panavas, Thomas Mikkelson, Cam Hinton, Stacey Ganss, Bradley Monton, Emily Kendall, Michelle Spradlin, Lydia Bye, Michael O'Brien, Lauren Ylvisaker, Derek Ray, Suhaas Garre, Sushant Mehta, Edwin Chen

## Abstract

Professional work often starts with a brief request that leaves the professional to work out what is needed, which documents matter, and whether the request's premise holds. We introduce DAYJOB, a benchmark of 130 tasks built by professionals in healthcare (50) and finance (80). The tasks are estimated to take a professional 13.6 hours on average in healthcare and 16.6 in finance. Each task is a containerized Harbor environment with an expert rubric of binary criteria (median 47.5 and 57.5 per task) that an agentic judge applies to the delivered files, and an attempt passes only if it meets every criterion. Across 30 model configurations from 13 developers, the strongest, Claude Opus 5.5, passes 24.7% of healthcare and 23.9% of finance attempts, and the median configuration passes 0.6% and 2.5%. In case studies, agents accept premises that the record contradicts and carry wrong inputs through otherwise consistent analyses. We release all healthcare tasks, 50 of the 80 finance tasks, the evaluation harness, and the leaderboard.
