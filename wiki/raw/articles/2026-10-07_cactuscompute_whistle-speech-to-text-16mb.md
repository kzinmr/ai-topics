---
source_url: https://cactuscompute.com/blog/whistle
ingested: 2026-10-09
sha256: 64655a125973e72a5684a55649bc6118551c37a7a4ea4ec95b0f9b67037659ba
---

URL: https://cactuscompute.com/blog/whistle
FINAL: https://cactuscompute.com/blog/whistle
TITLE: Whistle: Speech to Text in 16.9 MB
DESC: An open speech recognition model that runs on the same CPU engine as Needle. It transcribes seven languages, reaches the first token in 11 ms, and loads beside Needle so one binary turns a clip straight into tool calls.

Whistle: Speech to Text in 16.9 MB | Cactus Cactus Needle Whistle Platform Pricing Research Blog ⌘K 4.2k+ stars Fine-tune Needle [ NEW ] Needle 3: our 8-29 MB foundation model for tiny devices Back to blog Models Research Whistle: Speech to Text in 16.9 MB An open speech recognition model that runs on the same CPU engine as Needle. It transcribes seven languages, reaches the first token in 11 ms, and loads beside Needle so one binary turns a clip straight into tool calls. JM Jakub Mroz HN Henry Ndubuaku | October 2, 2026 | 6 min read Today we release Whistle, a speech recognition model for mobiles, wearables, robots, smart home, automotive and microcontrollers. It is one 16.9 MB file, runs on the CPU with no dependencies, and loads into the same C++ engine as Needle , from the same container and the same quantisation. 
 Whistle sandbox Speak, and Whistle transcribes it on your device 16.9 MB · runs in this tab Language Keywords Press the mic and say something. Up to 30 seconds in English, German, French, Spanish, Italian, Dutch or Polish. The first press downloads the 16.9 MB model, and audio never leaves your device. 
 Whistle does three jobs, all of them on the device: 
 
 Transcription. 16 kHz mono audio, up to 30 seconds in one pass, in English, German, French, Spanish, Italian, Dutch and Polish. The language is detected unless you name it. 
 Word timestamps. Every word with its start, end and probability, aligned from the decoder's attention. 
 Speech embedding. The encoder output, one row per 80 ms frame, without decoding a transcript. 
 
 The model 
 ENCODER Waveform 16 kHz mono, up to 30 s = 480,000 samples Log-mel 80 bins, 25 ms window, 10 ms hop, 250-3500 Hz, normalised per channel → 3,000 frames Convolutional stem 128 channels, kernel 9, three halvings → 375 frames, one per 80 ms Simple Attention blocks × 8 shared with Needle self-attention over every frame at once, 4 mHC lanes, Monarch Hadamard MLP in place of the FFN DECODER Cross memory K and V projected once per clip, 375 frames × 8 layers, shared by every beam Laddered Simple Attention blocks × 8 shared with Needle GQA 8q : 2kv, 48 qk / 64 v, 3-tap causal conv, engram at layers 3 and 7, width 512 Gated cross attention every decoder layer reads the encoder: x ← x + σ(g) · softmax(q̂ K̂ᵀ/√d) V Beam search × 5 length-normalised log prob, keyword bias by Aho-Corasick automaton Transcript 8,192 text pieces + 7 language tokens, up to 320 of them, word times from the decoder's own attention Blocks marked shared run Needle's code, not a copy of it. --audio-depth selects decoder layers; the encoder always runs all eight. 
 The front end. 16 kHz mono audio is framed at a 25 ms window and a 10 ms hop into 80 log-mel bins, band-limited to 250-3500 Hz and normalised per channel. Thirty seconds is 3,000 frames. A convolutional stem of 128 channels and kernel 9 halves that count three times, leaving 375 frames at one per 80 ms. Every stage after this runs at that rate, and embed returns one row per frame. 
 The encoder. Eight Simple Attention blocks: four mHC residual lanes and a Monarch Hadamard MLP in place of the feed-forward network, the same blocks Needle uses. The attention is not causal. A frame at 3 s attends to a frame at 12 s. 
 The decoder. Eight Laddered Simple Attention blocks at width 512, 8 query heads to 2 KV heads, 48-dimensional queries and keys, 64-dimensional values, a 3-tap causal convolution on Q, K and V, and engram lookups at layers 3 and 7 over 18,432 slots. That is Needle's block list with a different layer count. 
 The speech-specific part is one addition per layer. Each decoder layer reads the encoder through a gated cross attention, x ← x + σ(g) · softmax(q̂ K̂ᵀ/√d) V , with a gate learned per layer and K and V taken from the clip. Those projections run once when the clip arrives, 375 frames across 8 layers, and are then held for the whole decode. Five beams therefore cost five short transcript caches, not five passes over the audio. 
 Decoding. Five beams scored by length-normalised log probability. Keyword biasing walks an Aho-Corasick automaton over the phrases you pass in, alongside the beams, and lifts their log probability as the automaton advances. The transcript is capped at 320 tokens. The vocabulary is 8,192 text pieces plus seven language tokens, one per language, so the detected language is emitted as a token rather than returned out of band. 
 The ladder is on the decoder. Every depth from 2 layers up was trained as a model of its own, and --audio-depth selects one at load time. The encoder is never sliced: all eight blocks run at every depth. 
 Silence. The engine measures the clip's loudness range before the decoder starts. Below the threshold it returns an empty transcript and an empty language, and never enters the beam search. 
 Benchmarks 
 Whistle Whisper base Moonshine tiny v2 Word error rate, lower is better. A missing bar is a benchmark that model's authors never published: Moonshine is English only, and Whisper reports no SPGISpeech, Earnings-22 or AMI cleaned. Whisper's AMI figure is AMI-IHM, a different subset from the AMI the other two report. 
 Whistle is ahead on LibriSpeech test-clean and test-other, on SPGISpeech, on Earnings-22 and on the FLEURS average. Whisper base is ahead on TED-LIUM, on AMI and on the MLS average, at 145.3 MB against 16.9. 
 Size megabytes, smaller is better Whistle 16.9 MB Whisper base 145.3 MB Moonshine tiny v2 41.9 MB Time to first token milliseconds, smaller is better Whistle 11.1 ms Whisper base 73.2 ms Moonshine tiny v2 22.8 ms Decode tokens per second, larger is better Whistle 1,319/s Whisper base 266/s Moonshine tiny v2 262/s Ten seconds of audio on an Apple M4 Pro CPU. Bars are scaled within each panel. 
 Each model ran on its official runtime at its defaults: Whistle's C++ engine at 5 beams, openai-whisper , and moonshine-voice non-streaming over whole audio. Time to first token is audio in to first token. Decode is tokens divided by the wall time after it, so the encoder is not counted twice. Whisper pads every input to 30 seconds, so its time to first token is flat across clip lengths. Whistle's tracks the clip: 5.9 ms at 5 seconds, 11.1 ms at 10, 36.3 ms at 30. 
 Word error rates are scored with the Whisper normalizers. Whistle's are measured over 86,174 utterances. Whisper's and Moonshine's are the figures their authors published, from the multilingual checkpoints rather than the English-only ones. No test audio appears in Whistle's training or validation data, verified by comparing audio checksums and speaker IDs across every reported test set. 
 One engine, three ways to load it 
 needle_load reads whichever model a .cact file holds, so the same binary does speech, text, or both: 
 needle --model whistle.cact --audio clip.wav 
 
 needle --model needle3.cact --tools tools.json --prompt "turn off the kitchen lights" 
 
 needle --model needle3.cact --model whistle.cact --tools tools.json --audio clip.wav 
 On the third line needle_complete takes the clip directly. The engine transcribes it, answers the transcript against your tools, and returns one JSON object with the calls and the speech fields, the speech ones prefixed audio_ . No transcript is handled by the caller. 
 { "function_calls" :[{ "name" : "set_lights" , "arguments" :{ "room" : "kitchen" , "on" : false }}], 
 "confidence" : 0.94 , 
 "audio_text" : "turn off the kitchen lights" , 
 "audio_language" : "en" } 
 Get started 
 pip install cactus-needle 
 import needle 
 
 print (needle.transcribe( "clip.wav" )[ "text" ]) 
 # turn off the kitchen lights 
 A 16 kHz WAV or raw samples need nothing beyond the base install. Other sample rates and microphone capture need the [mic] extra, which adds soxr and sounddevice . 
 Every call returns the text, the language, the milliseconds to the first token and the decoder's tokens per second after it. word_timestamps=True adds each word with its times and probability. keywords=["Siobhan", "Krzysztof"] raises the log probability of those phrases during the search. language="de" forces the language instead of detecting it. needle.Whistle() is the same model as an object, for embed(audio) or to hold one tuned .cact . 
 needle whistle playground transcribes from the microphone in the terminal, and needle whistle compare runs the same clip through Whistle, Whisper and Moonshine side by side with their timings. 
 Deploy 
 The engine ships prebuilt for seventeen targets, from macOS and Linux through Android, iOS, watchOS, Windows on ARM, RISC-V, MIPS, the browser and a WASI component. Every folder holds a needle binary, libneedle.a and needle.h , and loads any .cact you hand it. 
 needle download macos-arm64 
 needle download whistle 
 ./macos-arm64/needle --model whistle.cact --audio clip.wav --audio-word-timestamps 
 needle_load , needle_transcribe and needle_embed are the whole speech C API. The engine reads no environment variables. Every behaviour is a compiled default or an explicit flag. 
 Weights are on Hugging Face , the engine and its platform folders are in Cactus-Compute/needle3 , and the source is on GitHub . On this page The model Benchmarks One engine, three ways to load it Get started Deploy Cactus Terms Privacy © 2026 Cactus Compute. All rights reserved.
