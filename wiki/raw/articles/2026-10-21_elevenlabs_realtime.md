---
title: "Introducing Eleven Realtime: a simpler way to build natural voice agents"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/realtime"
scraped: "2026-10-21T06:01:01.071194+00:00"
lastmod: "2026-10-20T14:23:56.096Z"
type: "sitemap"
---

# Introducing Eleven Realtime: a simpler way to build natural voice agents

**Source**: [https://elevenlabs.io/blog/realtime](https://elevenlabs.io/blog/realtime)

Blog
Product
Introducing Eleven Realtime: a simpler way to build natural voice agents
Written by
Min
Kim
Published
Oct 20, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
On this page
Introduction
Why we built realtime models
How they perform
Get started
Building a voice agent that sounds natural today requires a lot of decisions. You have to make choices on individual components like speech recognition, voice activity detection, turn-taking, the underlying LLM, and text to speech. Building this stack is a project in itself, and getting all the components to work well together takes more testing and tuning.
Eleven Realtime
is a new class of Speech to Speech models that removes those hurdles. Each model is a complete voice agent, optimized for separate use cases. Both support more than 90 languages and can use any of the 17,000+ voices in the ElevenLabs library:
Today, we’re launching:
Eleven Realtime v1 Mini
for natural conversations at low cost. This is the best choice for AI assistants, teachers, and interactive characters, and will be sufficient for most use cases.
Eleven Realtime v1 Max
for complex tasks. This is ideal for customer support, lead qualification, and multi-step workflows, where the agent has to follow a process and reason through steps.
Why we built realtime models
You shouldn’t have to become a configuration expert to build a voice agent that sounds natural. Getting an agent to feel and sound right is about small judgment calls that require nuance such as how long to wait after a pause before answering, how to recover when the user interrupts the agent, and how voice, prompts, and a model all work together. In ElevenAgents, these are all settings you can adjust.
The same goes for developers already on a realtime API. Ours is compatible with OpenAI’s Realtime API, so trying Eleven Realtime simply means changing the endpoint and model name in the code you might already have.
How they perform
Artificial Analysis evaluated both models independently across three public benchmarks: Big Bench Audio for speech reasoning, Full-Duplex-Bench for conversational dynamics, and the Speech Agent Arena for human preference and task success.
Speech reasoning
Big Bench Audio asks 1,000 reasoning questions by voice and scores the spoken answer. Realtime v1 Max answered 98.8% questions correctly, and v1 Mini answered 75.9% correctly.
Speed
Big Bench Audio asks 1,000 reasoning questions by voice and scores the spoken answer. V1 Max starts speaking in 0.57 seconds on average, and v1 Mini in 0.62 seconds.
The Pareto frontier for accuracy and speed
Accuracy and speed are usually seen as a trade-off. The models that score highest on Big Bench Audio take the longest to answer, and the fastest ones give up a lot of accuracy. v1 Max excels in both of these metrics.
Conversational dynamics and human preferences
On Full-Duplex-Bench, which tests pauses, turn-taking, interruptions, and backchannels, v1 Mini scores 95.8% and v1 Max 94.1%. In the Speech Agent Arena, where people compare two models in blind live conversations, v1 Max scored 998 and v1 Mini 988. On tool-use tasks, v1 Max completed 87.1% and v1 Mini 60.3%, which is why we recommend Max for use cases with heavy tool calling.
Get started
In ElevenAgents (recommended)
Create an agent, or open an existing one, and select a Realtime model from the dropdown. From there you have everything ElevenAgents provides for running agents in production deployment. That includes phone, web, WhatsApp, and CCaaS channels, workflows, a knowledge base, guardrails, testing, and monitoring.
Check out the
ElevenAgents docs
for more details.
Through the Realtime API
If you already have an integration with OpenAI's Realtime API, the fastest way to try Eleven Realtime is to keep your code and change where it points. The Realtime API connects over WebSocket and follows the OpenAI Realtime specs, so OpenAI's SDK works as is.
import
{ OpenAIRealtimeWebSocket, RealtimeAgent, RealtimeSession }
from
"@openai/agents-realtime"
;
const
{
value
:
clientSecret
} =
await
fetch(
"/api/token"
).then((
res
)
=>
res.json());
const
agent
= new RealtimeAgent({
name:
"ElevenLabs agent"
,
instructions:
"You are a helpful, friendly voice assistant. Keep replies concise."
,
});
const
transport
= new OpenAIRealtimeWebSocket({
url:
"wss://api.elevenlabs.io/v1/convai/realtime"
,
});
const
session
= new RealtimeSession(agent, {
  transport,
model:
"eleven_realtime_v1_mini"
,
config:
{
outputModalities:
[
"audio"
],
audio:
{
output:
{
voice:
"brian"
} },
  },
});
await
session.connect({
apiKey:
clientSecret });
The Realtime API connects over WebSocket only, so a WebRTC integration needs to move to WebSocket first. It also runs separately from ElevenAgents, so if you need channels, a knowledge base, or other platform features, build on ElevenAgents from the start.
The
migration guide
covers the steps and the differences from OpenAI's API.
Written by
Min Kim
View profile
