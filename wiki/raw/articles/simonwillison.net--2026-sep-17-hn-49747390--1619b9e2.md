---
title: "Near-Lossless Compression in a 9x Smaller Footprint"
url: "https://simonwillison.net/2026/Sep/17/hn-49747390/"
fetched_at: 2026-09-26T10:00:58.333887+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Near-Lossless Compression in a 9x Smaller Footprint

Source: https://simonwillison.net/2026/Sep/17/hn-49747390/

If you want to try out out the GGUFs from
https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf#th...
be aware that you need Prism's llama.cpp fork to get them to work, from
https://github.com/PrismML-Eng/llama.cpp/releases/tag/prism-...
This should work:
cd /tmp

# Get the Prism macOS runtime
curl -fL https://github.com/PrismML-Eng/llama.cpp/releases/download/prism-b10685-7dffb15/llama-prism-b10685-7dffb15-bin-macos-arm64.tar.gz -o bonsai-runtime.tar.gz
tar -xzf bonsai-runtime.tar.gz

# Get the ~5.95 GB GGUF model:
curl -fL https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf/resolve/main/Ternary-Bonsai-2-27B-PTQ1_0.gguf -o Ternary-Bonsai-2-27B-PTQ1_0.gguf

# Run the server, I used port 8331
./llama-prism-b10685-7dffb15/llama-server \
  -m Ternary-Bonsai-2-27B-PTQ1_0.gguf \
  --port 8331 -ngl 99 -fa on -c 32768
Then open http://localhost:8331 for the (very good) baked in llama-server web UI... or run a prompt via the API like this:
uvx llm openai endpoint http://127.0.0.1:8331/v1 \
  --model bonsai-2-27b --responses hi
That's running at ~20 token/second for me on an M5 Pro (after a server restart I got 44 token/second, not sure why), but I'm pretty sure something isn't working right, on startup the server said "
ggml_metal_device_init: - the tensor API is not supported in this environment - disabling
".
