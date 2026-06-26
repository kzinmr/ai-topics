---
title: "Real-time Speech to Text latency guide: Under 200 ms"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/real-time-speech-to-text-under-200ms"
scraped: "2026-06-26T06:00:29.149459+00:00"
lastmod: "2026-06-25T18:19:36.966Z"
type: "sitemap"
---

# Real-time Speech to Text latency guide: Under 200 ms

**Source**: [https://elevenlabs.io/blog/real-time-speech-to-text-under-200ms](https://elevenlabs.io/blog/real-time-speech-to-text-under-200ms)

Blog
Resources
Real-time Speech to Text under 200ms: an architecture guide
Written by
Tadas
Petra
Jack
Limebear
Published
Jun 25, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Sign up
Learn more
On this page
Introduction
TL;DR
WebSocket vs. WebRTC for real-time speech to text
Partials and final transcripts: interim results explained
End-pointing and voice activity detection (VAD)
In-stream features: language detection and speaker diarization
Audio formats for streaming: PCM and mu-law
The pipeline in code
Benchmarking speech to text latency and word error rate
Recapping how you can achieve real-time speech to text
Construct real-time speech to text systems with Scribe v2 Realtime
Real-time speech to text latency FAQ
Real-time speech to text (STT) actively transcribes audio as a person speaks, returning their words as text within a few hundred milliseconds. But keeping STT latency low is as much an architectural problem as a model one. Engineers need to plan across the transport, chunking, end-pointing, and capture path, each of which adds latency to the equation. Inefficiency in any one of these can blow your 200ms budget.
This guide offers a practical system you can use to build real-time speech to text pipelines from the transport layer up. We’ll anchor on
Scribe v2 Realtime
, which produces partial transcriptions in roughly 150ms of model latency, supports 90+ languages, accepts PCM (8kHz-48kHz) and mu-law audio, and exposes Voice Activity Detection plus manual commit control for segment finalization.
We’ll trace how the audio reaches the server, how hypotheses evolve into committed text, what in-stream features cost, and how to capture and forward audio correctly.
TL;DR
Creating real-time speech to text systems requires architectural fine-tuning, ensuring latency remains low across the entire pipeline.
WebSocket is the right default for most pipelines, although WebRTC does offer a range of benefits while being more complex.
Voice Activity Detection handles hands-free segmentation, with manual commit giving your applications an override when it knows the turn is over.
Partials are provisional and finals are committed, meaning you should render them differently.
Small PCM chunks of around 100ms minimize latency to the first partial.
WebSocket vs. WebRTC for real-time speech to text
Before any transcription happens, audio has to travel from the source to the recognizer. The channel you choose sets the latency floor for everything downstream. There are two viable options for audio to reach the transcription layer.
WebSocket is a long-lived, ordered, reliable, bidirectional channel over TCP. You open a connection, push binary audio frames up, and read transcript events down. It is straightforward on both client and server, it traverses the corporate proxies and firewalls that already allow HTTPS, and every browser and server runtime supports it.
The constraint with WebSocket is that it rides on TCP. If a packet is lost, TCP retransmits and holds back later data until the gap is filled. Under good network conditions this is not noticeable. Under packet loss, it produces head-of-line blocking, a brief stall where audio backs up and then arrives in a burst.
WebRTC is built for real-time media. It runs media over UDP (via SRTP), so a lost packet does not stall the stream; the pipeline continues. It includes a jitter buffer that absorbs variation in packet arrival timing, it negotiates NAT traversal with ICE/STUN/TURN so peers behind routers can connect, and it carries its own audio capture and encoding machinery.
You typically need TURN servers for clients that cannot connect directly, and the server side has to terminate a media stream rather than read a byte stream.
Here is the tradeoff at a glance:
WebSocket
Transport
TCP (reliable, ordered)
Behavior under packet loss
Head-of-line blocking, bursty recovery
Jitter handling
Your responsibility
NAT traversal
Not needed (client-initiated)
Browser support
Universal, trivial
Server complexity
Low
WebRTC
Transport
UDP/SRTP (real-time, loss-tolerant)
Behavior under packet loss
Graceful degradation
Jitter handling
Built-in jitter buffer
NAT traversal
Requires ICE/STUN/TURN
Browser support
Universal, but more API surface
Server complexity
High (media server or SFU)
Concern
WebSocket
WebRTC
Transport
TCP (reliable, ordered)
UDP/SRTP (real-time, loss-tolerant)
Behavior under packet loss
Head-of-line blocking, bursty recovery
Graceful degradation
Jitter handling
Your responsibility
Built-in jitter buffer
NAT traversal
Not needed (client-initiated)
Requires ICE/STUN/TURN
Browser support
Universal, trivial
Universal, but more API surface
Server complexity
Low
High (media server or SFU)
For most use cases, WebSocket is the right option. Use it when your clients have decent connectivity and you control the capture path: server-to-server pipelines, desktop apps, browser apps on broadband, and most contact-center backends where audio already arrives at your server by some other means.
Choose WebRTC when you are capturing directly from consumer devices on unreliable mobile networks, when you are already running a WebRTC stack for two-way audio (a voice agent that also speaks back, for example), or when low-loss real-time behavior matters more than implementation simplicity.
The rest of this guide uses WebSocket transport for the recognizer connection, because it keeps the moving parts visible and is the right starting point for most teams. None of it is specific to WebSocket, so you can later add a WebRTC media leg in front, decode the audio to PCM on the server, and forward the same chunks into the pipeline.
Partials and final transcripts: interim results explained
A real-time reorganizer doesn’t wait for a complete sentence before it speaks. Instead, it emits a running stream of guesses that sharpen as more audio arrives, then locks them in. Understanding the difference between those two states is what separates a transcript that feels alive from one that feels broken.
A partial (interim) hypothesis is the model's best guess given the audio received so far. Partials are unstable by design. As more audio arrives, the model revises earlier words: "I want to" can become "I want two tickets" once later context resolves the ambiguity. They arrive fast (this is what the ~150ms latency figure describes) and are meant to be overwritten.
A final hypothesis is a committed segment that will not change. Once a segment is finalized, the recognizer moves on, and subsequent hypotheses describe later audio. Finals are what you persist, send to an LLM, or store as a transcript.
The distinction between partials and finals drives three things that you will get wrong if you blur it:
User experience:
Showing partials makes a transcript feel live: the user sees words appear as they speak, which confirms that the microphone works and the system is listening.
End-pointing:
Partials give you a continuous signal of speech activity. Combined with VAD, they let you decide when the speaker has actually stopped.
Downstream timing:
In a
voice agent pipeline
the steps are audio in, then speech to text, then an LLM, then text to speech, then audio out. You can begin speculative work on partials and confirm on finals, reducing perceived response time at the cost of occasionally discarding speculative work.
Render partials and finals differently. A simple, effective pattern is to keep a single mutable "current line" bound to the latest partial and commit it to an append-only transcript when a final arrives:
type
TranscriptState = {
committed
:
string
[];
// finalized segments, never rewritten
current
:
string
;
// latest partial, overwritten on each update
};
const
onPartial = (
s
: TranscriptState,
text
:
string
): TranscriptState
=>
({ ...s,
current:
text });
const
onFinal = (
s
: TranscriptState,
text
:
string
): TranscriptState
=>
({
committed:
[...s.
committed
, text],
current:
""
});
Visually, render committed as settled text and current in a lighter or italic style so the user understands it may still change.
End-pointing and voice activity detection (VAD)
Knowing what was said is only half the battle. A recognizer also has to know when a thought has ended. That decision drives when you finalize a segment and, in an agent, when the system starts to respond.
End-pointing is the decision that an utterance has ended. Finalizing too early cuts users off mid-sentence. Finalizing too late leaves an agent silent after the user has clearly finished.
Scribe v2 Realtime gives you two complementary mechanisms to work with:
Voice Activity Detection segments audio based on silence:
The recognizer detects when speech gives way to sustained silence and uses that boundary to finalize a segment automatically. VAD is the right default for conversational interfaces because it adapts to natural speech rhythm without you tracking timing by hand.
Manual commit control:
Manual commit control lets your application decide when to finalize the current segment, independent of silence. You send a commit signal, the recognizer closes the current segment and emits a final. This is the right tool when your application already knows the turn is over: a push-to-talk button release, a "send" action or an external turn-taking policy.
The two compose well together. A typical voice agent uses VAD for hands-free operation and exposes manual commit as an override, so a user who pauses to think is not cut off, but a user who taps a button gets an immediate boundary.
The silence threshold is a genuine tradeoff with no universally correct value:
A short end-of-speech timeout (for example, finalization after ~200-400ms of silence) makes the system feel responsive. It also cuts off users who pause naturally between clauses, splitting one thought into several segments and, in an agent, triggering a premature response.
A long timeout (for example, ~800-1200ms) tolerates natural pauses and keeps utterances intact, at the cost of a noticeable lag before the system reacts.
There is no global constant to use here; tune the threshold to the interaction:
Dictation and note-taking tolerate longer pauses because users think mid-sentence. Bias toward longer timeouts and lean on VAD.
Command-and-control and transactional agents benefit from shorter timeouts plus manual commit, because turns are short and crisp.
Multilingual or non-native speakers pause more, so budget more silence before finalizing.
Using these tips helps guide you to build an effective end-pointing system and move toward real-time speech to text.
In-stream features: language detection and speaker diarization
Streaming recognition can do more than produce words. That said, every extra signal you ask for interacts with latency and stability. The rule of thumb here is to turn on only what the live experience needs and defer the rest to a batch pass.
Automatic language recognition lets Scribe v2 Realtime identify the spoken language across its 90+ supported languages rather than requiring you to declare it up front. The cost is that the model needs a short span of audio to make a confident determination, so the first partials of a stream may be less stable while the language settles. If you already know the language, specifying it removes that ambiguity and tends to yield steadier early partials.
Speaker diarization attributes speech to distinct speakers, identifying who said what. In batch transcription, this is comparatively easy because the model sees the whole file. In streaming it is harder: the recognizer has to assign a speaker label from only the audio so far, and a label given to early audio may need revising once more of that speaker's voice is heard. Treat streaming speaker labels the same way you treat partial text: provisional until the segment finalizes.
Word-level timing and entity context follow the same logic. The more per-token metadata you request, the more both the model and the wire have to carry. For most real-time UIs you need the text and segment boundaries live and nothing more, and you can defer the fine-grained metadata to a post-call batch pass with Scribe v2.
Audio formats for streaming: PCM and mu-law
Transport and recognition logic get most of the attention, but a surprising share of real-world bugs originate one layer down, in how you encode and chunk the audio. Getting the format and chunk size right is the cheapest speech to text latency win available.
PCM (linear, 16-bit signed, little-endian) is the format to use when you control capture. Higher sample rates carry more acoustic detail: 16kHz is the standard floor for speech recognition and is usually sufficient; 8kHz is telephone-grade and loses high-frequency content. Use the rate that matches your source. There is no benefit to upsampling 8kHz telephony audio to 48kHz, because the information is not there to recover.
Mu-law at 8kHz is the telephony format. If you are ingesting calls from a provider such as Twilio, audio arrives as 8kHz mu-law, and you should forward it in that format rather than transcoding it twice. Matching the source format avoids resampling artifacts and a needless conversion step.
Chunk sizing is the lever that most directly shapes perceived latency. You send audio in chunks, and the recognizer produces partials as chunks arrive. Smaller chunks mean more frequent updates and lower latency to the first partial; larger chunks mean fewer messages and slightly more context per inference. A practical range is 20-250ms of audio per chunk. As a concrete anchor, at 16kHz mono 16-bit PCM one second of audio is 32,000 bytes, so a 100ms chunk is about 3,200 bytes.
Capturing microphone input in the browser
In the browser, the right tool is the Web Audio API with an AudioWorklet. The worklet runs on the audio rendering thread, receives audio in small frames, and is not subject to main-thread jank the way the older ScriptProcessorNode was. Its job is to convert the browser's native float samples to 16-bit PCM and hand them to the main thread, which forwards them over the WebSocket.
The core of the worklet processor is the float-to-PCM conversion:
// pcm-worklet.ts - registered via audioContext.audioWorklet.addModule()
class
PCMWorklet
extends
AudioWorkletProcessor {
  process(
inputs
: Float32Array[][]) {
const
channel
= inputs[
0
]?.[
0
];
// mono; Float32, range [-1, 1]
if
(!channel)
return
true
;
const
pcm
= new Int16Array(channel.
length
);
for
(
let
i =
0
; i < channel.
length
; i++) {
const
s
= Math.max(-
1
, Math.min(
1
, channel[i]));
      pcm[i] = s <
0
? s *
0x8000
: s *
0x7fff
;
    }
// Transfer the buffer to the main thread without copying.
this
.port.postMessage(pcm.
buffer
, [pcm.
buffer
]);
return
true
;
  }
}
registerProcessor(
"pcm-worklet"
, PCMWorklet);
The pipeline in code
The pipeline has three moving parts: a browser client that captures the microphone and streams PCM to your server, a Node server that relays audio to Scribe v2 Realtime and relays transcripts back, and a scriptable client that streams PCM from a file or telephony bridge.
The server relays rather than exposing the recognizer directly to the browser for one important reason: your ElevenLabs API key is a secret and must never appear in client-side code. The server holds the key. If you do need the browser to talk to the recognizer directly, mint a short-lived single-use token server-side and hand the client that instead of the API key.
Browser client
The client opens a WebSocket to your server, captures the microphone through the worklet above, and forwards each PCM frame as it is produced. Incoming events (already normalized by the server into { type, text }) drive the partial/final state from earlier:
// client.ts - runs in the browser. ws is an open WebSocket to your server.
const
audioContext
= new AudioContext({
sampleRate: 16000
});
await
audioContext.audioWorklet.addModule(
"pcm-worklet.js"
);
const
mediaStream
=
await
navigator.mediaDevices.getUserMedia({
audio:
{
channelCount: 1
,
echoCancellation: true
,
noiseSuppression: true
},
});
const
source
= audioContext.createMediaStreamSource(mediaStream);
const
worklet
= new AudioWorkletNode(audioContext,
"pcm-worklet"
);
// Forward each PCM frame to the server the moment it is produced.
worklet.port.onmessage = (
e
: MessageEvent<ArrayBuffer>)
=>
{
if
(ws.
readyState
=== WebSocket.
OPEN
) ws.send(e.
data
);
};
source.connect(worklet);
// Manual commit: tell the server to finalize the current segment.
const
commit = ()
=>
ws.send(
JSON
.stringify({
type:
"commit"
}));
Server relay
The server opens one recognizer connection per client, keeps the API key on the server, forwards binary PCM straight through, and normalizes recognizer events into the stable { type, text } shape the client consumes:
// server.ts - Node, using the `ws` library. ELEVENLABS_API_KEY and the
// recognizer URL come from the environment; see the Speech to Text reference
// for the exact path and query parameters.
import
{ WebSocketServer, WebSocket }
from
"ws"
;

new WebSocketServer({
port: 8080
}).on(
"connection"
, (
client
)
=>
{
// The API key stays on the server, never on the wire to the browser.
const
recognizer
= new WebSocket(process.env.
RECOGNIZER_WSS_URL
!, {
headers:
{
"xi-api-key"
:
process.env.
ELEVENLABS_API_KEY
! },
  });
// Browser -> recognizer: forward binary PCM, translate control messages.
client.on(
"message"
, (
data
,
isBinary
)
=>
{
if
(recognizer.
readyState
!== WebSocket.
OPEN
)
return
;
if
(isBinary) recognizer.send(data);
// raw PCM bytes
else if
(
JSON
.parse(data.toString()).
type
===
"commit"
)
      recognizer.send(sendCommit());
  });
// Recognizer -> browser: normalize events into a stable shape.
recognizer.on(
"message"
, (
raw
)
=>
{
const
event
= parseRecognizerEvent(raw.toString());
if
(event && client.
readyState
=== WebSocket.
OPEN
)
      client.send(
JSON
.stringify(event));
  });
// ... open handshake, queueing pre-open audio, and teardown on close/error
});
Everything endpoint-specific is confined to the two adapter functions below. Replace the field names with the exact ones from the Speech to Text reference; the rest of the pipeline does not change:
// The single place that knows the recognizer's wire format.
const
sendCommit = ():
string
=>
JSON
.stringify({
type:
"commit"
});
type
NormalizedEvent =
  | {
type
:
"partial"
;
text
:
string
}
  | {
type
:
"final"
;
text
:
string
}
  | {
type
:
"vad"
;
speaking
:
boolean
};
function
parseRecognizerEvent(
raw
:
string
): NormalizedEvent |
null
{
const
msg
=
JSON
.parse(raw);
if
(msg.
is_final
===
true
|| msg.
type
===
"final"
)
return
{
type:
"final"
,
text:
msg.
text
??
""
};
if
(msg.
type
===
"vad"
)
return
{
type:
"vad"
,
speaking:
!!msg.
speaking
};
if
(typeof msg.
text
===
"string"
)
return
{
type:
"partial"
,
text:
msg.
text
};
return
null
;
}
Scriptable backend client
For backend pipelines and for the benchmark below, the same recognizer connection works without a browser: read PCM from any source, pace it at the real-time chunk cadence, and read events back. The API key and URL come from the environment, as on the server.
// stream-stt.ts - pace ~100ms chunks at real time, then commit the tail.
const
SAMPLE_RATE
=
16000
,
CHUNK_MS
=
100
;
const
CHUNK_BYTES
= (
SAMPLE_RATE
*
2
*
CHUNK_MS
) /
1000
;
// 3200 bytes
const
ws
= new WebSocket(process.env.
RECOGNIZER_WSS_URL
!, {
headers:
{
"xi-api-key"
:
process.env.
ELEVENLABS_API_KEY
! },
});
// Send: walk the PCM buffer in 100ms chunks, sleeping between to mimic a
// live source. For audio that already arrives in real time, drop the sleep.
async function
sendAudio(
pcm
: Buffer) {
for
(
let
off =
0
; off < pcm.
length
; off +=
CHUNK_BYTES
) {
    ws.send(pcm.subarray(off, off +
CHUNK_BYTES
));
await
new
Promise
((
r
)
=>
setTimeout(r,
CHUNK_MS
));
  }
  ws.send(
JSON
.stringify({
type:
"commit"
}));
// finalize the trailing segment
}
// Receive: print partials in place, append finals.
ws.on(
"message"
, (
raw
)
=>
{
const
e
= parseRecognizerEvent(raw.toString());
if
(e?.
type
===
"final"
) console.log(
`[final]   ${
e
.
text
}`
);
else if
(e?.
type
===
"partial"
) process.stdout.write(
`[partial] ${
e
.
text
}
\r
`
);
});
Benchmarking speech to text latency and word error rate
Latency and word error rate both vary with the speaker, the language, the acoustic conditions, the audio length, your network path to each provider's nearest region, and the current load on each service.
A result measured from a laptop in one city does not generalize to your production fleet in another. Run the harness from infrastructure that resembles production, on audio that resembles your real input, and report ranges and distributions rather than single numbers.
The only latency and accuracy figures that matter are the ones you measure on your own audio from infrastructure that resembles production. Here is a guide to benchmarking speech to text latency.
What to measure for speech to text latency
Below are the main metrics you should measure when benchmarking real-time speech to text latency:
Time to first partial:
From sending the first audio chunk to receiving the first non-empty partial.
Partial-to-final lag:
From the last audio chunk of an utterance to the final hypothesis.
Word error rate (WER):
WER on the finalized transcript against a human reference, computed identically across all systems.
Stability churn:
How many partials are rewritten before finalizing. This measure is a proxy for how much the live UI will appear to change.
Controls
To avoid unreliable data, you should implement several controls into your experiment to keep things consistent.
Here are the main controls to use with speech to text latency benchmarking:
Identical audio:
Use the same files, same sample rate, and same encoding fed to every system.
Identical pacing:
Stream every system at the same real-time chunk cadence (for example 100ms chunks).
Repeat and report distributions:
Run each file many times across the day; report median and tail (p50/p95).
Identical references and scoring:
Normalize text the same way (casing, punctuation, numbers) before computing WER.
Disclose region and network:
State where the harness ran and the path to each provider.
By keeping all of these elements the same, you’ll generate more precise metrics.
Harness skeleton
The measurement core takes a provider adapter and records time-to-first-partial, finalization lag, and partial churn:
// benchmark.ts - measurement core; one StreamFn adapter per provider.
type
StreamFn = (
audioPath
:
string
,
  onEvent: (
kind
:
"partial"
|
"final"
,
text
:
string
)
=>
void
,
result
: RunResult
)
=>
Promise<
void
>;
// adapter sets result.lastChunkSentAt on the final chunk
interface
RunResult {
firstPartialMs
?:
number
;
finalLagMs
?:
number
;
hypothesis
:
string
;
partialEdits
:
number
;
lastChunkSentAt
:
number
;
startedAt
:
number
;
}
async function
measure(
streamFn
: StreamFn,
audioPath
:
string
): Promise<RunResult> {
const
result
: RunResult = {
hypothesis:
""
,
partialEdits: 0
,
lastChunkSentAt: 0
,
startedAt:
performance.now(),
  };
let
prevPartial =
""
;
await
streamFn(audioPath, (
kind
,
text
)
=>
{
const
now
= performance.now();
if
(kind ===
"partial"
) {
if
(text && result.
firstPartialMs
===
undefined
)
        result.
firstPartialMs
= now - result.
startedAt
;
if
(text !== prevPartial) { result.
partialEdits
++; prevPartial = text; }
    }
else
{
// final
result.
hypothesis
= result.
hypothesis
?
`${
result
.
hypothesis
} ${
text
}`
: text;
if
(result.
lastChunkSentAt
)
        result.
finalLagMs
= now - result.
lastChunkSentAt
;
    }
  }, result);
return
result;
}
Word error rate is a standard token-level Levenshtein distance over normalized text. Lowercase and strip punctuation identically on both reference and hypothesis before computing it, or you will measure your normalizer rather than the model. Wrap this measure in a loop that runs each file ~10 times per provider and reports the median time-to-first-partial and median WER (p50/p95), since a single sample is dominated by network variance.
To make it run, you supply two things. First, write one StreamFn adapter per system. The scriptable client above is already one, with adapters for the others following the same (audioPath, onEvent, result) contract and setting result.lastChunkSentAt when the final audio chunk goes out. Second, load your audio files and references and call measures across them. Run it from a machine that represents your deployment, on audio that represents your users, and you will have a comparison you can reproduce.
Recapping how you can achieve real-time speech to text
We’ve covered a lot of architectural changes in this article, allowing you to iteratively improve your system and push toward real-time speech to text.
A production real-time STT system comes down to a handful of decisions:
Transport:
Choose WebSocket for simplicity and controlled networks and WebRTC when you need loss tolerance and are capturing from consumer devices.
Partials and finals:
Treat partials as provisional and finals as committed, and render them differently so users trust the live text.
End-pointing:
Use VAD for hands-free segmentation, manual commit as an override, and tune the silence threshold to the interaction rather than to a constant.
In-stream features:
Turn on in-stream features only where the live experience needs them, and defer the rest to a batch pass with Scribe v2.
Audio format:
Capture in small PCM frames, send ~100ms chunks, and match the source format for telephony.
Benchmarking:
Set the accuracy-versus-latency knobs empirically against your own audio and target metric.
API security:
Keep your
API key on the server
, or mint single-use tokens for direct client connections.
If you’d like to see how to
optimize latency in a voice agent
, we’ve also written a guide for you.
Construct real-time speech to text systems with Scribe v2 Realtime
Scribe v2 Realtime produces partials in roughly 150ms of model latency. Whether your users experience that number or something larger depends on the architecture around it, which is the part you control. By using the strategies set out in this article, you’ll build enhanced pipeline architecture that reduces latency and improves the customer experience.
To go deeper, discover the
Speech to Text capabilities
overview, read through our
models reference
for the full feature and language list, and visit the realtime product pages:
realtime Speech to Text API
and
realtime Speech to Text
.
When you’re ready to build,
create a free ElevenLabs account
and stream your first transcript today.
Real-time speech to text latency FAQ
What is real-time speech to text latency?
Real-time speech to text latency is a measure that describes the total delay between someone speaking and text automatically appearing. You can measure it as time-to-first-partial, which is the gap before the first provisional words begin to appear.
What is the lowest latency speech to text API?
The lowest latency speech to text API comes from streaming APIs that return partial transcripts over a persistent connection. Scribe v2 Realtime returns partials in around 150ms of model latency over WebSocket. The total latency, however, depends on your wider pipeline.
What latency should I expect for streaming transcription?
The time-to-first-partial should come in within the low hundreds of milliseconds in a well-built streaming pipeline, with the model contributing 150ms. Voice agents typically target sub-300ms perceived latency, which you can achieve through pipeline optimization.
Is streaming or batch speech to text better for low latency?
If you’re looking for low-latency speech to text, then streaming is your only option. Batch transcription is unstable for live agents and captioning, as it produces a complete audio file and then returns it. Use batch when you want to prioritize cost over speed.
How do I reduce real-time speech to text latency?
There are several strategies you can use to reduce speech to text latency. For example, send small audio chunks of around 100ms, use WebSocket transport, and match the source format to avoid needing to transcode. If possible, render partials immediately and then fine-tune your end-pointing threshold to the actual interaction, rather than having a fixed constant.
