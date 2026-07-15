---
title: "How to build an AI voice agent with Twilio and ElevenLabs"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/build-voice-agent-twilio-elevenlabs"
scraped: "2026-07-15T06:00:11.252714+00:00"
lastmod: "2026-07-14T17:53:33.479Z"
type: "sitemap"
---

# How to build an AI voice agent with Twilio and ElevenLabs

**Source**: [https://elevenlabs.io/blog/build-voice-agent-twilio-elevenlabs](https://elevenlabs.io/blog/build-voice-agent-twilio-elevenlabs)

Blog
Resources
Build a voice agent in 20 minutes with ElevenLabs and Twilio
Written by
Tadas
Petra
Jack
Limebear
Published
Jul 14, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
On this page
Introduction
How voice agent architecture works
What you need before you start to build a voice agent
Understanding the Twilio Media Streams protocol
Step 1: Serve the TwiML webhook
Step 2: Accept the Media Stream WebSocket
Step 3: Transcribe with Scribe v2 Realtime
Step 4: Generate a reply with an LLM
Step 5: Synthesize with Flash TTS in ulaw_8000
Hardening your AI voice agent for production
Build production-ready voice agents with ElevenAPI
Build a voice agent with Twilio and ElevenLabs FAQ
A voice agent can answer inbound phone calls, transcribe callers in real time with speech to text (STT), generate a response with a large language model (LLM), and speak back with a text to speech (TTS) module. With ElevenLabs and Twilio, you can have a working agent on a real phone number in roughly 20 minutes.
For developers, the full stack you’ll be using is ElevenLabs for speech synthesis (Flash v2.5) and transcription (Scribe v2 Realtime), Twilio for telephony, and either OpenAI or Anthropic as the LLM. That said, all of these are swappable, meaning you can select the components you’re most familiar with and use them instead.
This article shows how to build a voice agent in 20 minutes, using
Node.js
and Typescript. If you want a managed alternative that handles turn-taking, interruptions, and telephony without maintaining the cascade yourself, head to
ElevenAgents.
How voice agent architecture works
Before writing any code, it helps to understand how all three services in your tech stack connect.
Twilio:
Handles the phone call and audio transport.
ElevenLabs:
Handles STT via Scribe v2 Realtime and TTS via Flash v2.5.
LLM:
Handles tool calling and writing the response.
Each stage is a thin adapter, which is why you can swap one out for another service without touching the rest. For example, you could switch the OpenAI LLM with Anthropic without having to rewrite your other components.
A phone call reaches your server through Twilio. Twilio answers the PSTN call, opens a WebSocket back to your server, and forwards the caller's audio as a stream of base64-encoded mu-law frames. Your server runs the cascade and streams synthesized audio back over that same WebSocket, and Twilio plays it to the caller.
Here is the flow that you'll use to build a voice agent:
A caller dials your Twilio number. Twilio fetches a TwiML document from your webhook. The TwiML tells Twilio to open a Media Stream to your WebSocket endpoint. Twilio streams inbound audio as JSON events containing base64 mu-law (ulaw_8000) payloads.
Your server forwards audio chunks to
Scribe v2 Realtime
for streaming transcription. When a caller turn finalizes, you send the transcript to the LLM, then synthesize the reply with
Flash v2.5
in ulaw_8000. You send the synthesized mu-law frames back to Twilio over the WebSocket, base64-encoded, and Twilio plays them to the caller.
Scribe v2 Realtime emits partial transcriptions at roughly 150ms latency, and Flash v2.5 runs at approximately 75ms model inference, excluding network and application latency. The LLM is the largest and least predictable contributor to time-to-first-audio, and it is where most of the latency budget goes. To keep the gap short, we stream the LLM output token by token and start synthesizing before the model has finished its sentence.
For the model tradeoffs behind these choices, see the
models overview
and the explainer on
understanding latency
.
What you need before you start to build a voice agent
The guide assumes you have four things in place. Each is quick to set up, but missing any one of them will block the server from running.
Here are the prerequisites to check:
A Twilio phone number with Voice capability
: Note the number along with your Account SID and Auth Token from the Twilio console.
ElevenLabs API key: Created in your ElevenLabs dashboard. The key travels in the xi-api-key header and is a secret, so keep it server-side only. See API authentication.
LLM API key:
This tutorial treats Anthropic Claude and OpenAI as interchangeable backends, so pick one.
Ngrok (or any tunnel) for local development:
Twilio has to reach your server over a public HTTPS and WSS URL, and ngrok provides that without deploying anything.
Set your secrets as environment variables, and never commit them.
export ELEVENLABS_API_KEY="..."
export ANTHROPIC_API_KEY="..."          # or OPENAI_API_KEY
export TWILIO_AUTH_TOKEN="..."          # used for webhook signature validation
export PUBLIC_HOST="your-subdomain.ngrok.app"
Then start a tunnel pointing at the port your server will use:
ngrok http 8080
Understanding the Twilio Media Streams protocol
Twilio doesn't give you a raw audio socket. Instead, it wraps everything in a structured JSON protocol over WebSocket. Understanding the four event types and the send format means the WebSocket handler in Step 2 will make complete sense before you write it.
Once Twilio connects to your WebSocket, it sends a sequence of JSON text messages, which can have four event types.
The connected event arrives first and confirms the WebSocket is up. The start event is sent once when the media stream begins; it carries a streamSid you must store, as you need it to send audio back, and it also includes call metadata under start.customParameters and start.callSid.
The media event is recurring: media.payload is a base64-encoded chunk of 8kHz mu-law audio, 20ms per frame, and media.track is inbound for caller audio. Finally, stop is sent when the stream ends, typically because the call hung up.
To play audio back, you send a message of type media with the same streamSid and a base64 mu-law payload. To interrupt audio you have already queued, you send a clear message with the streamSid, which flushes Twilio's outbound buffer.
The inbound and outbound encodings are identical (ulaw_8000). We request ulaw_8000 from ElevenLabs Text to Speech and forward the bytes straight to Twilio without resampling anything in between.
Step 1: Serve the TwiML webhook
When a call arrives, Twilio issues an HTTP request to your webhook, and you answer with TwiML that connects the call to your Media Stream. The <Connect><Stream> verb opens a bidirectional WebSocket. Use <Connect> rather than <Start> here: it keeps the call alive for the duration of the stream and lets you send audio back, which is the purpose of this setup.
The TwiML the webhook returns is:
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Connect>
    <Stream url="wss://your-subdomain.ngrok.app/media" />
  </Connect>
</Response>
In Express, that is a single POST handler that fills in the host and returns the document:
// ... imports and app setup
app.post(
"/incoming-call"
, (
_req
,
res
)
=>
{
const
twiml
=
`<?xml version="1.0" encoding="UTF-8"?>
<Response>
<Connect>
<Stream url="wss://${
process
.
env
.
PUBLIC_HOST
}/media" />
</Connect>
</Response>`
;
  res.type(
"application/xml"
).send(twiml);
});
In the Twilio console, set the number's "A call comes in" webhook to
https://your-subdomain.ngrok.app/incoming-call
using HTTP POST.
Step 2: Accept the Media Stream WebSocket
The WebSocket handler reads Twilio events, drives the cascade, and writes audio back.
We hold a small amount of per-call state: the streamSid, an STT connection, and a flag for whether the agent is currently speaking. The handler decodes each inbound media frame from base64 and forwards the raw mu-law bytes to STT:
import
{ WebSocketServer }
from
"ws"
;
// ... http server bound to the same port as Express
const
wss
= new WebSocketServer({ server,
path:
"/media"
});

wss.on(
"connection"
, (
ws
)
=>
{
const
state
= {
streamSid: null
as
string
|
null
,
agentSpeaking: false
};

  ws.on(
"message"
,
async
(
raw
)
=>
{
const
event
=
JSON
.parse(raw.toString());
switch
(event.
event
) {
case
"start"
:
        state.
streamSid
= event.start.
streamSid
;
await
startSttSession(ws, state);
break
;
case
"media"
:
await
forwardToStt(Buffer.from(event.media.
payload
,
"base64"
), state);
break
;
case
"stop"
:
await
teardown(state);
        ws.close();
break
;
    }
  });
});
Step 3: Transcribe with Scribe v2 Realtime
Scribe v2 Realtime accepts streaming audio chunks and returns partial and final transcriptions, and it supports mu-law encoding directly, so we feed it Twilio's frames unchanged.
It also offers Voice Activity Detection for silence-based segmentation and manual commit control to finalize a segment. For a phone agent, VAD-driven segmentation is usually the right choice because a natural pause is the most reliable signal that a caller turn has ended.
Here are the steps: Open an STT stream when the call starts. Push every inbound mu-law chunk. React to finalized transcripts by invoking the LLM.
The realtime STT client surface is still evolving, so the shape below is kept behind a small TypeScript adapter (openRealtimeStt) that you implement against the live API rather than a frozen set of field names. Treat onFinal as the hook that hands a completed caller turn to the next stage.
async function
startSttSession(
ws
,
state
) {
// openRealtimeStt is a thin adapter over the realtime STT API:
// model_id="scribe_v2_realtime", mu-law encoding, 8kHz, VAD on
// so turns finalize on silence.
const
session
=
await
openRealtimeStt({
modelId:
"scribe_v2_realtime"
,
encoding:
"ulaw"
,
sampleRate: 8000
,
  });
  state.
stt
= session;

  session.onFinal(
async
(
text
:
string
)
=>
{
if
(text.trim())
await
handleTurn(ws, state, text);
  });
}
async function
forwardToStt(
audioBytes
,
state
) {
if
(state.
stt
)
await
state.stt.sendAudio(audioBytes);
}
Realtime recognition latency is roughly 150ms for partials, which keeps the perceived gap between the caller finishing and the agent starting small. For the batch counterpart and the full feature set, see the
Speech to Text docs
and the
realtime Speech to Text
product page.
Step 4: Generate a reply with an LLM
This is the stage that produces the response. The LLM takes the conversation history and returns the assistant's text. Stream the response so you can begin synthesis on the first sentence.
Here it’s backed by OpenAI:
// ... client init: new OpenAI({ apiKey: process.env.OPENAI_API_KEY })
const
SYSTEM_PROMPT
=
"You are a concise phone assistant. Keep replies to one or two sentences."
;
async function
llmReply(
history
) {
const
stream
=
await
llm.chat.completions.create({
model:
"gpt-4.1-mini"
,
stream: true
,
messages:
[{
role:
"system"
,
content: SYSTEM_PROMPT
}, ...history],
  });
for await
(
const
part
of stream) {
const
token
= part.
choices
[
0
]?.delta?.
content
;
if
(token)
yield
token;
// incremental tokens
}
}
The model ID above, gpt-4.1-mini, is an example low-latency choice; claude-haiku-4-5 is a comparable option on the Anthropic side. Either provider can back the same llmReply contract; swap the body of the function, and the rest of the agent is unchanged.
The system prompt caps reply length, which matters on the phone: long replies feel slow and are awkward to interrupt naturally.
Step 5: Synthesize with Flash TTS in ulaw_8000
The text now has to become audio Twilio can play. Request Flash v2.5 with outputFormat: "ulaw_8000" so the bytes match Twilio's expected encoding, then stream the audio and forward each chunk back over the WebSocket as a media event.
Accumulate LLM tokens into sentence-sized fragments and synthesize each fragment as it completes, rather than waiting for the whole reply. That shortens time-to-first-audio because the caller hears the first sentence while the model is still producing the second. For deeper control over incremental synthesis, the realtime TTS WebSocket guide shows how to feed text into a single open synthesis socket; the HTTP streaming approach below is simpler and adequate for short conversational turns.
import
{ ElevenLabsClient }
from
"@elevenlabs/elevenlabs-js"
;
const
eleven
= new ElevenLabsClient();
// reads ELEVENLABS_API_KEY
const
VOICE_ID
=
"JBFqnCBsd6RMkjVDRZzb"
;
// George, a default voice
async function
speak(
ws
,
state
,
text
:
string
) {
  state.
agentSpeaking
=
true
;
const
stream
=
await
eleven.textToSpeech.stream(
VOICE_ID
, {
    text,
modelId:
"eleven_flash_v2_5"
,
outputFormat:
"ulaw_8000"
,
  });
for await
(
const
chunk
of stream) {
if
(!state.
agentSpeaking
)
break
;
// interrupted by barge-in
ws.send(
JSON
.stringify({
event:
"media"
,
streamSid:
state.
streamSid
,
media:
{
payload:
Buffer.from(chunk).toString(
"base64"
) },
      })
    );
  }
  state.
agentSpeaking
=
false
;
}
Hardening your AI voice agent for production
After the five steps above, you have a working agent. This is not the same thing as a production deployment.
There are several concerns you need to be aware of before you put the agent on a real phone line.
Validate Twilio webhook signatures
Anyone who learns your webhook URL can POST to it, so the first job is confirming the request actually came from Twilio. Twilio signs every request with your Auth Token in the X-Twilio-Signature header, and you reject anything that fails validation. The signature is computed over the full URL and the POST parameters, so you have to compute it the same way Twilio does.
Twilio's helper does that for you:
import
twilio
from
"twilio"
;

app.post(
"/incoming-call"
, express.urlencoded({
extended: false
}), (
req
,
res
)
=>
{
const
url
=
`https://${
process
.
env
.
PUBLIC_HOST
}/incoming-call`
;
const
valid
= twilio.validateRequest(
    process.env.
TWILIO_AUTH_TOKEN
!,
    req.header(
"X-Twilio-Signature"
) ||
""
,
    url,
    req.
body
);
if
(!valid)
return
res.sendStatus(
403
);
// ... return TwiML as before
});
Manage secrets properly
Keep ELEVENLABS_API_KEY, the LLM key, and TWILIO_AUTH_TOKEN in a secrets manager, not in the source and not in plaintext env files committed to a repo. Scope the ElevenLabs key to only the endpoints this service needs and give it a credit quota so a leak has a bounded blast radius rather than an open-ended one.
Enterprise plans can additionally restrict a key to specific IP ranges with IP whitelisting. This server uses the API key directly because the key never leaves your backend; if any audio logic moved to a browser or mobile client, you would switch to single-use tokens so the key is never exposed client-side.
Understand the concurrency limit
Each plan has a concurrency limit that differs per model family, and the limit counts how many requests are actively generating audio at the same time.
For a phone agent, that accounting works in your favor. Audio generation is faster than playback, so each call only consumes TTS concurrency during the brief windows when a reply is being synthesized, not for the whole length of the call. As a rough heuristic, a concurrency limit of around five can support on the order of 100 simultaneous conversational broadcasts, because generation finishes well before playback does.
Even so, monitor headroom rather than guessing. ElevenLabs responses expose current-concurrent-requests and maximum-concurrent-requests headers; log them and alert as you approach the maximum. When you exceed the limit, requests queue by priority, which typically adds about 50ms, and sustained overload returns HTTP 429.
Handle HTTP 429 responses with a short backoff. If they persist, raise limits by upgrading on the pricing page or, for Enterprise customers, through your account manager.
Handle barge-in and interruptions
A caller who starts talking while the agent is speaking expects the agent to stop. This is barge-in, and handling it correctly is a large part of what makes an agent feel natural rather than scripted.
Detect caller speech during agent playback using the STT VAD signal. When you detect it, do two things. First, stop forwarding TTS chunks, which the agentSpeaking flag in speak already handles by breaking the loop. Second, send Twilio a clear message to flush the audio you have already queued on its side.
function
interrupt(
ws
,
state
) {
  state.
agentSpeaking
=
false
;
  ws.send(
JSON
.stringify({
event:
"clear"
,
streamSid:
state.
streamSid
}));
}
If you skip the clear, Twilio keeps playing buffered audio after you have stopped sending, so the agent appears to talk over the caller.
Log, monitor, and fail gracefully
Instrument each stage so you can attribute latency when a call feels slow. Time the gap from final transcript to first LLM token, from first LLM token to first TTS byte, and from first TTS byte to the frame sent to Twilio. You will find that most of your variable latency sits in the LLM stage; the STT and TTS stages are comparatively stable.
Then plan for partial failure. The LLM can time out, the STT stream can drop, and the network round-trip to ElevenLabs varies from roughly 20 to 200ms over the public internet depending on geography. Co-locate your server near your callers, not only near ElevenLabs, since ElevenLabs already routes to the nearest of its North America, Europe, and Southeast Asia clusters.
When a stage fails, do not leave the caller in silence: synthesize a short fallback line ("Sorry, could you say that again?") and keep the call alive. Wrap each stage in a timeout and a try/catch so one failed turn does not tear down the whole WebSocket.
A few more defaults are worth setting before you ship:
Cap reply length in the system prompt, as shown, so turns stay short and interruptible.
Bound conversation history so long calls do not grow the LLM context without limit.
Set a maximum call duration as a backstop against stuck sessions quietly consuming concurrency.
To keep tuning the pieces you do control, the
latency document
explains where time-to-first-audio comes from, the
models overview
covers the speed and quality tradeoffs, and the
realtime TTS WebSocket guide
shows how to push synthesis latency lower with incremental text input.
Build production-ready voice agents with ElevenAPI
Now that 20 minutes have gone by, you have every layer of a production voice agent. Twilio handles telephony, Scribe v2 Realtime transcribes, an LLM generates replies, and Flash v2.5 speaks back over the same WebSocket.
If you would rather not maintain the cascade yourself, ElevenAgents provides turn-taking, interruption handling, and telephony integration as a managed service built on the same models you just wired together by hand.
To keep tuning a stack you control, explore the
ElevenAPI
product page for plans, concurrency limits, and the voice library. Alternatively,
sign up
and get started today to make your first call.
Build a voice agent with Twilio and ElevenLabs FAQ
How do I build an AI voice agent?
To build an AI voice agent, you’ll first need to connect a telephony layer to a transcription model and add a text to speech API system. The telephony model forwards audio as a WebSocket stream. The server then transcribes with an STT model, sends the transcript to the LLM, and synthesizes a response with a TTS engine.
What is the best Text to Speech API for a voice agent?
For phone agents, Flash v2.5 with ulaw_8000 is one of the leading options to turn to for your TTS API. It offers roughly 75ms model inference, supports 32 languages, and outputs mu-law audio that matches Twilio’s encoding directly.
How do I handle barge-in in a voice agent?
When the STT VAD signal detects caller speech during agent playback, you can set a flag to stop forwarding TTS chunks and also send a clear message to flush your telephony layer’s outbound audio buffer. Both of these work together to handle barge-ins.
How does concurrency work for a phone voice agent?
Each ElevenLabs plan limits how many requests can generate audio simultaneously. For a phone agent, TTS generation finishes well before playback ends, so each call only consumes concurrency during the brief window when a reply is being synthesized. A Flash concurrency limit of around five can support on the order of 100 simultaneous conversational calls.
Can I swap the LLM in a voice agent?
You can swap out the LLM in your voice agent stack using the llmReply function. Swap that function to point at a different provider while keeping the rest of the cascade the same. Remember to keep replies in your LLM capped at one or two sentences, as longer replies may frustrate the caller and lead to multiple interruptions.
