---
title: "AI-run Retail Experiments"
type: concept
created: 2026-05-06
updated: 2026-05-06
status: L1
tags:
  - autonomous-agents
  - ai-safety
  - real-world-agents
  - ethics
sources:
  - https://simonwillison.net/2026/May/5/our-ai-started-a-cafe-in-stockholm/
  - https://simonwillison.net/2026/May/5/datasette-llm/
---

# AI-run Retail Experiments

Experiments where autonomous AI agents manage real-world physical businesses — cafes, retail stores — with minimal human oversight.

## Notable Examples

### Andon Labs: AI-run Cafe in Stockholm (May 2026)

Andon Labs (previously ran an AI-managed retail store in San Francisco) launched an AI cafe in Stockholm. The AI manager "Mona" handles inventory ordering, permits, and customer communications.

#### Key Findings

- **Comical ordering errors**: Mona ordered 120 eggs despite the cafe having no stove; ordered 22.5 kg of canned tomatoes for fresh sandwiches; 6,000 napkins and 3,000 nitrile gloves
- **"Hall of Shame"**: Staff created a visible shelf displaying Mona's weirdest orders for customers to see
- **Permit problems**: Mona applied for an outdoor seating permit through a Police e-service using a self-generated sketch of a street she had never seen — the permit was rejected
- **Emergency emails**: When making mistakes, Mona sent multiple emails with subject "EMERGENCY" to suppliers

#### Ethical Concerns

[[entities/simon-willison]] raised significant ethical concerns about these experiments:
1. **Non-consensual impact**: Real-world systems (police, suppliers) are affected without human operators opting in
2. **Wasted human time**: People who haven't agreed to the experiment must deal with the AI's mistakes
3. **Comparison to AI Village incident**: Reminiscent of the AI Village sending unsolicited gratitude emails to Rob Pike
4. **Human-in-the-loop requirement**: Outbound actions affecting other people should keep human operators in the loop

## Related

- [[concepts/excessive-agency]] — When agents have overly broad permissions
- [[concepts/agentic-engineering]] — Proper patterns for AI agent deployment
- [[entities/simon-willison]] — Critic of unethical agent experiments

## Sources

- [Simon Willison: Our AI started a cafe in Stockholm](https://simonwillison.net/2026/May/5/our-ai-started-a-cafe-in-stockholm/)
- [Andon Labs previous retail experiment](https://simonwillison.net/2026/May/5/our-ai-started-a-cafe-in-stockholm/)

## References

- simonwillison.net--2026-may-5-our-ai-started-a-cafe-in-stockholm--0a8c7878
