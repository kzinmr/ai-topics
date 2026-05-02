---
source: https://www.antoinebuteau.com/automation-series-5-state-idempotency-retries-and-queues/
title: "Automation Series #6: State, Idempotency, Retries, and Queues"
author: Antoine Buteau
date: 2026-05-02
tags: [automation, idempotency, state-management, queues, retries]
---

# Automation Series #6: State, Idempotency, Retries, and Queues

**Core Thesis:** While AI handles "intelligence," unglamorous backend components prevent failures, duplicates, and data corruption.

## Key Concepts
1. **Durable State:** Workflows must remember progress in durable storage, not chat transcripts.
2. **Idempotency:** Same operation multiple times = same effect as once. Use idempotency keys.
3. **Retries:** Only for temporary failures (timeouts, rate limits). Never retry logical failures.
4. **Queues:** Absorb bursts, manage rate limits, dead-letter storage.

## State Transition Flow
RECEIVED -> VALIDATED -> MODEL_REQUESTED -> MODEL_COMPLETED -> GATE_DECIDED -> ACTION_COMPLETED (+ human review and exception paths)

**The Operator's Rule:** "If you cannot answer 'What happens if this runs twice?' you are not ready to launch. If you cannot answer 'Where is this item in the workflow?' you are not ready to scale."
