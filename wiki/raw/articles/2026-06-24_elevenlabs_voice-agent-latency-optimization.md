---
title: "Voice agent latency optimization: Techniques and methods"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/voice-agent-latency-optimization"
scraped: "2026-06-24T06:00:51.878824+00:00"
lastmod: "2026-06-23T17:00:04.790Z"
type: "sitemap"
---

# Voice agent latency optimization: Techniques and methods

**Source**: [https://elevenlabs.io/blog/voice-agent-latency-optimization](https://elevenlabs.io/blog/voice-agent-latency-optimization)

Blog
Resources
Voice agent latency optimization: Step-by-step guide
Written by
Tadas
Petra
Jack
Limebear
Published
Jun 23, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Contact sales
Learn more
On this page
Introduction
TL;DR
Defining the voice agent latency budget
Speech to Text: transcription and endpointing latency optimization
The LLM latency contribution
Text to Speech: streaming and voice choice
Streaming chunk size choices
Codec choices
Geography and network distances
Measuring voice agent latency yourself
What reduces voice agent latency the most?
Build low-latency voice agents with ElevenAgents
FAQs about voice agent latency optimization
The responsiveness of a voice agent is determined by the total delay between when a user finishes speaking and when the agent begins to reply. That delay is rarely caused by a single slow component. It accumulates across several independent stages, each contributing a few tens or hundreds of milliseconds, and reducing it requires knowing how much each stage spends.
Voice agent latency optimization is the work of finding where that time hides and recovering it stage by stage.
This article acts as a companion to the
conceptual latency overview
. Where that page explains what latency is, this one covers architecture and measurement, so you’ll leave with a latency budget you can measure against and a set of concrete actions to take.
TL;DR
Time-to-first-audio represents the whole pipeline, not a single model’s inference time.
The LLM’s time-to-first-token and endpointing are the two largest line items.
Overlapping stages, rather than running them in series, recovers most of the budget.
Streaming, codec choice, and player buffer tuning each shave measurable milliseconds.
You should measure per region against your own deployment, reporting P50 and P95.
Defining the voice agent latency budget
A latency budget is a total time-to-first audio target decided across the pipeline stages, with each stage given an allowance that has to sum under your target. Defining it is the first step and is also where latency work most often goes wrong, as engineers may conflate two numbers that look similar but mean different things.
The first is model inference latency: the time a model spends generating output. For our
Flash models
this is approximately 75ms for typical short inputs, excluding network and application overhead. It is an internal figure, and it is useful for comparing one model against another. It is not the number your user experiences.
From a user’s perspective, you’ll focus on time-to-first-audio (TTFA): the elapsed time from when the user stops speaking to when they hear the first sample of the agent's reply. TTFA is always larger than any single model's inference latency, because it sums the whole pipeline.
A cascaded voice agent is a chain of five stages:
capture (mic) -> STT -> LLM -> TTS -> playback
Audio is captured from the microphone, transcribed to text, sent to a language model, the model's text is synthesized back to speech, and that speech is buffered and played. Each stage adds latency, and in several stages the largest cost is not the one you would expect.
Here is a worked example for an English-language agent with servers reasonably close to the user. The numbers are illustrative ranges, not guarantees.
What it covers
Capture + endpointing
Mic capture, VAD/turn-detection delay before the turn is considered finished
STT finalization
Last partial to committed transcript after end-of-speech
Network (client to your server to our API)
Round-trips across the pipeline
LLM time-to-first-token
Prompt processing until the first usable token
TTS time-to-first-audio
First TTS request until first audio chunk leaves the model
Player buffering
Client-side buffer before playback begins
End-to-end TTFA
The total latency of the end-to-end pipeline
P50
Capture + endpointing
120 ms
STT finalization
60 ms
Network (client to your server to our API)
60 ms
LLM time-to-first-token
250 ms
TTS time-to-first-audio
110 ms
Player buffering
80 ms
End-to-end TTFA
~680 ms
P95
Capture + endpointing
280 ms
STT finalization
150 ms
Network (client to your server to our API)
160 ms
LLM time-to-first-token
600 ms
TTS time-to-first-audio
220 ms
Player buffering
150 ms
End-to-end TTFA
~1560 ms
Stage
What it covers
P50
P95
Capture + endpointing
Mic capture, VAD/turn-detection delay before the turn is considered finished
120 ms
280 ms
STT finalization
Last partial to committed transcript after end-of-speech
60 ms
150 ms
Network (client to your server to our API)
Round-trips across the pipeline
60 ms
160 ms
LLM time-to-first-token
Prompt processing until the first usable token
250 ms
600 ms
TTS time-to-first-audio
First TTS request until first audio chunk leaves the model
110 ms
220 ms
Player buffering
Client-side buffer before playback begins
80 ms
150 ms
End-to-end TTFA
The total latency of the end-to-end pipeline
~680 ms
~1560 ms
Typically, the two largest latency line items are the LLM's time-to-first-token and the endpointing delay at the start of the chain.
The table is a useful way to visualize the pipeline, but it implies the stages run strictly in series, which they don’t. Several of the most significant voice agent latency optimizations come from overlapping them, and that overlap is where most of the budget below is recovered.
Speech to Text: transcription and endpointing latency optimization
Transcription is the second stage in the pipeline, and its real cost is not the transcription itself but deciding when the user has stopped talking. This section covers both aspects to help you optimize voice agent latency.
Transcription happens before it reaches the LLM.
Scribe v2 Realtime
(scribe_v2_realtime) returns partial transcriptions in approximately 150ms and streams in audio chunks, so the transcript is materialized while the user is still speaking. It supports PCM at 8kHz to 48kHz and mu-law encoding, which matters for the codec section below. The 150ms partials are inexpensive.
The larger latency cost is endpointing: the moment your system decides the user has actually finished their turn.
Voice Activity Detection (VAD) segments speech on silence, and that is where the time accumulates. If you wait for, say, 700ms of silence before declaring the turn over, you have added 700ms to every turn, on top of the transcription itself. That delay is invisible in a transcription-accuracy benchmark but very present in a real conversation. It is frequently the largest controllable latency in the whole pipeline, and because it is controllable, it is a good place to start.
Endpointing is a tradeoff between responsiveness and interruption. A short silence threshold makes the agent reply quickly but risks cutting the user off mid-sentence on a natural pause. A long threshold is safe but sluggish. In practice, the three changes that optimize latency in speech to text are:
Fine-tune the silence threshold:
Tighten the silence threshold to the smallest value that does not truncate your users' natural pauses, then measure interruption rate in production rather than guessing.
Embed a physical control event:
Use manual commit control when your application knows the turn is over from another signal (a push-to-talk release, a UI event), instead of waiting for the VAD timer.
Overlap with LLM processes:
Run partials downstream early. Feed stable partials into the LLM and revise if the final transcript differs, a form of speculative execution that hides the endpointing delay behind LLM prompt processing.
For more information, Scribe v2 Realtime is described in more detail on the
speech to text capabilities
page and the
realtime speech to text
product page.
The LLM latency contribution
The language model is usually the largest single contributor to TTFA, so it is also where overlap pays off most in voice agent latency optimization. The key insight here is that the agent does not need the whole answer before it starts speaking.
The pattern that recovers the most latency budget is to stream tokens out of the LLM and feed them into TTS as they arrive, chunked at sentence or clause boundaries. The logic is to buffer tokens until a sentence boundary, then synthesize that sentence while the next one is still being generated:
const
SENTENCE_END
=
/(?<=
[.!?]
)
\s
+
/
;
async function*
speakLlmStream(
tokens
: AsyncIterable<
string
>) {
let
buffer =
""
;
for await
(
const
token
of tokens) {
    buffer += token;
const
parts
= buffer.split(
SENTENCE_END
);
    buffer = parts.pop() ??
""
;
// keep the incomplete fragment
for
(
const
sentence
of parts) {
if
(sentence.trim())
yield*
synthesize(sentence.trim());
    }
  }
if
(buffer.trim())
yield*
synthesize(buffer.trim());
}
async function*
synthesize(
text
:
string
) {
const
stream
=
await
elevenlabs.textToSpeech.stream(
"JBFqnCBsd6RMkjVDRZzb"
, {
    text,
modelId:
"eleven_flash_v2_5"
,
outputFormat:
"mp3_44100_128"
,
  });
yield*
stream;
}
For long-running conversations, prefer the
TTS WebSocket
so that an open connection can receive text incrementally without re-paying connection setup on every sentence. Only the time the model is actively generating audio counts toward your concurrency limit, so an idle open WebSocket is nearly free.
Text to Speech: streaming and voice choice
Text to speech is the stage where you can pin down latency most precisely. It has two main levers: how you stream the audio out and which voice you choose.
Flash v2.5 (eleven_flash_v2_5) is the model to use in an agent. It delivers approximately 75ms of model inference for short inputs, supports 32 languages, and accepts up to 40,000 characters per request.
The 75ms figure is inference only. The TTS TTFA line in the budget above is larger because it adds the network round-trip and server scheduling on top of inference.
The largest lever here is streaming. If you request the full audio and wait for it, the user waits for the entire clip to synthesize before hearing anything. If you stream, the user hears the first chunk as soon as it is generated, and the rest arrives while they are already listening. Streaming does not make the model faster; it simply starts outputting to the user while it is still generating.
The
streaming how-to guide
covers HTTP streaming, and the
realtime WebSocket guide
covers the WebSocket path you will want when feeding tokens from an LLM.
Initialize the client once and reuse it for every call below:
import
{ ElevenLabsClient }
from
"@elevenlabs/elevenlabs-js"
;
const
elevenlabs
= new ElevenLabsClient({
apiKey:
process.env.
ELEVENLABS_API_KEY
});
Then set up a stream and forward it as it comes in:
const
stream
=
await
elevenlabs.textToSpeech.stream(
"JBFqnCBsd6RMkjVDRZzb"
, {
text:
"Your call is connected. How can I help today?"
,
modelId:
"eleven_flash_v2_5"
,
outputFormat:
"mp3_44100_128"
,
});
for await
(
const
chunk
of stream) {
// forward each chunk to your audio sink as it arrives
}
The other lever is the choice of voice, which also has a latency cost. Default voices, synthetic voices, and Instant Voice Clones (IVCs) synthesize faster than Professional Voice Clones (PVCs), because PVCs carry additional model complexity that adds per-generation overhead. For an agent with strict latency requirements, the combination of Flash plus an IVC or a default voice is the lowest-latency option.
Streaming chunk size choices
With tokens flowing into TTS and audio flowing back, the next decision is how large to make the pieces and how much the player buffers before it starts.
Smaller chunks reach the player sooner, lowering first-byte latency, at the cost of more messages and slightly more per-chunk overhead. Larger chunks are more efficient to transport but make the user wait longer for the first one. For interactive agents, bias toward smaller chunks early in the utterance, because the first chunk is the one the user is waiting on; later chunks arrive while audio is already playing, and their size matters less.
The player accounts for a significant amount of the remaining latency. Most audio players do not begin playback at the first byte. They buffer a small amount to avoid stuttering if the stream briefly slows. A 500ms default buffer is common, and it is added directly to perceived latency. Reducing it trades a small increase in stutter risk for lower TTFA, and the right value depends on the network jitter between your server and the client:
On a stable connection (server-side playback, a co-located client), a buffer of 50 to 150ms is usually safe and shaves a noticeable amount off TTFA.
On a jittery mobile or cross-region connection, a larger buffer prevents audible gaps that are worse than the latency they cost.
The exact configuration you choose here depends on your active use case and what you prioritize.
Codec choices
Where the audio is going should dictate the codec you request. We return formats such as mp3_44100_128, mp3_22050_32, pcm_16000, pcm_24000, and ulaw_8000. Matching the transport’s native format removes a transcoding step, helping with voice agent latency optimization.
For telephony, such as Twilio and similar providers, use ulaw_8000. The telephony network is 8kHz mu-law end-to-end, so requesting it directly avoids a transcoding step in your pipeline and matches what the carrier expects. There is no benefit to synthesizing higher-fidelity audio that the phone network will immediately downsample; you would only add latency and lose nothing audible.
For WebRTC and browser playback, use PCM (pcm_24000 or pcm_16000) or an MP3 format. PCM is uncompressed, so there is no decode step on the client, which removes a small amount of per-chunk latency and is convenient when you are feeding a Web Audio pipeline directly. MP3 is more compact on the wire, which helps on constrained connections, at the cost of a lightweight client-side decode.
Geography and network distances
Every optimization above assumes the bytes have a short distance to travel. Geography sets the floor on your latency budget, meaning it's worth examining before you tune anything else.
We serve requests from clusters in North America, Europe, and Southeast Asia and route each request to the nearest cluster automatically. The network round-trip over the public internet is typically 20 to 200ms depending on geographic proximity, and it is irreducible without changing where your infrastructure runs.
An agent that feels instant in San Francisco, a short hop from a North American cluster, can feel sluggish to a user in South Asia whose traffic crosses an ocean twice per turn.
The fix is to co-locate your application servers with your users, not only with us. If your users are in Europe, run your agent backend in Europe so that the user-to-your-server leg is short; our routing then handles the your-server-to-model leg from a nearby cluster.
Measuring voice agent latency yourself
The numbers in the latency budget table above are illustrative ranges to plan against. The numbers you ship against should come from a script like this one, run against your own deployment.
The instrumentation below measures TTFA for the TTS stage in isolation, the time from request to first audio chunk, across many trials, and reports the percentiles. Run it from the same region your servers run in, not from your development machine. It assumes the elevenlabs client from earlier:
const
VOICE_ID
=
"JBFqnCBsd6RMkjVDRZzb"
;
const
TEXT
=
"Thanks for waiting. I have pulled up your account and I can help with that now."
;
const
TRIALS
=
50
;
async function
measureTtfa(): Promise<
number
|
null
> {
const
start
= performance.now();
const
stream
=
await
elevenlabs.textToSpeech.stream(
VOICE_ID
, {
text: TEXT
,
modelId:
"eleven_flash_v2_5"
,
outputFormat:
"mp3_44100_128"
,
  });
for await
(
const
_chunk
of stream) {
return
performance.now() - start;
// first chunk -> stop the clock
}
return
null
;
}
function
percentile(
values
:
number
[],
p
:
number
):
number
{
const
v
= [...values].sort((
a
,
b
)
=>
a - b);
const
k
= (v.
length
-
1
) * (p /
100
);
const
lo
= Math.floor(k);
const
hi
= Math.min(lo +
1
, v.
length
-
1
);
return
v[lo] + (v[hi] - v[lo]) * (k - lo);
}
const
samples
:
number
[] = [];
for
(
let
i =
0
; i <
TRIALS
; i++) {
const
ttfa
=
await
measureTtfa();
if
(ttfa !==
null
) samples.push(ttfa);
await
new
Promise
((
r
)
=>
setTimeout(r,
300
));
// space requests, don't measure your own queueing
}

console.log(
`trials: ${
samples
.
length
}`
);
console.log(
`P50:    ${
percentile
(
samples
,
50
).
toFixed
(
0
)} ms`
);
console.log(
`P95:    ${
percentile
(
samples
,
95
).
toFixed
(
0
)} ms`
);
A few things to remember:
Report P50 and P95:
Focus on these, rather than mean. The mean hides the tail, and the tail is what makes an agent feel unreliable. P95 is the experience of one turn in twenty.
Location-based experimentation:
Run the same script from each region you serve and keep the results separate.
Stagger for accuracy:
Space your requests (the setTimeout above). If you fire them all at once, you measure your own queuing instead of the service. When the concurrency limit is exceeded, requests queue by priority, which typically adds about 50ms, and beyond capacity you receive HTTP 429.
Measure the entire latency chain:
Extend the same timing pattern to the other stages. Wrap your STT finalization, your LLM first-token, and your player startup in the same performance.now() brackets, and you can populate the full budget table with your own numbers and see which stage to attack first.
By following these tips, you’ll be able to measure voice agent latency yourself. From there, you’ll have a clear path of priorities to tackle first.
What reduces voice agent latency the most?
If you want some quick action items to focus on, these are the highest-leverage changes.
Roughly in order of impact, you can use the following methods to reduce agent latency:
Start LLM work on stable STT partials to hide the endpointing delay.
Stream LLM tokens into TTS at sentence boundaries so the synthesis of sentence one overlaps the generation of sentence two.
Stream TTS audio to the player and trim the player buffer to the smallest value your network jitter tolerates.
Use Flash plus a default voice or IVC for the lowest-latency TTS, and match the codec to the transport (ulaw_8000 for telephony, PCM or MP3 for browser/WebRTC).
Co-locate your servers with your users and measure per region, because the network legs are real and unequal.
For deeper specific techniques, see the
latency optimization how-to developer guide
. For a full runnable starting point, the API quickstart and the streaming how-to have complete examples.
Want faster access to fine-tuned agent cascades?
ElevenAgents
implements this pipeline with overlap optimizations already in place.
Build low-latency voice agents with ElevenAgents
Voice agent latency optimization requires measuring each stage and then overlapping stages so the slowest ones run behind work that’s already happening. You can build and tune that cascade by hand over several iterations, making use of the patterns above or get started from a pipeline that already has latency optimizations in place.
ElevenAgents implements this full cascade, from streaming STT to token-by-token LLM handoff to Flash TTS, with overlap techniques already built in. Rather than starting from scratch, you’ll tune thresholds for the performance that matters most to you.
Get started by using ElevenAgents to
create an agent today
or
contact sales
for more information.
FAQs about voice agent latency optimization
What is voice agent latency?
Voice agent latency is the total delay between when a user finishes speaking and when the agent begins to reply. It’s the sum of all the moving components that connect to capture, transcribe, fetch data, synthesize speech, and play the audio. From a user perspective, this figure is time-to-first audio, which measures the full end-to-end chain, rather than any one model’s speed.
What causes latency in voice AI agents?
There are five separate components in a voice AI agent that work together from end-to-end. Latency begins to accumulate when any one of these components takes additional time. The two largest contributors are the LLMs’ time-to-first-token and the endpointing delay, which is the total amount of silence your system waits through before deciding the user has finished. Other aspects, like geographical location and network distance from servers, also add to voice agent latency.
What is a good latency for a voice agent?
A natural-feeling voice AI agent typically targets a P50 time-to-first audio under 800ms and a P95 under 1.5 seconds. P95 still represents the user experience of one turn in twenty, with slow tail agents feeling unreliable. That said, measuring against your own deployment rather than using these illustrative figures will be more instructive.
How do you reduce voice agent latency?
The most significant action you can take to reduce agent latency is overlapping pipeline stages rather than running them in series. Actions like starting LLM work on stable speech to text partials and streaming LLM tokens into text to speech at sentence boundaries all help reduce voice agent latency.
What’s the difference between TTFA and inference latency?
Time-to-first-audio is the full delay the user experiences when interacting with a voice AI agent, from the moment they stop speaking to the first sample of the reply. TTFA is the accumulation of every pipeline stage. Inference latency is the time a single model spends generating output. You can compare specific models by looking at inference latency while TTFA measures the real experience.
