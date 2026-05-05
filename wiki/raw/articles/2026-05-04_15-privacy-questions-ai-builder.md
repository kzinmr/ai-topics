---
title: "15 Privacy Questions Every AI Builder is Asking"
date: 2026-05-04
author: Hugo Bowne-Anderson, Katharine Jarmul
source: https://open.substack.com/pub/hugobowne/p/15-privacy-questions-every-ai-builder
type: newsletter
---

# 15 Privacy Questions Every AI Builder is Asking

**Authors:** Hugo Bowne-Anderson, Katharine Jarmul | **Date:** May 4, 2026

## Key Insights

### Privacy as Engineering Discipline
- Privacy is subjective: legal (GDPR/HIPAA), social/cultural, and technical dimensions
- Goal: translate norms into mathematical/architectural implementation

### The Agent Harness Vulnerability
- **System prompts are public by default** — treat them as if published on your website
- **Context leakage**: RAG database contents can be deduced from model output variations
- **Memory exposure**: All information fed to an agent harness should be treated as potentially exposed

### Three-Layer Guardrail Framework
1. **External Deterministic**: Fast regex/hash-based filters (copyright blocks, PII stripping)
2. **External Algorithmic**: Secondary classifier models (Llama Guard)
3. **Internal Alignment**: RLHF to refuse dangerous requests natively

### Tools & Approaches
- **Microsoft Presidio**: Open-source NLP for PII redaction
- **Privacy Routing**: API gateway routes sensitive queries to local open-weight models
- **Federated Learning + Differential Privacy**: For keeping raw data localized

### Actionable Advice
- Assume users will share "deep, dark secrets" with AI — build retention policies
- Privacy is grayscale: every step toward data minimization is a win
- Designate privacy champions rather than relying on collective responsibility
