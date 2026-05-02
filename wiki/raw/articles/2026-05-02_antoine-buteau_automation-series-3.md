---
source: https://www.antoinebuteau.com/automation-series-3-ai-automation-when-judgment-language-or-ambiguity-matters/
title: "Automation Series #3: AI Automation: When Judgment, Language, or Ambiguity Matters"
author: Antoine Buteau
date: 2026-05-02
tags: [automation, ai-automation, confidence-scores, structured-output, evaluation-loops]
---

# Automation Series #3: AI Automation

**Core Thesis:** AI should be a **narrow, bounded step** within a larger workflow.

## AI Job Patterns
Classify, Extract, Draft, Summarize, Route, Recommend — each with strict input/output contracts and gates.

## Operationalizing Confidence
Confidence scores must drive specific actions or they are "decorative." High confidence + low risk = auto-proceed. Low confidence = exception queue. High confidence + irreversible action = human approval.

## Evaluation Loops
Gold sets (50-200 examples), sampled review (5-10%), drift checks, and failure taxonomies.

**The Operator's Rule:** "Use AI where ambiguity is the job. Do not use AI to replace state management, permissions, retries, audit logs, policy enforcement, or ownership."
