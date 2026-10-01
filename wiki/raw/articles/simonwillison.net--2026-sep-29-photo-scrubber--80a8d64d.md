---
title: "local face blur & metadata removal"
url: "https://simonwillison.net/2026/Sep/29/photo-scrubber/"
fetched_at: 2026-10-01T10:00:42.373188+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# local face blur & metadata removal

Source: https://simonwillison.net/2026/Sep/29/photo-scrubber/

I took a photograph of some protesters, then thought about how I don't like sharing photographs of strangers with identifiable faces. I
had GPT-6 Astra build
this experimental tool that would identify faces and automatically blur them out.
It uses Google's
MediaPipe
C++ library, compiled to WebAssembly via
@mediapipe/tasks-vision
, plus the
BlazeFace
face detection model.
