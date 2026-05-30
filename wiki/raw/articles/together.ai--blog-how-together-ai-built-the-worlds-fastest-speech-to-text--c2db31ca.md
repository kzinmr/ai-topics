---
title: "How Together AI built the world’s fastest speech-to-text stack"
url: "https://www.together.ai/blog/how-together-ai-built-the-worlds-fastest-speech-to-text-stack"
fetched_at: 2026-05-30T07:01:26.915792+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# How Together AI built the world’s fastest speech-to-text stack

Source: https://www.together.ai/blog/how-together-ai-built-the-worlds-fastest-speech-to-text-stack

‍
Artificial Analysis reported speed factor (Input audio seconds transcribed per second) -- Higher is better
Modality matters
A 1M-token text prompt can fit the entire Harry Potter series and still only weigh around 5 MB. That scale sounds enormous, but the input itself is compact. Text also arrives almost ready for inference: tokenize it, batch it, and move it through the model.
Audio changes the shape of the problem. The same Harry Potter corpus as audiobooks is 5 to 10 GB, roughly three orders of magnitude larger than the text. Before any of it reaches the GPU, the server has to decode the container, resample, filter noise, run VAD, segment speech, and compute audio features.
The model side flips too. LLMs these days have hundreds of billions or trillions of parameters, so serving work naturally concentrates inside the GPU: quantization, KV cache, attention kernels, batching, and parallelism. Speech-to-text models are much smaller, often in the hundreds of millions to low billions of parameters, so the surrounding data path matters much more.
That makes ASR serving a full-path systems problem spanning GPU execution, CPU preprocessing, memory movement, transport, connection scheduling, and runtime behavior. The same stack also has to serve two different regimes: offline transcription, where throughput matters most, and streaming transcription, where latency and jitter dominate.
Together’s ASR stack serves the two lowest-latency speech-to-text models ranked by Artificial Analysis: NVIDIA’s Parakeet-TDT 0.6B v3 and OpenAI’s Whisper Large v3. The faster of the two, NVIDIA Parakeet-TDT 0.6B v3, can transcribe roughly 20 hours of speech, about the runtime of the Harry Potter film franchise, in under 10 seconds.
The rest of this post breaks down the production changes behind that result: TensorRT profiles for real audio shapes, GPU-side decoder control flow, lower-copy CPU paths, evented streaming I/O, and runtime GC control.
Compile the encoder for real audio shapes
Parakeet uses an encoder-decoder architecture, and roughly 95% of its weights sit in the encoder. The encoder takes a variable-length speech segment and produces acoustic frames for the decoder, which made it the first place to optimize.
Audio inputs span a wide range of lengths, from a 200 ms streaming packet to 30 seconds of uninterrupted speech. A kernel plan tuned for one input shape can be substantially slower at another, so the engine needs to know the shape distribution it will see at compile time.
Before TensorRT, we were already using an optimized PyTorch path with
torch.compile
and CUDA graphs, tuned across the same shape profiles. That gave us a strong baseline: profile-aware execution without leaving the PyTorch stack.
TensorRT gave us a faster encoder path for production. It builds an optimized execution plan ahead of time, fusing kernels where possible, tuning memory layouts, and benchmarking kernel variants for the shape ranges we expect to serve.
The important detail is profile tuning. A single engine tuned only for the largest input shape forces shorter audio segments into a padded path, which is especially costly for streaming chunks and short utterances. A multi-profile TensorRT engine lets us keep one copy of the encoder weights in memory while selecting the right optimization profile per request.
The memory savings were modest, roughly 6 GB to 5 GB. The larger win was avoiding bad shape matches and moving from optimized PyTorch to TensorRT for tuned profiles. In the small-input regime, profile-aware TensorRT can be several times faster than sending those requests through a large padded profile.
With the encoder optimized, the decoder loop became the next bottleneck.
Remove the CPU from the decoder loop
Parakeet’s decoder iterates over the encoder’s acoustic frames and emits either a token or a
BLANK
for frames that do not advance the transcript. The code is essentially:
state = init()
for frame in encoder_output:
token = predict(frame, state)
if token != BLANK:
emit(token)
state = update(state, token)
When profiling, we found that
predict
and
update
were both fast. The per-iteration GPU work was measured in microseconds.
The expensive line was the branch:
if token != BLANK:
That branch requires the CPU to read the token back from GPU memory to decide which path to take. This host sync prevents the decode loop from being captured as a single CUDA graph and forces every iteration to round-trip through Python. The GPU does a few microseconds of work, waits for the CPU, launches the next kernel, and repeats that pattern thousands of times per request.
Conditional CUDA graph nodes moved that branch onto the GPU. A small device-side kernel evaluates the condition and tells the CUDA runtime whether to enter the token-emission and state-update subgraph. The branch resolves without leaving the GPU, so the entire decoder loop, counter, condition, emit, and state update, can be captured and launched as one CUDA graph.
The CPU leaves the decoder’s inner loop, and the result is a 2 to 3x faster decoder.
‍
Stop copying audio bytes
Once the encoder and decoder were running well, the remaining latency came from the CPU path around the model. That is where most ASR code we’ve audited spends its latency budget: redundant copies, unnecessary process hops on the hot path, and single-threaded functions that would benefit from higher parallelism.
The first lever was collapsing unnecessary process boundaries.
Audio preprocessing, whether file decoding, resampling, voice activity detection (VAD), feature extraction, or chunk handling, is mostly I/O or native C/C++ work that releases the Python Global Interpreter Lock (GIL). A typical microservice architecture splits preprocessing across three or four separate processes, paying for isolation the workload does not need. Collapsing most of that work into fewer processes removes kernel copies and serialization/deserialization passes that can cost hundreds of milliseconds on large files.
When inter-process communication is genuinely needed, common options like ZeroMQ also carry meaningful overhead. In our workload, a simple custom protocol over persistent Unix domain sockets carrying raw audio bytes performs best under high concurrency because it keeps framing minimal and avoids repeated connection setup.
For large files, sockets still impose two copies: sender userspace to kernel buffer, then kernel buffer to receiver userspace. To avoid that path, we use shared memory. With shared memory, both processes map the same physical region, so data written by the producer is visible to the consumer without a kernel round trip. That gives us a zero-copy data path.
The complexity cost is real, so shared memory is worth reaching for only when the data volume justifies it.
Use evented I/O for streaming
Streaming ASR adds another problem: connection lifecycle.
Our first streaming implementation used one thread per connection. When hundreds of streams sent chunks at once, hundreds of threads woke up together, GIL contention exploded, and tail latency spiked.
We moved to one thread blocked on
epoll
.
epoll
lets one thread register thousands of connections and ask the kernel in a single syscall: “wake me up when any of these has data.” When messages arrive, the kernel returns the full ready set, and that thread processes the active sockets before going back to sleep.
Same workload, far less scheduler pressure. For streaming ASR, that predictability matters because delayed partial transcripts can make a voice system feel slow even when average latency looks fine.
‍
‍
Freeze startup state to remove GC tail latency
We almost missed this one.
Under load for streaming workflows, p50 and p90 latency looked healthy, but p95 would periodically spike by about 200 ms. The logs showed small queue depth and normal GPU times, but CPU functions that normally ran in under 5 ms suddenly took over 100 ms.
Something in the background was stealing time from the request loop.
Profiling pointed at Python’s garbage collector (GC). Python uses reference counting for most memory management, with a cycle-detecting collector to catch reference cycles. That collector runs in generations. The oldest generation contains long-lived objects, and full collections can walk a large object graph.
We had preallocated a large pool of buffers, model state, and lookup tables at startup specifically to avoid allocation latency at steady state. Those long-lived objects landed in the oldest generation, so full GC passes walked hundreds of thousands of references. That was the 200 ms stall.
The fix was one line after startup preallocation:
gc.freeze()
gc.freeze()
tells Python to exclude the preallocated state from future GC scans, so normal request-scoped objects still get collected while the giant initial state is left alone.
The p95 spikes disappeared, and p50 improved because the system could sustain smoother traffic patterns.
The lesson was to keep profiling beyond the model. GPU time, queue depth, and model execution all looked normal; the latency spike lived in the Python runtime.
Voice latency is an end-to-end systems problem
Voice agents usually run as a cascade: ASR produces a transcript, an LLM generates the response, and TTS produces audio. ASR is the first stage in that path, so its latency and jitter set the earliest bound on user-visible response time.
The optimizations above target different parts of that path. TensorRT multi-profile engines tune encoder execution for real audio shapes. Conditional CUDA graphs remove CPU round trips from the decoder loop. Persistent Unix domain sockets, shared memory, and
epoll
reduce CPU-path overhead.
gc.freeze()
removes a runtime-level p95 failure mode.
The same constraint applies to the rest of the stack: every stage has to control both median latency and tail latency across model execution, preprocessing, transport, scheduling, and runtime behavior.
‍
NVIDIA Parakeet-TDT 0.6B v3
and
OpenAI Whisper Large v3
are available on Together. Reach out if you’re scaling voice AI in production.
Parakeet v3 is the successor to v2, which was an English-only model that set the pace on the Hugging Face Open ASR Leaderboard for single-language throughput. v3 extends that foundation significantly, expanding language support from English to 25 European languages, adding automatic language detection without requiring a language prompt, and was trained on 1.7 million hours of audio data — including NVIDIA's Granary multilingual corpus.
