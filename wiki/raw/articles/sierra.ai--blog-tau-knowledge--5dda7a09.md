---
title: "𝜏-knowledge: benchmarking agents on realistic knowledge"
url: "https://sierra.ai/blog/tau-knowledge"
fetched_at: 2026-05-14T07:00:38.210128+00:00
source: "Sierra Blog"
tags: [blog, raw]
---

# 𝜏-knowledge: benchmarking agents on realistic knowledge

Source: https://sierra.ai/blog/tau-knowledge

Customer-facing agents are only as good as their ability to find and apply the right information. In practice, that means navigating large, messy, and constantly evolving knowledge bases like policy manuals, product catalogs, procedural guides, and internal tool descriptions.
Despite how common this is in real-world settings, existing benchmarks don't capture this complexity well. They test an agent's ability to find information, or take action, but rarely both at once.
𝜏-knowledge fills this gap — evaluating agents on their ability to search a realistic knowledge base, reason over what they find, and execute multi-step tool calls, all while handling a live user conversation.
Introducing 𝜏-knowledge
𝜏-knowledge extends Sierra's conversational benchmark 𝜏-bench with a new domain: 𝜏-Banking, a fintech-inspired customer support setting built around a realistic knowledge base of 698 documents across 21 product categories (~195K tokens). Coverage spans personal and business checking accounts, tiered savings, rewards credit cards, buy-now-pay-later plans, and more. Documents detail not only customer-facing product specs — APY rates, fees, cashback structures — but also internal agent protocols: dispute procedures, card replacement workflows, retention offers, and identity verification.
Tasks require agents to search these documents, reason over what they find, and execute multi-step tool calls. Each task requires information from an average of 18.6 documents and an average of 9.5 tool calls, with some requiring up to 33. The walkthrough below condenses one such task to its key turns. The agent must handle two requests — a transaction dispute and a credit-limit increase — which requires it to: (1) retrieve two policies from the knowledge base; (2) recognize that these policies interact and that order matters; (3) discover and chain multiple procedures that live only within the knowledge base; and (4) refuse a later user claim that contradicts policy. Skipping or misordering any of these results in a wrong final database state.
How the 𝜏-Knowledge frontier has shifted
When we first released 𝜏-knowledge in early March 2026, the picture was sobering: the best frontier model — GPT-5.2 with high reasoning — passed just 25.5% of tasks on the first try (Pass^1), and only 9.3% reliably (Pass^4). Even when we removed the retrieval challenge entirely by handing the agent the relevant documents directly, the ceiling sat at ~40% Pass^1. By comparison, frontier models routinely break 80% Pass^1 on existing 𝜏-Bench domains like airline, retail, and telecom. Retrieval-aware knowledge work was a real gap.
In the months since, we've evaluated 11 frontier model variants at maximum reasoning effort under a standardized retrieval setting — giving each model access to BM25, dense embeddings, and a freeform shell, and letting it pick its own search strategy. The frontier has moved meaningfully.
GPT-5.5 with xhigh reasoning leads the leaderboard today at 37.4% Pass^1 — up 11.9 percentage points from the launch best, with Pass^4 more than doubling from 9.3% to 20.6%. But 𝜏-knowledge is still nowhere near saturated: even the leading model fails roughly 60% of these tasks at maximum reasoning effort.
What separates the strong agents from the rest
Parsing through thousands of agent trajectories across models reveals behavioral patterns that distinguish the strongest agents:
Strong models treat retrieval as ongoing, not a one-time step.
The weakest agents treat retrieval as a one-shot upfront step: search at the start of the task, then operate on whatever came back. The strongest agents continuously search the knowledge base whenever the conversation introduces new context — recognizing that a customer's mid-task pivot ("actually, this is a medical emergency") may unlock a new internal procedure the agent didn't know to look for at turn one. For example, when customers became increasingly frustrated, GPT-5.5 would issue a follow-up search to identify the right escalation protocol; weaker models would commit to the original strategy and stop searching.
Strong models search smarter, not harder.
Within the GPT family, 5.5 issues fewer search queries than 5.2 (19.4 → 9.1 searches per task) while Pass^1 climbed 12 percentage points. The improvement isn't volume — it's targeting. GPT-5.5 issues surgical queries like "transfer reason codes customer frustrated demands human medical emergency" that surface the right internal doc on the first try; older models spray related-but-imprecise queries until something hits.
Strong models know when to act — and when not to.
Many models fall into the trap of executing the expected actions correctly, then adding ostensibly helpful extras without user permission (e.g., filing a fraud dispute alongside an expected card-replacement order). Strong agents recognize the expected action set and stop. Opus 4.7's tighter calibration helps on this axis compared to 4.6's more eager behavior.
Open evaluation to progress the frontier
As agents are increasingly deployed into knowledge-heavy workflows, evaluations need to reflect the same conditions they face in practice. 𝜏-Banking remains far from solved, with ~63 percentage points of Pass^1 headroom still remaining. The behavioral patterns above point to the specific calibration problems models need to solve next.
We invite model providers and agent developers to use 𝜏-knowledge as a measure of where agents actually stand on knowledge-grounded tasks by evaluating their models on 𝜏-Banking. The benchmark is open, the tasks are verifiable, and the gap between current performance and reliable deployment is clear.
Leaderboard
Code & tasks
Paper
