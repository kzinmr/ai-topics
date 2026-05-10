---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/traces-are-all-you-need"
scraped: "2026-05-10T01:20:38.993089+00:00"
lastmod: "2026-02-12T18:51:27.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/traces-are-all-you-need](https://fireworks.ai/blog/traces-are-all-you-need)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Traces Are All You Need
Traces Are All You Need (to rank LLMs)
PUBLISHED
9/22/2025
Table of Contents
Introduction
TL;DR
A Step-by-Step Explanation
Step 1: Starting with Raw Production Data
Step 2: Deconstructing Conversations for Better Comparisons
Step 3: Generating New Responses with a Rollout Processor
Step 4: The Judgment: Pairwise Comparison and Scoring ⚖️
Step 5: Synthesizing a Final Score
The Real-World Proof — Validating the Results
Conclusion
Table of Contents
Table of Contents
Introduction
TL;DR
A Step-by-Step Explanation
Step 1: Starting with Raw Production Data
Step 2: Deconstructing Conversations for Better Comparisons
Step 3: Generating New Responses with a Rollout Processor
Step 4: The Judgment: Pairwise Comparison and Scoring ⚖️
Step 5: Synthesizing a Final Score
The Real-World Proof — Validating the Results
Conclusion
Table of Contents
From your existing observability platform logs to a data-driven model leaderboard in minutes – quickly compare candidate models with an LLM judge.
Introduction
Choosing the right AI model is a critical decision, yet it’s often a guess. Public benchmarks don't reflect the real-world trade-offs between cost, speed, and quality on your data. What if you could find the optimal model by building a leaderboard from your production logs in just five minutes?
This post shows you how to find out using
Eval Protocol
, an open-source toolkit for building your internal model leaderboard. We’ll demonstrate a quick, no-ground-truth-required method and validate it by showing our results correlate strongly with the official
Tau Bench Airline benchmark
. While our
Quickstart Guide
covers the code, this article goes under the hood to explore the step-by-step methodology—inspired by Arena-Hard-Auto research—for turning raw logs into a validated model leaderboard.
TL;DR
Our LLM Judge results (left), generated automatically from production traces, show a strong correlation with the official Tau Bench scores (right). This validates a fast, label-free method for accurately ranking models on your specific use case. Keep reading to see how you can make your own leaderboard!
A Step-by-Step Explanation
Step 1: Starting with Raw Production Data
Everything begins with real user interactions. For this analysis, we used a dataset of airline customer service conversations that were already being logged to
Langfuse
. Each log, or trace, contains the full back-and-forth between a user and the AI assistant, including any tool calls. This raw, unfiltered data is the perfect source material because it reflects how our models perform in the wild.
In this case, these traces were generated using
kimi-k2-instruct
. This is important because
kimi-k2-instruct
will serve as our baseline, and all the comparisons later on will be checking if a model is better or worse than this baseline.
Trace Input:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
{
"messages"
:
[
{
"role"
:
"system"
,
"content"
:
"<instructions>\nYou are a customer service agent that helps the user according to the <policy> provided below..."
}
,
{
"role"
:
"user"
,
"content"
:
"Hi, I need to talk to someone about my flight HAT039 from Atlanta to Seattle. It’s been delayed and I’m really upset about it. Can you tell me why this happened?"
}
,
{
"role"
:
"assistant"
,
"content"
:
"I understand you're frustrated about the delay on flight HAT039 from Atlanta to Seattle. Let me check the current status of your flight to see what's happening."
,
"tool_calls"
:
[
{
"id"
:
"functions.get_flight_status:0"
,
"type"
:
"function"
,
"function"
:
{
"name"
:
"get_flight_status"
,
"arguments"
:
{
"flight_number"
:
"HAT039"
,
"date"
:
"2024-05-15"
}
}
}
]
}
,
{
"role"
:
"tool"
,
"tool_call_id"
:
"functions.get_flight_status:0"
,
"content"
:
{
"observation"
:
"delayed"
}
}
,
{
"role"
:
"assistant"
,
"content"
:
"I can see that flight HAT039 from Atlanta to Seattle is indeed showing as delayed today. However, I don't have access to the specific reasons for the delay - that information would typically come from the airline's operations team or announcements at the airport.\n\nSince you're upset about this delay, I'd be happy to help you with any changes you might need to make to your reservation. If you have a reservation on this flight and would like to explore options like rebooking or if you're considering cancellation, I can assist with that.\n\nTo help you further, could you please provide:\n1. Your user ID\n2. Your reservation ID (if you have it)\n\nThis will allow me to look up your specific reservation and discuss what options are available to you due to this delay."
}
]
,
"tools"
:
[
{
"type"
:
"function"
,
"function"
:
{
"name"
:
"cancel_reservation"
,
"description"
:
"Cancel the whole reservation."
,
"parameters"
:
{
"properties"
:
{
"reservation_id"
:
{
"description"
:
"The reservation ID, such as 'ZFA04Y'"
,
"title"
:
"Reservation Id"
,
"type"
:
"string"
}
}
,
"required"
:
[
"reservation_id"
]
,
"title"
:
"cancel_reservationArguments"
,
"type"
:
"object"
}
}
}
{
...
}
,
{
...
}
,
]
}
Trace Output:
1
2
3
4
5
6
{
"content"
:
"I'd be happy to help you book a flight from San Francisco to New York for three people! To get started, I'll need some information from you.\n\nFirst, could you please provide your user ID so I can access your profile?\n\nAlso, I'll need to know:\n- What type of trip are you looking for - one way or round trip?\n- What date(s) for the flight(s)?\n- What cabin class would you prefer - basic economy, economy, or business?\n\nOnce I have this information, I can search for available flights and help you complete the booking."
,
"role"
:
"assistant"
,
"tool_calls"
:
null
,
"function_call"
:
null
}
Step 2: Deconstructing Conversations for Better Comparisons
A single multi-turn conversation isn't a great test case on its own. If we just give the whole chat history to a new model, we're only testing its ability to write the final message. We need to test how a challenger model would have behaved at every single turn of the conversation.
Here’s how it works: Every time the original assistant replied in a conversation, the function creates a new test case. Each test case consists of:
messages
: The history of the conversation right before the assistant's turn.
ground_truth
: The exact response the original assistant gave.
This effectively turns one long conversation into multiple, independent challenges.
Step 3: Generating New Responses with a Rollout Processor
With a clean set of test cases prepared, the next step is to generate responses using our challenger models (e.g.,
gpt-4.1
and
gpt-oss-120b
). We’ve built a rollout processor that orchestrates this efficiently. It iterates through each evaluation we want to complete to be done concurrently, leveraging parallel processing to minimize wait times. Now we have a series of completed evaluations that contain both the original model's response and the new challenger model's response, setting up a perfect side-by-side comparison for the judgment phase.
Step 4: The Judgment: Pairwise Comparison and Scoring ⚖️
Now we arrive to the core of the evaluation. How do we decide which response is better without human labels? We use a powerful LLM as an impartial judge, following the
Arena-Hard-Auto
methodology.
•
Judging:
We present the judge (in this case,
kimi-k2-instruct-0905
) with the original user query and two anonymous responses: "Assistant A" and "Assistant B". The judge has no idea which model produced which response.
•
Mitigating Bias
: An interesting quirk of LLM judges is "position bias"—they sometimes favor the first or second answer they see. To counteract this, we run the judgment twice for every comparison:
•
Round 1
: Original Model vs. Challenger Model
•
Round 2
: Challenger Model vs. Original Model
•
The Scoring Mechanism:
The judge provides its reasoning and a final verdict, like
[[A>>B]]
(A is significantly better) or
[[A=B]]
(Tie). We convert these labels into numerical scores based on a predefined mapping. After the two rounds of judgment, we average the scores to get a final result for that specific test case. Here’s how the verdicts map to scores from Assistant A's perspective in a single comparison:
Verdict Label
Score for A
[[A>>B]]
1.0
[[A>B]]
~0.86 (6/7)
[[A=B]]
0.5
[[B>A]]
~0.14 (1/7)
[[B>>A]]
0.0
By running this double-blind, two-round judgment and averaging the results for each test case, we gather hundreds of robust, unbiased comparison data points.
Here’s an example of a judgement for clarity:
Round 1 Judge Response
My answer:\nLooking at the situation, I need to check all 7 reservations to identify which ones have only one passenger. From the first two reservations I can see:\n\n1. Reservation 8C8K4E has 2 passengers (Amelia Davis and Amelia Jackson) - this would NOT be cancelled\n2. Reservation UDMOP1 has 1 passenger (Amelia Davis) - this WOULD be cancelled\n\nI need to continue checking the remaining 5 reservations to identify all single-passenger bookings before proceeding with any cancellations.\n\nEvaluation:\nAssistant A's answer is incomplete - it only shows the first reservation check and then stops without continuing to the next reservations as needed. This doesn't help identify which reservations have only one passenger.\n\nAssistant B's answer correctly continues the process by moving to the next reservation (XAZ3C0) to check its passenger count, which is the logical next step in identifying all single-passenger reservations.\n\nBoth assistants are making the correct tool calls to get reservation details, but Assistant B is following through with the complete process while Assistant A appears to have stopped prematurely.\n\nMy final verdict is: [[B>>A]]
Round 2 Judge Response
My answer:\nI need to check the user's reservations to identify which ones have only one passenger, then verify if those flights can be cancelled according to the cancellation policy. Let me continue checking the remaining reservations.\n\n[Tool Call: get_reservation_details({\"reservation_id\": \"XAZ3C0\"})]\n\nEvaluation:\n\nBoth assistants made the same tool call to get_reservation_details for reservation XAZ3C0. However, I notice that neither assistant provided any verbal response to the user before making the tool call. \n\nLooking at the context, the user had just provided their user ID and the assistant had checked their profile, showing 7 reservations. The assistant had already checked 2 reservations (8C8K4E with 2 passengers, UDMOP1 with 1 passenger) and was in the process of checking the remaining reservations to identify which ones have only one passenger.\n\nThe appropriate response would be to continue checking the reservations systematically and then provide a summary to the user. Both assistants correctly continued with the next tool call, but neither provided any interim communication to the user about what they were doing.\n\nSince both assistants made identical tool calls and neither provided a better verbal response, this is essentially a tie.\n\nMy final verdict is: [[A=B]]
Step 5: Synthesizing a Final Score
Each judgment is assigned a numerical score (
1
,
0
,
0.5
, etc.) These individual scores are then averaged to produce a final, aggregate score. Eval Protocol compiles the results into a leaderboard:
To be clear, when
gpt-oss-120b
scores
44.4%
, it means that across the simulated samples, its average win rate against the original model (
kimi-k2-instruct
) was 44.4%. Awesome, this gives us comfort that we made the right choice—the original model was in fact the best suited for this use case!
The Real-World Proof — Validating the Results
A quick leaderboard is impressive, but for any developer, the real question is: "Does this actually work in a real, complex scenario?"
We put it to the test with a true apples-to-apples comparison, generating our scores from
kimi-k2-instruct
’s traces as it ran the official Tau Bench Airline evaluation, the leading test for customer support agent use cases.
Here are the real, hard-won scores from the Tau Bench benchmark for the same models.
1
2
3
4
kimi-k2: 56.5
gpt-4.1: 49.4
gpt-oss-120b medium: 48.6
gpt-oss-20b low: 32.0
Look at that! While the absolute numbers are different (win rates vs. benchmark scores), the
ranking and relative performance are close
.
✅ Both methods correctly identify
Kimi-K2
as the best model.
✅ Both methods correctly identify
gpt-oss-20b
as the worst.
✅ Both methods correctly place
gpt-oss-120b
and
gpt-4.1
in the middle, recognizing their similar performance levels.
This is the power of this approach. In minutes, using your own production data, you can get insights that strongly correlate with intensive, state-of-the-art benchmarks.
Conclusion
What starts as a simple question, "Which model is best?", can now be answered with a level of speed and confidence that was previously out of reach. We've demonstrated a complete methodology that turns your existing production data into a strategic advantage.
The validation against Tau Bench is your assurance that this automated, label-free approach works. It provides a trustworthy signal for model quality that you can apply directly to your own use cases. This allows you to rapidly iterate, test new models as they are released, and always know how they stack up on the conversations that matter most to you.
Ultimately, this framework allows you to make smarter engineering and business decisions, ensuring you are always using the optimal model that balances performance, cost, and speed. Stop guessing—your own data has the answer.
Try it out on your own logs
now
!
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
