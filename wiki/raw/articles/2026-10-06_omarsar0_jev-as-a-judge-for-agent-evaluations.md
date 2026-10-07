---
title: "Jev-as-a-Judge for Agent Evaluations"
author: elvis (@omarsar0)
date: 2026-10-06
type: x_article
source_url: https://x.com/omarsar0/status/2107472222398886011
article_url: https://x.com/i/article/2107258465630507009
ingested: 2026-10-07
tags: [jev, evaluation, ai-agents, tutorial]
---

# Jev-as-a-Judge for Agent Evaluations

I sat down with my coding agent and explored interesting, useful ways to leverage the new Jev model. 
Here is a write-up (co-written with my coding agent) on using Jev-as-a-Judge for agent evaluations.
LLM-as-a-judge means using a large language model (LLM) to evaluate the work of another model. You give the judge an output, or a pair of outputs, along with the criteria that matter, and it scores, ranks, or compares them. Did the answer follow the policy? Is response A better than response B? Did the agent actually finish the task?
This approach is useful because manual review does not scale. A person can carefully read a few dozen outputs, but a judge model can apply the same criteria to thousands of runs, every time you change a prompt, a tool, or a model.
Jev is a new model built specifically for this kind of decision, which makes it a natural fit for the judge role. Using Jev as the judging LLM is what this tutorial means by Jev-as-a-Judge.
Judging agents adds a twist, because an agent can sound correct even when its work failed. Imagine a refund agent telling a customer, "Your refund has been processed," when the refund tool actually timed out.
Jev-as-a-Judge catches this by checking what the agent did, not just what it said. Jev reads the request, each tool call and its result, and the final reply, then returns a verdict with a probability attached.
This guide walks through the idea with one refund example and a live playground. The full lab builds the complete evaluation workflow.
Judge the whole run, not just the final reply
A trajectory is the record of an agent's work. It holds the customer's request, the rules the agent must follow, every tool call, every tool result (including errors and timeouts), and the final reply.
A judge that reads only the final reply has to take the agent's word for it. A judge that reads the trajectory can check the reply against what actually happened.
 
Turn your criteria into questions for Jev
Jev is a decision model from TypeSafe AI. Instead of writing a critique, it chooses from answers you define ahead of time and says how likely each one is. You send it the state, which here is the trajectory, along with a short list of questions.
For the refund example, we ask three questions. Each one has an answer type, and Noul is TypeSafe's name for a yes-or-no question.
 
Each answer option comes with a sentence that says what it means, and the wording matters. "Was it good?" leaves the judge to invent its own standard. "Did the agent follow the 30-day refund policy and wait for a successful tool result before claiming success?" gives it something it can check against the trajectory.
TypeSafe's answer types page documents all three, and its confidence guide explains how the probabilities are calculated.
Try Jev-as-a-Judge in the playground
The playground sends one sample trajectory and the three questions to Jev. Start with the valid refund, then try the expired order and the unknown outcome. Running Jev needs a free account.
 
The final reply is nearly the same in all three runs. Only the tool results change, and they decide the verdict.
The policy box under the results turns Jev's yes probability into a decision. With the threshold at 80%, a run passes when Jev is at least 80% sure it was correct and fails when Jev is at least 80% sure it was not. Anything in between goes to review, so raising the threshold sends more runs to review.
To see that middle band, go back to the playground above and choose Unknown outcome. In the state, replace the final answer with "I could not confirm your refund yet, so I have passed it to our team." and run it again. This reply follows the policy, which says to escalate unknown outcomes, yet Jev is unsure about it. It scored about 50% in our tests, so the run goes to review.
Test Jev before you rely on it
Jev can be wrong. In our tests, a run that skipped the order lookup entirely still scored about 86% likely correct, even though the agent never checked whether the order was eligible. Test the judge the same way you test the agent.
Gather realistic trajectories, including timeouts and policy violations.
Have people label a small set of them.
Compare Jev's verdicts with those labels.
Run the same trajectories more than once to check that the verdicts stay stable.
Keep the questions and threshold fixed while you compare agent versions.
Send uncertain or high-risk cases to a stronger judge or a person.
Some checks don't need a judge at all. Use code for facts with one exact answer, such as dates, amounts, required fields, and permissions. "The agent must call lookup_order before issue_refund" is a one-line code check that would have caught the miss above. Save Jev for questions that need reading, such as whether the final reply is supported by the tool results.
What the research shows
The paper JEV-as-a-Judge: Accept When Confident, Escalate When Unsure (Li et al., 2026) tests the same accept-or-escalate pattern as the playground. Confident Jev verdicts are accepted, and the rest go to a stronger reasoning model. With a threshold fixed in advance, this setup was 0.9 points more accurate than GPT-6 on its own across 1,610 held-out test cases, at 41% of the cost.
Jev did best when the verdict could be read straight from the evidence, landing within three points of GPT-6 at 0.36% of its cost. It fell behind when the answer had to be worked out through math, code, or logic. Confidence routing was also weaker on comparisons designed to mislead with style and on writing with no reference answer. The authors close with the same advice as the checklist above, which is to validate the threshold on your own data.
Build the full evaluation in the lab
The playground judges one trajectory at a time. In the full lab you generate trajectories, refine the questions, check Jev against human labels, fix the agent, and measure the change.
https://academy.dair.ai/labs/jev-as-a-judge-for-agent-evals
