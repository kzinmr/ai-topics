---
title: "Latency optimization"
url: "https://developers.openai.com/api/docs/guides/latency-optimization"
fetched_at: 2026-11-14T10:02:24.536897+00:00
source: "OpenAI Developers Blog"
tags: [blog, raw]
---

# Latency optimization

Source: https://developers.openai.com/api/docs/guides/latency-optimization

Measure where users wait before changing the model or prompt.
Time to first token (TTFT)
measures how long an API request takes to start returning content. For streaming text in the Responses API, time the request from when you send it until you receive the first nonempty
response.output_text.delta
.
End-to-end latency
measures how long the user waits for the complete result. Time it from the user’s action through retrieval, model and tool calls, retries, and rendering.
Compare the median (p50) and the 95th percentile (p95) on representative traffic. Group similar requests by model, service tier, and task. Record input, cached input, and output tokens alongside the timings. If TTFT looks good but users still see a blank screen, time the work before the model call and check when the client displays the first text.
Process tokens faster.
Generate fewer tokens.
Use fewer input tokens.
Make fewer requests.
Parallelize.
Make your users wait less.
Don’t default to an LLM.
Choose a model using examples from your workload. For a focused task like routing a support ticket, try
gpt-6-luna
. For more demanding work, use the
model selection guide
to choose a comparison model. Keep the fastest configuration that meets your quality target, including on difficult cases.
If you need to keep the same model, compare Standard processing with
Fast mode
or
Ultrafast mode
where supported. Both charge a premium. Compare the same prompts and output lengths, and record the
service_tier
returned in each response.
For long answers, measure visible output speed in tokens per second. Count the text tokens received after the first text event and divide by the time from the first text event to the last. A streamed event can contain multiple tokens. A tokens-per-minute rate limit measures how much traffic you can send across requests.
For Chat Completions on a supported model,
Predicted Outputs
can reduce generation time when you already know most of the answer, such as when editing a few lines in a file. Check model and parameter compatibility before using this option.
If an answer starts quickly but takes too long to finish, inspect what the model generates.
Visible text.
Ask for the amount of detail the user needs, such as “Give the next step in one sentence.” On supported Responses API models, lower
text.verbosity
for shorter answers.
Reasoning.
For routine extraction or classification, try a lower supported
reasoning.effort
. Compare accuracy and time to first text on the same examples. Check
usage.output_tokens_details.reasoning_tokens
to see how much reasoning the model used.
Structured output.
Request only the fields your application consumes. Compute values you already know, such as a message count, in application code. Use
Structured Outputs
when the response must follow a schema.
In the Responses API,
max_output_tokens
caps both reasoning and visible output tokens. A low cap can leave the response
incomplete
, even before it produces visible text. Use the cap as a budget and check response status before consuming a partial answer.
A long prompt can delay the first token, especially when much of the input is new. Filter search results for relevance, strip markup you don’t need, and send only the context required to answer accurately.
For repeated inputs, put stable instructions, examples, and tool definitions first. In multi-turn conversations,
keep the prefix unchanged
and append new messages and tool results.
Prompt caching
can reuse an eligible exact prefix match. In the Responses API, inspect
usage.input_tokens_details.cached_tokens
and compare TTFT for requests with and without cache hits.
Each sequential model or tool call adds another wait. Combine steps when one request has all the information it needs. For example, a model can turn a customer’s follow-up into a standalone search query and decide whether a lookup is necessary in the same response. A reply that depends on a lookup still needs its result.
If your agent makes many short, sequential tool calls, try
WebSocket mode
. Reuse the connection and continue from the prior response with
previous_response_id
, sending only new input items and tool results. This reduces overhead between turns.
Run independent work concurrently. For example, once you have an order ID, you can look up its shipment status while fetching the return policy. An answer that needs both can start as soon as the slower lookup finishes. On supported models,
async tool calling
also lets the model continue independent work while your application runs a tool.
For a likely but uncertain branch, consider starting a read-only lookup early and discarding it if it’s unnecessary. Measure the extra cost on a wrong guess. Wait for required checks before displaying a result or taking an action such as issuing a refund.
For interactive text over HTTP,
stream the response
with
stream: true
and display text as it arrives. Streaming lets the user start reading before generation finishes. Time to the first visible text still depends on the request, including any reasoning or tool work before the answer.
If you check or moderate output before displaying it, buffer enough text to perform that check. For longer tasks, show actual progress, such as “Looking up your order,” while the lookup runs. When the user can return later,
Background mode
lets your application submit the work and retrieve the result asynchronously.
Use application code when you already know the answer. Render an order status from the order API, use a template to confirm a refund that succeeded, or show search results directly. Each of these can remove a model call from the user’s wait.
A customer asks, “Is it still eligible for a return?” after discussing a pair of headphones. The support assistant makes three model calls in sequence. The first rewrites the question with the product name. The second decides whether to search. After retrieval, the third generates a reply plus internal fields for message count, sentiment, and tone. The customer sees nothing until the final call finishes.
Step
Change
What to measure
Route the question
Ask one model to decide whether to search and, if so, produce the standalone query. For this turn, the query is “headphones return policy.” An acknowledgment can skip retrieval.
Routing accuracy on both kinds of turns and time until retrieval starts.
Fetch the evidence
Once the router identifies a return question, fetch the policy and the customer’s order details concurrently if both inputs are available.
Elapsed time until both results are ready.
Answer
Give the model the policy and order details, request only the customer-facing reply, and stream the text. If the policy or order lacks a fact needed to decide eligibility, ask for it.
Time to first visible text, time to the complete reply, and whether the eligibility decision is correct.
On the return-question path, this removes one of three sequential model calls and overlaps two independent lookups. Replay the same support conversations before and after each change. Include ambiguous follow-ups and cases that need no lookup so a faster answer still sends customers to the right place.
